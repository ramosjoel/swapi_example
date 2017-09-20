from requests import Request, Session

class PlanetsSvc(object):

    def __init__(self):
        self.base_url = 'https://swapi.co/api/planets'
        self.session = Session()
        self.history = []

    def get_planet(self):
        req = Request()
        req.method = 'GET'
        req.url = '{base_url}/{planet_id}'.format(base_url=self.base_url, planet_id=self.planet_id)
        prepped = self.session.prepare_request(req)
        response = self.session.sent(prepped)
        self.history.append(response)
        return response
