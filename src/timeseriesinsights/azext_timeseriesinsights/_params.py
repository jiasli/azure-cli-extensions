# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    name_type,
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azext_timeseriesinsights.action import TimeSeriesIdPropertyAction


def load_arguments(self, _):

    with self.argument_context('timeseriesinsights operation list') as c:
        pass

    with self.argument_context('timeseriesinsights') as c:
        c.argument('resource_group', resource_group_name_type)

# region environment
    with self.argument_context('timeseriesinsights environment') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', arg_type=name_type, id_part=None, help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('sku_name', arg_type=get_enum_type(['S1', 'S2', 'P1', 'L1']), id_part=None, help='The name of this SKU.')
        c.argument('sku_capacity', id_part=None, help='The capacity of the sku. For standard environments, this value can be changed to support scale out of environments after they have been created.')

    with self.argument_context('timeseriesinsights environment standard create') as c:
        c.argument('storage_limit_exceeded_behavior', arg_type=get_enum_type(['PurgeOldData', 'PauseIngress']))
        c.argument('partition_key', id_part=None, help='The list of event properties which will be used to partition data in the environment.')

    with self.argument_context('timeseriesinsights environment standard update') as c:
        c.argument('data_retention_time', id_part=None, help='ISO8601 timespan specifying the minimum number of days the environment\'s events will be available for query.')
        c.argument('storage_limit_exceeded_behavior', arg_type=get_enum_type(['PurgeOldData', 'PauseIngress']), id_part=None, help='The behavior the Time Series Insights service should take when the environment\'s capacity has been exceeded. If "PauseIngress" is specified, new events will not be read from the event source. If "PurgeOldData" is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData.')
        c.argument('partition_key_properties', id_part=None, help='The list of event properties which will be used to partition data in the environment.')

    with self.argument_context('timeseriesinsights environment longterm create') as c:
        c.argument('time_series_id_properties', help='The list of event properties which will be used to define the environment\'s time series id.')
        c.argument('storage_account_name', help='The name of the storage account that will hold the environment\'s long term data.')
        c.argument('storage_management_key', id_part=None, help='The value of the management key that grants the Time Series Insights service write access to the storage account. This property is not shown in environment responses.')

    with self.argument_context('timeseriesinsights environment longterm update') as c:
        c.argument('data_retention_time', id_part=None, help='ISO8601 timespan specifying the minimum number of days the environment\'s events will be available for query.')
        c.argument('storage_limit_exceeded_behavior', arg_type=get_enum_type(['PurgeOldData', 'PauseIngress']), id_part=None, help='The behavior the Time Series Insights service should take when the environment\'s capacity has been exceeded. If "PauseIngress" is specified, new events will not be read from the event source. If "PurgeOldData" is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData.')
        c.argument('partition_key_properties', id_part=None, help='The list of event properties which will be used to partition data in the environment.')

    # endregion

    # region event-source
    with self.argument_context('timeseriesinsights event-source') as c:
        c.argument('environment_name', help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('event_source_name', arg_type=name_type, help='The name of the Time Series Insights event source associated with the specified environment.')

    with self.argument_context('timeseriesinsights event-source create') as c:
        pass

    with self.argument_context('timeseriesinsights event-source update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('environment_name', id_part=None, help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
    # endregion

    # region reference-data-set
    with self.argument_context('timeseriesinsights reference-data-set create') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('environment_name', id_part=None, help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('name', id_part=None, help='The name of the Time Series Insights reference data set associated with the specified environment.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('key_properties', id_part=None, help='The list of key properties for the reference data set.', action=TimeSeriesIdPropertyAction, nargs='+')
        c.argument('data_string_comparison_behavior', arg_type=get_enum_type(['Ordinal', 'OrdinalIgnoreCase']), id_part=None, help='The reference data set key comparison behavior can be set using this property. By default, the value is \'Ordinal\' - which means case sensitive key comparison will be performed while joining reference data with events or while adding new reference data. When \'OrdinalIgnoreCase\' is set, case insensitive comparison will be used.')

    with self.argument_context('timeseriesinsights reference-data-set update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('environment_name', id_part=None, help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('name', id_part=None, help='The name of the Time Series Insights reference data set associated with the specified environment.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('key_properties', id_part=None, help='The list of key properties for the reference data set.', action=TimeSeriesIdPropertyAction, nargs='+')
        c.argument('data_string_comparison_behavior', arg_type=get_enum_type(['Ordinal', 'OrdinalIgnoreCase']), id_part=None, help='The reference data set key comparison behavior can be set using this property. By default, the value is \'Ordinal\' - which means case sensitive key comparison will be performed while joining reference data with events or while adding new reference data. When \'OrdinalIgnoreCase\' is set, case insensitive comparison will be used.')

    with self.argument_context('timeseriesinsights reference-data-set delete') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('environment_name', id_part=None, help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('name', id_part=None, help='The name of the Time Series Insights reference data set associated with the specified environment.')

    with self.argument_context('timeseriesinsights reference-data-set show') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('environment_name', id_part=None, help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('name', id_part=None, help='The name of the Time Series Insights reference data set associated with the specified environment.')

    with self.argument_context('timeseriesinsights reference-data-set list') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('environment_name', id_part=None, help='The name of the Time Series Insights environment associated with the specified resource group.')
    # endregion

    # region access-policy
    with self.argument_context('timeseriesinsights access-policy') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('environment_name', id_part=None, help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('name', arg_type=name_type, id_part=None, help='The name of the Time Series Insights access policy associated with the specified environment.')
        c.argument('principal_object_id', help='The objectId of the principal in Azure Active Directory.')
        c.argument('description', help='An description of the access policy.')
        c.argument('roles', help='The list of roles the principal is assigned on the environment.', nargs='+')

    with self.argument_context('timeseriesinsights access-policy create') as c:
        pass

    with self.argument_context('timeseriesinsights access-policy update') as c:
        pass

    with self.argument_context('timeseriesinsights access-policy delete') as c:
        pass

    with self.argument_context('timeseriesinsights access-policy show') as c:
        pass

    # endregion
