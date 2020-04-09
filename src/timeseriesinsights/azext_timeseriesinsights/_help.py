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

helps['timeseriesinsights environment standard create'] = """
type: command
short-summary: Create or update a standard environment in the specified subscription and resource group.
examples:
  - name: Create a standard environment
    text: az timeseriesinsights environment standard create --resource-group {rg} --name {env} --location westus --sku-name S1 --sku-capacity 1 --data-retention-time P31D --partition-key DeviceId1 --storage-limit-exceeded-behavior PauseIngress
"""

helps['timeseriesinsights environment standard update'] = """
type: command
short-summary: Update a standard environment in the specified subscription and resource group.
examples:
  - name: Update sku capacity
    text: az timeseriesinsights environment standard update --resource-group {rg} --name {env} --sku-name S1 --sku-capacity 2
  - name: Update data retention days
    text: az timeseriesinsights environment standard update --resource-group {rg} --name {env} --data-retention-time 8
  - name: Update storage limit exceeded behavior
    text: az timeseriesinsights environment standard update --resource-group {rg} --name {env} --storage-limit-exceeded-behavior PurgeOldData
"""

helps['timeseriesinsights environment longterm create'] = """
type: command
short-summary: Create or update a longterm environment in the specified subscription and resource group.
examples:
  - name: Create storage account and use it to create a longterm environment
    text: |
        storage=mystorageaccount
        rg=rg1
        az storage account create -g $rg -n $storage --https-only
        key=$(az storage account keys list -g $rg -n $storage --query [0].value --output tsv)        
        az timeseriesinsights environment longterm create --resource-group $rg --name env1 --location westus --sku-name L1 --sku-capacity 1 --data-retention 7 --time-series-id-properties DeviceId1 --storage-account-name $storage --storage-management-key $key
"""

helps['timeseriesinsights environment longterm update'] = """
type: command
short-summary: Update a longterm environment in the specified subscription and resource group.
examples:
  - name: Update dataRetention
    text: az timeseriesinsights environment longterm update --resource-group {rg} --name {env} --data-retention 8
  - name: Update storageLimitExceededBehavior (not working yet)
    text: az timeseriesinsights environment standard update --resource-group {rg} --name {env} --storage-limit-exceeded-behavior PurgeOldData
"""

helps['timeseriesinsights environment delete'] = """
type: command
short-summary: Deletes the environment with the specified name in the specified subscription and resource group.
examples:
  - name: Delete an environments
    text: |-
           az timeseriesinsights environment delete --resource-group rg1 --name env1
"""

helps['timeseriesinsights environment show'] = """
type: command
short-summary: Gets the environment with the specified name in the specified subscription and resource group.
examples:
  - name: Show an environments
    text: |-
           az timeseriesinsights environment show --resource-group rg1 --name env1
"""

helps['timeseriesinsights environment list'] = """
type: command
short-summary: Lists all the available environments associated with the subscription and within the specified resource group.
examples:
  - name: List environments by resource group
    text: |-
           az timeseriesinsights environment list --resource-group rg1
  - name: List environments by subscription
    text: |-
           az timeseriesinsights environment list
"""

helps['timeseriesinsights event-source'] = """
type: group
short-summary: Commands to manage timeseriesinsights event source.
"""

helps['timeseriesinsights event-source eventhub create'] = """
type: command
short-summary: Create or update an event hub event source under the specified environment.
examples:
  - name: Create an event hub and use it for event source
    text: |
        rg=rg1
        ehns=ehns0410
        eh=eh0410
        az eventhubs namespace create -g $rg -n $ehns
        es_resource_id=$(az eventhubs eventhub create -g $rg -n $eh --namespace-name $ehns --query id --output tsv)
        shared_access_key=$(az eventhubs namespace authorization-rule keys list -g $rg --namespace-name $ehns -n RootManageSharedAccessKey --query primaryKey --output tsv)
        az timeseriesinsights event-source eventhub create -g $rg --environment-name env1 --name es1 --service-bus-namespace $ehns --event-hub-name $eh --key-name RootManageSharedAccessKey --shared-access-key $shared_access_key --event-source-resource-id $es_resource_id --consumer-group-name '$Default' --timestamp-property-name DeviceId
"""

helps['timeseriesinsights event-source eventhub update'] = """
type: command
short-summary: Create or update an event source under the specified environment.
examples:
  - name: Update timestampPropertyName
    text: az timeseriesinsights event-source eventhub update -g {rg} --environment-name {env} --name {es} --timestamp-property-name DeviceId1
  - name: Update localTimestamp (not working yet)
    text: az timeseriesinsights event-source eventhub update -g {rg} --environment-name {env} --name {es} --local-timestamp-format Timespan --time-zone-offset-property-name OffsetDeviceId1
  - name: Update sharedAccessKey
    text: az timeseriesinsights event-source eventhub update -g {rg} --environment-name {env} --name {es} --shared-access-key {shared_access_key}
"""

