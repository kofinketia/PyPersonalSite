from flask import Flask, render_template, request

app = Flask(__name__)

#function to read in details for page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

@app.route("/")
def homePage():
    name = "Kofi Nketia Ackaah-Gyasi"
    details = readDetails('static/details.txt')
    return render_template("base.html", name=name, aboutMe=details)

@app.route('/user/<name>')
def greet(name):
    return f'<p>Hello, {name}!</p>'

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)

@app.route('/research', methods=['GET', 'POST'])
def researchDemo():
    name = None
    #if request.method == 'POST':
        #name=request.form['name']
    return render_template('research.html', name=name)

@app.route('/resume', methods=['GET', 'POST'])
def resumeDemo():
    name = None
    #if request.method == 'POST':
        #name=request.form['name']
    return render_template('resume.html', name=name)

@app.route('/projects', methods=['GET', 'POST'])
def projectsDemo():
    name = None
    #if request.method == 'POST':
        #name=request.form['name']
    return render_template('projects.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
