🧠 Quiz Game (Python Tkinter)

A simple GUI-based Quiz Application built using Python and Tkinter, following clean separation of logic and interface.
The quiz logic is handled by a QuizBrain class, while the user interface is managed by QuizInterface.

📌 Features

Graphical User Interface using Tkinter

True / False question format

Real-time score tracking

Visual feedback for correct and wrong answers

Automatically moves to the next question

Clean separation of UI and quiz logic

End-of-quiz detection with button disabling

🛠️ Technologies Used

Python 3

Tkinter (standard GUI library)

Object-Oriented Programming (OOP)

📂 Project Structure
Quiz_Game/
│
├── main.py                 # Entry point of the program
├── quiz_brain.py           # Quiz logic (question handling, score)
├── ui.py                   # Tkinter-based GUI (QuizInterface)
├── data.py                 # Question data (if applicable)
│
├── images/
│   ├── true.png            # True button image
│   └── false.png           # False button image
│
└── README.md               # Project documentation

▶️ How to Run the Project

Clone or download the project

Make sure Python 3 is installed:

python --version


Navigate to the project folder:

cd Quiz_Game


Run the program:

python main.py

🎮 How the Game Works

A question is displayed on the screen

Click:

✅ True if you think the answer is correct

❌ False if you think the answer is wrong

The screen:

Turns green for correct answers

Turns red for wrong answers

The next question appears automatically after 1 second

Your score updates in real time

At the end of the quiz:

A completion message is shown

Buttons are disabled

🧩 Code Design Overview
QuizBrain (Logic Layer)

Manages:

Questions

Answer checking

Score calculation

Has no GUI code

QuizInterface (UI Layer)

Handles:

Tkinter window

Buttons and canvas

User interaction

Communicates with QuizBrain only through methods

This separation makes the code:

Easier to debug

Easier to extend

More professional

💡 Key Concepts Used

Tkinter Canvas and Button

Callback functions (command=)

Delayed execution using window.after()

Object-Oriented Programming

Garbage collection safety for images

🚀 Future Improvements

Add multiple-choice questions

Add sound effects

Add progress bar

Load questions from an API

Restart quiz option

Dark mode / theme switch

📷 Screenshot (Optional)

Add a screenshot of the quiz window here for better presentation.

👨‍💻 Author

Noufan N
Python Developer | Learning GUI & Application Design

📄 License

This project is created for learning and educational purposes.

If you want, I can:

✨ shorten this for a college submission

🧑‍🏫 rewrite it in exam-friendly language

🌐 adapt it for GitHub portfolio

📦 auto-generate a requirements.txt

Just tell me 👍

the data is from api open triva dataase

Great 👍
Here is the updated, correct README.md, explicitly mentioning that the questions are fetched from the Open Trivia Database API.
This version is accurate, professional, and portfolio-ready.

You can replace your existing README.md with this.

🧠 Quiz Game (Python Tkinter)

A GUI-based Quiz Application built using Python and Tkinter, where quiz questions are dynamically fetched from the Open Trivia Database API.
The application follows a clean separation of logic and interface using Object-Oriented Programming.

🌐 Data Source

This project uses the Open Trivia Database API to fetch quiz questions in real time.

API Name: Open Trivia Database

Website: https://opentdb.com/

Type: Free public trivia API

Question Format: True / False

Questions are retrieved via HTTP requests and parsed before being displayed in the GUI.

📌 Features

GUI built with Tkinter

Questions fetched dynamically from an external API

True / False quiz format

Real-time score tracking

Visual feedback (green/red) for answers

Automatic transition between questions

End-of-quiz detection and UI disabling

Clean separation between UI and logic

🛠️ Technologies Used

Python 3

Tkinter (GUI)

Requests (for API calls)

Object-Oriented Programming (OOP)

📂 Project Structure
Quiz_Game/
│
├── main.py                 # Program entry point
├── quiz_brain.py           # Quiz logic & scoring
├── question_model.py       # Question data model
├── data.py                 # API call to Open Trivia Database
├── ui.py                   # Tkinter GUI (QuizInterface)
│
├── images/
│   ├── true.png
│   └── false.png
│
└── README.md

▶️ How to Run the Project

Clone or download the project

Ensure Python 3 is installed:

python --version


Install required dependency:

pip install requests


Run the application:

python main.py

🎮 How the Quiz Works

Questions are fetched from the Open Trivia Database API

Each question is displayed in the Tkinter window

Click:

✅ True if the statement is correct

❌ False if incorrect

Immediate visual feedback is shown:

Green → Correct

Red → Wrong

After 1 second, the next question appears

Score updates automatically

When questions end:

A completion message is shown

Buttons are disabled

🧩 Code Design Overview
data.py

Sends HTTP requests to the Open Trivia Database API

Parses JSON response into question objects

question_model.py

Defines the Question class

Stores question text and correct answer

quiz_brain.py

Controls quiz flow

Checks answers

Maintains score

ui.py

Handles Tkinter GUI

Displays questions and feedback

Interacts with QuizBrain

💡 Key Concepts Demonstrated

API integration in Python

Tkinter event-driven programming

MVC-style architecture

Delayed execution (after())

Proper image handling in Tkinter

Clean OOP design