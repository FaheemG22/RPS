from tkinter import *
import random
from threading import Thread


class RPS:
    def __init__(self):
        self.lives = 3
        self.wins = 0
        Thread(target=self.display).start()
        Thread(target=self.player).start()

    def display(self):
        self.win = Tk()
        self.win.mainloop()

    def player(self):
        while True:
            choices = ['rock', 'paper', 'scissors']
            comp_choice = random.choice(choices)
            print(comp_choice)
RPS()
