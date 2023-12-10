import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkbox


# GLOBAL VARIABLES
man_saved = False
so_saved = False
pin_saved = False
wind_saved = False
dragon_saved = False
man_list = None
so_list = None
pin_list = None
wind_list = None
dragon_list = None


def number_or_none(input_str):
    """ Validates and converts the inputs as integers.
    """
    try:
        if input_str == "":
            return int(0)
        return int(input_str)
    except ValueError:
        tkbox.showerror("Bad Value", "Input is not an integer.")
        return None


def input_so():
    global man_saved
    man_saved = True

    man1 = number_or_none(app.man1_string.get())
    man2 = number_or_none(app.man2_string.get())
    man3 = number_or_none(app.man3_string.get())
    man4 = number_or_none(app.man4_string.get())
    man5 = number_or_none(app.man5_string.get())
    man6 = number_or_none(app.man6_string.get())
    man7 = number_or_none(app.man7_string.get())
    man8 = number_or_none(app.man8_string.get()) 
    man9 = number_or_none(app.man9_string.get())

    if ( man1 is not None and man2 is not None and man3 is not None and man4 is not None
    and man5 is not None
    and man6 is not None and man7 is not None
    and man8 is not None and man9 is not None):
        try:
            temp = [man1, man2, man3, man4, man5, man6, man7, man8, man9]
            for man in temp:
                if man < 0 or man > 4:
                    raise ValueError

            global man_list
            man_list = [0, man1, man2, man3, man4, man5, man6, man7, man8, man9]
            print(man_list)
            app.root.destroy()
        except ValueError:
            tkbox.showerror("Too Big or Too Small",
                            "0 <= man number <= 4")
    else:
        return


def input_pin():
    global so_saved
    so_saved = True

    so1 = number_or_none(app.so1_string.get())
    so2 = number_or_none(app.so2_string.get())
    so3 = number_or_none(app.so3_string.get())
    so4 = number_or_none(app.so4_string.get())
    so5 = number_or_none(app.so5_string.get())
    so6 = number_or_none(app.so6_string.get())
    so7 = number_or_none(app.so7_string.get())
    so8 = number_or_none(app.so8_string.get()) 
    so9 = number_or_none(app.so9_string.get())

    if (so1 is not None and so2 is not None and so3 is not None and so4 is not None
    and so5 is not None
    and so6 is not None and so7 is not None
    and so8 is not None and so9 is not None):
        try:
            temp = [so1, so2, so3, so4, so5, so6, so7, so8, so9]
            for so in temp:
                if so < 0 or so > 4:
                    raise ValueError
            
            global so_list
            so_list = [0, so1, so2, so3, so4, so5, so6, so7, so8, so9]
            print(so_list)
            app.root.destroy()
        except ValueError:
            tkbox.showerror("Too Big or Too Small",
                            "0 <= so number <= 4")

    else:
        return


def input_windtiles():
    global pin_saved
    pin_saved = True

    pin1 = number_or_none(app.pin1_string.get())
    pin2 = number_or_none(app.pin2_string.get())
    pin3 = number_or_none(app.pin3_string.get())
    pin4 = number_or_none(app.pin4_string.get())
    pin5 = number_or_none(app.pin5_string.get())
    pin6 = number_or_none(app.pin6_string.get())
    pin7 = number_or_none(app.pin7_string.get())
    pin8 = number_or_none(app.pin8_string.get()) 
    pin9 = number_or_none(app.pin9_string.get())

    if ( pin1 is not None and pin2 is not None and pin3 is not None and pin4 is not None
    and pin5 is not None
    and pin6 is not None and pin7 is not None
    and pin8 is not None and pin9 is not None):
        try:
            temp = [pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9]
            for pin in temp:
                if pin < 0 or pin > 4:
                    raise ValueError
            global pin_list
            pin_list = [0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9]
            print(pin_list)
            app.root.destroy()
        except ValueError:
            tkbox.showerror("Too Big or Too Small",
                            "0 <= pin number <= 4")
    else:
        return


