from http.server import BaseHTTPRequestHandler
from flask import Flask, render_template
from random import randint


class Handler(BaseHTTPRequestHandler):

    def do_get(self):
        self.send_response(200)
        self.send_header('content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('hello world!'.encode('utf-8'))

        app = Flask(__name__)
        canning = [
            '南大米', '北大米', '顺溜', '牛蛙', '饺子', '陈香贵', '干锅', '麻辣烫', '肯德基', '老乡鸡', '再抽一次',
            '陕老顺', '那个绿色的店'
        ]

        @app.route('/index')
        def index():
            return render_template('index.html', canning=canning)

        @app.route('/chisha')
        def chisha():
            num = randint(0, len(canning) - 1)
            return render_template('index.html', canning=canning, c=canning[num])

        app.run(debug=True)

        return
