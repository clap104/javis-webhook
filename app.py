#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()
import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
	port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')