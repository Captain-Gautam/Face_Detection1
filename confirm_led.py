# import serial

# port = serial.Serial('/dev/ttyUSB0', 9600)

# # while (port.isOpen()):
# #     data = input("Enter 1 to ""ON"" the led and 0 to ""OFF"" the led: ")
# #     if (data == '1'):
# #         port.write('1')
# #     elif (data == '0'):
# #         port.write('0')
# #     else:
# #         print("Invalid Input")

# while port.isOpen():
#     data = input("Enter 1 to 'ON' the led and 0 to 'OFF' the led: ")
#     if data == '1' or data == '0':
#         port.write(data.encode())  # Convert string to bytes before sending
#     else:
#         print("Invalid Input")



# import tkinter as tk
# from pyfiglet import Figlet

# def create_window():
#     window = tk.Tk()
#     window.geometry("1360x688+0+0")
#     window.title("ASCII Window")
#     window.configure(bg="black")

#     figlet = Figlet(font='slant') #univers
#     ascii_text = figlet.renderText("Hello, Gautam\nWel-Come to SSIT")

#     label = tk.Label(window, text=ascii_text, font=("Courier", 20), fg="white", bg="red")#, justify=tk.LEFT)
#     label.pack(padx=20, pady=20)

#     window.mainloop()

# # Create the tkinter window
# create_window()


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def window_unknown():
    def show_description(choice):
        descriptions = {
            1: {
                "text": """
                    Professor Niraj Sir is an experienced faculty member in the Computer Science department.
                    He specializes in topics such as algorithms, data structures, and software engineering.
                    """,
                "image_path": "images/modi.jpg"
            },
            2: {
                "text": """
                    Professor Dharmesh Sir is a dedicated teacher in the Electronics and Communication department.
                    He focuses on subjects like digital electronics, communication systems, and signal processing.
                    """,
                "image_path": "images/modi.jpg"
            },
            3: {
                "text": """
                    Professor Hitesh Sir is a renowned educator in the Mechanical Engineering department.
                    His expertise lies in thermodynamics, fluid mechanics, and machine design.
                    """,
                "image_path": "images/modi.jpg"
            },
            4: {
                "text": """
                    Dr. Ramesh Sir (IT Department):
                    Dr. Ramesh is a distinguished professor in the Information Technology department,
                    specializing in areas such as database management and artificial intelligence.

                    Professor Darshan Sir (CE Department):
                    Professor Darshan is an accomplished faculty member in the Civil Engineering department,
                    with expertise in structural engineering and construction management.
                    """,
                "image_path": "images/modi.jpg"
            },
            5: {
                "text": """
                    Gautam Prajapati is a student pursuing studies in Computer Science.
                    He is passionate about programming, machine learning, and web development.
                    """,
                "image_path": "images/modi.jpg"
            }
        }
        def go_home():
            description_window.destroy()
            root.deiconify()

        description_window = tk.Toplevel(root)
        description_window.title(f"Choice {choice} Description")
        description_window.geometry("1360x688+0+0")
        description_window.configure(bg="black")

        description_label = tk.Label(description_window, text=descriptions[choice]["text"], font=("Courier", 14), justify=tk.LEFT)
        description_label.pack(padx=20, pady=20)

        #to exit the choice descriptiion with esc button
        def escape(event):
            description_window.destroy()

        description_window.bind("<Escape>", escape)



        # Load and display the image
        image_path = descriptions[choice]["image_path"]
        if image_path:
            img = Image.open(image_path)
            img = img.resize((100, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            image_label = tk.Label(description_window, image=img)
            image_label.image = img  # To prevent garbage collection
            image_label.pack(padx=20, pady=20)

        home_button = tk.Button(description_window, text="Home", command=go_home, font=("Courier", 14))
        home_button.pack(pady=10)

    # Function to handle the choice selection
    def handle_choice():
        try:
            choice = int(entry.get())
            if 1 <= choice <= 5:
                entry.delete(0, tk.END) 
                show_description(choice)
            else:
                messagebox.showwarning("Invalid Choice", "Please enter a valid choice between 1 and 7.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a numeric value.")
    # Create the main window
    root = tk.Tk()
    root.geometry("1360x688+0+0")
    root.title("Choice Description App")
    root.configure(bg = "black")

    # Add widgets to the main window
    menu = "1.Addmission Process Faculty Detail \n2.Director Sir Details\n3.Principal Details\n4.HOD'sDetails\n5.Admin Contact"
    label = tk.Label(root, text=menu, font=("Courier", 14), justify=tk.LEFT, bg="pink")
    label.pack(padx=20, pady=20)

    entry = tk.Entry(root, font=("Courier", 14), bg="pink")
    entry.pack(padx=20, pady=20)

    button = tk.Button(root, text="Show Description", command=handle_choice, font=("Courier", 14), fg="purple", bg="pink")
    button.pack(padx=20, pady=20)
    
    #To exit the main window with esc button
    def on_escape(event):
        root.destroy()
    
    #root.after(5000, root.destroy)
    root.bind("<Escape>", on_escape)
    # Start the Tkinter event loop
    root.mainloop()

window_unknown()



        