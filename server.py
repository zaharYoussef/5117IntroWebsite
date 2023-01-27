from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def main():
  user_name = request.args.get("userName", "unknown")
  return render_template('index.html', user=user_name) 