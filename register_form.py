from wtforms import form, StringField, TextAreaField, PasswordField, validators


#with wt forms you have to create a class for the form you are creating.


class RegisterForm(Form):
    user_name = StringField('User Name', [validators.Length(min = 4, max = 25)])
    email = StringField('Email: ', [validators.Length(min = 6, max = 25)])
    password = StringField('Password: ', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Passwords do not match")
        ]
    )
    confirm = PasswordField('Confirm Password')