


from flask import Flask

app = Flask(__name__)

# This function runs for the homepage URL ('/')
@app.route('/')
def index():
    return '<h1>Welcome to the main page!</h1>'

# This function runs for the '/about' URL
@app.route('/about')
def about_page():
    return '<h2>This is the about page.</h2>'

if __name__ == '__main__':
    app.run(debug=True)




print('this is a test')



