from flask import Blueprint, render_template

landing = Blueprint('landing', __name__)

@landing.route('/landing')
def landingpage():
	return render_template('landing.html')