
from flask import render_template
from weasyprint import HTML
from invoice_generator import app
from datetime import datetime


@app.route("/")
def index():

    d = datetime.now()
    new_date = d.strftime("%B") + " " + d.strftime("%d") + ", " + d.strftime("%Y")

    return render_template("invoice.html", date=new_date)



def generate_pdf():

    file_path = "./invoice_generator/templates/invoice.html"

    my_html = HTML(file_path)
    my_html.write_pdf("./invoice.pdf")
