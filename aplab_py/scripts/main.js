// main.js

// Global state
let currentLang = localStorage.getItem('language') || 'en';

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    initLanguage();
    initNavigation();
    initStreamlit();
    initIcons();
    updateIframeLanguage();
});

// Language management
function initLanguage() {
    changeLanguage(currentLang);
}

function changeLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('language', lang);
    updateContent();
    updateLanguageButtons();
    updateHTMLLang();
    updateIframeLanguage();
}

function updateContent() {
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[currentLang] && translations[currentLang][key]) {
            element.textContent = translations[currentLang][key];
        }
    });
}

function updateLanguageButtons() {
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-lang') === currentLang);
    });
}

function updateHTMLLang() {
    document.documentElement.lang = currentLang;
}

// Navigation
function initNavigation() {
    const header = document.querySelector('.nav-container');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll <= 0) {
            header.classList.remove('scroll-up');
            return;
        }

        if (currentScroll > lastScroll && !header.classList.contains('scroll-down')) {
            header.classList.remove('scroll-up');
            header.classList.add('scroll-down');
        } else if (currentScroll < lastScroll && header.classList.contains('scroll-down')) {
            header.classList.remove('scroll-down');
            header.classList.add('scroll-up');
        }
        lastScroll = currentScroll;
    });
}

// Streamlit integration
function initStreamlit() {
    const container = document.querySelector('.streamlit-container');
    if (container) {
        container.classList.add('loading');
        
        const iframe = container.querySelector('iframe');
        if (iframe) {
            iframe.addEventListener('load', () => {
                container.classList.remove('loading');
            });
        }
    }
}

// Update Streamlit iframe language
function updateIframeLanguage() {
    const iframe = document.querySelector('.streamlit-container iframe');
    if (iframe) {
        const currentSrc = new URL(iframe.src);
        currentSrc.searchParams.set('lang', currentLang);
        iframe.src = currentSrc.toString();
    }
}

// Error handling
window.addEventListener('error', function(e) {
    console.warn('Global error:', e.message);
});

// Performance monitoring
if (window.performance) {
    window.addEventListener('load', function() {
        const timing = window.performance.timing;
        const pageLoad = timing.loadEventEnd - timing.navigationStart;
        console.log('Page load time:', pageLoad + 'ms');
    });
}

function initIcons() {
    if (typeof feather !== 'undefined') {
        try {
            feather.replace({
                'width': 24,
                'height': 24,
                'stroke-width': 2
            });
        } catch (error) {
            console.warn('Error initializing icons:', error);
        }
    } else {
        console.warn('Feather icons not loaded');
    }
}

// Retry icon initialization on window load
window.addEventListener('load', () => {
    if (typeof feather !== 'undefined') {
        initIcons();
    }
});