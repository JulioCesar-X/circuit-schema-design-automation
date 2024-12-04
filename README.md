# circuit-schema-design-automation
An automated environment for circuit design projects using Python and Schemdraw, optimized for Arch Linux.

---

## Features
- **Pre-configured project skeleton** for easy setup.
- **Dynamic circuit visualization**.
- Option to **save designs as PNG images**.
- **Automation script** for creating new projects effortlessly.

---

## Getting Started

### Requirements

1. **Install Python and pip**:
   ```bash
   sudo pacman -S python python-pip
   ```

2. **(Optional) Install Git and VS Code**:
   ```bash
   sudo pacman -S git code
   ```

3. **Install Virtualenv Tools**:
   ```bash
   sudo pacman -S python-virtualenv
   ```

---

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JulioCesar-X/circuit-schema-design-automation.git
   cd circuit-design-automation
   ```

2. **Set Up the Skeleton**:
   Navigate to `default_project/` and initialize the virtual environment:
   ```bash
   cd default_project
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the Base Code**:
   ```bash
   python main.py
   ```

---

### Usage

#### Create a New Project
Use the automation script to generate a new project:
```bash
python create_project.py
```

Example:
```bash
Enter the name of the new project: interactive_circuit
Project 'interactive_circuit' successfully created in: ./interactive_circuit
```

#### Navigate to the New Project
```bash
cd interactive_circuit
```

#### Execute the Main Script
```bash
python main.py
```

You’ll see:
1. The circuit displayed on your screen.
2. A prompt to save the circuit:
   ```bash
   Do you want to save the circuit as .png? (y/n):
   ```
   Choose `y` to save it in the `assets/` folder.

#### View Saved Image
```bash
xdg-open assets/circuit_xxxx-xx-xx_.png
```
---

### Contributing

Contributions are welcome!

---