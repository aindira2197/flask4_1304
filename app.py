from flask import Flask, render_template

app = Flask(__name__)

@app.route('/mahsulotlar')
def mahsulotlar():
    data = ["Non", "Sut", "Olma"]
    return render_template('mahsulotlar.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
