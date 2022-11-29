import tkinter as tk

# TODO
# Zmenić tło przycisków
# Sprawdzić, czy dane są poprawne

main = tk.Tk()
main.title("Kalkulator centylowy")

# get screen width and height
width = main.winfo_screenwidth()
height = main.winfo_screenheight()

# full screen
# main.geometry(f"{width}x{height}")
# 1280x720 window
main.geometry("1280x720")

# set background color
main.configure(bg="#FFCC99")


# check if provided data is a double or integer
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def append_data():
    with open("data.txt", "a") as file:
        file.write(
            f"{selected_gender.get()}, {age_input.get()}, {height_input.get()}, {weight_input.get()}, {head_input.get()}\n")


def is_empty_or_not_number():
    if age_input.get() == "" or height_input.get() == "" or weight_input.get() == "" or head_input.get() == "" or not is_number(
            age_input.get()) or not is_number(height_input.get()) or not is_number(weight_input.get()) or not is_number(
        head_input.get()):
        return True
    else:
        return False


def button_click():
    error_label = tk.Label(main, text="Wprowadź poprawne dane!", fg="red")
    # if any of the inputs is empty or not a number then show error message
    if age_input.get() == "" or height_input.get() == "" or weight_input.get() == "" or head_input.get() == "" or not is_number(
            age_input.get()) or not is_number(height_input.get()) or not is_number(weight_input.get()) or not is_number(
        head_input.get()):
        error_label.grid(row=12, column=0, columnspan=2)
        # hide window after 3 seconds
        main.after(3000, error_label.destroy)
    else:
        input_button['state'] = 'disabled'
        # hide window after 3 seconds
        main.after(3000, error_label.destroy)
        success_label = tk.Label(main, text="Dane zostały zapisane!", fg="green")
        success_label.grid(row=12, column=0, columnspan=2)
        # hide windwo after 3 seconds
        main.after(3000, success_label.destroy)
        # append data to file
        append_data()




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

if __name__ == "__main__":
    main.mainloop()
