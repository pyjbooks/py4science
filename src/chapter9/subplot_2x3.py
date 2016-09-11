import matplotlib.pyplot as plt

plt.figure(1), plt.clf()

plt.subplot(2, 3, 1), plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,3,1)', ha='center', va='center', size=25)
plt.subplot(2, 3, 2), plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,3,2)', ha='center', va='center', size=25)
plt.subplot(2, 3, 3), plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,3,3)', ha='center', va='center', size=25)
plt.subplot(2, 3, 4), plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,3,4)', ha='center', va='center', size=25)
plt.subplot(2, 3, 5), plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,3,5)', ha='center', va='center', size=25)
plt.subplot(2, 3, 6), plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'subplot(2,3,6)', ha='center', va='center', size=25)

# プロット全体の表示
plt.show()
