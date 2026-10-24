from utils.dictionaries import lang_memory
phrases = {
    "start": {"uz":  }
}

def get_test(label, user_id):
    lang = lang_memory.get(user_id, "uz")
    return phrases[label][lang]