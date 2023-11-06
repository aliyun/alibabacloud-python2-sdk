# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ga20191120 import models as ga_20191120_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ga', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_entries_to_acl_with_options(self, request, runtime):
        """
        **AddEntriesToAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetAcl](~~258292~~) or [ListAcls](~~258291~~) operation to query the status of the ACL to which you want to add IP entries.
        *   If the ACL is in the **configuring** state, it indicates that IP entries are added to the ACL. In this case, you can perform only query operations.
        *   If the ACL is in the **active** state, it indicates that IP entries are added to the ACL.
        *   The **AddEntriesToAcl** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: AddEntriesToAclRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddEntriesToAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEntriesToAcl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.AddEntriesToAclResponse(),
            self.call_api(params, req, runtime)
        )

    def add_entries_to_acl(self, request):
        """
        **AddEntriesToAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetAcl](~~258292~~) or [ListAcls](~~258291~~) operation to query the status of the ACL to which you want to add IP entries.
        *   If the ACL is in the **configuring** state, it indicates that IP entries are added to the ACL. In this case, you can perform only query operations.
        *   If the ACL is in the **active** state, it indicates that IP entries are added to the ACL.
        *   The **AddEntriesToAcl** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: AddEntriesToAclRequest

        @return: AddEntriesToAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_entries_to_acl_with_options(request, runtime)

    def associate_acls_with_listener_with_options(self, request, runtime):
        """
        ## Description
        *   **AssociateAclsWithListener** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeListener](~~153254~~) operation to query the state of the listener with which you attempt to associate an ACL.
        *   If the listener is in the **updating** state, it indicates that the ACL is being associated. In this case, you can perform only query operations.
        *   If the listener is in the **active** state, it indicates that the ACL is associated.
        *   The **AssociateAclsWithListener** operation cannot be called repeatedly for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: AssociateAclsWithListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AssociateAclsWithListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAclsWithListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.AssociateAclsWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_acls_with_listener(self, request):
        """
        ## Description
        *   **AssociateAclsWithListener** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeListener](~~153254~~) operation to query the state of the listener with which you attempt to associate an ACL.
        *   If the listener is in the **updating** state, it indicates that the ACL is being associated. In this case, you can perform only query operations.
        *   If the listener is in the **active** state, it indicates that the ACL is associated.
        *   The **AssociateAclsWithListener** operation cannot be called repeatedly for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: AssociateAclsWithListenerRequest

        @return: AssociateAclsWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_acls_with_listener_with_options(request, runtime)

    def associate_additional_certificates_with_listener_with_options(self, request, runtime):
        """
        Only HTTPS listeners can be associated with additional certificates.
        *   **AssociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeListener](~~153254~~) operation to query the status of the listener with which you want to associate an additional certificate.
        *   If the listener is in the **updating** state, it indicates that the additional certificate is being associated. In this case, you can perform only query operations.
        *   If the listener is in the **active** state, it indicates that the additional certificate is associated.
        *   The **AssociateAdditionalCertificatesWithListener** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: AssociateAdditionalCertificatesWithListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AssociateAdditionalCertificatesWithListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAdditionalCertificatesWithListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.AssociateAdditionalCertificatesWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_additional_certificates_with_listener(self, request):
        """
        Only HTTPS listeners can be associated with additional certificates.
        *   **AssociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeListener](~~153254~~) operation to query the status of the listener with which you want to associate an additional certificate.
        *   If the listener is in the **updating** state, it indicates that the additional certificate is being associated. In this case, you can perform only query operations.
        *   If the listener is in the **active** state, it indicates that the additional certificate is associated.
        *   The **AssociateAdditionalCertificatesWithListener** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: AssociateAdditionalCertificatesWithListenerRequest

        @return: AssociateAdditionalCertificatesWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_additional_certificates_with_listener_with_options(request, runtime)

    def attach_ddos_to_accelerator_with_options(self, request, runtime):
        """
        When you call this operation, take note of the following items:
        *   **AttachDdosToAccelerator** is an asynchronous operation. After you call the operation, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) or [ListAccelerators](~~153236~~) operation to query the status of the GA instance.
        *   If the GA instance is in the **configuring** state, the Anti-DDoS Pro/Premium instance is being associated with the GA instance. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, the Anti-DDoS Pro/Premium instance is associated with the GA instance.
        *   You cannot repeatedly call the **AttachDdosToAccelerator** operation for the same GA instance within a specific period of time.
        

        @param request: AttachDdosToAcceleratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachDdosToAcceleratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.ddos_id):
            query['DdosId'] = request.ddos_id
        if not UtilClient.is_unset(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDdosToAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.AttachDdosToAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_ddos_to_accelerator(self, request):
        """
        When you call this operation, take note of the following items:
        *   **AttachDdosToAccelerator** is an asynchronous operation. After you call the operation, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) or [ListAccelerators](~~153236~~) operation to query the status of the GA instance.
        *   If the GA instance is in the **configuring** state, the Anti-DDoS Pro/Premium instance is being associated with the GA instance. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, the Anti-DDoS Pro/Premium instance is associated with the GA instance.
        *   You cannot repeatedly call the **AttachDdosToAccelerator** operation for the same GA instance within a specific period of time.
        

        @param request: AttachDdosToAcceleratorRequest

        @return: AttachDdosToAcceleratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_ddos_to_accelerator_with_options(request, runtime)

    def attach_log_store_to_endpoint_group_with_options(self, request, runtime):
        """
        **AttachLogStoreToEndpointGroup** is an asynchronous operation. After you send a request, the system returns a request ID, but this operation is still being performed in the system background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the state of an endpoint group.
        *   If the endpoint group is in the **updating** state, it indicates that a Logstore is being associated with the group. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, it indicates that a Logstore is associated with the group.
        *   The **AttachLogStoreToEndpointGroup** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: AttachLogStoreToEndpointGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachLogStoreToEndpointGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sls_log_store_name):
            query['SlsLogStoreName'] = request.sls_log_store_name
        if not UtilClient.is_unset(request.sls_project_name):
            query['SlsProjectName'] = request.sls_project_name
        if not UtilClient.is_unset(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachLogStoreToEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.AttachLogStoreToEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_log_store_to_endpoint_group(self, request):
        """
        **AttachLogStoreToEndpointGroup** is an asynchronous operation. After you send a request, the system returns a request ID, but this operation is still being performed in the system background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the state of an endpoint group.
        *   If the endpoint group is in the **updating** state, it indicates that a Logstore is being associated with the group. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, it indicates that a Logstore is associated with the group.
        *   The **AttachLogStoreToEndpointGroup** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: AttachLogStoreToEndpointGroupRequest

        @return: AttachLogStoreToEndpointGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_log_store_to_endpoint_group_with_options(request, runtime)

    def bandwidth_package_add_accelerator_with_options(self, request, runtime):
        """
        **BandwidthPackageAddAccelerator** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeBandwidthPackage](~~153241~~) operation to query the status of the bandwidth plan that you want to associate.
        *   If the bandwidth plan is in the **binding** state, it indicates that the bandwidth plan is being associated. In this case, you can perform only query operations.
        *   If the bandwidth plan is in the **active** state, it indicates that the bandwidth plan is associated.
        *   The **BandwidthPackageAddAccelerator** operation holds an exclusive lock on the GA instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: BandwidthPackageAddAcceleratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BandwidthPackageAddAcceleratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BandwidthPackageAddAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.BandwidthPackageAddAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def bandwidth_package_add_accelerator(self, request):
        """
        **BandwidthPackageAddAccelerator** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeBandwidthPackage](~~153241~~) operation to query the status of the bandwidth plan that you want to associate.
        *   If the bandwidth plan is in the **binding** state, it indicates that the bandwidth plan is being associated. In this case, you can perform only query operations.
        *   If the bandwidth plan is in the **active** state, it indicates that the bandwidth plan is associated.
        *   The **BandwidthPackageAddAccelerator** operation holds an exclusive lock on the GA instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: BandwidthPackageAddAcceleratorRequest

        @return: BandwidthPackageAddAcceleratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bandwidth_package_add_accelerator_with_options(request, runtime)

    def bandwidth_package_remove_accelerator_with_options(self, request, runtime):
        """
        **BandwidthPackageRemoveAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeBandwidthPackage](~~153241~~) operation to query the status of the bandwidth plan that you attempt to disassociate.
        *   If the bandwidth plan is in the **unbinding** state, it indicates that the bandwidth plan is being disassociated. In this case, you can perform only query operations.
        *   If the bandwidth plan is in the **active** state, it indicates that the bandwidth plan is disassociated.
        *   The **BandwidthPackageRemoveAccelerator** cannot be called repeatedly for the same GA instance.
        

        @param request: BandwidthPackageRemoveAcceleratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BandwidthPackageRemoveAcceleratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BandwidthPackageRemoveAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.BandwidthPackageRemoveAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def bandwidth_package_remove_accelerator(self, request):
        """
        **BandwidthPackageRemoveAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeBandwidthPackage](~~153241~~) operation to query the status of the bandwidth plan that you attempt to disassociate.
        *   If the bandwidth plan is in the **unbinding** state, it indicates that the bandwidth plan is being disassociated. In this case, you can perform only query operations.
        *   If the bandwidth plan is in the **active** state, it indicates that the bandwidth plan is disassociated.
        *   The **BandwidthPackageRemoveAccelerator** cannot be called repeatedly for the same GA instance.
        

        @param request: BandwidthPackageRemoveAcceleratorRequest

        @return: BandwidthPackageRemoveAcceleratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bandwidth_package_remove_accelerator_with_options(request, runtime)

    def change_resource_group_with_options(self, request, runtime):
        """
        You cannot call the *ChangeResourceGroup** operation again on the same GA instance before the previous operation is complete.
        

        @param request: ChangeResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def change_resource_group(self, request):
        """
        You cannot call the *ChangeResourceGroup** operation again on the same GA instance before the previous operation is complete.
        

        @param request: ChangeResourceGroupRequest

        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    def config_endpoint_probe_with_options(self, request, runtime):
        """
        **ConfigEndpointProbe** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the status of the endpoint group to which an endpoint belongs and determine whether latency monitoring is configured for the endpoint.
        *   If the endpoint group is in the **updating** state, it indicates that latency monitoring is being configured for the endpoint. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, it indicates that latency monitoring is configured for the endpoint.
        *   The **ConfigEndpointProbe** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: ConfigEndpointProbeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ConfigEndpointProbeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.probe_port):
            query['ProbePort'] = request.probe_port
        if not UtilClient.is_unset(request.probe_protocol):
            query['ProbeProtocol'] = request.probe_protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigEndpointProbe',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ConfigEndpointProbeResponse(),
            self.call_api(params, req, runtime)
        )

    def config_endpoint_probe(self, request):
        """
        **ConfigEndpointProbe** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the status of the endpoint group to which an endpoint belongs and determine whether latency monitoring is configured for the endpoint.
        *   If the endpoint group is in the **updating** state, it indicates that latency monitoring is being configured for the endpoint. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, it indicates that latency monitoring is configured for the endpoint.
        *   The **ConfigEndpointProbe** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: ConfigEndpointProbeRequest

        @return: ConfigEndpointProbeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_endpoint_probe_with_options(request, runtime)

    def create_accelerator_with_options(self, request, runtime):
        """
        ## Description
        **CreateAccelerator** is an asynchronous operation. After you send a request, the system returns the ID of a GA instance, but the operation is still being performed in the system background. You can call the [DescribeAccelerator](~~153235~~) operation to query the state of a GA instance.
        *   If the GA instance is in the **init** state, it indicates that the GA instance is being created. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, it indicates that the GA instance is created.
        

        @param request: CreateAcceleratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAcceleratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.bandwidth_billing_type):
            query['BandwidthBillingType'] = request.bandwidth_billing_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.ip_set_config):
            query['IpSetConfig'] = request.ip_set_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_accelerator(self, request):
        """
        ## Description
        **CreateAccelerator** is an asynchronous operation. After you send a request, the system returns the ID of a GA instance, but the operation is still being performed in the system background. You can call the [DescribeAccelerator](~~153235~~) operation to query the state of a GA instance.
        *   If the GA instance is in the **init** state, it indicates that the GA instance is being created. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, it indicates that the GA instance is created.
        

        @param request: CreateAcceleratorRequest

        @return: CreateAcceleratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_accelerator_with_options(request, runtime)

    def create_acl_with_options(self, request, runtime):
        """
        *CreateAcl** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [GetAcl](~~258292~~) or [ListAcls](~~258291~~) operation to query the state of an ACL.
        *   If the ACL is in the **init** state, the ACL is being created. In this case, you can only perform only query operations.
        *   If the ACL is in the **active** state, the ACL is created.
        

        @param request: CreateAclRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAcl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateAclResponse(),
            self.call_api(params, req, runtime)
        )

    def create_acl(self, request):
        """
        *CreateAcl** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [GetAcl](~~258292~~) or [ListAcls](~~258291~~) operation to query the state of an ACL.
        *   If the ACL is in the **init** state, the ACL is being created. In this case, you can only perform only query operations.
        *   If the ACL is in the **active** state, the ACL is created.
        

        @param request: CreateAclRequest

        @return: CreateAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    def create_application_monitor_with_options(self, request, runtime):
        """
        You can call the *CreateApplicationMonitor** operation to create an origin probing task. An origin probing task monitors the network quality between the client and origin server and checks the availability of the origin.
        Before you call this operation, take note of the following items:
        *   **CreateApplicationMonitor** is an asynchronous operation. After you send a request, the system returns the ID of an origin probing task, but the origin probing task is still being created in the system background. You can call the [DescribeApplicationMonitor](~~408463~~) or [ListApplicationMonitor](~~408462~~) operation to query the state of the origin probing task.
        *   If the origin probing task is in the **init** state, it indicates that the task is being created. In this case, you can only perform query operations.
        *   If the origin probing task is in the **active** state, it indicates that the task is created.
        *   The **CreateApplicationMonitor** operation cannot be called repeatedly for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: CreateApplicationMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateApplicationMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.detect_enable):
            query['DetectEnable'] = request.detect_enable
        if not UtilClient.is_unset(request.detect_threshold):
            query['DetectThreshold'] = request.detect_threshold
        if not UtilClient.is_unset(request.detect_times):
            query['DetectTimes'] = request.detect_times
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationMonitor',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_application_monitor(self, request):
        """
        You can call the *CreateApplicationMonitor** operation to create an origin probing task. An origin probing task monitors the network quality between the client and origin server and checks the availability of the origin.
        Before you call this operation, take note of the following items:
        *   **CreateApplicationMonitor** is an asynchronous operation. After you send a request, the system returns the ID of an origin probing task, but the origin probing task is still being created in the system background. You can call the [DescribeApplicationMonitor](~~408463~~) or [ListApplicationMonitor](~~408462~~) operation to query the state of the origin probing task.
        *   If the origin probing task is in the **init** state, it indicates that the task is being created. In this case, you can only perform query operations.
        *   If the origin probing task is in the **active** state, it indicates that the task is created.
        *   The **CreateApplicationMonitor** operation cannot be called repeatedly for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: CreateApplicationMonitorRequest

        @return: CreateApplicationMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_monitor_with_options(request, runtime)

    def create_bandwidth_package_with_options(self, request, runtime):
        """
        To use Global Accelerator (GA) for acceleration, you must purchase a basic bandwidth plan. A basic bandwidth plan supports the following bandwidth types:
        *   **Basic**: Both the default acceleration region and the default service region are in the Chinese mainland. The accelerated service is deployed on Alibaba Cloud.
        *   **Enhanced**: Both the default acceleration region and the default service region are in the Chinese mainland. The accelerated service can be deployed on and off Alibaba Cloud.
        *   **Premium**: Both the default acceleration region and the default service region are outside the Chinese mainland. The accelerated service can be deployed on and off Alibaba Cloud. If you want to accelerate data transfer for clients in the Chinese mainland, you must select China (Hong Kong) as the acceleration region.
        When you call this operation, take note of the following items:
        *   **CreateBandwidthPackage** is an asynchronous operation. After you send a request, the system returns the ID of a bandwidth plan, but the bandwidth plan is still being created in the system background. You can call the [DescribeBandwidthPackage](~~153241~~) operation to query the status of the bandwidth plan.
        *   If the bandwidth plan is in the **init** state, it indicates that the bandwidth plan is being created. In this case, you can perform only query operations.
        *   If the bandwidth plan is in the **active** state, it indicates that the bandwidth plan is created.
        *   The **CreateBandwidthPackage** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: CreateBandwidthPackageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBandwidthPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not UtilClient.is_unset(request.billing_type):
            query['BillingType'] = request.billing_type
        if not UtilClient.is_unset(request.cbn_geographic_region_id_a):
            query['CbnGeographicRegionIdA'] = request.cbn_geographic_region_id_a
        if not UtilClient.is_unset(request.cbn_geographic_region_id_b):
            query['CbnGeographicRegionIdB'] = request.cbn_geographic_region_id_b
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.ratio):
            query['Ratio'] = request.ratio
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBandwidthPackage',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_bandwidth_package(self, request):
        """
        To use Global Accelerator (GA) for acceleration, you must purchase a basic bandwidth plan. A basic bandwidth plan supports the following bandwidth types:
        *   **Basic**: Both the default acceleration region and the default service region are in the Chinese mainland. The accelerated service is deployed on Alibaba Cloud.
        *   **Enhanced**: Both the default acceleration region and the default service region are in the Chinese mainland. The accelerated service can be deployed on and off Alibaba Cloud.
        *   **Premium**: Both the default acceleration region and the default service region are outside the Chinese mainland. The accelerated service can be deployed on and off Alibaba Cloud. If you want to accelerate data transfer for clients in the Chinese mainland, you must select China (Hong Kong) as the acceleration region.
        When you call this operation, take note of the following items:
        *   **CreateBandwidthPackage** is an asynchronous operation. After you send a request, the system returns the ID of a bandwidth plan, but the bandwidth plan is still being created in the system background. You can call the [DescribeBandwidthPackage](~~153241~~) operation to query the status of the bandwidth plan.
        *   If the bandwidth plan is in the **init** state, it indicates that the bandwidth plan is being created. In this case, you can perform only query operations.
        *   If the bandwidth plan is in the **active** state, it indicates that the bandwidth plan is created.
        *   The **CreateBandwidthPackage** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: CreateBandwidthPackageRequest

        @return: CreateBandwidthPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_bandwidth_package_with_options(request, runtime)

    def create_basic_accelerate_ip_with_options(self, request, runtime):
        """
        **CreateBasicAccelerateIp** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [GetBasicAccelerateIp](~~466794~~) operation to query the status of an accelerated IP address:
        *   If no status information is returned, the accelerated IP address is being created. In this case, you can perform only query operations.
        *   If the accelerated IP address is in the **active** state, the accelerated IP address is created.
        *   The **CreateBasicAccelerateIp** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: CreateBasicAccelerateIpRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBasicAccelerateIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBasicAccelerateIp',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicAccelerateIpResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_accelerate_ip(self, request):
        """
        **CreateBasicAccelerateIp** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [GetBasicAccelerateIp](~~466794~~) operation to query the status of an accelerated IP address:
        *   If no status information is returned, the accelerated IP address is being created. In this case, you can perform only query operations.
        *   If the accelerated IP address is in the **active** state, the accelerated IP address is created.
        *   The **CreateBasicAccelerateIp** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: CreateBasicAccelerateIpRequest

        @return: CreateBasicAccelerateIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_basic_accelerate_ip_with_options(request, runtime)

    def create_basic_accelerate_ip_endpoint_relation_with_options(self, request, runtime):
        """
        **CreateBasicAccelerateIpEndpointRelation** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [GetBasicAccelerateIp](~~466794~~) or [ListBasicEndpoints](~~466831~~) API operation to query the status of an accelerated IP address or an endpoint to determine the association status between the accelerated IP address and endpoint.
        *   If the status of the accelerated IP address and endpoint is **binding**, the accelerated IP address is being associated with the endpoint. In this case, you can query the accelerated IP address and endpoint but cannot perform other operations.
        *   If the status of the accelerated IP address and endpoint is **bound** and the status returned by the [ListBasicAccelerateIpEndpointRelations](~~466803~~) API operation is **active**, the accelerated IP address is associated with the endpoint.
        *   The **CreateBasicAccelerateIpEndpointRelation** API operation cannot be repeatedly called for the same basic GA instance within a period of time.
        

        @param request: CreateBasicAccelerateIpEndpointRelationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBasicAccelerateIpEndpointRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBasicAccelerateIpEndpointRelation',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicAccelerateIpEndpointRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_accelerate_ip_endpoint_relation(self, request):
        """
        **CreateBasicAccelerateIpEndpointRelation** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [GetBasicAccelerateIp](~~466794~~) or [ListBasicEndpoints](~~466831~~) API operation to query the status of an accelerated IP address or an endpoint to determine the association status between the accelerated IP address and endpoint.
        *   If the status of the accelerated IP address and endpoint is **binding**, the accelerated IP address is being associated with the endpoint. In this case, you can query the accelerated IP address and endpoint but cannot perform other operations.
        *   If the status of the accelerated IP address and endpoint is **bound** and the status returned by the [ListBasicAccelerateIpEndpointRelations](~~466803~~) API operation is **active**, the accelerated IP address is associated with the endpoint.
        *   The **CreateBasicAccelerateIpEndpointRelation** API operation cannot be repeatedly called for the same basic GA instance within a period of time.
        

        @param request: CreateBasicAccelerateIpEndpointRelationRequest

        @return: CreateBasicAccelerateIpEndpointRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_basic_accelerate_ip_endpoint_relation_with_options(request, runtime)

    def create_basic_accelerate_ip_endpoint_relations_with_options(self, request, runtime):
        """
        The **CreateBasicAccelerateIpEndpointRelations** is asynchronous. After you send a request, the system returns a request ID and runs the task in the system background. You can call the [GetBasicAccelerateIp](~~466794~~) or [ListBasicEndpoints](~~466831~~) API operation to query the status of an accelerated IP address or an endpoint to determine the association status.
        *   If an accelerated IP address and the endpoint are in the **binding** state, the accelerated IP address is being associated with the endpoint. In this case, you can only query the accelerated IP address and endpoint, but cannot perform other operations.
        *   If all the accelerated IP addresses and the endpoint are in the **bound** state, and the association status returned by the [ListBasicAccelerateIpEndpointRelations](~~466803~~) API operation is **active**, the accelerated IP addresses are associated with the endpoints.
        *   The **CreateBasicAccelerateIpEndpointRelations** API operation cannot be repeatedly called for the same basic GA instance within a period of time.
        

        @param request: CreateBasicAccelerateIpEndpointRelationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBasicAccelerateIpEndpointRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerate_ip_endpoint_relations):
            query['AccelerateIpEndpointRelations'] = request.accelerate_ip_endpoint_relations
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBasicAccelerateIpEndpointRelations',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicAccelerateIpEndpointRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_accelerate_ip_endpoint_relations(self, request):
        """
        The **CreateBasicAccelerateIpEndpointRelations** is asynchronous. After you send a request, the system returns a request ID and runs the task in the system background. You can call the [GetBasicAccelerateIp](~~466794~~) or [ListBasicEndpoints](~~466831~~) API operation to query the status of an accelerated IP address or an endpoint to determine the association status.
        *   If an accelerated IP address and the endpoint are in the **binding** state, the accelerated IP address is being associated with the endpoint. In this case, you can only query the accelerated IP address and endpoint, but cannot perform other operations.
        *   If all the accelerated IP addresses and the endpoint are in the **bound** state, and the association status returned by the [ListBasicAccelerateIpEndpointRelations](~~466803~~) API operation is **active**, the accelerated IP addresses are associated with the endpoints.
        *   The **CreateBasicAccelerateIpEndpointRelations** API operation cannot be repeatedly called for the same basic GA instance within a period of time.
        

        @param request: CreateBasicAccelerateIpEndpointRelationsRequest

        @return: CreateBasicAccelerateIpEndpointRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_basic_accelerate_ip_endpoint_relations_with_options(request, runtime)

    def create_basic_accelerator_with_options(self, request, runtime):
        """
        Basic GA instances leverage the immense bandwidth of Alibaba Cloud\\"s high-quality global network to provide end-to-end acceleration services. You can use basic GA instances to accelerate content delivery at Layer 3 (IP). For more information, see [Overview of GA instances](~~153127~~).
        **CreateBasicAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [GetBasicAccelerator](~~353188~~) or [ListBasicAccelerators](~~353189~~) operation to query the status of a basic GA instance:
        *   If the basic GA instance is in the **init** state, it indicates that the basic GA instance is being created. In this case, you can continue to perform query operations on the GA instance.
        *   If the basic GA instance is in the **active** state, it indicates that the basic GA instance is created.
        

        @param request: CreateBasicAcceleratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBasicAcceleratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.bandwidth_billing_type):
            query['BandwidthBillingType'] = request.bandwidth_billing_type
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBasicAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_accelerator(self, request):
        """
        Basic GA instances leverage the immense bandwidth of Alibaba Cloud\\"s high-quality global network to provide end-to-end acceleration services. You can use basic GA instances to accelerate content delivery at Layer 3 (IP). For more information, see [Overview of GA instances](~~153127~~).
        **CreateBasicAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [GetBasicAccelerator](~~353188~~) or [ListBasicAccelerators](~~353189~~) operation to query the status of a basic GA instance:
        *   If the basic GA instance is in the **init** state, it indicates that the basic GA instance is being created. In this case, you can continue to perform query operations on the GA instance.
        *   If the basic GA instance is in the **active** state, it indicates that the basic GA instance is created.
        

        @param request: CreateBasicAcceleratorRequest

        @return: CreateBasicAcceleratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_basic_accelerator_with_options(request, runtime)

    def create_basic_endpoint_with_options(self, request, runtime):
        """
        **CreateBasicEndpoint** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [ListBasicEndpoints](~~466831~~) API operation to query the status of an endpoint.
        *   If the endpoint is in the **init** state, the endpoint is being created. In this case, you can perform only query operations.
        *   If the endpoint is in the **active** state, the endpoint is created.
        *   The **CreateBasicEndpoint** API operation cannot be repeatedly called for the same basic GA instance within a specific period of time.
        

        @param request: CreateBasicEndpointRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBasicEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_address):
            query['EndpointAddress'] = request.endpoint_address
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoint_sub_address):
            query['EndpointSubAddress'] = request.endpoint_sub_address
        if not UtilClient.is_unset(request.endpoint_sub_address_type):
            query['EndpointSubAddressType'] = request.endpoint_sub_address_type
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.endpoint_zone_id):
            query['EndpointZoneId'] = request.endpoint_zone_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBasicEndpoint',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_endpoint(self, request):
        """
        **CreateBasicEndpoint** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [ListBasicEndpoints](~~466831~~) API operation to query the status of an endpoint.
        *   If the endpoint is in the **init** state, the endpoint is being created. In this case, you can perform only query operations.
        *   If the endpoint is in the **active** state, the endpoint is created.
        *   The **CreateBasicEndpoint** API operation cannot be repeatedly called for the same basic GA instance within a specific period of time.
        

        @param request: CreateBasicEndpointRequest

        @return: CreateBasicEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_basic_endpoint_with_options(request, runtime)

    def create_basic_endpoint_group_with_options(self, request, runtime):
        """
        **CreateBasicEndpointGroup** is an asynchronous operation. After a request is sent, the system returns an endpoint group ID and runs the task in the background. You can call the [GetBasicEndpointGroup](~~362984~~) operation to query the status of the task.
        *   If the endpoint group is in the **init** state, the endpoint is being created. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, the endpoint group is created.
        *   You cannot call the **CreateBasicEndpointGroup** operation again on the same GA instance before the previous request is completed.
        

        @param request: CreateBasicEndpointGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBasicEndpointGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint_address):
            query['EndpointAddress'] = request.endpoint_address
        if not UtilClient.is_unset(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not UtilClient.is_unset(request.endpoint_sub_address):
            query['EndpointSubAddress'] = request.endpoint_sub_address
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBasicEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_endpoint_group(self, request):
        """
        **CreateBasicEndpointGroup** is an asynchronous operation. After a request is sent, the system returns an endpoint group ID and runs the task in the background. You can call the [GetBasicEndpointGroup](~~362984~~) operation to query the status of the task.
        *   If the endpoint group is in the **init** state, the endpoint is being created. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, the endpoint group is created.
        *   You cannot call the **CreateBasicEndpointGroup** operation again on the same GA instance before the previous request is completed.
        

        @param request: CreateBasicEndpointGroupRequest

        @return: CreateBasicEndpointGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_basic_endpoint_group_with_options(request, runtime)

    def create_basic_endpoints_with_options(self, request, runtime):
        """
        **CreateBasicEndpoints** is an asynchronous operation. After you call this operation, the system returns a request ID and runs the task in the background. You can call the [ListBasicEndpoints](~~466831~~) operation to query the status of endpoints. - If one or more endpoints are in the **init** state, it indicates that the endpoints are being created. In this case, you can continue to perform query operations on the endpoints. If all endpoints are in the **active** state, it indicates that the endpoints are created.
        *   You cannot call the **CreateBasicEndpoints** operation again on the same GA instance before the previous operation is complete.
        

        @param request: CreateBasicEndpointsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBasicEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoints):
            query['Endpoints'] = request.endpoints
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBasicEndpoints',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_endpoints(self, request):
        """
        **CreateBasicEndpoints** is an asynchronous operation. After you call this operation, the system returns a request ID and runs the task in the background. You can call the [ListBasicEndpoints](~~466831~~) operation to query the status of endpoints. - If one or more endpoints are in the **init** state, it indicates that the endpoints are being created. In this case, you can continue to perform query operations on the endpoints. If all endpoints are in the **active** state, it indicates that the endpoints are created.
        *   You cannot call the **CreateBasicEndpoints** operation again on the same GA instance before the previous operation is complete.
        

        @param request: CreateBasicEndpointsRequest

        @return: CreateBasicEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_basic_endpoints_with_options(request, runtime)

    def create_basic_ip_set_with_options(self, request, runtime):
        """
        Take note of the following limits:
        *   You can specify only one acceleration region for each basic GA instance, and only IPv4 clients can connect to basic GA instances.
        *   **CreateBasicIpSet** is an asynchronous operation. After you send a request, the system returns an acceleration region ID and runs the task in the background. You can call the [GetBasicIpSet](~~362987~~) operation to query the status of the task.
        *   If the acceleration region is in the **init** state, the acceleration region is being created. In this case, you can perform only query operations.
        *   If the acceleration region is in the **active** state, the acceleration region is created.
        *   You cannot call the **CreateBasicIpSet** operation again on the same GA instance before the previous task is completed.
        

        @param request: CreateBasicIpSetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateBasicIpSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerate_region_id):
            query['AccelerateRegionId'] = request.accelerate_region_id
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.isp_type):
            query['IspType'] = request.isp_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBasicIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def create_basic_ip_set(self, request):
        """
        Take note of the following limits:
        *   You can specify only one acceleration region for each basic GA instance, and only IPv4 clients can connect to basic GA instances.
        *   **CreateBasicIpSet** is an asynchronous operation. After you send a request, the system returns an acceleration region ID and runs the task in the background. You can call the [GetBasicIpSet](~~362987~~) operation to query the status of the task.
        *   If the acceleration region is in the **init** state, the acceleration region is being created. In this case, you can perform only query operations.
        *   If the acceleration region is in the **active** state, the acceleration region is created.
        *   You cannot call the **CreateBasicIpSet** operation again on the same GA instance before the previous task is completed.
        

        @param request: CreateBasicIpSetRequest

        @return: CreateBasicIpSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_basic_ip_set_with_options(request, runtime)

    def create_custom_routing_endpoint_group_destinations_with_options(self, request, runtime):
        """
        readAndWrite
        

        @param request: CreateCustomRoutingEndpointGroupDestinationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCustomRoutingEndpointGroupDestinationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_configurations):
            query['DestinationConfigurations'] = request.destination_configurations
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomRoutingEndpointGroupDestinations',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateCustomRoutingEndpointGroupDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_custom_routing_endpoint_group_destinations(self, request):
        """
        readAndWrite
        

        @param request: CreateCustomRoutingEndpointGroupDestinationsRequest

        @return: CreateCustomRoutingEndpointGroupDestinationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_routing_endpoint_group_destinations_with_options(request, runtime)

    def create_custom_routing_endpoint_groups_with_options(self, request, runtime):
        """
        Global Accelerator (GA) forwards client requests to endpoints in an endpoint group based on the routing type of the listener that is associated with the endpoint group.
        *   After you configure an intelligent routing listener for a GA instance, the GA instance selects a nearby and healthy endpoint group and forwards client requests to a healthy endpoint in the endpoint group.
        *   After you configure a custom routing listener for a GA instance, the instance generates a port mapping table based on the listener port range, protocols and port ranges of the associated endpoint groups, and IP addresses of endpoints (vSwitches), and forwards client requests to specified IP addresses and ports in the vSwitches.
        You can call this operation to create endpoint groups for custom routing listeners. For information about how to create endpoint groups for intelligent routing listeners, see [CreateEndpointGroup](~~153259~~).
        When you call this operation, take note of the following items:
        *   **CreateCustomRoutingEndpointGroups** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) or [ListCustomRoutingEndpointGroups](~~449374~~) operation to query the status of the endpoint groups that are associated with custom routing listeners.
        *   If one or more endpoint groups are in the **init** state, it indicates that the endpoint groups are being created. In this case, you can perform only query operations.
        *   If all endpoint groups are in the **active** state, it indicates that the endpoint groups are created.
        *   The **CreateCustomRoutingEndpointGroups** operation cannot be called repeatedly for the same GA instance within a specific period of time.
        ### Prerequisites
        Make sure that the following requirements are met before you call this operation:
        *   A standard GA instance is created. For more information, see [CreateAccelerator](~~206786~~).
        *   A bandwidth plan is associated with the standard GA instance. For more information, see [BandwidthPackageAddAccelerator](~~153239~~).
        *   An application is deployed to receive requests that are forwarded from GA. You can specify only vSwitches as endpoints for custom routing listeners.
        *   The permissions to use custom routing listeners are acquired and a custom routing listener is created for the GA instance. Custom routing listeners are in invitational preview. To use custom routing listeners, contact your account manager. For more information about how to create a custom routing listener, see [CreateListener](~~153253~~).
        

        @param request: CreateCustomRoutingEndpointGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCustomRoutingEndpointGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_group_configurations):
            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomRoutingEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateCustomRoutingEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_custom_routing_endpoint_groups(self, request):
        """
        Global Accelerator (GA) forwards client requests to endpoints in an endpoint group based on the routing type of the listener that is associated with the endpoint group.
        *   After you configure an intelligent routing listener for a GA instance, the GA instance selects a nearby and healthy endpoint group and forwards client requests to a healthy endpoint in the endpoint group.
        *   After you configure a custom routing listener for a GA instance, the instance generates a port mapping table based on the listener port range, protocols and port ranges of the associated endpoint groups, and IP addresses of endpoints (vSwitches), and forwards client requests to specified IP addresses and ports in the vSwitches.
        You can call this operation to create endpoint groups for custom routing listeners. For information about how to create endpoint groups for intelligent routing listeners, see [CreateEndpointGroup](~~153259~~).
        When you call this operation, take note of the following items:
        *   **CreateCustomRoutingEndpointGroups** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) or [ListCustomRoutingEndpointGroups](~~449374~~) operation to query the status of the endpoint groups that are associated with custom routing listeners.
        *   If one or more endpoint groups are in the **init** state, it indicates that the endpoint groups are being created. In this case, you can perform only query operations.
        *   If all endpoint groups are in the **active** state, it indicates that the endpoint groups are created.
        *   The **CreateCustomRoutingEndpointGroups** operation cannot be called repeatedly for the same GA instance within a specific period of time.
        ### Prerequisites
        Make sure that the following requirements are met before you call this operation:
        *   A standard GA instance is created. For more information, see [CreateAccelerator](~~206786~~).
        *   A bandwidth plan is associated with the standard GA instance. For more information, see [BandwidthPackageAddAccelerator](~~153239~~).
        *   An application is deployed to receive requests that are forwarded from GA. You can specify only vSwitches as endpoints for custom routing listeners.
        *   The permissions to use custom routing listeners are acquired and a custom routing listener is created for the GA instance. Custom routing listeners are in invitational preview. To use custom routing listeners, contact your account manager. For more information about how to create a custom routing listener, see [CreateListener](~~153253~~).
        

        @param request: CreateCustomRoutingEndpointGroupsRequest

        @return: CreateCustomRoutingEndpointGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_routing_endpoint_groups_with_options(request, runtime)

    def create_custom_routing_endpoint_traffic_policies_with_options(self, request, runtime):
        """
        This operation takes effect only when the traffic access policy of an endpoint allows traffic to specified destinations. You can call the [DescribeCustomRoutingEndpoint](~~449386~~) operation to query the traffic access policy of an endpoint. The CreateCustomRoutingEndpointTrafficPolicies operation takes effect only when *TrafficToEndpointPolicy** of an endpoint is set to **AllowCustom**.
        When you call this operation, take note of the following items:
        *   **CreateCustomRoutingEndpointTrafficPolicies** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the status of an endpoint group to check whether traffic destinations are created for an endpoint in the endpoint group.
        *   If the endpoint group is in the **updating** state, traffic destinations are being created. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, traffic destinations are created.
        *   You cannot repeatedly call the **CreateCustomRoutingEndpointTrafficPolicies** operation for the same Global Accelerator (GA) instance within a specific period of time.
        ### Prerequisites
        Before you call this operation, make sure that the following requirements are met:
        *   A standard GA instance is created. For more information, see [CreateAccelerator](~~206786~~).
        *   A bandwidth plan is associated with the standard GA instance. For more information, see [BandwidthPackageAddAccelerator](~~153239~~).
        *   An application is deployed to receive requests that are forwarded from GA. You can specify only vSwitches as endpoints for custom routing listeners.
        *   The permissions to use custom routing listeners are acquired and a custom routing listener is created for the GA instance. Custom routing listeners are in invitational preview. To use custom routing listeners, contact your account manager. For more information about how to create a custom routing listener, see [CreateListener](~~153253~~).
        *   An endpoint group is created for the custom routing listener. For more information, see [CreateCustomRoutingEndpointGroups](~~449363~~).
        *   An endpoint is created for the custom routing listener. For more information, see [CreateCustomRoutingEndpoints](~~449382~~).
        

        @param request: CreateCustomRoutingEndpointTrafficPoliciesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCustomRoutingEndpointTrafficPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.policy_configurations):
            query['PolicyConfigurations'] = request.policy_configurations
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomRoutingEndpointTrafficPolicies',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateCustomRoutingEndpointTrafficPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_custom_routing_endpoint_traffic_policies(self, request):
        """
        This operation takes effect only when the traffic access policy of an endpoint allows traffic to specified destinations. You can call the [DescribeCustomRoutingEndpoint](~~449386~~) operation to query the traffic access policy of an endpoint. The CreateCustomRoutingEndpointTrafficPolicies operation takes effect only when *TrafficToEndpointPolicy** of an endpoint is set to **AllowCustom**.
        When you call this operation, take note of the following items:
        *   **CreateCustomRoutingEndpointTrafficPolicies** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the status of an endpoint group to check whether traffic destinations are created for an endpoint in the endpoint group.
        *   If the endpoint group is in the **updating** state, traffic destinations are being created. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, traffic destinations are created.
        *   You cannot repeatedly call the **CreateCustomRoutingEndpointTrafficPolicies** operation for the same Global Accelerator (GA) instance within a specific period of time.
        ### Prerequisites
        Before you call this operation, make sure that the following requirements are met:
        *   A standard GA instance is created. For more information, see [CreateAccelerator](~~206786~~).
        *   A bandwidth plan is associated with the standard GA instance. For more information, see [BandwidthPackageAddAccelerator](~~153239~~).
        *   An application is deployed to receive requests that are forwarded from GA. You can specify only vSwitches as endpoints for custom routing listeners.
        *   The permissions to use custom routing listeners are acquired and a custom routing listener is created for the GA instance. Custom routing listeners are in invitational preview. To use custom routing listeners, contact your account manager. For more information about how to create a custom routing listener, see [CreateListener](~~153253~~).
        *   An endpoint group is created for the custom routing listener. For more information, see [CreateCustomRoutingEndpointGroups](~~449363~~).
        *   An endpoint is created for the custom routing listener. For more information, see [CreateCustomRoutingEndpoints](~~449382~~).
        

        @param request: CreateCustomRoutingEndpointTrafficPoliciesRequest

        @return: CreateCustomRoutingEndpointTrafficPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_routing_endpoint_traffic_policies_with_options(request, runtime)

    def create_custom_routing_endpoints_with_options(self, request, runtime):
        """
        readAndWrite
        

        @param request: CreateCustomRoutingEndpointsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCustomRoutingEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomRoutingEndpoints',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateCustomRoutingEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_custom_routing_endpoints(self, request):
        """
        readAndWrite
        

        @param request: CreateCustomRoutingEndpointsRequest

        @return: CreateCustomRoutingEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_routing_endpoints_with_options(request, runtime)

    def create_domain_with_options(self, request, runtime):
        """
        After you associate an accelerated domain name that has obtained an ICP number with a Global Accelerator (GA) instance, you do not need to complete filing for the accelerated domain name or its subdomains on Alibaba Cloud.
        You can call this operation to add an accelerated domain name and associate the accelerated domain name with GA instances. When you call this operation, take note of the following items:
        *   If your accelerated domain name is hosted in the Chinese mainland, you must obtain an ICP number for the domain name.
        *   The same accelerated domain name cannot be repeatedly associated with the same GA instance.
        *   You cannot repeatedly call the **CreateDomain** operation by using the same Alibaba Cloud account within a specific period of time.
        

        @param request: CreateDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_ids):
            query['AcceleratorIds'] = request.accelerator_ids
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def create_domain(self, request):
        """
        After you associate an accelerated domain name that has obtained an ICP number with a Global Accelerator (GA) instance, you do not need to complete filing for the accelerated domain name or its subdomains on Alibaba Cloud.
        You can call this operation to add an accelerated domain name and associate the accelerated domain name with GA instances. When you call this operation, take note of the following items:
        *   If your accelerated domain name is hosted in the Chinese mainland, you must obtain an ICP number for the domain name.
        *   The same accelerated domain name cannot be repeatedly associated with the same GA instance.
        *   You cannot repeatedly call the **CreateDomain** operation by using the same Alibaba Cloud account within a specific period of time.
        

        @param request: CreateDomainRequest

        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    def create_endpoint_group_with_options(self, request, runtime):
        """
        **CreateEndpointGroup** is an asynchronous operation. After you send a request, the system returns the ID of an endpoint group, but the endpoint group is still being created in the system background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the state of the endpoint group.
        *   If the endpoint group is in the **init** state, it indicates that the endpoint group is being created. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, it indicates that the endpoint group is created.
        *   The **CreateEndpointGroup** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: CreateEndpointGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateEndpointGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not UtilClient.is_unset(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not UtilClient.is_unset(request.endpoint_group_type):
            query['EndpointGroupType'] = request.endpoint_group_type
        if not UtilClient.is_unset(request.endpoint_request_protocol):
            query['EndpointRequestProtocol'] = request.endpoint_request_protocol
        if not UtilClient.is_unset(request.health_check_enabled):
            query['HealthCheckEnabled'] = request.health_check_enabled
        if not UtilClient.is_unset(request.health_check_interval_seconds):
            query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
        if not UtilClient.is_unset(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not UtilClient.is_unset(request.health_check_port):
            query['HealthCheckPort'] = request.health_check_port
        if not UtilClient.is_unset(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.port_overrides):
            query['PortOverrides'] = request.port_overrides
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.threshold_count):
            query['ThresholdCount'] = request.threshold_count
        if not UtilClient.is_unset(request.traffic_percentage):
            query['TrafficPercentage'] = request.traffic_percentage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_endpoint_group(self, request):
        """
        **CreateEndpointGroup** is an asynchronous operation. After you send a request, the system returns the ID of an endpoint group, but the endpoint group is still being created in the system background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the state of the endpoint group.
        *   If the endpoint group is in the **init** state, it indicates that the endpoint group is being created. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, it indicates that the endpoint group is created.
        *   The **CreateEndpointGroup** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: CreateEndpointGroupRequest

        @return: CreateEndpointGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_endpoint_group_with_options(request, runtime)

    def create_endpoint_groups_with_options(self, request, runtime):
        """
        **CreateEndpointGroups** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeEndpointGroup](~~153260~~) or [ListEndpointGroups](~~153261~~) to query the state of an endpoint group.
        *   If an endpoint group is in the **init** state, the endpoint group is being created. In this case, you can perform only query operations.
        *   If all endpoint groups are in the **active**, endpoint groups are created.
        *   The **CreateEndpointGroups** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: CreateEndpointGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateEndpointGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_group_configurations):
            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_endpoint_groups(self, request):
        """
        **CreateEndpointGroups** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeEndpointGroup](~~153260~~) or [ListEndpointGroups](~~153261~~) to query the state of an endpoint group.
        *   If an endpoint group is in the **init** state, the endpoint group is being created. In this case, you can perform only query operations.
        *   If all endpoint groups are in the **active**, endpoint groups are created.
        *   The **CreateEndpointGroups** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: CreateEndpointGroupsRequest

        @return: CreateEndpointGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_endpoint_groups_with_options(request, runtime)

    def create_forwarding_rules_with_options(self, request, runtime):
        """
        HTTP and HTTPS listeners of Global Accelerator (GA) support domain name-based and path-based forwarding rules. After an HTTP or HTTPS listener receives a request, the system matches the request against the forwarding conditions in a forwarding rule and then performs the corresponding forwarding action. For example, if you set *Host** to `www.example.com` as the forwarding condition and **Forward** to `epg-bp1enpdcrqhl78g6r****` as the forwarding action in a forwarding rule, requests to the `www.example.com` domain name match this forwarding rule and are forwarded to the `epg-bp1enpdcrqhl78g6r****` endpoint group. Before you call this API operation to create a forwarding rule, we recommend that you understand forwarding rules. For more information, see [Forwarding rules](~~204224~~).
        When you call this operation, take note of the following items:
        *   **CreateForwardingRules** is an asynchronous operation. After you send a request, the system returns the ID of a forwarding rule, but the forwarding rule is still being created in the system background. You can call the [ListForwardingRules](~~205817~~) operation to query the state of the forwarding rule.
        *   If the forwarding rule is in the **configuring** state, it indicates that the rule is being created. In this case, you can only perform query operations.
        *   If the forwarding rule is in the **active** state, it indicates that the rule is created.
        *   The **CreateForwardingRules** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: CreateForwardingRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateForwardingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.forwarding_rules):
            query['ForwardingRules'] = request.forwarding_rules
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateForwardingRules',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_forwarding_rules(self, request):
        """
        HTTP and HTTPS listeners of Global Accelerator (GA) support domain name-based and path-based forwarding rules. After an HTTP or HTTPS listener receives a request, the system matches the request against the forwarding conditions in a forwarding rule and then performs the corresponding forwarding action. For example, if you set *Host** to `www.example.com` as the forwarding condition and **Forward** to `epg-bp1enpdcrqhl78g6r****` as the forwarding action in a forwarding rule, requests to the `www.example.com` domain name match this forwarding rule and are forwarded to the `epg-bp1enpdcrqhl78g6r****` endpoint group. Before you call this API operation to create a forwarding rule, we recommend that you understand forwarding rules. For more information, see [Forwarding rules](~~204224~~).
        When you call this operation, take note of the following items:
        *   **CreateForwardingRules** is an asynchronous operation. After you send a request, the system returns the ID of a forwarding rule, but the forwarding rule is still being created in the system background. You can call the [ListForwardingRules](~~205817~~) operation to query the state of the forwarding rule.
        *   If the forwarding rule is in the **configuring** state, it indicates that the rule is being created. In this case, you can only perform query operations.
        *   If the forwarding rule is in the **active** state, it indicates that the rule is created.
        *   The **CreateForwardingRules** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: CreateForwardingRulesRequest

        @return: CreateForwardingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_forwarding_rules_with_options(request, runtime)

    def create_ip_sets_with_options(self, request, runtime):
        """
        **CreateIpSets** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeIpSet](~~153246~~) operation to query the status of the task.
        *   If acceleration regions are in the **init** state, it indicates that the acceleration regions are being created. In this case, you can perform only query operations.
        *   If acceleration regions are in the **active** state, it indicates that the acceleration regions are created.
        *   You cannot call the **CreateIpSets** operation again on the same GA instance before the previous operation is completed.
        

        @param request: CreateIpSetsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateIpSetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerate_region):
            query['AccelerateRegion'] = request.accelerate_region
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpSets',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ip_sets(self, request):
        """
        **CreateIpSets** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeIpSet](~~153246~~) operation to query the status of the task.
        *   If acceleration regions are in the **init** state, it indicates that the acceleration regions are being created. In this case, you can perform only query operations.
        *   If acceleration regions are in the **active** state, it indicates that the acceleration regions are created.
        *   You cannot call the **CreateIpSets** operation again on the same GA instance before the previous operation is completed.
        

        @param request: CreateIpSetsRequest

        @return: CreateIpSetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ip_sets_with_options(request, runtime)

    def create_listener_with_options(self, request, runtime):
        """
        A listener listens for connection requests and then distributes the requests to endpoints based on the forwarding rules that are defined by a specified scheduling algorithm. You can call this operation to create a listener for a standard GA instance.
        Before you call this operation, take note of the following limits:
        *   **CreateListener** is an asynchronous operation. After you send a request, the system returns a listener ID and runs the task in the background. You can call the [DescribeListener](~~153254~~) operation to query the status of a listener:
        *   If a listener is in the **init** state, the listener is being created. In this case, you can perform only query operations.
        *   If a listener is in the **active** state, the listener is created.
        *   The **CreateListener** operation cannot be repeatedly called to create listeners for the same GA instance in a specific period of time.
        

        @param request: CreateListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_affinity):
            query['ClientAffinity'] = request.client_affinity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.custom_routing_endpoint_group_configurations):
            query['CustomRoutingEndpointGroupConfigurations'] = request.custom_routing_endpoint_group_configurations
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint_group_configurations):
            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.port_ranges):
            query['PortRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.proxy_protocol):
            query['ProxyProtocol'] = request.proxy_protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_listener(self, request):
        """
        A listener listens for connection requests and then distributes the requests to endpoints based on the forwarding rules that are defined by a specified scheduling algorithm. You can call this operation to create a listener for a standard GA instance.
        Before you call this operation, take note of the following limits:
        *   **CreateListener** is an asynchronous operation. After you send a request, the system returns a listener ID and runs the task in the background. You can call the [DescribeListener](~~153254~~) operation to query the status of a listener:
        *   If a listener is in the **init** state, the listener is being created. In this case, you can perform only query operations.
        *   If a listener is in the **active** state, the listener is created.
        *   The **CreateListener** operation cannot be repeatedly called to create listeners for the same GA instance in a specific period of time.
        

        @param request: CreateListenerRequest

        @return: CreateListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_listener_with_options(request, runtime)

    def create_spare_ips_with_options(self, request, runtime):
        """
        **CreateSpareIps** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) operation to query the status of a GA instance.
        *   If the GA instance is in the **configuring** state, it indicates that secondary IP addresses are being created for the CNAME that is assigned to the GA instance. In this case, you can only perform query operations.
        *   If the GA instance is in the **active** state, it indicates that secondary IP addresses are created for the CNAME that is assigned to the GA instance.
        *   The **CreateSpareIps** operation holds an exclusive lock on the GA instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: CreateSpareIpsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSpareIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spare_ips):
            query['SpareIps'] = request.spare_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSpareIps',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.CreateSpareIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_spare_ips(self, request):
        """
        **CreateSpareIps** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) operation to query the status of a GA instance.
        *   If the GA instance is in the **configuring** state, it indicates that secondary IP addresses are being created for the CNAME that is assigned to the GA instance. In this case, you can only perform query operations.
        *   If the GA instance is in the **active** state, it indicates that secondary IP addresses are created for the CNAME that is assigned to the GA instance.
        *   The **CreateSpareIps** operation holds an exclusive lock on the GA instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: CreateSpareIpsRequest

        @return: CreateSpareIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_spare_ips_with_options(request, runtime)

    def delete_accelerator_with_options(self, request, runtime):
        """
        Subscription GA instances cannot be deleted.
        *   GA instances that have bandwidth plans associated cannot be deleted. To delete such GA instances, disassociate the bandwidth plans first. For information about how to disassociate a bandwidth plan from a GA instance, see [BandwidthPackageRemoveAccelerator](~~153240~~).
        *   **DeleteAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can use the [DescribeAccelerator](~~153235~~) operation to query the state of a GA instance.
        *   If the GA instance is in the **deleting** state, the GA instance is being deleted. In this case, you can perform only query operations.
        *   If the GA instance cannot be queried, it indicates that the GA instance is deleted.
        

        @param request: DeleteAcceleratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAcceleratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_accelerator(self, request):
        """
        Subscription GA instances cannot be deleted.
        *   GA instances that have bandwidth plans associated cannot be deleted. To delete such GA instances, disassociate the bandwidth plans first. For information about how to disassociate a bandwidth plan from a GA instance, see [BandwidthPackageRemoveAccelerator](~~153240~~).
        *   **DeleteAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can use the [DescribeAccelerator](~~153235~~) operation to query the state of a GA instance.
        *   If the GA instance is in the **deleting** state, the GA instance is being deleted. In this case, you can perform only query operations.
        *   If the GA instance cannot be queried, it indicates that the GA instance is deleted.
        

        @param request: DeleteAcceleratorRequest

        @return: DeleteAcceleratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_accelerator_with_options(request, runtime)

    def delete_acl_with_options(self, request, runtime):
        """
        *DeleteAcl** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [GetAcl](~~258292~~) operation to query the state of a network ACL.
        *   If the network ACL is in the **deleting** state, it indicates that the network ACL is being deleted. In this case, you can perform only query operations.
        *   If the network ACL cannot be queried, it indicates that the network ACL is deleted.
        

        @param request: DeleteAclRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteAclResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_acl(self, request):
        """
        *DeleteAcl** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [GetAcl](~~258292~~) operation to query the state of a network ACL.
        *   If the network ACL is in the **deleting** state, it indicates that the network ACL is being deleted. In this case, you can perform only query operations.
        *   If the network ACL cannot be queried, it indicates that the network ACL is deleted.
        

        @param request: DeleteAclRequest

        @return: DeleteAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    def delete_application_monitor_with_options(self, request, runtime):
        """
        **DeleteApplicationMonitor** is an asynchronous operation. After you call this operation, the system returns a request ID, but the operation is still being performed in the system background. You can call the [ListApplicationMonitor](~~408462~~) operation to query the state of an origin probing task.
        *   If the origin probing task is in the **deleting** state, it indicates that the task is being deleted. In this case, you can perform only query operations.
        <!---->
        *   If the origin probing task cannot be queried, it indicates that the task is deleted.
        *   The **DeleteApplicationMonitor** operation cannot be called repeatedly for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteApplicationMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteApplicationMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationMonitor',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_application_monitor(self, request):
        """
        **DeleteApplicationMonitor** is an asynchronous operation. After you call this operation, the system returns a request ID, but the operation is still being performed in the system background. You can call the [ListApplicationMonitor](~~408462~~) operation to query the state of an origin probing task.
        *   If the origin probing task is in the **deleting** state, it indicates that the task is being deleted. In this case, you can perform only query operations.
        <!---->
        *   If the origin probing task cannot be queried, it indicates that the task is deleted.
        *   The **DeleteApplicationMonitor** operation cannot be called repeatedly for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteApplicationMonitorRequest

        @return: DeleteApplicationMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_monitor_with_options(request, runtime)

    def delete_bandwidth_package_with_options(self, request, runtime):
        """
        By default, subscription bandwidth plans cannot be deleted. If you want to delete subscription bandwidth plans, contact your account manager.
        *   Bandwidth plans that are associated with Global Accelerator (GA) instances cannot be deleted. Before you can delete a bandwidth plan that is associated with a GA instance, you must disassociate the bandwidth plan from the GA instance. For information about how to disassociate a bandwidth plan from a GA instance, see [BandwidthPackageRemoveAccelerator](~~153240~~).
        *   **DeleteBandwidthPackage** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeBandwidthPackage](~~153241~~) operation to query the status of the task.
        *   If the bandwidth plan is in the **deleting** state, it indicates that the bandwidth plan is being deleted. In this case, you can perform only query operations.
        *   If the bandwidth plan cannot be found, it indicates that the bandwidth plan is deleted.
        *   The **DeleteBandwidthPackage** operation cannot be called repeatedly for the same bandwidth plan within a specific period of time.
        

        @param request: DeleteBandwidthPackageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBandwidthPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBandwidthPackage',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_bandwidth_package(self, request):
        """
        By default, subscription bandwidth plans cannot be deleted. If you want to delete subscription bandwidth plans, contact your account manager.
        *   Bandwidth plans that are associated with Global Accelerator (GA) instances cannot be deleted. Before you can delete a bandwidth plan that is associated with a GA instance, you must disassociate the bandwidth plan from the GA instance. For information about how to disassociate a bandwidth plan from a GA instance, see [BandwidthPackageRemoveAccelerator](~~153240~~).
        *   **DeleteBandwidthPackage** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeBandwidthPackage](~~153241~~) operation to query the status of the task.
        *   If the bandwidth plan is in the **deleting** state, it indicates that the bandwidth plan is being deleted. In this case, you can perform only query operations.
        *   If the bandwidth plan cannot be found, it indicates that the bandwidth plan is deleted.
        *   The **DeleteBandwidthPackage** operation cannot be called repeatedly for the same bandwidth plan within a specific period of time.
        

        @param request: DeleteBandwidthPackageRequest

        @return: DeleteBandwidthPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_bandwidth_package_with_options(request, runtime)

    def delete_basic_accelerate_ip_with_options(self, request, runtime):
        """
        **DeleteBasicAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [GetBasicAccelerateIp](~~466794~~) API operation to query the status of an accelerated IP address:
        *   If the accelerated IP address is in the **deleting** state, the accelerated IP address is being deleted. In this case, you can perform only query operations.
        *   If the system fails to return information about the accelerated IP address, the accelerated IP address is deleted.
        *   The **DeleteBasicAccelerateIp** API operation cannot be repeatedly called for the same basic GA instance within a period of time.
        

        @param request: DeleteBasicAccelerateIpRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBasicAccelerateIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBasicAccelerateIp',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBasicAccelerateIpResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_basic_accelerate_ip(self, request):
        """
        **DeleteBasicAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [GetBasicAccelerateIp](~~466794~~) API operation to query the status of an accelerated IP address:
        *   If the accelerated IP address is in the **deleting** state, the accelerated IP address is being deleted. In this case, you can perform only query operations.
        *   If the system fails to return information about the accelerated IP address, the accelerated IP address is deleted.
        *   The **DeleteBasicAccelerateIp** API operation cannot be repeatedly called for the same basic GA instance within a period of time.
        

        @param request: DeleteBasicAccelerateIpRequest

        @return: DeleteBasicAccelerateIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_basic_accelerate_ip_with_options(request, runtime)

    def delete_basic_accelerate_ip_endpoint_relation_with_options(self, request, runtime):
        """
        **DeleteBasicAccelerateIpEndpointRelation** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the following operations to check whether an accelerated IP address is disassociated from an endpoint:
        *   You can call the [GetBasicAccelerateIp](~~466794~~) and [ListBasicEndpoints](~~466831~~) operations to query the status of an accelerated IP address and an endpoint. If the accelerated IP address and the endpoint are in the **unbinding** state, the accelerated IP address is being disassociated from the endpoint. In this case, you can query the IP address and endpoint but cannot perform other operations.
        *   If the association status between the accelerated IP address and the endpoint cannot be queried by calling the [ListBasicAccelerateIpEndpointRelations](~~466803~~) operation, the accelerated IP address is disassociated from the endpoint.
        *   The **DeleteBasicAccelerateIpEndpointRelation** API operation cannot be repeatedly called for the same basic GA instance within a period of time.
        

        @param request: DeleteBasicAccelerateIpEndpointRelationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBasicAccelerateIpEndpointRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBasicAccelerateIpEndpointRelation',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBasicAccelerateIpEndpointRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_basic_accelerate_ip_endpoint_relation(self, request):
        """
        **DeleteBasicAccelerateIpEndpointRelation** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the following operations to check whether an accelerated IP address is disassociated from an endpoint:
        *   You can call the [GetBasicAccelerateIp](~~466794~~) and [ListBasicEndpoints](~~466831~~) operations to query the status of an accelerated IP address and an endpoint. If the accelerated IP address and the endpoint are in the **unbinding** state, the accelerated IP address is being disassociated from the endpoint. In this case, you can query the IP address and endpoint but cannot perform other operations.
        *   If the association status between the accelerated IP address and the endpoint cannot be queried by calling the [ListBasicAccelerateIpEndpointRelations](~~466803~~) operation, the accelerated IP address is disassociated from the endpoint.
        *   The **DeleteBasicAccelerateIpEndpointRelation** API operation cannot be repeatedly called for the same basic GA instance within a period of time.
        

        @param request: DeleteBasicAccelerateIpEndpointRelationRequest

        @return: DeleteBasicAccelerateIpEndpointRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_basic_accelerate_ip_endpoint_relation_with_options(request, runtime)

    def delete_basic_accelerator_with_options(self, request, runtime):
        """
        *DeleteBasicAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [GetBasicAccelerator](~~353188~~) operation to query the state of a basic GA instance.
        *   If the basic GA instance is in the **deleting** state, it indicates that the instance is being deleted. In this case, you can perform only query operations.
        *   If the information of the basic GA instance is not displayed in the response, it indicates that the instance is deleted.
        

        @param request: DeleteBasicAcceleratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBasicAcceleratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBasicAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_basic_accelerator(self, request):
        """
        *DeleteBasicAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [GetBasicAccelerator](~~353188~~) operation to query the state of a basic GA instance.
        *   If the basic GA instance is in the **deleting** state, it indicates that the instance is being deleted. In this case, you can perform only query operations.
        *   If the information of the basic GA instance is not displayed in the response, it indicates that the instance is deleted.
        

        @param request: DeleteBasicAcceleratorRequest

        @return: DeleteBasicAcceleratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_basic_accelerator_with_options(request, runtime)

    def delete_basic_endpoint_with_options(self, request, runtime):
        """
        **DeleteBasicEndpoint** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [ListBasicEndpoints](~~466831~~) operation to query the status of endpoints.
        *   If the endpoint is in the **deleting** state, it indicates that the endpoint is being deleted. In this case, you can perform only query operations.
        *   If the endpoint cannot be found, it indicates that the endpoint is deleted.
        *   The **DeleteBasicEndpoint** API operation cannot be repeatedly called for the same basic GA instance within a period of time.
        

        @param request: DeleteBasicEndpointRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBasicEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBasicEndpoint',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBasicEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_basic_endpoint(self, request):
        """
        **DeleteBasicEndpoint** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [ListBasicEndpoints](~~466831~~) operation to query the status of endpoints.
        *   If the endpoint is in the **deleting** state, it indicates that the endpoint is being deleted. In this case, you can perform only query operations.
        *   If the endpoint cannot be found, it indicates that the endpoint is deleted.
        *   The **DeleteBasicEndpoint** API operation cannot be repeatedly called for the same basic GA instance within a period of time.
        

        @param request: DeleteBasicEndpointRequest

        @return: DeleteBasicEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_basic_endpoint_with_options(request, runtime)

    def delete_basic_endpoint_group_with_options(self, request, runtime):
        """
        **DeleteBasicEndpointGroup** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [GetBasicEndpointGroup](~~362984~~) operation to query the state of an endpoint group.
        *   If the endpoint group is in the **deleting** state, it indicates that the endpoint group is being deleted. In this case, you can perform only query operations.
        *   If the endpoint group cannot be queried, it indicates that the endpoint group is deleted.
        *   The **DeleteBasicEndpointGroup** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: DeleteBasicEndpointGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBasicEndpointGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBasicEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_basic_endpoint_group(self, request):
        """
        **DeleteBasicEndpointGroup** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [GetBasicEndpointGroup](~~362984~~) operation to query the state of an endpoint group.
        *   If the endpoint group is in the **deleting** state, it indicates that the endpoint group is being deleted. In this case, you can perform only query operations.
        *   If the endpoint group cannot be queried, it indicates that the endpoint group is deleted.
        *   The **DeleteBasicEndpointGroup** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: DeleteBasicEndpointGroupRequest

        @return: DeleteBasicEndpointGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_basic_endpoint_group_with_options(request, runtime)

    def delete_basic_ip_set_with_options(self, request, runtime):
        """
        \\*\\*DeleteBasicIpSet\\*\\* is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [GetBasicIpSet](~~362987~~) operation to query the status of an acceleration region:
        *   If the acceleration region is in the **deleting** state, it indicates that the acceleration region is being deleted. In this case, you can perform only query operations.
        *   If the information of the acceleration region is not displayed in the response, it indicates that the acceleration region is deleted.
        *   The \\*\\*DeleteBasicIpSet\\*\\* operation cannot be called repeatedly for the same basic GA instance within a specific period of time.
        

        @param request: DeleteBasicIpSetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteBasicIpSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBasicIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_basic_ip_set(self, request):
        """
        \\*\\*DeleteBasicIpSet\\*\\* is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [GetBasicIpSet](~~362987~~) operation to query the status of an acceleration region:
        *   If the acceleration region is in the **deleting** state, it indicates that the acceleration region is being deleted. In this case, you can perform only query operations.
        *   If the information of the acceleration region is not displayed in the response, it indicates that the acceleration region is deleted.
        *   The \\*\\*DeleteBasicIpSet\\*\\* operation cannot be called repeatedly for the same basic GA instance within a specific period of time.
        

        @param request: DeleteBasicIpSetRequest

        @return: DeleteBasicIpSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_basic_ip_set_with_options(request, runtime)

    def delete_custom_routing_endpoint_group_destinations_with_options(self, request, runtime):
        """
        **DeleteCustomRoutingEndpointGroupDestinations** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) to query the status of the task.
        *   If the endpoint group is in the **updating** state, it indicates that mappings are being deleted from the endpoint group. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state and no information about the mappings that you want to delete is found in the response when you call the [DescribeCustomRoutingEndpointGroupDestinations](~~449378~~) operation, it indicates the mappings are deleted from the endpoint group.
        *   You cannot call the **DeleteCustomRoutingEndpointGroupDestinations** operation again on the same Global Accelerator (GA) instance before the previous request is completed.
        

        @param request: DeleteCustomRoutingEndpointGroupDestinationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCustomRoutingEndpointGroupDestinationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_ids):
            query['DestinationIds'] = request.destination_ids
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomRoutingEndpointGroupDestinations',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteCustomRoutingEndpointGroupDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_routing_endpoint_group_destinations(self, request):
        """
        **DeleteCustomRoutingEndpointGroupDestinations** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) to query the status of the task.
        *   If the endpoint group is in the **updating** state, it indicates that mappings are being deleted from the endpoint group. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state and no information about the mappings that you want to delete is found in the response when you call the [DescribeCustomRoutingEndpointGroupDestinations](~~449378~~) operation, it indicates the mappings are deleted from the endpoint group.
        *   You cannot call the **DeleteCustomRoutingEndpointGroupDestinations** operation again on the same Global Accelerator (GA) instance before the previous request is completed.
        

        @param request: DeleteCustomRoutingEndpointGroupDestinationsRequest

        @return: DeleteCustomRoutingEndpointGroupDestinationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_routing_endpoint_group_destinations_with_options(request, runtime)

    def delete_custom_routing_endpoint_groups_with_options(self, request, runtime):
        """
        **DeleteCustomRoutingEndpointGroups** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the state of the endpoint groups associated with a custom routing listener that you attempt to delete.
        *   If the endpoint groups are in the **deleting** state, the endpoint groups are being deleted. In this case, you can perform only query operations.
        *   If the endpoint groups cannot be queried, the endpoint groups are deleted.
        *   You cannot use the **DeleteCustomRoutingEndpointGroups** operation on the same Global Accelerator (GA) instance before the previous operation is complete.
        

        @param request: DeleteCustomRoutingEndpointGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCustomRoutingEndpointGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomRoutingEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteCustomRoutingEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_routing_endpoint_groups(self, request):
        """
        **DeleteCustomRoutingEndpointGroups** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the state of the endpoint groups associated with a custom routing listener that you attempt to delete.
        *   If the endpoint groups are in the **deleting** state, the endpoint groups are being deleted. In this case, you can perform only query operations.
        *   If the endpoint groups cannot be queried, the endpoint groups are deleted.
        *   You cannot use the **DeleteCustomRoutingEndpointGroups** operation on the same Global Accelerator (GA) instance before the previous operation is complete.
        

        @param request: DeleteCustomRoutingEndpointGroupsRequest

        @return: DeleteCustomRoutingEndpointGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_routing_endpoint_groups_with_options(request, runtime)

    def delete_custom_routing_endpoint_traffic_policies_with_options(self, request, runtime):
        """
        **DeleteCustomRoutingEndpointTrafficPolicies** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the status of an endpoint group to check whether the traffic destinations are deleted.
        *   If the endpoint group is in the **updating** state, the traffic destinations are being deleted. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state and the traffic destinations that you want to delete cannot be queried by calling the [DescribeCustomRoutingEndPointTrafficPolicy](~~449392~~) operation, the traffic destinations are deleted.
        *   The **DeleteCustomRoutingEndpointTrafficPolicies** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteCustomRoutingEndpointTrafficPoliciesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCustomRoutingEndpointTrafficPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomRoutingEndpointTrafficPolicies',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteCustomRoutingEndpointTrafficPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_routing_endpoint_traffic_policies(self, request):
        """
        **DeleteCustomRoutingEndpointTrafficPolicies** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the status of an endpoint group to check whether the traffic destinations are deleted.
        *   If the endpoint group is in the **updating** state, the traffic destinations are being deleted. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state and the traffic destinations that you want to delete cannot be queried by calling the [DescribeCustomRoutingEndPointTrafficPolicy](~~449392~~) operation, the traffic destinations are deleted.
        *   The **DeleteCustomRoutingEndpointTrafficPolicies** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteCustomRoutingEndpointTrafficPoliciesRequest

        @return: DeleteCustomRoutingEndpointTrafficPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_routing_endpoint_traffic_policies_with_options(request, runtime)

    def delete_custom_routing_endpoints_with_options(self, request, runtime):
        """
        **DeleteCustomRoutingEndpoints** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) to query the status of the task.
        *   If an endpoint group is in the **updating** state, the endpoint is being deleted. In this case, you can perform only query operations.
        *   If an endpoint group is in the **active** state and the endpoint cannot be found after you call the [DescribeCustomRoutingEndpoint](~~449386~~) operation, the endpoint is deleted.
        *   You cannot call the **DeleteCustomRoutingEndpoints** operation again on the same Global Accelerator (GA) instance before the previous task is completed.
        

        @param request: DeleteCustomRoutingEndpointsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCustomRoutingEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomRoutingEndpoints',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteCustomRoutingEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_routing_endpoints(self, request):
        """
        **DeleteCustomRoutingEndpoints** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) to query the status of the task.
        *   If an endpoint group is in the **updating** state, the endpoint is being deleted. In this case, you can perform only query operations.
        *   If an endpoint group is in the **active** state and the endpoint cannot be found after you call the [DescribeCustomRoutingEndpoint](~~449386~~) operation, the endpoint is deleted.
        *   You cannot call the **DeleteCustomRoutingEndpoints** operation again on the same Global Accelerator (GA) instance before the previous task is completed.
        

        @param request: DeleteCustomRoutingEndpointsRequest

        @return: DeleteCustomRoutingEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_routing_endpoints_with_options(request, runtime)

    def delete_domain_accelerator_relation_with_options(self, request, runtime):
        """
        You cannot call the *DeleteDomainAcceleratorRelation** operation again by using the same Alibaba Cloud account before the previous operation is complete.
        

        @param request: DeleteDomainAcceleratorRelationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDomainAcceleratorRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_ids):
            query['AcceleratorIds'] = request.accelerator_ids
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainAcceleratorRelation',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteDomainAcceleratorRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain_accelerator_relation(self, request):
        """
        You cannot call the *DeleteDomainAcceleratorRelation** operation again by using the same Alibaba Cloud account before the previous operation is complete.
        

        @param request: DeleteDomainAcceleratorRelationRequest

        @return: DeleteDomainAcceleratorRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_accelerator_relation_with_options(request, runtime)

    def delete_endpoint_group_with_options(self, request, runtime):
        """
        **DeleteEndpointGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the status of the endpoint group.
        *   If the endpoint group is in the **deleting** state, it indicates that the endpoint group is being deleted. In this case, you can perform only query operations.
        *   If the endpoint group cannot be queried, it indicates that the endpoint group is deleted.
        *   The **DeleteEndpointGroup** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: DeleteEndpointGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteEndpointGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_endpoint_group(self, request):
        """
        **DeleteEndpointGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the status of the endpoint group.
        *   If the endpoint group is in the **deleting** state, it indicates that the endpoint group is being deleted. In this case, you can perform only query operations.
        *   If the endpoint group cannot be queried, it indicates that the endpoint group is deleted.
        *   The **DeleteEndpointGroup** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: DeleteEndpointGroupRequest

        @return: DeleteEndpointGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_endpoint_group_with_options(request, runtime)

    def delete_endpoint_groups_with_options(self, request, runtime):
        """
        **DeleteEndpointGroups** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the status of the task.
        *   If an endpoint group is in the **deleting** state, the endpoint group is being deleted. In this case, you can perform only query operations.
        *   If an endpoint group cannot be queried, the endpoint group is deleted.
        *   The **DeleteEndpointGroups** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteEndpointGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteEndpointGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_endpoint_groups(self, request):
        """
        **DeleteEndpointGroups** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the status of the task.
        *   If an endpoint group is in the **deleting** state, the endpoint group is being deleted. In this case, you can perform only query operations.
        *   If an endpoint group cannot be queried, the endpoint group is deleted.
        *   The **DeleteEndpointGroups** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteEndpointGroupsRequest

        @return: DeleteEndpointGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_endpoint_groups_with_options(request, runtime)

    def delete_forwarding_rules_with_options(self, request, runtime):
        """
        **DeleteForwardingRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListForwardingRules](~~205817~~) operation to query the status of the task.
        *   If a forwarding rule is in the **deleting** state, the forwarding rule is being deleted. In this case, you can perform only query operations.
        *   If a forwarding rule cannot be queried, the forwarding rule is deleted.
        *   The **DeleteForwardingRules** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteForwardingRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteForwardingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.forwarding_rule_ids):
            query['ForwardingRuleIds'] = request.forwarding_rule_ids
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteForwardingRules',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_forwarding_rules(self, request):
        """
        **DeleteForwardingRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListForwardingRules](~~205817~~) operation to query the status of the task.
        *   If a forwarding rule is in the **deleting** state, the forwarding rule is being deleted. In this case, you can perform only query operations.
        *   If a forwarding rule cannot be queried, the forwarding rule is deleted.
        *   The **DeleteForwardingRules** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteForwardingRulesRequest

        @return: DeleteForwardingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_forwarding_rules_with_options(request, runtime)

    def delete_ip_set_with_options(self, request, runtime):
        """
        **DeleteIpSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeIpSet](~~153246~~) operation to query the status of an acceleration region.
        *   If the acceleration region is in the **deleting** state, it indicates that the acceleration region is being deleted. In this case, you can perform only query operations.
        *   If the acceleration region cannot be queried, it indicates that the acceleration region is deleted.
        *   The **DeleteIpSet** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: DeleteIpSetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteIpSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ip_set(self, request):
        """
        **DeleteIpSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeIpSet](~~153246~~) operation to query the status of an acceleration region.
        *   If the acceleration region is in the **deleting** state, it indicates that the acceleration region is being deleted. In this case, you can perform only query operations.
        *   If the acceleration region cannot be queried, it indicates that the acceleration region is deleted.
        *   The **DeleteIpSet** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: DeleteIpSetRequest

        @return: DeleteIpSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_set_with_options(request, runtime)

    def delete_ip_sets_with_options(self, request, runtime):
        """
        **DeleteIpSets** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeIpSet](~~153246~~) operation to query the state of an acceleration region.
        *   If the acceleration region is in the **deleting** state, the acceleration region is being deleted. In this case, you can perform only query operations.
        *   If the acceleration region cannot be queried, the acceleration region is deleted.
        *   The **DeleteIpSets** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteIpSetsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteIpSetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_set_ids):
            query['IpSetIds'] = request.ip_set_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpSets',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ip_sets(self, request):
        """
        **DeleteIpSets** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeIpSet](~~153246~~) operation to query the state of an acceleration region.
        *   If the acceleration region is in the **deleting** state, the acceleration region is being deleted. In this case, you can perform only query operations.
        *   If the acceleration region cannot be queried, the acceleration region is deleted.
        *   The **DeleteIpSets** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteIpSetsRequest

        @return: DeleteIpSetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_sets_with_options(request, runtime)

    def delete_listener_with_options(self, request, runtime):
        """
        **DeleteListener** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeListener](~~153254~~) operation to query the state of the listener.
        *   If the listener is in the **deleting** state, it indicates that the listener is being deleted. In this case, you can continue to perform query operations on the listener.
        *   If the listener cannot be queried, it indicates that the listener is deleted.
        *   The **DeleteListener** operation cannot be repeatedly called to delete listeners for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_listener(self, request):
        """
        **DeleteListener** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeListener](~~153254~~) operation to query the state of the listener.
        *   If the listener is in the **deleting** state, it indicates that the listener is being deleted. In this case, you can continue to perform query operations on the listener.
        *   If the listener cannot be queried, it indicates that the listener is deleted.
        *   The **DeleteListener** operation cannot be repeatedly called to delete listeners for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DeleteListenerRequest

        @return: DeleteListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_listener_with_options(request, runtime)

    def delete_spare_ips_with_options(self, request, runtime):
        """
        **DeleteSpareIps** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) operation to query the status of a GA instance.
        *   If the GA instance is in the **configuring** state, it indicates that the secondary IP addresses for the CNAME are being deleted. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state and the secondary IP addresses for the CNAME cannot be queried by calling the [ListSpareIps](~~262121~~) operation, it indicates that the IP addresses are deleted.
        *   The **DeleteSpareIps** operation holds an exclusive lock on the GA instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: DeleteSpareIpsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSpareIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spare_ips):
            query['SpareIps'] = request.spare_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSpareIps',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DeleteSpareIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_spare_ips(self, request):
        """
        **DeleteSpareIps** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) operation to query the status of a GA instance.
        *   If the GA instance is in the **configuring** state, it indicates that the secondary IP addresses for the CNAME are being deleted. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state and the secondary IP addresses for the CNAME cannot be queried by calling the [ListSpareIps](~~262121~~) operation, it indicates that the IP addresses are deleted.
        *   The **DeleteSpareIps** operation holds an exclusive lock on the GA instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: DeleteSpareIpsRequest

        @return: DeleteSpareIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_spare_ips_with_options(request, runtime)

    def describe_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accelerator_with_options(request, runtime)

    def describe_accelerator_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAcceleratorAutoRenewAttribute',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeAcceleratorAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_accelerator_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accelerator_auto_renew_attribute_with_options(request, runtime)

    def describe_accelerator_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAcceleratorServiceStatus',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeAcceleratorServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_accelerator_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accelerator_service_status_with_options(request, runtime)

    def describe_application_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationMonitor',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_application_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_application_monitor_with_options(request, runtime)

    def describe_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBandwidthPackage',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_package_with_options(request, runtime)

    def describe_bandwidth_package_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBandwidthPackageAutoRenewAttribute',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeBandwidthPackageAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_bandwidth_package_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_package_auto_renew_attribute_with_options(request, runtime)

    def describe_commodity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommodity',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_commodity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_commodity_with_options(request, runtime)

    def describe_commodity_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.orders):
            query['Orders'] = request.orders
        if not UtilClient.is_unset(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommodityPrice',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeCommodityPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_commodity_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_commodity_price_with_options(request, runtime)

    def describe_custom_routing_end_point_traffic_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomRoutingEndPointTrafficPolicy',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeCustomRoutingEndPointTrafficPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_routing_end_point_traffic_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_routing_end_point_traffic_policy_with_options(request, runtime)

    def describe_custom_routing_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_group):
            query['EndpointGroup'] = request.endpoint_group
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomRoutingEndpoint',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeCustomRoutingEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_routing_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_routing_endpoint_with_options(request, runtime)

    def describe_custom_routing_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomRoutingEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeCustomRoutingEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_routing_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_routing_endpoint_group_with_options(request, runtime)

    def describe_custom_routing_endpoint_group_destinations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_id):
            query['DestinationId'] = request.destination_id
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomRoutingEndpointGroupDestinations',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeCustomRoutingEndpointGroupDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_custom_routing_endpoint_group_destinations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_routing_endpoint_group_destinations_with_options(request, runtime)

    def describe_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoint_group_with_options(request, runtime)

    def describe_ip_set_with_options(self, request, runtime):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Ga\\&api=DescribeIpSet\\&type=RPC\\&version=2019-11-20)
        

        @param request: DescribeIpSetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeIpSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ip_set(self, request):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Ga\\&api=DescribeIpSet\\&type=RPC\\&version=2019-11-20)
        

        @param request: DescribeIpSetRequest

        @return: DescribeIpSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_set_with_options(request, runtime)

    def describe_listener_with_options(self, request, runtime):
        """
        This operation is used to query configuration information about a specified listener of a GA instance. The information includes the routing type of the listener, the state of the listener, the timestamp that indicates when the listener was created, and the listener ports.
        

        @param request: DescribeListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_listener(self, request):
        """
        This operation is used to query configuration information about a specified listener of a GA instance. The information includes the routing type of the listener, the state of the listener, the timestamp that indicates when the listener was created, and the listener ports.
        

        @param request: DescribeListenerRequest

        @return: DescribeListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_listener_with_options(request, runtime)

    def describe_log_store_of_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreOfEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeLogStoreOfEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_log_store_of_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_of_endpoint_group_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def detach_ddos_from_accelerator_with_options(self, request, runtime):
        """
        The **DetachDdosFromAccelerator** operation is asynchronous. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) or [ListAccelerators](~~153236~~) operation to query the status of the GA instance.
        *   If the GA instance is in the **configuring** state, the Anti-DDoS Pro/Premium instance is being disassociated from the GA instance. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, the Anti-DDoS Pro/Premium instance is disassociated from the GA instance.
        *   **DetachDdosFromAccelerator** cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: DetachDdosFromAcceleratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DetachDdosFromAcceleratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDdosFromAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DetachDdosFromAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_ddos_from_accelerator(self, request):
        """
        The **DetachDdosFromAccelerator** operation is asynchronous. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) or [ListAccelerators](~~153236~~) operation to query the status of the GA instance.
        *   If the GA instance is in the **configuring** state, the Anti-DDoS Pro/Premium instance is being disassociated from the GA instance. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, the Anti-DDoS Pro/Premium instance is disassociated from the GA instance.
        *   **DetachDdosFromAccelerator** cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: DetachDdosFromAcceleratorRequest

        @return: DetachDdosFromAcceleratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_ddos_from_accelerator_with_options(request, runtime)

    def detach_log_store_from_endpoint_group_with_options(self, request, runtime):
        """
        ## Description
        *   **DetachLogStoreFromEndpointGroup** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the state of an endpoint group.
        *   If the endpoint group is in the **updating** state, the Log Service Logstore is being disassociated from the endpoint group. In this case, you can perform only query operations.
        <!---->
        *   If the endpoint group is in the **active** state, the Log Service Logstore is disassociated from the endpoint group.
        *   The **DetachLogStoreFromEndpointGroup** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DetachLogStoreFromEndpointGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DetachLogStoreFromEndpointGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachLogStoreFromEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DetachLogStoreFromEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_log_store_from_endpoint_group(self, request):
        """
        ## Description
        *   **DetachLogStoreFromEndpointGroup** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the state of an endpoint group.
        *   If the endpoint group is in the **updating** state, the Log Service Logstore is being disassociated from the endpoint group. In this case, you can perform only query operations.
        <!---->
        *   If the endpoint group is in the **active** state, the Log Service Logstore is disassociated from the endpoint group.
        *   The **DetachLogStoreFromEndpointGroup** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DetachLogStoreFromEndpointGroupRequest

        @return: DetachLogStoreFromEndpointGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_log_store_from_endpoint_group_with_options(request, runtime)

    def detect_application_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectApplicationMonitor',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DetectApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_application_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_application_monitor_with_options(request, runtime)

    def disable_application_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationMonitor',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DisableApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_application_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_application_monitor_with_options(request, runtime)

    def dissociate_acls_from_listener_with_options(self, request, runtime):
        """
        ## Description
        *   **DissociateAclsFromListener** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeListener](~~153254~~) operation to query the state of a listener:
        *   If the listener is in the **updating** state, ACLs are being disassociated from the listener. In this case, you can perform only query operations.
        *   If the listener is in the **active** state, ACLs are disassociated from the listener.
        *   The **DissociateAclsFromListener** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DissociateAclsFromListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DissociateAclsFromListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateAclsFromListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DissociateAclsFromListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def dissociate_acls_from_listener(self, request):
        """
        ## Description
        *   **DissociateAclsFromListener** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeListener](~~153254~~) operation to query the state of a listener:
        *   If the listener is in the **updating** state, ACLs are being disassociated from the listener. In this case, you can perform only query operations.
        *   If the listener is in the **active** state, ACLs are disassociated from the listener.
        *   The **DissociateAclsFromListener** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: DissociateAclsFromListenerRequest

        @return: DissociateAclsFromListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dissociate_acls_from_listener_with_options(request, runtime)

    def dissociate_additional_certificates_from_listener_with_options(self, request, runtime):
        """
        ## Description
        *   **DissociateAdditionalCertificatesFromListener** is an asynchronous operation. After you send a request, the system returns a request ID, but this operation is still being performed in the system background. You can call the [DescribeListener](~~153254~~) operation to query the state of an HTTPS listener.
        *   If the listener is in the **updating** state, it indicates that the additional certificate is being dissociated from the listener. In this case, you can perform only query operations.
        *   If the listener is in the **active** state, it indicates that the additional certificate is dissociated from the listener.
        *   The **DissociateAdditionalCertificatesFromListener** operation cannot be repeatedly called for the same Global Accelerator (GA) instance with a specific period of time.
        

        @param request: DissociateAdditionalCertificatesFromListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DissociateAdditionalCertificatesFromListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateAdditionalCertificatesFromListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.DissociateAdditionalCertificatesFromListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def dissociate_additional_certificates_from_listener(self, request):
        """
        ## Description
        *   **DissociateAdditionalCertificatesFromListener** is an asynchronous operation. After you send a request, the system returns a request ID, but this operation is still being performed in the system background. You can call the [DescribeListener](~~153254~~) operation to query the state of an HTTPS listener.
        *   If the listener is in the **updating** state, it indicates that the additional certificate is being dissociated from the listener. In this case, you can perform only query operations.
        *   If the listener is in the **active** state, it indicates that the additional certificate is dissociated from the listener.
        *   The **DissociateAdditionalCertificatesFromListener** operation cannot be repeatedly called for the same Global Accelerator (GA) instance with a specific period of time.
        

        @param request: DissociateAdditionalCertificatesFromListenerRequest

        @return: DissociateAdditionalCertificatesFromListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dissociate_additional_certificates_from_listener_with_options(request, runtime)

    def enable_application_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationMonitor',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.EnableApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_application_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_application_monitor_with_options(request, runtime)

    def get_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAcl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetAclResponse(),
            self.call_api(params, req, runtime)
        )

    def get_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_acl_with_options(request, runtime)

    def get_basic_accelerate_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBasicAccelerateIp',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetBasicAccelerateIpResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_accelerate_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_basic_accelerate_ip_with_options(request, runtime)

    def get_basic_accelerate_ip_endpoint_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBasicAccelerateIpEndpointRelation',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetBasicAccelerateIpEndpointRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_accelerate_ip_endpoint_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_basic_accelerate_ip_endpoint_relation_with_options(request, runtime)

    def get_basic_accelerate_ip_idle_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBasicAccelerateIpIdleCount',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetBasicAccelerateIpIdleCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_accelerate_ip_idle_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_basic_accelerate_ip_idle_count_with_options(request, runtime)

    def get_basic_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBasicAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_basic_accelerator_with_options(request, runtime)

    def get_basic_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBasicEndpoint',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetBasicEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_basic_endpoint_with_options(request, runtime)

    def get_basic_endpoint_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBasicEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_endpoint_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_basic_endpoint_group_with_options(request, runtime)

    def get_basic_ip_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBasicIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def get_basic_ip_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_basic_ip_set_with_options(request, runtime)

    def get_health_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHealthStatus',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_health_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_health_status_with_options(request, runtime)

    def get_invalid_domain_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInvalidDomainCount',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetInvalidDomainCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_invalid_domain_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_invalid_domain_count_with_options(request, runtime)

    def get_ipsets_bandwidth_limit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIpsetsBandwidthLimit',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetIpsetsBandwidthLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ipsets_bandwidth_limit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ipsets_bandwidth_limit_with_options(request, runtime)

    def get_spare_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spare_ip):
            query['SpareIp'] = request.spare_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpareIp',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.GetSpareIpResponse(),
            self.call_api(params, req, runtime)
        )

    def get_spare_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_spare_ip_with_options(request, runtime)

    def list_accelerate_areas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccelerateAreas',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAccelerateAreasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_accelerate_areas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accelerate_areas_with_options(request, runtime)

    def list_accelerators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccelerators',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAcceleratorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_accelerators(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accelerators_with_options(request, runtime)

    def list_acls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAcls',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAclsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_acls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_acls_with_options(request, runtime)

    def list_application_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationMonitor',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def list_application_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_application_monitor_with_options(request, runtime)

    def list_application_monitor_detect_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationMonitorDetectResult',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListApplicationMonitorDetectResultResponse(),
            self.call_api(params, req, runtime)
        )

    def list_application_monitor_detect_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_application_monitor_detect_result_with_options(request, runtime)

    def list_available_accelerate_areas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableAccelerateAreas',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAvailableAccelerateAreasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_available_accelerate_areas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_available_accelerate_areas_with_options(request, runtime)

    def list_available_busi_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableBusiRegions',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListAvailableBusiRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_available_busi_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_available_busi_regions_with_options(request, runtime)

    def list_bandwidth_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBandwidthPackages',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBandwidthPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bandwidth_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bandwidth_packages_with_options(request, runtime)

    def list_bandwidthackages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBandwidthackages',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBandwidthackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bandwidthackages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bandwidthackages_with_options(request, runtime)

    def list_basic_accelerate_ip_endpoint_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBasicAccelerateIpEndpointRelations',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBasicAccelerateIpEndpointRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_basic_accelerate_ip_endpoint_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_basic_accelerate_ip_endpoint_relations_with_options(request, runtime)

    def list_basic_accelerate_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerate_ip_address):
            query['AccelerateIpAddress'] = request.accelerate_ip_address
        if not UtilClient.is_unset(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBasicAccelerateIps',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBasicAccelerateIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_basic_accelerate_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_basic_accelerate_ips_with_options(request, runtime)

    def list_basic_accelerators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBasicAccelerators',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBasicAcceleratorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_basic_accelerators(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_basic_accelerators_with_options(request, runtime)

    def list_basic_endpoints_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBasicEndpoints',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBasicEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_basic_endpoints(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_basic_endpoints_with_options(request, runtime)

    def list_busi_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBusiRegions',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListBusiRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_busi_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_busi_regions_with_options(request, runtime)

    def list_common_areas_with_options(self, request, runtime):
        """
        You can call this operation to query the acceleration areas and regions that you can specify on the wizard page of Global Accelerator (GA) and for free-trial GA instances. You can filter acceleration areas and regions based on specified conditions.
        

        @param request: ListCommonAreasRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCommonAreasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.is_epg):
            query['IsEpg'] = request.is_epg
        if not UtilClient.is_unset(request.is_ip_set):
            query['IsIpSet'] = request.is_ip_set
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCommonAreas',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListCommonAreasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_common_areas(self, request):
        """
        You can call this operation to query the acceleration areas and regions that you can specify on the wizard page of Global Accelerator (GA) and for free-trial GA instances. You can filter acceleration areas and regions based on specified conditions.
        

        @param request: ListCommonAreasRequest

        @return: ListCommonAreasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_common_areas_with_options(request, runtime)

    def list_custom_routing_endpoint_group_destinations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.from_port):
            query['FromPort'] = request.from_port
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protocols):
            query['Protocols'] = request.protocols
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.to_port):
            query['ToPort'] = request.to_port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomRoutingEndpointGroupDestinations',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListCustomRoutingEndpointGroupDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_custom_routing_endpoint_group_destinations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_custom_routing_endpoint_group_destinations_with_options(request, runtime)

    def list_custom_routing_endpoint_groups_with_options(self, request, runtime):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code for different SDKs.](https://api.aliyun.com/#product=Ga\\&api=ListCustomRoutingEndpointGroups\\&type=RPC\\&version=2019-11-20)
        

        @param request: ListCustomRoutingEndpointGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCustomRoutingEndpointGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomRoutingEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListCustomRoutingEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_custom_routing_endpoint_groups(self, request):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code for different SDKs.](https://api.aliyun.com/#product=Ga\\&api=ListCustomRoutingEndpointGroups\\&type=RPC\\&version=2019-11-20)
        

        @param request: ListCustomRoutingEndpointGroupsRequest

        @return: ListCustomRoutingEndpointGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_routing_endpoint_groups_with_options(request, runtime)

    def list_custom_routing_endpoint_traffic_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomRoutingEndpointTrafficPolicies',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListCustomRoutingEndpointTrafficPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_custom_routing_endpoint_traffic_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_custom_routing_endpoint_traffic_policies_with_options(request, runtime)

    def list_custom_routing_endpoints_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomRoutingEndpoints',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListCustomRoutingEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_custom_routing_endpoints(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_custom_routing_endpoints_with_options(request, runtime)

    def list_custom_routing_port_mappings_with_options(self, request, runtime):
        """
        After you configure a custom routing listener for a Global Accelerator (GA) instance, the instance generates a port mapping table based on the listener port range, backend service protocols and port ranges of the associated endpoint groups, and IP addresses of endpoints (vSwitches). The custom routing listener forwards client requests to specified IP addresses and ports in the vSwitches based on the port mapping table. This operation is used to query the generated port mapping table.
        

        @param request: ListCustomRoutingPortMappingsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCustomRoutingPortMappingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomRoutingPortMappings',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListCustomRoutingPortMappingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_custom_routing_port_mappings(self, request):
        """
        After you configure a custom routing listener for a Global Accelerator (GA) instance, the instance generates a port mapping table based on the listener port range, backend service protocols and port ranges of the associated endpoint groups, and IP addresses of endpoints (vSwitches). The custom routing listener forwards client requests to specified IP addresses and ports in the vSwitches based on the port mapping table. This operation is used to query the generated port mapping table.
        

        @param request: ListCustomRoutingPortMappingsRequest

        @return: ListCustomRoutingPortMappingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_routing_port_mappings_with_options(request, runtime)

    def list_custom_routing_port_mappings_by_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_address):
            query['DestinationAddress'] = request.destination_address
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomRoutingPortMappingsByDestination',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListCustomRoutingPortMappingsByDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_custom_routing_port_mappings_by_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_custom_routing_port_mappings_by_destination_with_options(request, runtime)

    def list_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_domains_with_options(request, runtime)

    def list_endpoint_group_ip_address_cidr_blocks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEndpointGroupIpAddressCidrBlocks',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListEndpointGroupIpAddressCidrBlocksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_endpoint_group_ip_address_cidr_blocks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_endpoint_group_ip_address_cidr_blocks_with_options(request, runtime)

    def list_endpoint_groups_with_options(self, request, runtime):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Ga\\&api=ListEndpointGroups\\&type=RPC\\&version=2019-11-20)
        

        @param request: ListEndpointGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListEndpointGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.access_log_switch):
            query['AccessLogSwitch'] = request.access_log_switch
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoint_group_type):
            query['EndpointGroupType'] = request.endpoint_group_type
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_endpoint_groups(self, request):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Ga\\&api=ListEndpointGroups\\&type=RPC\\&version=2019-11-20)
        

        @param request: ListEndpointGroupsRequest

        @return: ListEndpointGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_endpoint_groups_with_options(request, runtime)

    def list_forwarding_rules_with_options(self, request, runtime):
        """
        >  This operation is used to query only custom forwarding rules, not the default forwarding rule.
        

        @param request: ListForwardingRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListForwardingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.forwarding_rule_id):
            query['ForwardingRuleId'] = request.forwarding_rule_id
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListForwardingRules',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_forwarding_rules(self, request):
        """
        >  This operation is used to query only custom forwarding rules, not the default forwarding rule.
        

        @param request: ListForwardingRulesRequest

        @return: ListForwardingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_forwarding_rules_with_options(request, runtime)

    def list_ip_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpSets',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ip_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ip_sets_with_options(request, runtime)

    def list_isp_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not UtilClient.is_unset(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIspTypes',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListIspTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_isp_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_isp_types_with_options(request, runtime)

    def list_listener_certificates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListenerCertificates',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListListenerCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_listener_certificates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_listener_certificates_with_options(request, runtime)

    def list_listeners_with_options(self, request, runtime):
        """
        This operation is used to query information about the listeners of a GA instance, including the state of each listener, the timestamp that indicates when each listener was created, and the listener ports.
        

        @param request: ListListenersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListListenersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListeners',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListListenersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_listeners(self, request):
        """
        This operation is used to query information about the listeners of a GA instance, including the state of each listener, the timestamp that indicates when each listener was created, and the listener ports.
        

        @param request: ListListenersRequest

        @return: ListListenersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_with_options(request, runtime)

    def list_spare_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSpareIps',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListSpareIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_spare_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_spare_ips_with_options(request, runtime)

    def list_system_security_policies_with_options(self, request, runtime):
        """
        You can select a TLS security policy when you create an HTTPS listener. This API operation is used to query the TLS security policies that are supported by HTTPS listeners.
        

        @param request: ListSystemSecurityPoliciesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSystemSecurityPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSystemSecurityPolicies',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListSystemSecurityPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_system_security_policies(self, request):
        """
        You can select a TLS security policy when you create an HTTPS listener. This API operation is used to query the TLS security policies that are supported by HTTPS listeners.
        

        @param request: ListSystemSecurityPoliciesRequest

        @return: ListSystemSecurityPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_system_security_policies_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        You must specify **ResourceId.N** or **Tag.N** in the request to specify the object that you want to query.********\
        *   **Tag.N** is a resource tag that consists of a key-value pair (Tag.N.Key and Tag.N.Value). If you specify only **Tag.N.Key**, all tag values that are associated with the specified tag key are returned. If you specify only **Tag.N.Value**, an error message is returned.
        *   If you specify **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        *   If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        You must specify **ResourceId.N** or **Tag.N** in the request to specify the object that you want to query.********\
        *   **Tag.N** is a resource tag that consists of a key-value pair (Tag.N.Key and Tag.N.Value). If you specify only **Tag.N.Key**, all tag values that are associated with the specified tag key are returned. If you specify only **Tag.N.Value**, an error message is returned.
        *   If you specify **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        *   If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def open_accelerator_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenAcceleratorService',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.OpenAcceleratorServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_accelerator_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_accelerator_service_with_options(request, runtime)

    def query_cross_border_approval_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCrossBorderApprovalStatus',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.QueryCrossBorderApprovalStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cross_border_approval_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cross_border_approval_status_with_options(request, runtime)

    def remove_entries_from_acl_with_options(self, request, runtime):
        """
        **RemoveEntriesFromAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetAcl](~~258292~~) or [ListAcls](~~258291~~) operation to query the status of the ACL from which you want to delete IP entries.
        *   If the ACL is in the **configuring** state, it indicates that the IP entries are being deleted. In this case, you can perform only query operations.
        *   If the ACL is in the **active** state, it indicates that the IP entries are deleted.
        *   The **RemoveEntriesFromAcl** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: RemoveEntriesFromAclRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveEntriesFromAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveEntriesFromAcl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.RemoveEntriesFromAclResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_entries_from_acl(self, request):
        """
        **RemoveEntriesFromAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetAcl](~~258292~~) or [ListAcls](~~258291~~) operation to query the status of the ACL from which you want to delete IP entries.
        *   If the ACL is in the **configuring** state, it indicates that the IP entries are being deleted. In this case, you can perform only query operations.
        *   If the ACL is in the **active** state, it indicates that the IP entries are deleted.
        *   The **RemoveEntriesFromAcl** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: RemoveEntriesFromAclRequest

        @return: RemoveEntriesFromAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_entries_from_acl_with_options(request, runtime)

    def replace_bandwidth_package_with_options(self, request, runtime):
        """
        When you call this operation, take note of the following items:
        *   The GA instance continues to forward network traffic.
        *   **ReplaceBandwidthPackage** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) or [ListAccelerators](~~153236~~) operation to query the status of the GA instance.
        *   If the GA instance is in the **configuring** state, it indicates that the associated bandwidth plan is being replaced. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, it indicates that the associated bandwidth plan is replaced.
        *   The **ReplaceBandwidthPackage** operation holds an exclusive lock on the GA instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: ReplaceBandwidthPackageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReplaceBandwidthPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_bandwidth_package_id):
            query['TargetBandwidthPackageId'] = request.target_bandwidth_package_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceBandwidthPackage',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.ReplaceBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def replace_bandwidth_package(self, request):
        """
        When you call this operation, take note of the following items:
        *   The GA instance continues to forward network traffic.
        *   **ReplaceBandwidthPackage** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) or [ListAccelerators](~~153236~~) operation to query the status of the GA instance.
        *   If the GA instance is in the **configuring** state, it indicates that the associated bandwidth plan is being replaced. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, it indicates that the associated bandwidth plan is replaced.
        *   The **ReplaceBandwidthPackage** operation holds an exclusive lock on the GA instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: ReplaceBandwidthPackageRequest

        @return: ReplaceBandwidthPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.replace_bandwidth_package_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        ### Description
        You can add up to 20 tags to each GA resource. When you call this operation, Alibaba Cloud first checks the number of existing tags attached to the resource. If the quota is reached, an error message is returned.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        ### Description
        You can add up to 20 tags to each GA resource. When you call this operation, Alibaba Cloud first checks the number of existing tags attached to the resource. If the quota is reached, an error message is returned.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_accelerator_with_options(self, request, runtime):
        """
        **UpdateAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) operation to query the status of a GA instance.
        *   If the GA instance is in the **configuring** state, the GA instance is being modified. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, the GA instance is modified.
        *   The **UpdateAccelerator** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: UpdateAcceleratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAcceleratorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_accelerator(self, request):
        """
        **UpdateAccelerator** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) operation to query the status of a GA instance.
        *   If the GA instance is in the **configuring** state, the GA instance is being modified. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, the GA instance is modified.
        *   The **UpdateAccelerator** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: UpdateAcceleratorRequest

        @return: UpdateAcceleratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_accelerator_with_options(request, runtime)

    def update_accelerator_auto_renew_attribute_with_options(self, request, runtime):
        """
        The *UpdateAcceleratorAutoRenewAttribute** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: UpdateAcceleratorAutoRenewAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAcceleratorAutoRenewAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAcceleratorAutoRenewAttribute',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAcceleratorAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_accelerator_auto_renew_attribute(self, request):
        """
        The *UpdateAcceleratorAutoRenewAttribute** operation cannot be repeatedly called for the same GA instance within a specific period of time.
        

        @param request: UpdateAcceleratorAutoRenewAttributeRequest

        @return: UpdateAcceleratorAutoRenewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_accelerator_auto_renew_attribute_with_options(request, runtime)

    def update_accelerator_confirm_with_options(self, request, runtime):
        """
        After you modify the specification of a GA instance, you must confirm the modification. The *UpdateAcceleratorConfirm** operation is used to confirm the specification of a GA instance that is modified. When you call this operation to confirm the specification of a GA instance, take note of the following items:
        *   **UpdateAcceleratorConfirm** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) operation to query the status of a GA instance.
        *   If the GA instance is in the **configuring** state, it indicates that the specification of the instance is being modified. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, it indicates that the specification of the instance is modified.
        *   The **UpdateAcceleratorConfirm** operation cannot be called repeatedly for the same GA instance within a specific period of time.
        

        @param request: UpdateAcceleratorConfirmRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAcceleratorConfirmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAcceleratorConfirm',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAcceleratorConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    def update_accelerator_confirm(self, request):
        """
        After you modify the specification of a GA instance, you must confirm the modification. The *UpdateAcceleratorConfirm** operation is used to confirm the specification of a GA instance that is modified. When you call this operation to confirm the specification of a GA instance, take note of the following items:
        *   **UpdateAcceleratorConfirm** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) operation to query the status of a GA instance.
        *   If the GA instance is in the **configuring** state, it indicates that the specification of the instance is being modified. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, it indicates that the specification of the instance is modified.
        *   The **UpdateAcceleratorConfirm** operation cannot be called repeatedly for the same GA instance within a specific period of time.
        

        @param request: UpdateAcceleratorConfirmRequest

        @return: UpdateAcceleratorConfirmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_accelerator_confirm_with_options(request, runtime)

    def update_accelerator_cross_border_mode_with_options(self, request, runtime):
        """
        ### Prerequisites
        You can call this operation to change the type of transmission network for a **standard** GA instance whose bandwidth metering method is **pay-by-data-transfer**. Before you call this operation, make sure that the following requirements are met:
        *   Cloud Data Transfer (CDT) is activated. When you call the [CreateAccelerator](~~206786~~) operation and set **BandwidthBillingType** to **CDT** to create a **standard** GA instance whose bandwidth metering method is **pay-by-data-transfer**, CDT is automatically activated. The data transfer fees are managed by CDT.
        *   If you want to set **CrossBorderMode** to **private**, which specifies cross-border Express Connect circuit as the type of transmission network, make sure that your enterprise account completed real-name verification. For more information, see [Real-name verification](~~52595~~).
        

        @param request: UpdateAcceleratorCrossBorderModeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAcceleratorCrossBorderModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_border_mode):
            query['CrossBorderMode'] = request.cross_border_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAcceleratorCrossBorderMode',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAcceleratorCrossBorderModeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_accelerator_cross_border_mode(self, request):
        """
        ### Prerequisites
        You can call this operation to change the type of transmission network for a **standard** GA instance whose bandwidth metering method is **pay-by-data-transfer**. Before you call this operation, make sure that the following requirements are met:
        *   Cloud Data Transfer (CDT) is activated. When you call the [CreateAccelerator](~~206786~~) operation and set **BandwidthBillingType** to **CDT** to create a **standard** GA instance whose bandwidth metering method is **pay-by-data-transfer**, CDT is automatically activated. The data transfer fees are managed by CDT.
        *   If you want to set **CrossBorderMode** to **private**, which specifies cross-border Express Connect circuit as the type of transmission network, make sure that your enterprise account completed real-name verification. For more information, see [Real-name verification](~~52595~~).
        

        @param request: UpdateAcceleratorCrossBorderModeRequest

        @return: UpdateAcceleratorCrossBorderModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_accelerator_cross_border_mode_with_options(request, runtime)

    def update_accelerator_cross_border_status_with_options(self, request, runtime):
        """
        You can use this operation to enable or disable the cross-border data transmission feature for a GA instance. Before you enable the cross-border data transmission feature, make sure that the following requirements are met:
        - **Basic GA instances**:
        Cloud Data Transfer (CDT) is activated. When you call the CreateBasicAccelerator operation to create a basic GA instance, set BandwidthBillingType to CDT. Then, the system automatically activates CDT. The data transfer fees are managed by CDT.
        If you want to enable the cross-border data transmission feature, make sure that the current account has completed enterprise real-name registration. For more information, see Real-name registration FAQs.
        - **Standard GA instances**:
        CDT is activated. When you call the CreateAccelerator operation to create a standard GA instance, set BandwidthBillingType to CDT. Then, the system automatically activates CDT. The data transfer fees are managed by CDT.
        

        @param request: UpdateAcceleratorCrossBorderStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAcceleratorCrossBorderStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_border_status):
            query['CrossBorderStatus'] = request.cross_border_status
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAcceleratorCrossBorderStatus',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAcceleratorCrossBorderStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_accelerator_cross_border_status(self, request):
        """
        You can use this operation to enable or disable the cross-border data transmission feature for a GA instance. Before you enable the cross-border data transmission feature, make sure that the following requirements are met:
        - **Basic GA instances**:
        Cloud Data Transfer (CDT) is activated. When you call the CreateBasicAccelerator operation to create a basic GA instance, set BandwidthBillingType to CDT. Then, the system automatically activates CDT. The data transfer fees are managed by CDT.
        If you want to enable the cross-border data transmission feature, make sure that the current account has completed enterprise real-name registration. For more information, see Real-name registration FAQs.
        - **Standard GA instances**:
        CDT is activated. When you call the CreateAccelerator operation to create a standard GA instance, set BandwidthBillingType to CDT. Then, the system automatically activates CDT. The data transfer fees are managed by CDT.
        

        @param request: UpdateAcceleratorCrossBorderStatusRequest

        @return: UpdateAcceleratorCrossBorderStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_accelerator_cross_border_status_with_options(request, runtime)

    def update_acl_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAclAttribute',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAclAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_acl_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_acl_attribute_with_options(request, runtime)

    def update_additional_certificate_with_listener_with_options(self, request, runtime):
        """
        The UpdateAdditionalCertificateWithListener operation is used to replace an additional certificate. You can use this operation when you want to replace an expired additional certificate with a new additional certificate without changing the associated domain name.
        *   **UpdateAdditionalCertificateWithListener** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can use the [ListListenerCertificates](~~307743~~) operation to query the state of the additional certificate that is associated with an HTTP listener:
        *   If the certificate that you want to replace is in the **updating** state, it is being replaced for the HTTP listener. In this case, you can perform only query operations.
        *   If the replacement certificate is in the **active** state, it indicates that the replacement operation is complete and the replacement certificate is associated with the HTTP listener.
        *   You cannot perform the **UpdateAdditionalCertificateWithListener** operation again on the same Global Accelerator (GA) instance before the previous operation is complete.
        

        @param request: UpdateAdditionalCertificateWithListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAdditionalCertificateWithListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAdditionalCertificateWithListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateAdditionalCertificateWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_additional_certificate_with_listener(self, request):
        """
        The UpdateAdditionalCertificateWithListener operation is used to replace an additional certificate. You can use this operation when you want to replace an expired additional certificate with a new additional certificate without changing the associated domain name.
        *   **UpdateAdditionalCertificateWithListener** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can use the [ListListenerCertificates](~~307743~~) operation to query the state of the additional certificate that is associated with an HTTP listener:
        *   If the certificate that you want to replace is in the **updating** state, it is being replaced for the HTTP listener. In this case, you can perform only query operations.
        *   If the replacement certificate is in the **active** state, it indicates that the replacement operation is complete and the replacement certificate is associated with the HTTP listener.
        *   You cannot perform the **UpdateAdditionalCertificateWithListener** operation again on the same Global Accelerator (GA) instance before the previous operation is complete.
        

        @param request: UpdateAdditionalCertificateWithListenerRequest

        @return: UpdateAdditionalCertificateWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_additional_certificate_with_listener_with_options(request, runtime)

    def update_application_monitor_with_options(self, request, runtime):
        """
        *UpdateApplicationMonitor** is an asynchronous operation. After you send a request, the system returns a request ID, but this operation is still being performed in the system background. You can call the [DescribeApplicationMonitor](~~408463~~) or [ListApplicationMonitor](~~408462~~) operation to check whether the configurations of an origin probing task are modified.
        *   If the values of modified parameters remain unchanged, it indicates that the origin probing task is being modified. In this case, you can perform only query operations.
        *   If the values of modified parameters change, it indicates that the origin probing task is modified.
        

        @param request: UpdateApplicationMonitorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateApplicationMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.detect_enable):
            query['DetectEnable'] = request.detect_enable
        if not UtilClient.is_unset(request.detect_threshold):
            query['DetectThreshold'] = request.detect_threshold
        if not UtilClient.is_unset(request.detect_times):
            query['DetectTimes'] = request.detect_times
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.options_json):
            query['OptionsJson'] = request.options_json
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationMonitor',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_application_monitor(self, request):
        """
        *UpdateApplicationMonitor** is an asynchronous operation. After you send a request, the system returns a request ID, but this operation is still being performed in the system background. You can call the [DescribeApplicationMonitor](~~408463~~) or [ListApplicationMonitor](~~408462~~) operation to check whether the configurations of an origin probing task are modified.
        *   If the values of modified parameters remain unchanged, it indicates that the origin probing task is being modified. In this case, you can perform only query operations.
        *   If the values of modified parameters change, it indicates that the origin probing task is modified.
        

        @param request: UpdateApplicationMonitorRequest

        @return: UpdateApplicationMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_monitor_with_options(request, runtime)

    def update_bandwidth_packaga_auto_renew_attribute_with_options(self, request, runtime):
        """
        You cannot repeatedly call the *UpdateBandwidthPackagaAutoRenewAttribute** operation to modify the auto-renewal settings of a bandwidth plan.
        

        @param request: UpdateBandwidthPackagaAutoRenewAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateBandwidthPackagaAutoRenewAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBandwidthPackagaAutoRenewAttribute',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateBandwidthPackagaAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_bandwidth_packaga_auto_renew_attribute(self, request):
        """
        You cannot repeatedly call the *UpdateBandwidthPackagaAutoRenewAttribute** operation to modify the auto-renewal settings of a bandwidth plan.
        

        @param request: UpdateBandwidthPackagaAutoRenewAttributeRequest

        @return: UpdateBandwidthPackagaAutoRenewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_bandwidth_packaga_auto_renew_attribute_with_options(request, runtime)

    def update_bandwidth_package_with_options(self, request, runtime):
        """
        Take note of the following items:
        *   **UpdateBandwidthPackage** is a synchronous operation when you call the operation to modify the configuration excluding the bandwidth value of a bandwidth plan. The new configuration immediately takes effect after the operation is performed.
        *   **UpdateBandwidthPackage** is an asynchronous operation when you call the operation to modify the configuration including the bandwidth value of a bandwidth plan that is not associated with a Global Accelerator (GA) instance. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeBandwidthPackage](~~153241~~) operation to query the status of the task.
        *   If the parameter values of the bandwidth plan remain unchanged, the bandwidth plan is being modified. In this case, you can perform only query operations.
        *   If the parameter values of the bandwidth plan are changed, the bandwidth plan is modified.
        *   **UpdateBandwidthPackage** is an asynchronous operation when you call the operation to modify the configuration including the bandwidth value of a bandwidth plan that is associated with a GA instance. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) operation to query the status of the task.
        *   If the GA instance is in the **configuring** state, the bandwidth plan is being modified. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, the bandwidth plan is modified.
        *   You cannot repeatedly call the **UpdateBandwidthPackage** operation for the same bandwidth plan within a specific period of time.
        

        @param request: UpdateBandwidthPackageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateBandwidthPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBandwidthPackage',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def update_bandwidth_package(self, request):
        """
        Take note of the following items:
        *   **UpdateBandwidthPackage** is a synchronous operation when you call the operation to modify the configuration excluding the bandwidth value of a bandwidth plan. The new configuration immediately takes effect after the operation is performed.
        *   **UpdateBandwidthPackage** is an asynchronous operation when you call the operation to modify the configuration including the bandwidth value of a bandwidth plan that is not associated with a Global Accelerator (GA) instance. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeBandwidthPackage](~~153241~~) operation to query the status of the task.
        *   If the parameter values of the bandwidth plan remain unchanged, the bandwidth plan is being modified. In this case, you can perform only query operations.
        *   If the parameter values of the bandwidth plan are changed, the bandwidth plan is modified.
        *   **UpdateBandwidthPackage** is an asynchronous operation when you call the operation to modify the configuration including the bandwidth value of a bandwidth plan that is associated with a GA instance. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeAccelerator](~~153235~~) operation to query the status of the task.
        *   If the GA instance is in the **configuring** state, the bandwidth plan is being modified. In this case, you can perform only query operations.
        *   If the GA instance is in the **active** state, the bandwidth plan is modified.
        *   You cannot repeatedly call the **UpdateBandwidthPackage** operation for the same bandwidth plan within a specific period of time.
        

        @param request: UpdateBandwidthPackageRequest

        @return: UpdateBandwidthPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_bandwidth_package_with_options(request, runtime)

    def update_basic_accelerator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBasicAccelerator',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_basic_accelerator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_basic_accelerator_with_options(request, runtime)

    def update_basic_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBasicEndpoint',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateBasicEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def update_basic_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_basic_endpoint_with_options(request, runtime)

    def update_basic_endpoint_group_with_options(self, request, runtime):
        """
        **UpdateBasicEndpointGroup** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. After you call this operation to modify an endpoint group that is associated with a basic GA instance, the system deletes the endpoint group and creates another endpoint group in the background for the basic GA instance. You can call the [GetBasicAccelerator](~~353188~~) operation to query the state of the basic GA instance.
        *   If the basic GA instance is in the **configuring** state, it indicates that the configurations of the endpoint group are being modified. In this case, you can perform only query operations.
        *   If the basic GA instance is in the **active** state, it indicates that the configurations of the endpoint group are modified.
        *   The **UpdateBasicEndpointGroup** operation cannot be called repeatedly for the same basic GA instance within a specific period of time.
        

        @param request: UpdateBasicEndpointGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateBasicEndpointGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint_address):
            query['EndpointAddress'] = request.endpoint_address
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoint_sub_address):
            query['EndpointSubAddress'] = request.endpoint_sub_address
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBasicEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_basic_endpoint_group(self, request):
        """
        **UpdateBasicEndpointGroup** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. After you call this operation to modify an endpoint group that is associated with a basic GA instance, the system deletes the endpoint group and creates another endpoint group in the background for the basic GA instance. You can call the [GetBasicAccelerator](~~353188~~) operation to query the state of the basic GA instance.
        *   If the basic GA instance is in the **configuring** state, it indicates that the configurations of the endpoint group are being modified. In this case, you can perform only query operations.
        *   If the basic GA instance is in the **active** state, it indicates that the configurations of the endpoint group are modified.
        *   The **UpdateBasicEndpointGroup** operation cannot be called repeatedly for the same basic GA instance within a specific period of time.
        

        @param request: UpdateBasicEndpointGroupRequest

        @return: UpdateBasicEndpointGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_basic_endpoint_group_with_options(request, runtime)

    def update_basic_ip_set_with_options(self, request, runtime):
        """
        Before you call this operation, take note of the following limits:
        *   You can call this operation for only basic GA instances whose bandwidth is billed by Cloud Data Transfer (CDT).
        *   The **UpdateBasicIpSet** operation is asynchronous. After you send a request, the system returns a request ID, but the operation is still being performed in the background. You can call the [GetBasicIpSet](~~362987~~) operation to query the status of an acceleration region:
        *   If an acceleration region is in the **updating** state, the bandwidth of the acceleration region is being modified. In this state, you can perform only query operations.
        *   If an acceleration region is in the **active** state, the bandwidth of the acceleration region is modified.
        *   You cannot repeatedly call the **UpdateBasicIpSet** operation for the same basic GA instance within the specified period of time.
        

        @param request: UpdateBasicIpSetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateBasicIpSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBasicIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def update_basic_ip_set(self, request):
        """
        Before you call this operation, take note of the following limits:
        *   You can call this operation for only basic GA instances whose bandwidth is billed by Cloud Data Transfer (CDT).
        *   The **UpdateBasicIpSet** operation is asynchronous. After you send a request, the system returns a request ID, but the operation is still being performed in the background. You can call the [GetBasicIpSet](~~362987~~) operation to query the status of an acceleration region:
        *   If an acceleration region is in the **updating** state, the bandwidth of the acceleration region is being modified. In this state, you can perform only query operations.
        *   If an acceleration region is in the **active** state, the bandwidth of the acceleration region is modified.
        *   You cannot repeatedly call the **UpdateBasicIpSet** operation for the same basic GA instance within the specified period of time.
        

        @param request: UpdateBasicIpSetRequest

        @return: UpdateBasicIpSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_basic_ip_set_with_options(request, runtime)

    def update_custom_routing_endpoint_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomRoutingEndpointGroupAttribute',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateCustomRoutingEndpointGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_custom_routing_endpoint_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_custom_routing_endpoint_group_attribute_with_options(request, runtime)

    def update_custom_routing_endpoint_group_destinations_with_options(self, request, runtime):
        """
        **UpdateCustomRoutingEndpointGroupDestinations** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the status of an endpoint group associated with a custom routing listener to check whether the mapping configurations of the endpoint group are modified.
        *   If the endpoint group is in the **updating** state, the mapping configurations of the endpoint group are being modified. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, the mapping configurations of the endpoint group are modified.
        *   The **UpdateCustomRoutingEndpointGroupDestinations** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: UpdateCustomRoutingEndpointGroupDestinationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCustomRoutingEndpointGroupDestinationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.destination_configurations):
            query['DestinationConfigurations'] = request.destination_configurations
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomRoutingEndpointGroupDestinations',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateCustomRoutingEndpointGroupDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_custom_routing_endpoint_group_destinations(self, request):
        """
        **UpdateCustomRoutingEndpointGroupDestinations** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the status of an endpoint group associated with a custom routing listener to check whether the mapping configurations of the endpoint group are modified.
        *   If the endpoint group is in the **updating** state, the mapping configurations of the endpoint group are being modified. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, the mapping configurations of the endpoint group are modified.
        *   The **UpdateCustomRoutingEndpointGroupDestinations** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: UpdateCustomRoutingEndpointGroupDestinationsRequest

        @return: UpdateCustomRoutingEndpointGroupDestinationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_routing_endpoint_group_destinations_with_options(request, runtime)

    def update_custom_routing_endpoint_traffic_policies_with_options(self, request, runtime):
        """
        **UpdateCustomRoutingEndpointTrafficPolicies** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the status of the task.
        *   If the endpoint group is in the **updating** state, traffic policies are being modified for endpoints in the endpoint group. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, traffic policies are modified for endpoints in the endpoint group.
        *   The **UpdateCustomRoutingEndpointTrafficPolicies** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: UpdateCustomRoutingEndpointTrafficPoliciesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCustomRoutingEndpointTrafficPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not UtilClient.is_unset(request.policy_configurations):
            query['PolicyConfigurations'] = request.policy_configurations
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomRoutingEndpointTrafficPolicies',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateCustomRoutingEndpointTrafficPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_custom_routing_endpoint_traffic_policies(self, request):
        """
        **UpdateCustomRoutingEndpointTrafficPolicies** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the status of the task.
        *   If the endpoint group is in the **updating** state, traffic policies are being modified for endpoints in the endpoint group. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, traffic policies are modified for endpoints in the endpoint group.
        *   The **UpdateCustomRoutingEndpointTrafficPolicies** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: UpdateCustomRoutingEndpointTrafficPoliciesRequest

        @return: UpdateCustomRoutingEndpointTrafficPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_routing_endpoint_traffic_policies_with_options(request, runtime)

    def update_custom_routing_endpoints_with_options(self, request, runtime):
        """
        ## Description
        *   **UpdateCustomRoutingEndpoints** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the state of the endpoint groups associated with a custom routing listener to check whether the endpoints in the endpoint groups are modified.
        *   If an endpoint group is in the **updating** state, the endpoints in the endpoint group are being modified. In this case, you can perform only query operations.
        *   If an endpoint group is in the **active** state, the endpoints in the endpoint group are modified.
        *   The **UpdateCustomRoutingEndpoints** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: UpdateCustomRoutingEndpointsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCustomRoutingEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomRoutingEndpoints',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateCustomRoutingEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_custom_routing_endpoints(self, request):
        """
        ## Description
        *   **UpdateCustomRoutingEndpoints** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeCustomRoutingEndpointGroup](~~449373~~) operation to query the state of the endpoint groups associated with a custom routing listener to check whether the endpoints in the endpoint groups are modified.
        *   If an endpoint group is in the **updating** state, the endpoints in the endpoint group are being modified. In this case, you can perform only query operations.
        *   If an endpoint group is in the **active** state, the endpoints in the endpoint group are modified.
        *   The **UpdateCustomRoutingEndpoints** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: UpdateCustomRoutingEndpointsRequest

        @return: UpdateCustomRoutingEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_routing_endpoints_with_options(request, runtime)

    def update_domain_with_options(self, request, runtime):
        """
        You can call this operation to modify an accelerated domain name. If the new accelerated domain name is hosted in the Chinese mainland, you must obtain an Internet content provider (ICP) number for the domain name.
        You cannot call the **UpdateDomain** operation again by using the same Alibaba Cloud account before the previous request is completed.
        

        @param request: UpdateDomainRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_domain):
            query['TargetDomain'] = request.target_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomain',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def update_domain(self, request):
        """
        You can call this operation to modify an accelerated domain name. If the new accelerated domain name is hosted in the Chinese mainland, you must obtain an Internet content provider (ICP) number for the domain name.
        You cannot call the **UpdateDomain** operation again by using the same Alibaba Cloud account before the previous request is completed.
        

        @param request: UpdateDomainRequest

        @return: UpdateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_domain_with_options(request, runtime)

    def update_domain_state_with_options(self, request, runtime):
        """
        You can call this operation to query and update the ICP filing status of an accelerated domain name.
        The **UpdateDomainState** operation holds an exclusive lock on the GA instance. While the operation is in progress, you cannot call the same operation with the same Alibaba Cloud account.
        

        @param request: UpdateDomainStateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDomainStateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainState',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateDomainStateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_domain_state(self, request):
        """
        You can call this operation to query and update the ICP filing status of an accelerated domain name.
        The **UpdateDomainState** operation holds an exclusive lock on the GA instance. While the operation is in progress, you cannot call the same operation with the same Alibaba Cloud account.
        

        @param request: UpdateDomainStateRequest

        @return: UpdateDomainStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_domain_state_with_options(request, runtime)

    def update_endpoint_group_with_options(self, request, runtime):
        """
        **UpdateEndpointGroup** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the state of an endpoint group.
        *   If the endpoint group is in the **updating** state, it indicates that the configurations of the endpoint group are being modified. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, it indicates that the configurations of the endpoint group are modified.
        *   The **UpdateEndpointGroup** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: UpdateEndpointGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateEndpointGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not UtilClient.is_unset(request.endpoint_request_protocol):
            query['EndpointRequestProtocol'] = request.endpoint_request_protocol
        if not UtilClient.is_unset(request.health_check_enabled):
            query['HealthCheckEnabled'] = request.health_check_enabled
        if not UtilClient.is_unset(request.health_check_interval_seconds):
            query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
        if not UtilClient.is_unset(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not UtilClient.is_unset(request.health_check_port):
            query['HealthCheckPort'] = request.health_check_port
        if not UtilClient.is_unset(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.port_overrides):
            query['PortOverrides'] = request.port_overrides
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.threshold_count):
            query['ThresholdCount'] = request.threshold_count
        if not UtilClient.is_unset(request.traffic_percentage):
            query['TrafficPercentage'] = request.traffic_percentage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEndpointGroup',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_endpoint_group(self, request):
        """
        **UpdateEndpointGroup** is an asynchronous operation. After you send a request, the system returns a request ID, but the operation is still being performed in the system background. You can call the [DescribeEndpointGroup](~~153260~~) operation to query the state of an endpoint group.
        *   If the endpoint group is in the **updating** state, it indicates that the configurations of the endpoint group are being modified. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, it indicates that the configurations of the endpoint group are modified.
        *   The **UpdateEndpointGroup** operation cannot be repeatedly called for the same Global Accelerator (GA) instance within a specific period of time.
        

        @param request: UpdateEndpointGroupRequest

        @return: UpdateEndpointGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_endpoint_group_with_options(request, runtime)

    def update_endpoint_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEndpointGroupAttribute',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateEndpointGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_endpoint_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_endpoint_group_attribute_with_options(request, runtime)

    def update_endpoint_groups_with_options(self, request, runtime):
        """
        ### Description
        *   **UpdateEndpointGroups** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeEndpointGroup](~~153260~~) or [ListEndpointGroups](~~153261~~) operation to query the status of an endpoint group.
        *   If the endpoint group is in the **updating** state, it indicates that the configuration of the endpoint group is being modified. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, it indicates that the configuration of the endpoint group is modified.
        *   The **UpdateEndpointGroups** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: UpdateEndpointGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateEndpointGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.endpoint_group_configurations):
            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEndpointGroups',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_endpoint_groups(self, request):
        """
        ### Description
        *   **UpdateEndpointGroups** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeEndpointGroup](~~153260~~) or [ListEndpointGroups](~~153261~~) operation to query the status of an endpoint group.
        *   If the endpoint group is in the **updating** state, it indicates that the configuration of the endpoint group is being modified. In this case, you can perform only query operations.
        *   If the endpoint group is in the **active** state, it indicates that the configuration of the endpoint group is modified.
        *   The **UpdateEndpointGroups** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: UpdateEndpointGroupsRequest

        @return: UpdateEndpointGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_endpoint_groups_with_options(request, runtime)

    def update_forwarding_rules_with_options(self, request, runtime):
        """
        **UpdateForwardingRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListForwardingRules](~~205817~~) operation to query the status of a forwarding rule.
        *   If the forwarding rule is in the **configuring** state, it indicates that the forwarding rule is being modified. In this case, you can perform only query operations.
        *   If the forwarding rule is in the **active** state, it indicates that the forwarding rule is modified.
        *   The **UpdateForwardingRules** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: UpdateForwardingRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateForwardingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.forwarding_rules):
            query['ForwardingRules'] = request.forwarding_rules
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateForwardingRules',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_forwarding_rules(self, request):
        """
        **UpdateForwardingRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListForwardingRules](~~205817~~) operation to query the status of a forwarding rule.
        *   If the forwarding rule is in the **configuring** state, it indicates that the forwarding rule is being modified. In this case, you can perform only query operations.
        *   If the forwarding rule is in the **active** state, it indicates that the forwarding rule is modified.
        *   The **UpdateForwardingRules** operation holds an exclusive lock on the Global Accelerator (GA) instance. While the operation is in progress, you cannot call the same operation in the same Alibaba Cloud account.
        

        @param request: UpdateForwardingRulesRequest

        @return: UpdateForwardingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_forwarding_rules_with_options(request, runtime)

    def update_ip_set_with_options(self, request, runtime):
        """
        **UpdateIpSet** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeIpSet](~~153246~~) operation to query the status of an acceleration region.
        *   If the acceleration region is in the **updating** state, it indicates that the acceleration region is being modified. In this case, you can continue to perform query operations on the acceleration regions.
        *   If the acceleration region is in the **active** state, it indicates that the acceleration region is modified.
        *   You cannot call the **UpdateIpSet** operation again on the same GA instance before the previous operation is complete.
        

        @param request: UpdateIpSetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateIpSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIpSet',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ip_set(self, request):
        """
        **UpdateIpSet** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeIpSet](~~153246~~) operation to query the status of an acceleration region.
        *   If the acceleration region is in the **updating** state, it indicates that the acceleration region is being modified. In this case, you can continue to perform query operations on the acceleration regions.
        *   If the acceleration region is in the **active** state, it indicates that the acceleration region is modified.
        *   You cannot call the **UpdateIpSet** operation again on the same GA instance before the previous operation is complete.
        

        @param request: UpdateIpSetRequest

        @return: UpdateIpSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ip_set_with_options(request, runtime)

    def update_ip_sets_with_options(self, request, runtime):
        """
        **UpdateIpSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeIpSet](~~153246~~) operation to query the status of the task.
        *   If an acceleration region is in the **updating** state, the acceleration region is being modified. In this case, you can perform only query operations.
        *   If an acceleration region is in the **active** state, the acceleration region is modified.
        *   You cannot repeatedly call the **UpdateIpSet** operation for the same GA instance within a specific period of time.
        

        @param request: UpdateIpSetsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateIpSetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_sets):
            query['IpSets'] = request.ip_sets
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIpSets',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ip_sets(self, request):
        """
        **UpdateIpSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [DescribeIpSet](~~153246~~) operation to query the status of the task.
        *   If an acceleration region is in the **updating** state, the acceleration region is being modified. In this case, you can perform only query operations.
        *   If an acceleration region is in the **active** state, the acceleration region is modified.
        *   You cannot repeatedly call the **UpdateIpSet** operation for the same GA instance within a specific period of time.
        

        @param request: UpdateIpSetsRequest

        @return: UpdateIpSetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ip_sets_with_options(request, runtime)

    def update_listener_with_options(self, request, runtime):
        """
        This operation can be called to modify the configurations such as the protocol and ports of a listener to meet your business requirements.
        When you call this operation, take note of the following items:
        *   **UpdateListener** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeListener](~~153254~~) operation to query the status of a listener.
        *   If the listener is in the **updating** state, it indicates that its configurations are being modified. In this case, you can perform only query operations.
        *   If the listener is in the **active** state, it indicates that its configurations are modified.
        *   The **UpdateListener** operation cannot be repeatedly called to modify listener configurations for the same GA instance within a specific period of time.
        

        @param request: UpdateListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_ports):
            query['BackendPorts'] = request.backend_ports
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_affinity):
            query['ClientAffinity'] = request.client_affinity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.port_ranges):
            query['PortRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.proxy_protocol):
            query['ProxyProtocol'] = request.proxy_protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateListener',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def update_listener(self, request):
        """
        This operation can be called to modify the configurations such as the protocol and ports of a listener to meet your business requirements.
        When you call this operation, take note of the following items:
        *   **UpdateListener** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call the [DescribeListener](~~153254~~) operation to query the status of a listener.
        *   If the listener is in the **updating** state, it indicates that its configurations are being modified. In this case, you can perform only query operations.
        *   If the listener is in the **active** state, it indicates that its configurations are modified.
        *   The **UpdateListener** operation cannot be repeatedly called to modify listener configurations for the same GA instance within a specific period of time.
        

        @param request: UpdateListenerRequest

        @return: UpdateListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_listener_with_options(request, runtime)

    def update_service_managed_control_with_options(self, request, runtime):
        """
        This operation is applicable only to **managed** Global Accelerator (GA) instances.
        *   After you change the control mode of a GA instance from managed mode to unmanaged mode, you cannot change the mode of the instance to managed mode.
        *   After you change the control mode of a GA instance from managed mode to unmanaged mode, you can obtain all operation permissions on the instance.
        <warning>If you change or delete a configuration of a GA instance whose control mode is changed from managed mode to unmanaged mode, the cloud services that depend on the instance may not work as expected. Proceed with caution.></warning>
        

        @param request: UpdateServiceManagedControlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateServiceManagedControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_managed):
            query['ServiceManaged'] = request.service_managed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceManagedControl',
            version='2019-11-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ga_20191120_models.UpdateServiceManagedControlResponse(),
            self.call_api(params, req, runtime)
        )

    def update_service_managed_control(self, request):
        """
        This operation is applicable only to **managed** Global Accelerator (GA) instances.
        *   After you change the control mode of a GA instance from managed mode to unmanaged mode, you cannot change the mode of the instance to managed mode.
        *   After you change the control mode of a GA instance from managed mode to unmanaged mode, you can obtain all operation permissions on the instance.
        <warning>If you change or delete a configuration of a GA instance whose control mode is changed from managed mode to unmanaged mode, the cloud services that depend on the instance may not work as expected. Proceed with caution.></warning>
        

        @param request: UpdateServiceManagedControlRequest

        @return: UpdateServiceManagedControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_service_managed_control_with_options(request, runtime)
