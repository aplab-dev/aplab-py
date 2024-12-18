import streamlit as st
import importlib

st.set_page_config(
    page_title="APlab",
    page_icon="🔬",
    layout="wide"
)

TOPICS = {
    "0. Programming Fundamentals": {
        "0.1 Programming Basics": "aplab.topics.t00_fundamentals.t01_programming_basics",
    },
    "1. Python Basics": {
        "1.1 Variables": "aplab.topics.t01_basics.t01_variables",
        "1.2 Data Types": "aplab.topics.t01_basics.t02_data_types",
        "1.3 Operations": "aplab.topics.t01_basics.t03_operations"
    },
    "2. Control Flow": {
        "2.1 Conditionals": "aplab.topics.t02_control_flow.t01_conditionals",
        "2.2 Loops": "aplab.topics.t02_control_flow.t02_loops",
        "2.3 Functions": "aplab.topics.t02_control_flow.t03_functions"
    },
    "3. Data Structures": {
        "3.1 Lists": "aplab.topics.t03_data_structures.t01_lists",
        "3.2 Dictionaries": "aplab.topics.t03_data_structures.t02_dictionaries",
        "3.3 Sets": "aplab.topics.t03_data_structures.t03_sets"
    }
}

def main():
    st.title("APlab - Interactive Python Learning")

    st.sidebar.title("Topics")

    selected_category = st.sidebar.selectbox(
        "Select Category",
        list(TOPICS.keys())
    )

    selected_topic = st.sidebar.selectbox(
        "Select Topic",
        list(TOPICS[selected_category].keys())
    )

    module_path = TOPICS[selected_category][selected_topic]
    try:
        module = importlib.import_module(module_path)
        module.show()
    except Exception as e:
        st.error(f"Error loading topic: {str(e)}")
        st.error(f"Module path: {module_path}")

if __name__ == "__main__":
    main()