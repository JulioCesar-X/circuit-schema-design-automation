import os
import shutil

# Constants
DEFAULT_DIR_NAME = 'default_project'
PROJECTS_BASE_DIR = os.path.expanduser('~/dev/projects')

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

def create_projects_base_dir():
    """
    Ensures the base projects directory exists, creating it if necessary.
    """
    try:
        os.makedirs(PROJECTS_BASE_DIR, exist_ok=True)
    except OSError as e:
        print(f"Error creating base projects directory: {e}")
        raise

def copy_default_project(default_dir, new_project_dir):
    """
    Copies the default directory to create a new project.

    Args:
        default_dir (str): Path to the default directory.
        new_project_dir (str): Path to the new project directory.
    """
    try:
        shutil.copytree(default_dir, new_project_dir)
        print(f"Project '{os.path.basename(new_project_dir)}' successfully created at: {new_project_dir}")
    except Exception as e:
        print(f"Error copying default project: {e}")
        raise

def display_next_steps(project_name):
    """
    Displays next steps to the user after project creation.

    Args:
        project_name (str): The name of the new project.
    """
    print("\nNext Steps:")
    print(f"1. Navigate to the project directory: cd {os.path.join(PROJECTS_BASE_DIR, project_name)}")
    print("2. Run: python main.py to view your circuit diagram.")

def create_project(project_name):
    """
    Main function to create a new project by copying the default directory.

    Args:
        project_name (str): The name of the new project.
    """
    create_projects_base_dir()
    default_dir, new_project_dir = get_project_paths(project_name)

    if os.path.exists(new_project_dir):
        print(f"Error: The directory '{new_project_dir}' already exists!")
        return

    copy_default_project(default_dir, new_project_dir)
    display_next_steps(project_name)

if __name__ == "__main__":
    project_name = input("Enter the name of the new project: ").strip()
    if project_name:
        create_project(project_name)
    else:
        print("Error: Project name cannot be empty.")