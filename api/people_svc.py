
from requests import Session, Request


class PeopleSvc(object):
    """
    Class that wraps the SWAPI /person endpoint
    """
    def __init__(self):
        self.history = []
        self.base_url = 'https://swapi.co/api/people'
        self.session = Session()

    def get_person(self, person_id):
        """
        Returns Star Wars person from /people endpoint based
        on ID passed in
        :param person_id: int Person ID
        :return: requests.Response object containing JSON for Person
        """
        req = Request()
        req.method = 'GET'
        req.url = '{base_url}/{person_id}'.format(base_url=self.base_url, person_id=person_id)
        prepped = self.session.prepare_request(req)
        response = self.session.send(prepped)
        self.history.append(response)
        return response
