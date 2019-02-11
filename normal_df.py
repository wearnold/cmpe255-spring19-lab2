import math
from matplotlib import pyplot as plt

def normal_pdf(x, mu=0, sigma=1):

    variance = sigma ** 2
    first_portion = 1/(math.sqrt(2 * math.pi * variance))
    exp_portion = math.exp(-((x-mu) ** 2)/(2 * variance))
    return first_portion * exp_portion

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()