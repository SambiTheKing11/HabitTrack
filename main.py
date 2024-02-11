from tkinter import *
import customtkinter
from tkinter import PhotoImage  # Use Tkinter's PhotoImage for image handling
from PIL import Image, ImageTk



'''
            Log Jan 7, 2023
    Just starting using tkinter, cheers to a successful project! :)
    
        Log Jan 23, 2023
    Practicing with Tkinter, learned how to put widgets onto the window via pack or place as well as how to organize widgets using grid! ^_^
    
        Log Feb 4, 2023
    More practicing with Tkinter, learned how to make elements interactive with Tkinter.
    
        Log 10, 2023
    Creating the user interface for the homepage using customer Tkinter
'''


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


root = customtkinter.CTk()
root.geometry("500x500")


# Load the settings icon image
#settings_icon = PhotoImage(file='setting.png')  # Update the path to your image file

# Load and resize the settings icon image
original_image = Image.open('setting.png')  # Ensure the path to your image file is correct
# Use Image.Resampling.LANCZOS for high-quality downsampling in newer Pillow versions
resized_image = original_image.resize((20, 20), Image.Resampling.LANCZOS)
settings_icon = ImageTk.PhotoImage(resized_image)

# Create a button with the resized image, positioned at the top left with padding
settings_button = customtkinter.CTkButton(root, image=settings_icon, text="", width=30, height=30, corner_radius=10)
settings_button.pack(anchor='nw', padx=10, pady=10)


#SettingButton = customtkinter.CTkButton(master = root, text = "Settings")
#SettingButton.pack(anchor='nw', side='top')

frame = customtkinter.CTkScrollableFrame(master = root)
frame.pack(padx=20, pady=20, expand=True, fill='both')

#Putting in a checkbox for the main frame in the homepage
habitList = ['var1', 'var2', 'var3']

checkList = []

#Creating a checklist with unchecked states of each box.
for habit in habitList:
    booleanCheckHabit = customtkinter.BooleanVar(value = False)
    checkList.append(booleanCheckHabit)
    CheckBox  = customtkinter.CTkCheckBox(master = frame, text = habit, variable = booleanCheckHabit )
    CheckBox.pack(anchor = 'w')

#return the state of the checkbox via terminal
def get_checklist_states():
    for index, habit in enumerate(habitList):
     if checkList[index].get():
        state = 'Checked'
     else:
        state = 'Unchecked'
        print(f'{habit}: {state}')

state_of_button = customtkinter.CTkButton(master = root, text = "Check States", command = get_checklist_states)
state_of_button.pack(pady = 20)

#button = customtkinter.CTkButton(master = root, text = "Click me")

#button.place(relx=0.5, rely=0.5, anchor = CENTER)


root.mainloop()

"""class MyGUI:
    def __init__(self):
        self.root=tk.Tk()

        self.label=tk.Label(self.root, text = "Your Message", font = ('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font = ('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text = "Show MessageBox", font = ('Arial', 16), variable = self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text = "Show Message", font = ('Arial', 18), command = self.show_message)
        self.button.pack(padx=10, pady=10)

        #self.root.title("HabitTracker")

        self.root.mainloop()

    def show_message(self):
           if self.check_state.get() == 0:
               print(self.textbox.get('1.0', tk.END))
           else:
               messagebox.showinfo(title = "Message", message = self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        print(event.key)
        print(event.state)


MyGUI()
"""
#creates the window
#root = tk.Tk()

#root.geometry('500x500')

#root.title('HabitTracker')

#TKinter is all about widgets!!!

''' 

Tutorial on how to set up interface with TKinter

label = tk.Label(root, text = "Hello World!", font = ('Arial', '18'))
label.pack(padx = 20, pady = 20)

textbox = tk.Text(root, font = ('Arial', 16), height = 2, width = 50)
textbox.pack(padx = 10)

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight = 1)
buttonFrame.columnconfigure(1, weight = 1)
buttonFrame.columnconfigure(2, weight = 1)
buttonFrame.columnconfigure(3, weight = 1
buttonFrame.columnconfigure(4, weight = 1)

button1 = tk.Button(buttonFrame, text = "1", font = ('Arial', '18'))
button1.grid (row = 0, column = 0, sticky = tk.W + tk.E) #sticky makes sure the buttons stretch and comrpess in tandeum with the window

button2 = tk.Button(buttonFrame, text = "2", font = ('Arial', '18'))
button2.grid (row = 0, column = 1, sticky = tk.W + tk.E) #sticky makes sure the buttons stretch and comrpess in tandeum with the window

button3 = tk.Button(buttonFrame, text = "3", font = ('Arial', '18'))
button3.grid (row = 0, column = 2, sticky = tk.W + tk.E) #sticky makes sure the buttons stretch and comrpess in tandeum with the window

button4 = tk.Button(buttonFrame, text = "4", font = ('Arial', '18'))
button4.grid (row = 1, column = 0, sticky = tk.W + tk.E) #sticky makes sure the buttons stretch and comrpess in tandeum with the window

button5 = tk.Button(buttonFrame, text = "5", font = ('Arial', '18'))
button5.grid (row = 1, column = 1, sticky = tk.W + tk.E) #sticky makes sure the buttons stretch and comrpess in tandeum with the window

button6 = tk.Button(buttonFrame, text = "6", font = ('Arial', '18'))
button6.grid (row = 1, column = 2, sticky = tk.W + tk.E) #sticky makes sure the buttons stretch and comrpess in tandeum with the window

buttonFrame.pack(fill = 'x')

anotherBTN = tk.Button(buttonFrame, text = "YO")
anotherBTN.place (x=100, y=100, width = 100, height = 100) # use place over pack when you want a specific location u wanna put button on

'''





# Start the GUI event loop
#root.mainloop()
