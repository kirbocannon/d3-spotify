import os
import app.config as config
from flask import Flask, render_template, \
    send_from_directory


app = Flask(
    __name__,
    static_folder=os.path.join(config.BASEDIR, "static"),
    template_folder=os.path.join(config.BASEDIR, "templates"),
    static_url_path=""
)


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/<path:path>')
def send_data_files(path):
    return send_from_directory('data', path)


@app.route('/network-graph')
def network_graph():
    return render_template('network-graph.html')


if __name__ == '__main__':

    mode = 'development'

    if mode == 'development':
        app.config.from_object(config.Development)
        app.run()
    elif mode == 'production':
        app.config.from_object(config.Production)
        app.run()
