import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def show():
    st.header("1.2 Data Types in Python")

    # Introduction
    st.markdown("""
    ### Understanding Data Types in Python 🎯
    
    Just like we have different types of measurements in real life 
    (temperature in degrees, weight in kilograms, text in letters), 
    Python uses different types to store different kinds of data.
    
    Let's explore each type with practical examples!
    """)

    # Main Types Overview using Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📝 Text (Strings)",
        "🔢 Numbers",
        "✅ Booleans",
        "📋 Lists",
        "🔑 Dictionaries"
    ])

    # 1. STRING TAB
    with tab1:
        st.markdown("""
        ### Text Data (Strings) 📝
        
        Strings are used to store text. Any text you can type can be stored in a string:
        - Names
        - Messages
        - Addresses
        - Words and sentences
        """)

        # Interactive String Example
        st.markdown("### Try It Yourself!")
        text_input = st.text_input(
            "Type any text:",
            "Hello, Python!"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Your String Properties:")
            st.code(f"""
# Basic Properties
Text: "{text_input}"
Length: {len(text_input)} characters
Type: {type(text_input).__name__}

# Common Operations
Uppercase: "{text_input.upper()}"
Lowercase: "{text_input.lower()}"
First character: "{text_input[0] if text_input else ''}"
Last character: "{text_input[-1] if text_input else ''}"
            """)

        with col2:
            st.markdown("#### Common String Uses:")
            st.markdown("""
            - 👤 User names
            - 📧 Email addresses
            - 📝 Messages
            - 📚 Document text
            """)

        # String Character Display
        if text_input:
            st.markdown("#### Character Positions (Index)")

            # Create visual representation of string characters
            fig = go.Figure()

            # Add characters
            for i, char in enumerate(text_input):
                fig.add_trace(go.Scatter(
                    x=[i], y=[1],
                    mode='text',
                    text=[char],
                    textfont=dict(size=20),
                    name=f'Character {i}'
                ))
                # Add index numbers
                fig.add_trace(go.Scatter(
                    x=[i], y=[0],
                    mode='text',
                    text=[str(i)],
                    textfont=dict(size=14),
                    name=f'Index {i}'
                ))

            fig.update_layout(
                title='String Characters and Their Positions (Index)',
                showlegend=False,
                yaxis=dict(
                    visible=False,
                    range=[-0.5, 1.5]
                ),
                xaxis=dict(visible=False),
                height=200,
                margin=dict(l=20, r=20, t=40, b=20)
            )

            st.plotly_chart(fig)

            st.markdown("""
            #### Understanding String Index:
            - Each character has a position number (index)
            - First character is at index 0
            - Last character is at index -1
            - Spaces and punctuation marks count as characters
            """)

        # String Practice
        st.markdown("### 🎯 Practice with Strings")
        with st.expander("Try String Operations"):
            st.markdown("""
            Let's create a personalized message:
            """)

            name = st.text_input("Enter a name:", "Alice")
            age = st.number_input("Enter age:", 0, 150, 25)
            city = st.text_input("Enter city:", "New York")

            message = f"Hello, {name}! You are {age} years old and live in {city}."

            st.markdown("#### Generated Message:")
            st.success(message)

            st.markdown("#### Message Properties:")
            st.code(f"""
# Message analysis:
Length: {len(message)} characters
Words: {len(message.split())} words
Uppercase: {message.upper()}
Contains 'Hello': {"Hello" in message}
            """)


    # 2. NUMBERS TAB
    with tab2:
        st.markdown("""
        ### Numbers in Python 🔢
        
        Python has two main types of numbers:
        
        #### 1. Integers (int)
        - Whole numbers (no decimal point)
        - Examples: -5, 0, 42, 1000
        - Used for: counting, indexes, whole quantities
        
        #### 2. Floating-Point Numbers (float)
        - Numbers with decimal points
        - Examples: 3.14, -0.001, 2.0, 99.99
        - Used for: measurements, calculations, precise values
        """)

        # Number Explorer
        st.markdown("### 🎮 Number Explorer")

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("#### Integer Examples")
            int_num = st.number_input("Enter a whole number:", value=42, step=1)

            st.code(f"""
# Integer Operations
Number: {int_num}
Type: {type(int_num).__name__}

Basic Math:
× 2 = {int_num * 2}
² = {int_num ** 2}
÷ 2 = {int_num // 2} (integer division)
Remainder ÷ 2 = {int_num % 2}
            """)

        with col4:
            st.markdown("#### Float Examples")
            float_num = st.number_input("Enter a decimal number:", value=3.14)

            st.code(f"""
# Float Operations
Number: {float_num}
Type: {type(float_num).__name__}

Formats:
Regular: {float_num}
Rounded: {round(float_num, 2)}
Scientific: {format(float_num, '.2e')}
Percentage: {float_num * 100}%
            """)

        # Number Line Visualization
        st.markdown("### 📏 Interactive Number Line")

        start_num = st.slider("Select range:", -10.0, 10.0, (-5.0, 5.0))

        # Create number line
        fig_numbers = go.Figure()

        # Add integer points
        integers = list(range(int(np.ceil(start_num[0])), int(np.floor(start_num[1])) + 1))
        fig_numbers.add_trace(go.Scatter(
            x=integers,
            y=[0] * len(integers),
            mode='markers+text',
            marker=dict(size=12, color='blue'),
            text=[str(i) for i in integers],
            textposition='top center',
            name='Integers'
        ))

        fig_numbers.update_layout(
            title='Number Line',
            xaxis=dict(
                title='Numbers',
                range=[start_num[0] - 0.5, start_num[1] + 0.5]
            ),
            yaxis=dict(visible=False),
            height=200,
            margin=dict(l=20, r=20, t=40, b=20)
        )

        st.plotly_chart(fig_numbers)

        st.markdown("""
        #### Understanding the Number Line:
        - Blue dots represent whole numbers (integers)
        - Numbers increase from left to right
        - Negative numbers are left of zero
        - Positive numbers are right of zero
        """)

    # 3. BOOLEAN TAB
    with tab3:
        st.markdown("""
        ### Boolean Values (True/False) ✅
        
        Booleans are simple but powerful - they can only be `True` or `False`.
        Think of them as Yes/No switches.
        
        Common uses:
        - Checking conditions
        - Controlling program flow
        - Storing yes/no states
        """)

        # Boolean Explorer
        st.markdown("### 🎮 Boolean Explorer")

        col5, col6 = st.columns(2)

        with col5:
            st.markdown("#### Create Boolean Values")
            is_active = st.checkbox("Is Active?", value=True)
            is_admin = st.checkbox("Is Admin?", value=False)

            st.code(f"""
# Your Boolean Values:
is_active = {is_active}
is_admin = {is_admin}

# Type:
Type of is_active: {type(is_active).__name__}
            """)

        with col6:
            st.markdown("#### Boolean Operations")
            st.code(f"""
# Logical Operations:
AND: {is_active} AND {is_admin} = {is_active and is_admin}
OR:  {is_active} OR {is_admin} = {is_active or is_admin}
NOT: NOT {is_active} = {not is_active}
            """)

        # Boolean Logic Visualization
        st.markdown("### 📊 Boolean Logic Table")

        logic_data = {
            'A': [True, True, False, False],
            'B': [True, False, True, False],
            'A AND B': [True, False, False, False],
            'A OR B': [True, True, True, False],
            'NOT A': [False, False, True, True]
        }

        df_logic = pd.DataFrame(logic_data)
        st.table(df_logic)

        # Boolean Practice
        st.markdown("### 🎯 Boolean Practice")
        with st.expander("Try Boolean Logic"):
            st.markdown("""
            Let's create a simple login system:
            """)

            correct_password = "secret123"
            entered_password = st.text_input("Enter password:", type="password")
            is_correct = entered_password == correct_password

            st.markdown("#### Check Results:")
            st.code(f"""
# Password Check
Password correct: {is_correct}
Can login: {is_correct and is_active}
Has admin access: {is_correct and is_admin}
            """)

    # 4. LISTS TAB
    with tab4:
        st.markdown("""
        ### Lists - Collections of Items 📋
        
        Lists are ordered collections that can store multiple items of any type.
        Think of them as:
        - Shopping lists
        - To-do lists
        - Collection of scores
        - Series of names
        """)

        # List Builder
        st.markdown("### 🏗️ Interactive List Builder")

        # Initialize session state for list
        if 'list_items' not in st.session_state:
            st.session_state.list_items = ['apple', 'banana', 'orange']

        col7, col8 = st.columns(2)

        with col7:
            # Add items to list
            new_item = st.text_input("Add an item to the list:", "")
            if st.button("Add Item") and new_item:
                st.session_state.list_items.append(new_item)
                st.success(f"Added '{new_item}' to the list!")

        with col8:
            # Remove items from list
            if st.button("Remove Last Item") and st.session_state.list_items:
                removed_item = st.session_state.list_items.pop()
                st.info(f"Removed '{removed_item}' from the list!")

        # Display current list
        st.markdown("#### Your Current List:")
        st.code(f"""
# List Contents:
my_list = {st.session_state.list_items}

# List Properties:
Length: {len(st.session_state.list_items)} items
First item: {st.session_state.list_items[0] if st.session_state.list_items else 'None'}
Last item: {st.session_state.list_items[-1] if st.session_state.list_items else 'None'}
        """)

        # List Visualization
        if st.session_state.list_items:
            st.markdown("#### List Visualization")
            fig_list = go.Figure()

            for i, item in enumerate(st.session_state.list_items):
                # Add boxes for items
                fig_list.add_shape(
                    type="rect",
                    x0=i-0.4, x1=i+0.4,
                    y0=-0.4, y1=0.4,
                    line=dict(color="RoyalBlue"),
                    fillcolor="LightSkyBlue",
                )
                # Add item text
                fig_list.add_trace(go.Scatter(
                    x=[i],
                    y=[0],
                    mode='text',
                    text=[item],
                    textposition='middle center',
                    showlegend=False
                ))
                # Add index numbers
                fig_list.add_trace(go.Scatter(
                    x=[i],
                    y=[-0.6],
                    mode='text',
                    text=[f"Index: {i}"],
                    textposition='top center',
                    showlegend=False
                ))

            fig_list.update_layout(
                title='List Items and Their Indices',
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                height=200,
                margin=dict(l=20, r=20, t=40, b=20),
                showlegend=False
            )

            st.plotly_chart(fig_list)

        # List Operations
        st.markdown("### 🛠️ Common List Operations")
        with st.expander("Explore List Operations"):
            st.code("""
# Common List Operations:
my_list = ['apple', 'banana', 'orange']

# Adding items
my_list.append('grape')      # Adds to end
my_list.insert(0, 'mango')   # Adds at index 0

# Removing items
my_list.pop()               # Removes last item
my_list.remove('banana')    # Removes specific item

# Accessing items
first = my_list[0]          # First item
last = my_list[-1]          # Last item
slice = my_list[1:3]        # Items from index 1 to 2

# Other operations
length = len(my_list)       # Number of items
sorted_list = sorted(my_list)  # Alphabetical order
reversed_list = my_list[::-1]  # Reverse order
            """)

    # FINAL PRACTICE SECTION
    st.markdown("### 🎯 Final Practice: Combining Data Types")
    with st.expander("Try Complete Exercise"):
        st.markdown("""
        Let's create a simple student record using different data types:
        """)

        # Student Record Builder
        student_name = st.text_input("Student Name:", "John Doe")
        student_age = st.number_input("Student Age:", 0, 100, 20)
        student_grade = st.number_input("Grade Average:", 0.0, 100.0, 85.5)
        is_active = st.checkbox("Is Active Student?", True)
        courses = st.multiselect(
            "Select Courses:",
            ["Math", "Physics", "Chemistry", "Biology", "History"],
            ["Math"]
        )

        # Display Student Record
        st.markdown("#### Student Record:")
        st.code(f"""
# Student Information
name: "{student_name}"        # Type: {type(student_name).__name__}
age: {student_age}           # Type: {type(student_age).__name__}
grade: {student_grade}       # Type: {type(student_grade).__name__}
active: {is_active}         # Type: {type(is_active).__name__}
courses: {courses}          # Type: {type(courses).__name__}
        """)

    # SUMMARY
    st.markdown("### 📚 Summary of Python Data Types")
    st.markdown("""
    1. **Strings (str)**
       - Store text
       - Created with quotes: "Hello" or 'Hello'
       - Used for names, messages, text data
    
    2. **Numbers**
       - Integers (int): Whole numbers (42, -17)
       - Floats (float): Decimal numbers (3.14, -0.001)
       - Used for calculations and measurements
    
    3. **Booleans (bool)**
       - Only True or False
       - Used for conditions and states
       - Control program flow
    
    4. **Lists**
       - Ordered collections of items
       - Can mix different types
       - Flexible and changeable
    """)

    # ADDITIONAL RESOURCES
    with st.expander("📚 Additional Resources"):
        st.markdown("""
        Want to learn more about Python data types?
        
        - [Python Official Documentation](https://docs.python.org/3/library/datatypes.html)
        - [Real Python - Data Types](https://realpython.com/python-data-types/)
        - [W3Schools Python Tutorial](https://www.w3schools.com/python/python_datatypes.asp)
        
        Practice Exercises:
        1. Try creating variables of different types
        2. Experiment with list operations
        3. Combine different types in meaningful ways
        """)

    # 5. DICTIONARIES TAB
    with tab5:
        st.markdown("""
        ### Dictionaries (dict) - Key-Value Pairs 🔑
        
        Dictionaries are like real-world dictionaries where:
        - Each word (key) has a definition (value)
        - You look up values using their keys
        - Keys must be unique
        
        Real-world examples:
        - Phone book: name → phone number
        - Dictionary: word → definition
        - Menu: dish name → price
        - User profile: attribute → value
        """)

        # Dictionary Builder
        st.markdown("### 🏗️ Interactive Dictionary Builder")

        # Initialize session state for dictionary
        if 'dict_items' not in st.session_state:
            st.session_state.dict_items = {
                'name': 'John',
                'age': 25,
                'city': 'New York'
            }

        # Add key-value pairs
        col9, col10 = st.columns(2)

        with col9:
            new_key = st.text_input("Enter key:", "")
            new_value = st.text_input("Enter value:", "")
            if st.button("Add Key-Value Pair") and new_key:
                st.session_state.dict_items[new_key] = new_value
                st.success(f"Added {new_key}: {new_value}")

        with col10:
            if st.session_state.dict_items:
                key_to_remove = st.selectbox(
                    "Select key to remove:",
                    list(st.session_state.dict_items.keys())
                )
                if st.button("Remove Key"):
                    removed_value = st.session_state.dict_items.pop(key_to_remove)
                    st.info(f"Removed {key_to_remove}: {removed_value}")

        # Display current dictionary
        st.markdown("#### Your Dictionary:")
        st.code(f"""
# Dictionary Contents:
my_dict = {st.session_state.dict_items}

# Dictionary Properties:
Number of items: {len(st.session_state.dict_items)}
Keys: {list(st.session_state.dict_items.keys())}
Values: {list(st.session_state.dict_items.values())}
        """)

        # Dictionary Operations
        st.markdown("### 🛠️ Common Dictionary Operations")
        with st.expander("Explore Dictionary Operations"):
            st.code("""
# Creating a dictionary
user = {
    'name': 'Alice',
    'age': 30,
    'is_active': True,
    'courses': ['Python', 'Data Science']
}

# Accessing values
name = user['name']          # Using key
age = user.get('age', 0)     # Using get() with default value

# Modifying dictionary
user['city'] = 'London'      # Adding new key-value pair
user['age'] = 31             # Updating existing value
del user['is_active']        # Removing a key-value pair

# Dictionary methods
keys = user.keys()           # Get all keys
values = user.values()       # Get all values
items = user.items()         # Get all key-value pairs
            """)

        # Practical Example
        st.markdown("### 📝 Practical Dictionary Example")
        st.markdown("""
        Let's create a product catalog:
        """)

        # Product Catalog Builder
        if 'catalog' not in st.session_state:
            st.session_state.catalog = {
                'laptop': 999.99,
                'phone': 499.99,
                'tablet': 299.99
            }

        # Add new product
        new_product = st.text_input("Product name:", "")
        new_price = st.number_input("Product price:", 0.0, 10000.0, 0.0)
        if st.button("Add Product") and new_product:
            st.session_state.catalog[new_product] = new_price

        # Display catalog
        st.markdown("#### Product Catalog:")

        # Create a DataFrame for better visualization
        df_catalog = pd.DataFrame([
            {'Product': k, 'Price': f"${v:.2f}"}
            for k, v in st.session_state.catalog.items()
        ])
        st.table(df_catalog)

        # Dictionary Visualization
        st.markdown("#### Dictionary Structure Visualization")

        fig_dict = go.Figure()

        # Add visualization elements for each key-value pair
        for i, (key, value) in enumerate(st.session_state.catalog.items()):
            # Key box
            fig_dict.add_shape(
                type="rect",
                x0=0, x1=1,
                y0=i-0.4, y1=i+0.4,
                line=dict(color="RoyalBlue"),
                fillcolor="LightSkyBlue",
            )
            # Value box
            fig_dict.add_shape(
                type="rect",
                x0=1, x1=2,
                y0=i-0.4, y1=i+0.4,
                line=dict(color="Green"),
                fillcolor="LightGreen",
            )
            # Add text
            fig_dict.add_trace(go.Scatter(
                x=[0.5, 1.5],
                y=[i, i],
                mode='text',
                text=[key, f"${value:.2f}"],
                textposition='middle center',
                showlegend=False
            ))

        fig_dict.update_layout(
            title='Dictionary Key-Value Pairs',
            xaxis=dict(
                ticktext=['Keys', 'Values'],
                tickvals=[0.5, 1.5],
                range=[-0.5, 2.5]
            ),
            yaxis=dict(visible=False),
            height=50 + 50*len(st.session_state.catalog),
            margin=dict(l=20, r=20, t=40, b=20)
        )

        st.plotly_chart(fig_dict)

        # Best Practices
        st.markdown("""
        ### 📌 Dictionary Best Practices
        
        1. **Keys must be unique**
           - Each key can only appear once
           - New value overwrites old value for same key
        
        2. **Keys must be immutable**
           - Can use: strings, numbers, tuples
           - Cannot use: lists, dictionaries
        
        3. **Common Use Cases**
           - Configuration settings
           - Caching/memoization
           - Counting occurrences
           - Grouping related data
        """)