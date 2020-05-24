import matplotlib.pyplot as plt
import seaborn as sns


def labels(title=None, x=None, y=None, legend=False):
    if legend:
        plt.legend()
    if title:
        plt.title(title)
    if x:
        plt.xlabel(x)
    if y:
        plt.ylabel(y)


def theme():
    sns.set(style="ticks")
    x = 1
    sns.set(rc={'figure.figsize': (15 / x, 10 / x)}, font_scale = 2.5 / x)
