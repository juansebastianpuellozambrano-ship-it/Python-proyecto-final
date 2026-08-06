from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/segunda_ruta")
def otro_nombre():
    return render_template("index2.html")

@app.route("/front", methods=["post", "get"])  # backend
def nombre3():
    name = request.form.get("nombre")
    password = request.form.get("contr")
    date = request.form.get("fecha")
    print(name, password, date)
    return render_template("otra_plantilla.html", papoi=name, papoi2=password, papoi3=date)



app.run()

