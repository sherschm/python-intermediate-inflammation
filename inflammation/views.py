"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
#import numpy as np


def visualize(data_dict):
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()

    plt.show()


def analyse_data(data_source):
   """Calculate the standard deviation by day between datasets
   Gets all the inflammation csvs within a directory, works out the mean
   inflammation value for each day across all datasets, then graphs the
   standard deviation of these means."""
   
   data = data_source.load_inflammation_data()
   #data = load_inflammation_data(data_dir)
   daily_standard_deviation = compute_standard_deviation_by_day(data)

   graph_data = {
       'standard deviation by day': daily_standard_deviation,
   }
   visualize(graph_data)
   return daily_standard_deviation
