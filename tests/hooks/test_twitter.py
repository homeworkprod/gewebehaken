from gewebehaken.hooks.twitter import twitter_followed, twitter_mentioned

from ..base import AbstractHooksTestCase


class TwitterHooksTestCase(AbstractHooksTestCase):

    def test_followed(self):
        @twitter_followed.connect
        def receive_signal(sender, **data):
            self.storeReceivedSignalData(data)

        request_data = {
            'screen_name': 'example',
            'name': 'Example User',
        }

        result = self.post_json('/twitter/followed', data=request_data)

        self.assert204(result)
        self.assertReceivedSignalDataEqual(request_data)

    def test_mentioned(self):
        @twitter_mentioned.connect
        def receive_signal(sender, **data):
            self.storeReceivedSignalData(data)

        request_data = {
            'screen_name': 'example',
            'name': 'Example User',
            'url': 'http://twitter.com/example',
        }

        result = self.post_json('/twitter/mentioned', data=request_data)

        self.assert204(result)
        self.assertReceivedSignalDataEqual(request_data)
