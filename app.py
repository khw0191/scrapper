from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def search():
    params = request.args.get("keyword")
    print(params)
    return render_template("search.html", keyword=params)



if __name__ == '__main__':
    app.run(debug=True)