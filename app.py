from flask import Flask, render_template, request, redirect, send_file
from scrapper import search_incruit
from file import save_to_file

app = Flask(__name__)

db = {}

# db = { 
#     "간호사": [1, 2, 3, 4, 5, ... 30]
# }

# db["간호사"]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def search():
    keyword = request.args.get("keyword")
    jobs = search_incruit(keyword, 2)

    db[keyword] = jobs
    
    return render_template(
        "search.html", 
        keyword=keyword, 
        jobs=jobs
        )

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    
    if keyword not in db:
        return redirect("/search")

    save_to_file(db[keyword])

    return send_file("./file.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)