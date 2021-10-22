from flask import request, redirect, render_template, flash, \
url_for, session, Blueprint, config
from imageUpload import app, db
from imageUpload.auth.models import User, RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
	if session.get('username'):
		flash('You are alredy logged in', 'info')
		return redirect(url_for('home.index'))

	form = RegistrationForm()

	if form.validate_on_submit():
		username = request.form.get('username')
		password = request.form.get('password')
		existing_user = User.query.filter_by(username=username).first()
		if existing_user:
			flash(
				'This username alredy exists. Try another one!', 'warning'
			)
			return render_template('register.html', form=form)
		user = User(username, password)
		db.session.add(user)
		db.session.commit()
		flash('You are now registered, please log in!', 'succes')
		return redirect(url_for('auth.login'))
	if form.errors:
		flash(form.errors, 'danger')
	return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		username = request.form.get('username')
		password = request.form.get('password')
		existing_user = User.query.filter_by(username=username).first()

		if not (existing_user and existing_user.check_password(password)):
			flash('Invalid username or password. Please try again.', 'danger')
			return render_template('login.html', form=form)

		session['username'] = username
		flash('You have successfully logged in.', 'success')
		return redirect(url_for('home.index'))

	if form.errors:
		flash(form.errors, 'danger')

	return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
		flash('You have successfully logged out.', 'success')
	return redirect(url_for('home'))