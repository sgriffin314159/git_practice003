# Quiz questions for the Gradio app game

# Store quiz questions as a list of dictionaries. 
# Each dictionary contains:
# - "question" (the text of the question)
# - "options" (a list of possible answers)
# - "answer" (the correct answer)

QUIZ_QUESTIONS = [
    {
        "question": "Which value is not an integer?",
        "options": ["0", "33", "-78", "0.5"],
        "answer": "0.5"
    },
    {
        "question": "Which mathematician was from Italy?",
        "options": ["Chebyshev", "Weierstrass", "Pythagoras", "Agnesi"],
        "answer": "Agnesi"
    },
    {
        "question": "Which number listed is both perfect and triangular?",
        "options": ["10", "28", "2", "16"],
        "answer": "28"
    },
    {
        "question": "Which polynomial listed is a quadratic binomial?",
        "options": ["x^2 + 25", "x^2 - 3x - 28", "16x^2", "x + 36"],
        "answer": "x^2 + 25"
    }
]