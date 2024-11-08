from translate import Translator


def translate_text(text, target_lang="en"):
    translator = Translator(to_lang=target_lang)
    try:
        translation = translator.translate(text)
        return translation
    except Exception as e:
        print(f"Erro na tradução: {e}")
        return None
