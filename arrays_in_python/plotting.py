# Just a random plotting - demo plots


import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 34, 23, 56, 78]

plt.plot(x, y)
plt.title('Random plot')
plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.xticks(x)
plt.show()

