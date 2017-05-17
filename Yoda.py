from flask import Flask, render_template, request
import unirest

app = Flask(__name__)
MASHAPE_KEY = "YOUR MASHAPE KEY HERE"


def yoda_says(input_text):
    # remove the first character '=' from decode function
    input_words = input_text[1:]
    # split based on %20, (html space)
    input_words = input_words.replace("%20", "+")
    response = unirest.get(
        "https://yoda.p.mashape.com/yoda?sentence=" + input_words,
        headers={
            "X-Mashape-Key": MASHAPE_KEY,
            "Accept": "text/plain"
        }
    )
    return (response.body)


@app.route('/api/yoda_speak', methods=['POST'])
def story():

    input = request.data.decode(encoding='UTF-8')
    return yoda_says(input)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
