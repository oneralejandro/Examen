from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')





@app.route('/calculoCompras', methods=['GET', 'POST'])
def calculoCompras():
    if request.method == 'POST':
        res =None
        resSinDesco = None
        resTotal = None
        nombre = str(request.form['nombre'])
        edad = float(request.form['edad'])
        cantidadTarros = float(request.form['cantidadTarros'])

        resultado = nombre
        if edad >= 18 and edad <=30:
            resSinDesco = 9000 * cantidadTarros
            res = (cantidadTarros * 9000)/100 * 15
            resTotal = resSinDesco - (cantidadTarros * 9000)/100 * 15
        elif    edad > 30:
                resSinDesco = 9000 * cantidadTarros
                res = (cantidadTarros * 9000)/100 * 25
                resTotal = resSinDesco - (cantidadTarros * 9000)/100 * 25
        else:
            resSinDesco = 9000 * cantidadTarros
            res = "NO TIENE DESCUENTO POR SER MENOR A 18 AÑOS "
            resTotal = resSinDesco - (cantidadTarros * 9000) / 100 * 25
        return render_template('calculoCompras.html', resultado=resultado, nombre=nombre, edad = edad, cantidadTarros = cantidadTarros, res=res
                               ,resSinDesco = resSinDesco, resTotal = resTotal)
    return render_template('calculoCompras.html')




@app.route('/inicioSesion', methods=['GET', 'POST'])
def inicioSesion():
    if request.method == 'POST':
        resultado= None

        usuario = str(request.form['usuario'])
        contraseña = str(request.form['contraseña'])

        if usuario == "juan" and contraseña == "admin":
            resultado = "Bienvenido ADMINISTRADOR ", usuario;

        elif usuario == "pepe" and contraseña == "user":
            resultado = "Bienvenido USUARIO ", usuario;
        else:
            resultado = "Usuario y o contraseña incorrecta  !";




        return render_template('inicioSesion.html', resultado=resultado, usuario = usuario, contraseña = contraseña)
    return render_template('inicioSesion.html')










if __name__ == '__main__':
    app.run(debug=True)