from urllib.parse import urlparse

from flask import Flask, request, render_template, redirect
from sqlite3 import OperationalError
import sqlite3

from utils import to_base62, to_base10

host = 'http://localhost:5000/'


# Assuming urls.db is in your app root folder
def table_check():
	create_table = ("CREATE TABLE WEB_URL("
					"ID INT PRIMARY KEY AUTOINCREMENT,"
					"URL TEXT NOT NULL")
	with sqlite3.connect('urls.db') as conn:
		cursor = conn.cursor()
		try:
			cursor.execute(create_table)
		except OperationalError:
			pass


app = Flask(__name__)


# Home page where user should enter
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		original_url = request.form.get('url')
		if urlparse(original_url).scheme == '':
			original_url = 'http://' + original_url
		with sqlite3.connect('urls.db') as conn:
			cursor = conn.cursor()
			insert_row = "INSERT INTO WEB_URL (URL) VALUES ('%s')".format(original_url)
			result_cursor = cursor.execute(insert_row)
			encoded_string = to_base62(result_cursor.lastrowid)
		return render_template('home.html', short_url=host + encoded_string)
	return render_template('home.html')


@app.route('/<short_url>')
def redirect_short_url(short_url):
	decoded_string = to_base10(short_url)
	redirect_url = 'http://localhost:5000'
	with sqlite3.connect('urls.db') as conn:
		cursor = conn.cursor()
		select_row = f"SELECT URL FROM WEB_URL WHERE ID={decoded_string}"
		result_cursor = cursor.execute(select_row)
		try:
			redirect_url = result_cursor.fetchone()[0]
		except Exception as e:
			print(e)
	return redirect(redirect_url)


if __name__ == '__main__':
	# This code checks whether database table is created or not
	table_check()
	app.run(debug=True)
