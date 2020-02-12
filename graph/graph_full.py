import matplotlib.pyplot as plt

files = [
  ['data/model1.txt', 'Траектория (модель)']
  #['data/data-10.txt', 'Движение в (-1, 0)'],
  #['data/data0-1.txt', 'Движение в (0, -1)'],
]

data = []
square_length = 0.5 # m

for file in files:
  time = []
  x = []
  y = []
  angle = []

  with open(file[0], 'r') as f:
    for line in f:
      line = line.split(' ')
      if len(line) == 2:
        x.append(float(line[0]))
        y.append(float(line[1]))
      elif len(line) == 4:
        time.append(float(line[0]))
        x.append(float(line[1]))
        y.append(float(line[2]))
        angle.append(float(line[3]))

  data.append([time, x, y, angle, file[1]])

for graph in data:
  plt.plot(graph[1], graph[2], label=graph[4])

for dot in [[square_length, 0], [square_length, square_length], [0, square_length], [0, 0]]:
  plt.scatter(dot[0], dot[1], marker='.', s=250, color="orange")

plt.title(r'Движения робота')
plt.axis([-1, 1, -1, 1])
plt.xlabel(r'x, м')
plt.ylabel(r'y, м')

plt.grid(which='major', color = 'k')

plt.grid(which='minor', color='grey', linestyle=':')
plt.minorticks_on()

plt.legend(loc='lower left')

plt.show()