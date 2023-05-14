import tkinter as tk

from ui import *
import global_variables
from db_connection import *

# Importing module
import mysql.connector

if __name__ == "__main__":
    """
    Main function, create main window and call create_user_interface function
    
    Function create_user_interface is in ui.py file, and as an argument it takes main window
    create 
    """

    # create main window
    main = tk.Tk()
    main.title("Kalkulator centylowy")

    # get screen width and height
    width = main.winfo_screenwidth()
    height = main.winfo_screenheight()

    # setting up first window size
    # main.geometry(f"{width}x{height}") # set window size to screen size
    # main.geometry("740x800")  # set window size to 1100x800

    #making window in center
    # Uzyskanie wymiarów ekranu
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    # Ustalenie wymiarów okna i pozycji, aby wyśrodkować okno
    window_width = 730
    window_height = 780
    x_pos = (screen_width // 2) - (window_width // 2)
    y_pos = (screen_height // 2) - (window_height // 2)

    # Ustawienie pozycji okna
    main.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

    # background color
    main.configure(bg=global_variables.background_color)  # setting background color`

    create_main_menu(main)

    # running main window
    main.mainloop()

