from tkinter import *
import random
from PIL import Image, ImageTk


class RPS:
    def __init__(self):
        self.lives = 3
        self.wins = 0

        self.win = Tk()
        self.win.geometry('250x200')

        size = 80, 80
        rock_image = Image.open('rock.png')
        rock_image.thumbnail(size)
        rock_image = ImageTk.PhotoImage(rock_image)
        label_rock = Label(self.win, image=rock_image)
        label_rock.image = rock_image
        label_rock.grid(column=0, row=0)

        paper_image = Image.open('paper.png')
        paper_image.thumbnail(size)
        paper_image = ImageTk.PhotoImage(paper_image)
        label_paper = Label(self.win, image=paper_image)
        label_paper.image = paper_image
        label_paper.grid(column=1, row=0)

        scissors_image = Image.open('scissors.png')
        scissors_image.thumbnail(size)
        scissors_image = ImageTk.PhotoImage(scissors_image)
        label_scissors = Label(self.win, image=scissors_image)
        label_scissors.image = scissors_image
        label_scissors.grid(column=2, row=0)

        rock = Button(self.win, text="Rock", height=5, width=10, command=lambda: self.choice('rock'))
        rock.grid(column=0, row=1)

        paper = Button(self.win, text="Paper", height=5, width=10, command=lambda: self.choice('paper'))
        paper.grid(column=1, row=1)

        scissors = Button(self.win, text="Scissors", height=5, width=10, command=lambda: self.choice('scissors'))
        scissors.grid(column=2, row=1)

        self.label_lives = Label(self.win, text=f'Lives: {self.lives}')
        self.label_lives.grid(column=0, row=2)

        self.label_wins = Label(self.win, text=f'Wins: {self.wins}')
        self.label_wins.grid(column=1, row=2)
        self.win.mainloop()

    def choice(self, play_choice):
        try:
            choices = ['rock', 'paper', 'scissors']
            comp_choice = random.choice(choices)
            print(f'{play_choice}')
            print(f'{comp_choice}\n')
            # print(comp_choice)
            if comp_choice == play_choice:
                print('Tie :^|')
            # player winning
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

            self.label_lives = Label(self.win, text=f'Lives: {self.lives}')
            self.label_lives.grid(column=0, row=2)

            self.label_wins = Label(self.win, text=f'Wins: {self.wins}')
            self.label_wins.grid(column=1, row=2)
        except:
            print(EXCEPTION)


RPS()
