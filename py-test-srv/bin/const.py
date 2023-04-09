URL = 'http://py-srv-post:5000'

GET_ALL_URL = URL + '/dog'

GET_ALL = {
  "results": [
    {
      "breed": "Snozier",
      "color": "black",
      "id": 1
    },
    {
      "breed": "Shepard",
      "color": "brown",
      "id": 2
    },
    {
      "breed": "Mastif",
      "color": "spotted",
      "id": 3
    },
    {
      "breed": "Am Bulldog",
      "color": "white",
      "id": 4
    }
  ]
}

UNSUPPORTED = {
  "results": "This action is unsupported"
}

DELETE_URL = URL + '/dog/1'

INSERT_URL = URL + '/dog/pink/lemonade'

SMOKE_URL = URL + '/'

SMOKE = {"hello": "world"}

UPDATE_URL = URL + '/dog/2/clear/crystal'
