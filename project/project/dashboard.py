from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from course import courseClass
from student import StudentClass
from result import resultClass
from report import reportClass
import sqlite3
import os


# Login Class
def login_window():
    def login():
        username = "harshu"
        password = "12345"
        if username_entry.get() == username and password_entry.get() == password:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            login_root.destroy() 
            open_dashboard() 
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    login_root = Tk()
    login_root.title("Login Form")
    login_root.geometry("1100x440")
    login_root.configure(bg='#333333')

    frame = Frame(login_root, bg='#333333')
    frame.place(relx=0.5, rely=0.5, anchor="center")

    login_label = Label(frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
    username_label = Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    username_entry = Entry(frame, font=("Arial", 16))
    password_label = Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    password_entry = Entry(frame, show="*", font=("Arial", 16))
    login_button = Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    login_root.mainloop()


# Dashboard Class
def open_dashboard():
    class RMS:
        def __init__(self, root):
            self.root = root
            self.root.title("course and Student Management System - by harshada bedse")
            self.root.geometry("1350x700+0+0")
            self.root.config(bg="white")

            # Icons
            self.logo_dash = ImageTk.PhotoImage(file="project/images/logo.jpg")

            # Title
            title = Label(self.root, text=" course and Student Management System", padx=10, compound=LEFT,
                          image=self.logo_dash, font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
            title.place(x=0, y=0, relwidth=1, height=50)

            # Menu
            M_Frame = LabelFrame(self.root, text="Menus", font=("time new roman", 15), bg="white")
            M_Frame.place(x=10, y=70, width=1340, height=80)

            Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
            Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=240, y=5, width=200, height=40)
            Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=460, y=5, width=200, height=40)
            Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=680, y=5, width=200, height=40)
            Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.logout).place(x=900, y=5, width=200, height=40)
            Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.exit).place(x=1120, y=5, width=200, height=40)

            # Content Window
            self.bg_img = Image.open("project/images/main.jpg")
            self.bg_img = self.bg_img.resize((920, 350))
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
            Label(self.root, image=self.bg_img).place(x=200, y=180, width=920, height=350)

            # Update Details
            self.lbl_course = Label(self.root, text="Total Course\n[0]", font=("goudy old style", 20), bd=10,
                                     relief=RIDGE, bg="#e43b06", fg="white")
            self.lbl_course.place(x=200, y=530, width=300, height=100)

            self.lbl_student = Label(self.root, text="Total Student\n[0]", font=("goudy old style", 20), bd=10,
                                      relief=RIDGE, bg="#0676ad", fg="white")
            self.lbl_student.place(x=510, y=530, width=300, height=100)

            self.lbl_result = Label(self.root, text="Total Result\n[0]", font=("goudy old style", 20), bd=10,
                                     relief=RIDGE, bg="#038074", fg="white")
            self.lbl_result.place(x=820, y=530, width=300, height=100)

            # Footer
            footer = Label(self.root, text="course and  Student Management System\nContact Us for any Technical Issue: 8788360663",
                           font=("goudy old style", 12), bg="#262626", fg="white")
            footer.pack(side=BOTTOM, fill=X)

            # Call update_details 
            self.update_details()

        def update_details(self):
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM course")
                courses = cur.fetchall()
                self.lbl_course.config(text=f"Total Course\n[{str(len(courses))}]")

                cur.execute("SELECT * FROM student")
                students = cur.fetchall()
                self.lbl_student.config(text=f"Total Student\n[{str(len(students))}]")

                cur.execute("SELECT * FROM result")
                results = cur.fetchall()
                self.lbl_result.config(text=f"Total Result\n[{str(len(results))}]")

                self.lbl_course.after(2000, self.update_details)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")
            finally:
                con.close()

    
        def add_course(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=courseClass(self.new_win)

        def add_student(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=StudentClass(self.new_win)

        def add_result(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=resultClass(self.new_win)

        def add_report(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=reportClass(self.new_win)  

        def logout(self):
            op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
            if op:
                self.root.destroy() 
                login_window()  


        def exit(self):
            if messagebox.askyesno("Confirm", "Do you really want to exit?", parent=self.root):
                self.root.destroy()

    root = Tk()
    obj = RMS(root)
    root.mainloop()


if __name__ == "__main__":
    login_window()
