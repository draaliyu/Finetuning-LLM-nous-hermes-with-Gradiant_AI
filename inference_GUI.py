import tkinter as tk
from tkinter import scrolledtext
import os
import json
from gradientai import Gradient

# Set environment variables for Gradient workspace and access token
os.environ['GRADIENT_WORKSPACE_ID'] = 'your-workspace_id'
os.environ['GRADIENT_ACCESS_TOKEN'] = 'your_access_token'

def load_model_info(file_path='adapter_details.json'):
    """Load model information from a JSON file."""
    with open(file_path, 'r') as file:
        model_info = json.load(file)
    return model_info

def get_response(user_query, model_adapter):
    """Generate a response using the loaded model adapter."""
    sample_query = f'### Instruction: {user_query} \n\n ### Response:'
    completion = model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
    return completion

def main_gui():
    root = tk.Tk()
    root.title("Q&A Bot")

    def on_ask():
        user_query = question_entry.get("1.0", "end-1c")  # Get user input from text area
        full_response = get_response(user_query, model_adapter)

        # Assuming the answer is separated by a known delimiter or pattern from the question, extract it.
        # For demonstration, let's assume "Helpful answer:" is part of the response to indicate the start of the answer.
        # Adjust the delimiter as needed based on the actual response format.
        answer_start = full_response.find("Helpful answer:")
        if answer_start != -1:
            answer = full_response[answer_start + len("Helpful answer:"):].strip()
        else:
            answer = full_response  # Fallback if the delimiter isn't found

        answer_text.config(state=tk.NORMAL)
        answer_text.delete('1.0', tk.END)
        answer_text.insert(tk.END, answer)
        answer_text.config(state=tk.DISABLED)

    def on_clear():
        question_entry.delete('1.0', tk.END)
        answer_text.config(state=tk.NORMAL)
        answer_text.delete('1.0', tk.END)
        answer_text.config(state=tk.DISABLED)

    # Load model information and initialize Gradient
    model_info = load_model_info()
    model_adapter_id = model_info.get('model_adapter_id')
    gradient = Gradient()
    model_adapter = gradient.get_model_adapter(model_adapter_id=model_adapter_id)

    question_label = tk.Label(root, text="Enter your question:")
    question_label.pack()

    question_entry = scrolledtext.ScrolledText(root, height=5)
    question_entry.pack()

    ask_button = tk.Button(root, text="Ask", command=on_ask)
    ask_button.pack()

    clear_button = tk.Button(root, text="Clear", command=on_clear)
    clear_button.pack()

    answer_label = tk.Label(root, text="Answer:")
    answer_label.pack()

    answer_text = scrolledtext.ScrolledText(root, height=10, state=tk.DISABLED)
    answer_text.pack()

    root.mainloop()

if __name__ == "__main__":
    main_gui()
