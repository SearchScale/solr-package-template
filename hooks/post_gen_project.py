import os
import sys
import json

def substitute(filename, vars):
    with open(filename) as file:
        contents = file.read()
        for key in vars:
            contents = contents.replace("$$" + key, vars[key])
    with open(filename, "w") as file:
        file.write(contents)

def handleCommas(filename):
    with open(filename) as file:
        contents = file.read()
        for key in vars:
            for i in range(10):
              sentinel="$$COMMA"+str(i)
              contents = contents.replace(sentinel, ",", contents.count(sentinel)-1)
              contents = contents.replace(sentinel, "")
    with open(filename, "w") as file:
        file.write(contents)


class_names = {"RequestHandler.java": "REQUESTHANDLER_CLASS_NAME",
               "UpdateRequestProcessor.java": "URP_CLASS_NAME"}
vars = json.load(open("vars.json"))

# Substitute all classnames and other inputs inside the file
substitute("src/main/resources/manifest.json", vars)

# Handle commas in manifest.json
handleCommas("src/main/resources/manifest.json")

for file in class_names:
    substitute("src/main/java/" + file, vars)

# Remove all unnecessary files
REMOVE_PATHS = [
    '{% if cookiecutter.RequestHandler != "True" %} src/main/java/RequestHandler.java {% endif %}',
    '{% if cookiecutter.UpdateRequestProcessor != "True" %} src/main/java/UpdateRequestProcessor.java {% endif %}',
]
for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)

# Rename all the java classes to user specified names
for file in class_names:
    if os.path.isfile("src/main/java/" + file):
        suffix=""
        if file == "UpdateRequestProcessor.java": suffix="Factory"
        os.rename("src/main/java/" + file, "src/main/java/" + vars[class_names[file]] + suffix + ".java")

# Remove vars.json
os.unlink("vars.json")