# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
from azure.cli.core.commands import CliCommandType
from azure.cli.core.commands.transform import gen_dict_to_list_transform


def load_command_table(self, _):

    with self.command_group('timeseriesinsights', is_experimental=True) as g:
        pass

    from ._client_factory import cf_operations
    timeseriesinsights_operations = CliCommandType(
        operations_tmpl='azext_timeseriesinsights.vendored_sdks.timeseriesinsights.operations._operations_operations#OperationsOperations.{}',
        client_factory=cf_operations)
    with self.command_group('timeseriesinsights operation', timeseriesinsights_operations, client_factory=cf_operations) as g:
        g.custom_command('list', 'list_timeseriesinsights_operation')

    # region environment
    from ._client_factory import cf_environments
    timeseriesinsights_environments = CliCommandType(
        operations_tmpl='azext_timeseriesinsights.vendored_sdks.timeseriesinsights.operations._environments_operations#EnvironmentsOperations.{}',
        client_factory=cf_environments)

    with self.command_group('timeseriesinsights environment standard', timeseriesinsights_environments, client_factory=cf_environments) as g:
        g.custom_command('create', 'create_timeseriesinsights_environment_standard',
                         doc_string_source="azext_timeseriesinsights.vendored_sdks.timeseriesinsights.models#StandardEnvironmentCreateOrUpdateParameters")
        g.custom_command('update', 'update_timeseriesinsights_environment_standard')

    with self.command_group('timeseriesinsights environment longterm', timeseriesinsights_environments, client_factory=cf_environments) as g:
        g.custom_command('create', 'create_timeseriesinsights_environment_longterm',
                         doc_string_source="azext_timeseriesinsights.vendored_sdks.timeseriesinsights.models#LongTermEnvironmentCreateOrUpdateParameters")
        g.custom_command('update', 'update_timeseriesinsights_environment_longterm')

    with self.command_group('timeseriesinsights environment', timeseriesinsights_environments, client_factory=cf_environments) as g:
        g.custom_command('delete', 'delete_timeseriesinsights_environment')
        g.custom_show_command('show', 'get_timeseriesinsights_environment')
        g.custom_command('list', 'list_timeseriesinsights_environment', transform=gen_dict_to_list_transform(key='value'))
    # endregion

    from ._client_factory import cf_event_sources
    timeseriesinsights_event_sources = CliCommandType(
        operations_tmpl='azext_timeseriesinsights.vendored_sdks.timeseriesinsights.operations._event_sources_operations#EventSourcesOperations.{}',
        client_factory=cf_event_sources)

    # region event-source
    with self.command_group('timeseriesinsights event-source eventhub', timeseriesinsights_event_sources, client_factory=cf_event_sources) as g:
        g.custom_command('create', 'create_timeseriesinsights_event_source_eventhub',
                         doc_string_source="azext_timeseriesinsights.vendored_sdks.timeseriesinsights.models#EventHubEventSourceCreateOrUpdateParameters")
        g.custom_command('update', 'update_timeseriesinsights_event_source_eventhub',
                         doc_string_source="azext_timeseriesinsights.vendored_sdks.timeseriesinsights.models#EventHubEventSourceCreateOrUpdateParameters")

    with self.command_group('timeseriesinsights event-source iothub', timeseriesinsights_event_sources, client_factory=cf_event_sources) as g:
        g.custom_command('create', 'create_timeseriesinsights_event_source_iothub',
                         doc_string_source="azext_timeseriesinsights.vendored_sdks.timeseriesinsights.models#IoTHubEventSourceCreateOrUpdateParameters")
        g.custom_command('update', 'update_timeseriesinsights_event_source_iothub',
                         doc_string_source="azext_timeseriesinsights.vendored_sdks.timeseriesinsights.models#IoTHubEventSourceCreateOrUpdateParameters")

    with self.command_group('timeseriesinsights event-source', timeseriesinsights_event_sources, client_factory=cf_event_sources) as g:
        g.custom_command('delete', 'delete_timeseriesinsights_event_source')
        g.custom_show_command('show', 'get_timeseriesinsights_event_source')
        g.custom_command('list', 'list_timeseriesinsights_event_source')
    # endregion

    from ._client_factory import cf_reference_data_sets
    timeseriesinsights_reference_data_sets = CliCommandType(
        operations_tmpl='azext_timeseriesinsights.vendored_sdks.timeseriesinsights.operations._reference_data_sets_operations#ReferenceDataSetsOperations.{}',
        client_factory=cf_reference_data_sets)

    with self.command_group('timeseriesinsights reference-data-set', timeseriesinsights_reference_data_sets, client_factory=cf_reference_data_sets) as g:
        g.custom_command('create', 'create_timeseriesinsights_reference_data_set')
        g.custom_command('update', 'update_timeseriesinsights_reference_data_set')
        g.custom_command('delete', 'delete_timeseriesinsights_reference_data_set')
        g.custom_show_command('show', 'get_timeseriesinsights_reference_data_set')
        g.custom_command('list', 'list_timeseriesinsights_reference_data_set')

    from ._client_factory import cf_access_policies
    timeseriesinsights_access_policies = CliCommandType(
        operations_tmpl='azext_timeseriesinsights.vendored_sdks.timeseriesinsights.operations._access_policies_operations#AccessPoliciesOperations.{}',
        client_factory=cf_access_policies)
    with self.command_group('timeseriesinsights access-policy', timeseriesinsights_access_policies, client_factory=cf_access_policies) as g:
        g.custom_command('create', 'create_timeseriesinsights_access_policy')
        g.custom_command('update', 'update_timeseriesinsights_access_policy')
        g.custom_command('delete', 'delete_timeseriesinsights_access_policy')
        g.custom_show_command('show', 'get_timeseriesinsights_access_policy')
        g.custom_command('list', 'list_timeseriesinsights_access_policy')
