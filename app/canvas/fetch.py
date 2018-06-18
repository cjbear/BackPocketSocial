

import requests
import os

params = {
  'api_key': '{API_KEY}',
}
r = requests.get(
    'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
    params=params)

with open('/tmp/movies.tmp.json', 'w') as f:
  f.write(r.text)

os.rename('/tmp/movies.tmp.json', '/tmp/movies.json')