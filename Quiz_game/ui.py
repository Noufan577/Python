from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text="Score: 0",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white",
            highlightthickness=0
        )
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=270,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.true_image = PhotoImage(
            file=r"C:\Users\noufa\OneDrive\Desktop\ml\python\Python\Quiz_game\images\true.png"
        )
        self.false_image = PhotoImage(
            file=r"C:\Users\noufa\OneDrive\Desktop\ml\python\Python\Quiz_game\images\false.png"
        )

        # Buttons
        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            bd=0,
            command=self.true_click
        )
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            bd=0,
            command=self.false_click
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_qns()
        self.window.mainloop()

    def get_next_qns(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            return

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_click(self):
        res = self.quiz.check_answer("true")
        self.feedback(res)

    def false_click(self):
        res = self.quiz.check_answer("false")
        self.feedback(res)

    def feedback(self, res: bool):
        if res:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_qns)
