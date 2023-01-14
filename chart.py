import pandas as pd

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import global_variables


def create_charts(main):
    """
    Create charts and show them in main window

    :param main:
    :return:
    """
    def draw_plot():

        # load data from csv file, and crate lists for each column
        data = pd.read_csv("data.csv")
        gender = data.iloc[:, 0]
        age = data.iloc[:, 1]
        height = data.iloc[:, 2]
        weight = data.iloc[:, 3]
        head = data.iloc[:, 4]

        # converse age to int
        age = [int(i) for i in age]

        # create 3 plots
        # (3, 1, 1) means 3 rows, 1 column, 1st plot
        fig = plt.figure()
        ax1 = fig.add_subplot(311)
        ax2 = fig.add_subplot(312)
        ax3 = fig.add_subplot(313)

        # plot age and height
        ax1.plot(age, height, color="blue")
        ax1.grid(linestyle="--")
        ax1.set_title("Wzrost")
        ax1.set_xlabel("Wiek [miesiące]")
        ax1.set_ylabel("Wzrost [cm]")
        ax1.set_ylim(bottom=0)
        ax1.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        ax1.set_ylim(top=ax1.get_ylim()[1] * 1.2)

        # plot age and weight
        ax2.plot(age, weight, color="red")
        ax2.grid(linestyle="--")
        ax2.set_title("Waga")
        ax2.set_xlabel("Wiek [miesiące]")
        ax2.set_ylabel("Waga [kg]")
        ax2.set_ylim(bottom=0)
        ax2.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        ax2.set_ylim(top=ax2.get_ylim()[1] * 1.2)

        # plot age and head circumference
        ax3.plot(age, head, color="green")
        ax3.grid(linestyle="--")
        ax3.set_title("Obwód głowy")
        ax3.set_xlabel("Wiek [miesiące]")
        ax3.set_ylabel("Obwód głowy [cm]")
        ax3.set_ylim(bottom=0)
        ax3.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        ax3.set_ylim(top=ax3.get_ylim()[1] * 1.2)

        # improve layout
        plt.tight_layout()
        # increase plot height
        fig.set_figheight(8)
        # decrease plot width
        fig.set_figwidth(5)
        # decrease space between plots
        fig.subplots_adjust(hspace=0.5)

        # change background color to the same as main window
        fig.patch.set_facecolor(global_variables.background_color)

        # draw widget
        canvas = FigureCanvasTkAgg(fig, main)
        canvas.draw()

        # move plot to the right
        canvas.get_tk_widget().grid(row=0, column=6, rowspan=20, padx=150, pady=15)  # possible improvement

    draw_plot()
