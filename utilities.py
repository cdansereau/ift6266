import numpy as np
import matplotlib.pyplot as plt
import cPickle

# from code of Alexandre : https://github.com/adbrebs/dogs_vs_cats/blob/master/results/utilities.py
def plot_statistics(statistics, legends, title="", ylabel="", xlim=None, ylim=None, writeto="default.jpeg"):
    plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel("Number of epochs")
    plt.ylabel(ylabel)
    plt.title(title)

    for stat in statistics:
        plt.plot(stat, linestyle="solid", marker=".")
    plt.grid()
    plt.legend(legends, loc='upper right')

    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)

    plt.savefig("./results/" + writeto)


def analyse_pylearn2_channels(path, xlim=None, ylim_nll=None, ylim_err=None):
    channels = cPickle.load(open(path, "rb" ))

    train_misclass = channels['train_y_misclass'].val_record
    val_misclass = channels['valid_y_misclass'].val_record
    train_nll = channels['train_y_nll'].val_record
    val_nll = channels['valid_y_nll'].val_record
    legends = ['training', 'validation']

    plot_statistics([train_misclass, val_misclass], legends,
                    ylabel="Error rate", xlim=xlim, ylim=ylim_err, writeto="error_rate_pylearn2.jpeg")
    plot_statistics([train_nll, val_nll], legends,
                    ylabel="Negative Log Likelihood", xlim=xlim, ylim=ylim_nll, writeto="nll_pylearn2.jpeg")




if __name__ == '__main__':

    analyse_pylearn2_channels("./_6.pkl", xlim=xlim, ylim_nll=ylim_nll, ylim_err=ylim_err)
