import matplotlib.pyplot as plt

# setting
n = 5
x = list(range(1, n))
y = [i*(i-1)**(i-1) for i in range(1, n)]
print(x)
print(y)
plt.plot(x, y)
plt.scatter(x, y, s=5)
plt.show()
