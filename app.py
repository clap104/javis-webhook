#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
	#port = int(os.getenv('PORT', 5000))

    #print("Starting app on port %d" % port)

    app.run(Debug=False, port=8000, host='0.0.0.0')