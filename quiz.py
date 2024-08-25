import tkinter as tk  
from tkinter import messagebox, ttk  
from ttkbootstrap import Style  

# Sample quiz data  
quiz_data = [  
    {  
        "question": "What is the capital of France?",  
        "choices": ["Paris", "London", "Berlin", "Madrid"],  
        "answer": "Paris"  
    },  
    {  
        "question": "What is 2 + 2?",  
        "choices": ["3", "4", "5", "6"],  
        "answer": "4"  
    },  
    {  
        "question": "What is the largest ocean on Earth?",  
        "choices": ["Atlantic", "Indian", "Arctic", "Pacific"],  
        "answer": "Pacific"  
    },  
    {  
        "question": "What is the color of the sky?",  
        "choices": ["Blue", "Green", "Red", "Yellow"],  
        "answer": "Blue"  
    },  
]  

# Initialize global variables  
score = 0  
current_question = 0  

# Function to display the current question and choices  
def show_question():  
    global current_question  
    # Get the current question from the quiz_data list  
    question = quiz_data[current_question]  

    # Print the question for debugging purposes  
    print(question)  # Debugging line  

    if "question" not in question or "choices" not in question:  
        raise ValueError("The current question dictionary is missing required keys.")  

    qs_label.config(text=question["question"])  

    # Display the choices on the buttons  
    choices = question["choices"]  
    for i in range(4):  
        choice_btns[i].config(text=choices[i], state="normal")  # Reset button state  

    # Clear the feedback label and disable the next button  
    feedback_label.config(text="")  
    next_btn.config(state="disabled")  

# Function to check the selected answer and provide feedback  
def check_answer(choice):  
    global score  
    # Get the current question from the quiz_data list  
    question = quiz_data[current_question]  
    selected_choice = choice_btns[choice].cget("text")  

    # Check if the selected choice matches the correct answer  
    if selected_choice == question["answer"]:  
        score += 1  
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))  
        feedback_label.config(text="Correct!", foreground="green")  
    else:  
        feedback_label.config(text="Incorrect!", foreground="red")  

    # Disable all choice buttons and enable the next button  
    for button in choice_btns:  
        button.config(state="disabled")  
    next_btn.config(state="normal")  

# Function to move to the next question  
def next_question():  
    global current_question  
    current_question += 1  

    if current_question < len(quiz_data):  
        show_question()  
    else:  
        messagebox.showinfo("Quiz Completed", "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))  
        root.destroy()  

# Create the main window  
root = tk.Tk()  
root.title("Quiz App")  
root.geometry("600x500")  
style = Style(theme="flatly")  

# Configure the font size for the question and choice buttons  
style.configure("TLabel", font=("Helvetica", 20))  
style.configure("TButton", font=("Helvetica", 16))  

# Create the question label  
qs_label = ttk.Label(root, anchor="center", wraplength=500, padding=10)  
qs_label.pack(pady=10)  

# Create the choice buttons  
choice_btns = []  
for i in range(4):  
    button = ttk.Button(root, command=lambda i=i: check_answer(i))  
    button.pack(pady=5)  
    choice_btns.append(button)  

# Create the feedback label  
feedback_label = ttk.Label(root, anchor="center", padding=10)  
feedback_label.pack(pady=10)  

# Create the score label  
score_label = ttk.Label(root, text="Score: 0/{}".format(len(quiz_data)), anchor="center", padding=10)  
score_label.pack(pady=10)  

# Create the next button  
next_btn = ttk.Button(root, text="Next", command=next_question, state="disabled")  
next_btn.pack(pady=10)  

# Show the first question  
show_question()  

# Start the main event loop  
root.mainloop()