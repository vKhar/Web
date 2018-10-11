from flask import Flask
app=Flask(__name__) ## all paths will be relative to __name__(HelloFlask)
print("*** {} ***".format(__name__))
import HelloFlask.views

