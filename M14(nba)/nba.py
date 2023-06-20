from flask import Flask, render_template,request,redirect,url_for
from flask_mysqldb import MySQL
import csv
import pandas as pd
import mysql.connector

app = Flask(__name__)


# funciones

# def leerArchivo():
#     df= pd.read_csv("NBA_Stats.csv")
#     df = pd.DataFrame(df)
#     df = df.drop(["GP","MPG","USG%","TO%","FTA","FT%","eFG%","TS%","VI","ORtg","DRtg"],axis=1)
#     return df

def conectarbd():
    bd = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "metamorfo2", 
        database = "NBA")
    return bd

def iniciarbd():
    bd = conectarbd()
    cursor = bd.cursor()
    
    query = "create table if not exists usuario(\
    usuario varchar(50) not null primary key,\
    nombre varchar(50) not null,\
    apellidos varchar(50) not null,\
    edad int not null,\
    nacionalidad varchar(100),\
    contraseña varchar(50) not null);"
    cursor.execute(query)
    bd.commit()
    bd.close()
    
def crearUsuario(usuario, nombre, apellidos, edad, nacionalidad, contrasena):
    bd = conectarbd()
    cursor = bd.cursor()
    query = "insert into usuarios(usuario, nombre, apellidos, edad, nacionalidad, contrasena) value(%s,%s,%s,%s,%s,%s)"
    values = (f"{usuario}",f"{contrasena}",f"{nombre}",f"{apellidos}",f"{edad}",f"{nacionalidad}")
    cursor.execute(query,values)
    n = cursor.rowcount
    bd.commit()
    bd.close()
    return n

def aceptarUsuario(usuario,contrasena):
    bd = conectarbd()
    cursor = bd.cursor()
    query = f"""SELECT usuario,contrasena FROM usuarios WHERE usuario=%s\
        AND contrasena=%s"""
    valores = (usuario, contrasena)
    cursor.execute(query, valores)
    bd.close()
    if usuario == []:
        return False
    else:
        return True
 
# Rutas
 
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    conectarbd()
    return render_template("login.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")
        
@app.route ("/confirmarUsuario",methods=("GET","POST"))
def confirmarUsuario():
       if request.method == "POST":
        formData = request.form
        usuario = formData['usuario']
        contrasena = formData['contrasena']
        confirmar = aceptarUsuario(usuario, contrasena)
        if confirmar == True:
            return redirect(url_for("seleccionar_imagen"))
        else:
            return render_template("login.html")
        
@app.route("/nuevoUsuario", methods=("GET","POST"))
def nuevoUsuario():
    if request.method == "POST":
        #es un diccionario que contiene los campos y valores del formulario
        formData = request.form
        #obtencion de valores
        usuario = formData['usuario']
        nombre = formData['nombre']
        apellidos = formData['apellidos']
        edad = formData['edad']
        nacionalidad = formData['nacionalidad']
        contrasena = formData['contrasena']
        #crear un nuevo usuario con los datos proporcionados
        datosUsuario = crearUsuario(usuario, nombre, apellidos, edad, nacionalidad, contrasena)
        if datosUsuario == True:
            return render_template("home.html")
        else:
            return render_template("home.html")


@app.route('/formulario',methods=['GET','POST'])
def seleccionar_imagen():
    if request.method == 'POST':
        # el código obtiene el valor de la opción seleccionada en el formulario
        opcion = request.form['opciones']
        data = pd.read_csv("NBA_Stats.csv")
        # despusharemos un render a nuestro html con la variableanterior
        return render_template('formulario.html', imagen=opcion, data=data)    
    else :
        return render_template('formulario.html')


    
# Configuración y arranque de la aplicación web
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(host='localhost', port=5000, debug=True)


