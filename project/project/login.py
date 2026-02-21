import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow

window = tkinter.Tk()
window.title("Login form")
window.geometry('1100x440')
window.configure(bg='#333333')

# Load background image using Pillow
bg_image_path = "images/login.jpg"  # Replace with your image file path
bg_image = Image.open(bg_image_path)  # Open the image
bg_image = bg_image.resize((1100, 440),)  # Resize to match window dimensions
bg_photo = ImageTk.PhotoImage(bg_image)  # Convert to PhotoImage

bg_label = tkinter.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Set the label to cover the entire window

def login():
    username = "harshu"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#333333')
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame on the screen

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

window.mainloop()
