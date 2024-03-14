# import tkinter as tk
# from tkinter import Label, PhotoImage, ttk
# from PIL import Image, ImageTk

# class Menu:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1360x688+0+0")
#         self.root.title("SSIT Information Center")
#         self.root.config(bg='#282b30')

#         # Logo
#         img = Image.open(r"images/ssit_logo2.jpg")
#         img = img.resize((140, 100), Image.BICUBIC)
#         self.photoimg = ImageTk.PhotoImage(img)

#         first_label = Label(self.root, image=self.photoimg)
#         first_label.place(x=0, y=0, width=140, height=100)

#         # Title Of Institute
#         title_label = Label(text="SHREE SWAMINARAYAN INSTITUTE OF TECHNOLOGY", font=("palatino", 32, "bold",),
#                             bg='black', fg='#f5f5f5')
#         title_label.place(x=140, y=0, width=1220, height=100)

#         # Creator's Logo
#         img1 = Image.open("GP Logo-modified.png")
#         img1 = img1.resize((100, 100), Image.BICUBIC)
#         self.photoimg1 = ImageTk.PhotoImage(img1)

#         second_label = Label(self.root, image=self.photoimg1)
#         second_label.place(x=650, y=600, width=100, height=100)

#         # Title Of Project
#         title_label1 = Label(text="SSIT Information", font=("palatino", 26, "bold", "underline"), bg='#282b30', fg='#f5f5f5')
#         title_label1.place(x=0, y=120, width=1360, height=50)

#         # List of choices
#         choices = [
#             "Admission Details",
#             "Director's Sir Details",
#             "Principal Details",
#             "Faculties",
#             "Other Information"
#         ]

#         # Labels for choices
#         label_height = 40
#         for i, choice in enumerate(choices, start=1):
#             tk.Label(root, text=f"{i}. {choice}", font=("palatino", 24, "italic"), bg='#282b30', fg='#f5f5f5').place(
#                 x=560, y=205 + (i - 1) * label_height, anchor="w")



#         # Entry for entering choice
#         self.choice_entry = ttk.Entry(root, font=("Helvetica", 14))
#         self.choice_entry.place(x=570, y=190 + i * label_height, width=250, height=30)
#         self.choice_entry.bind("<Return>", self.on_enter_pressed)
#         self.choice_entry.focus()

#     def on_enter_pressed(self, event):
#         try:
#             choice = int(self.choice_entry.get())
#             self.on_option_selected(choice)
#         except ValueError:
#             print("Please enter a valid choice.")

#     def on_option_selected(self, choice):
#         # Modify this function based on the desired actions for each choice
#         print(f"Selected Choice: {choice}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Menu(root)

#     # Function to exit on "Esc" key press
#     def on_escape(event):
#         root.destroy()

#     root.bind("<Escape>", on_escape)

#     root.mainloop()

import tkinter as tk
from tkinter import Label, ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x688+0+0")
        self.root.title("SSIT Information Center")
        self.root.config(bg='#282b30')

        def basic():
            # Logo
            img = Image.open(r"images/ssit_logo2.jpg")
            img = img.resize((140, 100), Image.BICUBIC)
            self.photoimg = ImageTk.PhotoImage(img)

            first_label = Label(self.root, image=self.photoimg)
            first_label.place(x=0, y=0, width=140, height=100)

            # Title Of Institute
            title_label = Label(text="SHREE SWAMINARAYAN INSTITUTE OF TECHNOLOGY", font=("palatino", 32, "bold",),
                                bg='black', fg='#f5f5f5')
            title_label.place(x=140, y=0, width=1220, height=100)

            # Creator's Logo
            img1 = Image.open("GP Logo-modified.png")
            img1 = img1.resize((100, 100), Image.BICUBIC)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            second_label = Label(self.root, image=self.photoimg1)
            second_label.place(x=650, y=600, width=100, height=100)

            # Title Of Project
            title_label1 = Label(text="SSIT Information", font=("palatino", 26, "bold", "underline"), bg='#282b30', fg='#f5f5f5')
            title_label1.place(x=0, y=120, width=1360, height=50)
        basic()

        # List of choices
        choices = [
            "Admission Details",
            "Director's Sir Details",
            "Principal Details",
            "Faculties",
            "Other Information"
        ]

        # Labels for choices
        label_height = 40
        for i, choice in enumerate(choices, start=1):
            tk.Label(root, text=f"{i}. {choice}", font=("palatino", 24, "italic"), bg='#282b30', fg='#f5f5f5').place(
                x=560, y=205 + (i - 1) * label_height, anchor="w")

        # Entry for entering choice
        self.choice_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.choice_entry.place(x=570, y=190 + i * label_height, width=250, height=30)
        self.choice_entry.bind("<Return>", self.on_enter_pressed)
        self.choice_entry.focus()

    def on_enter_pressed(self, event):
        try:
            choice = int(self.choice_entry.get())
            self.show_details_window(choice)
        except ValueError:
            tk.messagebox.showwarning("Invalid Input", "Please enter a numeric value.")

    def show_details_window(self, choice):
        new_window = tk.Toplevel(self.root)
        new_window.geometry("1360x688+0+0")
        new_window.title("SSIT Information Center")

        # Logo
        img2 = Image.open(r"images/topic_1.png")
        img2 = img2.resize((140, 100), Image.BICUBIC)
        photoimg2 = ImageTk.PhotoImage(img2)

        third_label = Label(new_window, image=photoimg2)
        third_label.place(x=0, y=0, width=1360, height=100)

        # # Title Of Institute
        # title_label3 = Label(new_window, text="SHREE SWAMINARAYAN INSTITUTE OF TECHNOLOGY", font=("palatino", 32, "bold",),bg='black', fg='#f5f5f5')
        # title_label3.place(x=140, y=0, width=1220, height=100)

        # Creator's Logo
        img3 = Image.open("GP Logo-modified.png")
        img3 = img3.resize((100, 100), Image.BICUBIC)
        photoimg3 = ImageTk.PhotoImage(img3)

        second_label = Label(new_window, image=photoimg3)
        second_label.place(x=650, y=600, width=100, height=100)
        
        def on_escape(event):
            new_window.destroy()

        new_window.bind("<Escape>", on_escape)


    def on_option_selected(self, choice):
        # Modify this function based on the desired actions for each choice
        print(f"Selected Choice: {choice}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)

    # Function to exit on "Esc" key press
    def on_escape(event):
        root.destroy()

    root.bind("<Escape>", on_escape)

    root.mainloop()


