#!/usr/bin/env python3

import cognitive_face as CF

SUBSCRIPTION_KEY_FILENAME="subscription_key.txt"
ENDPOINT_FILENAME="endpoint.txt"

class SubscriptionKey(object):
    """Subscription Key."""

    @classmethod
    def get(cls):
        """Get the subscription key."""
        if not hasattr(cls, 'key'):
            cls.key = ''
        if not cls.key:
            if os.path.isfile(SUBSCRIPTION_KEY_FILENAME):
                with file(SUBSCRIPTION_KEY_FILENAME) as fin:
                    cls.key = fin.read().strip()
            else:
                cls.key = ''

        CF.Key.set(KEY)
        return cls.key

    @classmethod
    def set(cls, key):
        """Set the subscription key."""
        cls.key = key
        with file(SUBSCRIPTION_KEY_FILENAME, 'w') as fout:
            print >>fout, key
        CF.Key.set(cls.key)

    @classmethod
    def delete(cls):
        """Delete the subscription key."""
        cls.key = ''
        if os.path.isfile(SUBSCRIPTION_KEY_FILENAME):
            os.remove(SUBSCRIPTION_KEY_FILENAME)
        CF.Key.set(cls.key)


class Endpoint(object):
    """Endpoint."""

    @classmethod
    def get(cls):
        """Get the endpoint."""
        if not hasattr(cls, 'endpoint'):
            cls.endpoint = ''
        if not cls.endpoint:
            if os.path.isfile(ENDPOINT_FILENAME):
                with file(ENDPOINT_FILENAME) as fin:
                    cls.endpoint = fin.read().strip()
            else:
                cls.endpoint = CF.BaseUrl.get()
        CF.BaseUrl.set(cls.endpoint)
        return cls.endpoint

    @classmethod
    def set(cls, endpoint):
        """Set the endpoint."""
        cls.endpoint = endpoint
        with file(ENDPOINT_FILENAME, 'w') as fout:
            print >>fout, endpoint
        CF.BaseUrl.set(cls.endpoint)

    @classmethod
    def delete(cls):
        """Delete the endpoint."""
        cls.endpoint = ''
        if os.path.isfile(ENDPOINT_FILENAME):
            os.remove(ENDPOINT_FILENAME)
        CF.BaseUrl.set(CF.util.DEFAULT_BASE_URL)


