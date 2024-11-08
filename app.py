from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)

supported_languages = {
    "en": "English",
    "es": "Spanish",
    "pt": "Portuguese",
}

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get("text")
    target_lang = data.get("target_lang", "en")
    
    if not text:
        return jsonify({"error": "Texto não fornecido para tradução"}), 400

    if target_lang not in supported_languages:
        return jsonify({"error": "Idioma não suportado"}), 400

    try:
        translation = GoogleTranslator(source='auto', target=target_lang).translate(text)
        print("Texto traduzido:", translation)
        return jsonify({"translated_text": translation}), 200
    except Exception as e:
        print("Erro na tradução:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/languages', methods=['GET'])
def get_languages():
    return jsonify(supported_languages), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
