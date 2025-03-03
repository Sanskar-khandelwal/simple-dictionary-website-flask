from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


def find_word(name):
    df = pd.read_csv("dictionary.csv")
    defination = (df.loc[df['word'] == name], 'definition')
    if not definition.empty:
        return definition.squeeze()  # Return the definition
    else:
        return None  
    return defination


@app.route("/api/v1/<word>")
def hello_world(word):
    defination = find_word(word)
    if defination:       return jsonify({
            "word": word,
            "definition": defination
        })
    else:
        return jsonify({
            "word": word,
            "definition": "Sorry!, Word Not Found"
        })


if __name__ == "__main__":
    app.run(debug=True)