import argparse
import json
from knack.util import CLIError


# pylint: disable=protected-access, too-few-public-methods
class TimeSeriesIdPropertyAction(argparse._AppendAction):

    def __call__(self, parser, namespace, values, option_string=None):
        obj = {}
        for property_str in values:
            try:
                key, value = property_str.split('=', 1)
                obj[key] = value
            except ValueError:
                raise CLIError('Usage error: {} name=NAME type=TYPE'.format(option_string))

        super(TimeSeriesIdPropertyAction, self).__call__(parser, namespace, obj, option_string)
