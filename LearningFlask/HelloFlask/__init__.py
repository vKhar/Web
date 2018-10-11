from flask import Flask
app=Flask("__name__", template_folder="HelloFlask/templates")
print("*** {} ***".format(__name__))
import HelloFlask.views

