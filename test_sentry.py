__author__ = 'li'

import sentry

client = sentry.initialize_connection(
    "http://ea8723b06f824d55b49031a702caa2c6:20fdb8b37c354c05b9c5c6ae1807c4a7@sentry.platform.vn/11"
)

sentry.push_to_sentry(client, "type1", {"IP": "1.1.1.1"})
