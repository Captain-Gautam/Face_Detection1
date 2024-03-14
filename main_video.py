
# #=============With GTTS code==================
# import cv2
# from simple_facerec import SimpleFacerec
# from gtts import gTTS
# import os

# # Function to speak the name using gTTS
# def speak_name(name):
#     text_to_speech = gTTS(f"Hello, {name}", lang='en', tld='co.in')
#     text_to_speech.save("temp.mp3")
#     os.system("mpg321 temp.mp3")  # You may need to install mpg321 or use another player

# # Encode faces from a folder
# sfr = SimpleFacerec()
# sfr.load_encoding_images("images/")

# # Load Camera
# cap = cv2.VideoCapture(0)

# prev_name = None  # Variable to store the previous name

# while True:
#     ret, frame = cap.read()

#     # Detect Faces
#     face_locations, face_names = sfr.detect_known_faces(frame)
#     for face_loc, name in zip(face_locations, face_names):
#         y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

#         cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

#         # Speak the name only if it's different from the previous name
#         if name != prev_name:
#             speak_name(name)
#             prev_name = name

#     cv2.imshow("Frame", frame)

#     key = cv2.waitKey(1)
#     if key == 13:
#         break

# cap.release()
# cv2.destroyAllWindows()

# #==========For Display with GTTS=========
import cv2
from PIL import Image, ImageTk
from simple_facerec import SimpleFacerec
from gtts import gTTS
import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from pyfiglet import Figlet
import pygame

# Function to speak the known name using gTTS
def speak_name():
    # text_to_speech = gTTS(f"Hello, {name}, Welcome to SSIT", lang='en', tld='co.in')
    # text_to_speech.save("temp.mp3")
    #os.system("mpg321 temp.mp3")  # You may need to install mpg321 or use another player
    # Play the audio using pygame
    pygame.mixer.init()
    pygame.mixer.music.load("JSS1.mp3")
    pygame.mixer.music.play()
    # pygame.time.delay(3000)
    pygame.mixer.quit()

# Function to speak the unknown name using gTTS
def speak_unknown_name():
    # text_to_speech = gTTS(f"Jay Shree Swaminarayan, Welcome to SSIT ", lang='en', tld='co.in')
    # text_to_speech.save("unknown.mp3")
    #os.system("mpg321 unknown.mp3")  # You may need to install mpg321 or use another player
    # Play the audio using pygame
    pygame.mixer.init()
    pygame.mixer.music.load("JSS2.mp3")
    pygame.mixer.music.play()
    # pygame.time.delay(5000)
    pygame.mixer.quit()

# Function to create a tkinter window to open the known face to display the name
def create_window(name):
    window = tk.Tk()
    window.geometry("1360x688+0+0")
    window.title("Recognition Window")
    window.configure(bg="black")

    figlet = Figlet(font='slant')
    ascii_text = figlet.renderText(f"Hello, {name} \nWelcome to\nS. S. I. T.")

    label = tk.Label(window, text=ascii_text, font=("Courier", 20), fg="white", bg="black", justify=tk.LEFT)
    label.pack(padx=20, pady=20)

    logo_path = "GP Logo-modified.png"  # Replace with the path to your logo image
    img = Image.open(logo_path)
    img = img.resize((100, 100), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)
    logo_label = tk.Label(window, image=img, bg="black")
    logo_label.image = img  # To prevent garbage collection
    logo_label.pack(side=tk.RIGHT, padx=20, pady=20)

    window.after(3000, window.destroy)

    window.mainloop()

# Function for unknown person to have the menu
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
        

        # Load and display the image
        image_path = descriptions[choice]["image_path"]
        if image_path:
            img = Image.open(image_path)
            img = img.resize((300, 300), Image.BICUBIC)
            img = ImageTk.PhotoImage(img)
            image_label = tk.Label(description_window, image=img)
            image_label.image = img  # To prevent garbage collection
            image_label.pack(padx=20, pady=20)

        home_button = tk.Button(description_window, text="Home", command=go_home, font=("Courier", 14))
        home_button.pack(pady=10)
        description_window.bind("<Escape>", on_escape)

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
    img = img.resize((100, 100), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)
    logo_label = tk.Label(main_window, image=img, bg="black")
    logo_label.image = img  # To prevent garbage collection
    logo_label.pack(side=tk.RIGHT, padx=20, pady=20)

    main_window.bind("<Escape>", on_escape)

    main_window.mainloop()

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

#prev_name = None  # Variable to store the previous name
# folder_name = "c:\Users\SSP\Desktop\Face-Detection-main"
# audio_file = '\unknown.mp3'
# audio_path = os.path.join(folder_name , audio_file)

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        # Speak the name only if it's different from the previous name
        
        if name != "Unknown":
            speak_name()
            create_window(name)
            #prev_name = name
        else:
            speak_unknown_name()
            #subprocess.run(['unknown.mp3', audio_path])
            
            window_unknown()           #This is :
               
        # if name != "Unknown":
        #     speak_name(name)
        #     create_window(name)
        # else:
        #     window_unknown()
        # prev_name = name


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 13:
        break

cap.release()
cv2.destroyAllWindows()
















