
# This is the running file for the invoice generator application

from invoice_generator import app

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