def input_Dragontiles():
    global wind_saved
    wind_saved = True

    east = number_or_none(app.east_string.get())
    south = number_or_none(app.south_string.get())
    west = number_or_none(app.west_string.get())
    north = number_or_none(app.north_string.get())

    if (east is not None and south is not None and west is not None and north is not None):
        try:
            temp = [east, south, west, north]
            for wind in temp:
                if wind < 0 or wind > 4:
                    raise ValueError
            global wind_list
            wind_list = [0, east, south, west, north]
            print(wind_list)
            app.root.destroy()
        except ValueError:
                    tkbox.showerror("Too Big or Too Small",
                                    "0 <= wind tile number <= 4")
    else:
        return


def on_start():

    white = number_or_none(app.white_string.get())
    green = number_or_none(app.green_string.get())
    red = number_or_none(app.red_string.get())

    if (white is not None and green is not None and red is not None):
        try:
            temp = [red, green, white]
            for wind in temp:
                if wind < 0 or wind > 4:
                    raise ValueError
            global dragon_list
            dragon_list = [red, green, white]
            print(dragon_list)
            app.root.destroy()
        except ValueError:
            tkbox.showerror("Too Big or Too Small",
                            "0 <= dragon tile number <= 4")
    else:
        return


class App:
    def run_hand_to_check(self):
        """
        Runs the input window.
        """

        self.root = tk.Tk()
        self.root.title("Mahjong Assisting Program")
        my_frame = ttk.Frame(self.root, padding=50)
        my_frame.grid()

        ttk.Label(my_frame, text="How many Mans in hand?").grid(row=0, column=0)

        ttk.Label(my_frame, text="1 Man:").grid(row=1, column=0)
        self.man1_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man1_string).grid(row=1,
                                                                 column=1)

        ttk.Label(my_frame, text="2 Man:").grid(row=2, column=0)
        self.man2_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man2_string).grid(row=2,
                                                                column=1)

        ttk.Label(my_frame, text="3 Man:").grid(row=3, column=0)
        self.man3_string = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.man3_string).grid(row=3,
                                                                      column=1)

        ttk.Label(my_frame, text="4 Man:").grid(row=4, column=0)
        self.man4_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man4_string).grid(row=4,
                                                                    column=1)

        ttk.Label(my_frame, text="5 Man:").grid(row=5, column=0)
        self.man5_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man5_string).grid(row=5,
                                                                    column=1)

        ttk.Label(my_frame, text="6 Man:").grid(row=6, column=0)
        self.man6_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man6_string).grid(row=6,
                                                                    column=1)

        ttk.Label(my_frame, text="7 Man:").grid(row=7, column=0)
        self.man7_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man7_string).grid(row=7,
                                                                    column=1)
        ttk.Label(my_frame, text="8 Man:").grid(row=8, column=0)
        self.man8_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man8_string).grid(row=8,
                                                                    column=1)
        ttk.Label(my_frame, text="9 Man:").grid(row=9, column=0)
        self.man9_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man9_string).grid(row=9,
                                                                    column=1)

        ttk.Button(my_frame, text="Next", command=input_so).grid(row=10,
                                                                 column=0)
        self.root.mainloop()

        global man_saved
        if man_saved:
            self.root = tk.Tk()
            self.root.title("Mahjong Assisting Program")
            my_frame = ttk.Frame(self.root, padding=50)
            my_frame.grid()

            ttk.Label(my_frame, text="How many Sos in hand?").grid(row=0, column=0)

            ttk.Label(my_frame, text="1 So:").grid(row=1, column=0)
            self.so1_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so1_string).grid(row=1,
                                                                    column=1)

            ttk.Label(my_frame, text="2 So:").grid(row=2, column=0)
            self.so2_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so2_string).grid(row=2,
                                                                    column=1)

            ttk.Label(my_frame, text="3 So:").grid(row=3, column=0)
            self.so3_string = tk.StringVar()
            ttk.Entry(my_frame, textvariable=self.so3_string).grid(row=3,
                                                                        column=1)

            ttk.Label(my_frame, text="4 So:").grid(row=4, column=0)
            self.so4_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so4_string).grid(row=4,
                                                                        column=1)

            ttk.Label(my_frame, text="5 So:").grid(row=5, column=0)
            self.so5_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so5_string).grid(row=5,
                                                                        column=1)

            ttk.Label(my_frame, text="6 So:").grid(row=6, column=0)
            self.so6_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so6_string).grid(row=6,
                                                                        column=1)

            ttk.Label(my_frame, text="7 So:").grid(row=7, column=0)
            self.so7_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so7_string).grid(row=7,
                                                                        column=1)
            ttk.Label(my_frame, text="8 So:").grid(row=8, column=0)
            self.so8_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so8_string).grid(row=8,
                                                                        column=1)
            ttk.Label(my_frame, text="9 So:").grid(row=9, column=0)
            self.so9_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so9_string).grid(row=9,
                                                                        column=1)

            ttk.Button(my_frame, text="Next", command=input_pin).grid(row=10,
                                                                    column=0)
            self.root.mainloop()
            
            global so_saved
            if so_saved:
                self.root = tk.Tk()
                self.root.title("Mahjong Assisting Program")
                my_frame = ttk.Frame(self.root, padding=50)
                my_frame.grid()

                ttk.Label(my_frame, text="How many Pins in hand?").grid(row=0, column=0)

                ttk.Label(my_frame, text="1 Pin:").grid(row=1, column=0)
                self.pin1_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin1_string).grid(row=1,
                                                                        column=1)

                ttk.Label(my_frame, text="2 Pin:").grid(row=2, column=0)
                self.pin2_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin2_string).grid(row=2,
                                                                        column=1)

                ttk.Label(my_frame, text="3 Pin:").grid(row=3, column=0)
                self.pin3_string = tk.StringVar()
                ttk.Entry(my_frame, textvariable=self.pin3_string).grid(row=3,
                                                                            column=1)

                ttk.Label(my_frame, text="4 Pin:").grid(row=4, column=0)
                self.pin4_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin4_string).grid(row=4,
                                                                            column=1)

                ttk.Label(my_frame, text="5 Pin:").grid(row=5, column=0)
                self.pin5_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin5_string).grid(row=5,
                                                                            column=1)

                ttk.Label(my_frame, text="6 Pin:").grid(row=6, column=0)
                self.pin6_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin6_string).grid(row=6,
                                                                            column=1)

                ttk.Label(my_frame, text="7 Pin:").grid(row=7, column=0)
                self.pin7_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin7_string).grid(row=7,
                                                                            column=1)
                ttk.Label(my_frame, text="8 Pin:").grid(row=8, column=0)
                self.pin8_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin8_string).grid(row=8,
                                                                            column=1)
                ttk.Label(my_frame, text="9 Pin:").grid(row=9, column=0)
                self.pin9_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin9_string).grid(row=9,
                                                                            column=1)

                ttk.Button(my_frame, text="Next", command=input_windtiles).grid(row=10,
                                                                        column=0)

                self.root.mainloop()

                global pin_saved
                if pin_saved:
                    self.root = tk.Tk()
                    self.root.title("Mahjong Assisting Program")
                    my_frame = ttk.Frame(self.root, padding=50)
                    my_frame.grid()

                    ttk.Label(my_frame, text="How many wind tiles in hand?").grid(row=0, column=0)

                    ttk.Label(my_frame, text="East Wind:").grid(row=1, column=0)
                    self.east_string = tk.StringVar()
                    ttk.Entry(my_frame,
                            textvariable=self.east_string).grid(row=1,
                                                                            column=1)

                    ttk.Label(my_frame, text="South Wind:").grid(row=2, column=0)
                    self.south_string = tk.StringVar()
                    ttk.Entry(my_frame,
                            textvariable=self.south_string).grid(row=2,
                                                                            column=1)

                    ttk.Label(my_frame, text="West Wind:").grid(row=3, column=0)
                    self.west_string = tk.StringVar()
                    ttk.Entry(my_frame, textvariable=self.west_string).grid(row=3,
                                                                                column=1)

                    ttk.Label(my_frame, text="North Wind:").grid(row=4, column=0)
                    self.north_string = tk.StringVar()
                    ttk.Entry(my_frame,
                            textvariable=self.north_string).grid(row=4,
                                                                                column=1)
                    ttk.Button(my_frame, text="Next", command=input_Dragontiles).grid(row=5,
                                                                        column=0)
                    self.root.mainloop()

                    global wind_saved
                    if wind_saved:
                        self.root = tk.Tk()
                        self.root.title("Mahjong Assisting Program")
                        my_frame = ttk.Frame(self.root, padding=50)
                        my_frame.grid()

                        ttk.Label(my_frame, text="How many Dragon tiles in hand?").grid(row=0, column=0)

                        ttk.Label(my_frame, text="White:").grid(row=2, column=0)
                        self.white_string = tk.StringVar()
                        ttk.Entry(my_frame,
                                textvariable=self.white_string).grid(row=2,
                                                                                column=1)

                        ttk.Label(my_frame, text="Green:").grid(row=3, column=0)
                        self.green_string = tk.StringVar()
                        ttk.Entry(my_frame,
                                textvariable=self.green_string).grid(row=3,
                                                                                column=1)

                        ttk.Label(my_frame, text="Red:").grid(row=1, column=0)
                        self.red_string = tk.StringVar()
                        ttk.Entry(my_frame, textvariable=self.red_string).grid(row=1,
                                                                                    column=1)

                        ttk.Button(my_frame, text="Save", command=on_start).grid(row=4,
                                                                            column=0)
                        self.root.mainloop()

        hand_to_check = man_list + so_list + pin_list + wind_list + dragon_list
        print(len(hand_to_check))

        if sum(hand_to_check) != 14:
            tkbox.showerror("Tile number error", "The total number of tiles in hand should be 14.")
            man_saved = False
            so_saved = False
            pin_saved = False
            wind_saved = False
            global dragon_saved
            dragon_saved = False

            self.run_hand_to_check()

        man_saved = False
        so_saved = False
        pin_saved = False
        wind_saved = False
        dragon_saved = False

        return hand_to_check

    def run_tiles_on_table(self):
        """
        Runs the input window for tiles on table.
        """
        self.root = tk.Tk()
        self.root.title("Mahjong Assisting Program")
        my_frame = ttk.Frame(self.root, padding=50)
        my_frame.grid()

        ttk.Label(my_frame, text="How many Mans on table?").grid(row=0, column=0)

        ttk.Label(my_frame, text="1 Man:").grid(row=1, column=0)
        self.man1_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man1_string).grid(row=1,
                                                                 column=1)

        ttk.Label(my_frame, text="2 Man:").grid(row=2, column=0)
        self.man2_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man2_string).grid(row=2,
                                                                column=1)

        ttk.Label(my_frame, text="3 Man:").grid(row=3, column=0)
        self.man3_string = tk.StringVar()
        ttk.Entry(my_frame, textvariable=self.man3_string).grid(row=3,
                                                                      column=1)

        ttk.Label(my_frame, text="4 Man:").grid(row=4, column=0)
        self.man4_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man4_string).grid(row=4,
                                                                    column=1)

        ttk.Label(my_frame, text="5 Man:").grid(row=5, column=0)
        self.man5_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man5_string).grid(row=5,
                                                                    column=1)

        ttk.Label(my_frame, text="6 Man:").grid(row=6, column=0)
        self.man6_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man6_string).grid(row=6,
                                                                    column=1)

        ttk.Label(my_frame, text="7 Man:").grid(row=7, column=0)
        self.man7_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man7_string).grid(row=7,
                                                                    column=1)
        ttk.Label(my_frame, text="8 Man:").grid(row=8, column=0)
        self.man8_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man8_string).grid(row=8,
                                                                    column=1)
        ttk.Label(my_frame, text="9 Man:").grid(row=9, column=0)
        self.man9_string = tk.StringVar()
        ttk.Entry(my_frame,
                  textvariable=self.man9_string).grid(row=9,
                                                                    column=1)

        ttk.Button(my_frame, text="Next", command=input_so).grid(row=10,
                                                                 column=0)
        self.root.mainloop()

        global man_saved
        if man_saved:
            self.root = tk.Tk()
            self.root.title("Mahjong Assisting Program")
            my_frame = ttk.Frame(self.root, padding=50)
            my_frame.grid()

            ttk.Label(my_frame, text="How many Sos on table?").grid(row=0, column=0)

            ttk.Label(my_frame, text="1 So:").grid(row=1, column=0)
            self.so1_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so1_string).grid(row=1,
                                                                    column=1)

            ttk.Label(my_frame, text="2 So:").grid(row=2, column=0)
            self.so2_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so2_string).grid(row=2,
                                                                    column=1)

            ttk.Label(my_frame, text="3 So:").grid(row=3, column=0)
            self.so3_string = tk.StringVar()
            ttk.Entry(my_frame, textvariable=self.so3_string).grid(row=3,
                                                                        column=1)

            ttk.Label(my_frame, text="4 So:").grid(row=4, column=0)
            self.so4_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so4_string).grid(row=4,
                                                                        column=1)

            ttk.Label(my_frame, text="5 So:").grid(row=5, column=0)
            self.so5_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so5_string).grid(row=5,
                                                                        column=1)

            ttk.Label(my_frame, text="6 So:").grid(row=6, column=0)
            self.so6_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so6_string).grid(row=6,
                                                                        column=1)

            ttk.Label(my_frame, text="7 So:").grid(row=7, column=0)
            self.so7_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so7_string).grid(row=7,
                                                                        column=1)
            ttk.Label(my_frame, text="8 So:").grid(row=8, column=0)
            self.so8_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so8_string).grid(row=8,
                                                                        column=1)
            ttk.Label(my_frame, text="9 So:").grid(row=9, column=0)
            self.so9_string = tk.StringVar()
            ttk.Entry(my_frame,
                    textvariable=self.so9_string).grid(row=9,
                                                                        column=1)

            ttk.Button(my_frame, text="Next", command=input_pin).grid(row=10,
                                                                    column=0)
            self.root.mainloop()
            
            global so_saved
            if so_saved:
                self.root = tk.Tk()
                self.root.title("Mahjong Assisting Program")
                my_frame = ttk.Frame(self.root, padding=50)
                my_frame.grid()

                ttk.Label(my_frame, text="How many Pins on table?").grid(row=0, column=0)

                ttk.Label(my_frame, text="1 Pin:").grid(row=1, column=0)
                self.pin1_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin1_string).grid(row=1,
                                                                        column=1)

                ttk.Label(my_frame, text="2 Pin:").grid(row=2, column=0)
                self.pin2_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin2_string).grid(row=2,
                                                                        column=1)

                ttk.Label(my_frame, text="3 Pin:").grid(row=3, column=0)
                self.pin3_string = tk.StringVar()
                ttk.Entry(my_frame, textvariable=self.pin3_string).grid(row=3,
                                                                            column=1)

                ttk.Label(my_frame, text="4 Pin:").grid(row=4, column=0)
                self.pin4_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin4_string).grid(row=4,
                                                                            column=1)

                ttk.Label(my_frame, text="5 Pin:").grid(row=5, column=0)
                self.pin5_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin5_string).grid(row=5,
                                                                            column=1)

                ttk.Label(my_frame, text="6 Pin:").grid(row=6, column=0)
                self.pin6_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin6_string).grid(row=6,
                                                                            column=1)

                ttk.Label(my_frame, text="7 Pin:").grid(row=7, column=0)
                self.pin7_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin7_string).grid(row=7,
                                                                            column=1)
                ttk.Label(my_frame, text="8 Pin:").grid(row=8, column=0)
                self.pin8_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin8_string).grid(row=8,
                                                                            column=1)
                ttk.Label(my_frame, text="9 Pin:").grid(row=9, column=0)
                self.pin9_string = tk.StringVar()
                ttk.Entry(my_frame,
                        textvariable=self.pin9_string).grid(row=9,
                                                                            column=1)

                ttk.Button(my_frame, text="Next", command=input_windtiles).grid(row=10,
                                                                        column=0)

                self.root.mainloop()

                global pin_saved
                if pin_saved:
                    self.root = tk.Tk()
                    self.root.title("Mahjong Assisting Program")
                    my_frame = ttk.Frame(self.root, padding=50)
                    my_frame.grid()

                    ttk.Label(my_frame, text="How many wind tiles on table?").grid(row=0, column=0)

                    ttk.Label(my_frame, text="East Wind:").grid(row=1, column=0)
                    self.east_string = tk.StringVar()
                    ttk.Entry(my_frame,
                            textvariable=self.east_string).grid(row=1,
                                                                            column=1)

                    ttk.Label(my_frame, text="South Wind:").grid(row=2, column=0)
                    self.south_string = tk.StringVar()
                    ttk.Entry(my_frame,
                            textvariable=self.south_string).grid(row=2,
                                                                            column=1)

                    ttk.Label(my_frame, text="West Wind:").grid(row=3, column=0)
                    self.west_string = tk.StringVar()
                    ttk.Entry(my_frame, textvariable=self.west_string).grid(row=3,
                                                                                column=1)

                    ttk.Label(my_frame, text="North Wind:").grid(row=4, column=0)
                    self.north_string = tk.StringVar()
                    ttk.Entry(my_frame,
                            textvariable=self.north_string).grid(row=4,
                                                                                column=1)
                    ttk.Button(my_frame, text="Next", command=input_Dragontiles).grid(row=5,
                                                                        column=0)
                    self.root.mainloop()

                    global wind_saved
                    if wind_saved:
                        self.root = tk.Tk()
                        self.root.title("Mahjong Assisting Program")
                        my_frame = ttk.Frame(self.root, padding=50)
                        my_frame.grid()

                        ttk.Label(my_frame, text="How many Dragon tiles on table?").grid(row=0, column=0)

                        ttk.Label(my_frame, text="White:").grid(row=2, column=0)
                        self.white_string = tk.StringVar()
                        ttk.Entry(my_frame,
                                textvariable=self.white_string).grid(row=2,
                                                                                column=1)

                        ttk.Label(my_frame, text="Green:").grid(row=3, column=0)
                        self.green_string = tk.StringVar()
                        ttk.Entry(my_frame,
                                textvariable=self.green_string).grid(row=3,
                                                                                column=1)

                        ttk.Label(my_frame, text="Red:").grid(row=1, column=0)
                        self.red_string = tk.StringVar()
                        ttk.Entry(my_frame, textvariable=self.red_string).grid(row=1,
                                                                                    column=1)

                        ttk.Button(my_frame, text="Save", command=on_start).grid(row=4,
                                                                            column=0)
                        self.root.mainloop()

        hand_on_table = man_list + so_list + pin_list + wind_list + dragon_list
        print(len(hand_on_table))

        return hand_on_table


if __name__ == "__main__":
    app = App()
    app.run_hand_to_check()
    app.run_tiles_on_table()
