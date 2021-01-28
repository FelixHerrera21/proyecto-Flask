from flask import Flask, render_template

#Funcion inicial obligatoria
app = Flask(__name__)

"""
#Ejemplo pagina de inicio
@app.route("/inicio")
def inicio():
	return "pagina de inicio!"
"""
"""
#Ejemplo paso de parametro
@app.route("/inicio")
def inicio():
	variable = "kola"
	return render_template("inicio.html", variable1 = variable)
"""

"""
#Ejemplo if
@app.route("/ejemploif")
def ejemploif():
	variable = 1
	return render_template("ejemploif.html", variable1 = variable)
"""
"""
#Ejemplo for
@app.route("/ejemplofor")
def ejemplofor():
	variable = [4,3,2,1]
	return render_template("ejemplofor.html", variable1 = variable)
"""

#Ejemplo for
@app.route("/ejemplobase")
def ejemplobase():
	variable = 3
	return render_template("ejemplobase.html", variable1 = variable)

#Esta funcion es para debug
if __name__ == "__main__":
	app.run(debug = True)