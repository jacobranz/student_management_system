import sys
import subprocess
from Tkinter import *
from ttk import *
import tkMessageBox

print("Attempting to detect any pending reboots...")

cmd_result = "Reboot is probably not necessary."

if cmd_result == "Reboot is probably not necessary.":
    print("Reboot detected")
    
    window = Tk()
    window.title("Reboot Prompt")
    window.geometry('210x260')
    
    label0 = Label(window, text = "This machine has pending reboots!", font = ('Calibri', 10, 'bold', 'underline'))
    label0.grid(row = 0, column = 6, pady = 20)
    
    label1 = Label(window, text = "View reboot info here...")
    label1.grid(row =1, column = 6)
    
    label2 = Label(window, text = "Reboot system (Now)")
    label1.grid(row =3, column = 6)
    
    label3 = Label(window, text = "Snooze (30 minutes)")
    label1.grid(row =5, column = 6)
    
    def disable_event():
        pass
    
    def clicked_info():
        tkMessageBox.showinfo("Pending rbeoots detected!", "This system has pending reboots")
        
    def clicked_reboot():
        prompt = tkMessageBox.askquestion(title = "Reboot now?", message = "Do you wish to reboot?")
        if prompt == 'yes':
            subprocess.check_output("systemctl reboot now", shell=True)
        else:
            prompt = tkMessageBox.showwarning("Warning!", "You will be prompted to reboot your machine every 30 minutes until you reboot!")
            window.quit()
            
    def clicked_snooze():
        prompt = tkMessageBox.showwarning("Warning!", "You will be prompted to reboot your machine every 30 minutes until you reboot!")
        window.quit()
        
    style = Style()
    style.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = blue)
    style.configure('A.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = green)
    style.configure('B.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = red)
    
    btn = Button(window, text = "Notification Info", command = clicked_info(), style = 'W.TButton')
    btn.grid(row = 2, column = 6, padx = 55, pady = 10)
    btn = Button(window, text = "Reboot", command = clicked_reboot(), style = 'A.TButton')
    btn.grid(row = 4, column = 6, padx = 55, pady = 10)
    btn = Button(window, text = "Snooze", command = clicked_snooze(), style = 'B.TButton')
    btn.grid(row = 6, column = 6, padx = 55, pady = 10)
    
    window.attributes('-topmost', True)
    window.protocol("WM_DELETE_WINDOW", disable_event())
    window.mainloop()
    
else:
    print("No reboot necessary")
    sys.exit(1)