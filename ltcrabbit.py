__all__ = ["LtcRabbit"]
__version__ = "0.1.3"

import requests


class LtcRabbit(object):
    """Main class to access LTCRabbit.com API.
    """

    DEFAULT_ENDPOINT = "https://www.ltcrabbit.com/index.php?page=api"

    appname = "PyLtcRabbit"
    appversion = __version__

    def __init__(self, api_key=None):
        if not api_key:
            raise RuntimeError("No API key provided.")

        self.api_key = api_key
        self.url = self.DEFAULT_ENDPOINT

    def __repr__(self):
        return "Connection(%r)" % self.api_key

    def call(self, action, **kwargs):
        payload = kwargs
        payload['api_key'] = self.api_key
        payload['appname'] = self.appname
        payload['appversion'] = self.appversion
        payload['action'] = action

        r = requests.get(self.url, params=payload)

        return r.json()

    def get_appdata(self):

        return self.call('getappdata')['getappdata']

    def add_worker(self, workerlist=None):
        """Add Workers

        worker = {
            'name': 'workername',
            'pass': 'workerpassword',
            'algo': 'scrypt'
        }
        add_worker([worker])
        """
        if not workerlist: workerlist = []

        wl = []
        for worker in workerlist:
            wl.append(".".join([worker['name'], worker['pass'], worker['algo']]))

        w = ','.join(wl)

        return self.call('setappdata', do='add_worker', workerlist=w)

    def delete_worker(self, workerlist=None):
        """Delete worker

        workerlist - List of Workernames (default: [])

        delete_worker(workerlist=['workername'])
        """
        if not workerlist: workerlist = []

        return self.call('setappdata', do='delete_worker', workerlist=",".join(workerlist))
