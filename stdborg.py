# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging

from uniborg import Uniborg

import os
api_key_id = os.environ['API_ID']
api_key_hash = os.environ['API_HASH']
SESSION = os.environ['STRING_SESSION']

logging.basicConfig(level=logging.INFO)

borg = Uniborg(
    StringSession(SESSION),
    plugin_path="stdplugins",
    connection_retries=None,
    api_id=api_key_id,
    api_hash=api_key_hash
)

borg.run_until_disconnected()
