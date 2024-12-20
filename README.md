# APlab 🔬

Interactive Python learning platform with hands-on examples and visualizations.

## 📚 Topics

### 1. Python Basics
1.1. Variables and Memory
1.2. Data Types
1.3. Basic Operations

### 2. Control Flow
2.1. Conditional Statements
2.2. Loops and Iterations
2.3. Functions

### 3. Data Structures
3.1. Lists and Arrays
3.2. Dictionaries
3.3. Sets and Tuples

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- Poetry (Python package manager)

### Installation

1. Install Poetry if you haven't already:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Clone the repository:
```bash
git clone https://github.com/yourusername/APlab.git
cd APlab
```

3. Install dependencies:
```bash
poetry install
```

4. Run the application:
```bash
poetry shell
streamlit run aplab_py/app.py
```

## 💻 Development

### Project Structure
```
APlab/
├── pyproject.toml          # Poetry configuration
├── poetry.lock            # Locked dependencies
├── aplab/
│   ├── __init__.py
│   ├── app.py            # Main Streamlit application
│   └── topics/           # Interactive examples
│       ├── 01_basics/
│       ├── 02_control_flow/
│       └── 03_data_structures/
└── tests/                # Test files
```

### Adding New Topics

1. Create a new Python file in the appropriate topic directory
2. Follow the template structure:
```python
import streamlit as st

def show():
    st.header("Topic Title")
    # Your interactive content here
```

## 🤝 Support

...

---
Made with ❤️ by AP