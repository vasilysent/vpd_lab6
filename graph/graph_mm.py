import matplotlib.pyplot as plt

files = [
  ['data/m1.txt', 'Траектория (модель)']
  #['data/data10.txt', 'Движение в (1, 0)'],
  #['data/data-10.txt', 'Движение в (-1, 0)'],
  #['data/data0-1.txt', 'Движение в (0, -1)'],
]

data = []

for file in files:
  time = []
  x = []
  y = []
  angle = []

  with open(file[0], 'r') as f:
    for line in f:
      line = line.split(' ')
      x.append(float(line[0]) / 1000) # mm -> m
      y.append(float(line[1]) / 1000) # mm -> m

  data.append([time, x, y, angle, file[1]])

for graph in data:
  plt.plot(graph[1], graph[2], label=graph[4])

for dot in [[0.35, 0], [0.35, 0.35], [0, 0.35], [0, 0]]:
  plt.scatter(dot[0], dot[1], marker='.', s=250, color="orange")

plt.title(r'Движения робота')
plt.axis([-0.25, 0.75, -0.25, 0.75])
plt.xlabel(r'x, м')
plt.ylabel(r'y, м')

plt.grid(which='major', color = 'k')

plt.grid(which='minor', color='grey', linestyle=':')
plt.minorticks_on()

plt.legend(loc='lower left')

plt.show()