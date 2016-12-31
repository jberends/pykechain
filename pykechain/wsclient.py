import json

import logging

import sys

from datetime import datetime
from ws4py.client.threadedclient import WebSocketClient


class KEchainClient(WebSocketClient):
    def __init__(self, *args, **kwargs):
        super(KEchainClient, self).__init__(*args, **kwargs)

    def send(self, payload, binary=False):
        """
        Send messages as JSON.

        :param dict payload: Dictionary to send
        :param boolean binary: Should be false
        """
        payload = json.dumps(payload)
        logging.info("Sending message: %s" % payload)
        super(KEchainClient, self).send(payload, binary=binary)

    def opened(self):
        """
        Executed when the connection to KE-chain is opened.
        This function registers a KE-node with KE-chain.
        """
        logging.info("Connected with KE-chain")

    def received_message(self, message):
        message = json.loads(message.data)
        logging.info(
            "Received message: on {}\n{}".format(datetime.utcnow(),
                                                 json.dumps(message, sort_keys=True, indent=4, separators=(',', ': '))))
        data = message['data']


def run_client(url):
    client = KEchainClient(url)
    try:
        client.connect()
        client.run_forever()
    except KeyboardInterrupt:
        client.close()


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    run_client('ws://127.0.0.1:8000/kevent')
