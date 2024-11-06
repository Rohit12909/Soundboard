from playsound import playsound as ps
import os
from tkinter import *
from customtkinter import *

class SoundBoard():
    def __init__(self):
        
        self.root = CTk()
        self.root.title("Soundboard")
        self.root.geometry("800x500")
        self.frame = CTkFrame(master=self.root)
        self.frame.grid(row=5, column=5, padx=50, pady=50, sticky="news")

        self.grid = CTkFrame(master=self.frame)
        self.grid.grid(sticky="news", column=0, row=7, padx=10, pady=10)

        self.row = 0
        self.col = 0

        self.menuFrame = CTkFrame(master=self.root, width=660, height=50)
        self.menuFrame.grid(row=0, column=5, sticky="news", padx=25, pady=25)


        self.addSoundButton = CTkButton(self.menuFrame, text="Add New Sound", corner_radius=10, command=lambda soundPath=None: self.createBoard(soundPath=None))
        self.addSoundButton.place(x=10, y=13)

        self.loadStateButton = CTkButton(self.menuFrame, text="Load State", corner_radius=10, command=self.loadState)
        self.loadStateButton.place(x=155, y=13)

        self.daveStateButton = CTkButton(self.menuFrame, text="Save State", corner_radius=10, command=self.saveState)
        self.daveStateButton.place(x=300, y=13)

        self.deleteSoundBoard = CTkButton(self.menuFrame, text="DELETE ENTIRE SOUNDBOARD", corner_radius=10, command=self.deleteSave)
        self.deleteSoundBoard.place(x=445, y=13)

        self.sounds = []

    def createBoard(self, soundPath):
        
        if soundPath is None:
            soundPath = filedialog.askopenfilename()

        if soundPath not in self.sounds:
            self.sounds.append(soundPath)

        filename = os.path.basename(soundPath)

        btn = CTkButton(master=self.grid, text=filename, corner_radius=10, command=lambda soundPath=soundPath: self.playSound(soundPath=soundPath))
        btn.grid(column=self.col, row=self.row, padx=5, pady=5, sticky="news")

        # Position Buttons in a 5x5 grid
        self.col += 1

        if self.col > 4:
            self.row += 1
            self.col = 0

        if self.row > 4:
            self.row = 0
            # Disable button if grid is full (5x5)
            self.addSoundButton.configure(state='disabled')
            self.loadStateButton.configure(state='disabled')
            

    def playSound(self, soundPath):
        ps(soundPath)

    def saveState(self):
        
        effects = [sound for sound in self.sounds]

        with open("sound effects.txt", "w") as f:
            text = "\n".join(effects)
            f.write(text)


    def loadState(self):
        if self.row > 4 and self.col > 4:
            self.loadStateButton.configure(state='disabled')

        with open("sound effects.txt", "r") as f:
            effects = [x.rstrip() for x in f.readlines()]

            for sound in effects:
                self.createBoard(sound)

    def deleteSave(self):
        for widgets in self.grid.winfo_children():
            widgets.destroy()

        self.row = 0
        self.col = 0

        self.addSoundButton.configure(state='normal')
        self.loadStateButton.configure(state='normal')
        self.sounds = []

        f = open("sound effects.txt", 'w')
        f.close()


board = SoundBoard()

board.root.mainloop()
