# {{cookiecutter.project_name}}
A simple Solr package for a question answering engine

## Installing

* Start Solr (version 8.4 or later) nodes with -Denable.packages=true

    `bin/solr -c -Denable.packages=true`

* Add repository:

    `bin/solr package add-repo chatman-qa "https://raw.githubusercontent.com/chatman/question-answering/master/repo/"`

* See available packages:

    `bin/solr package list-available`

* Install the package

    `bin/solr package install question-answering`

* Create a collection and add a document

    `curl "http://localhost:8983/solr/admin/collections?action=CREATE&name=facts&numShards=1" && curl -XPOST -d '[{"id": 1, "name_t":"Japan", "type_s": "country", "capital_s": "Tokyo"}]' "http://localhost:8983/solr/facts/update?commit=true"`

* Deploy package on the collection

    `bin/solr package deploy question-answering -y -collections facts -p RH-HANDLER-PATH=/qa`

* Use the plugin

    `curl "http://localhost:8983/solr/facts/qa?q=what%20is%20the%20capital%20of%20japan"`

