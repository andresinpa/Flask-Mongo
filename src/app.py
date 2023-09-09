from flask import Flask, flash, redirect, render_template, request, url_for
from config import *
from visitante import Visitante

con_bd = Conexion() #Creación de instancia de conexión
app = Flask(__name__)
app.secret_key = 'admin'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/camilo')
def camilo():
    return render_template("camilo_bio.html")

@app.route('/lore')
def lorena():
    return render_template("lorena_bio.html")

@app.route('/jesus')
def jesus():
    return render_template("jesus_bio.html")

@app.route('/comentarios')
def comentario():
    return render_template("formulario.html")

def error_404(error):
    return render_template('error_404.html'), 404

@app.route('/guardar_visitantes', methods=['POST'])
def agregarVisitante():
    visitantes = con_bd['Visitantes']
    nombre = request.form['nombre']
    correo = request.form['correo']
    comentario = request.form['comentario']
    
    if nombre and correo and comentario:
        visitante = Visitante(nombre ,correo, comentario) #Metodo constructor
        visitantes.insert_one(visitante.format_doc()) #Insertando docuemnto dentro de la colección
        flash('¡Comentario enviado exitosamente! 👍')
        return redirect(url_for('index'))
    else:
        flash('Error: Todos los campos son obligatorios. 👀')
        return render_template("formulario.html")

if __name__ == '__main__':
    app.register_error_handler(404, error_404)
    app.run(debug=True, port=9999)