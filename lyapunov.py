import math
import matplotlib.pyplot as plt

files = [
  #['model_data/LyapunovLin0_0.5.txt', 'Движение в (0, 500), лин.', (0, 0.5)],
  #['model_data/LyapunovLin0.5_0.txt', 'Движение в (500, 0), лин.', (0.5, 0)],
  #['model_data/LyapunovLin0_-0.5.txt', 'Движение в (0, -500), лин.', (0, -0.5)],
  ['model_data/LyapunovLin-0.5_0.txt', 'Движение в (-500, 0), лин.', (-0.5, 0)],

  #['model_data/LyapunovNelin0_500.txt', 'Движение в (0, 500), нелин.', (0, 0.5)],
  #['model_data/LyapunovNelin500_0.txt', 'Движение в (500, 0), нелин.', (0.5, 0)],
  #['model_data/LyapunovNelin0_-500.txt', 'Движение в (0, -500), нелин.', (0, -0.5)],
  ['model_data/LyapunovNelin-500_0.txt', 'Движение в (-500, 0), нелин.', (-0.5, 0)],
]

data = []

for f in files:
  graph = []
  point = [i*1000 for i in f[2]]
  with open(f[0], 'r') as fs:
    for line in fs:
      line = line.split(' ')
      #data.append([float(line[3]), float(line[0]), float(line[1]), float(line[2])]) # [time, x, y, angle]
      graph.append([float(line[0]), float(line[1])]) # [time, value]
  data.append([graph, f[1]])
  '''
  v = []
  #x_prev, y_prev = 0, 0
  for cur_data in data:
    pho = math.sqrt((point[0] - cur_data[1])**2 + (point[1] - cur_data[2])**2)
    theta = math.atan2(point[1] - cur_data[2], point[0] - cur_data[1])
    angle = theta - cur_data[3]

    v.append((pho**2 + angle**2)/2)
    #v.append(pho)
    #v.append(angle)
  '''

for graph in data:
  plt.plot([d[0] for d in graph[0]], [d[1] for d in graph[0]], label=graph[1])

plt.title(r'График V(t)')
plt.axis([0, 15, 0, 130*10**3])
plt.xlabel(r't, c')
plt.ylabel(r'V(t)')

plt.grid(which='major', color = 'k')

plt.grid(which='minor', color='grey', linestyle=':')
plt.minorticks_on()

plt.legend(loc='upper right')

plt.show()

