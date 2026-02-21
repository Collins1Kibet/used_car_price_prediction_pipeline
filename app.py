from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('auto_price_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        input_data = {
            'symboling': float(request.form['symboling']),
            'wheel-base': float(request.form['wheel-base']),
            'length': float(request.form['length']),
            'width': float(request.form['width']),
            'height': float(request.form['height']),
            'curb-weight': float(request.form['curb-weight']),
            'engine-size': float(request.form['engine-size']),
            'bore': float(request.form['bore']),
            'stroke': float(request.form['stroke']),
            'compression-ratio': float(request.form['compression-ratio']),
            'horse-power': float(request.form['horse-power']),
            'peak-rpm': float(request.form['peak-rpm']),
            'city-mpg': float(request.form['city-mpg']),
            'highway-mpg': float(request.form['highway-mpg']),
            'normalized-losses': float(request.form['normalized-losses']),
            'make': request.form['make'],
            'fuel-type': request.form['fuel-type'],
            'aspiration': request.form['aspiration'],
            'num-of-doors': request.form['num-of-doors'],
            'body-style': request.form['body-style'],
            'drive-wheels': request.form['drive-wheels'],
            'engine-location': request.form['engine-location'],
            'engine-type': request.form['engine-type'],
            'num-of-cylinders': request.form['num-of-cylinders'],
            'fuel-system': request.form['fuel-system']
        }

        df = pd.DataFrame([input_data])
        prediction = model.predict(df)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
