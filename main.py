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
main.geometry("1280x720")

# set background color
main.configure(bg="#FFCC99")


def append_data():
    with open("test.txt", "a") as file:
        file.write(f"\n{age_input.get()},{selected_sex.get()}")


selected_sex = tk.StringVar()
sex = (("Dziewczynka", "girl"),
       ("Chłopiec", "boy"))

tk.Label(main, text="Kalkulator centylowy", bg="#FFCC99",font=("Arial", 30)).place(x=50, y=20)



tk.Label(main, text="Wiek [miesiące]:", bg="#FFCC99").place(x=50, y=100)
age_input = tk.Entry(main)
age_input.place(x=200, y=100)


tk.Label(main, text="Płeć dziecka:", bg="#FFCC99").place(x=50, y=150)

tk.Radiobutton( main, text="Dziewczynka", value="girl", variable=selected_sex ).place(x=200, y=150)
tk.Radiobutton( main, text="Chłopczyk", value="boy", variable=selected_sex ).place(x=320, y=150)

tk.Label(main, text="Wzrost [cm]:", bg="#FFCC99").place(x=50, y=200)
height_input = tk.Entry(main)
height_input.place(x=200, y=200)

tk.Label(main, text="Waga [kg]:", bg="#FFCC99").place(x=50, y=250)
weight_input = tk.Entry(main)
weight_input.place(x=200, y=250)

tk.Label(main, text="Obwód głowy [cm]:", bg="#FFCC99").place(x=50, y=300)
head_input = tk.Entry(main)
head_input.place(x=200, y=300)

tk.Button(main, text="Zapisz dane", command=lambda: [append_data, print(selected_sex.get())]).place(x=50, y=350)
main.mainloop()
