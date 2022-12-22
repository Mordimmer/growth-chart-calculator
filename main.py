from ui import *

if __name__ == "__main__":
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

    # create user interface
    create_user_interface(main)
    create_charts(main)
    # running main window
    main.mainloop()