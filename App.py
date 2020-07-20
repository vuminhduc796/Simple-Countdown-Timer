import tkinter as tk
import time
from tkinter import *

from threading import Thread

class PopUp(object):
    def __init__(self,master):
        self.task = None
        top = self.top = Toplevel(master)
        self.l = Label(top, text="Enter Task", padx=64, pady=20,fg = "#381310", bg="#de9e99",font=("Comic Sans MS",25,"bold")).grid(row=0,column=0,columnspan=6)
        self.l1 = Label(top, text="Task Name", padx=30, pady=10,fg = "#473433", bg="#bfadac", font=("Comic Sans MS", 15)).grid(row=1, column=0,columnspan=3)
        self.l2 = Label(top, text="Duration",padx=30, pady=10,fg = "#473433", bg="#bfadac", font=("Comic Sans MS", 15)).grid(row=1, column=3,columnspan=3)
        self.entry_name = Entry(top,font=("Calibri 12"))
        self.entry_name.grid(row=3,column=0,columnspan=3)
        self.entry_hour = Entry(top,width = 2,font=("Calibri 12"))
        self.entry_hour.insert(END, "00")
        self.entry_min = Entry(top,width = 2,font=("Calibri 12"))
        self.entry_min.insert(END, "00")
        self.entry_sec = Entry(top,width = 2,font=("Calibri 12"))
        self.entry_sec.insert(END, "00")

        self.photo_down = PhotoImage(file="down.png")
        self.photo_up = PhotoImage(file = "up.png")
        self.up1 = Button(top, image = self.photo_up,height = 10, width = 10,command=lambda: self.increase("hour")).grid(row=2, column=3,pady =5)
        self.up2 = Button(top, image= self.photo_up,height = 10, width = 10,command=lambda: self.increase("min")).grid(row=2, column=4,pady =5)
        self.up3 = Button(top, image= self.photo_up,height = 10, width = 10,command=lambda: self.increase("sec")).grid(row=2, column=5,pady =5)
        self.entry_hour.grid(row=3,column=3,padx=5)
        self.entry_min.grid(row=3, column=4,padx=5)
        self.entry_sec.grid(row=3, column=5,padx=5)
        self.down1 = Button(top, image=self.photo_down,height = 10, width = 10,command=lambda: self.decrease("hour")).grid(row=4, column=3,pady =5)
        self.down2 = Button(top, image=self.photo_down,height = 10, width = 10,command=lambda: self.decrease("min")).grid(row=4, column=4,pady =5)
        self.down3 = Button(top, image=self.photo_down,height = 10, width = 10,command=lambda: self.decrease("sec")).grid(row=4, column=5,pady =5)

        self.b = Button(top, text='Save', padx=20, pady=5,bg="#bfadac",command=self.cleanup).grid(row=6,column=0,columnspan=6, pady =5)

    def increase(self,type):
        if type == "hour":
            if int(self.entry_hour.get()) >= 23:
                new_val = "00"
            else:
                new_val = str(int(self.entry_hour.get()) + 1)
            self.entry_hour.delete(0, END)
            self.entry_hour.insert(0, new_val)
        elif type == "min":
            if int(self.entry_min.get()) >= 59:
                new_val = "00"
            else:
                new_val = str(int(self.entry_min.get()) + 1)
            self.entry_min.delete(0, END)
            self.entry_min.insert(0, new_val)
        elif type == "sec":
            if int(self.entry_sec.get()) >= 59:
                new_val = "00"
            else:
                new_val = str(int(self.entry_sec.get()) + 1)
            self.entry_sec.delete(0, END)
            self.entry_sec.insert(0, new_val)
    def decrease(self,type):
        if type == "hour":
            if int(self.entry_hour.get()) <= 0:
                new_val = "59"
            else:
                new_val = str(int(self.entry_hour.get()) - 1)
            self.entry_hour.delete(0, END)
            self.entry_hour.insert(0, new_val)
        elif type == "min":
            if int(self.entry_min.get()) <= 0:
                new_val = "59"
            else:
                new_val = str(int(self.entry_min.get()) - 1)
            self.entry_min.delete(0, END)
            self.entry_min.insert(0, new_val)
        elif type == "sec":
            if int(self.entry_sec.get()) <= 0:
                new_val = "59"
            else:
                new_val = str(int(self.entry_sec.get()) - 1)
            self.entry_sec.delete(0, END)
            self.entry_sec.insert(0, new_val)
    def cleanup(self):
        entry_time= [self.entry_hour.get(),self.entry_min.get(),self.entry_sec.get()]
        self.task = Task(self.entry_name.get(), entry_time)
        self.top.destroy()

