https://www.coursehero.com/file/49730409/quiztxt/

Curso de Design thinking
https://multidimensionbase.blogspot.com/2020/12/design-thinking.html
https://www.passeidireto.com/arquivo/89231965/understanding-design-thinking-v-2

# BeginPython
BeginPython
#Para las excepciones
 except Exception as e:
            print("Error Message :", str(e))



#Página(s) para respuestas de frescoplay(solvedcode.com)

# también pip install --upgrade pip(Para instalar)
#Pasos para crear el ambiente: *python -m venv projenv
#*source projenv/Scripts/activate
#Nota: Para desactivar el ambiente virtual deactivate
#*pip3 install flask ó pip install flask
#python3 ó python (y se pone en la subconsola) -> import flask
#Nota: Para salir de la "subconsola" -> exit
#Para ejecutar simplement con py archivo.py
#Intento de solución problema de los ejercicios con frescoplay: python -m pip install --upgrade pip

#ERROR AL EJECUTAR UN ARCHIVO .PY ESTANDO EN EL ENVIRONMENT
#En ocasiones para poder que permita instalar flask_wtf por ejemplo debe agregarse --user al final
#Ejecutar proyecto con flask y otras cosas importadas(por ejemplo flask-wtf y ...sqlalchemy)
#Se debe tener en cuenta que si uno instala cosas estando ejecutando el environment es posible que solo se pueda ejecutar la app estando en ese #environment
#con pip install se instalan librerias como email_validator, flask_sqlalchemy, etc
Para ejecutar la app con todas las importaciones que se tienen sin estar en un environment: python -m flask run



#actualizar versión de pip 
#python -m pip



#Para configurar el puerto y el host:
#example: app.run(host="10.100.100.10", port=9566)


#Documentación extensiones flask: https://flask.palletsprojects.com/en/2.0.x/extensions/

##Para manejar las bases de datos:
#pip install flask-sqlalchemy
#para la activación de migraciones: pip install flask-migrate

#Para evitar problemas configurando variables de entorno: 
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = False

#Dudas: ¿Hay que ejecutar el ambiente para poder instalar o importar?

#Conectarse a una base de datos en flask
#instalando pip install flask_sqlalchemypu

#Página donde se crea el proyecto en la nube: https://www.pythonanywhere.com/user/gilbertrendon/files/home/gilbertrendon

#PENDIENTE(S)
#Hubieron problemas con sqlalchemy, se instaló con diferentes versiones de python, 
#Para el manejo de las conexiones con bd, se intentó con mysql con sql sin obtener éxito
#Principalmente se identificaron dificultades con las versiones de pip, de python, etc


#REVISAR SI ASÍ ME FUNCIONA LA CREACIÓN DE UNA CLASE DEBIDO A QUE ESTO SE BASA EN UNA DE ESTE MISMIO PROYECTO


#hackerrank CREATING WEB FORMS IN FLASK:
forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

# Define QuoteForm below
class QuoteForm(FlaskForm):
  qauthor = StringField("qauthor",[validators.DataRequired("This field is required"), validators.Length(min=3, max=100)])
  qstring = StringField("qauthor",[validators.DataRequired("This field is required"), validators.Length(min=3, max=200)])
################
addquote.html

QuoteForm : quoteform


#AYUDA FLASK
from helloapp import db# Define Quotes model belowclass Quotes(db.Model):id = db.Column(db.Integer, primary_key=True)quoteauthor = db.Column(db.String(100), index=True)quotestring = db.Column(db.String(200), index=True)def __repr__(self):return "<Quote : {}>".format(self.quotestring)
