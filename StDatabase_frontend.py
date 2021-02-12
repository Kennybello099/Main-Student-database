from tkinter import*
import tkinter.messagebox
from tkinter import Tk
import st_database

class Student(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.studentID = StringVar()
        self.student_fname = StringVar()
        self.student_surname = StringVar()
        self.student_gender = StringVar()
        self.student_age = StringVar()
        self.studentphone_no = StringVar()
        self.student_dateofbirth = StringVar()
        self.student_address = StringVar()



# =====================================frame  ====================================================================

        self.MainFrame = Frame(self, bg="cadet blue")
        self.MainFrame.grid()

        self.TitleFrame = Frame(self.MainFrame, bd=2, padx=54, pady=8, bg='Ghost White', relief=RIDGE)
        self.TitleFrame.pack(side=TOP)

        self.lblTitle = Label(self.TitleFrame, font=('arial', 47, 'bold'), text="Student Database Management System",
                              bg="Ghost White")
        self.lblTitle.grid()

        self.ButtonFrame = Frame(self.MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg='Ghost white',
                                 relief=RIDGE)
        self.ButtonFrame.pack(side=BOTTOM)

        self.DataFrame = Frame(self.MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,
                               bg='cadet blue')
        self.DataFrame.pack(side=BOTTOM)

        self.DataFrameLeft = LabelFrame(self.DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE,
                                        bg='Ghost White', font=('arial', 20, 'bold'), text='Student Info\n')
        self.DataFrameLeft.pack(side=LEFT)

        self.DataFrameright = LabelFrame(self.DataFrame, bd=1, width=450, height=300, padx=20, relief=RIDGE,
                                        bg='Ghost White', font=('arial', 20, 'bold'), text='Student Details\n')
        self.DataFrameright.pack(side=RIGHT)

# =====================================Labels and Entry Widget  ========================================================

        self.LblStudentID = Label(self.DataFrameLeft, font=('arial', 20, 'bold'), text='Student ID:', padx=2, pady=2,
                                  bg='Ghost White')
        self.LblStudentID.grid(row=0, column=0, sticky=W)
        self.txtStudentID = Entry(self.DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.studentID, width=39)
        self.txtStudentID.grid(row=0, column=1)

        self.LblFirstname = Label(self.DataFrameLeft, font=('arial', 20, 'bold'), text='First name:', padx=2, pady=2,
                                  bg='Ghost White')
        self.LblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(self.DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.student_fname,
                                  width=39)
        self.txtFirstname.grid(row=1, column=1)

        self.LblSurname = Label(self.DataFrameLeft, font=('arial', 20, 'bold'), text='Surname:', padx=2, pady=2,
                                  bg='Ghost White')
        self.LblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(self.DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.student_surname,
                                  width=39)
        self.txtSurname.grid(row=2, column=1)


        self.LblGender = Label(self.DataFrameLeft, font=('arial', 20, 'bold'), text='Gender:', padx=2, pady=2,
                                bg='Ghost White')
        self.LblGender.grid(row=3, column=0, sticky=W)
        self.txtGender = Entry(self.DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.student_gender,
                                width=39)
        self.txtGender.grid(row=3, column=1)

        self.LblAge = Label(self.DataFrameLeft, font=('arial', 20, 'bold'), text='Age:', padx=2, pady=2,
                               bg='Ghost White')
        self.LblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(self.DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.student_age,
                               width=39)
        self.txtAge.grid(row=4, column=1)

        self.LblPhone_no = Label(self.DataFrameLeft, font=('arial', 20, 'bold'), text='Phone_no:', padx=2, pady=2,
                                 bg='Ghost White')
        self.LblPhone_no.grid(row=5, column=0, sticky=W)
        self.txtPhone_no = Entry(self.DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.studentphone_no,
                                 width=39)
        self.txtPhone_no.grid(row=5, column=1)

        self.LblStudent_dateofbirth = Label(self.DataFrameLeft, font=('arial', 20, 'bold'), text='Date of birth:', padx=2,
                                        pady=2,
                                        bg='Ghost White')
        self.LblStudent_dateofbirth.grid(row=6, column=0, sticky=W)
        self.txtStudent_dateofbirth = Entry(self.DataFrameLeft, font=('arial', 20, 'bold'),
                                        textvariable=self.student_dateofbirth,
                                        width=39)
        self.txtStudent_dateofbirth.grid(row=6, column=1)

        self.LblStudent_address = Label(self.DataFrameLeft, font=('arial', 20, 'bold'), text='Address:',
                                            padx=2,
                                            pady=2,
                                            bg='Ghost White')
        self.LblStudent_address.grid(row=7, column=0, sticky=W)
        self.txtStudent_address = Entry(self.DataFrameLeft, font=('arial', 20, 'bold'),
                                            textvariable=self.student_address,
                                            width=39)
        self.txtStudent_address.grid(row=7, column=1)

# =====================================ListBox and scrollbar widget ==================================================


        self.scrollbar = Scrollbar(self.DataFrameright)

        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.studentlist = Listbox(self.DataFrameright, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=self.scrollbar.set)
        self.studentlist.bind_all('<<ListboxSelection>>', self.StudentRec)
        self.studentlist.grid(row=0, column=0, padx=8)
        self.scrollbar.config(command=self.studentlist.yview)


        # =====================================Button Widget =================================================================
        self.btnAdd = Button(self.ButtonFrame, text='Add New', font=('arial', 20, 'bold'),command=self.Adddata,
                             height=1, width=10, bd=4)
        self.btnAdd.grid(row=0, column=0)

        self.btnDisplay = Button(self.ButtonFrame, text='Display', font =('arial', 20, 'bold'), command=self.Displaydata,
                                 height=1, width=10, bd=4)
        self.btnDisplay.grid(row=0, column=1)

        self.btnClear = Button(self.ButtonFrame, text='Clear', font=('arial', 20, 'bold'), command=self.Cleardata,
                               height=1, width=10, bd=4)
        self.btnClear.grid(row=0, column=2)

        self.btnDelete = Button(self.ButtonFrame, text='Delete', font=('arial', 20, 'bold'),command=self.Deletedata,
                                height=1, width=10, bd=4)
        self.btnDelete.grid(row=0, column=3)

        self.btnSearch = Button(self.ButtonFrame, text='Search', font=('arial', 20, 'bold'), command=self.Searchdata,
                                height=1, width=10, bd=4)
        self.btnSearch.grid(row=0, column=4)

        self.btnUpdate = Button(self.ButtonFrame, text='Update', font=('arial', 20, 'bold'), command=self.Updatedata,
                                height=1, width=10, bd=4)
        self.btnUpdate.grid(row=0, column=5)

        self.btnExit = Button(self.ButtonFrame, text='Exit', font=('arial', 20, 'bold'), command=self.iExit,
                              height=1, width=10, bd=4)
        self.btnExit.grid(row=0, column=6)


    # =============================================function==============================================================

    def iExit(self):
        iExit = tkinter.messagebox.askyesno('Student Database System', 'Do you want to exit?')
        if iExit > 0:
            root.destroy()

    def Cleardata(self):
        self.txtStudentID.delete(0, END)
        self.txtFirstname.delete(0, END)
        self.txtSurname.delete(0, END)
        self.txtGender.delete(0, END)
        self.txtAge.delete(0, END)
        self.txtPhone_no.delete(0, END)
        self.txtStudent_dateofbirth.delete(0, END)
        self.txtStudent_address.delete(0, END)


    def Adddata(self):
        studentID = self.studentID
        student_fname = self.student_fname
        student_surname = self.student_surname
        student_gender = self.student_gender
        student_age = self.student_age
        studentphone_no = self.studentphone_no
        student_dateofbirth = self.student_dateofbirth
        student_address = self.student_address

        if len(self.studentID.get()) != 0:
            st_database.AddRec(studentID.get(), student_fname.get(), student_surname.get(), student_gender.get(),
                               student_age.get(), studentphone_no.get(), student_dateofbirth.get(), student_address.get())
            self.studentlist.delete(0, END)
            self.studentlist.insert(END, studentID.get(), student_fname.get(), student_surname.get(),
                                    student_gender.get(), student_age.get(), studentphone_no.get(),
                                    student_dateofbirth.get(), student_address.get(),  str(""))

    def Displaydata(self):
        self.studentlist.delete(0, END)
        for j in st_database.DisplayRec():
            self.studentlist.insert(END, j, str(""))

    def StudentRec(self):
        global conn
        search_student = self.studentlist.curselection()[0]
        conn = self.studentlist.get(search_student)

        self.txtStudentID.delete(0, END)
        self.txtFirstname.delete(0, END)
        self.txtSurname.delete(0, END)
        self.txtGender.delete(0, END)
        self.txtAge.delete(0, END)
        self.txtPhone_no.delete(0, END)
        self.txtStudent_dateofbirth.delete(0, END)
        self.txtStudent_address.delete(0, END)

    def Deletedata(self):
        global conn

        search_student = self.studentlist.curselection()[0]
        conn = self.studentlist.get(search_student)

        self.txtStudentID.delete(0, END)
        self.txtStudentID.insert(END, conn[1])

        self.txtFirstname.delete(0, END)
        self.txtFirstname.insert(END, conn[2])

        self.txtSurname.delete(0, END)
        self.txtSurname.insert(END, conn[3])

        self.txtGender.delete(0, END)
        self.txtGender.insert(END, conn[4])

        self.txtAge.delete(0, END)
        self.txtAge.insert(END, conn[5])

        self.txtPhone_no.delete(0, END)
        self.txtPhone_no.insert(END, conn[6])

        self.txtStudent_dateofbirth.delete(0, END)
        self.txtStudent_dateofbirth.insert(END, conn[7])

        self.txtStudent_address.delete(0, END)
        self.txtStudent_address.insert(END, conn[8])

        if len(self.studentID.get()) != 0:
            self.studentlist.delete(0, END)
            st_database.deleteRec(conn[0])
            self.Cleardata()
            self.Displaydata()

    def Searchdata(self):
        studentID = self.studentID
        student_fname = self.student_fname
        student_surname = self.student_surname
        student_gender = self.student_gender
        studentphone_no = self.studentphone_no
        student_address = self.student_address
        student_dateofbirth = self.student_dateofbirth
        student_age = self.student_age

        self.studentlist.delete(0, END)
        for row in st_database.searchRec(studentID.get(), student_fname.get(), student_surname.get(), student_gender.get(),
                                         studentphone_no.get(), student_address.get(), student_dateofbirth.get(),
                                         student_age.get()):
            self.studentlist.insert(END, row, str(""))


    def Updatedata(self):
        if len(self.studentID.get()) != 0:
            st_database.deleteRec(self.studentID.get())
        if len(self.studentID.get()) != 0:
            st_database.AddRec(self.studentID.get(), self.student_fname.get(), self.student_surname.get(),
                               self.student_gender.get(), self.studentphone_no.get(), self.student_address.get(),
                               self.student_dateofbirth.get(), self.student_age.get())
            self.studentlist.delete(0, END)
            self.studentlist.insert(END, (self.studentID.get(), self.student_fname.get(), self.student_surname.get(),
                                          self.student_gender.get(), self.studentphone_no.get(),
                                          self.student_address.get(), self.student_dateofbirth.get(),
                                          self.student_age.get()))



if __name__ == '__main__':
    root = Tk()
    root.title('Student Database Management System')
    root.geometry('1350x750+0+0')
    myapp = Student(root)
    myapp.mainloop()



