from flask import Flask, request, redirect, render_template, render_template_string
app = Flask(__name__)
@app.route('/')
def main():
	return "abc"
