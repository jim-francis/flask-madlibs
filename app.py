from flask import Flask, request, render_template
from stories import Story, story

app = Flask(__name__)

@app.route("/")
def home_page():
    story_prompts = story.prompts;
    return render_template("home.html", story_prompts=story_prompts)

@app.route("/story")
def show_story():
    story_text = story.generate(request.args)
    return render_template("story.html", story_text=story_text)