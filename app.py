from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")

def find_word(name):
    definition = df.loc[df['word'].str.lower() == name.lower(), 'definition']
    if not definition.empty:  # Check if the result is not empty
        return definition.iloc[0]  # Return the first (and only) definition
    else:
        return None  


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/api/v1/<word>")
def hello_world(word):
    definition = find_word(word)
    if definition:
            return jsonify({
            "word": word,
            "definition": definition
        })
    else:
        return jsonify({
            "word": word,
            "definition": "Sorry!, Word Not Found"
        })


