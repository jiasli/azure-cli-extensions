# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RoutingRuleListResult(Model):
    """Result of the request to list Routing Rules. It contains a list of Routing
    Rule objects and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: List of Routing Rules within a Front Door.
    :vartype value: list[~azure.mgmt.frontdoor.models.RoutingRule]
    :param next_link: URL to get the next set of RoutingRule objects if there
     are any.
    :type next_link: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[RoutingRule]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RoutingRuleListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = kwargs.get('next_link', None)
