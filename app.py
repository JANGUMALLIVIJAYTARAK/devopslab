from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "This is Vijay Tarak Jangumalli"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Debug print
        print(f"Name: {name}, Email: {email}, Password: {password}")

        return render_template("Success.html")  # Render success page
    return render_template("Register.html")  # Render registration form

if __name__ == '__main__':
    app.run(debug=True)
