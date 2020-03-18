# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument

from msrest.serialization import attribute_key_case_insensitive_extractor


def list_timeseriesinsights_operation(cmd, client):
    return client.list()


def create_timeseriesinsights_environment_standard(cmd, client,
                                                   resource_group,
                                                   name,
                                                   location,
                                                   sku_name,
                                                   sku_capacity,
                                                   tags=None,
                                                   data_retention_time=None,
                                                   storage_limit_exceeded_behavior=None,
                                                   partition_key_properties=None):
    body = {}
    body['kind'] = 'Standard'
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body.setdefault('sku', {})['name'] = sku_name  # str
    body.setdefault('sku', {})['capacity'] = sku_capacity  # int
    body['data_retention_time'] = data_retention_time  # duration
    body['storage_limit_exceeded_behavior'] = storage_limit_exceeded_behavior  # str
    body['partition_key_properties'] = [{"name": partition_key_properties, "type": "String"}]  # [TimeSeriesIdProperty]
    return client.create_or_update(resource_group_name=resource_group, environment_name=name, parameters=body)


def update_timeseriesinsights_environment_standard(cmd, client,
                                                   resource_group,
                                                   name,
                                                   tags=None,
                                                   sku_name=None,
                                                   sku_capacity=None,
                                                   data_retention_time=None,
                                                   storage_limit_exceeded_behavior=None,
                                                   partition_key_properties=None):
    body = {}
    if tags is not None:
        body['tags'] = tags  # dictionary
    if sku_name is not None:
        body.setdefault('sku', {})['name'] = sku_name  # str
    if sku_capacity is not None:
        body.setdefault('sku', {})['capacity'] = sku_capacity  # number
    if data_retention_time is not None:
        body['data_retention_time'] = data_retention_time  # duration
    if storage_limit_exceeded_behavior is not None:
        body['storage_limit_exceeded_behavior'] = storage_limit_exceeded_behavior  # str
    if partition_key_properties is not None:
        body['partition_key_properties'] = [{"name": partition_key_properties, "type": "String"}]  # [TimeSeriesIdProperty]

    return client.update(resource_group_name=resource_group, environment_name=name, standard_environment_update_parameters=body)


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
    body = {}
    body['kind'] = 'LongTerm'
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body.setdefault('sku', {})['name'] = sku_name  # str
    body.setdefault('sku', {})['capacity'] = sku_capacity  # number
    body['time_series_id_properties'] = [{"name": "deviceId", "type": "String"}, {"name": "deviceId2", "type": "String"}]  # [TimeSeriesIdProperty]
    body['storage_configuration'] = {"account_name": storage_account_name, "management_key": storage_management_key}  # LongTermStorageConfigurationInput
    body['data_retention'] = data_retention

    # Bypass the bug in msrest that it can't extract properties.warmStoreConfiguration.dataRetention
    # with rest_key_case_insensitive_extractor
    # https://github.com/Azure/msrest-for-python/issues/194
    from azext_timeseriesinsights.vendored_sdks.timeseriesinsights.models import LongTermEnvironmentCreateOrUpdateParameters
    parameters = LongTermEnvironmentCreateOrUpdateParameters.from_dict(body, key_extractors=[attribute_key_case_insensitive_extractor])
    return client.create_or_update(resource_group_name=resource_group, environment_name=name, parameters=parameters)


def update_timeseriesinsights_environment_longterm(cmd, client,
                                                   resource_group,
                                                   name,
                                                   location=None,
                                                   tags=None,
                                                   sku_name=None,
                                                   sku_capacity=None,
                                                   data_retention_time=None,
                                                   storage_limit_exceeded_behavior=None,
                                                   partition_key_properties=None):
    body = {}
    if location is not None:
        body['location'] = location  # str
    if tags is not None:
        body['tags'] = tags  # dictionary
    if sku_name is not None:
        body.setdefault('sku', {})['name'] = sku_name  # str
    if sku_capacity is not None:
        body.setdefault('sku', {})['capacity'] = sku_capacity  # number
    if data_retention_time is not None:
        body['data_retention_time'] = data_retention_time  # unknown-primary[timeSpan]
    if storage_limit_exceeded_behavior is not None:
        body['storage_limit_exceeded_behavior'] = storage_limit_exceeded_behavior  # str
    if partition_key_properties is not None:
        body['partition_key_properties'] = partition_key_properties
    return client.create_or_update(resource_group_name=resource_group, environment_name=name, parameters=body)


def delete_timeseriesinsights_environment(cmd, client,
                                          resource_group,
                                          name):
    return client.delete(resource_group_name=resource_group, environment_name=name)


def get_timeseriesinsights_environment(cmd, client,
                                       resource_group,
                                       name):
    return client.get(resource_group_name=resource_group, environment_name=name)


def list_timeseriesinsights_environment(cmd, client,
                                        resource_group=None):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


def create_timeseriesinsights_event_source(cmd, client,
                                           resource_group,
                                           environment_name,
                                           name,
                                           location,
                                           tags=None):
    return client.create_or_update(resource_group_name=resource_group, environment_name=environment_name, event_source_name=name, location=location, tags=tags)


def update_timeseriesinsights_event_source(cmd, client,
                                           resource_group,
                                           environment_name,
                                           name,
                                           location=None,
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
                                            resource_group,
                                            environment_name,
                                            name,
                                            description=None,
                                            roles=None):
    return client.create_or_update(resource_group_name=resource_group, environment_name=environment_name, access_policy_name=name, description=description, roles=roles)


def update_timeseriesinsights_access_policy(cmd, client,
                                            resource_group,
                                            environment_name,
                                            name,
                                            description=None,
                                            roles=None):
    return client.create_or_update(resource_group_name=resource_group, environment_name=environment_name, access_policy_name=name, description=description, roles=roles)


def delete_timeseriesinsights_access_policy(cmd, client,
                                            resource_group,
                                            environment_name,
                                            name):
    return client.delete(resource_group_name=resource_group, environment_name=environment_name, access_policy_name=name)


def get_timeseriesinsights_access_policy(cmd, client,
                                         resource_group,
                                         environment_name,
                                         name):
    return client.get(resource_group_name=resource_group, environment_name=environment_name, access_policy_name=name)


def list_timeseriesinsights_access_policy(cmd, client,
                                          resource_group,
                                          environment_name):
    return client.list_by_environment(resource_group_name=resource_group, environment_name=environment_name)
