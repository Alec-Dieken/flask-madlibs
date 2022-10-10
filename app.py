from flask import Flask, request, render_template
from stories import *

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('stories-form.html', prompts=story.prompts)

@app.route('/story')
def storypage():
    return render_template('story.html', mystory=story.generate(request.args))