class Task:
    def __init__(self,name,duration):
        self.name = name
        self.duration = duration
        self.running = False

    def decrease_time(self):
        self.duration = str(int(self.duration) - 1)


class CountDown:
    def __init__(self):
        self.task_list =[]
        self.remove_img = PhotoImage(file="remove.png")
        thread = Thread(target=self.update, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution
    def add_task(self,task):
        self.task_list.append(task)
        task_name = Label(root, text=task.name,fg = "#381310", bg="#de9e99",font=("Comic Sans MS",15))
        task_name.grid(row=len(self.task_list), column=0, pady = 5,padx = 10)
        task_name.bind("<Button-1>", lambda e: self.clock_trigger(self.task_list.index(task)))
        duration = Label(root, text=task.duration[0]+" : "+task.duration[1]+" : "+task.duration[2],fg = "#381310", bg="#de9e99",font=("Comic Sans MS",15))
        duration.grid(row=len(self.task_list), column=1, pady = 5)
        remove = Button(root, image=self.remove_img,height = 20, width = 20,command=lambda: self.remove(task))
        remove.grid(row=len(self.task_list),column = 2, padx= 10)


    def edit(self):
    
        return
    def clock_trigger(self,index):

        self.task_list[index].running = not self.task_list[index].running

    def update(self):
        while 1:

            time.sleep(1)
            for index in range(len(self.task_list)):
                if self.task_list[index].running:
                    self.decrement(index)

    def decrement(self,index):
        current = self.task_list[index].duration

        if (current[2] == 0 or current[2] == "00") and current[1] != 0 and current[1] != "00":
            new_duration = [current[0],int(current[1]) -1, 59]
        elif (current[1] == 0 or current[1] == "00") and current[0] != 0 and current[0] != "00" and (current[2] == 0 or current[2] == "00") :
            new_duration = [int(current[0]) -1 ,59, 59]
        elif (current[1] == 0 or current[1] == "00") and (current[2] == 0 or current[2] == "00") and (current[0] == 0 or current[0] == "00"):
            new_duration = []
        else:
            new_duration = [current[0],current[1],int(current[2]) - 1]
        self.task_list[index].duration = new_duration

        duration = Label(root, text=str(new_duration[0])+" : "+str(new_duration[1])+" : "+str(new_duration[2]),fg = "#381310", bg="#de9e99",font=("Comic Sans MS",15))
        duration.grid(row=index + 1, column=1)

    def remove(self,task):
        task.running = False
        for label in root.grid_slaves():
            if int(label.grid_info()["row"])  == self.task_list.index(task)+1:
                label.grid_forget()


class main(object):
    def __init__(self,master):
        self.countdown = CountDown()
        self.master = master
        self.addButton = Button(master, text="Add Task", padx=40, pady=20, command=self.call_popup)
        self.addButton.grid(row=0, column=0)
        self.renderButton = Button(master, text="Render", padx=40, pady=20, command=self.countdown.edit)
        self.renderButton.grid(row=0, column=1)

    def call_popup(self):
        popup = PopUp(self.master)
        self.master.wait_window(popup.top)
        if popup.task.name != "" and popup.task.duration != "":
            self.countdown.add_task(popup.task)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Countdown App")

    m=main(root)
    root.mainloop()



