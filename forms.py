from wtforms import Form, StringField, PasswordField, BooleanField, SelectField, SubmitField, validators
from wtforms.fields.html5 import EmailField

class Formulario_Usuario(Form):
    email = StringField('Correo electronico', 
    [ 
        validators.DataRequired(), 
        validators.Length(min=8,max=25)
    ] )
    password = PasswordField('Contraseña',
    [ 
        validators.DataRequired(), 
        validators.Length(min=8,max=25) 
    ])
    recordar = BooleanField('Recordar correo electronico')
    enviar = SubmitField('Iniciar sesión')
    
