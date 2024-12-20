# aplab/config/styles.py

COLORS = {
    'primary': {
        'blue': '#2196F3',
        'green': '#4CAF50',
        'orange': '#FF5722'
    },
    'text': {
        'dark': '#000000',
        'light': '#FFFFFF',
        'grey': '#666666'
    },
    'background': {
        'white': '#FFFFFF',
        'light': '#F5F5F5',
        'dark': '#1E1E1E'
    },
    'accent': {
        'success': '#4CAF50',
        'warning': '#FFC107',
        'error': '#F44336'
    }
}

TEXT_STYLES = {
    'header': {
        'size': 20,
        'color': COLORS['text']['dark'],
        'family': 'Arial Bold'
    },
    'body': {
        'size': 14,
        'color': COLORS['text']['dark'],
        'family': 'Arial'
    },
    'code': {
        'size': 14,
        'color': COLORS['text']['light'],
        'family': 'Consolas'
    }
}

CHART_STYLES = {
    'node_colors': [COLORS['primary']['blue'],
                    COLORS['primary']['green'],
                    COLORS['primary']['orange']],
    'arrow_color': COLORS['text']['grey'],
    'background': COLORS['background']['white'],
    'border_color': COLORS['text']['dark']
}