import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk

def window_unknown():
    def show_description(choice):
        descriptions = {
            1: {
                "text": """Professor Niraj Sir is an experienced faculty member in the Computer Science department.\nHe specializes in topics such as algorithms, data structures, and software engineering.
                    """
            },
            2: {
                "text": """Professor Dharmesh Sir is a dedicated teacher in the Electronics and Communication department.\n
                    He focuses on subjects like digital electronics, communication systems, and signal processing.
                    """
            },
            3: {
                "text": """Professor Hitesh Sir is a renowned educator in the Mechanical Engineering department.\n
                    His expertise lies in thermodynamics, fluid mechanics, and machine design.
                    """
            },
            4: {
                "text": """Dr. Ramesh Sir (IT Department):\n
                    Dr. Ramesh is a distinguished professor in the Information Technology Department,\n
                    specializing in areas such as database management and artificial intelligence.\n\nProfessor Darshan Sir (CE Department):\n
                    Professor Darshan is an accomplished faculty member in the Computer Engineering Department,\n
                    with expertise in structural engineering and construction management.
                    """
            },
            5: {
                "text": """Gautam Prajapati is a student pursuing studies in Information Technology.\nHe is passionate about programming, Robotics and Machine Learning.
                    """
            }
        }

        def go_home():
            description_window.destroy()
            main_window.deiconify()

        description_window = tk.Toplevel(main_window)
        description_window.title(f"Choice {choice} Description")
        description_window.geometry("1360x688+0+0")
        description_window.configure(bg="black")

        description_label = tk.Label(description_window, text=descriptions[choice]["text"], font=("Courier", 14),justify=tk.LEFT, anchor="center")
        description_label.pack(padx=20, pady=20)
        

        # # Load and display the image
        # image_path = descriptions[choice]["image_path"]
        # if image_path:
        #     img = Image.open(image_path)
        #     img = img.resize((300, 300), Image.BICUBIC)
        #     img = ImageTk.PhotoImage(img)
        #     image_label = tk.Label(description_window, image=img)
        #     image_label.image = img  # To prevent garbage collection
        #     image_label.pack(padx=20, pady=20)

        home_button = tk.Button(description_window, text="Home", command=go_home, font=("Courier", 14))
        home_button.pack(pady=10)
        def on_escape_choice(event):
            exit_application_choice()

        def exit_application_choice():
            description_window.destroy()
        description_window.bind("<Escape>", on_escape_choice)

    def handle_choice():
        try:
            choice = int(entry.get())
            if 1 <= choice <= 7:
                show_description(choice)
                main_window.iconify()
            else:
                tk.messagebox.showwarning("Invalid Choice", "Please enter a valid choice between 1 and 7.")
        except ValueError:
            tk.messagebox.showwarning("Invalid Input", "Please enter a numeric value.")

    def on_escape(event):
        exit_application()

    def exit_application():
        main_window.destroy()

    # Main window
    main_window = tk.Tk()
    main_window.title("Choice Description App")
    main_window.geometry("1360x688+0+0")
    main_window.configure(bg="black")

    menu = "1.Admission Enquiry Details \n2.Managing Director Details \n3.Principal Details \n4.HOD's Details \n5.Developer Details. \n\n\nPRESS 'ESC' TO EXIT"
    label = tk.Label(main_window, text=menu, font=("Courier", 14), fg="white", bg="black",justify=tk.LEFT)
    label.pack(padx=20, pady=20)

    entry = tk.Entry(main_window, font=("Courier", 14))
    entry.pack(padx=20, pady=20)

    button = tk.Button(main_window, text="Show Description", command=handle_choice, font=("Courier", 14))
    button.pack(padx=20, pady=20)

    # exit_button = tk.Button(main_window, text="Exit", command=exit_application, font=("Courier", 14))
    # exit_button.pack(padx=20, pady=20)
    logo_path = "GP Logo-modified.png"  # Replace with the path to your logo image
    img = Image.open(logo_path)
    img = img.resize((100, 100), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)
    logo_label = tk.Label(main_window, image=img, bg="black")
    logo_label.img = img  # To prevent garbage collection
    logo_label.pack(side="bottom", padx=20, pady=20)

    main_window.bind("<Escape>", on_escape)

    main_window.mainloop()

    # Main window
    main_window = tk.Tk()
    main_window.title("Choice Description App")

    label = tk.Label(main_window, text="Enter your choice (1-7):", font=("Courier", 14))
    label.pack(padx=20, pady=20)

    entry = tk.Entry(main_window, font=("Courier", 14))
    entry.pack(padx=20, pady=20)

    button = tk.Button(main_window, text="Show Description", command=handle_choice, font=("Courier", 14))
    button.pack(padx=20, pady=20)

    # exit_button = tk.Button(main_window, text="Exit", command=exit_application, font=("Courier", 14))
    # exit_button.pack(padx=20, pady=20)
    logo_path = "GP Logo-modified.png"  # Replace with the path to your logo image
    img = Image.open(logo_path)
    img = img.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    logo_label = tk.Label(main_window, image=img, bg="black")
    logo_label.image = img  # To prevent garbage collection
    logo_label.pack(side=tk.RIGHT, padx=20, pady=20)

    main_window.bind("<Escape>", on_escape)

    main_window.mainloop()

# Example of using the function
window_unknown()
