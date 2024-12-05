import schemdraw
import schemdraw.elements as elm
import os
import shutil
import tempfile
from datetime import datetime

OUTPUT_DIR = 'assets'
OUTPUT_FILE_FORMAT = 'project_{timestamp}_circuit.png'

def create_directory_if_needed(directory):
    """
    Ensures the specified directory exists, creating it if necessary.

    Args:
        directory (str): Path to the directory to create.
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory '{directory}': {e}")
        raise

def generate_output_filename():
    """
    Generates a unique filename using the current date and time.

    Returns:
        str: The dynamically generated filename.
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return OUTPUT_FILE_FORMAT.format(timestamp=timestamp)

def save_circuit_temp(drawing):
    """
    Saves the circuit drawing to a temporary file and returns its path.

    Args:
        drawing (schemdraw.Drawing): The circuit drawing to save.

    Returns:
        str: Path to the temporary file.
    """
    try:
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            drawing.save(temp_file.name)
            return temp_file.name
    except Exception as e:
        print(f"Error saving temporary file: {e}")
        raise

def move_to_final_directory(temp_file, directory):
    """
    Moves a temporary file to the final directory with a dynamically generated name.

    Args:
        temp_file (str): Path to the temporary file.
        directory (str): Path to the final directory.
    """
    try:
        create_directory_if_needed(directory)
        final_path = os.path.join(directory, generate_output_filename())
        shutil.move(temp_file, final_path)  # Moves the file
        print(f"Circuit saved to '{final_path}'.")
    except Exception as e:
        print(f"Error moving file to final directory: {e}")
        raise

def draw_circuit():
    """
    Creates, displays, and optionally saves a simple circuit diagram.
    """
    try:
        drawing = schemdraw.Drawing()
        # Modify the code below to create a new circuit diagram
        # ------------------------------------------------------- #
	
        drawing += elm.Resistor().label("R1")  # Add a resistor
        drawing += elm.Capacitor().label("C1")  # Add a capacitor
	
	    # ------------------------------------------------------- #
        temp_file = save_circuit_temp(drawing)
        drawing.draw(show=True)
        print("\nThe circuit diagram has been displayed.")

        while True:
            response = input("Would you like to save the circuit as a PNG file? (y/n): ").strip().lower()
            if response in ('y', 'n'):
                break
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        if response == 'y':
            move_to_final_directory(temp_file, OUTPUT_DIR)
        else:
            os.remove(temp_file)
            print("The circuit diagram was not saved.")

    except Exception as e:
        print(f"An error occurred while drawing or saving the circuit: {e}")

if __name__ == "__main__":
    draw_circuit()
