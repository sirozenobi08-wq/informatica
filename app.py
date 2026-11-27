from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def homepage():
    return render_template ("index.html")

@app.route("/tutti-i-viaggi")
def tutti_i_viaggi():
    return render_template ("tutti_i_viaggi.html")

@app.route("/destinazioni")
def destinazioni():
    return render_template ("destinazioni.html")

@app.route("/chi-siamo")
def chi_siamo():
    return render_template ("chi_siamo.html")

@app.route("/contatti")
def contatti():
    return render_template ("contatti.html")
if __name__ == "__main__":
    app.run(debug=True)

if  __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True)
