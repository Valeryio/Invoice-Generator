
from flask import render_template, send_file
from weasyprint import HTML
from invoice_generator import app
from datetime import datetime
import io


@app.route("/")
def index():

    d = datetime.now()
    new_date = d.strftime("%B") + " " + d.strftime("%d") + ", " + d.strftime("%Y")

    file_path = "./invoice_generator/templates/invoice.html"
    render = render_template("invoice.html", date=new_date)

    my_html = HTML(string=render)
    my_html.write_pdf("./pdf/invoice.pdf")
    rendered_pdf = my_html.write_pdf()

    return send_file(io.BytesIO(rendered_pdf), download_name="invoice.pdf")



def generate_pdf():

    file_path = "./invoice_generator/templates/invoice.html"
    my_html = HTML(file_path)
    my_html.write_pdf("./invoice.pdf")
