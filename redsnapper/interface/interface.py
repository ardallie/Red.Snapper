"""
 this module contains class Interface
 a complete Graphical User Interface (GUI) for the application
"""
import threading
from tkinter import Frame, StringVar, Label, Scale, Spinbox, Text
from tkinter import Radiobutton, PhotoImage
from tkinter import LEFT, HORIZONTAL, END, RIDGE, FLAT
from tkinter import ttk
from redsnapper.modules.dataset import Dataset
from redsnapper.modules.export import Export


class Interface:
    """ GUI class """

    def __init__(self, master):
        # colour swatches
        self.gray1 = "#f6f6f6"
        self.gray2 = "#eaeaea"
        self.gray3 = "#d9d9d9"
        # key parameters
        self.running = False
        self.sect_width = 360
        self.rb_choice = StringVar()
        self.dob1_val = StringVar()
        self.dob2_val = StringVar()
        self.df_records = StringVar()

        master.geometry("800x600+200+200")
        master.title("Red Snapper")
        master.resizable(False, False)
        master.configure(background=self.gray1)

        # LEFT SECTION LAYER
        # --------------------------------------------------------------------
        self.sect_left = Frame(master)
        self.sect_left.place(x=15, y=15, width=self.sect_width, height=570)
        self.sect_left.config(relief=RIDGE)
        self.sect_left.config(background=self.gray2)

        # RIGHT SECTION LAYER
        # --------------------------------------------------------------------
        self.sect_right = Frame(master)
        self.sect_right.place(x=-15, y=200, width=self.sect_width, height=385)
        self.sect_right.place(relx=1.0, anchor="ne")
        self.sect_right.config(relief=RIDGE)
        self.sect_right.config(background=self.gray2)

        # Sliders layer
        self.layer_sliders = Frame(self.sect_left)
        self.layer_sliders.place(y=0, width=self.sect_width, height=320)
        self.layer_sliders.config(**self.layer_props(self.gray2))
        self.lab_sliders = Label(self.layer_sliders)
        self.lab_sliders.config(**self.title_props("Parameters"))
        self.lab_sliders.pack()

        # DOB layer
        self.layer_dob = Frame(self.sect_left)
        self.layer_dob.place(y=320, width=self.sect_width, height=80)
        self.layer_dob.config(**self.layer_props(self.gray2))
        self.lab_dob = Label(self.layer_dob)
        self.lab_dob.config(**self.title_props("Birthdays range"))
        self.lab_dob.pack()

        # Export layer
        self.layer_export = Frame(self.sect_left)
        self.layer_export.place(y=400, width=self.sect_width, height=80)
        self.layer_export.config(**self.layer_props(self.gray2))
        self.lab_export = Label(self.layer_export)
        self.lab_export.config(**self.title_props("Export format"))
        self.lab_export.pack()

        # Run layer
        self.layer_run = Frame(self.sect_left)
        self.layer_run.place(y=480, width=self.sect_width, height=100)
        self.layer_run.config(**self.layer_props(self.gray2))
        self.lab_run = Label(self.layer_run)
        self.lab_run.config(**self.title_props("Run"))
        self.lab_run.pack()

        # About layer
        self.layer_about = Frame(self.sect_right)
        self.layer_about.place(width=self.sect_width, height=385)
        self.layer_about.config(**self.layer_props(self.gray2))
        self.lab_about = Label(self.layer_about)
        self.lab_about.config(**self.title_props("About Red Snapper"))
        self.lab_about.pack()

        # sliders
        self.sli_wom = Scale(self.layer_sliders, from_=0, to=100)
        self.sli_wom.config(**self.sli_props())
        self.sli_wom.config(label="Percentage of women in dataset.")
        self.sli_wom.pack(padx=20, pady=10)
        self.sli_wom.set(50)

        self.sli_nam = Scale(self.layer_sliders, from_=0, to=100)
        self.sli_nam.config(**self.sli_props())
        self.sli_nam.config(label="Percentage of people with double name")
        self.sli_nam.pack(padx=20, pady=0)
        self.sli_nam.set(25)

        self.sli_sur = Scale(self.layer_sliders, from_=0, to=100)
        self.sli_sur.config(**self.sli_props())
        self.sli_sur.config(label="Percentage of people with double surname")
        self.sli_sur.pack(padx=20, pady=10)
        self.sli_sur.set(15)

        # DOB Layer - From Date
        self.dob1_val.set("1945")
        self.lab_dob1 = Label(self.layer_dob, text="From date")
        self.lab_dob1.config(**self.label_props())
        self.lab_dob1.pack(side=LEFT, padx=5)
        self.box_dob1 = Spinbox(self.layer_dob)
        self.box_dob1.config(from_=1945, to=1996, textvariable=self.dob1_val)
        self.box_dob1.config(**self.date_props())
        self.box_dob1.pack(side=LEFT)

        # DOB Layer - To Date
        self.dob2_val.set("1997")
        self.lab_dob2 = Label(self.layer_dob, text="To date")
        self.lab_dob2.config(**self.label_props())
        self.lab_dob2.pack(side=LEFT, padx=17)
        self.box_dob2 = Spinbox(self.layer_dob)
        self.box_dob2.config(from_=1946, to=1997, textvariable=self.dob2_val)
        self.box_dob2.config(**self.date_props())
        self.box_dob2.pack(side=LEFT)

        # Export layer - JSON / CSV radio buttons
        self.rb_choice.set("CSV")
        self.rb1 = Radiobutton(self.layer_export,
                               text="Save as CSV",
                               variable=self.rb_choice,
                               value="CSV")
        self.rb1.config(**self.radio_props())
        self.rb1.place(y=35, x=50)
        self.rb2 = Radiobutton(self.layer_export,
                               text="Save as JSON",
                               variable=self.rb_choice,
                               value="JSON")
        self.rb2.config(**self.radio_props())
        self.rb2.place(y=35, x=200)

        # Run layer - no of records spinbox
        self.df_records.set("100")
        self.box_gen = Spinbox(self.layer_run)
        self.box_gen.config(from_=1, to=999999, textvariable=self.df_records)
        self.box_gen.config(increment=1000, width=19)
        self.box_gen.place(x=70, y=53)
        self.lab_gen = Label(self.layer_run, text="Number of records")
        self.lab_gen.config(**self.label_props())
        self.lab_gen.place(x=70, y=30)

        # Run layer - generate button
        self.btn_run = ttk.Button(self.layer_run)
        self.btn_run.place(x=225, y=35, height=40)
        self.btn_run_reset()

        # header & logo section
        self.sect_logo = Frame(master)
        self.sect_logo.place(x=-15, y=30, width=350, height=120)
        self.sect_logo.place(relx=1.0, anchor="ne")
        self.logo = PhotoImage(file="./redsnapper/interface/logo.png")
        self.lab_logo = Label(self.sect_logo, image=self.logo)
        self.lab_logo.config(background=self.gray1)
        self.lab_logo.pack()

        # About
        box_about = Text(self.layer_about)
        box_about.config(**self.text_props())
        box_about.pack(pady=10, padx=10)
        txt = """This program allows generating thousands of rows filled with pseudo-random data. """ \
              + """\nThe generated records (like name,  """ \
              + """ surname, date of birth, e-mail address) can be used to provide sample data to:
        - test query performance of your database 
        - practice data operations with BI tools.""" \
              + """ \nThe application uses 4 processes to generate data simultaneously. """ \
              + """ It takes about 25 seconds to create 1 million rows of data.\n"""

        box_about.insert(END, txt)

    # styling wrapped into functions for reusability
    def sli_props(self):
        """
        bundle popular attributes of TK control so they can be reused
        :return: dict of bundled props
        """
        return {
            "length": 300,
            "orient": HORIZONTAL,
            "sliderrelief": FLAT,
            "showvalue": 1,
            "resolution": 1,
            "sliderlength": 25,
            "tickinterval": 100,
            "font": ("Arial", 8),
            "activebackground": "#333333",
            "background": "#666666",
            "troughcolor": "#d0d4d2",
            "foreground": "#eeeeee",
            "highlightthickness": 8,
            "highlightcolor": "#ffffff",
            "highlightbackground": self.gray3,
            "borderwidth": 1
        }

    @staticmethod
    def layer_props(bgcolor):
        """
        bundle popular attributes of TK control so they can be reused
        :return: dict of bundled props
        """
        return {
            "relief": RIDGE,
            "background": bgcolor
        }

    def title_props(self, title):
        """
        bundle popular attributes of TK control so they can be reused
        :return: dict of bundled props
        """
        return {
            "text": title,
            "background": self.gray3,
            "width": self.sect_width,
            "borderwidth": 1,
            "relief": RIDGE
        }

    def radio_props(self):
        """
        bundle popular attributes of TK control so they can be reused
        :return: dict of bundled props
        """
        return {
            "background": self.gray2,
            "activebackground": self.gray2,
        }

    def date_props(self):
        """
        bundle popular attributes of TK control so they can be reused
        :return: dict of bundled props
        """
        return {
            "width": 8,
            "increment": 1,
            "font": ("Arial", 8),
            "background": "#666666",
            "buttonbackground": "#666666",
            "foreground": "#eeeeee",
            "highlightthickness": 8,
            "highlightcolor": "#ffffff",
            "highlightbackground": self.gray2,
            "borderwidth": 1
        }

    def label_props(self):
        """
        bundle popular attributes of TK control so they can be reused
        :return: dict of bundled props
        """
        return {
            "background": self.gray2,
            "highlightcolor": "#ffffff",
            "highlightbackground": self.gray2,
            "borderwidth": 1
        }

    def text_props(self):
        """
        bundle popular attributes of TK control so they can be reused
        :return: dict of bundled props
        """
        return {
            "font": ("Arial", 11),
            "background": self.gray1,
            "foreground": "#212121",
            "highlightthickness": 8,
            "highlightbackground": self.gray1,
            "highlightcolor": self.gray1,
            "borderwidth": 0,
            "wrap": "word",
            "spacing1": 11,
            "spacing2": 7,
        }

    def produce_props(self):
        """
        produce dict of key GUI parameters selected by user
        :return: no return parameters
        """
        rows = int(self.box_gen.get())
        props = {
            "pgender": self.sli_wom.get(),
            "pdname": self.sli_nam.get(),
            "pdsurname": self.sli_sur.get(),
            "dob1": self.box_dob1.get(),
            "dob2": self.box_dob2.get(),
        }
        dataset = Dataset().run_workload(rows, **props)
        exp_format = self.rb_choice.get()
        if exp_format == "CSV":
            Export().to_csv(dataset)
        else:
            Export().to_json(dataset)
        self.btn_run_reset()
        return

    def btn_run_reset(self):
        """
        abort button (when generating)
        :return: no return parameters
        """
        self.running = False
        self.btn_run.config(text="Generate", command=self.btn_run_start)
        return

    def btn_run_start(self):
        """
        handle the run button
        :return: no return parameters
        """
        self.running = True
        newthread = threading.Thread(target=self.produce_props)
        newthread.start()
        self.btn_run.config(text="Abort", command=self.btn_run_reset)
        return
