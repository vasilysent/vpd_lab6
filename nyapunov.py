import math
import matplotlib.pyplot as plt

files = [
  #['data/linear_exp_0_0.5.txt', 'Движение в (0, 0.5), лин.', (0, 0.5)],
  #['data/linear_exp_0.5_0.txt', 'Движение в (0.5, 0), лин.', (0.5, 0)],
  #['data/linear_exp_0_-0.5.txt', 'Движение в (0, -0.5), лин.', (0, -0.5)],
  ['data/linear_exp_-0.5_0.txt', 'Движение в (-0.5, 0), лин.', (-0.5, 0)],
  ['data/nonlinear_exp_0_0.5.txt', 'Движение в (0, 0.5), нелин.', (0, 0.5)],
  ['data/nonlinear_exp_0.5_0.txt', 'Движение в (0.5, 0), нелин.', (0.5, 0)],
  ['data/nonlinear_exp_0_-0.5.txt', 'Движение в (0, -0.5), нелин.', (0, -0.5)],
  ['data/nonlinear_exp_-0.5_0.txt', 'Движение в (-0.5, 0), нелин.', (-0.5, 0)],
]

for f in files:
  data = []
  point = [i*1000 for i in f[2]]
  with open(f[0], 'r') as fs:
    for line in fs:
      line = line.split(' ')
      data.append([float(line[3]), float(line[0]), float(line[1]), float(line[2])]) # [time, x, y, angle]

  v = []
  #x_prev, y_prev = 0, 0
  for cur_data in data:
    pho = math.sqrt((point[0] - cur_data[1])**2 + (point[1] - cur_data[2])**2)
    theta = math.atan2(point[1] - cur_data[2], point[0] - cur_data[1])
    angle = theta - cur_data[3]

    v.append((pho**2 + angle**2)/2)
    #v.append(pho)
    #v.append(angle)


  plt.plot([dat[0] for dat in data], v, label=f[1])

  plt.title(r'График V(t)')
  #plt.axis([-1, 1, -1, 1])
  plt.xlabel(r't, c')
  plt.ylabel(r'V(t)')

  plt.grid(which='major', color = 'k')

  plt.grid(which='minor', color='grey', linestyle=':')
  plt.minorticks_on()

  plt.legend(loc='upper right')

  plt.show()

