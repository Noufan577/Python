from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ----------------------- LOAD DATA ------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")   
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")     
content = data.to_dict(orient="records")  

curr = {}

# ----------------------- FUNCTIONS ------------------------- #
def next_card():
    global curr, flip_timer

    window.after_cancel(flip_timer) 
    curr = random.choice(content)

    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=curr["French"], fill="black")

    flip_timer = window.after(3000, flip_card)   # Auto flip timer


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr["English"], fill="white")


def know():
    """Remove the known word, save progress, and move to next card."""
    content.remove(curr)

    df = pd.DataFrame(content)
    df.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# ----------------------- UI SETUP ------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card App")

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=880, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
button_cross = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=next_card)
button_cross.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
button_tick = Button(image=right_img, highlightthickness=0, borderwidth=0, command=know)
button_tick.grid(row=1, column=1)

next_card()

window.mainloop()
