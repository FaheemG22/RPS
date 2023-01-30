from tkinter import *
import random
from PIL import Image, ImageTk
class RPS:
    def __init__(self):
        self.lives = 3
        self.wins = 0
        self.label=[0, 0, 0]
        self.win = Tk()
        self.win.geometry('250x270')

        self.images('paper', 0, 0, 80)
        self.images('paper', 2, 0, 80)

        self.images('rock', 0, 1, 60)
        self.images('paper', 1, 1, 60)
        self.images('scissors', 2, 1, 60)

        rock = Button(self.win, text="Rock", height=5, width=10, command=lambda: self.choice('rock'))
        rock.grid(column=0, row=2)
        paper = Button(self.win, text="Paper", height=5, width=10, command=lambda: self.choice('paper'))
        paper.grid(column=1, row=2)
        scissors = Button(self.win, text="Scissors", height=5, width=10, command=lambda: self.choice('scissors'))
        scissors.grid(column=2, row=2)

        self.label_lives = Label(self.win, text=f'Lives: {self.lives}', fg='red', font='monospace')
        self.label_lives.grid(column=0, row=3, columnspan=2, rowspan=2)
        self.label_wins = Label(self.win, text=f'Wins: {self.wins}', fg='green', font='monospace')
        self.label_wins.grid(column=1, row=3, columnspan=2, rowspan=2)

        self.win.mainloop()

    def images(self, img, col, ro, size):
        sizes = size, size
        image = Image.open(img+'.png')
        image.thumbnail(sizes)
        image = ImageTk.PhotoImage(image)
        self.label[col] = Label(self.win, image=image)
        self.label[col].image = image
        self.label[col].grid(column=col, row=ro)

    def choice(self, play_choice):
        try:
            choices = ['rock', 'paper', 'scissors']
            comp_choice = random.choice(choices)
            self.images(comp_choice, 2, 0, 80)
            self.images(play_choice, 0, 0, 80)

            if comp_choice == play_choice:
                print('Tie :^|')

            elif comp_choice == 'rock' and play_choice == 'paper':
                self.wins += 1
            elif comp_choice == 'paper' and play_choice == 'scissors':
                self.wins += 1
            elif comp_choice == 'scissors' and play_choice == 'rock':
                self.wins += 1

            # player lost
            elif comp_choice == 'rock' and play_choice == 'scissors':
                self.lives -= 1
            elif comp_choice == 'paper' and play_choice == 'rock':
                self.lives -= 1
            elif comp_choice == 'scissors' and play_choice == 'paper':
                self.lives -= 1

            if self.wins == 3:
                print('winner')
                self.win.destroy()
            if self.lives == 0:
                print('loser')
                self.win.destroy()

            self.label_lives.destroy()
            self.label_wins.destroy()

            self.label_lives = Label(self.win, text=f'Lives: {self.lives}', fg='red', font='monospace', width=12, height=1)
            self.label_lives.grid(column=0, row=3, columnspan=2, rowspan=2)

            self.label_wins = Label(self.win, text=f'Wins: {self.wins}', fg='green', font='monospace', width=12, height=1)
            self.label_wins.grid(column=1, row=3, columnspan=2, rowspan=2)
        except:
            print(EXCEPTION)

RPS()
