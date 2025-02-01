from matplotlib import pyplot as plt

def plot(plotSettings, *args, **kwargs):

    if plotSettings == "line": plt.plot(*args, **kwargs)
    if plotSettings == "scatter": plt.scatter(*args, **kwargs)

    # general functions
    plt.show()