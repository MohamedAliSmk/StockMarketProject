const setLanguage = (language) => {
    const elements = document.querySelectorAll("[data-i18n]");
    elements.forEach((element) => {
        const translationKey = element.getAttribute("data-i18n");
        element.textContent = translations[language][translationKey];
    });
    document.dir = language === "ar" ? "rtl" : "ltr";
    
    // update URL parameter with new language preference
    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set('lang', language);
    const newUrl = window.location.pathname + '?' + urlParams.toString();
    window.history.replaceState(null, null, newUrl);
};

const languageSelector = document.querySelector("#language-selector");
languageSelector.addEventListener("change", (event) => {
    setLanguage(event.target.value);
    // update language preference in URL parameter
    window.history.replaceState(null, null, "?lang=" + event.target.value);
});

document.addEventListener("DOMContentLoaded", () => {
    let language = "{{ user_language }}";
    if (!language) {
        const urlParams = new URLSearchParams(window.location.search);
        language = urlParams.get('lang') || "en"; // default to English if no lang parameter is found
    }
    console.log('language preference:', language);
    setLanguage(language);
});
