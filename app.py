from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

# Создаем объект Translator
translator = Translator()

# Функция для перевода текста
def translate_text(text, source_lang, target_lang):
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)
    return translated_text.text

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Обработка формы перевода
@app.route('/translate', methods=['POST'])
def translate():
    source_text = request.form['source_text']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    translated_text = translate_text(source_text, source_lang, target_lang)
    return render_template('index.html', translated_text=translated_text)

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)