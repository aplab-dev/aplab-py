import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show():
    st.header("1.1 Variables in Python")

    # Theory Section
    with st.expander("📚 Understanding Variables", expanded=True):
        st.markdown("""
        ### What is a Variable? 
        
        Imagine a variable as a labeled box where you can store things. Just like you might have boxes labeled 
        "Winter Clothes" or "Books" in your home, in Python we have variables that store different types of information.

        #### Real-Life Example:
        - 📦 Box labeled "Age" contains the number 25
        - 📦 Box labeled "Name" contains the text "John"
        - 📦 Box labeled "Temperature" contains the number 72.5

        ### How Variables Work

        1. **Creating a Variable**
           - You give it a name (label the box)
           - You put something in it (store the value)
           - Python automatically knows what type of thing you stored

        2. **Variable Names**
           - Can contain letters, numbers, and underscores
           - Must start with a letter or underscore
           - Cannot use special characters like !@#$%
           - Are case-sensitive (age and Age are different)

        3. **Variable Types**
           - Text (strings): "Hello", "John"
           - Whole numbers (integers): 1, 42, -17
           - Decimal numbers (floats): 3.14, -0.001
           - True/False (boolean): True, False
        """)

    # Interactive Examples Section
    st.markdown("### 🎮 Interactive Examples")

    # Example 1: Basic Variable Assignment
    st.subheader("1️⃣ Create Your First Variables")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Enter your name:", "John")
        age = st.number_input("Enter your age:", 0, 150, 25)
        height = st.number_input("Enter your height (in cm):", 0.0, 300.0, 170.0)

    with col2:
        st.markdown("### Variables Created:")
        st.code(f"""
name = "{name}"
age = {age}
height = {height}
        """)

        st.markdown("### Variable Types:")
        df = pd.DataFrame({
            'Variable': ['name', 'age', 'height'],
            'Value': [str(name), str(age), str(height)],  # Convert all values to strings
            'Type': [type(name).__name__, type(age).__name__, type(height).__name__]
        })
        st.table(df)

    # Example 2: Changing Variable Values
    st.subheader("2️⃣ Changing Variable Values")

    st.markdown("""
    One of the key features of variables is that they can change their values during program execution.
    Think of it as updating the content of your labeled box.
    
    Let's see this in action with a simple counter:
    """)

    # Interactive counter example
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Control Panel")
        if st.button("➕ Increase Counter"):
            st.session_state.counter += 1
        if st.button("➖ Decrease Counter"):
            st.session_state.counter -= 1
        if st.button("🔄 Reset Counter"):
            st.session_state.counter = 0

    with col2:
        st.markdown("### Variable State")
        st.code(f"""
# Initial state
counter = 0

# Current state
counter = {st.session_state.counter}
        """)

    # Show the history of changes
    st.markdown("### 📝 Understanding Variable Changes")
    st.markdown("""
    When you click the buttons above:
    1. The variable `counter` changes its value
    2. Python updates what's stored in the 'box' labeled `counter`
    3. The old value is replaced with the new value
    
    This is like:
    - Having a scoreboard (variable)
    - Changing the score (value) during a game
    - The scoreboard always shows the current score
    """)

    # Visual representation of variable change
    import plotly.graph_objects as go

    # Create a simple visualization of the counter
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = st.session_state.counter,
        title = {'text': "Counter Variable Value"},
        gauge = {
            'axis': {'range': [-10, 10]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [-10, 0], 'color': "lightgray"},
                {'range': [0, 10], 'color': "lightblue"}
            ],
        }
    ))

    st.plotly_chart(fig)

    # Practical example
    st.markdown("### 🎮 Real-world Example: Game Score")

    st.markdown("""
    Imagine you're making a simple game. You need to keep track of the player's score:
    """)

    if 'score' not in st.session_state:
        st.session_state.score = 0

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### Game Actions")
        if st.button("🎯 Hit Target (+10 points)"):
            st.session_state.score += 10
        if st.button("⭐ Collect Star (+5 points)"):
            st.session_state.score += 5
        if st.button("❌ Miss Target (-3 points)"):
            st.session_state.score -= 3
        if st.button("🔄 New Game"):
            st.session_state.score = 0

    with col4:
        st.markdown("### Score Variable")
        st.code(f"""
# Score variable keeps changing
score = {st.session_state.score}
        """)

        # Show score history
        if 'score_history' not in st.session_state:
            st.session_state.score_history = [0]
        if st.session_state.score != st.session_state.score_history[-1]:
            st.session_state.score_history.append(st.session_state.score)

        # Create line chart of score history
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            y=st.session_state.score_history,
            mode='lines+markers',
            name='Score'
        ))
        fig2.update_layout(
            title='Score History',
            yaxis_title='Score Value',
            xaxis_title='Actions'
        )
        st.plotly_chart(fig2)

    # Example 3: Variable Rules and Best Practices
    st.subheader("3️⃣ Variable Naming Rules")

    st.markdown("""
    Let's practice creating valid variable names!
    """)

    user_input = st.text_input("Try creating a variable name:", "my_variable")

    def is_valid_variable_name(name):
        if not name:
            return False
        if not (name[0].isalpha() or name[0] == '_'):
            return False
        for char in name:
            if not (char.isalnum() or char == '_'):
                return False
        return True

    if is_valid_variable_name(user_input):
        st.success(f"✅ '{user_input}' is a valid variable name!")
        st.code(f"""
# You can use it like this:
{user_input} = 42
        """)
    else:
        st.error(f"❌ '{user_input}' is not a valid variable name!")
        st.markdown("""
        Remember:
        - Start with a letter or underscore
        - Use only letters, numbers, and underscores
        - No spaces or special characters
        """)

    # Practice Section
    st.markdown("### 🎯 Practice Exercise")

    with st.expander("Try it yourself!"):
        st.markdown("""
        Create three variables to describe a car:
        1. Car brand (text)
        2. Car year (whole number)
        3. Car price (decimal number)
        """)

        car_brand = st.text_input("Car brand:", "Toyota")
        car_year = st.number_input("Car year:", 1900, 2024, 2020)
        car_price = st.number_input("Car price ($):", 0.0, 1000000.0, 25000.0)

        if st.button("Check Your Variables"):
            st.code(f"""
# Your variables:
car_brand = "{car_brand}"  # Type: {type(car_brand).__name__}
car_year = {car_year}      # Type: {type(car_year).__name__}
car_price = {car_price}    # Type: {type(car_price).__name__}
            """)
            st.success("Great job! You've created three different types of variables!")

    # Additional Resources
    with st.expander("📚 Additional Resources"):
        st.markdown("""
        Want to learn more about variables? Check out these resources:
        - [Python Official Documentation](https://docs.python.org/3/tutorial/introduction.html)
        - [Real Python - Variables Tutorial](https://realpython.com/python-variables/)
        - [W3Schools Python Variables](https://www.w3schools.com/python/python_variables.asp)
        """)