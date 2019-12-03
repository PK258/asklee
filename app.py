from flask import Flask, request, render_template
from functions import fetch_plot_data

app = Flask(__name__)


@app.route('/')
def page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def values():
    try:
        if request.method == 'POST':
            for UserID, FromDate, ToDate in \
                    zip(request.form.getlist('user_id'),
                        request.form.getlist('from_date'),
                        request.form.getlist('to_date')):
                fetch_plot_data()
                return render_template('Asklee_paths.html')
            else:
                return render_template('index.html')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)