from flask import Flask, request, render_template
from functions import fetch_plot_data
import plotly

app = Flask(__name__)


@app.route('/')
def page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def values():
    try:
        if request.method == 'POST':
            for FromDate, ToDate in \
                    zip(request.form.getlist('from_date'),
                        request.form.getlist('to_date')):
                fig = fetch_plot_data(FromDate, ToDate)
                plotly.offline.plot(fig, filename='/home/git/asklee/templates/Asklee_paths.html')
            return render_template('Asklee_paths.html')
        else:
            return render_template('Asklee_paths.html')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
