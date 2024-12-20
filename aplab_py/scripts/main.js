// main.js

// Global state
let currentLang = localStorage.getItem('language') || 'en';

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Check if language switcher exists
    const langSwitcher = document.querySelector('.language-switcher');
    if (!langSwitcher) {
        console.warn('Language switcher not found in DOM');
    }

    // Check if language buttons exist
    const langButtons = document.querySelectorAll('.lang-btn');
    if (langButtons.length === 0) {
        console.warn('Language buttons not found');
    }

    document.querySelectorAll('.lang-btn .feather-icon').forEach(icon => {
        icon.setAttribute('width', '16');
        icon.setAttribute('height', '16');
    });

    initLanguage();
    initNavigation();
    initStreamlit();
    initIcons();
    updateIframeLanguage();
});

// Language management
function initLanguage() {
    // Set initial language
    const savedLang = localStorage.getItem('language') || 'en';
    changeLanguage(savedLang);
    
    // Make sure buttons are visible and working
    console.log('Language initialized:', savedLang);
}

function changeLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('language', lang);
    
    // Update content
    updateContent();
    updateLanguageButtons();
    updateHTMLLang();
    
    // Log for debugging
    console.log('Language changed to:', lang);
}

function updateLanguageButtons() {
    document.querySelectorAll('.lang-btn').forEach(btn => {
        const btnLang = btn.getAttribute('data-lang');
        if (btnLang === currentLang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
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
                'width': 24,        // Use numbers instead of units
                'height': 24,       // Use numbers instead of units
                'stroke-width': 2,
                class: 'feather-icon' // Add a class for easier styling
            });
        } catch (error) {
            console.warn('Error initializing icons:', error);
        }
    }
}

// Retry icon initialization on window load
window.addEventListener('load', () => {
    if (typeof feather !== 'undefined') {
        initIcons();
    }
});