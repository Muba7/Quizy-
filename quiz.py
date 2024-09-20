# Step 1: Define questions for different subjects
user_name=(input("Enter your Name: "))
math_quiz = [
    {"question": "If 5x - 2 = 3x + 8, what is x?", "options": ["1. 2", "2. 4", "3. 5", "4. 6"], "answer": 2},
    {"question": "The function f(x) = x² - 5x + 6 has roots at which values of x?", "options": ["1. 1 and 6", "2. 2 and 3", "3. -2 and -3", "4. -1 and 6"], "answer": 2},
    {"question": "What is the derivative of f(x) = 3x² + 5x - 7?", "options": ["1. 6x + 5", "2. 3x + 5", "3. 6x + 7", "4. 6x - 7"], "answer": 1},
    {"question": "Solve for x: 2x² - 4x - 6 = 0", "options": ["1. 3, -1", "2. 2, -3", "3. -2, 3", "4. 1, -3"], "answer": 1},
    {"question": "In a right triangle, if one leg is 3 and the hypotenuse is 5, what is the other leg?", "options": ["1. 4", "2. 5", "3. 6", "4. 7"], "answer": 1},
    {"question": "If f(x) = 2x + 1 and g(x) = x², what is f(g(2))?", "options": ["1. 9", "2. 5", "3. 7", "4. 11"], "answer": 1},
    {"question": "What is the sum of the interior angles of a pentagon?", "options": ["1. 540°", "2. 360°", "3. 180°", "4. 720°"], "answer": 1},
    {"question": "If sin(θ) = 1/2, what is θ in degrees?", "options": ["1. 30°", "2. 45°", "3. 60°", "4. 90°"], "answer": 1},
    {"question": "What is the limit of (3x² - 5x + 2) / (x - 1) as x approaches 1?", "options": ["1. 0", "2. 3", "3. 4", "4. 2"], "answer": 3},
    {"question": "The length of a rectangle is twice the width. If the perimeter is 24, what is the width?", "options": ["1. 4", "2. 5", "3. 6", "4. 8"], "answer": 1},
    {"question": "If x² - 4x + 4 = 0, what are the roots of the equation?", "options": ["1. 2", "2. 4", "3. 1, 2", "4. -2, 2"], "answer": 1},
    {"question": "What is the probability of rolling a sum of 7 with two six-sided dice?", "options": ["1. 1/6", "2. 1/5", "3. 1/12", "4. 1/7"], "answer": 1},
    {"question": "The area of a circle is 36π. What is the radius?", "options": ["1. 6", "2. 12", "3. 18", "4. 9"], "answer": 1},
    {"question": "What is the volume of a sphere with a radius of 3?", "options": ["1. 36π", "2. 27π", "3. 54π", "4. 4π"], "answer": 3},
    {"question": "If the sum of two numbers is 14 and their product is 48, what are the numbers?", "options": ["1. 6 and 8", "2. 7 and 8", "3. 4 and 12", "4. 2 and 16"], "answer": 1},
    {"question": "What is the value of log₂(16)?", "options": ["1. 4", "2. 8", "3. 16", "4. 2"], "answer": 1},
    {"question": "If a car travels at 60 miles per hour for 3 hours, how far does it travel?", "options": ["1. 120 miles", "2. 180 miles", "3. 200 miles", "4. 240 miles"], "answer": 2},
    {"question": "What is the remainder when 15 is divided by 4?", "options": ["1. 2", "2. 3", "3. 1", "4. 4"], "answer": 3},
    {"question": "Solve for x: 3x - 5 = 7", "options": ["1. 4", "2. 5", "3. 3", "4. 6"], "answer": 1},
    {"question": "If the area of a triangle is 30 and its base is 10, what is its height?", "options": ["1. 6", "2. 7", "3. 8", "4. 9"], "answer": 1}
]

history_quiz = [
    {"question": "Who was the first president of the USA?", "options": ["1. Abraham Lincoln", "2. George Washington", "3. Thomas Jefferson", "4. John Adams"], "answer": 2},
    {"question": "In which year did World War II end?", "options": ["1. 1940", "2. 1942", "3. 1945", "4. 1950"], "answer": 3},
    {"question": "Who was the British Prime Minister during WWII?", "options": ["1. Winston Churchill", "2. Neville Chamberlain", "3. Clement Attlee", "4. Margaret Thatcher"], "answer": 1},
    {"question": "What ancient civilization built the pyramids?", "options": ["1. Romans", "2. Greeks", "3. Egyptians", "4. Aztecs"], "answer": 3},
    {"question": "Which empire did Genghis Khan lead?", "options": ["1. Roman", "2. Mongol", "3. Ottoman", "4. Byzantine"], "answer": 2},
    {"question": "In which year did the American Civil War start?", "options": ["1. 1860", "2. 1861", "3. 1862", "4. 1865"], "answer": 2},
    {"question": "Who wrote the Declaration of Independence?", "options": ["1. George Washington", "2. John Adams", "3. Thomas Jefferson", "4. Benjamin Franklin"], "answer": 3},
    {"question": "Which country was Adolf Hitler born in?", "options": ["1. Germany", "2. Austria", "3. Poland", "4. France"], "answer": 2},
    {"question": "What year did the Titanic sink?", "options": ["1. 1911", "2. 1912", "3. 1913", "4. 1914"], "answer": 2},
    {"question": "Who was known as the 'Iron Lady'?", "options": ["1. Angela Merkel", "2. Golda Meir", "3. Margaret Thatcher", "4. Indira Gandhi"], "answer": 3},
    {"question": "Which empire was known as the 'Holy Roman Empire'?", "options": ["1. Byzantine Empire", "2. Ottoman Empire", "3. Roman Empire", "4. German Empire"], "answer": 4},
    {"question": "Who was the first man to walk on the moon?", "options": ["1. Yuri Gagarin", "2. Neil Armstrong", "3. Buzz Aldrin", "4. Michael Collins"], "answer": 2},
    {"question": "Which war was fought between the North and South regions of the United States?", "options": ["1. Revolutionary War", "2. War of 1812", "3. Civil War", "4. Spanish-American War"], "answer": 3},
    {"question": "What year did the Berlin Wall fall?", "options": ["1. 1987", "2. 1988", "3. 1989", "4. 1990"], "answer": 3},
    {"question": "Who was the first female Prime Minister of the UK?", "options": ["1. Theresa May", "2. Margaret Thatcher", "3. Elizabeth I", "4. Mary I"], "answer": 2},
    {"question": "Which war was fought in Vietnam?", "options": ["1. World War II", "2. Korean War", "3. Vietnam"] } 
    ] 


# Step 2: Function to run the selected quiz
def run_quiz(quiz):
    score = 0
    for i, question in enumerate(quiz):
        print(f"\nQuestion {i + 1}: {question['question']}")
        for option in question['options']:
            print(option)
        user_answer = int(input("Enter the number of your answer: "))
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Wrong.")
    print(f"\nYour score: {score}/{len(quiz)}")

# Step 3: Let the user choose the subject
def choose_subject():
    print("Choose a subject:")
    print("1. Math")
    print("2. History")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        run_quiz(math_quiz)
    elif choice == 2:
        run_quiz(history_quiz)
    else:
        print("Invalid choice!")
        print(f"\n{user_name}, your final score is: {score}/{len(quiz)}")
    print(f"Congratulations, {user_name}!")



# Step 4: Start the quiz selection
choose_subject()