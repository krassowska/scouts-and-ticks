import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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


def show_corelations(dane, only=None, exclude=None):
    if only:
        dane = dane[only]
    if exclude:
        dane = dane.drop(exclude, axis='columns')

    corr = dane.corr()
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(10, 10))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    return sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
