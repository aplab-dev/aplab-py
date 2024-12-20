# aplab/topics/t00_fundamentals/t01_programming_basics.py

from typing import List, Dict
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from aplab_py.components.code_editor import CodeEditor
from aplab_py.components.visualizations import create_flow_chart
from aplab_py.config.styles import (
    COLORS,
    TEXT_STYLES,
    CHART_STYLES
)

def create_sandwich_maker() -> Dict:
    """Creates the sandwich making exercise data"""
    return {
        "steps": [
            "Locate the bread bag",
            "Check if bread bag is open",
            "Get a plate",
            "Take bread from the bag",
            "Place bread on plate",
            "Put ingredients on the bread",
            "Close the sandwich",
            "Cut the sandwich"
        ],
        "tips": [
            "Don't assume the robot knows anything",
            "Break down every action",
            "Order matters!"
        ]
    }

def create_program_flow_chart():
    """Creates the program flow visualization"""
    nodes = ['Input', 'Process', 'Output']
    return create_flow_chart(nodes)

def show():
    """Main function to display the programming basics content"""

    st.header("0. Introduction to Programming and Algorithmic Thinking")

    st.markdown("""
    Before diving into Python, let's understand the fundamentals of programming 
    and how to think like a programmer. This will make learning any programming 
    language much easier!
    """)

    # Main Navigation
    tab1, tab2, tab3, tab4 = st.tabs([
        "🧠 What is Programming?",
        "🔄 Algorithmic Thinking",
        "🎯 Problem Solving",
        "🔨 Programming Tools"
    ])

    # 1. WHAT IS PROGRAMMING
    with tab1:
        st.markdown("""
        ## What is Programming? 🤔
        
        Imagine you're teaching a very intelligent robot to do tasks. This robot:
        - ✅ Is incredibly fast and accurate
        - ✅ Never gets tired
        - ✅ Follows instructions perfectly
        - ❌ But can't understand context or guess what you mean
        
        Programming is writing these instructions in a way the computer can understand.
        """)

        # Interactive Example 1: Robot Instructions
        with st.expander("🤖 Robot Instructions Example"):
            st.markdown("""
            ### Make a Sandwich Challenge
            
            Imagine you're programming a robot to make a sandwich. The robot needs 
            **exact, ordered instructions**. It can't guess or assume anything!
            
            Drag and arrange the steps in the correct order:
            """)

            # Define the correct sequence
            correct_sequence = [
                "Locate the bread bag",
                "Check if bread bag is open",
                "Get a plate",
                "Take bread from the bag",
                "Place bread on plate",
                "Put ingredients on the bread",
                "Close the sandwich",
                "Cut the sandwich"
            ]

            # Create selection interface
            selected_steps = st.multiselect(
                "Drag steps in the correct order:",
                correct_sequence,  # Use the same list for options
                [],  # Start with empty selection
                help="Click or drag steps in the order they should be performed"
            )

            # Only show feedback if steps have been selected
            if selected_steps:
                # Check if all steps are present and in correct order
                if selected_steps == correct_sequence:
                    st.success("""
                    🎉 Perfect! You've thought like a programmer:
                    1. ✅ Considered all necessary steps
                    2. ✅ Put them in logical order
                    3. ✅ Didn't skip obvious steps
                    
                    This is exactly how we need to think when programming!
                    """)
                else:
                    # Find what's missing or out of order
                    if len(selected_steps) < len(correct_sequence):
                        missing = [s for s in correct_sequence if s not in selected_steps]
                        st.warning(f"Missing steps: {', '.join(missing)}")
                    else:
                        st.error("""
                        Steps are in wrong order. Remember:
                        - Start with preparation steps
                        - Follow logical sequence
                        - Think about dependencies
                        """)

        # Program Flow Section
        st.markdown("""
        ### How Programs Work 🔄
        
        Every program follows a basic flow:
        1. 📥 **INPUT**: Get data or information
        2. ⚙️ **PROCESS**: Do something with it
        3. 📤 **OUTPUT**: Show or save the result
        """)

        # Create improved flow chart
        nodes = ['INPUT', 'PROCESS', 'OUTPUT']
        fig = go.Figure()

        # Add nodes with better styling
        x_positions = [0, 1, 2]
        colors = ['#4361EE', '#3A0CA3', '#7209B7']  # Better color scheme

        # Add nodes
        fig.add_trace(go.Scatter(
            x=x_positions,
            y=[0, 0, 0],
            mode='markers+text',
            marker=dict(
                size=50,
                color=colors,
                line=dict(color='white', width=2)
            ),
            text=nodes,
            textfont=dict(
                size=14,
                color='white',
                family='Arial Bold'
            ),
            textposition='middle center'
        ))

        # Add arrows
        for i in range(len(nodes)-1):
            fig.add_annotation(
                x=x_positions[i]+0.5,
                y=0,
                ax=x_positions[i],
                ay=0,
                xref='x',
                yref='y',
                axref='x',
                ayref='y',
                text='',
                showarrow=True,
                arrowhead=2,
                arrowsize=1.5,
                arrowwidth=2,
                arrowcolor='white'
            )

        # Update layout
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                range=[-0.5, 2.5]
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                range=[-0.5, 0.5]
            ),
            margin=dict(l=20, r=20, t=20, b=20),
            height=150,
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

        # Interactive Program Example
        st.markdown("### 🎮 Try a Simple Program")

        with st.expander("Interactive Program Example"):
            st.markdown("""
            Let's create a simple greeting program that shows all three parts of program flow:
            
            1. **INPUT**: Get your name
            2. **PROCESS**: Create a personalized greeting
            3. **OUTPUT**: Display the result
            """)

            col1, col2 = st.columns(2)

            with col1:
                # Input
                name = st.text_input("👤 Enter your name:",
                                     placeholder="Type your name here...")

                # Process & Output
                if name:
                    greeting = f"Hello, {name}! Welcome to programming! 🎉"
                    st.success(greeting)

            with col2:
                if name:
                    st.markdown("#### How it works:")
                    st.code(f"""
# 1. INPUT
name = "{name}"

# 2. PROCESS
greeting = f"Hello, {name}!"

# 3. OUTPUT
print(greeting)
                    """)

        # First Code Example
        st.markdown("""
        ### 👨‍💻 Your First Python Code
        
        Try these simple examples to see how Python works:
        """)

        CodeEditor.create_with_examples({
            "Hello World": '''# The classic first program
print("Hello, World!")
print("I'm learning Python!")''',

            "Simple Math": '''# Python as a calculator
number1 = 10
number2 = 5

print(f"Addition: {number1} + {number2} = {number1 + number2}")
print(f"Multiplication: {number1} × {number2} = {number1 * number2}")''',

            "Name Greeter": '''# Interactive program
name = input("What's your name? ")
age = input("How old are you? ")
print(f"Nice to meet you, {name}!")
print(f"You are {age} years old.")'''
        })

        # Tips for Beginners
        with st.expander("💡 Tips for Success"):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("""
                ### Getting Started
                1. **Start Small**
                   - Begin with simple programs
                   - Practice basic concepts
                   - Build gradually
                
                2. **Learn by Doing**
                   - Type code yourself
                   - Experiment with examples
                   - Make mistakes and learn
                """)

            with col2:
                st.markdown("""
                ### Common Mistakes to Avoid
                1. **Don't Rush**
                   - Understand each concept
                   - Take time to practice
                   - Ask questions
                
                2. **Keep it Simple**
                   - One concept at a time
                   - Clear, readable code
                   - Regular practice
                """)

    # 2. ALGORITHMIC THINKING
    with tab2:
        st.markdown("""
        ## Algorithmic Thinking 🧮
        
        An algorithm is a step-by-step procedure to solve a problem, like a detailed recipe.
        
        ### Key Components of an Algorithm:
        1. 📥 **Input**: Starting materials/data
        2. 📝 **Steps**: Clear, ordered instructions
        3. 🎯 **Decisions**: Handling different situations
        4. 📤 **Output**: Final result
        """)

        # Algorithm Explorer
        st.markdown("### 🎮 Algorithm Explorer")

        algorithm_choice = st.selectbox(
            "Choose an algorithm to explore:",
            ["🫖 Making Tea", "🔢 Finding Largest Number", "📊 Sorting Numbers"]
        )

        if algorithm_choice == "🫖 Making Tea":
            st.markdown("""
            #### Making the Perfect Cup of Tea
            Let's break down tea-making into a precise algorithm.
            """)

            col1, col2 = st.columns(2)

            with col1:
                tea_type = st.selectbox(
                    "Select tea type:",
                    ["Black Tea", "Green Tea", "Herbal Tea"]
                )

                # Tea requirements dictionary
                tea_requirements = {
                    "Black Tea": {"temp": 90, "time": 3},
                    "Green Tea": {"temp": 80, "time": 2},
                    "Herbal Tea": {"temp": 95, "time": 4}
                }

                water_temp = st.slider(
                    "Water temperature (°C):",
                    40, 100,
                    tea_requirements[tea_type]["temp"]
                )

                steep_time = st.slider(
                    "Steeping time (minutes):",
                    0, 7,
                    tea_requirements[tea_type]["time"]
                )

            with col2:
                st.markdown(f"""
                #### Requirements for {tea_type}:
                - Ideal Temperature: {tea_requirements[tea_type]["temp"]}°C
                - Ideal Steeping Time: {tea_requirements[tea_type]["time"]} minutes
                """)

                # Check conditions
                temp_ok = water_temp >= tea_requirements[tea_type]["temp"] - 5
                time_ok = steep_time >= tea_requirements[tea_type]["time"]

                # Visual feedback with emojis
                st.markdown("#### Status Check:")
                st.markdown(f"Temperature: {'✅' if temp_ok else '❌'}")
                st.markdown(f"Steep Time: {'✅' if time_ok else '❌'}")

                if temp_ok and time_ok:
                    st.success("Perfect cup of tea! 🫖")
                else:
                    st.warning("Adjust parameters for better tea")

            # Show the algorithm
            st.markdown("#### The Algorithm:")
            st.code(f"""
def make_tea(tea_type, water_temp, steep_time):
    # 1. Check tea requirements
    required_temp = {tea_requirements[tea_type]["temp"]}
    required_time = {tea_requirements[tea_type]["time"]}
    
    # 2. Check water temperature
    if water_temp < required_temp - 5:
        return "Water too cold"
    
    # 3. Check steeping time
    if steep_time < required_time:
        return "Need more steeping time"
    
    # 4. All conditions met
    return "Perfect cup of tea!"

# Run the algorithm
result = make_tea("{tea_type}", {water_temp}, {steep_time})
print(result)
            """)

        elif algorithm_choice == "🔢 Finding Largest Number":
            st.markdown("""
            #### Finding the Largest Number
            Watch how we find the largest number in a list step by step.
            """)

            # Input numbers
            numbers_input = st.text_input(
                "Enter numbers separated by commas:",
                "42, 17, 23, 8, 91, 31"
            )

            try:
                numbers = [float(x.strip()) for x in numbers_input.split(",")]

                # Initialize variables for visualization
                current_max = numbers[0]
                steps = []

                # Process each number
                for i, num in enumerate(numbers):
                    is_new_max = num > current_max
                    if is_new_max:
                        current_max = num

                    steps.append({
                        'Step': i + 1,
                        'Number': num,
                        'Current Max': current_max,
                        'Is New Max?': '✅' if is_new_max else '❌'
                    })

                # Display steps in a table
                st.markdown("#### Algorithm Steps:")
                st.table(pd.DataFrame(steps))

                # Visualize the numbers
                fig = go.Figure()

                # Add bars for all numbers
                fig.add_trace(go.Bar(
                    x=list(range(len(numbers))),
                    y=numbers,
                    name='Numbers',
                    marker_color=[
                        COLORS['primary']['orange'] if n == max(numbers)
                        else COLORS['primary']['blue']
                        for n in numbers
                    ]
                ))

                fig.update_layout(
                    title='Numbers Visualization',
                    xaxis_title='Position',
                    yaxis_title='Value',
                    height=400,
                    showlegend=False
                )

                st.plotly_chart(fig)

                st.success(f"Largest number is: {max(numbers)}")

                # Show the algorithm
                st.markdown("#### The Algorithm:")
                st.code("""
def find_largest(numbers):
    if not numbers:  # Handle empty list
        return None
        
    largest = numbers[0]  # Start with first number
    
    for number in numbers:
        if number > largest:
            largest = number  # Update if we find bigger
            
    return largest
                """)

            except Exception as e:
                st.error("Please enter valid numbers separated by commas")
                st.error(f"Error: {str(e)}")

        else:  # Sorting Numbers
            st.markdown("""
            #### Bubble Sort Algorithm
            Watch how numbers get sorted step by step.
            """)

            # Input for sorting
            numbers_input = st.text_input(
                "Enter numbers to sort (comma-separated):",
                "64, 34, 25, 12, 22, 11, 90"
            )

            try:
                numbers = [int(x.strip()) for x in numbers_input.split(",")]

                def bubble_sort_steps(arr):
                    steps = [arr.copy()]
                    n = len(arr)

                    for i in range(n):
                        swapped = False
                        for j in range(0, n-i-1):
                            if arr[j] > arr[j+1]:
                                arr[j], arr[j+1] = arr[j+1], arr[j]
                                swapped = True
                                steps.append(arr.copy())
                        if not swapped:
                            break

                    return steps

                # Get sorting steps
                steps = bubble_sort_steps(numbers.copy())

                # Visualization controls
                step_number = st.slider(
                    "Move through sorting steps:",
                    0,
                    len(steps) - 1,
                    0
                )

                # Create visualization
                fig = go.Figure()

                # Add bars for current state
                fig.add_trace(go.Bar(
                    x=list(range(len(steps[step_number]))),
                    y=steps[step_number],
                    marker_color=COLORS['primary']['blue']
                ))

                fig.update_layout(
                    title=f'Step {step_number} of Bubble Sort',
                    xaxis_title='Position',
                    yaxis_title='Value',
                    height=400
                )

                st.plotly_chart(fig)

                # Show the algorithm
                st.markdown("#### The Algorithm:")
                st.code("""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they are in wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
                """)

            except Exception as e:
                st.error("Please enter valid numbers separated by commas")
                st.error(f"Error: {str(e)}")

        # Algorithm Design Tips
        st.markdown("""
        ### 💡 Algorithm Design Tips
        
        1. **Start Simple**
           - Begin with basic steps
           - Test with simple inputs
           - Add complexity gradually
        
        2. **Break It Down**
           - Split into smaller sub-tasks
           - Handle one piece at a time
           - Combine solutions
        
        3. **Consider Edge Cases**
           - Empty inputs
           - Invalid data
           - Extreme values
        
        4. **Optimize Later**
           - Make it work first
           - Make it right second
           - Make it fast last
        """)

    # 3. PROBLEM SOLVING
    with tab3:
        st.markdown("""
        ## Problem Solving Approach 🎯
        
        Learning to solve problems like a programmer involves a systematic approach:
        
        ### The 4-Step Process:
        1. 📋 **Understand** - Define the problem clearly
        2. 🔍 **Plan** - Break down into steps
        3. 💻 **Code** - Implement the solution
        4. 🔄 **Test & Refine** - Check and improve
        """)

        # Problem-Solving Explorer
        st.markdown("### 🎮 Problem-Solving Explorer")

        problem_type = st.selectbox(
            "Choose a problem to solve:",
            [
                "🌡️ Temperature Converter",
                "🎯 Grade Calculator",
                "🛒 Shopping Cart",
                "🎲 Password Generator"
            ]
        )

        if problem_type == "🌡️ Temperature Converter":
            st.markdown("""
            #### Temperature Converter
            Let's solve this step by step using our problem-solving approach.
            """)

            # Problem Understanding
            with st.expander("1. Understanding the Problem"):
                st.markdown("""
                **What do we need?**
                - Input: Temperature value and unit (C or F)
                - Output: Converted temperature
                - Formulas: 
                  - C to F: (C × 9/5) + 32
                  - F to C: (F - 32) × 5/9
                """)

            # Planning
            with st.expander("2. Planning the Solution"):
                st.markdown("""
                **Steps needed:**
                1. Get temperature value
                2. Get current unit
                3. Apply correct formula
                4. Round result
                5. Display result with unit
                """)

            # Implementation
            st.markdown("#### 3. Implementation:")

            col1, col2 = st.columns(2)

            with col1:
                temp = st.number_input("Enter temperature:", value=0.0)
                unit = st.selectbox("Select unit:", ["Celsius", "Fahrenheit"])

                if st.button("Convert"):
                    if unit == "Celsius":
                        result = (temp * 9/5) + 32
                        st.success(f"{temp}°C = {result:.1f}°F")
                    else:
                        result = (temp - 32) * 5/9
                        st.success(f"{temp}°F = {result:.1f}°C")

            with col2:
                st.markdown("#### The Code:")
                st.code("""
def convert_temperature(temp: float, unit: str) -> str:
    \"\"\"
    Convert temperature between Celsius and Fahrenheit.
    
    Args:
        temp: Temperature value
        unit: 'Celsius' or 'Fahrenheit'
    
    Returns:
        Converted temperature with unit
    \"\"\"
    if unit == "Celsius":
        result = (temp * 9/5) + 32
        return f"{temp}°C = {result:.1f}°F"
    else:
        result = (temp - 32) * 5/9
        return f"{temp}°F = {result:.1f}°C"
                """)

        elif problem_type == "🎯 Grade Calculator":
            st.markdown("""
            #### Grade Calculator
            Calculate final grade based on multiple assignments and weights.
            """)

            col1, col2 = st.columns(2)

            with col1:
                homework = st.slider("Homework (30%):", 0, 100, 75)
                midterm = st.slider("Midterm (30%):", 0, 100, 80)
                final = st.slider("Final (40%):", 0, 100, 85)

                final_score = (homework * 0.3) + (midterm * 0.3) + (final * 0.4)

                st.markdown("#### Results:")
                st.progress(final_score/100)
                st.write(f"Final Score: {final_score:.1f}%")

                # Grade calculation
                grade = (
                    'A' if final_score >= 90 else
                    'B' if final_score >= 80 else
                    'C' if final_score >= 70 else
                    'D' if final_score >= 60 else
                    'F'
                )

                if grade in ['A', 'B', 'C', 'D']:
                    st.success(f"Final Grade: {grade}")
                else:
                    st.error(f"Final Grade: {grade}")

            with col2:
                # Visualization of score distribution
                fig = go.Figure()

                components = ['Homework', 'Midterm', 'Final']
                scores = [homework, midterm, final]
                weights = [30, 30, 40]

                # Add bars
                fig.add_trace(go.Bar(
                    x=components,
                    y=scores,
                    text=[f"{s}%" for s in scores],
                    textposition='auto',
                    marker_color=[COLORS['primary']['blue']] * 3
                ))

                fig.update_layout(
                    title='Score Distribution',
                    yaxis_range=[0, 100],
                    height=300
                )

                st.plotly_chart(fig)

                # Show calculation
                st.code(f"""
# Grade calculation
homework = {homework} * 0.30 = {homework * 0.3:.1f}
midterm  = {midterm} * 0.30 = {midterm * 0.3:.1f}
final    = {final} * 0.40 = {final * 0.4:.1f}
                
final_score = {final_score:.1f}
grade = '{grade}'
                """)

        elif problem_type == "🛒 Shopping Cart":
            st.markdown("""
            #### Shopping Cart Calculator
            Calculate total price with discounts and tax.
            """)

            # Initialize session state for cart
            if 'cart' not in st.session_state:
                st.session_state.cart = []

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### Add Items")
                item_name = st.text_input("Item name:")
                item_price = st.number_input("Price ($):", min_value=0.0, value=10.0)
                item_quantity = st.number_input("Quantity:", min_value=1, value=1)

                if st.button("Add to Cart"):
                    st.session_state.cart.append({
                        'name': item_name,
                        'price': item_price,
                        'quantity': item_quantity
                    })
                    st.success(f"Added {item_name} to cart!")

            with col2:
                st.markdown("#### Cart Summary")

                if not st.session_state.cart:
                    st.info("Cart is empty")
                else:
                    # Calculate totals
                    subtotal = sum(item['price'] * item['quantity']
                                   for item in st.session_state.cart)
                    tax = subtotal * 0.1  # 10% tax
                    total = subtotal + tax

                    # Display cart items
                    for item in st.session_state.cart:
                        st.write(
                            f"{item['name']}: "
                            f"${item['price']} × {item['quantity']} = "
                            f"${item['price'] * item['quantity']:.2f}"
                        )

                    st.markdown("---")
                    st.write(f"Subtotal: ${subtotal:.2f}")
                    st.write(f"Tax (10%): ${tax:.2f}")
                    st.success(f"Total: ${total:.2f}")

                    if st.button("Clear Cart"):
                        st.session_state.cart = []
                        st.rerun()

        else:  # Password Generator
            st.markdown("""
            #### Password Generator
            Create secure passwords based on criteria.
            """)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### Set Password Criteria")
                length = st.slider("Password length:", 8, 32, 12)
                include_upper = st.checkbox("Include uppercase letters", True)
                include_lower = st.checkbox("Include lowercase letters", True)
                include_numbers = st.checkbox("Include numbers", True)
                include_special = st.checkbox("Include special characters", True)

            with col2:
                st.markdown("#### Password Strength")

                # Calculate strength
                strength = 0
                if include_upper: strength += 25
                if include_lower: strength += 25
                if include_numbers: strength += 25
                if include_special: strength += 25

                # Display strength meter
                st.progress(strength/100)
                st.write(f"Password Strength: {strength}%")

                # Strength assessment
                if strength < 50:
                    st.warning("⚠️ Weak password criteria")
                elif strength < 75:
                    st.info("ℹ️ Moderate password criteria")
                else:
                    st.success("✅ Strong password criteria")

            # Generate password
            if st.button("Generate Password"):
                import random
                import string

                # Build character set
                chars = ''
                if include_upper: chars += string.ascii_uppercase
                if include_lower: chars += string.ascii_lowercase
                if include_numbers: chars += string.digits
                if include_special: chars += string.punctuation

                if chars:
                    # Generate password
                    password = ''.join(random.choice(chars) for _ in range(length))

                    # Display password
                    st.code(password)

                    # Show password composition
                    st.markdown("#### Password Analysis:")
                    analysis = {
                        'Uppercase': sum(1 for c in password if c.isupper()),
                        'Lowercase': sum(1 for c in password if c.islower()),
                        'Numbers': sum(1 for c in password if c.isdigit()),
                        'Special': sum(1 for c in password if not c.isalnum())
                    }

                    for category, count in analysis.items():
                        st.write(f"{category}: {count} characters")
                else:
                    st.error("Please select at least one character type")

        # Problem-Solving Tips
        st.markdown("""
        ### 💡 Problem-Solving Tips
        
        1. **Understand First**
           - Read the problem carefully
           - Identify inputs and outputs
           - List all requirements
        
        2. **Plan Before Coding**
           - Break down the problem
           - Write pseudocode
           - Consider edge cases
        
        3. **Start Simple**
           - Begin with basic functionality
           - Add features gradually
           - Test each addition
        
        4. **Test Thoroughly**
           - Try different inputs
           - Check edge cases
           - Verify results
        """)

    # 4. PROGRAMMING TOOLS
    with tab4:
        st.markdown("""
        ## Programming Tools 🔨
        
        Modern programming uses various tools to make development easier and more efficient.
        Let's explore the essential tools every programmer needs.
        """)

        tool_category = st.selectbox(
            "Choose tool category:",
            [
                "👩‍💻 Code Editor",
                "⚡ Interactive Python",
                "📚 Documentation",
                "🔄 Version Control",
                "🐞 Debugging Tools"
            ]
        )

        if tool_category == "👩‍💻 Code Editor":
            st.markdown("""
            ### Code Editors and IDEs
            
            A code editor is your main programming workspace. Modern editors provide:
            - Syntax highlighting (colored code)
            - Auto-completion (code suggestions)
            - Error detection (find mistakes)
            - Code formatting (make code neat)
            """)

            # Popular Editors Comparison
            with st.expander("Popular Code Editors"):
                editors_df = pd.DataFrame({
                    'Editor': ['VS Code', 'PyCharm', 'Sublime Text', 'Jupyter'],
                    'Best For': [
                        'General purpose, beginners',
                        'Python specialists, large projects',
                        'Fast, lightweight editing',
                        'Data science, interactive coding'
                    ],
                    'Features': [
                        '✅ Free, ✅ Extensions, ✅ Integrated terminal',
                        '✅ Advanced features, ❌ Paid, ✅ Debugging',
                        '✅ Fast, ✅ Lightweight, ❌ Limited features',
                        '✅ Interactive, ✅ Visualization, ✅ Markdown'
                    ],
                    'Learning Curve': [
                        'Easy',
                        'Steep',
                        'Easy',
                        'Moderate'
                    ]
                })
                st.table(editors_df)

            # Interactive Editor Demo
            st.markdown("### 🎮 Try the Code Editor")

            CodeEditor.create_with_examples({
                "Syntax Highlighting": """
# Different colors for different parts
def greet(name):
    # This is a comment
    message = f"Hello, {name}!"
    return message

# Numbers and strings look different
age = 25
name = "Alice"
print(greet(name))
""",
                "Error Detection": """
# The editor shows errors
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # What if numbers is empty?

# Test with different inputs
print(calculate_average([1, 2, 3]))
print(calculate_average([]))  # This will cause an error
""",
                "Code Formatting": """
# The editor can format messy code
def  messy_function   (x,y,z):
    result=x+y*z
    return     result

# This becomes neat code when formatted
def messy_function(x, y, z):
    result = x + y * z
    return result
"""
            })

        elif tool_category == "⚡ Interactive Python":
            st.markdown("""
            ### Interactive Python (REPL)
            
            REPL stands for Read-Eval-Print Loop. It's like a conversation with Python:
            1. You type code (Read)
            2. Python understands it (Eval)
            3. Python shows results (Print)
            4. Ready for more code (Loop)
            """)

            # Interactive Python Demo
            st.markdown("### 🎮 Try Interactive Python")

            CodeEditor.create_with_examples({
                "Quick Calculations": """
# Try instant calculations
print(2 + 2)
print(10 * 5)
print(sum([1, 2, 3, 4, 5]))

# Variables work too
x = 42
print(f"The answer is {x}")
""",
                "Experiment with Code": """
# Try different things quickly
name = "Python"
print(name.upper())
print(name.lower())
print(len(name))
print(name * 3)
""",
                "Test Functions": """
# Define and test immediately
def square(x):
    return x * x

# Try it right away
print(square(4))
print(square(10))
print([square(x) for x in range(5)])
"""
            })

        elif tool_category == "📚 Documentation":
            st.markdown("""
            ### Documentation and Resources
            
            Documentation is like an instruction manual for code. It helps you:
            - Learn how things work
            - Find examples
            - Solve problems
            - Discover features
            """)

            # Documentation Types
            doc_type = st.radio(
                "Choose documentation type:",
                ["Official Docs", "Tutorials", "API Reference"]
            )

            if doc_type == "Official Docs":
                st.markdown("""
                #### Official Python Documentation
                
                [Python Official Docs](https://docs.python.org/3/)
                
                Key sections:
                1. **Tutorial**
                   - Step-by-step introduction
                   - Basic concepts
                   - Getting started
                
                2. **Library Reference**
                   - All built-in features
                   - Standard library modules
                   - Detailed explanations
                
                3. **Language Reference**
                   - How Python works
                   - Syntax rules
                   - Technical details
                """)

            elif doc_type == "Tutorials":
                st.markdown("""
                #### Python Tutorials
                
                Great places to learn:
                1. [Real Python](https://realpython.com/)
                   - In-depth articles
                   - Video tutorials
                   - Practice projects
                
                2. [W3Schools Python](https://www.w3schools.com/python/)
                   - Interactive learning
                   - Simple examples
                   - Quick reference
                
                3. [Python for Beginners](https://www.pythonforbeginners.com/)
                   - Basic concepts
                   - Easy to follow
                   - Practical examples
                """)

            else:  # API Reference
                st.markdown("""
                #### API Reference
                
                How to read API docs:
                1. **Look at Parameters**
                   - What inputs are needed
                   - What types are expected
                   - What's optional
                
                2. **Check Return Values**
                   - What you get back
                   - Possible errors
                   - Special cases
                
                3. **Study Examples**
                   - How to use it
                   - Common patterns
                   - Best practices
                """)

        elif tool_category == "🔄 Version Control":
            st.markdown("""
            ### Version Control (Git)
            
            Version control helps you:
            - Track changes in your code
            - Collaborate with others
            - Maintain code history
            - Backup your work
            """)

            # Git Basics
            with st.expander("Essential Git Commands"):
                st.code("""
# Start a new repository
git init

# Add files to staging
git add filename.py    # Add specific file
git add .             # Add all files

# Commit changes
git commit -m "Add new feature"

# Check status
git status

# View history
git log

# Create branch
git branch feature-name

# Switch branch
git checkout feature-name

# Push to remote
git push origin main
                """)

            # Git Workflow Visualization
            st.markdown("### Git Workflow")

            # Create workflow diagram
            workflow_fig = go.Figure()

            # Add workflow steps
            steps = ['Working Directory', 'Staging Area', 'Local Repository', 'Remote Repository']
            x_pos = [0, 1, 2, 3]

            # Add nodes
            workflow_fig.add_trace(go.Scatter(
                x=x_pos,
                y=[0, 0, 0, 0],
                mode='markers+text',
                marker=dict(
                    size=40,
                    color=[COLORS['primary']['blue'],
                           COLORS['primary']['green'],
                           COLORS['primary']['orange'],
                           COLORS['accent']['success']],
                    line=dict(color='black', width=2)
                ),
                text=steps,
                textposition='bottom center',
                textfont=dict(size=12)
            ))

            # Add arrows
            for i in range(len(steps)-1):
                workflow_fig.add_annotation(
                    x=x_pos[i]+0.5,
                    y=0,
                    ax=x_pos[i],
                    ay=0,
                    xref='x',
                    yref='y',
                    axref='x',
                    ayref='y',
                    text='',
                    showarrow=True,
                    arrowhead=2,
                    arrowsize=1.5,
                    arrowwidth=2,
                    arrowcolor=COLORS['text']['grey']
                )

            workflow_fig.update_layout(
                showlegend=False,
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                height=200,
                margin=dict(l=20, r=20, t=20, b=40)
            )

            st.plotly_chart(workflow_fig)

        else:  # Debugging Tools
            st.markdown("""
            ### Debugging Tools
            
            Debugging is finding and fixing errors in your code.
            """)

            st.markdown("### 🔍 Debugging Techniques")

            with st.expander("1. Print Debugging"):
                st.code("""
# Using print statements to debug
def calculate_total(items):
    print(f"Processing items: {items}")  # Debug print
    
    total = 0
    for item in items:
        print(f"Adding item: {item}")    # Debug print
        total += item
    
    print(f"Final total: {total}")       # Debug print
    return total

# Test the function
numbers = [1, 2, 3, 4, 5]
result = calculate_total(numbers)
                """)

            with st.expander("2. Error Handling"):
                st.code("""
# Using try-except for debugging
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Success: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Test with different values
print(divide_numbers(10, 2))   # Should work
print(divide_numbers(10, 0))   # Should catch error
                """)

            with st.expander("3. Using Debugger"):
                st.markdown("""
                Python's built-in debugger (pdb):
                ```python
                import pdb

                def complex_function(x, y):
                    pdb.set_trace()  # Start debugger
                    result = x * y
                    return result
                ```
                
                Debugger commands:
                - `n` (next line)
                - `s` (step into)
                - `c` (continue)
                - `p variable` (print variable)
                - `q` (quit)
                """)

        # General Tools Tips
        st.markdown("""
        ### 💡 Tools Tips
        
        1. **Start with Basics**
           - Learn one tool at a time
           - Master common features first
           - Add tools as needed
        
        2. **Practice Regularly**
           - Use keyboard shortcuts
           - Try new features
           - Learn from others
        
        3. **Stay Updated**
           - Keep tools current
           - Read release notes
           - Follow tutorials
        
        4. **Build Your Toolkit**
           - Start simple
           - Add specialized tools
           - Customize your setup
        """)

    # Final Tips and Resources
    st.markdown("""
    ## 📚 Additional Resources
    
    1. **Online Learning Platforms**
       - [Codecademy](https://www.codecademy.com/learn/learn-python)
       - [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/)
       - [Real Python](https://realpython.com/)
    
    2. **Practice Sites**
       - [LeetCode](https://leetcode.com/)
       - [HackerRank](https://www.hackerrank.com/domains/python)
       - [Project Euler](https://projecteuler.net/)
    
    3. **Communities**
       - [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
       - [Reddit r/learnpython](https://www.reddit.com/r/learnpython/)
       - [Python Discord](https://discord.com/invite/python)
    """)

if __name__ == "__main__":
    show()