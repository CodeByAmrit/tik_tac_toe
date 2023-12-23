from tkinter import * 
from tkinter import messagebox,filedialog

class game(Tk):
    def restart_gui(self):
        # Destroy Current Window
        self.checkClick = False
        self.destroy()
        # Recreate the initial GUI components
        self.__init__()
        
    def displayResult(self, player):
        messagebox.showinfo(player, str(player).upper() + " Win the game")
        # messagebox.OK()
        self.checkValues.clear()
        self.restart_gui()
        
        
    def CheckRules(self,frame):
        self.checkValues.clear()
        i = 1
        for widget in frame.winfo_children():
            text1 = widget.cget("text")
            if text1 == "":
                self.checkValues.append(str(i))
                i+=1
            else:
                
                self.checkValues.append(str(text1))
        if i == 1:
            self.checkClick = True
        
        print(self.checkValues)
        
            
        
        if self.checkValues[0] == self.checkValues[1] and self.checkValues[1] == self.checkValues[2]:
            self.displayResult(self.checkValues[1])
        elif self.checkValues[3] == self.checkValues[4] and self.checkValues[4] == self.checkValues[5]:
            self.displayResult(self.checkValues[4])
        elif self.checkValues[6] == self.checkValues[7] and self.checkValues[7] == self.checkValues[8]:
            self.displayResult(self.checkValues[7])
        elif self.checkValues[0] == self.checkValues[3] and self.checkValues[3] == self.checkValues[6]:
            self.displayResult(self.checkValues[3])
        elif self.checkValues[1] == self.checkValues[4] and self.checkValues[4] == self.checkValues[7]:
            self.displayResult(self.checkValues[4])
        elif self.checkValues[2] == self.checkValues[5] and self.checkValues[5] == self.checkValues[8]:
            self.displayResult(self.checkValues[5])
        elif self.checkValues[0] == self.checkValues[4] and self.checkValues[4] == self.checkValues[8]:
            self.displayResult(self.checkValues[4])
        elif self.checkValues[2] == self.checkValues[4] and self.checkValues[4] == self.checkValues[6]:
            self.displayResult(self.checkValues[4])
            
        if self.checkClick:
            self.restart_gui()

    def tick(self,btn):
        
        if self.playerX:
            btn.config(text="X")
            self.playerX = False
        else:
            btn.config(text="Y")
            self.playerX = True
            
        btn["state"] = "disabled"
        self.CheckRules(win.frame1)
        
    def open_file(self):
        file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            print(f"Selected file: {file_path}")
            
    def __init__(self):
        self.playerX = True
        self.checkValues = list()
        self.checkClick = False
        
        super().__init__()
        
        self.width = 400
        self.height = 500
        self.configure(bg="#2C3E50")
        self.title("Tic Tac Toe")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - self.width) // 2
        y_position = (screen_height - self.height) // 2

        self.geometry(f"{self.width}x{self.height}+{x_position}+{y_position}")

        self.heading = Frame(self, width=400, height=60,bg="#2C3E50")
        self.heading.pack()
        
        self.topLabel = Label(self.heading, text="Tic Tac Toe", font=("Calibri Bold", 30),bg="#2C3E50",fg="#39AEA9")
        self.topLabel.pack()
        
        self.frame1 = Frame(self, width=400, height=400,bg="#2C3E50")
        self.frame1.pack()
        
        # Create a menu bar
        menubar = Menu(self)
        self.config(menu=menubar)

        # Create a "File" menu
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        # Add "Open" button to the "File" menu
        file_menu.add_command(label="Open", command=self.open_file)

        # Add a separator
        file_menu.add_separator()

        # Add "Exit" button to the "File" menu
        file_menu.add_command(label="Exit", command=self.destroy)

    
        
        self.btn1 = Button(self.frame1, text='', width=3, height=1, bg="#A2D5AB", disabledforeground="white", command=lambda: self.tick(self.btn1),font=("Calibri", 40) )
        self.btn2 = Button(self.frame1, text='', width=3, height=1, bg="#A2D5AB", disabledforeground="white", command=lambda: self.tick(self.btn2),font=("Calibri", 40) )
        self.btn3 = Button(self.frame1, text='', width=3, height=1, bg="#A2D5AB", disabledforeground="white", command=lambda: self.tick(self.btn3),font=("Calibri", 40) )
        self.btn4 = Button(self.frame1, text='', width=3, height=1, bg="#A2D5AB", disabledforeground="white", command=lambda: self.tick(self.btn4),font=("Calibri", 40) )
        self.btn5 = Button(self.frame1, text='', width=3, height=1, bg="#A2D5AB", disabledforeground="white", command=lambda: self.tick(self.btn5),font=("Calibri", 40) )
        self.btn6 = Button(self.frame1, text='', width=3, height=1, bg="#A2D5AB", disabledforeground="white", command=lambda: self.tick(self.btn6),font=("Calibri", 40) )
        self.btn7 = Button(self.frame1, text='', width=3, height=1, bg="#A2D5AB", disabledforeground="white", command=lambda: self.tick(self.btn7),font=("Calibri", 40) )
        self.btn8 = Button(self.frame1, text='', width=3, height=1, bg="#A2D5AB", disabledforeground="white", command=lambda: self.tick(self.btn8),font=("Calibri", 40) )
        self.btn9 = Button(self.frame1, text='', width=3, height=1, bg="#A2D5AB", disabledforeground="white", command=lambda: self.tick(self.btn9),font=("Calibri", 40) )

        self.btn1.grid(row=0, column=0, pady=3, padx=3)
        self.btn2.grid(row=0, column=1, pady=3, padx=3)
        self.btn3.grid(row=0, column=2, pady=3, padx=3)
        self.btn4.grid(row=1, column=0, pady=3, padx=3)
        self.btn5.grid(row=1, column=1, pady=3, padx=3)
        self.btn6.grid(row=1, column=2, pady=3, padx=3)
        self.btn7.grid(row=2, column=0, pady=3, padx=3)
        self.btn8.grid(row=2, column=1, pady=3, padx=3)
        self.btn9.grid(row=2, column=2, pady=3, padx=3)
        
        self.bottomFrame = Frame(self, width=300, height=100,bg="black")
        self.bottomFrame.pack()
        self.bottomLabel = Label(self.bottomFrame, text="Code By Amrit", font=("Calibri Bold", 15),bg="#2C3E50",fg="#E5EFC1")
        self.bottomLabel.pack()
        


if __name__ == "__main__":
    
    win = game()
    # Change the default icon to a custom icon
    # icon_path = "path/to/your/icon.ico"
    # win.iconbitmap(icon_path)
    win.mainloop()
