import os
from flask import Flask, request, render_template

app = Flask(__name__)

# Fix the template path using __file__
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')
app.template_folder = template_dir

# Hard-coded planet data
planet_data = {
    "Mercury": "The smallest and fastest planet in the Solar System.",
    "Venus": "The second planet from the Sun and the hottest planet.",
    "Earth": "Our home planet and the only known celestial body to support life.",
    "Mars": "The fourth planet from the Sun and often called the 'Red Planet'.",
    "Jupiter": "The largest planet in the Solar System and known for its great red spot.",
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        planet = request.form.get('planet', '')

        if not planet.strip():
            return '<h2>Please enter a planet name.</h2>'

        # Block only if actual HTML is submitted — not escaped
        if '<' in planet or '>' in planet or 'script' in planet.lower():
            return '<h2>Blocked</h2></p>'

        return render_template('details.html',
                               planet=planet,
                               info=get_planet_info(planet))
    return render_template('index.html')

def get_planet_info(planet):
    return planet_data.get(planet, 'Unknown planet.')

if __name__ == '__main__':
    app.run()
