from tkinter import *
import json

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.data_size = len(question)
        self.correct = 0

    def display_result(self):
        # Display the quiz result (correct, wrong, score)
        # ...

    def check_ans(self, q_no):
        # Check if the selected option is correct
        # ...

    def next_btn(self):
        # Handle Next button click
        # ...

    def buttons(self):
        # Create Next and Quit buttons
        # ...

    def display_options(self):
        # Display answer options
        # ...

    def display_question(self):
        # Display the current question
        # ...

# Create the main GUI window
gui = Tk()
gui.title("Quiz Game")
gui.geometry("800x500")

# Load quiz data from data.json
with open("data.json") as f:
    data = json.load(f)
    question = data["question"]
    answer = data["answer"]
    options = data["options"]

# Initialize the quiz
quiz = Quiz()

# Start the GUI event loop
gui.mainloop()
