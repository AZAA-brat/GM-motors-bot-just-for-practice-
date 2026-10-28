phrases = {
    "start": {"uz": "Assalomu Aleykum, tilni tanlang", "ru": "Здравствуйте, выберите язык", "en": "Hi, pick a language"},
    "test_drive": {"uz": "🎯 Test-drayv", "ru": "🎯 Тест-драйв", "en": "🎯 Test-drive"},
    "buy_a_car": {"uz": "🚗 Moşina sotib oliş", "ru": "🚗 Купить машину", "en": "🚗 Buy a car"},
    "lookup": {"uz": "Konfiguratsiyalarini körish 🔎", "ru": "Просмотреть конфигурации 🔎", "en": "View configurations 🔎"},
    "about": {"uz": "Haqida ❓", "ru": "О нас ❓", "en": "About ❓"},
    "review": {"uz": "Bizni baholaş ⭐️", "ru": "Оцените нас ⭐️", "en": "Review us ⭐️"},
    "request": {"uz": "Texnik xizmat 🛠", "ru": "технический осмотр 🛠", "en": "Car maintenance 🛠"},
    "show_contacts": {"uz": "Kontaktlarni körish ☎️", "ru": "Посмотреть контакты ☎️", "en": "Show contacts ☎️"},
}

def get_text(label: str, lang: str) -> str:
    return phrases[label][lang]