# aplab/components/code_editor.py

import streamlit as st
import streamlit.components.v1 as components

from aplab_py.config.styles import COLORS


class CodeEditor:
    @staticmethod
    def create(initial_code="", height=400, packages=None):
        if packages is None:
            packages = ["numpy", "pandas"]

        packages_str = '", "'.join(packages)

        components.html(f"""
            <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
            <script defer src="https://pyscript.net/latest/pyscript.js"></script>
            
            <py-config>
                packages = ["{packages_str}"]
            </py-config>
            
            <style>
                .py-repl {{
                    width: 100%;
                    min-height: {height-100}px;
                    background-color: {COLORS['background']['dark']};
                    border-radius: 8px;
                    padding: 10px;
                    margin: 10px 0;
                    color: {COLORS['text']['light']};
                }}
                .py-repl-output {{
                    background-color: #2d2d2d;
                    padding: 10px;
                    margin-top: 10px;
                    border-radius: 4px;
                    color: {COLORS['text']['light']};
                }}
                .py-config {{
                    color: {COLORS['text']['light']};
                }}
            </style>
            
            <py-repl auto-generate="true">
{initial_code}
            </py-repl>
        """, height=height)

    @staticmethod
    def create_with_examples(examples=None, height=400):
        if examples is None:
            examples = {
                "Hello World": 'print("Hello, World!")',
                "Basic Math": """
# Basic mathematics
a = 10
b = 5
print(f"Sum: {a + b}")
print(f"Product: {a * b}")
""",
                "Lists and Loops": """
# Working with lists
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Square of {num} is {num ** 2}")
""",
                "Functions": """
# Define and use a function
def greet(name):
    return f"Hello, {name}!"

print(greet("Python Learner"))
"""
            }

        example = st.selectbox(
            "Choose an example:",
            list(examples.keys())
        )

        CodeEditor.create(examples[example], height)