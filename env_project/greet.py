from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    print("Request method:", request.method)
    if request.method == 'POST':
        name = request.form.get('username')
        return render_template('greet.html', name=name)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
