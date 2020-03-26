# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument


def list_timeseriesinsights_operation(cmd, client):
    return client.list()


def create_timeseriesinsights_environment_standard(cmd, client,
                                                   resource_group, name, location,
                                                   sku_name, sku_capacity,
                                                   tags=None,
                                                   data_retention_time=None,
                                                   storage_limit_exceeded_behavior=None,
                                                   partition_key_properties=None):
    from .vendored_sdks.timeseriesinsights.models import StandardEnvironmentCreateOrUpdateParameters, Sku, TimeSeriesIdProperty
    parameters = StandardEnvironmentCreateOrUpdateParameters(
        location=location,
        tags=tags,
        sku=Sku(name=sku_name, capacity=sku_capacity),
        data_retention_time=data_retention_time,
        storage_limit_exceeded_behavior=storage_limit_exceeded_behavior,
        partition_key_properties=[TimeSeriesIdProperty(name=partition_key_properties, type="String")]
    )
    return client.create_or_update(resource_group_name=resource_group, environment_name=name, parameters=parameters)


def update_timeseriesinsights_environment_standard(instance, cmd,
                                                   tags=None,
                                                   sku_name=None,
                                                   sku_capacity=None,
                                                   data_retention_time=None,
                                                   storage_limit_exceeded_behavior=None,
                                                   partition_key_properties=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
        c.set_param('sku.name', sku_name)
        c.set_param('sku.capacity', sku_capacity)
        c.set_param('data_retention_time', data_retention_time)
        c.set_param('storage_limit_exceeded_behavior', storage_limit_exceeded_behavior)
        c.set_param('partition_key_properties', [{"name": partition_key_properties, "type": "String"}])

        # Need to clear provisioning_state because StandardEnvironmentResource.provisioning_state is not allowed by
        # StandardEnvironmentCreateOrUpdateParameters
        c.set_param('provisioning_state', '')

    return instance


def create_timeseriesinsights_environment_longterm(cmd, client,
                                                   resource_group,
                                                   name,
                                                   location,
                                                   sku_name,
                                                   sku_capacity,
                                                   tags=None,
                                                   time_series_id_properties=None,
                                                   storage_account_name=None,
                                                   storage_management_key=None,
                                                   data_retention=None):
    from .vendored_sdks.timeseriesinsights.models import LongTermEnvironmentCreateOrUpdateParameters, Sku, \
        TimeSeriesIdProperty, LongTermStorageConfigurationInput
    parameters = LongTermEnvironmentCreateOrUpdateParameters(
        location=location,
        tags=tags,
        sku=Sku(name=sku_name, capacity=sku_capacity),
        time_series_id_properties=[TimeSeriesIdProperty(name=time_series_id_properties, type="String")],
        storage_configuration=LongTermStorageConfigurationInput(account_name=storage_account_name, management_key=storage_management_key),
        data_retention=data_retention)
    return client.create_or_update(resource_group_name=resource_group, environment_name=name, parameters=parameters)


def update_timeseriesinsights_environment_longterm(cmd, client,
                                                   resource_group, name,
                                                   tags=None,
                                                   storage_management_key=None,
                                                   data_retention=None):
    from .vendored_sdks.timeseriesinsights.models import LongTermEnvironmentUpdateParameters, \
        LongTermStorageConfigurationMutableProperties
    parameters = LongTermEnvironmentUpdateParameters(
        tags=tags,
        storage_configuration=LongTermStorageConfigurationMutableProperties(management_key=storage_management_key),
        data_retention=data_retention)
    return client.update(resource_group_name=resource_group, environment_name=name, parameters=parameters)


def list_timeseriesinsights_environment(cmd, client,
                                        resource_group=None):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


def create_timeseriesinsights_event_source_eventhub(cmd, client,
                                                    resource_group, environment_name, event_source_name, location,
                                                    timestamp_property_name, event_source_resource_id,
                                                    service_bus_namespace, event_hub_name,
                                                    consumer_group_name, key_name, shared_access_key, tags=None):
    # https://docs.microsoft.com/en-us/rest/api/time-series-insights/management/eventsources/createorupdate
    from azext_timeseriesinsights.vendored_sdks.timeseriesinsights.models import EventHubEventSourceCreateOrUpdateParameters
    parameters = EventHubEventSourceCreateOrUpdateParameters(
        location=location,
        timestamp_property_name=timestamp_property_name,
        event_source_resource_id=event_source_resource_id,
        service_bus_namespace=service_bus_namespace,
        event_hub_name=event_hub_name,
        consumer_group_name=consumer_group_name,
        key_name=key_name,
        shared_access_key=shared_access_key,
        tags=tags
    )
    return client.create_or_update(resource_group_name=resource_group, environment_name=environment_name, event_source_name=event_source_name, parameters=parameters)


def update_timeseriesinsights_event_source_eventhub(cmd, client, resource_group, environment_name, event_source_name,
                                                    tags=None, timestamp_property_name=None,
                                                    local_timestamp=None, shared_access_key=None):

    from .vendored_sdks.timeseriesinsights.models import EventHubEventSourceUpdateParameters
    parameters = EventHubEventSourceUpdateParameters(tags=tags,
                                                     timestamp_property_name=timestamp_property_name,
                                                     local_timestamp=local_timestamp,
                                                     shared_access_key=shared_access_key)

    return client.update(resource_group_name=resource_group, environment_name=environment_name, event_source_name=event_source_name,
                         parameters=parameters)


def update_timeseriesinsights_event_source_eventhub_generic(instance, cmd,
                                                            tags=None, timestamp_property_name=None,
                                                            local_timestamp=None, shared_access_key=None):

    # GET-PUT doesn't work because sharedAccessKey is missing from GET output
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
        c.set_param('timestamp_property_name', timestamp_property_name)
        c.set_param('local_timestamp', local_timestamp)
        c.set_param('shared_access_key', shared_access_key)
        # Need to clear provisioning_state because StandardEnvironmentResource.provisioning_state is not allowed by
        # StandardEnvironmentCreateOrUpdateParameters
        c.set_param('provisioning_state', '')
        c.set_param('creation_time', '')
    return instance


def create_timeseriesinsights_event_source_iothub(cmd, client,
                                                  resource_group, environment_name, event_source_name, location,
                                                  timestamp_property_name, event_source_resource_id,
                                                  iot_hub_name,consumer_group_name, key_name, shared_access_key,
                                                  tags=None):
    from .vendored_sdks.timeseriesinsights.models import IoTHubEventSourceCreateOrUpdateParameters
    parameters = IoTHubEventSourceCreateOrUpdateParameters(
        location=location,
        tags=tags,
        timestamp_property_name=timestamp_property_name,
        event_source_resource_id=event_source_resource_id,
        iot_hub_name=iot_hub_name,
        consumer_group_name=consumer_group_name,
        key_name=key_name,
        shared_access_key=shared_access_key)
    return client.create_or_update(
        resource_group_name=resource_group, environment_name=environment_name, event_source_name=event_source_name,
        parameters=parameters)


def update_timeseriesinsights_event_source_iothub(cmd, client,
                                                  resource_group,
                                                  environment_name,
                                                  name,
                                                  location,
                                                  tags=None):
    return client.create_or_update(resource_group_name=resource_group, environment_name=environment_name, event_source_name=name, location=location, tags=tags)



def delete_timeseriesinsights_event_source(cmd, client,
                                           resource_group,
                                           environment_name,
                                           name):
    return client.delete(resource_group_name=resource_group, environment_name=environment_name, event_source_name=name)


def get_timeseriesinsights_event_source(cmd, client,
                                        resource_group,
                                        environment_name,
                                        name):
    return client.get(resource_group_name=resource_group, environment_name=environment_name, event_source_name=name)


def list_timeseriesinsights_event_source(cmd, client,
                                         resource_group,
                                         environment_name):
    return client.list_by_environment(resource_group_name=resource_group, environment_name=environment_name)


def create_timeseriesinsights_reference_data_set(cmd, client,
                                                 resource_group,
                                                 environment_name,
                                                 name,
                                                 location,
                                                 key_properties,
                                                 tags=None,
                                                 data_string_comparison_behavior=None):
    body = {}
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body['key_properties'] = key_properties
    body['data_string_comparison_behavior'] = data_string_comparison_behavior  # str
    return client.create_or_update(resource_group_name=resource_group, environment_name=environment_name, reference_data_set_name=name, parameters=body)


def update_timeseriesinsights_reference_data_set(cmd, client,
                                                 resource_group,
                                                 environment_name,
                                                 name,
                                                 location=None,
                                                 tags=None,
                                                 key_properties=None,
                                                 data_string_comparison_behavior=None):
    body = {}
    if location is not None:
        body['location'] = location  # str
    if tags is not None:
        body['tags'] = tags  # dictionary
    if key_properties is not None:
        body['key_properties'] = key_properties
    if data_string_comparison_behavior is not None:
        body['data_string_comparison_behavior'] = data_string_comparison_behavior  # str
    return client.create_or_update(resource_group_name=resource_group, environment_name=environment_name, reference_data_set_name=name, parameters=body)


def delete_timeseriesinsights_reference_data_set(cmd, client,
                                                 resource_group,
                                                 environment_name,
                                                 name):
    return client.delete(resource_group_name=resource_group, environment_name=environment_name, reference_data_set_name=name)


def get_timeseriesinsights_reference_data_set(cmd, client,
                                              resource_group,
                                              environment_name,
                                              name):
    return client.get(resource_group_name=resource_group, environment_name=environment_name, reference_data_set_name=name)


def list_timeseriesinsights_reference_data_set(cmd, client,
                                               resource_group,
                                               environment_name):
    return client.list_by_environment(resource_group_name=resource_group, environment_name=environment_name)


def create_timeseriesinsights_access_policy(cmd, client,
                                            resource_group, environment_name, access_policy_name,
                                            principal_object_id=None, description=None, roles=None):
    from .vendored_sdks.timeseriesinsights.models import AccessPolicyCreateOrUpdateParameters
    parameters = AccessPolicyCreateOrUpdateParameters(
        principal_object_id=principal_object_id,
        description=description,
        roles=roles)
    return client.create_or_update(resource_group_name=resource_group, environment_name=environment_name, access_policy_name=access_policy_name, parameters=parameters)


def update_timeseriesinsights_access_policy(cmd, client, resource_group, environment_name, access_policy_name,
                                            description=None, roles=None):
    return client.update(resource_group_name=resource_group, environment_name=environment_name, access_policy_name=access_policy_name, description=description, roles=roles)
