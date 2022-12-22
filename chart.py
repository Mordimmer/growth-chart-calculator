from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def create_charts(main):
    # draw simple plot in main window
    def draw_plot():
        # read data from file
        with open("data.txt", "r") as file:
            data = file.read()

        # split data by new line
        data = data.split("\n")

        # create list of lists
        data_list = []
        for i in data:
            data_list.append(i.split(","))

        # create lists for each
        age = []
        height = []
        weight = []
        head = []

        # fill lists with data
        for i in range(len(data_list)):
            age.append(int(data_list[i][1]))
            height.append(int(data_list[i][2]))
            weight.append(int(data_list[i][3]))
            head.append(int(data_list[i][4]))

        # create 3 plots
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

        # plot age and weight
        ax2.plot(age, weight, color="red")
        ax2.grid(linestyle="--")
        ax2.set_title("Waga")
        ax2.set_xlabel("Wiek [miesiące]")
        ax2.set_ylabel("Waga [kg]")

        # plot age and head circumference
        ax3.plot(age, head, color="green")
        ax3.grid(linestyle="--")
        ax3.set_title("Obwód głowy")
        ax3.set_xlabel("Wiek [miesiące]")
        ax3.set_ylabel("Obwód głowy [cm]")

        # improve layout
        plt.tight_layout()
        # increase plot height
        fig.set_figheight(8)
        # decrease plot width
        fig.set_figwidth(5)
        # decrease space between plots
        fig.subplots_adjust(hspace=0.5)

        # make fig background same color as main window
        fig.patch.set_facecolor('#FFCC99')

        # draw canvas on the right side of main window
        canvas = FigureCanvasTkAgg(fig, main)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=6, rowspan=20, padx=150, pady=15)


    draw_plot()
