# python-web-flaskl-api-csv-to-elasticsearch-client-sqlalchemy-raw-sql-simple

## Description
Reads a csv file into a single node for data in `dog` document.

Uses sqlalchemy to connect and executes raw sql.

Remotely tested with *testify*.

## Tech stack
- python
    - flask
    - sqlalchemy
    - elasticsearch
    - elasticsearch_dbapi
    - testify
    - requests
- elasticsearch
- kibana

## Docker stack
- python
- elasticsearch
- kibana

## To run
`sudo ./install.sh -u`
- Get all dogs: http://localhost/dog
  - Schema id, breed, and color
- CRUD opperations
  - Read: http://localhost/dog/<id>
  - Unsupported
    - Create: curl -i -X PUT localhost/dog/<id>
    - Update: curl -i -X POST localhost/dog/<id>/<breed>/<color>
    - Delete: curl -i -X DELETE localhost/dog/<id>

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
