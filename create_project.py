import os
import shutil

DEFAULT_DIR_NAME = 'default_project'
PROJECTS_BASE_DIR = os.path.expanduser('~/dev/projects')

def ensure_directory_exists(directory):
    """
    Ensures the specified directory exists, creating it if necessary.

    Args:
        directory (str): Path to the directory to ensure existence.
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory '{directory}': {e}")
        raise

def get_project_paths(project_name):
    """
    Get paths for the default directory and the new project directory.

    Args:
        project_name (str): The name of the new project.

    Returns:
        tuple: Paths to the default directory and the new project directory.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    default_dir = os.path.join(base_dir, DEFAULT_DIR_NAME)
    new_project_dir = os.path.join(PROJECTS_BASE_DIR, project_name)
    return default_dir, new_project_dir

def copy_directory(src, dest, ignore_patterns=None):
    """
    Copies a directory from source to destination.

    Args:
        src (str): Source directory path.
        dest (str): Destination directory path.
        ignore_patterns (list, optional): List of patterns to ignore during the copy.
    """
    try:
        shutil.copytree(
            src, 
            dest, 
            ignore=shutil.ignore_patterns(*ignore_patterns) if ignore_patterns else None
        )
        print(f"Project '{os.path.basename(dest)}' successfully created at: {dest}")
    except Exception as e:
        print(f"Error copying directory from '{src}' to '{dest}': {e}")
        raise

def display_next_steps(project_name):
    """
    Displays next steps to the user after project creation.

    Args:
        project_name (str): The name of the new project.
    """
    project_path = os.path.join(PROJECTS_BASE_DIR, project_name)
    print("\nNext Steps:")
    print(f"1. Navigate to the project directory: cd {project_path}")
    print("2. Run: python -m venv venv to create a virtual environment.")
    print("3. Run: source venv/bin/activate to activate the virtual environment.")
    print("4. Install required packages: pip install -r requirements.txt")
    print("5. Run: python main.py to view your circuit diagram.")
    print("5. good working into your project!")

def create_project(project_name):
    """
    Main function to create a new project by copying the default directory.

    Args:
        project_name (str): The name of the new project.
    """
    ensure_directory_exists(PROJECTS_BASE_DIR)
    default_dir, new_project_dir = get_project_paths(project_name)

    if os.path.exists(new_project_dir):
        print(f"Error: The directory '{new_project_dir}' already exists!")
        return

    copy_directory(default_dir, new_project_dir, ignore_patterns=['venv'])
    display_next_steps(project_name)

if __name__ == "__main__":
    project_name = input("Enter the name of the new project: ").strip()
    if project_name:
        create_project(project_name)
    else:
        print("Error: Project name cannot be empty.")