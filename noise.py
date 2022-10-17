"""https://qsm.quantumtinkerer.tudelft.nl/1_basics_of_noise/"""
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 1
ts = np.linspace(0, 100, 100)
vs = np.asarray([np.random.normal(mu, sigma) for t in ts])


def random_waveform():
    plt.plot(ts, vs)
    plt.title("Signal")
    plt.xlabel("Time (s)")
    plt.ylim(-3, 3)
    plt.ylabel("Voltage (mV)")
    plt.show()


def random_hist():
    count, bins, ignored = plt.hist(vs, 20, density=True)
    plt.plot(
        bins,
        1
        / (sigma * np.sqrt(2 * np.pi))
        * np.exp(-((bins - mu) ** 2) / (2 * sigma**2)),
        linewidth=2,
        color="r",
    )
    plt.title(
        "Histogram of measured voltages and fit to a Gaussian probability distribution"
    )
    plt.xlabel("Voltage [mV]")
    plt.ylabel("Probability of voltage value")
    plt.show()


def random_autocorrelation():  # ?? wrong
    ts = np.linspace(0, 3, 31)
    ys = np.exp(-ts)
    plt.plot(ts, ys)
    plt.title("Autocorrelation function")
    plt.ylabel("$R_{vv}$")
    plt.xlabel("Time difference between data points (ms)")
    plt.plot()
    plt.show()


if __name__ == "__main__":
    # random_hist()
    random_autocorrelation()
