import os
from flask import Flask, render_template
from dotenv import load_dotenv
import datetime
from deta import Deta

load_dotenv()

DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)

app = Flask(__name__)

now = datetime.datetime.now()

cotm_db =deta.Base("CoTM_File")
arch_db =deta.Base("Arch_File")
urban_db = deta.Base("Urban_File")

@app.route('/')
def home():
    """
    Home page
    """
    return render_template('home.html')

@app.route('/CoTM')
def cotm():
    """
    CoTM page
    """
    return render_template('cotm.html')

@app.route("/CoTM/<int:year>")
def cotm_year(year):
    """sumary_line
        year - file for specifc year
        Return: info, desc, resources, assignments, projects... of specifc year
    """
    # db.put({"file_name":"Life Cycle Cost Analysis", "file_type":"Project", "course_title":"Cost Efficent Construction", "year":year, "submitted_year":"2015", "uploaded_at":now.strftime("%d/%m/%y, %H:%M")})
    specific_year=cotm_db.fetch({"year":year}).items
    # print(specific_year)
    year_desc=[
        "In this year(1st) of CoTM BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(2nd) of CoTM BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(3rd) of CoTM BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(4th) of CoTM BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(5th) of CoTM BSc program this courses generally given..., And this...this.. concept are generally covered"
        ]
    return render_template("files.html", year=year, dep="CoTM", files=specific_year, year_desc=year_desc[year-1])

@app.route('/Arch')
def arch():
    """
    Arch page
    """
    return render_template('arch.html')

@app.route("/Arch/<int:year>")
def arch_year(year):
    """sumary_line
        year - file for specifc year
        Return: info, desc, resources, assignments, projects... of specifc year
    """
    specific_year=arch_db.fetch({"year":year}).items
    year_desc=[
        "In this year(1st) of Architecture BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(2nd) of Architecture BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(3rd) of Architecture BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(4th) of Architecture BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(5th) of Architecture BSc program this courses generally given..., And this...this.. concept are generally covered"
        ]
    return render_template("files.html", year=year, dep="Arch", files=specific_year, year_desc=year_desc[year-1])


@app.route('/Urban')
def urban():
    """
    Urban page
    """
    return render_template('urban.html')

@app.route('/Urban/<int:year>')
def urban_year(year):
    """sumary_line
        year - file for specifc year
        Return: info, desc, resources, assignments, projects... of specifc year
    """
    specific_year=urban_db.fetch({"year":year}).items
    year_desc=[
        "In this year(1st) of Urban BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(2nd) of Urban BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(3rd) of Urban BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(4th) of Urban BSc program this courses generally given..., And this...this.. concept are generally covered",
        "In this year(5th) of Urban BSc program this courses generally given..., And this...this.. concept are generally covered"
        ]
    return render_template("files.html", year=year, dep="Urban", files=specific_year, year_desc=year_desc[year-1])

if __name__ == "__main__":
    app.run(debug=True, host="192.168.1.14", port=5050)
    # app.run(debug=True, host="127.0.0.1", port=5055)