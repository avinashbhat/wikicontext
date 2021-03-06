import os
from flask import Flask, render_template, request, redirect, url_for
import requests
from main import basicSearch, advancedSearch

application= Flask(__name__)

article_name_input = "default"
article_name="default"
article_body = "default"

@application.route('/', methods=['GET', 'POST'])
def front():
	if request.method == 'POST':
		return redirect(url_for('search'))
	return render_template('front.html')

@application.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == 'POST':
		article_name_input =  request.form['article_name_input']
		return redirect(url_for('query',  article_name_input= article_name_input))
	return render_template('search.html')

@application.route('/basic/<article_name_input>')
def basic(article_name_input):
	article_name, article_body = basicSearch(article_name_input)
	return render_template('basic.html', article_name=article_name, article_body=article_body)

@application.route('/query/<article_name_input>', methods=['GET', 'POST'])
def query(article_name_input):
	if request.method == 'POST':
		if request.form['submit'] == 'Recommended Search':
			return redirect(url_for('basic', article_name_input=article_name_input))
		elif request.form['submit'] == 'Lenient Search':
			return redirect(url_for('advanced', article_name_input=article_name_input))
		else:
			render_template('search.html')
	return render_template('query.html', article_name=article_name_input)


@application.route('/advanced/<article_name_input>')
def advanced(article_name_input):
	article_name, article_body = advancedSearch(article_name_input)
	return render_template('advanced.html', article_name=article_name_input, article_body=article_body)
