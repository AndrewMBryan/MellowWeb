import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.calendarframe import CalendarFrame
from pygubu.widgets.editabletreeview import EditableTreeview
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
import pathlib


class HelloworldApp:
    def __init__(self, master=None):

        # MAIN FRAME 1
        self.main = ttk.Frame(master)
        self.mainframe = ttk.Frame(self.main)

        # SET UP FRAME - PARENT = mainframe, Level 2
        self.setupFrame = tk.Frame(self.mainframe)

        # CalendarPicker - PARENT = setupFrame, level 3
        self.calendarPicker = CalendarFrame(self.setupFrame)
        self.calendarPicker.grid(column='1',
                                 row='1')

        # inner_setupFrame - Parent = setupFrame, level 3
        self.inner_setupFrame = ttk.Frame(self.setupFrame)

        # TIME LABEL - PARENT = setupFrame, LEVEL 4
        self.time_label = ttk.Label(self.inner_setupFrame)
        self.time_label.configure(cursor='arrow', takefocus=False, text='Time 24h: ')
        self.time_label.grid(column='0', row='0')

        # Time Spinbox - PARENT = setupFrame, LEVEL 4
        self.Time = ttk.Spinbox(self.inner_setupFrame, from_=0, to=24)
        self.Time.configure(cursor='arrow', font='TkDefaultFont', increment='1', takefocus=True)
        _text_ = '''Time Picker'''
        self.Time.delete('0', 'end')
        self.Time.insert('0', _text_)
        self.Time.grid(column='1', row='0')

        
        self.inner_setupFrame.configure(height='200', width='200')
        self.inner_setupFrame.grid(column='1', row='2')

        # SUBMIT BUTTON
        self.submitButton = ttk.Button(self.setupFrame, command=lambda: [self.submitBC()])
        self.submitButton.configure(style='Toolbutton', text='Submit')
        self.submitButton.grid(column='1', pady='30', row='3', sticky='s')

        self.setupFrame.configure(background='#ffffff', borderwidth='5', height='0', highlightcolor='#ffffff')
        self.setupFrame.configure(width='0')
        self.setupFrame.grid(column='1', padx='30', row='1')

        # POST FRAME
        self.postFrame = tk.Frame(self.mainframe)
        self.postTitle = ttk.Label(self.postFrame)
        self.postTitle.configure(text='Post Title')
        self.postTitle.pack(side='top')
        self.titleEntry = ttk.Entry(self.postFrame)
        self.titleEntry.configure(exportselection='true', font='TkDefaultFont', justify='left', state='normal')
        self.titleEntry.pack(expand='false', fill='x', side='top')
        self.descriptionLabel = ttk.Label(self.postFrame)
        self.descriptionLabel.configure(text='Description')
        self.descriptionLabel.pack(side='top')
        self.descriptionText = tk.Text(self.postFrame)
        self.descriptionText.configure(font='TkDefaultFont', height='10', relief='raised',
                                       setgrid='false')
        self.descriptionText.configure(takefocus=False, width='50')
        self.descriptionText.pack(ipadx='0', ipady='0', padx='0', pady='0', side='top')
        self.frame2 = ttk.Frame(self.postFrame)

        # UPLOAD BUTTON
        self.uploadButton = ttk.Button(self.frame2, command=lambda: [self.uploadBC()])
        self.uploadButton.configure(text='Upload Photo')
        self.uploadButton.pack(side='top')
        self.frame2.configure(height='200', width='200')
        self.frame2.pack()
        self.postFrame.configure(height='200', width='200')
        self.postFrame.grid(column='2', padx='10', row='1')

        # CANVAS IMAGE
        img_pil = Image.open('../MellowFlowApp/upload.png')
        width, height = img_pil.size
        print(width, height)
        self.imgTK = ImageTk.PhotoImage(img_pil)

        self.uploadCanvas = tk.Canvas(self.frame2, width=width, height=height)
        self.uploadCanvas.pack()
        self.uploadCanvas.create_image(width // 200, height // 200, image=self.imgTK, anchor=tk.NW)

        # imgTK = tk.PhotoImage(imgPIL)
        # startimg = tk.PhotoImage(file=imgTK)
        # self.imgArea = self.uploadCanvas.create_image((0,0), image=startimg)
        # self.uploadCanvas.pack(padx='10', pady='10', side='top', expand=tk.YES, fill=tk.BOTH)
        # self.uploadCanvas.config(width=imgTK.width(), height=imgTK.height())

        # VIEW FRAME
        self.viewFrame = tk.Frame(self.mainframe)
        self.eventsList = EditableTreeview(self.viewFrame)
        self.eventsList.pack(fill='y', side='top')
        self.viewFrame.configure(height='200', width='200')
        self.viewFrame.grid(column='3', padx='30', row='1')

        # LOGOUT BUTTON
        self.logoutButton = ttk.Button(self.mainframe, command=lambda: [self.logoutBC()])
        self.logoutButton.configure(text='Logout')
        self.logoutButton.grid(column='0', row='0')

        # FINISH MAN CONFIG
        self.mainframe.configure(relief='raised')
        self.mainframe.pack()
        self.main.configure(height='200', width='200')
        self.main.pack(side='top')

        # Main widget
        self.mainwindow = self.main

    def run(self):
        self.mainwindow.mainloop()

    def popUp(self, text):
        popup = tk.Tk()
        popup.wm_title()
        label = ttk.Label(popup, text=text)
        label.pack()
        exit = ttk.Button(popup, text="Confirm", command=popup.destroy)
        exit.pack()
        popup.mainloop()

    # BUTTON CLICKS
    def submitBC(self, event=None):
        try:
            preDate = str(self.calendarPicker.selection.date())
        except:
            self.popUp("No Date Selected")
            print("No Date Picked")
            return
        print("Date Confirmed")
        date = preDate.split('-')
        year = date[0]
        month = date[1]
        day = date[2]
        print(month, day, year)

        try:
            time = float(self.Time.get()).__round__(2)
        except:
            print("Time Failed")
            self.popUp("Please Fix Time Input")
            return
        print(time)

    def logoutBC(self, event=None):
        print("Logout Click")

    def uploadBC(self, event=None):
        print("Upload Click")
        # filepath = self.getFile()
        filepath = askopenfilename(
            parent=self.frame2,
            filetypes=[("Images", "*.*"), ("All Files", "*.*")]
        )
        img_pil = Image.open(filepath)
        width, height = img_pil.size
        print(width, height)
        self.imgTK = ImageTk.PhotoImage(img_pil)
        self.uploadCanvas.destroy()
        self.uploadCanvas = tk.Canvas(self.frame2, width=width, height=height)
        # self.uploadCanvas.itemconfig(image=img)
        self.uploadCanvas.create_image(width // 200, height // 200, image=self.imgTK, anchor=tk.NW)
        self.uploadCanvas.pack()

        # self.uploadCanvas = tk.Canvas(self.frame2, width=width, height=height, bg='yellow')

    # Failed Attempt to getFile
    # def getFile(self) -> str:
    #     """Open a file for editing."""
    #     filepath = askopenfilename(
    #         filetypes=[("Text Files", "*.png"), ("All Files", "*.*")]
    #     )
    #     print(filepath)
    #     if not filepath:
    #         return ""
    #     return filepath


if __name__ == '__main__':
    import tkinter as tk

    root = tk.Tk()
    app = HelloworldApp(root)
    app.run()
