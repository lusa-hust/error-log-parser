__author__ = 'li'

from raven import Client
import raven


def initialize_connection(dsn):

    client = Client(dsn=dsn)
    # adding tag context
    client.tags_context({'version': '1.0'})

    return client


def push_to_sentry(client, errors):
    client.capture(
        'raven.events.Message',
        message='foo',
        extra=errors
    )