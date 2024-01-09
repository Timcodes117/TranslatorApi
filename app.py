from flask import Flask, request, jsonify
from functions import get_translation, supported_languges
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return '''
    <br>
    this is a python translation api <br>
    
    visit <a href="github.com/timcodes117"> link </a> to learn more on this api
    
    '''


@app.route('/get_translation')
def get_translation_data():
    sentence = request.form['sentence']
    language = request.form['target-language']
    if sentence and language:
        result = get_translation.get_translations(sentence, language)
        if result['status'] == 200:
            return jsonify(result), 200
        else:
            return jsonify(result), 400
    else:
        return jsonify({"message": "sentence or language is not sent"}), 400


@app.route('/get_language_data')
def get_languages():
    lang_list = supported_languges.get_supported_languages()
    if lang_list:
        return jsonify(lang_list), 200
    else:
        return jsonify({"message": "no language data is available"}), 404


if __name__ == "__main__":
    app.run(debug=True)