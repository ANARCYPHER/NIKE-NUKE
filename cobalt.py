#from flask import Flask, render_template

#Instaces
#app = Flask(__name__) 

#Routes
#@app.route('/')

#def index():
#	return render_template("index.html")
###########################################
from flask import Flask, render_template, flash
#from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#Instaces
app = Flask(__name__) 
# Secret Key!
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

#class NamerForm(FlaskForm):
 #   name = StringField("What's Your Name?", validators=[DataRequired()])
 #   submit = SubmitField("Submit") 

#Routes
@app.route('/')

#def index():
		#return render_template("index.html")
  
@app.route('/')
def index():
	first_name = "Ripper"
	stuff = "This is Stuff"

	human_corpse  = ["African", "Asian", "Caucasian", "Latino", 00]
	return render_template("index.html", 
		first_name=first_name,
		stuff=stuff,
		human_corpse=human_corpse,)
  

@app.route('/user/<name>')

def user(name):
    return render_template('user.html', user_name=name)

#ERROR 404, 500
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

# Name Page
# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
	name = None
	form = NamerForm()
	# Validate Form
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		flash("Form Submitted Successfully!")
		
	return render_template("name.html", 
		name = name,
		form = form)
  
#Doxing
@app.route('/doxing')
def doxing():
	doctor_name = "Ripper"
	plutonium = "Serial"

	serial_corpse  = ["Cobalt 59", "Cobalt 60", "Plutonium", "Uranium-233", "U235", 00]
	return render_template("doxing.html", 
		doctor_name=doctor_name,
		plutonium=plutonium,
		serial_corpse=serial_corpse,)
 
 
@app.route('/power')   
def power():
	return render_template("power.html")    