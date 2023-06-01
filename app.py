from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': "Data Analyst",
  'location': "Hyderabad,India",
  'salary': "Rs.10,00,000"
}, {
  'id': 2,
  'title': "Data Scientist",
  'location': "SanFransisco, USA",
  'salary': "Rs.1,00,00,000"
}, {
  'id': 3,
  'title': "Data Engineer",
  'location': "Bengaluru, India",
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Gkdss')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
