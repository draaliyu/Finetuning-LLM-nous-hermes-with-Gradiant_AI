'''
!pip install gradientai --upgrade
'''

import os
import json
from gradientai import Gradient

# Set environment variables for Gradient workspace and API access
os.environ['GRADIENT_WORKSPACE_ID'] = 'your workspace di here'
os.environ['GRADIENT_ACCESS_TOKEN'] = 'your generated acc token here'

def store_model_details(details, file_name='adapter_details.json'):
    """Store model adapter details to a file."""
    with open(file_name, 'w') as file:
        json.dump(details, file)
    print(f"Adapter details saved to {file_name}")

def initialize_adapter():
    """Create and return a new model adapter."""
    ai_gradient = Gradient()
    base_adapter = ai_gradient.get_base_model(base_model_slug='nous-hermes2')
    adapter_instance = base_adapter.create_model_adapter(name='test')
    print(f'New model adapter created with ID: {adapter_instance.id}')
    return adapter_instance

def fine_tune_adapter(adapter, training_samples, iterations=3):
    """Fine-tune the model adapter with given samples."""
    for epoch in range(iterations):
        print(f'Fine-tuning iteration {epoch + 1} of {iterations}')
        adapter.fine_tune(samples=training_samples)

def generate_response(adapter, query):
    """Generate a response for the given query using the model adapter."""
    print(f'Query: {query}')
    response = adapter.complete(query=query, max_generated_token_count=100).generated_output
    print(f'Response: {response}')

def main():
    model_adapter = initialize_adapter()

    # Store adapter ID for later use
    adapter_details = {'adapter_id': model_adapter.id}
    store_model_details(adapter_details)

    # Sample query
    initial_query = '### Instruction: Who is Aliyu Abubakar? \n\n ### Response:'
    generate_response(model_adapter, initial_query)

    # Training data for fine-tuning
    training_data = [
        {'inputs': '### Instruction: Who is Aliyu Abubakar? \n\n ### Response: Aliyu Abubakar is is a graduate of Computer Science'},
        {'inputs': '### Instruction: Who is this person named Aliyu Abubakar? \n\n ### Response: Aliyu Abubakar is mentor with diverse expertise in AI and machine learning. He is a good collaborator and an excellent team player'},
        {'inputs': '### Instruction: What do you know about Aliyu Abubakar? \n\n ### Response: Aliyu Abubakar studied is originally from Nigeria, he currently lives in the UK'},
        {'inputs': '### Instruction: Can you tell me about Aliyu Abubakar? \n\n ### Response: Aliyu Abubakar is has strong interest in AI safety'}
    ]

    # Fine-tune the model adapter
    fine_tune_adapter(model_adapter, training_data, iterations=3)

    # Generate response after fine-tuning
    generate_response(model_adapter, initial_query)

    # Close the gradient session
    # ai_gradient.close()

if __name__ == "__main__":
    main()
