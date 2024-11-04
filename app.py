from flask import Flask, request, jsonify
from googletrans import Translator
from googletrans import LANGUAGES 

app = Flask(__name__)

translator = Translator()

supported_languages = LANGUAGES  

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
        translation = translator.translate(text, dest=target_lang)
        return jsonify({"translated_text": translation.text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/languages', methods=['GET'])
def get_languages():
    return jsonify(supported_languages), 200

if __name__ == '__main__':
    app.run(debug=True)
