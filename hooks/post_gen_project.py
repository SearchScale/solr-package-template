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

class_names = {"RequestHandler.java": "REQUESTHANDLER_CLASS_NAME",
               "QueryParser.java": "QUERYPARSER_CLASS_NAME",
               "PostFilter.java": "POSTFILTER_CLASS_NAME"}
vars = json.load(open("vars.json"))

# Substitute all classnames and other inputs inside the file
substitute("src/main/resources/manifest.json", vars)
for file in class_names:
    substitute("src/main/java/" + file, vars)

# Remove all unnecessary files
REMOVE_PATHS = [
    '{% if cookiecutter.RequestHandler != "True" %} src/main/java/RequestHandler.java {% endif %}',
    '{% if cookiecutter.PostFilter != "True" %} src/main/java/PostFilter.java {% endif %}',
    '{% if cookiecutter.QueryParser != "True" %} src/main/java/QueryParser.java {% endif %}',
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
        os.rename("src/main/java/" + file, "src/main/java/" + vars[class_names[file]] + ".java")

# Remove vars.json
os.unlink("vars.json")