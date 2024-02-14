# Gradient AI Model Adapter Example

This Python script demonstrates the creation, fine-tuning, and utilization of a model adapter using the GradientAI library. It showcases how to set up environment variables for workspace and API access, initialize a new model adapter, fine-tune it with custom training samples, and generate responses based on queries.

## Installation

Before running the script, ensure you have installed the necessary library:

```bash
pip install gradientai --upgrade
```

## Configuration

The script uses environment variables for the Gradient workspace ID and access token. Replace the placeholder values in the script with your actual Gradient workspace ID and access token:
```bash
os.environ['GRADIENT_WORKSPACE_ID'] = 'your_workspace_id'
os.environ['GRADIENT_ACCESS_TOKEN'] = 'your_access_token'
```

## Usage
Run the script directly in your Python environment:
```bash
python your_script_name.py
```
Replace your_script_name.py with the name of your Python script file.

The script performs the following actions:
- Initializes a new model adapter using the GradientAI library.
- Stores the adapter's details for later use.
- Generates a response for a sample query.
- Fine-tunes the model adapter with provided training data.
- Generates a new response after fine-tuning.

## Customization
You can customize the training samples, number of fine-tuning iterations, and queries by modifying the training_data, iterations, and initial_query variables in the script.

## Sample Training Data

The script includes sample training data focused on a fictional character 'Aliyu Abubakar'. Update this data to reflect the context and information relevant to your application.

## Fine-tuning and Generation

The script shows how to fine-tune the adapter with your data and generate responses before and after fine-tuning. Observe the changes in responses to assess the impact of your training data.

## Note
Ensure you have proper access rights and have set up the correct environment variables for using Gradient AI services.

### **INFERENCE**
## Q&A Bot with Tkinter Interface

This section of the script demonstrates the integration of a Q&A Bot within a graphical user interface (GUI) built using Tkinter, the standard GUI toolkit for Python. It allows users to input questions and receive responses directly within the application window.

### Additional Dependencies

Ensure you have Tkinter installed, which is typically included with Python. If for some reason it's not installed, you can install it based on your operating system's package manager or Python distribution.

### Running the Tkinter Application

To run the application with the Tkinter GUI:

1. Execute the script normally through your Python environment:

    ```bash
    python your_script_name.py
    ```

    Replace `your_script_name.py` with the name of your Python script file.

2. The application window titled "Q&A Bot" should appear. You can enter your questions in the provided text area and click the 'Ask' button to generate a response.

### Interface Components

- **Question Entry**: A scrolled text area where you can type the question you want to ask the bot.
- **Ask Button**: Submit your question to the model for generating a response.
- **Clear Button**: Clears the question and answer fields for a new query.
- **Answer Display**: A disabled scrolled text area where the response from the bot is displayed.

### Customization

You can customize the script to load different model adapters or change the GUI layout and functionalities according to your needs.

### Model Adapter and GUI Interaction

The GUI application initializes a model adapter using the Gradient AI library and interacts with it to generate responses based on user input. The responses are then displayed within the GUI, providing an interactive experience.

### Note

Ensure the environment variables for the Gradient workspace ID and access token are correctly set before running the GUI application. Also, make sure the `adapter_details.json` file exists and contains valid information about the initialized model adapter.
