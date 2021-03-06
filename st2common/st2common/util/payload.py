# Copyright 2019 Extreme Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from jsonpath_rw import parse

from st2common.constants.keyvalue import SYSTEM_SCOPES
from st2common.constants.rules import TRIGGER_PAYLOAD_PREFIX
from st2common.services.keyvalues import KeyValueLookup


class PayloadLookup(object):

    def __init__(self, payload, prefix=TRIGGER_PAYLOAD_PREFIX):
        self.context = {
            prefix: payload
        }

        for system_scope in SYSTEM_SCOPES:
            self.context[system_scope] = KeyValueLookup(scope=system_scope)

    def get_value(self, lookup_key):
        expr = parse(lookup_key)
        matches = [match.value for match in expr.find(self.context)]
        if not matches:
            return None
        return matches
