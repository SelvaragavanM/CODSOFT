import random
import tkinter
from tkinter.constants import SUNKEN

def winner_select(choice):
    if not choice:
        return "", "You have not started to play"

    if random.random() <= (1/3):
        picked = "rock"
    elif (1/3) < random.random() <= (2/3):
        picked = "scissor"
    else:
        picked = "paper"

    if (picked == "rock" and choice == "Paper") or (picked == "paper" and choice == "Scissor") or (picked == "scissor" and choice == "Rock"):
        result = "You have Won the match!"
    elif picked == choice:
        result = "Match is Draw"
    else:
        result = "You have Lost the match!"

    return picked, result

def pass_s():
    picked, result = winner_select("Scissor")
    output.delete(1.0, tkinter.END)  
    output.insert(tkinter.END, "Computer have picked:" + picked + "\n" + result)
    playagain_button.grid(row=2, column=1)

def pass_r():
    picked, result = winner_select("Rock")
    output.delete(1.0, tkinter.END)
    output.insert(tkinter.END, "Computer have picked:" + picked + "\n" + result)
    playagain_button.grid(row=2, column=1)

def pass_p():
    picked, result = winner_select("Paper")
    output.delete(1.0, tkinter.END)
    output.insert(tkinter.END, "Computer have picked:" + picked + "\n" + result)
    playagain_button.grid(row=2, column=1)

def playagain():
    playagain_button.grid_forget()
    output.delete(1.0, tkinter.END)
    if output.get("1.0", "end-1c") == "You have not started to play":
        output.delete(1.0, tkinter.END)

window = tkinter.Tk()

scissor = tkinter.Button(window, text="Scissor", bg="#e30b5d", padx=5, pady=7, command=pass_s, width=20)
rock = tkinter.Button(window, text="Rock", bg="#00bfff", padx=5, pady=7, command=pass_r, width=20)
paper = tkinter.Button(window, text="Paper", bg="#ffd700", padx=5, pady=7, command=pass_p, width=20)

output = tkinter.Text(window, height=4, width=30)
output.grid(row=0, column=0, columnspan=8, ipady=5, pady=5)

playagain_button = tkinter.Button(window, text="Play Again", bg="#48d1cc", padx=5, pady=7, command=playagain)
playagain_button.grid(row=2, column=1)

scissor.grid(row=1, column=0, padx=5)
rock.grid(row=1, column=1, padx=5)
paper.grid(row=1, column=2, padx=5)

window.mainloop()
