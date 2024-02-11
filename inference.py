import json
from gradientai import Gradient
import os

# Set environment variables for Gradient workspace and access token
os.environ['GRADIENT_WORKSPACE_ID'] = 'your workspace di here'
os.environ['GRADIENT_ACCESS_TOKEN'] = 'your generated acc token here'

def load_model_info(file_path='model_info.json'):
    """Load model information from a JSON file."""
    with open(file_path, 'r') as file:
        model_info = json.load(file)
    return model_info

def main():
    # Load model information
    model_info = load_model_info()
    model_adapter_id = model_info.get('model_adapter_id')
    print(f"Loaded model adapter ID: {model_adapter_id}")
    if not model_adapter_id:
        print("Model adapter ID not found.")
        return

    # Initialize Gradient and load the model adapter by ID
    gradient = Gradient()
    model_adapter = gradient.get_model_adapter(model_adapter_id=model_adapter_id)

    if not model_adapter:
        print(f"Failed to load model adapter with ID: {model_adapter_id}")
        return

    while True:
        # Ask for the user to type the query prompt
        print("Please type your query prompt or type 'exit' to quit:")
        user_query = input("### Instruction: ")
        if user_query.lower() == 'exit':  # Check if the user wants to exit
            print("Exiting...")
            break

        sample_query = f'### Instruction: {user_query} \n\n ### Response:'

        # Perform inference
        print(f'Asking: {sample_query}')
        completion = model_adapter.complete(query=sample_query, max_generated_token_count=100).generated_output
        print(f'Generated: {completion}')
        print("\nAsk another question or type 'exit' to quit.")

    # Clean up or close the session as needed
    gradient.close()

if __name__ == "__main__":
    main()
