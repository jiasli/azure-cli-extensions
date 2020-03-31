# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=line-too-long
from knack.help_files import helps  # pylint: disable=unused-import


helps['timeseriesinsights'] = """
type: group
short-summary: Manage Azure Time Series Insights.
"""

helps['timeseriesinsights operation'] = """
    type: group
    short-summary: Commands to manage timeseriesinsights operation.
"""

helps['timeseriesinsights operation list'] = """
    type: command
    short-summary: Lists all of the available Time Series Insights related operations.
    examples:
      - name: List available operations for the Time Series Insights resource provider
        text: |-
               az timeseriesinsights operation list
"""

helps['timeseriesinsights environment'] = """
    type: group
    short-summary: Commands to manage timeseriesinsights environment.
"""

helps['timeseriesinsights environment create'] = """
    type: command
    short-summary: Create or update an environment in the specified subscription and resource group.
    examples:
      - name: EnvironmentsCreate
        text: |-
               az timeseriesinsights environment create --resource-group "rg1" --name "env1" --location \\
               "West US" --sku-name "S1" --sku-capacity "1" --data-retention-time "P31D"
"""

helps['timeseriesinsights environment update'] = """
    type: command
    short-summary: Create or update an environment in the specified subscription and resource group.
    examples:
      - name: EnvironmentsUpdate
        text: |-
               az timeseriesinsights environment update --resource-group "rg1" --name "env1" --sku-name \\
               "S1" --sku-capacity "10"
"""

helps['timeseriesinsights environment delete'] = """
    type: command
    short-summary: Deletes the environment with the specified name in the specified subscription and resource group.
    examples:
      - name: EnvironmentsDelete
        text: |-
               az timeseriesinsights environment delete --resource-group "rg1" --name "env1"
"""

helps['timeseriesinsights environment show'] = """
    type: command
    short-summary: Gets the environment with the specified name in the specified subscription and resource group.
    examples:
      - name: EnvironmentsGet
        text: |-
               az timeseriesinsights environment show --resource-group "rg1" --name "env1"
"""

helps['timeseriesinsights environment list'] = """
    type: command
    short-summary: Lists all the available environments associated with the subscription and within the specified resource group.
    examples:
      - name: EnvironmentsByResourceGroup
        text: |-
               az timeseriesinsights environment list --resource-group "rg1"
      - name: EnvironmentsBySubscription
        text: |-
               az timeseriesinsights environment list
"""

helps['timeseriesinsights event-source'] = """
    type: group
    short-summary: Commands to manage timeseriesinsights event source.
"""

helps['timeseriesinsights event-source create'] = """
    type: command
    short-summary: Create or update an event source under the specified environment.
    examples:
      - name: CreateEventHubEventSource
        text: |-
               az timeseriesinsights event-source create --resource-group "rg1" --environment-name \\
               "env1" --name "es1" --location "West US"
"""

helps['timeseriesinsights event-source update'] = """
    type: command
    short-summary: Create or update an event source under the specified environment.
    examples:
      - name: UpdateEventSource
        text: |-
               az timeseriesinsights event-source update --resource-group "rg1" --environment-name \\
               "env1" --name "es1"
"""

helps['timeseriesinsights event-source delete'] = """
    type: command
    short-summary: Deletes the event source with the specified name in the specified subscription, resource group, and environment
    examples:
      - name: DeleteEventSource
        text: |-
               az timeseriesinsights event-source delete --resource-group "rg1" --environment-name \\
               "env1" --name "es1"
"""

helps['timeseriesinsights event-source show'] = """
    type: command
    short-summary: Gets the event source with the specified name in the specified environment.
    examples:
      - name: GetEventHubEventSource
        text: |-
               az timeseriesinsights event-source show --resource-group "rg1" --environment-name "env1" \\
               --name "es1"
"""

