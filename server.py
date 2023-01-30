from flask import Flask, request, render_template


app = Flask(__name__)


# messages = [{'yesChoice': 'I am glad this coin was helpful'},
#             {'noChoice': 'Let the coin guide you, believe in its power'}
#             ]

@app.route("/")
def main():
  user_name = request.args.get("userName", "unknown")
  return render_template('index.html', user=user_name) 

@app.route('/form/', methods=('GET', 'POST'))
def form():
  if request.method == 'POST':
    try:
      choice = request.form['choice']
      message = "thank you for the feedback"
    except KeyError:
      message = "why did you submit without picking a choice??!?"
    
    return render_template('index.html', choice = message) 
          
  return render_template('form.html')