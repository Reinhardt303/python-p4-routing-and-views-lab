#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f"{parameter}")
    return f"{parameter}"

@app.route("/count/<int:parameter>")
def count(parameter):
    #i = 0
    #while i <= parameter:
     #   i += 1
     #   return str(f"{i}") #print(i)
        #
    #for i in range(parameter):
    #    return str(i) #print(i)
    def generate():
        for i in range(parameter):
            yield f"{i}\n"
    
    return Response(generate(), mimetype="text/plain")

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):

    return str(eval(f"{num1}{operation}{num2}")) #may need to use try/except here for invalid operations 

