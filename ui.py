import tkinter as tk

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# create main window
main = tk.Tk()
main.title("Kalkulator centylowy")

# get screen width and height
width = main.winfo_screenwidth()
height = main.winfo_screenheight()

# setting up window size
# main.geometry(f"{width}x{height}") # set window size to screen size
main.geometry("1200x800")  # set window size to 1200x800

# setting background color
main.configure(bg="#FFCC99")


# check if provided data is a double or integer
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# append data to data.txt file
def append_data():
    with open("data.txt", "a") as file:
        file.write(
            f"\n{selected_gender.get()}, {age_input.get()}, {height_input.get()}, {weight_input.get()}, {head_input.get()}")


# check if inputs are empty or not a number
def is_empty_or_not_number():
    if age_input.get() == "" or height_input.get() == "" or weight_input.get() == "" or head_input.get() == "" or not is_number(
            age_input.get()) or not is_number(height_input.get()) or not is_number(weight_input.get()) or not is_number(
                head_input.get()):
        return True
    else:
        return False


# behavior of button
def button_click():
    error_label = tk.Label(main, text="Wprowadź poprawne dane!", fg="red")
    # if any of the inputs is empty or not a number than show error message
    if height_input.get() == "" or weight_input.get() == "" or head_input.get() == "" or not is_number(
            height_input.get()) or not is_number(weight_input.get()) or not is_number(
            head_input.get()):
        error_label.grid(row=12, column=0, columnspan=2)
        # hide window after 3 seconds
        main.after(3000, error_label.destroy)
    else:
        # if age is empty then increase previous age from data.txt file by 1
        if age_input.get() == "":
            with open("data.txt", "r") as file:
                data = file.read()
            data = data.split("\n")
            data_list = []
            for i in data:
                data_list.append(i.split(","))
            age_input.insert(0, int(data_list[-1][1]) + 1)
        # disable button after click
        input_button['state'] = 'disabled'
        # hide window after 3 seconds
        main.after(3000, error_label.destroy)
        success_label = tk.Label(main, text="Dane zostały zapisane!", fg="green")
        success_label.grid(row=12, column=0, columnspan=2)
        # hide window after 3 seconds
        main.after(3000, success_label.destroy)
        # append data to file
        append_data()
        draw_plot()


# button that re-enable input button
def change_button_state():
    input_button['state'] = 'normal'


# button using change_button_state function
change_button_state_button = tk.Button(main, text="Wprowadź kolejne dane", command=change_button_state)
change_button_state_button.grid(row=12, column=0, columnspan=2, pady=10)

# drawing elements inside main window
selected_gender = tk.StringVar()
gender = (("Dziewczynka", "girl"),
          ("Chłopiec", "boy"))

tk.Label(main, text="Kalkulator centylowy", bg="#FFCC99", font=("Arial", 30)).grid(row=0, column=0, columnspan=2,
                                                                                   padx=10, pady=10)

tk.Label(main, text="Płeć dziecka:", bg="#FFCC99").grid(row=1, column=0, padx=10, pady=10, columnspan=2)
tk.Radiobutton(main,
               text="Dziewczynka",
               value="girl",
               variable=selected_gender,
               bg="#FFCC99",
               highlightbackground="#FFCC99",
               activebackground="#e6ac73").grid(row=2,
                                                column=0,
                                                padx=10,
                                                pady=10)
tk.Radiobutton(main,
               text="Chłopczyk",
               value="boy",
               highlightbackground="#FFCC99",
               activebackground="#e6ac73",
               variable=selected_gender,
               bg="#FFCC99").grid(row=2,
                                  column=1,
                                  padx=10,
                                  pady=10)

tk.Label(main, text="Wiek [miesiące]:", bg="#FFCC99").grid(row=3, column=0, padx=10, pady=10, columnspan=2)
age_input = tk.Entry(main)
age_input.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

tk.Label(main, text="Wzrost [cm]:", bg="#FFCC99").grid(row=5, column=0, padx=10, pady=10, columnspan=2)
height_input = tk.Entry(main)
height_input.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

tk.Label(main, text="Waga [kg]:", bg="#FFCC99").grid(row=7, column=0, padx=10, pady=10, columnspan=2)
weight_input = tk.Entry(main)
weight_input.grid(row=8, column=0, padx=10, pady=10, columnspan=2)

tk.Label(main, text="Obwód głowy [cm]:", bg="#FFCC99").grid(row=9, column=0, padx=10, pady=10, columnspan=2)
head_input = tk.Entry(main)
head_input.grid(row=10, column=0, padx=10, pady=10, columnspan=2)

input_button = tk.Button(main, text="Zapisz dane", command=button_click)
input_button.grid(row=11, column=0, padx=10, pady=10, columnspan=2)


# display all data from data.txt file in columns with headers first colum is gender, second is age, third is height,
# fourth is weight, fifth is head circumference, data are separated by comma
def display_data():
    # read data from file
    with open("data.txt", "r") as file:
        data = file.read()

    # split data by new line
    data = data.split("\n")

    # create list of lists
    data_list = []
    for i in data:
        data_list.append(i.split(","))

    # create headers
    headers = ["Płeć", "Wiek", "Wzrost", "Waga", "Obwód głowy"]

    # create table
    for i in range(len(headers)):
        tk.Label(main, text=headers[i], bg="#FFCC99", font=("Arial", 15)).grid(row=0, column=i + 3, padx=10, pady=10)

    # fill table with data
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            tk.Label(main, text=data_list[i][j], bg="#FFCC99", font=("Arial", 15)).grid(row=i + 1, column=j + 3,
                                                                                        padx=10,
                                                                                        pady=10)


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
    canvas.get_tk_widget().grid(row=0, column=6, rowspan=20, padx=300, pady=15)


draw_plot()

# button to end program
end_button = tk.Button(main, text="Zakończ", command=main.destroy)
end_button.grid(row=13, column=0, padx=10, pady=10, columnspan=2)
