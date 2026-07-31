from flask import Flask, render_template

app = Flask(
    __name__,
   template_folder = "templates",
   static_folder= "static"
    )

profile ={
        "name": "Asghar Rezaie",
        "description": "Junior Python developer and VoIP specialist"
}

@app.get('/')
def index():

    return render_template("home.html", profile=profile)

skill_list = [
    "Python",
    "Flask",
    "Linux",
    "VoIP",
    "Git"
]

@app.get('/skills')
def skills():

    return render_template("skills.html", skills=skill_list)

project_list = [
    {
        "title": "kivy_image_gallery",
        "description": "simple image gallery by kivy",
        "github": "https://github.com/A-Rezaie/masterclass-py/blob/main/kivy_image_gallery/main.py",
        "image": "kivy-gallery.png"
    },

       {
        "title": "gui_simple_calculator",
        "description": "simple calculator by tkinter",
        "github": "https://github.com/A-Rezaie/masterclass-py/blob/main/gui_simple_calculator/Gui_Simple_Calculator.py",
        "image": "gui-calculator.png"
    },

       {
        "title": "pyside_countdown_timer",
        "description": "simple countdown_timer by pyside",
        "github": "https://github.com/A-Rezaie/masterclass-py/blob/main/pyside_countdown_timer/Countdown_Timer.py",
        "image": "countdown-timer.png"
    }
]

@app.get('/projects')
def projects():

    return render_template("projects.html", projects=project_list)


