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
        from .vendored_sdks.timeseriesinsights.models import SkuName
        c.argument('resource_group', resource_group_name_type)
        c.argument('environment_name', arg_type=name_type, id_part=None, help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('sku_name', arg_group="SKU", arg_type=get_enum_type(SkuName), help='The sku determines the type of environment, either standard (S1 or S2) or long-term (L1). For standard environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.')
        c.argument('sku_capacity', arg_group="SKU", help='The capacity of the sku. For standard environments, this value can be changed to support scale out of environments after they have been created.')

    with self.argument_context('timeseriesinsights environment standard') as c:
        from .vendored_sdks.timeseriesinsights.models import StorageLimitExceededBehavior
        c.argument('storage_limit_exceeded_behavior', arg_type=get_enum_type(StorageLimitExceededBehavior))
        c.argument('partition_key_properties', nargs='+')

    with self.argument_context('timeseriesinsights environment longterm') as c:
        c.argument('storage_account_name', arg_group="Storage Configuration", help='The name of the storage account that will hold the environment\'s long term data.')
        c.argument('storage_management_key', arg_group="Storage Configuration", help='The value of the management key that grants the Time Series Insights service write access to the storage account. This property is not shown in environment responses.')
        c.argument('time_series_id_properties', nargs='+')
    # endregion

    # region event-source
    with self.argument_context('timeseriesinsights event-source') as c:
        from .vendored_sdks.timeseriesinsights.models import LocalTimestampFormat
        c.argument('environment_name', help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('event_source_name', arg_type=name_type, help='The name of the Time Series Insights event source associated with the specified environment.')

    # timeseriesinsights event-source eventhub update
    # timeseriesinsights event-source iothub update
    with self.argument_context('timeseriesinsights event-source') as c:
        c.argument('local_timestamp_format', arg_group="Local Timestamp", arg_type=get_enum_type(LocalTimestampFormat), help='An enum that represents the format of the local timestamp property that needs to be set.')
        c.argument('time_zone_offset_property_name', arg_group="Local Timestamp", help='The event property that will be contain the offset information to calculate the local timestamp. When the LocalTimestampFormat is Iana, the property name will contain the name of the column which contains IANA Timezone Name (eg: Americas/Los Angeles). When LocalTimestampFormat is Timespan, it contains the name of property which contains values representing the offset (eg: P1D or 1.00:00:00)')
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
        from .vendored_sdks.timeseriesinsights.models import AccessPolicyRole
        c.argument('resource_group', resource_group_name_type)
        c.argument('environment_name', id_part=None, help='The name of the Time Series Insights environment associated with the specified resource group.')
        c.argument('access_policy_name', arg_type=name_type, id_part=None, help='The name of the Time Series Insights access policy associated with the specified environment.')
        c.argument('principal_object_id', help='The objectId of the principal in Azure Active Directory.')
        c.argument('description', help='An description of the access policy.')
        c.argument('roles', arg_type=get_enum_type(AccessPolicyRole), nargs='+')

    # endregion
