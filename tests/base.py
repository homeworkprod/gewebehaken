import json
from unittest import TestCase

from gewebehaken.app import create_app


class AbstractAppTestCase(TestCase):

    def setUp(self):
        app = create_app()
        self.client = app.test_client()

    def post_json(self, path, data, headers=None):
        """Send a POST request with a JSON body."""
        return self.client.post(path,
                               content_type='application/json',
                               data=json.dumps(data),
                               headers=headers)

    def assert204(self, result):
        self.assertEqual(result.status_code, 204)
        self.assertEqual(result.data, b'')


class AbstractHooksTestCase(AbstractAppTestCase):

    def setUp(self):
        super().setUp()
        self.received_signal_data = {}

    def storeReceivedSignalData(self, data):
        self.received_signal_data.update(data)

    def assertReceivedSignalDataEqual(self, expected):
        self.assertEqual(self.received_signal_data, expected)
