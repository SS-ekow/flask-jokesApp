from flask import Flask, render_template
import pyjokes




app = Flask(__name__)

@app.route('/')
def hello():
    joke = pyjokes.get_joke('en')
    return render_template('index.html', joke=joke)






if __name__ == '__main__':
    app.run(debug=True)
