import sys
import cookiecutter.prompt
import os
import json


vars = {}

if "{{ cookiecutter.RequestHandler }}" == "True":
    vars["REQUESTHANDLER_CLASS_NAME"] = cookiecutter.prompt.read_user_variable("RequestHandler class name", "MyRequestHandler")
    vars["REQUESTHANDLER_PATH"] = cookiecutter.prompt.read_user_variable("RequestHandler path", "/myrh")
if "{{ cookiecutter.UpdateRequestProcessor }}" == "True":
    vars["URP_CLASS_NAME"] = cookiecutter.prompt.read_user_variable("UpdateRequestProcessor class name", "MyURP")
if "{{ cookiecutter.UpdateRequestProcessor }}" == "True":
    vars["URP_NAME"] = cookiecutter.prompt.read_user_variable("UpdateRequestProcessor simple name:", "my-processor")

with open("vars.json", "w") as outfile:
    json.dump(vars, outfile)

sys.exit(0)