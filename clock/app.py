from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    inp_hour = int(request.form['hour'])
    inp_min = int(request.form['minute'])

    if inp_hour == 12:
        s = inp_min * 6 - 0 * 30
        output = "{} degrees".format(s)
    else:
        s = inp_min * 6 - (inp_hour) * 30
        output = "{} degrees".format(s)
    
    # print("input hour:", inp_hour)
    # print("input minute:", inp_min)
    # print("output:", output)
    
    return render_template('index.html', prediction_text=output)


if __name__ == '__main__':
    app.run(debug=True)


