from flask import Flask

# WE will create a flask app here
# we will create the prpocess of conversion and expose the endpoint of every function we have
app = Flask(__name__)
if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)

