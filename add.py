from flask import Flask, render_template, request

app = Flask(__name__)

# Python function
def add(a, b):
    return a + b

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the values of 'a' and 'b' from the form
        a = int(request.form['a'])
        b = int(request.form['b'])
        
        # Call the add function
        result = add(a, b)
        
        # Return the result
        return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
