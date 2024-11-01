from flask import Flask, render_template, request

from flask import jsonify, make_response

import pusher

import mysql.connector
import datetime
import pytz

con = mysql.connector.connect(
    host="185.232.14.52",
    database="u760464709_tst_sep",
    user="u760464709_tst_sep_usr",
    password="dJ0CIAFF="
)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pago_curso():
    if request.method == 'POST':
        # Obtener datos del formulario
        telefono = request.form['telefono']
        confirmar_telefono = request.form['confirmar_telefono']
        archivo = request.files['archivo']

        # Validaciones básicas (más detalladas en jQuery)
        if not telefono.isdigit() or len(telefono) != 10 or telefono != confirmar_telefono:
            return render_template('pago_curso.html', error='Error en el número de teléfono')
        if not allowed_file(archivo.filename):
            return render_template('pago_curso.html', error='Tipo de archivo no válido')

        # Si todas las validaciones pasan, procesar el formulario
        # ... (guardar archivo, enviar correo, etc.)
        return 'Pago registrado correctamente'

    return render_template('pago_curso.html')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
