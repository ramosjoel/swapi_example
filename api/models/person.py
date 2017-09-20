from requests import Response

class Person(object):
    def __init__(self, response):
        assert isinstance(response, Response), \
            '"response" param must be a request.Response. Got {}.'.format(type(response))
    #    self.response = response
    #    self._birth_year = None #response.json()['birth_year']
    #    self._get_attributes()

    #def _get_attributes(self):
    #    self._birth_year = self.response.json()['birth_year']

    #@property
    #def birth_year(self):
    #    return self._birth_year

        self.response = response
        self.name = response.json()['name']
        self._birth_year = response.json()['birth_year']
