


from flask import Flask, render_template
import datetime




app = Flask(__name__)

# This function runs for the homepage URL ('/')
@app.route('/')
def home():
    return render_template('welcome_test.html')



@app.route('/about')
def level1():
    return render_template('level1_test.html')



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=8000)










