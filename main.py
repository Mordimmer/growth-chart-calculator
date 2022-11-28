import tkinter as tk

main = tk.Tk()
main.title("Kalkulator centylowy")

# get screen width and height
width = main.winfo_screenwidth()
height = main.winfo_screenheight()

# full screen
# main.geometry(f"{width}x{height}")
main.geometry("1280x720")

# set background color
main.configure(bg="#000000")

# draw input fields
tk.Label(main, text="Wzrost [cm]:", bg="#000000", fg="#ffffff").grid(row=0, column=0)
height_input = tk.Entry(main)
height_input.grid(row=1, column=0)

tk.Label(main, text="Waga [kg]:", bg="#000000", fg="#ffffff").grid(row=2, column=0)
weight_input = tk.Entry(main)
weight_input.grid(row=3, column=0)

tk.Label(main, text="Wiek [miesiące]:", bg="#000000", fg="#ffffff").grid(row=4, column=0)
age_input = tk.Entry(main)
age_input.grid(row=5, column=0)


# append values from input fields to file, each value separated by comma
def append_data():
    with open("data.txt", "a") as file:
        file.write(f"\n{height_input.get()}\t{weight_input.get()}\t{age_input.get()}")


# button to append data to file
tk.Button(main, text="Dodaj dane", command=append_data).grid(row=6, column=0)


# get data from file, and save it to list, first line is height, second is weight, third is age
def get_data():
    with open("data.txt", "r") as file:
        data = file.readlines()
        data = [x.strip() for x in data]
        return data


print(get_data())

# draw button

main.mainloop()
