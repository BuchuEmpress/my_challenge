# quiz master


import time  # Import time module for timing questions
import sys   # Import sys for progress bar display

# Define the data structure containing questions categorized by topic and difficulty
quiz_data = {
    "Science": {
        "easy": [
            {
                "question": "What is the chemical symbol for water?",
                "options": ["H2O", "CO2", "O2", "H2"],
                "answer": 0  # displays the index on where correct option is located
            },
            {
                "question": "How many planets are in the Solar System?",
                "options": ["7", "8", "9", "10"],
                "answer": 1
            },
            {
                "question": "Which gas is most abundant in Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"],
                "answer": 1
            },
            {
                "question": "What organ is responsible for pumping blood?",
                "options": ["Lungs", "Brain", "Heart", "Liver"],
                "answer": 2
            },
            {
                "question": "What is the speed of light?",
                "options": ["300,000 km/s", "150,000 km/s", "1,000 km/s", "30,000 km/s"],
                "answer": 0
            }
        ],
        "hard": [
            {
                "question": "What is the atomic number of Carbon?",
                "options": ["4", "6", "8", "12"],
                "answer": 1
            },
            {
                "question": "Which element has the highest melting point?",
                "options": ["Tungsten", "Gold", "Iron", "Copper"],
                "answer": 0
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["O-", "AB-", "B+", "A+"],
                "answer": 1
            },
            {
                "question": "Which planet has the most moons?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": 2
            },
            {
                "question": "What is the main gas responsible for the greenhouse effect?",
                "options": ["Methane", "Carbon Dioxide", "Ozone", "Nitrous Oxide"],
                "answer": 1
            }
        ]
    },
    "History": {
        "easy": [
            {
                "question": "Who was the first President of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
                "answer": 1
            }
            # More questions are needed...
        ],
        "hard": [
            # More questions questions...
        ]
    },
    "Sports": {
        "easy": [
            {"question": "Which sport is known as 'the beautiful game'?",
    "options": ["Basketball", "Soccer", "Tennis", "Cricket"],
    "answer": 1  # Soccer
            }
        ],
        "hard": [
            {
           "question": "Who holds the record for the most Olympic gold medals?",
    "options": ["Michael Phelps", "Larisa Latynina", "Mark Spitz", "Carl Lewis"],
    "answer": 0  # Michael Phelps
            }

        ]
    },
}

# Function to display a progress bar during the quiz
def show_progress(current, total):
    percent = int((current / total) * 100)             # Calculates the percentage completed
    blocks = int(percent / 10)                           # Calculates the number of blocks in the progress bar
    bar = '█' * blocks + '░' * (10 - blocks)              # Building the progress bar string
    sys.stdout.write(f"\r[{bar}] {percent}% Complete")      # Print the progress bar with carriage return(this carriage return causes the cursor to return the the
    # the beginnning of that same line) to overwrite previous line ( so each time a new result is recorded
    # it overrides the previous progress bar to print the new progress bar )
    sys.stdout.flush()                            # ensures that the progress bar is printed almost immediately
    # rather than waiting for it to fill up or another activity

# Function to get user's selected category
def select_category():
    print("Available categories:")
    for index, category in enumerate(quiz_data.keys(), 1):
        print(f"{index}. {category}")
    while True:
        choice = input("Select a category by number: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(quiz_data):               # if the choice is within the range of categories
                selected_category = list(quiz_data.keys())[choice - 1]
                return selected_category
        print("Invalid choice, please try again.")

# Function to get user's selected difficulty
def select_difficulty():
    options = ["easy", "hard"]
    print("Difficulties:")
    for index, diff in enumerate(options, 1):
        print(f"{index}. {diff.capitalize()}")
    while True:
        choice = input("Select difficulty by number: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice - 1]             # returns the selected choice by adjusting the undex and removing the one not chosen
        print("Invalid choice, please try again.")

# Main function to run the quiz
def run_quiz():
    high_scores = {}  # Dictionary to hold high scores per category
    total_questions = 0
    score = 0
    correct_answers = 0

    # Select category and difficulty
    category = select_category()
    difficulty = select_difficulty()

    questions = quiz_data[category][difficulty]
    total_questions = len(questions)

    # Check if questions list is empty
    if total_questions == 0:
        print(f"No questions available for {category} - {difficulty}.")
        return  # Exit the function if no questions

    print(f"\nStarting quiz in {category} - {difficulty.capitalize()}")
    print("Good luck!\n")
    start_time = time.time()  # Record start time

    # Loop through each question
    for idx, q in enumerate(questions, 1):
        print(f"Question {idx}/{total_questions}: {q['question']}")      #idx is the index ; prints index of question/ tot number of questions and the question itself
        # Show progress bar
        show_progress(idx - 1, total_questions)
        print()  # Newline after progress bar

        # Display options
        for i, option in enumerate(q['options']):
            print(f"{chr(65 + i)}) {option}")

        # Record time before user answer
        question_start = time.time()
        while True:
            answer = input("Your answer (A-D): ").upper()
            if answer in ['A', 'B', 'C', 'D']:
                answer_idx = ord(answer) - 65
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")

        # Record time after answer
        question_time = time.time() - question_start

        # Check if answer is correct
        if answer_idx == q['answer']:       # checks if the answer in that index matches given answer
            print("✅ Correct! (+10 points)")
            score += 10
            correct_answers += 1
        else:
            correct_option = chr(65 + q['answer'])
            print(f"❌ Wrong! Correct answer was {correct_option}) {q['options'][q['answer']]}")
        print(f"Time: {question_time:.2f} seconds\n")

    # Show final progress bar as completed
    show_progress(total_questions, total_questions)
    print()  # Move to next line

    total_time = time.time() - start_time
    print(f"\nFINAL SCORE: {score}/{total_questions * 10} ({correct_answers}/{total_questions} correct)")      # multiplies the number of correct answers you have times ten to get your score prints the number 
    # correct answers to the total questions
    print(f"Total time: {total_time:.2f} seconds")

    # Save high score if higher than previous
    if category not in high_scores or score > high_scores[category]:
        high_scores[category] = score
        print(f"New personal best in {category}!")

# Run the quiz
if __name__ == "__main__":
    run_quiz()