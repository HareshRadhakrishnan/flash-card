BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
rand_word = None
words = []
try:
    word_list = pandas.read_csv("data/words_to_learn.csv")
    words = word_list.to_dict(orient="records")
except FileNotFoundError:
    words_to_learn = pandas.read_csv("data/french_words.csv")
    words_to_learn.to_csv("data/words_to_learn.csv")
    word_list = pandas.read_csv("data/words_to_learn.csv")
    words = word_list.to_dict(orient="records")
def correct():
    words.remove(rand_word)
    next_card()
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv")
    print(len(words))
def next_card():
    global rand_word , turn_timer
    window.after_cancel(turn_timer)

    rand_word = random.choice(words)
    canvas.itemconfig(txt_title,text="French")
    canvas.itemconfig(txt_word, text=f"{rand_word['French']}")
    window.after(3000, turn_card)
    canvas.itemconfig(canvas_bg,image=card_front)
    canvas.itemconfig(txt_word, fill="black")
    canvas.itemconfig(txt_title, fill="black")
def turn_card():
    canvas.itemconfig(txt_title, text="English",fill="white")
    canvas.itemconfig(txt_word, text=f"{rand_word['English']}",fill="white")
    canvas.itemconfig(canvas_bg,image=card_back)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
turn_timer = window.after(3000, turn_card)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas( highlightthickness=0,width=800,height=526, bg= BACKGROUND_COLOR)
canvas_bg = canvas.create_image(400, 263, image=card_front)
txt_title = canvas.create_text(400,150,text="Titile",font=("Ariel",40,"italic"))
txt_word =canvas.create_text(400,263,text="word", font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

right = PhotoImage(file="./images/right.png")
btn_right = Button(image=right, highlightthickness=0,bg=BACKGROUND_COLOR,bd=0,command=correct)
btn_right.grid(row=1,column=0)
wrong = PhotoImage(file="./images/wrong.png")
btn_wrong = Button(image=wrong, highlightthickness=1, bg=BACKGROUND_COLOR,bd=0,command=next_card)
btn_wrong.grid(row=1, column=1)
next_card()

window.mainloop()