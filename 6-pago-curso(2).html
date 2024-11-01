from flask import Flask, request, render_template, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def mostrar_formulario():
    return render_template('pago_curso.html')

@app.route('/procesar_pago', methods=['POST'])
def procesar_pago():
    if 'comprobante' not in request.files:
        flash('No se envió ningún archivo')
        return redirect(url_for('mostrar_formulario'))
    
    file = request.files['comprobante']
    if file.filename == '':
        flash('No se seleccionó ningún archivo')
        return redirect(url_for('mostrar_formulario'))

    telefono = request.form.get('telefono')
    confirmar_telefono = request.form.get('confirmarTelefono')

    if telefono != confirmar_telefono:
        flash('Los números de teléfono no coinciden')
        return redirect(url_for('mostrar_formulario'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Pago registrado correctamente')
        return redirect(url_for('mostrar_formulario'))
    else:
        flash('Tipo de archivo no permitido')
        return redirect(url_for('mostrar_formulario'))

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
