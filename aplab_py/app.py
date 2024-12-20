import streamlit as st
import importlib

st.set_page_config(
    page_title="APlab",
    page_icon="🔬",
    layout="wide"
)


# Get language from URL parameters
current_lang = st.query_params.get('lang', ['en'])[0]


TOPICS = {
    "0. Programming Fundamentals": {
        "0.1 Programming Basics": "aplab_py.topics.t00_fundamentals.t01_programming_basics",
    },
    "1. Python Basics": {
        "1.1 Variables": "aplab_py.topics.t01_basics.t01_variables",
        "1.2 Data Types": "aplab_py.topics.t01_basics.t02_data_types",
        "1.3 Operations": "aplab_py.topics.t01_basics.t03_operations"
    },
    # "2. Control Flow": {
    #     "2.1 Conditionals": "aplab_py.topics.t02_control_flow.t01_conditionals",
    #     "2.2 Loops": "aplab_py.topics.t02_control_flow.t02_loops",
    #     "2.3 Functions": "aplab_py.topics.t02_control_flow.t03_functions"
    # },
    # "3. Data Structures": {
    #     "3.1 Lists": "aplab_py.topics.t03_data_structures.t01_lists",
    #     "3.2 Dictionaries": "aplab_py.topics.t03_data_structures.t02_dictionaries",
    #     "3.3 Sets": "aplab_py.topics.t03_data_structures.t03_sets"
    # }
}

# Translations
TRANSLATIONS = {
    'en': {
        'title': 'APlab - Interactive Python Learning',
        'select_category': 'Select Category',
        'select_topic': 'Select Topic',
        'error_loading': 'Error loading topic'
    },
    'ru': {
        'title': 'APlab - Интерактивное Изучение Python',
        'select_category': 'Выберите Категорию',
        'select_topic': 'Выберите Тему',
        'error_loading': 'Ошибка загрузки темы'
    }
}

def get_text(key):
    return TRANSLATIONS[current_lang].get(key, TRANSLATIONS['en'][key])

def main():
    st.title(get_text('title'))

    st.sidebar.title(get_text('select_category'))

    selected_category = st.sidebar.selectbox(
        get_text('select_category'),
        list(TOPICS.keys())
    )

    selected_topic = st.sidebar.selectbox(
        get_text('select_topic'),
        list(TOPICS[selected_category].keys())
    )

    module_path = TOPICS[selected_category][selected_topic]
    try:
        module = importlib.import_module(module_path)
        module.show()
    except Exception as e:
        st.error(f"{get_text('error_loading')}: {str(e)}")
        st.error(f"Module path: {module_path}")

if __name__ == "__main__":
    main()
