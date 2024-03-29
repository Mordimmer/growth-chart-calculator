import pandas as pd

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import db_connection
import global_variables


def create_charts(main, pesel: str):
    """
    Create charts and show them in main window

    :param pesel: pesel of the patient to read data for
    :param main: application window
    """

    def draw_plot():
        # load data from csv file, and crate lists for each column
        # data = pd.read_csv("data.csv")
        data = db_connection.read_patient_data(pesel)
        # sort all data by second column (age)
        data = data.sort_values(by=[data.columns[1]])
        gender = data.iloc[:, 0]
        age = data.iloc[:, 1]
        height = data.iloc[:, 2]
        weight = data.iloc[:, 3]
        head = data.iloc[:, 4]
        print(height)

        # converse age to int
        age = [int(i) for i in age]

        # if data.tail(1).iloc[0, 0] == "boy":
        if global_variables.selected_patient_gender == "boy":
            centyle_height = pd.read_csv("centyle/b_height.csv")
        else:
            centyle_height = pd.read_csv("centyle/g_height.csv")
        age_centyl = centyle_height.iloc[:, 0]
        height_2nd = centyle_height.iloc[:, 1]
        height_25th = centyle_height.iloc[:, 4]
        height_50th = centyle_height.iloc[:, 5]
        height_75th = centyle_height.iloc[:, 6]
        height_98th = centyle_height.iloc[:, 9]

        if global_variables.selected_patient_gender == "boy":
            centyle_weight = pd.read_csv("centyle/b_weight.csv")
        else:
            centyle_weight = pd.read_csv("centyle/g_weight.csv")

        age_centyl_weight = centyle_weight.iloc[:, 0]
        weight_2nd = centyle_weight.iloc[:, 1]
        weight_25th = centyle_weight.iloc[:, 4]
        weight_50th = centyle_weight.iloc[:, 5]
        weight_75th = centyle_weight.iloc[:, 6]
        weight_98th = centyle_weight.iloc[:, 9]

        if global_variables.selected_patient_gender == "boy":
            centyle_headc = pd.read_csv("centyle/b_headc.csv")
        else:
            centyle_headc = pd.read_csv("centyle/g_headc.csv")
        age_centyl_headc = centyle_headc.iloc[:, 0]
        headc_2nd = centyle_headc.iloc[:, 1]
        headc_5th = centyle_headc.iloc[:, 2]
        headc_10th = centyle_headc.iloc[:, 3]
        headc_25th = centyle_headc.iloc[:, 4]
        headc_50th = centyle_headc.iloc[:, 5]
        headc_75th = centyle_headc.iloc[:, 6]
        headc_90th = centyle_headc.iloc[:, 7]
        headc_95th = centyle_headc.iloc[:, 8]
        headc_98th = centyle_headc.iloc[:, 9]

        # create 3 plots
        # (3, 1, 1) means 3 rows, 1 column, 1st plot
        fig = plt.figure()
        ax1 = fig.add_subplot(311)
        ax2 = fig.add_subplot(312)
        ax3 = fig.add_subplot(313)

        ax1.plot(age, height, color="black", label="Wzrost")
        ax1.plot(age_centyl, height_2nd, 'r--', label="2nd")
        ax1.plot(age_centyl, height_25th, 'g--', label="25th")
        ax1.plot(age_centyl, height_50th, 'b-.', label="50th")
        ax1.plot(age_centyl, height_75th, 'g--', label="75th")
        ax1.plot(age_centyl, height_98th, 'r--', label="98th")
        ax1.grid(linestyle="--")
        ax1.set_xlim(left=0)
        if len(age) > 0:
            ax1.set_xlim(right=max(age))
        else:
            ax1.set_xlim(right=24)
        if len(height) > 0:
            ax1.set_ylim(bottom=min(height) - 0.1 * min(height))
            ax1.set_ylim(top=max(height) + 0.1 * max(height))
        else:
            ax1.set_ylim(bottom=40)
            ax1.set_ylim(top=100)

        ax1.set_title("Wzrost")
        ax1.set_xlabel("Wiek [miesiące]")
        ax1.set_ylabel("Wzrost [cm]")
        ax1.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        # show legend next to plot
        ax1.legend(loc="center left", bbox_to_anchor=(1, 0.5), prop={'size': 8})

        # plot age and weight
        ax2.plot(age, weight, color="black", label="Waga")
        ax2.plot(age_centyl_weight, weight_2nd, 'r--', label="2nd")
        ax2.plot(age_centyl_weight, weight_25th, 'g--', label="25th")
        ax2.plot(age_centyl_weight, weight_50th, 'b-.', label="50th")
        ax2.plot(age_centyl_weight, weight_75th, 'g--', label="75th")
        ax2.plot(age_centyl_weight, weight_98th, 'r--', label="98th")
        ax2.grid(linestyle="--")
        ax2.set_xlim(left=0)

        if len(age) > 0:
            ax2.set_xlim(right=max(age))
        else:
            ax2.set_xlim(right=24)
        # ax2.set_xlim(left=0)
        # ax2.set_xlim(right=max(age))

        if len(weight) > 0:
            ax2.set_ylim(bottom=min(weight) - 0.1 * min(weight))
            ax2.set_ylim(top=max(weight) + 0.1 * max(weight))
        else:
            ax2.set_ylim(bottom=0)
            ax2.set_ylim(top=17)
        # ax2.set_ylim(bottom=min(weight) - 0.1 * min(weight))
        # ax2.set_ylim(top=max(weight) + 0.1 * max(weight))

        ax2.set_title("Waga")
        ax2.set_xlabel("Wiek [miesiące]")
        ax2.set_ylabel("Waga [kg]")
        ax2.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        # show legend next to plot
        ax2.legend(loc="center left", bbox_to_anchor=(1, 0.5), prop={'size': 8})

        # plot age and head circumference
        ax3.plot(age, head, color="black", label="Obwód głowy")
        ax3.plot(age_centyl_headc, headc_2nd, 'r--', label="2nd")
        ax3.plot(age_centyl_headc, headc_25th, 'g--', label="25th")
        ax3.plot(age_centyl_headc, headc_50th, 'b-.', label="50th")
        ax3.plot(age_centyl_headc, headc_75th, 'g--', label="75th")
        ax3.plot(age_centyl_headc, headc_98th, 'r--', label="98th")
        ax3.grid(linestyle="--")
        ax3.set_xlim(left=0)
        if len(age) > 0:
            if 24 > max(age) > 0:
                ax3.set_xlim(right=max(age))
                ax3.set_xlabel("Wiek [miesiące]")
            else:
                ax3.set_xlim(right=24)
                # change x axis label
                ax3.set_xlabel("Wiek [miesiące]\n(nieliczony powyżej 2. roku życia)")
        else:
            ax3.set_xlim(right=24)
            ax3.set_xlabel("Wiek [miesiące]")

        ax3.set_title("Obwód głowy")
        ax3.set_ylabel("Obwód głowy [cm]")
        ax3.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        # show legend next to plot
        ax3.legend(loc="center left", bbox_to_anchor=(1, 0.5), prop={'size': 8})
        fig.set_size_inches(5, 6)

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
