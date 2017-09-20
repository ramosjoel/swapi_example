from requests import Response



class Person(object):
    def __init__(self, response):
        assert isinstance(response, Response),\
            '"response" param must be a request.Repsonse object Got{}.' .format(type(response))
        self.response = response
`       self.name = response.json()['name']
        self._birth_year = response.json()['birth_year']
