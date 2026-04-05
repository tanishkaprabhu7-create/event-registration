from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

FIREBASE_URL = "https://eventregistration-2542b-default-rtdb.asia-southeast1.firebasedatabase.app/registrations.json"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    college = request.form['college']
    college_id = request.form['college_id']
    semester = request.form['semester']
    event = request.form['event']

    if not name or not college or not college_id or not semester or not event:
        return "❌ Please fill all fields"

    data = {
        "name": name,
        "college": college,
        "college_id": college_id,
        "semester": semester,
        "event": event
    }

    response = requests.post(FIREBASE_URL, json=data)

    if response.status_code == 200:
        return redirect('/success')
    else:
        return f"❌ Error: {response.text}"


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/view')
def view():
    response = requests.get(FIREBASE_URL)
    data = response.json()

    return render_template('view.html', data=data)


if __name__ == '__main__':
    import os

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))