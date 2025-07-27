import matplotlib.pyplot as plt

x1 = [16, 64, 256, 1024, 4096]
y1 = [0.1264, 0.2642, 0.3629, 0.4002, 0.4108]

y2 = [0.4083, 0.4140, 0.4144, 0.4144, 0.4144]

y = [0.1264, 0.2642, 0.3629, 0.4002, 0.4108, 0.4083, 0.4140, 0.4144]

plt.plot(x1, y1, 'o')
plt.plot(x1, y1, '-', label='Q4')  # '-' for straight lines
plt.plot(x1, y2, 'o')
plt.plot(x1, y2, '-', label='Q8')

plt.xticks(x1, rotation=90)  # Rotate labels to be vertical
plt.yticks([y1[0], y1[1], y1[2], y1[3], y2[0], y2[2]])

plt.xlabel("number of elements")
plt.ylabel("Wmax-nondimentional")
plt.grid(True, which='both', linestyle='--', linewidth=0.005)
plt.legend()

# Show the plot
plt.show()