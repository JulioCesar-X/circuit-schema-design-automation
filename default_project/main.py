import schemdraw
import schemdraw.elements as elm
import os
from datetime import datetime

# Constants for the output directory and file format
OUTPUT_DIR = 'assets'
OUTPUT_FILE_FORMAT = 'project_{timestamp}_circuit.png'

def create_directory_if_needed(directory):
    """
    Ensures the specified directory exists, creating it if necessary.

    Args:
        directory (str): The path to the directory to create.
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {directory}: {e}")
        raise

def generate_output_filename():
    """
    Generates a dynamic filename using the current date and time.

    Returns:
        str: The dynamically generated filename.
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return OUTPUT_FILE_FORMAT.format(timestamp=timestamp)

def save_circuit(drawing, directory):
    """
    Saves the circuit drawing to a PNG file with a dynamic filename.

    Args:
        drawing (schemdraw.Drawing): The circuit drawing to save.
        directory (str): The directory where the file will be saved.
    """
    create_directory_if_needed(directory)
    filename = generate_output_filename()
    file_path = os.path.join(directory, filename)
    drawing.save(file_path)
    print(f"Circuit saved to '{file_path}'.")

def draw_circuit():
    """
    Creates, displays, and optionally saves a simple circuit diagram.
    """
    try:
        # Initialize the drawing
        drawing = schemdraw.Drawing()
        
        # Modify the code below to create a new circuit diagram
        # ------------------------------------------------------- #
	
        drawing += elm.Resistor().label("R1")  # Add a resistor
        drawing += elm.Capacitor().label("C1")  # Add a capacitor
	
	    # ------------------------------------------------------- #

        # Display the circuit diagram
        drawing.draw(show=True)
        print("\nThe circuit diagram has been displayed.")

        # Ask the user if they want to save the diagram
        response = input("Would you like to save the circuit as a PNG file? (y/n): ").strip().lower()
        if response == 'y':
            save_circuit(drawing, OUTPUT_DIR)
        else:
            print("The circuit diagram was not saved.")
    except Exception as e:
        print(f"An error occurred while drawing or saving the circuit: {e}")

if __name__ == "__main__":
    draw_circuit()
