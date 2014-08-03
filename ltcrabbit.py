__all__ = ["LtcRabbit"]
__version__ = "0.1dev"

import requests

BASE_URL = "https://www.ltcrabbit.com/index.php?page=api"

class LtcRabbit(object):

    appname = "PyLtcRabbit"
    appversion = __version__

    def __init__(self, api_key):
        self.api_key = api_key

    def call(self, action, **kwargs):
        payload = kwargs
        payload['api_key'] = self.api_key
        payload['appname'] = self.appname
        payload['appversion'] = self.appversion
        payload['action'] = action

        r = requests.get(BASE_URL, params=payload)
        pprint.pprint(r.url)

        return r.json()

    def get_worker_list(self):

        return self.call('getappdata')['getappdata']['worker']

    def add_worker(self, workerlist=[]):
        """Add Workers

        worker = {
            'name': 'workername',
            'pass': 'workerpassword',
            'algo': 'scrypt'
        }
        add_worker([worker])
        """

        wl = []
        for worker in workerlist:
            wl.append(".".join([worker['name'], worker['pass'], worker['algo']]))

        w = ','.join(wl)

        return self.call('setappdata', do='add_worker', workerlist=w)

    def delete_worker(self, workerlist=[]):
        """Delete worker

        workerlist - List of Workernames (default: [])

        delete_worker(workerlist=['workername'])
        """

        return self.call('setappdata', do='delete_worker', workerlist=",".join(workerlist))
