from flask import Flask, render_template
import unirest

app = Flask(__name__)
MASHAPE_KEY = "YOUR MASHAPE KEY GOES HERE"

# These code snippets use an open-source library. http://unirest.io/python
response = unirest.get("https://yoda.p.mashape.com/yoda?sentence=You+will+learn+how+to+speak+like+me+someday.++Oh+wait.",
  headers={
    "X-Mashape-Key": MASHAPE_KEY,
    "Accept": "text/plain"
  }
)
print(response.body)

@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
