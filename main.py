from tkinter import *
import mysql.connector

###----- DATABASE CONNECTION -----###
db = mysql.connector.connect(host ="localhost", user="root", password="12345", db="college")

# Cursor is used fetch data row by row
cursor = db.cursor()

###----- DATABASE OPERATIONS -----###
add_student_query = ("INSERT INTO students "
               "(studID, FirstName, LastName, Age) "
               "VALUES (%(studID)s, %(firstName)s, %(lastName)s, %(age)s)")

show_all_students_query = ("SELECT * FROM students")

delete_student_query = ("DELETE FROM students WHERE StudID=%(studID)s")

# delete_all_students_query = ("DELETE * FROM students")
delete_all_students_query = ("TRUNCATE TABLE students;")

###----- HELPER FUNCTIONS -----###

# Function To Raise The Chosen Frame
def show_frame(frame):
    frame.tkraise()

# ADDING STUDENT TO TABLE(add_to_table_button functionality)
# This function executes when add student button is pressed on the add_student_screen
def add_stud_to_table():
    # We are using get() function on the respective Entry Box variable to get the data
    studID = int(studIDEntry.get())
    firstName = firstNameEntry.get()
    lastName = lastNameEntry.get()
    age = int(ageEntry.get())

    # This structure is required to store data into SQL (dictionary format)
    student_data = {
    'studID': studID,
    'firstName': firstName,
    'lastName': lastName,
    'age': age,
    }

    cursor.execute(add_student_query, student_data)
    db.commit()

    # show_frame(HomeScreen)

def delete_single_student():
    studentID = int(studentIDEntry.get())

    student_detail = {
        'studID': studentID,
    }

    cursor.execute(delete_student_query, student_detail)
    db.commit()

def delete_all_students():
    cursor.execute(delete_all_students_query)
    db.commit()

# SHOWING ALL STUDENTS
def show_students():
    show_frame(show_student_screen)

    cursor.execute(show_all_students_query)
    
    # fetchall() function is used to store the retrieved data from SQL query into a variable
    students = cursor.fetchall()
    print(students)

    const_txt = "ID" + "  " + "First Name" + "\t" + "Last Name" + " " + "Age"
    txt_label = Label(show_student_screen, font =("Courier New", 8,"bold"), text=const_txt, pady=25)
    txt_label.place(x=80, y=5)

    disty = 60;

    for x in range(0, len(students)):
       studID = students[x][0]
       firstName = students[x][1]
       lastName = students[x][2]
       age = students[x][3]

       username_to_load_label = Label(show_student_screen, font =("Courier New", 8,"bold"), text=str(studID), pady=10)
       username_to_load_label.place(x=80, y=disty)

       userscore_to_load_label = Label(show_student_screen, font =("Courier New", 8,"bold"), text=firstName, pady=10)
       userscore_to_load_label.place(x=120, y=disty)

       userscore_to_load_label = Label(show_student_screen, font =("Courier New", 8,"bold"), text=lastName, pady=10)
       userscore_to_load_label.place(x=200, y=disty)

       userscore_to_load_label = Label(show_student_screen, font =("Courier New", 8,"bold"), text=str(age), pady=10)
       userscore_to_load_label.place(x=260, y=disty)

       disty += 40

# GUI INITIALIZAION
window = Tk()
# GUI SIZE DECLARATION
window.geometry("600x300")

window.title(" Admission Management System")

# INITIALIZE 1st row and 1st column to top left pixel of GUI Screen
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# INITIALIZE FRAMES FOR OUR GUI
HomeScreen = Frame(window)
add_student_screen = Frame(window)
show_student_screen = Frame(window)
delete_student_screen = Frame(window)
frame5 = Frame(window)

# INITIALIZE 1st row and 1st column FOR ALL FRAMES to top left pixel of GUI Screen
for frame in (HomeScreen, add_student_screen, show_student_screen, delete_student_screen, frame5):
    frame.grid(row=0,column=0,sticky='nsew')

                ###----- SCREENS -----###

                 #--- HOME SCREEN ---#
