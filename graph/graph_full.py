import matplotlib.pyplot as plt

files = [
  ['data/data01.txt', 'Движение в (0, 1)'],
  ['data/data10.txt', 'Движение в (1, 0)'],
  ['data/data-10.txt', 'Движение в (-1, 0)'],
  ['data/data0-1.txt', 'Движение в (0, -1)'],
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

plt.title(r'Движение к заданной точке (эксперимент)')
plt.axis([-1, 1, -1, 1])
plt.xlabel(r'x, м')
plt.ylabel(r'y, м')

plt.grid(which='major', color = 'k')

plt.grid(which='minor', color='grey', linestyle=':')
plt.minorticks_on()

plt.legend(loc='lower left')

plt.show()