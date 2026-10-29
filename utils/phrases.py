phrases = {
    "start": {"uz": "Assalomu Aleykum, tilni tanlang", "ru": "Здравствуйте, выберите язык", "en": "Hi, pick a language"},
    "test_drive": {"uz": "🎯 Test-drayv", "ru": "🎯 Тест-драйв", "en": "🎯 Test-drive"},
    "buy_a_car": {"uz": "🚗 Moşina sotib oliş", "ru": "🚗 Купить машину", "en": "🚗 Buy a car"},
    "lookup": {"uz": "Konfiguratsiyalarini körish 🔎", "ru": "Просмотреть конфигурации 🔎", "en": "View configurations 🔎"},
    "about": {"uz": "Haqida ❓", "ru": "О нас ❓", "en": "About ❓"},
    "review": {"uz": "Bizni baholaş ⭐️", "ru": "Оцените нас ⭐️", "en": "Review us ⭐️"},
    "request": {"uz": "Texnik xizmat 🛠", "ru": "технический осмотр 🛠", "en": "Car maintenance 🛠"},
    "show_contacts": {"uz": "Kontaktlarni körish ☎️", "ru": "Посмотреть контакты ☎️", "en": "Show contacts ☎️"},
    "lang_set": {"uz": "Til örnatildi", "ru": "Язык установлен", "en": "Language set"},
    "about_explanation": {"uz": "General Motors dunyodagi eng yirik avtomobil ishlab chiqaruvchi kompaniyalardan biri bo’lib, 1908-yilda Michigan shtatining Flint shahrida tashkil topgan va shtab-kvartirasi Detroytda joylashgan. Uning brendlari orasida Chevrolet, Buick, GMC va Cadillac bor. Bizning dilerlik markazimiz barcha GM avtomobillari uchun sinov haydashlar, modellar va konfiguratsiyalarning to’liq tanlovi hamda texnik xizmat ko’rsatishni taklif etadi.", "ru": "General Motors — один из крупнейших автопроизводителей в мире. Компания основана в 1908 году во Flint, штат Мичиган, а её штаб-квартира находится в Детройте. В число её брендов входят Chevrolet, Buick, GMC и Cadillac. Наш автосалон предлагает тест-драйвы, полный выбор моделей и комплектаций, а также техническое обслуживание для всех автомобилей GM.", "en": "General Motors is one of the world’s largest automakers, founded in 1908 in Flint, Michigan, and headquartered in Detroit. Its brands include Chevrolet, Buick, GMC, and Cadillac. Our dealership offers test drives, a full range of models and configurations, and maintenance support for every GM vehicle."},

}

def get_text(label: str, lang: str) -> str:
    return phrases[label][lang]