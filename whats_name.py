from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def name():
    print "Got the name!"
    name = request.form['name']
    return redirect('/')

app.run(debug=True)
