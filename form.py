from tkinter import *

if __name__ == '__main__':
	root = Tk()
# Form Configuration
	root.configure(background='light blue')
	root.title('School Registration Form')
	root.geometry('500x300')
	heading = Label(root, text='Registration form', bg='light blue')

# Labels
	name = Label(root, text='Name', bg='light blue')
	course = Label(root, text='Course', bg='light blue')
	semester = Label(root, text='Semester', bg='light blue')
	phone_number = Label(root, text='Phone Number', bg='light blue')
	email_id = Label(root, text='Email', bg='light blue')
	home_address = Label(root, text='Home Address', bg='light blue')


# Grid location
	heading.grid(row=0, column=1)
	name.grid(row=1, column=0)
	course.grid(row=2, column=0)
	semester.grid(row=3, column=0)
	phone_number.grid(row=4, column=0)
	email_id.grid(row=5, column=0)
	home_address.grid(row=6, column=0)

# Input EntryPoint
	name_field = Entry(root)
	course_field = Entry(root)
	semester_field = Entry(root)
	phoneNumber_field = Entry(root)
	emailId_field = Entry(root)
	homeAddress_field = Entry(root)

# Grid for Input
	name_field.grid(row=1, column=1, ipadx='100')
	course_field.grid(row=2, column=1, ipadx='100')
	semester_field.grid(row=3, column=1, ipadx='100')
	phoneNumber_field.grid(row=4, column=1, ipadx='100')
	emailId_field.grid(row=5, column=1, ipadx='100')
	homeAddress_field.grid(row=6, column=1, ipadx='100')
	
# Submit Button
	submit = Button(root, text="Submit",fg='red', bg='light blue')
	submit.grid(row=8, column=1)

	root.mainloop()