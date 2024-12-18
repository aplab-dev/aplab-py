import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def show():
    st.header("1.3 Operations in Python")

    st.markdown("""
    ### Understanding Python Operations 🔧
    
    Just like a calculator has different buttons for different operations,
    Python has various operators to perform different tasks.
    """)

    # Main operations categories using tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "➕ Arithmetic",
        "⚖️ Comparison",
        "🔄 Logical",
        "📝 Assignment"
    ])

    # 1. ARITHMETIC OPERATIONS TAB
    with tab1:
        st.markdown("""
        ### Arithmetic Operations
        
        These are the basic mathematical operations you can perform in Python:
        - Addition (+)
        - Subtraction (-)
        - Multiplication (*)
        - Division (/)
        - Power (**)
        - Integer Division (//)
        - Remainder/Modulo (%)
        """)

        # Interactive Calculator
        st.markdown("### 🧮 Interactive Calculator")

        col1, col2 = st.columns(2)

        with col1:
            num1 = st.number_input("First Number:", value=10.0)
            num2 = st.number_input("Second Number:", value=3.0)

        with col2:
            st.markdown("#### Results:")
            st.code(f"""
# Basic Operations:
{num1} + {num2} = {num1 + num2}
{num1} - {num2} = {num1 - num2}
{num1} × {num2} = {num1 * num2}
{num1} ÷ {num2} = {num1 / num2 if num2 != 0 else 'undefined'}

# Advanced Operations:
{num1} ** {num2} = {num1 ** num2}  (power)
{num1} // {num2} = {num1 // num2 if num2 != 0 else 'undefined'}  (integer division)
{num1} % {num2} = {num1 % num2 if num2 != 0 else 'undefined'}  (remainder)
            """)

        # Order of Operations
        st.markdown("### 📚 Order of Operations (PEMDAS)")

        st.markdown("""
        Python follows the standard mathematical order of operations:
        1. **P**arentheses
        2. **E**xponents
        3. **M**ultiplication and **D**ivision (left to right)
        4. **A**ddition and **S**ubtraction (left to right)
        """)

        # Interactive PEMDAS Example
        st.markdown("### 🎮 Order of Operations Explorer")

        expression = st.text_input(
            "Enter a mathematical expression:",
            "2 + 3 * 4"
        )

        try:
            result = eval(expression)  # Note: eval is used for demonstration
            st.success(f"Result: {result}")

            # Show step by step
            st.markdown("#### Steps:")
            if '*' in expression or '/' in expression:
                st.markdown("1. First, handle multiplication/division")
            if '+' in expression or '-' in expression:
                st.markdown("2. Then, handle addition/subtraction")

        except:
            st.error("Please enter a valid mathematical expression")

        # Visual Number Line for Operations
        st.markdown("### 📊 Operation Visualization")

        operation = st.selectbox(
            "Select operation to visualize:",
            ["Addition", "Subtraction", "Multiplication"]
        )

        vis_num1 = st.slider("First number:", -10, 10, 5)
        vis_num2 = st.slider("Second number:", -10, 10, 3)

        # Create visualization
        fig = go.Figure()

        # Number line
        fig.add_trace(go.Scatter(
            x=list(range(-10, 11)),
            y=[0] * 21,
            mode='markers',
            marker=dict(size=5, color='gray'),
            name='Number Line'
        ))

        # Operation visualization
        if operation == "Addition":
            # Show first number
            fig.add_trace(go.Scatter(
                x=[0, vis_num1],
                y=[0.1, 0.1],
                mode='lines+markers',
                name='First Number',
                line=dict(color='blue', width=3)
            ))
            # Show second number
            fig.add_trace(go.Scatter(
                x=[vis_num1, vis_num1 + vis_num2],
                y=[0.1, 0.1],
                mode='lines+markers',
                name='Second Number',
                line=dict(color='green', width=3)
            ))
            result_point = vis_num1 + vis_num2

        elif operation == "Subtraction":
            fig.add_trace(go.Scatter(
                x=[0, vis_num1],
                y=[0.1, 0.1],
                mode='lines+markers',
                name='First Number',
                line=dict(color='blue', width=3)
            ))
            fig.add_trace(go.Scatter(
                x=[vis_num1, vis_num1 - vis_num2],
                y=[0.1, 0.1],
                mode='lines+markers',
                name='Second Number',
                line=dict(color='red', width=3)
            ))
            result_point = vis_num1 - vis_num2

        else:  # Multiplication
            points = []
            for i in range(abs(vis_num2)):
                points.extend([vis_num1, 0])
            fig.add_trace(go.Scatter(
                x=points,
                y=[0.1] * len(points),
                mode='lines+markers',
                name='Multiplication',
                line=dict(color='purple', width=3)
            ))
            result_point = vis_num1 * vis_num2

        # Add result point
        fig.add_trace(go.Scatter(
            x=[result_point],
            y=[0],
            mode='markers',
            marker=dict(size=15, color='red'),
            name='Result'
        ))

        fig.update_layout(
            title=f'{operation}: {vis_num1} {operation.lower()} {vis_num2} = {result_point}',
            xaxis=dict(range=[-11, 11], title='Number Line'),
            yaxis=dict(range=[-0.5, 0.5], showticklabels=False),
            height=300,
            showlegend=True
        )

        st.plotly_chart(fig)

        # Practical Examples
        st.markdown("### 🌟 Practical Examples")
        with st.expander("Real-world Applications"):
            st.markdown("""
            1. **Shopping Cart Total**
            """)

            item1_price = st.number_input("Item 1 price:", 0.0, 1000.0, 10.0)
            item1_quantity = st.number_input("Item 1 quantity:", 0, 100, 2)
            item2_price = st.number_input("Item 2 price:", 0.0, 1000.0, 5.0)
            item2_quantity = st.number_input("Item 2 quantity:", 0, 100, 3)

            subtotal = (item1_price * item1_quantity) + (item2_price * item2_quantity)
            tax = subtotal * 0.1  # 10% tax
            total = subtotal + tax

            st.code(f"""
# Shopping Cart Calculation:
Item 1 total: ${item1_price} × {item1_quantity} = ${item1_price * item1_quantity}
Item 2 total: ${item2_price} × {item2_quantity} = ${item2_price * item2_quantity}
Subtotal: ${subtotal}
Tax (10%): ${tax}
Total: ${total}
            """)

    # 2. COMPARISON OPERATIONS TAB
    with tab2:
        st.markdown("""
        ### Comparison Operations ⚖️
        
        Comparison operators compare values and return True or False:
        - Equal to (==)
        - Not equal to (!=)
        - Greater than (>)
        - Less than (<)
        - Greater than or equal to (>=)
        - Less than or equal to (<=)
        """)

        # Interactive Comparison Tool
        st.markdown("### 🔍 Comparison Explorer")

        col3, col4 = st.columns(2)

        with col3:
            comp_num1 = st.number_input("First Value:", value=10)
            comp_operator = st.selectbox(
                "Select comparison operator:",
                ["==", "!=", ">", "<", ">=", "<="]
            )
            comp_num2 = st.number_input("Second Value:", value=5)

        with col4:
            # Show result
            result = eval(f"{comp_num1} {comp_operator} {comp_num2}")
            st.markdown("#### Result:")
            st.code(f"""
{comp_num1} {comp_operator} {comp_num2}
Result: {result}
Type: {type(result).__name__}
            """)

        # Visual Comparison
        st.markdown("### 📊 Visual Comparison")

        fig_comp = go.Figure()

        # Add bars for comparison
        fig_comp.add_trace(go.Bar(
            x=['First Value', 'Second Value'],
            y=[comp_num1, comp_num2],
            text=[comp_num1, comp_num2],
            textposition='auto',
        ))

        fig_comp.update_layout(
            title=f'Comparison: {comp_num1} {comp_operator} {comp_num2} = {result}',
            height=400
        )

        st.plotly_chart(fig_comp)

        # Multiple Comparisons
        st.markdown("### 🔄 Multiple Comparisons")

        st.markdown("""
        You can chain multiple comparisons in Python:
        - Check if a number is between two values
        - Compare multiple values at once
        """)

        # Range checker
        value = st.slider("Select a value:", 0, 100, 50)
        min_range = st.slider("Minimum range:", 0, 100, 30)
        max_range = st.slider("Maximum range:", 0, 100, 70)

        in_range = min_range <= value <= max_range

        st.code(f"""
# Check if {value} is between {min_range} and {max_range}:
{min_range} <= {value} <= {max_range}
Result: {in_range}
        """)

        # Practical Examples
        st.markdown("### 🎯 Practical Examples")
        with st.expander("Real-world Comparisons"):
            st.markdown("""
            1. **Grade Calculator**
            """)

            score = st.number_input("Enter test score (0-100):", 0, 100, 75)

            grade = (
                'A' if score >= 90 else
                'B' if score >= 80 else
                'C' if score >= 70 else
                'D' if score >= 60 else
                'F'
            )

            st.code(f"""
# Grade Calculation:
Score: {score}
Grade: {grade}

Conditions:
A: score >= 90 ({score >= 90})
B: score >= 80 ({score >= 80})
C: score >= 70 ({score >= 70})
D: score >= 60 ({score >= 60})
F: score < 60 ({score < 60})
            """)

    # 3. LOGICAL OPERATIONS TAB
    with tab3:
        st.markdown("""
        ### Logical Operations 🔄
        
        Logical operators combine conditions:
        - AND: both conditions must be True
        - OR: at least one condition must be True
        - NOT: reverses the condition
        """)

        # Interactive Logic Explorer
        st.markdown("### 🎮 Logic Gate Explorer")

        col5, col6 = st.columns(2)

        with col5:
            condition1 = st.checkbox("Condition 1", True)
            logical_op = st.selectbox(
                "Select logical operator:",
                ["AND", "OR", "NOT"]
            )
            condition2 = st.checkbox("Condition 2", False)

        with col6:
            # Calculate result based on operator
            if logical_op == "AND":
                logic_result = condition1 and condition2
            elif logical_op == "OR":
                logic_result = condition1 or condition2
            else:  # NOT
                logic_result = not condition1

            st.markdown("#### Result:")
            st.code(f"""
Condition 1: {condition1}
Operator: {logical_op}
Condition 2: {condition2}
Result: {logic_result}
            """)

        # Truth Table
        st.markdown("### 📑 Truth Tables")

        # Create truth table based on selected operator
        if logical_op == "AND":
            truth_table = pd.DataFrame([
                [True, True, True],
                [True, False, False],
                [False, True, False],
                [False, False, False]
            ], columns=['A', 'B', 'A AND B'])
        elif logical_op == "OR":
            truth_table = pd.DataFrame([
                [True, True, True],
                [True, False, True],
                [False, True, True],
                [False, False, False]
            ], columns=['A', 'B', 'A OR B'])
        else:  # NOT
            truth_table = pd.DataFrame([
                [True, False],
                [False, True]
            ], columns=['A', 'NOT A'])

        st.table(truth_table)

        # Practical Logic Examples
        st.markdown("### 🌟 Practical Logic Examples")
        with st.expander("Real-world Logic"):
            st.markdown("""
            1. **User Access Control**
            """)

            is_logged_in = st.checkbox("User is logged in", True)
            is_admin = st.checkbox("User is admin", False)
            has_permission = st.checkbox("User has permission", True)

            can_edit = is_logged_in and (is_admin or has_permission)

            st.code(f"""
# Access Control Logic:
Can user edit? {can_edit}

Logic:
1. Must be logged in: {is_logged_in}
2. Must be either:
   - Admin: {is_admin}
   - Have permission: {has_permission}
            """)

            st.markdown("""
            2. **Shopping Cart Validation**
            """)

            cart_not_empty = st.checkbox("Cart has items", True)
            valid_payment = st.checkbox("Payment method is valid", True)
            in_stock = st.checkbox("Items in stock", True)

            can_checkout = cart_not_empty and valid_payment and in_stock

            st.code(f"""
# Shopping Cart Logic:
Can proceed to checkout? {can_checkout}

Conditions:
1. Cart has items: {cart_not_empty}
2. Payment is valid: {valid_payment}
3. Items in stock: {in_stock}
            """)

    # 4. ASSIGNMENT OPERATIONS TAB
    with tab4:
        st.markdown("""
        ### Assignment Operations 📝
        
        Assignment operators are used to assign values to variables:
        - Basic assignment (=)
        - Compound assignments (+=, -=, *=, /=, etc.)
        - Multiple assignments
        """)

        # Basic Assignment
        st.markdown("### 🔄 Basic Assignment")

        st.code("""
# Basic assignment
x = 10

# Multiple assignment
a, b = 1, 2

# Swap values
x, y = y, x

# Assign same value to multiple variables
x = y = z = 0
        """)

        # Interactive Compound Assignment
        st.markdown("### 🎮 Compound Assignment Explorer")

        if 'variable_value' not in st.session_state:
            st.session_state.variable_value = 10

        col7, col8 = st.columns(2)

        with col7:
            st.markdown("#### Current Value:")
            st.code(f"value = {st.session_state.variable_value}")

            operation = st.selectbox(
                "Select compound operation:",
                ["+=", "-=", "*=", "/=", "//=", "%=", "**="]
            )

            amount = st.number_input("Amount:", value=2)

        with col8:
            if st.button("Apply Operation"):
                if operation == "+=":
                    st.session_state.variable_value += amount
                elif operation == "-=":
                    st.session_state.variable_value -= amount
                elif operation == "*=":
                    st.session_state.variable_value *= amount
                elif operation == "/=":
                    if amount != 0:
                        st.session_state.variable_value /= amount
                elif operation == "//=":
                    if amount != 0:
                        st.session_state.variable_value //= amount
                elif operation == "%=":
                    if amount != 0:
                        st.session_state.variable_value %= amount
                elif operation == "**=":
                    st.session_state.variable_value **= amount

            st.markdown("#### Operation Explanation:")
            st.code(f"""
# Before:
value = {st.session_state.variable_value}

# Operation:
value {operation} {amount}

# Equivalent to:
value = value {operation[0]} {amount}
            """)

        # Value History Visualization
        if 'value_history' not in st.session_state:
            st.session_state.value_history = [10]

        if len(st.session_state.value_history) == 0 or st.session_state.value_history[-1] != st.session_state.variable_value:
            st.session_state.value_history.append(st.session_state.variable_value)

        # Plot value history
        fig_hist = go.Figure()

        fig_hist.add_trace(go.Scatter(
            x=list(range(len(st.session_state.value_history))),
            y=st.session_state.value_history,
            mode='lines+markers',
            name='Value History'
        ))

        fig_hist.update_layout(
            title='Value Changes Over Operations',
            xaxis_title='Operation Number',
            yaxis_title='Value',
            height=400
        )

        st.plotly_chart(fig_hist)

        # Practical Examples
        st.markdown("### 🌟 Practical Assignment Examples")
        with st.expander("Real-world Applications"):
            st.markdown("""
            1. **Score Counter**
            """)

            if 'game_score' not in st.session_state:
                st.session_state.game_score = 0

            col9, col10 = st.columns(2)

            with col9:
                if st.button("Hit Target (+10)"):
                    st.session_state.game_score += 10
                if st.button("Collect Coin (+5)"):
                    st.session_state.game_score += 5
                if st.button("Take Damage (-3)"):
                    st.session_state.game_score -= 3
                if st.button("Reset Score"):
                    st.session_state.game_score = 0

            with col10:
                st.markdown("#### Score Updates:")
                st.code(f"""
Current Score: {st.session_state.game_score}

# Using compound assignments:
score += 10  # Hit target
score += 5   # Collect coin
score -= 3   # Take damage
score = 0    # Reset score
                """)

            st.markdown("""
            2. **Bank Account**
            """)

            if 'balance' not in st.session_state:
                st.session_state.balance = 1000.0

            amount = st.number_input("Transaction amount:", -1000.0, 1000.0, 0.0)

            col11, col12 = st.columns(2)

            with col11:
                if st.button("Deposit"):
                    st.session_state.balance += amount
                if st.button("Withdraw"):
                    st.session_state.balance -= amount

            with col12:
                st.markdown("#### Account Balance:")
                st.code(f"""
Previous balance: ${st.session_state.balance - amount}
Transaction: ${amount}
Current balance: ${st.session_state.balance}
                """)

        # Summary of All Operations
        st.markdown("### 📚 Operations Summary")
        with st.expander("Complete Operations Reference"):
            st.markdown("""
            #### 1. Arithmetic Operations
            - `+` Addition
            - `-` Subtraction
            - `*` Multiplication
            - `/` Division
            - `**` Power
            - `//` Integer division
            - `%` Modulo (remainder)

            #### 2. Comparison Operations
            - `==` Equal to
            - `!=` Not equal to
            - `>` Greater than
            - `<` Less than
            - `>=` Greater than or equal to
            - `<=` Less than or equal to

            #### 3. Logical Operations
            - `and` Logical AND
            - `or` Logical OR
            - `not` Logical NOT

            #### 4. Assignment Operations
            - `=` Basic assignment
            - `+=` Add and assign
            - `-=` Subtract and assign
            - `*=` Multiply and assign
            - `/=` Divide and assign
            - `//=` Integer divide and assign
            - `%=` Modulo and assign
            - `**=` Power and assign
            """)

            st.markdown("""
            ### Best Practices 🎯
            
            1. **Clarity First**
               - Use parentheses to make operations clear
               - Break complex operations into steps
            
            2. **Common Pitfalls**
               - Division by zero
               - Integer vs float division
               - Operator precedence confusion
            
            3. **Performance Tips**
               - Use compound assignments when possible
               - Be careful with very large numbers in power operations
               - Consider readability over clever one-liners
            """)

    # Final Practice Exercise
    st.markdown("### 🎯 Final Practice Exercise")
    with st.expander("Try All Operations"):
        st.markdown("""
        Create a simple calculator that combines all types of operations:
        """)

        num1 = st.number_input("Enter first number:", -100.0, 100.0, 10.0, key="final_num1")
        num2 = st.number_input("Enter second number:", -100.0, 100.0, 5.0, key="final_num2")

        arithmetic_op = st.selectbox("Select arithmetic operation:", ["+", "-", "*", "/", "**", "//", "%"])

        result = eval(f"{num1} {arithmetic_op} {num2}")

        comparison = st.selectbox("Compare result with:", [-100.0, 0.0, 100.0])

        comp_result = eval(f"{result} > {comparison}")

        st.code(f"""
# Step 1: Arithmetic Operation
{num1} {arithmetic_op} {num2} = {result}

# Step 2: Comparison
{result} > {comparison} is {comp_result}

# Step 3: Logical Operation
Result is positive AND greater than {comparison}: {result > 0 and result > comparison}
        """)