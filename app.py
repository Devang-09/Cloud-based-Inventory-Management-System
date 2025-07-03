from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure your file is in 'templates' folder

@app.route('/login')
def login():
    return render_template('login.html')  # Redirects to login page

if __name__ == '__main__':
    app.run(debug=True)
