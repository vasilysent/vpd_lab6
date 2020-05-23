import matplotlib.pyplot as plt

files = [
  #['data/linear_exp.txt', 'Траектория (эксп.), линейное управление', 1],
  #['data/hyperbolic_dich.txt', 'Траектория (эксп.), нелинейное управление', 1],
  #['data/nonlinear_exp.txt', 'Траектория (эксп.), нелинейное управление', 1],
  
  #['data/linear_exp_0_0.5.txt', 'Движение в (0, 500), лин. (эксп.)', 1],
  #['data/linear_exp_0.5_0.txt', 'Движение в (500, 0), лин. (эксп.)', 1],
  #['data/linear_exp_0_-0.5.txt', 'Движение в (0, -500), лин. (эксп.)', 1],
  #['data/linear_exp_-0.5_0.txt', 'Движение в (-500, 0), лин. (эксп.)', 1],
  #['data/nonlinear_exp_0_0.5.txt', 'Движение в (0, 500), нелин. (эксп.)', 1],
  #['data/nonlinear_exp_0.5_0.txt', 'Движение в (500, 0), нелин. (эксп.)', 1],
  #['data/nonlinear_exp_0_-0.5.txt', 'Движение в (0, -500), нелин. (эксп.)', 1],
  #['data/nonlinear_exp_-0.5_0.txt', 'Движение в (-500, 0), нелин. (эксп.)', 1],
  
  #['model_data/lin0_0.5.txt', 'Движение в (0, 500), лин. (модель)', 1000],
  #['model_data/lin0.5_0.txt', 'Движение в (500, 0), лин. (модель)', 1000],
  #['model_data/lin0_-0.5.txt', 'Движение в (0, -500), лин. (модель)', 1000],
  #['model_data/lin-0.5_0.txt', 'Движение в (-500, 0), лин. (модель)', 1000],
  #['model_data/nonlin0_500.txt', 'Движение в (0, 500), нелин. (модель)', 1],
  #['model_data/nonlin500_0.txt', 'Движение в (500, 0), нелин. (модель)', 1],
  #['model_data/nonlin0_-500.txt', 'Движение в (0, -500), нелин. (модель)', 1],
  #['model_data/nonlin-500_0.txt', 'Движение в (-500, 0), нелин. (модель)', 1],

  
  ['data/linear_exp.txt', 'Движение по квадрату, лин. (эксп.)', 1],
  ['data/nonlinear_exp.txt', 'Движение по квадрату, нелин. (эксп.)', 1],
  
  #['model_data/Lin.txt', 'Движение по квадрату, лин. (модель)', 1000],
  #['model_data/Nonlin.txt', 'Движение по квадрату, нелин. (модель)', 1],
]

factor = 1000
data = []
square_length = 500 # mm
points = [[square_length, 0], [square_length, square_length], [0, square_length], [0, 0]]
p_idx = 2
#points = [[square_length, 0], [0, square_length], [-square_length, 0], [0, -square_length]][p_idx:p_idx+1]

for file in files:
  time = []
  x = []
  y = []
  angle = []

  with open(file[0], 'r') as f:
    for line in f:
      line = line.split(' ')
      x.append(float(line[0]) * file[2]) # mm -> m
      y.append(float(line[1]) * file[2]) # mm -> m

  data.append([time, x, y, angle, file[1]])

for graph in data:
  plt.plot(graph[1], graph[2], label=graph[4])

for dot in points:
  plt.scatter(dot[0], dot[1], marker='.', s=250, color="orange")

plt.title(r'Траектории движения робота')
#plt.axis([-640, 640, -640, 640])
plt.axis([-140, 640, -140, 640])
plt.xlabel(r'x, мм')
plt.ylabel(r'y, мм')

plt.grid(which='major', color = 'k')

plt.grid(which='minor', color='grey', linestyle=':')
plt.minorticks_on()

plt.legend(loc="lower left")
#plt.legend(loc="upper left")

plt.show()