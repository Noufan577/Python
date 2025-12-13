?? Flashcard French Learning App

A simple and interactive Flashcard App built using Python + Tkinter to help users learn French vocabulary.
The app displays a French word and automatically flips the card after 3 seconds to reveal the English meaning. Users can also load a new card using buttons.

? Features

?? Random flashcards generated from a CSV file

? Auto flip to English after 3 seconds

?? Next card button to load a new word

?? Beautiful UI with front/back card images

?? Uses Pandas for data handling

?? Project Structure
.
ÃÄÄ main.py
ÃÄÄ data/
³   ÀÄÄ french_words.csv
ÃÄÄ images/
³   ÃÄÄ card_front.png
³   ÃÄÄ card_back.png
³   ÃÄÄ right.png
³   ÀÄÄ wrong.png
ÀÄÄ README.md

?? How It Works

Loads French-English words from CSV into a list of dictionaries

Displays a random French word on the card front

After 3 seconds, automatically flips the card to show English

? and ? buttons load a new random card

?? Installation
Install dependencies:
pip install pandas


Tkinter is included with Python by default.

?? How to Run
python main.py


Make sure the folder structure is correct (especially the images folder).

?? Code Overview (Simplified)
Load data:
data = pd.read_csv("data/french_words.csv")
content = data.to_dict(orient="records")

Pick a random card:
curr = random.choice(content)

Auto flip:
flip_timer = window.after(3000, flip_card)

Update the card UI:
canvas.itemconfig(card_title, text="French")
canvas.itemconfig(card_word, text=curr["French"])

?? Future Enhancements

Track known/unknown words

Save remaining words to a new CSV

Add animations

Add progress tracking

Add difficulty levels

?? License

This project is free to use and modify.