helps['timeseriesinsights event-source iothub create'] = """
type: command
short-summary: Create or update an event hub event source under the specified environment.
examples:
  - name: Create an event hub and use it for event source
    text: |
        rg=rg1
        ehns=ehns0410
        eh=eh0410
        az eventhubs namespace create -g $rg -n $ehns
        es_resource_id=$(az eventhubs eventhub create -g $rg -n $eh --namespace-name $ehns --query id --output tsv)
        shared_access_key=$(az eventhubs namespace authorization-rule keys list -g $rg --namespace-name $ehns -n RootManageSharedAccessKey --query primaryKey --output tsv)
        az timeseriesinsights event-source eventhub create -g $rg --environment-name env1 --name es1 --service-bus-namespace $ehns --event-hub-name $eh --key-name RootManageSharedAccessKey --shared-access-key $shared_access_key --event-source-resource-id $es_resource_id --consumer-group-name '$Default' --timestamp-property-name DeviceId
"""

helps['timeseriesinsights event-source iothub update'] = """
type: command
short-summary: Create or update an event source under the specified environment.
examples:
  - name: Update timestampPropertyName
    text: az timeseriesinsights event-source eventhub update -g {rg} --environment-name {env} --name {es} --timestamp-property-name DeviceId1
  - name: Update localTimestamp (not working yet)
    text: az timeseriesinsights event-source eventhub update -g {rg} --environment-name {env} --name {es} --local-timestamp-format Timespan --time-zone-offset-property-name OffsetDeviceId1
  - name: Update sharedAccessKey
    text: az timeseriesinsights event-source eventhub update -g {rg} --environment-name {env} --name {es} --shared-access-key {shared_access_key}
"""

helps['timeseriesinsights event-source delete'] = """
type: command
short-summary: Deletes the event source with the specified name in the specified subscription, resource group, and environment
examples:
  - name: DeleteEventSource
    text: az timeseriesinsights event-source delete --resource-group rg1 --environment-name env1 --name es1
"""

helps['timeseriesinsights event-source show'] = """
type: command
short-summary: Gets the event source with the specified name in the specified environment.
examples:
  - name: GetEventHubEventSource
    text: az timeseriesinsights event-source show --resource-group rg1 --environment-name env1 --name es1
"""

helps['timeseriesinsights event-source list'] = """
type: command
short-summary: Lists all the available event sources associated with the subscription and within the specified resource group and environment.
examples:
  - name: ListEventSourcesByEnvironment
    text: az timeseriesinsights event-source list --resource-group rg1 --environment-name env1
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
           az timeseriesinsights reference-data-set create --resource-group rg1 --environment-name \\
           env1 --name "rds1" --location "West US" --key-properties DeviceId1 String DeviceFloor Double
"""

helps['timeseriesinsights reference-data-set update'] = """
type: command
short-summary: Create or update a reference data set in the specified environment.
examples:
  - name: ReferenceDataSetsUpdate
    text: |-
           az timeseriesinsights reference-data-set update --resource-group rg1 --environment-name \\
           env1 --name "rds1"
"""

helps['timeseriesinsights reference-data-set delete'] = """
type: command
short-summary: Deletes the reference data set with the specified name in the specified subscription, resource group, and environment
examples:
  - name: ReferenceDataSetsDelete
    text: |-
           az timeseriesinsights reference-data-set delete --resource-group rg1 --environment-name \\
           env1 --name "rds1"
"""

helps['timeseriesinsights reference-data-set show'] = """
type: command
short-summary: Gets the reference data set with the specified name in the specified environment.
examples:
  - name: ReferenceDataSetsGet
    text: |-
           az timeseriesinsights reference-data-set show --resource-group rg1 --environment-name \\
           env1 --name "rds1"
"""

helps['timeseriesinsights reference-data-set list'] = """
type: command
short-summary: Lists all the available reference data sets associated with the subscription and within the specified resource group and environment.
examples:
  - name: ReferenceDataSetsListByEnvironment
    text: |-
           az timeseriesinsights reference-data-set list --resource-group rg1 --environment-name \\
           env1
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
           az timeseriesinsights access-policy create --resource-group rg1 --environment-name \\
           env1 --name "ap1" --description "some description" --roles "Reader"
"""

helps['timeseriesinsights access-policy update'] = """
type: command
short-summary: Create or update an access policy in the specified environment.
examples:
  - name: AccessPoliciesUpdate
    text: |-
           az timeseriesinsights access-policy update --resource-group rg1 --environment-name \\
           env1 --name "ap1" --roles "Reader,Contributor"
"""

helps['timeseriesinsights access-policy delete'] = """
type: command
short-summary: Deletes the access policy with the specified name in the specified subscription, resource group, and environment
examples:
  - name: AccessPoliciesDelete
    text: |-
           az timeseriesinsights access-policy delete --resource-group rg1 --environment-name \\
           env1 --name "ap1"
"""

helps['timeseriesinsights access-policy show'] = """
type: command
short-summary: Gets the access policy with the specified name in the specified environment.
examples:
  - name: AccessPoliciesGet
    text: |-
           az timeseriesinsights access-policy show --resource-group rg1 --environment-name env1 \\
           --name "ap1"
"""

helps['timeseriesinsights access-policy list'] = """
type: command
short-summary: Lists all the available access policies associated with the environment.
examples:
  - name: AccessPoliciesByEnvironment
    text: |-
           az timeseriesinsights access-policy list --resource-group rg1 --environment-name env1
"""
