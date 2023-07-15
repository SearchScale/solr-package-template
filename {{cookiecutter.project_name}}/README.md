# {{cookiecutter.project_name}}
A simple Solr package for a question answering engine

## Building the package

* Install OpenSSL for signing your packages.

    sudo apt update && sudo apt install -y openssl

* Create a private key, used for signing your packages, in a secure location. Ignore if you already have have a private key.

    openssl genrsa -out ~/.solr-private-key.pem 512

    export SOLR_PACKAGE_SIGNING_PRIVATE_KEY_PATH=~/.solr-private-key.pem

* Build and release

    mvn package

* Check in the repo/ folder to see if a jar file is generated, and the corresponding artifact is added to the repo/repository.json

* For testing the package locally, start a webserver

    python3 -m http.server

## Installing

* Start Solr (version {{cookiecutter.version_constraint}}) nodes with -Denable.packages=true

    `bin/solr -c -Denable.packages=true`

* Add the repository:

    # If hosted off Github:
    `bin/solr package add-repo {{cookiecutter.project_name}}-repo "https://raw.githubusercontent.com/myusername/{{cookiecutter.project_name}}/master/repo/"`

    # If hosted locally:
    `bin/solr package add-repo {{cookiecutter.project_name}}-repo "http://localhost:8000/repo/"`

* See available packages:

    `bin/solr package list-available`

* Install the package

    `bin/solr package install {{cookiecutter.project_name}}`

* Create a collection

    `curl "http://localhost:8983/solr/admin/collections?action=CREATE&name=facts&numShards=1"`

* Deploy package on the collection

    `bin/solr package deploy {{cookiecutter.project_name}} -y -collections facts -p RH-HANDLER-PATH=/myrh -p URP-NAME=mytimestamp-processor`

* Index a document

    `curl -XPOST -d '[{"id": 1, "name_t":"Russia", "type_s": "country", "capital_s": "Moscow"}]' "http://localhost:8983/solr/facts/update?rocessor=mytimestamp-processor&commit=true"`

* Test the RequestHandler

    `curl "http://localhost:8983/solr/facts/myrh?q=what%20is%20the%20capital%20of%20russia"`

* Test the UpdateProcessor

    `curl "http://localhost:8983/solr/facts/select?q=*:*"`

    # There's a `timestamp_dt` field in the indexed document, added by the UpdateProcessor