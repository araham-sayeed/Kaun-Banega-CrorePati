import tkinter as tk
from tkinter import messagebox

# Questions data
Questions = [
    ["Which language was used to create Facebook?", "Python", "C#", "JavaScript", "PHP", 'd'],
    ["What is the output of 'print(3 + 4)' in Python?", "7", "34", "Error", "None", 'a'],
    ["Which language is primarily used for front-end web development?", "Python", "C#", "JavaScript", "PHP", 'c'],
    ["Which data structure uses LIFO (Last In, First Out)?", "Queue", "Stack", "Array", "Linked List", 'b'],
    ["Which sorting algorithm has the best average-case time complexity?", "Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort", 'b'],
    ["In Object-Oriented Programming, what does 'inheritance' allow?", "Reuse of code", "Multiple constructors", "Multiple inheritance", "Memory optimization", 'a'],
    ["Which SQL command is used to retrieve data from a database?", "INSERT", "SELECT", "UPDATE", "DELETE", 'b'],
    ["Which protocol is used for secure communication over the internet?", "HTTP", "FTP", "SMTP", "HTTPS", 'd'],
    ["Which operating system is open-source?", "Windows", "macOS", "Linux", "Android", 'c'],
    ["Which cloud service provider is known for AWS?", "Microsoft", "Google", "Amazon", "IBM", 'c'],
    ["Which AI technique is used to train models using labeled data?", "Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Deep Learning", 'a'],
    ["Which algorithm is commonly used for finding the shortest path in a graph?", "DFS", "BFS", "Dijkstra's Algorithm", "Kruskal's Algorithm", 'c'],
    ["Which encryption algorithm is widely used in securing web traffic?", "AES", "RSA", "DES", "SHA", 'a'],
    ["What is the first stage of the compilation process?", "Lexical Analysis", "Syntax Analysis", "Semantic Analysis", "Code Optimization", 'a'],
    ["Which algorithm is commonly used for achieving consensus in a distributed system?", "Raft", "Paxos", "MapReduce", "Quorum", 'b'],
    ["Which machine learning algorithm is primarily used for classification problems?", "Linear Regression", "K-means Clustering", "Logistic Regression", "Decision Tree", 'c'],
    ["Which theorem is fundamental to the concept of NP-completeness?", "Fermat's Last Theorem", "P=NP", "Cook-Levin Theorem", "Gödel's Incompleteness Theorem", 'c']
]

# Levels and prize amounts
levels = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1250000, 2500000, 5000000, 7500000, 10000000, 50000000, 100000000]

# Global variables
current_question = 0
money = 0

# Initialize the Tkinter window
root = tk.Tk()
root.title("Kaun Banega Crorepati")
root.geometry("600x600")
root.config(bg="#E0F7FA")

# Display Name Entry Window
def start_game():
    global name
    name = entry_name.get()
    if not name:
        messagebox.showerror("Error", "Please enter your name")
        return
    start_button.pack_forget()
    entry_name.pack_forget()
    label_name.pack_forget()
    welcome_label.config(text=f"Welcome {name}!\nLet's begin the game!")
    welcome_label.pack()
    
    root.after(2000, ask_question)

# Update the question and options
def ask_question():
    global current_question
    if current_question >= len(Questions):
        messagebox.showinfo("Game Over", f"Congratulations {name}, you've won Rs. {money}!")
        root.quit()
        return

    question = Questions[current_question]
    question_label.config(text=f"Question {current_question+1} for Rs. {levels[current_question]}")
    question_text.config(text=question[0])
    option_a.config(text=f"a. {question[1]}")
    option_b.config(text=f"b. {question[2]}")
    option_c.config(text=f"c. {question[3]}")
    option_d.config(text=f"d. {question[4]}")

# Handle the selected answer
def check_answer(option):
    global current_question, money
    question = Questions[current_question]
    if option == question[5]:
        money = levels[current_question]
        messagebox.showinfo("Correct", f"Correct answer! You have won Rs. {money}")
        current_question += 1
        ask_question()
    else:
        messagebox.showinfo("Incorrect", f"Wrong answer! You leave with Rs. {money}")
        root.quit()

# Quit the game
def quit_game():
    messagebox.showinfo("Game Over", f"You quit the game with Rs. {money}")
    root.quit()

# Setting up the GUI layout
label_name = tk.Label(root, text="Enter your name: ")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

welcome_label = tk.Label(root, text="", bg="#E0F7FA", font=("Helvetica", 16, "bold"), fg="#1E88E5")

question_label = tk.Label(root, text="")
question_label.pack()

question_text = tk.Label(root, text="", wraplength=400)
question_text.pack()

option_a = tk.Button(root, text="a. Option 1", command=lambda: check_answer('a'))
option_a.pack()

option_b = tk.Button(root, text="b. Option 2", command=lambda: check_answer('b'))
option_b.pack()

option_c = tk.Button(root, text="c. Option 3", command=lambda: check_answer('c'))
option_c.pack()

option_d = tk.Button(root, text="d. Option 4", command=lambda: check_answer('d'))
option_d.pack()

quit_button = tk.Button(root, text="Quit Game", command=quit_game)
quit_button.pack()

root.mainloop()
