# Python program to illustrate a stop watch
# using Tkinter
#importing the required libraries
import tkinter
import customtkinter
from datetime import timedelta
import os

os.system('cls')

counter = 300   #default timer starting with 00:05:00, that is 5min=300sec
running = False

def counter_label(label):
    def count():
        if running:
            global counter
   
            # To manage the initial delay.
            if counter==300:            
                display_label='00:05:00'
            else:
                display_label = "0"+str(timedelta(seconds=counter))
     
            label.configure(text=display_label)
            # Delays by 1000ms=1sec, and call count() again.
            label.after(1000, count) 
            counter -= 1
   
    # Triggering the start of the counter.
    count()     
   
# start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)
    start.configure(state='disabled')
    stop.configure(state='normal')
    reset.configure(state='normal')
   
# Stop function of the stopwatch
def Stop():
    global running
    start.configure(state='normal')
    stop.configure(state='disabled')
    reset.configure(state='normal')
    running = False
   
# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=300
   
    # If rest is pressed after pressing stop.
    if running==False:      
        reset.configure(state='disabled')
        label.configure(text='00:05:00')
   
    # If reset is pressed while the stopwatch is running.
    else:               
        label.configure(text='00:05:00')

################################
###### CustomTkinter code ######
################################

# Setting-up window theme-colour
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Setting up window-size
app_custom = customtkinter.CTk()  # create CTk window like you do with the Tk window
app_custom.geometry("400x240")
app_custom.title("Stopwatch")

# Setting-up Label
label = customtkinter.CTkLabel(master=app_custom, text="00:05:00", font=('Verdana', 30))
label.place(relx=0.52, rely=0.35, anchor=tkinter.CENTER)

# Setting-up Buttons
start = customtkinter.CTkButton(master=app_custom, text='Start', width=60, state='enabled', command=lambda: Start(label=label))
stop = customtkinter.CTkButton(master=app_custom, text='Stop', width=60, state='disabled', command=Stop)
reset = customtkinter.CTkButton(master=app_custom, text='Reset', width=60, state='disabled', command=lambda: Reset(label=label))

# Placing Buttons on Screen
start.place(relx=0.25, rely=0.6)
stop.place(relx=0.45, rely=0.6)
reset.place(relx=0.65, rely=0.6)

# Placing a TextBox on the screen to Enter a Countdown time
# entry = customtkinter.CTkEntry(master=app_custom, placeholder_text="Enter time to Countdown", width=50, height=2)
# entry.pack(padx=30, pady=10)


# Starting the app
app_custom.mainloop()