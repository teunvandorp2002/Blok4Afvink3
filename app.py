from flask import Flask, request, render_template
import app_logic

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    filter_ = str()
    if request.method == "POST":
        filter_ = request.form['search']
    results = app_logic.get_info(filter_)
    return render_template("gene_viewer.html", genes=results,
                           number=len(results), query=filter_)


if __name__ == '__main__':
    app.run()
