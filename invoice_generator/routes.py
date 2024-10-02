
from flask import render_template, send_file
from weasyprint import HTML
from invoice_generator import app
from datetime import datetime
import io


@app.route("/")
def index():

    d = datetime.now()
    new_date = d.strftime("%B") + " " + d.strftime("%d") + ", " + d.strftime("%Y")

    # Get the render object that contains the HTML string, after the running
    # of the Motor Jinja
    render = render_template("invoice.html", date=new_date)

    my_html = HTML(string=render)

    # Writing to the local disk to save a copy of the pdf
    my_html.write_pdf("./pdf/invoice.pdf")

    # Getting the rendered pdf into an object
    rendered_pdf = my_html.write_pdf()

    # We use the io.BytesIO class to manipulate the PDF with binary mode, cause we don't
    # want to save it before sending the data
    return send_file(io.BytesIO(rendered_pdf), download_name="invoice.pdf")
