# Gradio web app for quiz game
# 1) Import the gradio library and our local quiz_data module
import gradio as gr
from quiz_data import QUIZ_QUESTIONS

# 2) Define a function to check the user's answer
def check_answer(selected_option, question_index):
    # We use control flow here: if the selected answer matches the correct one, we return "Correct!"
    if selected_option == QUIZ_QUESTIONS[question_index]["answer"]:
        return "Correct!"
    else:
        return "Incorrect. The correct answer is: " + QUIZ_QUESTIONS[question_index]["answer"]

# 3) Define a helper function that returns only question texts (using a list comprehension!)
def generate_question_texts():
    return [q["question"] for q in QUIZ_QUESTIONS]

# 4) Define a function that finds the question and its options, given a question text
def quiz_interface(question_text):
    # We'll locate the question index by searching in QUIZ_QUESTIONS
    question_idx = [index for (index, q) in enumerate(QUIZ_QUESTIONS) if q["question"] == question_text][0]
    if question_idx is None:
        return None, []
    return question_text, QUIZ_QUESTIONS[question_idx]["options"]

# 5) Build the Gradio demo using Blocks
def build_quiz_app():
    # Our list of question texts
    question_list = generate_question_texts()

    with gr.Blocks() as demo:
        # Dropdown for selecting a question
        question_dropdown = gr.Dropdown(label="Select a question", choices=question_list)
        question_display = gr.Textbox(label="Question", interactive=False)
        options_radio = gr.Radio(label="Choose your answer", choices=[])
        feedback_box = gr.Textbox(label="Feedback", interactive=False)

        # This function updates the displayed question and answer options
        def update_question(question_text):
            q_text, opts = quiz_interface(question_text)
            if q_text is None:
                return gr.update(value="No question found"), gr.update(choices=[])
            return gr.update(value=q_text), gr.update(choices=opts)

        # Link the dropdown change event to update_question
        question_dropdown.change(
            fn=update_question,
            inputs=[question_dropdown],
            outputs=[question_display, options_radio]
        )

        # This function is called when the user clicks "Check"
        def on_check(question_text, user_choice):
            q_index = question_list.index(question_text)
            return check_answer(user_choice, q_index)

        check_button = gr.Button("Check")
        check_button.click(
            fn=on_check,
            inputs=[question_display, options_radio],
            outputs=[feedback_box]
        )

    return demo

# 6) Launch the Gradio app if the script is run directly
if __name__ == "__main__":
    demo = build_quiz_app()
    demo.launch()
    # demo.launch(share = Ture) # If you want to create public URL