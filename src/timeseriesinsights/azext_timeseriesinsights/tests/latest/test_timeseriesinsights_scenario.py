# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, StorageAccountPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class TimeSeriesInsightsClientScenarioTest(ScenarioTest):

    def _create_timeseriesinsights_environment(self):
        self.kwargs.update({
            'env': self.create_random_name('cli-test-tsi-env', 24),
        })
        # Create an environment with the name of {env}. Similar to
        # https://github.com/Azure/azure-cli/blob/31a9724478c67751ae0bee6cc0d9b75b763df17c/src/azure-cli/azure/cli/command_modules/keyvault/tests/latest/test_keyvault_commands.py#L34
        return self.cmd('az timeseriesinsights environment standard create '
                        '--resource-group {rg} '
                        '--name "{env}" '
                        '--location "westus" '
                        '--sku-name "S1" '
                        '--sku-capacity "1" '
                        '--data-retention-time "P31D" '
                        '--partition-key-properties DeviceId1 '
                        '--storage-limit-exceeded-behavior PauseIngress')

    @ResourceGroupPreparer(name_prefix='cli_test_timeseriesinsights')
    @StorageAccountPreparer()
    def test_timeseriesinsights_environment(self, resource_group, storage_account):

        # Test environment standard create
        self.cmd('az timeseriesinsights environment standard create '
                 '--resource-group {rg} '
                 '--name "env1" '
                 '--location "westus" '
                 '--sku-name "S1" '
                 '--sku-capacity "1" '
                 '--data-retention-time "P31D" '
                 '--partition-key-properties DeviceId1 '
                 '--storage-limit-exceeded-behavior PauseIngress',
                 checks=[self.check('name', 'env1')])

        # Test environment longterm create
        key = self.cmd('az storage account keys list -g {rg} -n {sa}').get_output_in_json()[0]['value']

        self.cmd('az timeseriesinsights environment longterm create '
                 '--resource-group {rg} '
                 '--name "env2" '
                 '--location "westus" '
                 '--sku-name "L1" '
                 '--sku-capacity "1" '
                 '--data-retention "P31D" '
                 '--time-series-id-properties DeviceId1 '
                 '--storage-account-name {sa} '
                 '--storage-management-key ' + key,
                 checks=[self.check('name', 'env2')])

        self.cmd('az timeseriesinsights environment show '
                 '--resource-group {rg} '
                 '--name "env1"',
                 checks=[self.check('name', 'env1')])

        self.cmd('az timeseriesinsights environment show '
                 '--resource-group {rg} '
                 '--name "env2"',
                 checks=[self.check('name', 'env2')])

        self.cmd('az timeseriesinsights environment list '
                 '--resource-group {rg}',
                 checks=[self.check('length(@)', 2)])

        self.cmd('az timeseriesinsights environment list',
                 checks=[])

        self.cmd('az timeseriesinsights environment delete '
                 '--resource-group {rg} '
                 '--name "env1"',
                 checks=[])

        self.cmd('az timeseriesinsights environment delete '
                 '--resource-group {rg} '
                 '--name "env2"',
                 checks=[])

    def test_debug(self):
        self._create_timeseriesinsights_environment()

    @ResourceGroupPreparer(name_prefix='cli_test_timeseriesinsights')
    def test_timeseriesinsights_access_policy(self):

        self._create_timeseriesinsights_environment()

        # Create
        self.cmd('az timeseriesinsights access-policy create -g {rg} --environment-name {env} --name ap1 --principal-object-id 001 --description "some description" --roles Reader',
                 checks=[])

        # Show
        self.cmd('az timeseriesinsights access-policy show -g {rg} --environment-name {env} --name ap1',
                 checks=[])
        # List
        self.cmd('az timeseriesinsights access-policy list -g {rg} --environment-name {env}',
                 checks=[])

        # Update
        self.cmd('az timeseriesinsights access-policy update -g {rg} --environment-name {env} --name ap1 --description "some description updated"',
                 checks=[])

        self.cmd('az timeseriesinsights access-policy update -g {rg} --environment-name {env} --name ap1 --roles Contributor',
                 checks=[])

        # Delete
        self.cmd('az timeseriesinsights access-policy delete -g {rg} --environment-name {env} --name ap1',
                 checks=[])

    @ResourceGroupPreparer(name_prefix='cli_test_timeseriesinsights')
    def test_timeseriesinsights_other(self, resource_group):

        self.cmd('az timeseriesinsights event-source create '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "es1" '
                 '--location "West US"',
                 checks=[])

        self.cmd('az timeseriesinsights access-policy create '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "ap1" '
                 '--description "some description" '
                 '--roles "Reader"',
                 checks=[])

        self.cmd('az timeseriesinsights reference-data-set create '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "rds1" '
                 '--location "West US"',
                 checks=[])

        self.cmd('az timeseriesinsights reference-data-set show '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "rds1"',
                 checks=[])

        self.cmd('az timeseriesinsights access-policy show '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "ap1"',
                 checks=[])

        self.cmd('az timeseriesinsights event-source show '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "es1"',
                 checks=[])

        self.cmd('az timeseriesinsights reference-data-set list '
                 '--resource-group {rg} '
                 '--environment-name "env1"',
                 checks=[])

        self.cmd('az timeseriesinsights access-policy list '
                 '--resource-group {rg} '
                 '--environment-name "env1"',
                 checks=[])

        self.cmd('az timeseriesinsights event-source list '
                 '--resource-group {rg} '
                 '--environment-name "env1"',
                 checks=[])



        self.cmd('az timeseriesinsights operation list',
                 checks=[])

        self.cmd('az timeseriesinsights reference-data-set update '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "rds1"',
                 checks=[])

        self.cmd('az timeseriesinsights access-policy update '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "ap1" '
                 '--roles "Reader,Contributor"',
                 checks=[])

        self.cmd('az timeseriesinsights event-source update '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "es1"',
                 checks=[])

        self.cmd('az timeseriesinsights environment update '
                 '--resource-group {rg} '
                 '--name "env1" '
                 '--sku-name "S1" '
                 '--sku-capacity "10"',
                 checks=[])

        self.cmd('az timeseriesinsights reference-data-set delete '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "rds1"',
                 checks=[])

        self.cmd('az timeseriesinsights access-policy delete '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "ap1"',
                 checks=[])

        self.cmd('az timeseriesinsights event-source delete '
                 '--resource-group {rg} '
                 '--environment-name "env1" '
                 '--name "es1"',
                 checks=[])

        self.cmd('az timeseriesinsights environment delete '
                 '--resource-group {rg} '
                 '--name "env1"',
                 checks=[])
