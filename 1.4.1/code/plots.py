import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([3.10906096, 3.40119738, 3.68887945, 3.91202301, 4.09434456])
y1 = np.array([-3.19008566, -3.165016912, -3.11356565, -3.05760768, -3.03655427])
A1 = np.vstack([x1, np.ones(len(x1))]).T
m1, c1 = np.linalg.lstsq(A1, y1)[0]
print(m1, c1)
plt.errorbar(x1, y1, xerr=0, yerr=0.04, color='k', linestyle='None', elinewidth=0.5)

plt.plot(x1, m1 * x1 + c1, 'b')
plt.plot(x1, y1, '^', color='k', markersize=3)

# x2 = np.array([0.032135,	0.07283,	0.13085,	0.2073,	0.3303615])
# y2 = np.array([12.854,	12.9476,	13.084,	13.2672,	13.6827])
# A2 = np.vstack([x2, np.ones(len(x2))]).T
# m2, c2 = np.linalg.lstsq(A2, y2)[0]
# print(m2, c2)
# plt.errorbar(x2, y2, xerr=0, yerr=0, color='k', linestyle='None', elinewidth=0.5)
#
# plt.plot(x2, m2 * x2 + c2, 'r')
# plt.plot(x2, y2, 'o', color='k', markersize=3, label=r'$t_2$')
#
# x3 = np.array([0.03304,	0.07489,	0.13457,	0.213175,	0.31227])
# y3 = np.array([13.2162,	13.3153,	13.457,	13.6432,	13.8787])
# A3 = np.vstack([x3, np.ones(len(x3))]).T
# m3, c3 = np.linalg.lstsq(A3, y3)[0]
# print(m3, c3)
# plt.errorbar(x3, y3, xerr=0, yerr=0, color='k', linestyle='None', elinewidth=0.5)
#
# plt.plot(x3, m3 * x3 + c3, 'g')
# plt.plot(x3, y3, 's', color='k', markersize=3, label=r'$t_3$')
#
# x4 = np.array([0.034,	0.0770,	0.1383,	0.21894,	0.32052])
# y4 = np.array([13.6,	13.6947,	13.83,	14.012,	14.2453])
# A4 = np.vstack([x4, np.ones(len(x4))]).T
# m4, c4 = np.linalg.lstsq(A4, y4)[0]
# print(m4, c4)
# plt.errorbar(x4, y4, xerr=0, yerr=0, color='k', linestyle='None', elinewidth=0.5)
#
# plt.plot(x4, m4 * x4 + c4, 'pink')
# plt.plot(x4, y4, '*', color='k', markersize=3, label=r'$t_4$')
#
# x5 = np.array([0.03488,	0.079065,	0.14198,	0.22479,	0.32885])
# y5 = np.array([13.9514,	14.056,	14.1979,	14.3864,	14.615])
# A5 = np.vstack([x5, np.ones(len(x5))]).T
# m5, c5 = np.linalg.lstsq(A5, y5)[0]
# print(m5, c5)
# plt.errorbar(x5, y5, xerr=0, yerr=0, color='k', linestyle='None', elinewidth=0.5)
#
# plt.plot(x5, m5 * x5 + c5, 'y')
# plt.plot(x5, y5, 'x', color='k', markersize=3, label=r'$t_5$')


#plt.title('Рисунок 3 ' + r'$\kappa (t).$', font='Times New Roman', fontsize=15)
plt.minorticks_on()
plt.grid(which='major', color='k', linewidth=0.5)
plt.grid(which='minor', color='k', linestyle=':', linewidth=0.2)

plt.xlabel(r'$t, ^\circ C$' + ' ', font='Times New Roman', fontsize=15)
plt.ylabel(r'$\kappa$' + ' ', font='Times New Roman', fontsize=15)
plt.legend()
plt.show()

print((1 / (len(x1) - 1) * (np.var(y1) / np.var(x1) - m1 ** 2)) ** (1 / 2))
# print((1 / (len(x2) - 1) * (np.var(y2) / np.var(x2) - m2 ** 2)) ** (1 / 2))
# print((1 / (len(x3) - 1) * (np.var(y3) / np.var(x3) - m3 ** 2)) ** (1 / 2))
# print((1 / (len(x4) - 1) * (np.var(y4) / np.var(x4) - m4 ** 2)) ** (1 / 2))
# print((1 / (len(x5) - 1) * (np.var(y5) / np.var(x5) - m5 ** 2)) ** (1 / 2))

k = 0
for i in range(0, len(x1)):
    k += x1[i] ** 2
k = k / len(x1)
print(((1 / (len(x1) - 1) * (np.var(y1) / np.var(x1) - m1 ** 2)) ** (1 / 2)) * (k ** 0.5))