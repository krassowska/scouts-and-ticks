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


def mean_line(p, score_mean, color='#bf4045', width=1.5, label='Średnia', n=0):
    x, y = p.get_lines()[n].get_data()
    y_by_dist_from_mean = {}
    for xi, yi in zip(x, y):
        dist = abs(xi - score_mean)
        y_by_dist_from_mean[dist] = yi
    closest = min(y_by_dist_from_mean.keys())

    plt.vlines(
        score_mean, 0, y_by_dist_from_mean[closest],
        linewidth=width, colors=color, label=label
    )


def median_line(p, color='g', width=1.5, label='mediana', n=0):
    x, y = p.get_lines()[n].get_data()
    cdf = scipy.integrate.cumtrapz(y, x, initial=0)
    nearest_05 = np.abs(cdf-0.5).argmin()    
    x_median = x[nearest_05]
    y_median = y[nearest_05]

    plt.vlines(
        x_median, 0, y_median,
        linewidth=width, colors=color, label=label
    )


def czy_ma_zostac(desired_f_to_m_ratio, male_count):
    n_kobiet = 0
    def determine_if_shoud_stay(osoba):
        nonlocal n_kobiet
        if osoba.sex == 'Kobieta':
            if (n_kobiet + 1) / male_count <= desired_f_to_m_ratio:
                n_kobiet += 1
                return True
            else:
                return False
            # if true - stays, if false - delete
        else:
            return True
    return determine_if_shoud_stay