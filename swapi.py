
from api import PeopleSvc

svc = PeopleSvc()
response = svc.get_person(1)

print response.ok
print response.status_code
print response.json()
