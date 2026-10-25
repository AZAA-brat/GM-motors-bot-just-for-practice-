from utils.dictionaries import lang_memory
phrases = {
    "start": {"uz": "", "ru": "", "en": "" }
}

def get_text(label, user_id):
    lang = lang_memory.get(user_id, "uz")
    return phrases[label][lang]