#!/usr/bin/env cdpython3
from ev3dev.ev3 import *
import time
import math

#----------------------------------------- robot's parameters
R = 41 # radius of the wheels [mm]
L = 162 # distance between wheels [mm]
v_min = 20 * 2 * R
v_max = 90 * 2 * R
#-----------------------------------------

#----------------------------------------- aim position
x_des = 35
y_des = 5
eps = 55
# trajectory = [[300, -200]]
trajectory = [[300, 0], [300, 300], [0, 300], [0, 0]]
#-----------------------------------------

#----------------------------------------- 
kp_ang = 35             # proportional gain for angular speed
kp_v = 4                # proportional gain for linear speed
#-----------------------------------------

mB = LargeMotor('outB')
mC = LargeMotor('outC')

mB.position = 0
mC.position = 0
current_time = 0
way = eps + 1

x_cur = y_cur = 0
phi_cur = 0
r_enc = l_enc = 0
prev_l_pos = prev_r_pos = 0
start_time = time.time()
data = open ('lab5_kp_ang' + str(kp_ang) + '_kp_v_' + str(kp_v) + '_x_' + str(trajectory[0][0]) + '_y_' + str(trajectory[0][1])  + '.txt', 'w')
data.write ('0 0' + '\n')


for i in range(len(trajectory)):
    way = eps + 1
    phi_des = math.atan2( (trajectory[i][1] - y_cur) , (trajectory[i][0] - x_cur) )

    while way >= eps:

        way = math.sqrt( (trajectory[i][0] - x_cur)**2 + (trajectory[i][1] - y_cur)**2 ) # distance error

        r_enc = mC.position - prev_r_pos             # new delta encs right
        l_enc = mB.position - prev_l_pos             # new delta encs left
        prev_l_pos = mB.position
        prev_r_pos = mC.position

        l_dist = l_enc * 2 * math.pi * R / 360  # delta distance left
        r_dist = r_enc * 2 * math.pi * R / 360  # delta distance right
        dist = (l_dist + r_dist) / 2            # delta distance center
        x_cur += dist * math.cos(phi_cur)       # new x position
        y_cur += dist * math.sin(phi_cur)       # new y position

        if ( ( phi_cur + math.atan2((r_dist - l_dist) , L) ) > math.pi):  # new current phi angle
            phi_cur += math.atan2((r_dist - l_dist) , L) - 2 * math.pi    
        elif ( ( phi_cur + math.atan2((r_dist - l_dist) , L) ) < -math.pi):
            phi_cur += math.atan2((r_dist - l_dist) , L) + 2 * math.pi
        else:
            phi_cur += math.atan2((r_dist - l_dist) , L)

        print ('phi_current ' + str(phi_cur))
        angle_error = math.atan2( math.sin(phi_des - phi_cur) , math.cos(phi_des - phi_cur) )  # new angle error
        w = kp_ang * angle_error 
      
        u_v = kp_v * way
        if (kp_v * way < v_min):
            u_v = v_min
        if (kp_v * way > v_max):
            u_v = v_max
        if way < eps:
            u_v = 0

        # v_r = u_v + w
        # v_l = u_v - w
        v_r = (2 * u_v + w * L) / (2 * R)
        v_l = (2 * u_v - w * L) / (2 * R)

        print ('v left = ' + str(v_l) + ' v right = ' +  str(v_r) + ' angle error =  ' + str(angle_error) + ' r_dist = ' +  str(r_dist) + ' l_dist = ' +  str(l_dist) + ' way = ' +  str(way) )

        if v_r > 100:
            v_r = 100
        if v_r < -100:
            v_r = -100
        if v_l > 100:
            v_l = 100
        if v_l < -100:
            v_l = -100

        mB.run_direct(duty_cycle_sp = v_l)
        mC.run_direct(duty_cycle_sp = v_r)

        current_time = time.time() - start_time
        data.write(str(x_cur) + ' ' + str(y_cur) + ' ' + ' ' + str(phi_cur) + str(current_time) + '\n')


mB.stop(stop_action = 'brake')
mC.stop(stop_action = 'brake')

mB = LargeMotor('outB')
mC = LargeMotor('outC')
data.close()
time.sleep(0.1)

        

        