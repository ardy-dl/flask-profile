from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/areaOfcirle', methods=['GET', 'POST'])
def circle():
    if request.method == 'POST':
        radius = float(request.form.get('radius'))
        answer = 3.14159265359 * (radius ** 2)
        calc = "{:.2f}".format(answer)
        return render_template('circle.html', calc=calc)
    else:
        return render_template('circle.html', calc=None)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def triangle():
    if request.method == 'POST':
        base = float(request.form.get('base'))
        height = float(request.form.get('height'))
        area = 0.5 * base * height
        return render_template('triangle.html', answer=area)
    else:
        return render_template('triangle.html', answer=None)    

if __name__ == "__main__":
    app.run(debug=True)
