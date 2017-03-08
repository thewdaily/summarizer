import os
from flask import Flask
from flask import render_template

from flask import jsonify
from flask import request
from textteaser import TextTeaser
import nltk
app = Flask(__name__)
app.debug = False

@app.route("/")
def home():
    return render_template('summarize.html')

@app.route("/summarize", methods=['POST'])
def summarize():
	title = request.form.get('title')
	text = request.form.get('text')

	tt = TextTeaser()

	sentences = tt.summarize(title, text)
	summary = { "sentences": [] }
	for sentence in sentences:
		print sentence
		summary["sentences"].append(sentence)

	return jsonify(summary)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)