# FUNCTION TO IMPORT IMAGE
exit_btn = PhotoImage(file='images/exit.png')
# Button: Function to define button on GUI, Parameters(Frame, )
exit_button = Button(HomeScreen, image=exit_btn, cursor = "hand2", borderwidth=0, bg="#F0F0F0", command=window.destroy)
# exit_button = Button(HomeScreen, text="EXIT", cursor = "hand2", borderwidth=0, bg="#F0F0F0", command=window.destroy)
# pack(): used for placing the button on gui screen. padx, pady is padding(spacing), anchor-North-East 
exit_button.pack(padx=10, pady=10, anchor="ne")

add_button = Button(HomeScreen, text="Add Student", command=lambda:show_frame(add_student_screen))
add_button.pack(side="top", pady=20)

delete_button = Button(HomeScreen, text="Delete Student", command=lambda:show_frame(delete_student_screen))
delete_button.pack(side="top", pady=20)

show_student_button = Button(HomeScreen, text="Show Students", command=show_students)
show_student_button.pack(side="top", pady=20)


               #--- ADD STUDENT SCREEN ---#

exit_button = Button(add_student_screen, image=exit_btn, cursor = "hand2", borderwidth=0, bg="#F0F0F0", command=lambda:show_frame(HomeScreen))
exit_button.pack(padx=10, pady=10, anchor="ne")

# Label Function(In-built): Used to add text on GUI
lblfrstrow = Label(add_student_screen, text ="Student ID -", )
lblfrstrow.place(x = 180, y = 20)
# Entry Function(In-built): Used to take input from user
studIDEntry = Entry(add_student_screen, width = 35)
studIDEntry.place(x = 250, y = 20, width = 100)

lblscndrow = Label(add_student_screen, text ="FirsName -", )
lblscndrow.place(x = 180, y = 60)
firstNameEntry = Entry(add_student_screen, width = 35)
firstNameEntry.place(x = 250, y = 60, width = 100)

lblthrdrow = Label(add_student_screen, text ="LastName -", )
lblthrdrow.place(x = 180, y = 100)
lastNameEntry = Entry(add_student_screen, width = 35)
lastNameEntry.place(x = 250, y = 100, width = 100)

lblfrthrow = Label(add_student_screen, text ="Age -", )
lblfrthrow.place(x = 200, y = 140)
ageEntry = Entry(add_student_screen, width = 35)
ageEntry.place(x = 250, y = 140, width = 100)

add_to_table_button = Button(add_student_screen, text="Add Student", command=add_stud_to_table)
add_to_table_button.pack(side="bottom", pady=100)


               #--- SHOW STUDENTS SCREEN ---#
exit_button = Button(show_student_screen, image=exit_btn, cursor = "hand2", borderwidth=0, bg="#F0F0F0", command=lambda:show_frame(HomeScreen))
exit_button.pack(padx=10, pady=10, anchor="ne")

               #--- DELETE STUDENT SCREEN ---#

exit_button = Button(delete_student_screen, image=exit_btn, cursor = "hand2", borderwidth=0, bg="#F0F0F0", command=lambda:show_frame(HomeScreen))
exit_button.pack(padx=10, pady=10, anchor="ne")

delInfoLabel = Label(delete_student_screen, text ="Enter Student ID to Delete", )
delInfoLabel.place(x = 230, y = 20)
delLabel = Label(delete_student_screen, text ="ID -", )
delLabel.place(x = 220, y = 60)
studentIDEntry = Entry(delete_student_screen, width = 35)
studentIDEntry.place(x = 250, y = 60, width = 100)

delete_submit_button = Button(delete_student_screen, text="Delete Student", command=delete_single_student)
delete_submit_button.pack(side="top", pady=(100, 0))

delete_all_button = Button(delete_student_screen, text="Delete All Student", command=delete_all_students)
delete_all_button.pack(side="top", pady=(50, 0))

# CODE EXECUTION BEGINS HERE
show_frame(HomeScreen)

# mainloop(): inbuilt funtion - keeps running our GUI.
window.mainloop()

cursor.close()

db.close()