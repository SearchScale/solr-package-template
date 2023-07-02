import sys
import cookiecutter.prompt
import os
import json

'''
This pre_gen is to avoid to input tests variables if you don't want to create it
'''

vars = {}

if "{{ cookiecutter.RequestHandler }}" == "True":
    vars["REQUESTHANDLER_CLASS_NAME"] = cookiecutter.prompt.read_user_variable("RequestHandler class name", "MyRequestHandler")
    vars["REQUESTHANDLER_PATH"] = cookiecutter.prompt.read_user_variable("RequestHandler path", "/myrh")
if "{{ cookiecutter.QueryParser }}" == "True":
    vars["QUERYPARSER_CLASS_NAME"] = cookiecutter.prompt.read_user_variable("QueryParser class name", "MyQueryParser")
if "{{ cookiecutter.PostFilter }}" == "True":
    vars["POSTFILTER_CLASS_NAME"] = cookiecutter.prompt.read_user_variable("PostFilter class name", "MyPostFilter")

with open("vars.json", "w") as outfile:
    json.dump(vars, outfile)

sys.exit(0)