helps['timeseriesinsights event-source list'] = """
    type: command
    short-summary: Lists all the available event sources associated with the subscription and within the specified resource group and environment.
    examples:
      - name: ListEventSourcesByEnvironment
        text: |-
               az timeseriesinsights event-source list --resource-group "rg1" --environment-name "env1"
"""

helps['timeseriesinsights reference-data-set'] = """
    type: group
    short-summary: Commands to manage timeseriesinsights reference data set.
"""

helps['timeseriesinsights reference-data-set create'] = """
    type: command
    short-summary: Create or update a reference data set in the specified environment.
    examples:
      - name: ReferenceDataSetsCreate
        text: |-
               az timeseriesinsights reference-data-set create --resource-group "rg1" --environment-name \\
               "env1" --name "rds1" --location "West US" --key-properties DeviceId1 String DeviceFloor Double
"""

helps['timeseriesinsights reference-data-set update'] = """
    type: command
    short-summary: Create or update a reference data set in the specified environment.
    examples:
      - name: ReferenceDataSetsUpdate
        text: |-
               az timeseriesinsights reference-data-set update --resource-group "rg1" --environment-name \\
               "env1" --name "rds1"
"""

helps['timeseriesinsights reference-data-set delete'] = """
    type: command
    short-summary: Deletes the reference data set with the specified name in the specified subscription, resource group, and environment
    examples:
      - name: ReferenceDataSetsDelete
        text: |-
               az timeseriesinsights reference-data-set delete --resource-group "rg1" --environment-name \\
               "env1" --name "rds1"
"""

helps['timeseriesinsights reference-data-set show'] = """
    type: command
    short-summary: Gets the reference data set with the specified name in the specified environment.
    examples:
      - name: ReferenceDataSetsGet
        text: |-
               az timeseriesinsights reference-data-set show --resource-group "rg1" --environment-name \\
               "env1" --name "rds1"
"""

helps['timeseriesinsights reference-data-set list'] = """
    type: command
    short-summary: Lists all the available reference data sets associated with the subscription and within the specified resource group and environment.
    examples:
      - name: ReferenceDataSetsListByEnvironment
        text: |-
               az timeseriesinsights reference-data-set list --resource-group "rg1" --environment-name \\
               "env1"
"""

helps['timeseriesinsights access-policy'] = """
    type: group
    short-summary: Commands to manage timeseriesinsights access policy.
"""

helps['timeseriesinsights access-policy create'] = """
    type: command
    short-summary: Create or update an access policy in the specified environment.
    examples:
      - name: AccessPoliciesCreate
        text: |-
               az timeseriesinsights access-policy create --resource-group "rg1" --environment-name \\
               "env1" --name "ap1" --description "some description" --roles "Reader"
"""

helps['timeseriesinsights access-policy update'] = """
    type: command
    short-summary: Create or update an access policy in the specified environment.
    examples:
      - name: AccessPoliciesUpdate
        text: |-
               az timeseriesinsights access-policy update --resource-group "rg1" --environment-name \\
               "env1" --name "ap1" --roles "Reader,Contributor"
"""

helps['timeseriesinsights access-policy delete'] = """
    type: command
    short-summary: Deletes the access policy with the specified name in the specified subscription, resource group, and environment
    examples:
      - name: AccessPoliciesDelete
        text: |-
               az timeseriesinsights access-policy delete --resource-group "rg1" --environment-name \\
               "env1" --name "ap1"
"""

helps['timeseriesinsights access-policy show'] = """
    type: command
    short-summary: Gets the access policy with the specified name in the specified environment.
    examples:
      - name: AccessPoliciesGet
        text: |-
               az timeseriesinsights access-policy show --resource-group "rg1" --environment-name "env1" \\
               --name "ap1"
"""

helps['timeseriesinsights access-policy list'] = """
    type: command
    short-summary: Lists all the available access policies associated with the environment.
    examples:
      - name: AccessPoliciesByEnvironment
        text: |-
               az timeseriesinsights access-policy list --resource-group "rg1" --environment-name "env1"
"""
