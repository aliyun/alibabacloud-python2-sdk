# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ProductComponentRelationDetail(TeaModel):
    def __init__(self, app_version=None, category=None, class_=None, component_name=None,
                 component_orchestration_values=None, component_uid=None, component_version_uid=None, created_at=None, description=None,
                 documents=None, enable=None, images_mapping=None, namespace=None, orchestration_type=None,
                 parent_component=None, parent_component_version_relation_uid=None, parent_component_version_uid=None,
                 priority=None, product_version_uid=None, provider=None, public=None, readme=None, relation_uid=None,
                 release_name=None, resources=None, sequence=None, singleton=None, source=None, version=None):
        # appVersion
        self.app_version = app_version  # type: str
        # category
        self.category = category  # type: str
        # class
        self.class_ = class_  # type: str
        # componentName
        self.component_name = component_name  # type: str
        # componentOrchestrationValues
        self.component_orchestration_values = component_orchestration_values  # type: str
        # componentUID
        self.component_uid = component_uid  # type: str
        # componentVersionUID
        self.component_version_uid = component_version_uid  # type: str
        # createdAt
        self.created_at = created_at  # type: str
        # description
        self.description = description  # type: str
        # documents
        self.documents = documents  # type: str
        # enable
        self.enable = enable  # type: bool
        # imagesMapping
        self.images_mapping = images_mapping  # type: str
        # namespace
        self.namespace = namespace  # type: str
        # orchestrationType
        self.orchestration_type = orchestration_type  # type: str
        # parentComponent
        self.parent_component = parent_component  # type: bool
        # parentComponentVersionRelationUID
        self.parent_component_version_relation_uid = parent_component_version_relation_uid  # type: str
        # parentComponentVersionUID
        self.parent_component_version_uid = parent_component_version_uid  # type: str
        # priority
        self.priority = priority  # type: int
        # productVersionUID
        self.product_version_uid = product_version_uid  # type: str
        # provider
        self.provider = provider  # type: str
        # public
        self.public = public  # type: bool
        # readme
        self.readme = readme  # type: str
        # relationUID
        self.relation_uid = relation_uid  # type: str
        # releaseName
        self.release_name = release_name  # type: str
        # resources
        self.resources = resources  # type: str
        # sequence
        self.sequence = sequence  # type: int
        # singleton
        self.singleton = singleton  # type: bool
        # source
        self.source = source  # type: str
        # version
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProductComponentRelationDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.class_ is not None:
            result['class'] = self.class_
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_orchestration_values is not None:
            result['componentOrchestrationValues'] = self.component_orchestration_values
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.enable is not None:
            result['enable'] = self.enable
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.parent_component_version_relation_uid is not None:
            result['parentComponentVersionRelationUID'] = self.parent_component_version_relation_uid
        if self.parent_component_version_uid is not None:
            result['parentComponentVersionUID'] = self.parent_component_version_uid
        if self.priority is not None:
            result['priority'] = self.priority
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.readme is not None:
            result['readme'] = self.readme
        if self.relation_uid is not None:
            result['relationUID'] = self.relation_uid
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.resources is not None:
            result['resources'] = self.resources
        if self.sequence is not None:
            result['sequence'] = self.sequence
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentOrchestrationValues') is not None:
            self.component_orchestration_values = m.get('componentOrchestrationValues')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('parentComponentVersionRelationUID') is not None:
            self.parent_component_version_relation_uid = m.get('parentComponentVersionRelationUID')
        if m.get('parentComponentVersionUID') is not None:
            self.parent_component_version_uid = m.get('parentComponentVersionUID')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('relationUID') is not None:
            self.relation_uid = m.get('relationUID')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('sequence') is not None:
            self.sequence = m.get('sequence')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class FoundationVersionPlatforms(TeaModel):
    def __init__(self, architecture=None, os=None):
        # architecture
        self.architecture = architecture  # type: str
        # os
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FoundationVersionPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class FoundationVersion(TeaModel):
    def __init__(self, description=None, documents=None, name=None, platforms=None, status=None, uid=None,
                 version=None):
        # description
        self.description = description  # type: str
        # documents
        self.documents = documents  # type: str
        # name
        self.name = name  # type: str
        # platforms
        self.platforms = platforms  # type: FoundationVersionPlatforms
        # status
        self.status = status  # type: str
        # uid
        self.uid = uid  # type: str
        # version
        self.version = version  # type: str

    def validate(self):
        if self.platforms:
            self.platforms.validate()

    def to_map(self):
        _map = super(FoundationVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.platforms is not None:
            result['platforms'] = self.platforms.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platforms') is not None:
            temp_model = FoundationVersionPlatforms()
            self.platforms = temp_model.from_map(m['platforms'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Platform(TeaModel):
    def __init__(self, architecture=None, os=None):
        # architecture
        self.architecture = architecture  # type: str
        # os
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Platform, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ComponentVersion(TeaModel):
    def __init__(self, app_version=None, component_name=None, component_uid=None, description=None, documents=None,
                 images_mapping=None, namespace=None, orchestration_type=None, orchestration_values=None, package_url=None,
                 parent_component=None, platforms=None, readme=None, resources=None, source=None, uid=None, version=None):
        # appVersion
        self.app_version = app_version  # type: str
        # componentName
        self.component_name = component_name  # type: str
        # componentUID
        self.component_uid = component_uid  # type: str
        # description
        self.description = description  # type: str
        # documents
        self.documents = documents  # type: str
        # imagesMapping
        self.images_mapping = images_mapping  # type: str
        # namespace
        self.namespace = namespace  # type: str
        # orchestrationType
        self.orchestration_type = orchestration_type  # type: str
        # orchestrationValues
        self.orchestration_values = orchestration_values  # type: str
        # packageURL
        self.package_url = package_url  # type: str
        # parentComponent
        self.parent_component = parent_component  # type: bool
        # platforms
        self.platforms = platforms  # type: list[Platform]
        # readme
        self.readme = readme  # type: str
        # resources
        self.resources = resources  # type: str
        # source
        self.source = source  # type: str
        # uid
        self.uid = uid  # type: str
        # version
        self.version = version  # type: str

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ComponentVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = Platform()
                self.platforms.append(temp_model.from_map(k))
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetEnvironmentResponseBodyDataPlatform(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentResponseBodyDataPlatform, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class GetEnvironmentResponseBodyData(TeaModel):
    def __init__(self, cluster_id=None, created_at=None, description=None, instance_list=None, location=None,
                 name=None, platform=None, product_name=None, product_version=None, uid=None, vendor_config=None,
                 vendor_type=None, instance_status=None):
        self.cluster_id = cluster_id  # type: str
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.instance_list = instance_list  # type: str
        self.location = location  # type: str
        self.name = name  # type: str
        self.platform = platform  # type: GetEnvironmentResponseBodyDataPlatform
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.uid = uid  # type: str
        self.vendor_config = vendor_config  # type: str
        self.vendor_type = vendor_type  # type: str
        self.instance_status = instance_status  # type: str

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super(GetEnvironmentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = GetEnvironmentResponseBodyDataPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        return self


class GetEnvironmentResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetEnvironmentResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionRelatedComponentVersionsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: list[ProductComponentRelationDetail]
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductVersionRelatedComponentVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ProductComponentRelationDetail()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListProductVersionRelatedComponentVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductVersionRelatedComponentVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductVersionRelatedComponentVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProductVersionRelatedComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComponentVersionChildrenResponseBodyData(TeaModel):
    def __init__(self, component_name=None, component_uid=None, description=None, documents=None,
                 orchestration_values=None, package_url=None, parent_component=None, product_component_version_uid=None, provider=None,
                 readme=None, resources=None, uid=None, version=None):
        self.component_name = component_name  # type: str
        self.component_uid = component_uid  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: list[str]
        self.orchestration_values = orchestration_values  # type: str
        self.package_url = package_url  # type: str
        self.parent_component = parent_component  # type: bool
        self.product_component_version_uid = product_component_version_uid  # type: str
        self.provider = provider  # type: str
        self.readme = readme  # type: str
        self.resources = resources  # type: str
        self.uid = uid  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetComponentVersionChildrenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.product_component_version_uid is not None:
            result['productComponentVersionUID'] = self.product_component_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('productComponentVersionUID') is not None:
            self.product_component_version_uid = m.get('productComponentVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetComponentVersionChildrenResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, status=None, success=None):
        self.data = data  # type: list[GetComponentVersionChildrenResponseBodyData]
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetComponentVersionChildrenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetComponentVersionChildrenResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetComponentVersionChildrenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetComponentVersionChildrenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetComponentVersionChildrenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetComponentVersionChildrenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductEnvironmentResponseBodyData(TeaModel):
    def __init__(self, created_at=None, cluster_uid=None, description=None, instance_list=None,
                 instance_status=None, name=None, product_name=None, product_version=None, type=None, uid=None, vendor_config=None,
                 vendor_type=None):
        self.created_at = created_at  # type: str
        self.cluster_uid = cluster_uid  # type: str
        self.description = description  # type: str
        self.instance_list = instance_list  # type: str
        self.instance_status = instance_status  # type: str
        self.name = name  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.type = type  # type: str
        self.uid = uid  # type: str
        self.vendor_config = vendor_config  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductEnvironmentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.cluster_uid is not None:
            result['clusterUID'] = self.cluster_uid
        if self.description is not None:
            result['description'] = self.description
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.type is not None:
            result['type'] = self.type
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('clusterUID') is not None:
            self.cluster_uid = m.get('clusterUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class GetProductEnvironmentResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetProductEnvironmentResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProductEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionPackageRequest(TeaModel):
    def __init__(self, platform=None, package_type=None, old_product_version_uid=None):
        self.platform = platform  # type: str
        self.package_type = package_type  # type: str
        self.old_product_version_uid = old_product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductVersionPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.platform is not None:
            result['platform'] = self.platform
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        return self


class GetProductVersionPackageResponseBodyData(TeaModel):
    def __init__(self, package_url=None):
        self.package_url = package_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductVersionPackageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        return self


class GetProductVersionPackageResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetProductVersionPackageResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProductVersionPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductVersionPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductVersionPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductVersionPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductVersionPackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductVersionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlicloudRegionResponseBodyDataRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None, status=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlicloudRegionResponseBodyDataRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAlicloudRegionResponseBodyDataRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[ListAlicloudRegionResponseBodyDataRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlicloudRegionResponseBodyDataRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = ListAlicloudRegionResponseBodyDataRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class ListAlicloudRegionResponseBodyData(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: ListAlicloudRegionResponseBodyDataRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(ListAlicloudRegionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = ListAlicloudRegionResponseBodyDataRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAlicloudRegionResponseBody(TeaModel):
    def __init__(self, data=None, success=None):
        self.data = data  # type: ListAlicloudRegionResponseBodyData
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAlicloudRegionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListAlicloudRegionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListAlicloudRegionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlicloudRegionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlicloudRegionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlicloudRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentVersionsRequestPlatforms(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentVersionsRequestPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListComponentVersionsRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, platforms=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.platforms = platforms  # type: list[ListComponentVersionsRequestPlatforms]

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ListComponentVersionsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        return self


class ListComponentVersionsShrinkRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, platforms_shrink=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.platforms_shrink = platforms_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentVersionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        return self


class ListComponentVersionsResponseBodyDataList(TeaModel):
    def __init__(self, app_version=None, component_name=None, component_uid=None, description=None, documents=None,
                 images_mapping=None, orchestration_values=None, package_url=None, parent_component=None, provider=None,
                 readme=None, resources=None, uid=None, version=None):
        self.app_version = app_version  # type: str
        self.component_name = component_name  # type: str
        self.component_uid = component_uid  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: str
        self.images_mapping = images_mapping  # type: str
        self.orchestration_values = orchestration_values  # type: str
        self.package_url = package_url  # type: str
        self.parent_component = parent_component  # type: bool
        self.provider = provider  # type: str
        self.readme = readme  # type: str
        self.resources = resources  # type: str
        self.uid = uid  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentVersionsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.provider is not None:
            result['provider'] = self.provider
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListComponentVersionsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListComponentVersionsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListComponentVersionsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListComponentVersionsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, err_code=None, err_msg=None, success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: ListComponentVersionsResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListComponentVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = ListComponentVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListComponentVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListComponentVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListComponentVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSnapshotInstanceJoinOptionWithBatchRequest(TeaModel):
    def __init__(self, instance_uids=None, join_snapshot=None, root_password=None):
        self.instance_uids = instance_uids  # type: str
        self.join_snapshot = join_snapshot  # type: bool
        self.root_password = root_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSnapshotInstanceJoinOptionWithBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_uids is not None:
            result['instanceUIDs'] = self.instance_uids
        if self.join_snapshot is not None:
            result['joinSnapshot'] = self.join_snapshot
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceUIDs') is not None:
            self.instance_uids = m.get('instanceUIDs')
        if m.get('joinSnapshot') is not None:
            self.join_snapshot = m.get('joinSnapshot')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        return self


class UpdateSnapshotInstanceJoinOptionWithBatchResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSnapshotInstanceJoinOptionWithBatchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateSnapshotInstanceJoinOptionWithBatchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSnapshotInstanceJoinOptionWithBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSnapshotInstanceJoinOptionWithBatchResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSnapshotInstanceJoinOptionWithBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVendorConfigTemplateResponseBodyData(TeaModel):
    def __init__(self, vendor_config=None):
        self.vendor_config = vendor_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateVendorConfigTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        return self


class GenerateVendorConfigTemplateResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GenerateVendorConfigTemplateResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateVendorConfigTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GenerateVendorConfigTemplateResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GenerateVendorConfigTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateVendorConfigTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateVendorConfigTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateVendorConfigTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductComponentRequest(TeaModel):
    def __init__(self, component_orchestration_values=None, enable=None, release_name=None):
        self.component_orchestration_values = component_orchestration_values  # type: str
        self.enable = enable  # type: bool
        self.release_name = release_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductComponentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_orchestration_values is not None:
            result['componentOrchestrationValues'] = self.component_orchestration_values
        if self.enable is not None:
            result['enable'] = self.enable
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentOrchestrationValues') is not None:
            self.component_orchestration_values = m.get('componentOrchestrationValues')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        return self


class UpdateProductComponentResponseBody(TeaModel):
    def __init__(self, err_msg=None, success=None):
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductComponentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateProductComponentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProductComponentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductComponentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProductComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentNodesRequestDataDisk2(TeaModel):
    def __init__(self, name=None, size=None):
        self.name = name  # type: str
        self.size = size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentNodesRequestDataDisk2, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class UpdateEnvironmentNodesRequestSystemDisk2(TeaModel):
    def __init__(self, name=None, size=None):
        self.name = name  # type: str
        self.size = size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentNodesRequestSystemDisk2, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class UpdateEnvironmentNodesRequestTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        self.effect = effect  # type: str
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentNodesRequestTaints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateEnvironmentNodesRequest(TeaModel):
    def __init__(self, cpu=None, data_disk=None, data_disk_2=None, env_uid=None, identifier=None, labels=None,
                 memory=None, node_ip=None, root_password=None, system_disk=None, system_disk_2=None, taints=None):
        self.cpu = cpu  # type: int
        self.data_disk = data_disk  # type: list[str]
        self.data_disk_2 = data_disk_2  # type: list[UpdateEnvironmentNodesRequestDataDisk2]
        self.env_uid = env_uid  # type: str
        self.identifier = identifier  # type: str
        self.labels = labels  # type: dict[str, any]
        self.memory = memory  # type: int
        self.node_ip = node_ip  # type: str
        self.root_password = root_password  # type: str
        self.system_disk = system_disk  # type: list[str]
        self.system_disk_2 = system_disk_2  # type: list[UpdateEnvironmentNodesRequestSystemDisk2]
        self.taints = taints  # type: list[UpdateEnvironmentNodesRequestTaints]

    def validate(self):
        if self.data_disk_2:
            for k in self.data_disk_2:
                if k:
                    k.validate()
        if self.system_disk_2:
            for k in self.system_disk_2:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEnvironmentNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.data_disk is not None:
            result['dataDisk'] = self.data_disk
        result['dataDisk2'] = []
        if self.data_disk_2 is not None:
            for k in self.data_disk_2:
                result['dataDisk2'].append(k.to_map() if k else None)
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.labels is not None:
            result['labels'] = self.labels
        if self.memory is not None:
            result['memory'] = self.memory
        if self.node_ip is not None:
            result['nodeIP'] = self.node_ip
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        if self.system_disk is not None:
            result['systemDisk'] = self.system_disk
        result['systemDisk2'] = []
        if self.system_disk_2 is not None:
            for k in self.system_disk_2:
                result['systemDisk2'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('dataDisk') is not None:
            self.data_disk = m.get('dataDisk')
        self.data_disk_2 = []
        if m.get('dataDisk2') is not None:
            for k in m.get('dataDisk2'):
                temp_model = UpdateEnvironmentNodesRequestDataDisk2()
                self.data_disk_2.append(temp_model.from_map(k))
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('nodeIP') is not None:
            self.node_ip = m.get('nodeIP')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        if m.get('systemDisk') is not None:
            self.system_disk = m.get('systemDisk')
        self.system_disk_2 = []
        if m.get('systemDisk2') is not None:
            for k in m.get('systemDisk2'):
                temp_model = UpdateEnvironmentNodesRequestSystemDisk2()
                self.system_disk_2.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = UpdateEnvironmentNodesRequestTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class UpdateEnvironmentNodesResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateEnvironmentNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEnvironmentNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEnvironmentNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentPackagesRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentPackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnvironmentPackagesResponseBodyDataList(TeaModel):
    def __init__(self, env_uid=None, provider=None, status=None, uid=None, url=None):
        self.env_uid = env_uid  # type: str
        self.provider = provider  # type: str
        self.status = status  # type: str
        self.uid = uid  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentPackagesResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEnvironmentPackagesResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListEnvironmentPackagesResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentPackagesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentPackagesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentPackagesResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: ListEnvironmentPackagesResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentPackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentPackagesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentPackagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnvironmentPackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentPackagesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentHeaders(TeaModel):
    def __init__(self, common_headers=None, client_token=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateEnvironmentRequestPlatform(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentRequestPlatform, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class CreateEnvironmentRequest(TeaModel):
    def __init__(self, annotations=None, description=None, location=None, name=None, platform=None, vendor_type=None):
        self.annotations = annotations  # type: str
        self.description = description  # type: str
        self.location = location  # type: str
        self.name = name  # type: str
        self.platform = platform  # type: CreateEnvironmentRequestPlatform
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super(CreateEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.description is not None:
            result['description'] = self.description
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = CreateEnvironmentRequestPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class CreateEnvironmentResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateEnvironmentResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: CreateEnvironmentResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateEnvironmentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentLogResponseBodyData(TeaModel):
    def __init__(self, end=None, message=None):
        self.end = end  # type: bool
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentLogResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetEnvironmentLogResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetEnvironmentLogResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnvironmentLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEnvironmentLogResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetEnvironmentLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnvironmentLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnvironmentLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnvironmentLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentNodeRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, name=None, fuzzy=None, node_ip=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.name = name  # type: str
        self.fuzzy = fuzzy  # type: str
        self.node_ip = node_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.name is not None:
            result['name'] = self.name
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.node_ip is not None:
            result['nodeIp'] = self.node_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('nodeIp') is not None:
            self.node_ip = m.get('nodeIp')
        return self


class ListEnvironmentNodeResponseBodyDataList(TeaModel):
    def __init__(self, created_at=None, description=None, id=None, name=None, product_name=None,
                 product_version=None, product_version_uid=None, uid=None, vendor_type=None):
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: int
        self.name = name  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.uid = uid  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentNodeResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentNodeResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListEnvironmentNodeResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentNodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentNodeResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentNodeResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: ListEnvironmentNodeResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentNodeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnvironmentNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionRelatedFoundationComponentVersionsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: list[ProductComponentRelationDetail]
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductVersionRelatedFoundationComponentVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ProductComponentRelationDetail()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListProductVersionRelatedFoundationComponentVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductVersionRelatedFoundationComponentVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductVersionRelatedFoundationComponentVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProductVersionRelatedFoundationComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncComponentRequest(TeaModel):
    def __init__(self, region=None, bucket_name=None):
        self.region = region  # type: str
        self.bucket_name = bucket_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncComponentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        return self


class SyncComponentResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, status=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncComponentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SyncComponentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SyncComponentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncComponentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SyncComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateComponentToProductRequest(TeaModel):
    def __init__(self, component_version_id=None):
        # the component Version ID
        self.component_version_id = component_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateComponentToProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_version_id is not None:
            result['componentVersionID'] = self.component_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentVersionID') is not None:
            self.component_version_id = m.get('componentVersionID')
        return self


class UpdateComponentToProductResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateComponentToProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateComponentToProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateComponentToProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateComponentToProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateComponentToProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentNodeRequestDataDisk(TeaModel):
    def __init__(self, name=None, required=None):
        self.name = name  # type: str
        self.required = required  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentNodeRequestDataDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class CreateEnvironmentNodeRequestSystemDisk(TeaModel):
    def __init__(self, name=None, required=None):
        self.name = name  # type: str
        self.required = required  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentNodeRequestSystemDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('required') is not None:
            self.required = m.get('required')
        return self


class CreateEnvironmentNodeRequestTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        self.effect = effect  # type: str
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentNodeRequestTaints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateEnvironmentNodeRequest(TeaModel):
    def __init__(self, cpu=None, data_disk=None, host_name=None, identifier=None, labels=None, memory=None, os=None,
                 private_ip=None, provider=None, root_password=None, system_disk=None, taints=None):
        self.cpu = cpu  # type: int
        self.data_disk = data_disk  # type: list[CreateEnvironmentNodeRequestDataDisk]
        self.host_name = host_name  # type: str
        self.identifier = identifier  # type: str
        self.labels = labels  # type: dict[str, any]
        self.memory = memory  # type: int
        self.os = os  # type: str
        self.private_ip = private_ip  # type: str
        self.provider = provider  # type: str
        self.root_password = root_password  # type: str
        self.system_disk = system_disk  # type: list[CreateEnvironmentNodeRequestSystemDisk]
        self.taints = taints  # type: list[CreateEnvironmentNodeRequestTaints]

    def validate(self):
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        if self.system_disk:
            for k in self.system_disk:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEnvironmentNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        result['dataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['dataDisk'].append(k.to_map() if k else None)
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.labels is not None:
            result['labels'] = self.labels
        if self.memory is not None:
            result['memory'] = self.memory
        if self.os is not None:
            result['os'] = self.os
        if self.private_ip is not None:
            result['privateIP'] = self.private_ip
        if self.provider is not None:
            result['provider'] = self.provider
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        result['systemDisk'] = []
        if self.system_disk is not None:
            for k in self.system_disk:
                result['systemDisk'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        self.data_disk = []
        if m.get('dataDisk') is not None:
            for k in m.get('dataDisk'):
                temp_model = CreateEnvironmentNodeRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('privateIP') is not None:
            self.private_ip = m.get('privateIP')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        self.system_disk = []
        if m.get('systemDisk') is not None:
            for k in m.get('systemDisk'):
                temp_model = CreateEnvironmentNodeRequestSystemDisk()
                self.system_disk.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = CreateEnvironmentNodeRequestTaints()
                self.taints.append(temp_model.from_map(k))
        return self


class CreateEnvironmentNodeResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateEnvironmentNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEnvironmentNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEnvironmentNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComponentResponseBodyDataAnnotations(TeaModel):
    def __init__(self, additional_prop_1=None, additional_prop_2=None, additional_prop_3=None):
        self.additional_prop_1 = additional_prop_1  # type: str
        self.additional_prop_2 = additional_prop_2  # type: str
        self.additional_prop_3 = additional_prop_3  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetComponentResponseBodyDataAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_prop_1 is not None:
            result['additionalProp1'] = self.additional_prop_1
        if self.additional_prop_2 is not None:
            result['additionalProp2'] = self.additional_prop_2
        if self.additional_prop_3 is not None:
            result['additionalProp3'] = self.additional_prop_3
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalProp1') is not None:
            self.additional_prop_1 = m.get('additionalProp1')
        if m.get('additionalProp2') is not None:
            self.additional_prop_2 = m.get('additionalProp2')
        if m.get('additionalProp3') is not None:
            self.additional_prop_3 = m.get('additionalProp3')
        return self


class GetComponentResponseBodyData(TeaModel):
    def __init__(self, annotations=None, category=None, description=None, documents=None, name=None, provider=None,
                 public=None, singleton=None, source=None, uid=None):
        self.annotations = annotations  # type: GetComponentResponseBodyDataAnnotations
        self.category = category  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: str
        self.name = name  # type: str
        self.provider = provider  # type: str
        self.public = public  # type: bool
        self.singleton = singleton  # type: bool
        self.source = source  # type: str
        self.uid = uid  # type: str

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super(GetComponentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = GetComponentResponseBodyDataAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetComponentResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetComponentResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetComponentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetComponentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetComponentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetComponentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetComponentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationVersionRelatedComponentVersionsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ComponentVersion]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFoundationVersionRelatedComponentVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ComponentVersion()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListFoundationVersionRelatedComponentVersionsResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, err_code=None, err_msg=None, success=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: ListFoundationVersionRelatedComponentVersionsResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListFoundationVersionRelatedComponentVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = ListFoundationVersionRelatedComponentVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListFoundationVersionRelatedComponentVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFoundationVersionRelatedComponentVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFoundationVersionRelatedComponentVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFoundationVersionRelatedComponentVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSnapshotResponseBodyData(TeaModel):
    def __init__(self, description=None, instance_cidr=None, name=None, product_name=None, product_version=None,
                 product_version_desc=None, region=None, snapshot_region=None, snapshot_status=None, source_environment_uid=None,
                 source_type=None, uid=None, vpcid=None):
        self.description = description  # type: str
        self.instance_cidr = instance_cidr  # type: str
        self.name = name  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.product_version_desc = product_version_desc  # type: str
        self.region = region  # type: str
        self.snapshot_region = snapshot_region  # type: str
        self.snapshot_status = snapshot_status  # type: str
        self.source_environment_uid = source_environment_uid  # type: str
        self.source_type = source_type  # type: str
        self.uid = uid  # type: str
        self.vpcid = vpcid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSnapshotResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.instance_cidr is not None:
            result['instanceCIDR'] = self.instance_cidr
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_desc is not None:
            result['productVersionDesc'] = self.product_version_desc
        if self.region is not None:
            result['region'] = self.region
        if self.snapshot_region is not None:
            result['snapshotRegion'] = self.snapshot_region
        if self.snapshot_status is not None:
            result['snapshotStatus'] = self.snapshot_status
        if self.source_environment_uid is not None:
            result['sourceEnvironmentUID'] = self.source_environment_uid
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vpcid is not None:
            result['vpcid'] = self.vpcid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceCIDR') is not None:
            self.instance_cidr = m.get('instanceCIDR')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionDesc') is not None:
            self.product_version_desc = m.get('productVersionDesc')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('snapshotRegion') is not None:
            self.snapshot_region = m.get('snapshotRegion')
        if m.get('snapshotStatus') is not None:
            self.snapshot_status = m.get('snapshotStatus')
        if m.get('sourceEnvironmentUID') is not None:
            self.source_environment_uid = m.get('sourceEnvironmentUID')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vpcid') is not None:
            self.vpcid = m.get('vpcid')
        return self


class GetSnapshotResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetSnapshotResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLicenseResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLatestProductVersionHeaders(TeaModel):
    def __init__(self, common_headers=None, client_token=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLatestProductVersionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateLatestProductVersionResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLatestProductVersionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateLatestProductVersionResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: CreateLatestProductVersionResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateLatestProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateLatestProductVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateLatestProductVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateLatestProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLatestProductVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLatestProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlicloudVPCResponseBodyDataVpcsVpcUserCidrs(TeaModel):
    def __init__(self, user_cidr=None):
        self.user_cidr = user_cidr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlicloudVPCResponseBodyDataVpcsVpcUserCidrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')
        return self


class ListAlicloudVPCResponseBodyDataVpcsVpcVSwitchIds(TeaModel):
    def __init__(self, v_switch_id=None):
        self.v_switch_id = v_switch_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlicloudVPCResponseBodyDataVpcsVpcVSwitchIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class ListAlicloudVPCResponseBodyDataVpcsVpc(TeaModel):
    def __init__(self, cidr_block=None, creation_time=None, description=None, is_default=None, region_id=None,
                 status=None, user_cidrs=None, vrouter_id=None, v_switch_ids=None, vpc_id=None, vpc_name=None):
        self.cidr_block = cidr_block  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.is_default = is_default  # type: bool
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.user_cidrs = user_cidrs  # type: ListAlicloudVPCResponseBodyDataVpcsVpcUserCidrs
        self.vrouter_id = vrouter_id  # type: str
        self.v_switch_ids = v_switch_ids  # type: ListAlicloudVPCResponseBodyDataVpcsVpcVSwitchIds
        self.vpc_id = vpc_id  # type: str
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.user_cidrs:
            self.user_cidrs.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        _map = super(ListAlicloudVPCResponseBodyDataVpcsVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_cidrs is not None:
            result['UserCidrs'] = self.user_cidrs.to_map()
        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserCidrs') is not None:
            temp_model = ListAlicloudVPCResponseBodyDataVpcsVpcUserCidrs()
            self.user_cidrs = temp_model.from_map(m['UserCidrs'])
        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')
        if m.get('VSwitchIds') is not None:
            temp_model = ListAlicloudVPCResponseBodyDataVpcsVpcVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m['VSwitchIds'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class ListAlicloudVPCResponseBodyDataVpcs(TeaModel):
    def __init__(self, vpc=None):
        self.vpc = vpc  # type: list[ListAlicloudVPCResponseBodyDataVpcsVpc]

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlicloudVPCResponseBodyDataVpcs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = ListAlicloudVPCResponseBodyDataVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class ListAlicloudVPCResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, vpcs=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.vpcs = vpcs  # type: ListAlicloudVPCResponseBodyDataVpcs

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        _map = super(ListAlicloudVPCResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Vpcs') is not None:
            temp_model = ListAlicloudVPCResponseBodyDataVpcs()
            self.vpcs = temp_model.from_map(m['Vpcs'])
        return self


class ListAlicloudVPCResponseBody(TeaModel):
    def __init__(self, data=None, success=None):
        self.data = data  # type: ListAlicloudVPCResponseBodyData
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAlicloudVPCResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListAlicloudVPCResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListAlicloudVPCResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlicloudVPCResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlicloudVPCResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlicloudVPCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductHeaders(TeaModel):
    def __init__(self, common_headers=None, client_token=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateProductRequest(TeaModel):
    def __init__(self, annotations=None, component_version_uid=None, description=None, foundation_version_uid=None,
                 product_name=None, prometheus_uid=None):
        self.annotations = annotations  # type: str
        self.component_version_uid = component_version_uid  # type: str
        self.description = description  # type: str
        self.foundation_version_uid = foundation_version_uid  # type: str
        self.product_name = product_name  # type: str
        self.prometheus_uid = prometheus_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.description is not None:
            result['description'] = self.description
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.prometheus_uid is not None:
            result['prometheusUID'] = self.prometheus_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('prometheusUID') is not None:
            self.prometheus_uid = m.get('prometheusUID')
        return self


class CreateProductResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: CreateProductResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductEnvironmentsRequestPlatforms(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductEnvironmentsRequestPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class GetProductEnvironmentsRequest(TeaModel):
    def __init__(self, product_uid=None, env_type=None, platforms=None):
        self.product_uid = product_uid  # type: str
        self.env_type = env_type  # type: str
        self.platforms = platforms  # type: list[GetProductEnvironmentsRequestPlatforms]

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProductEnvironmentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.env_type is not None:
            result['envType'] = self.env_type
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('envType') is not None:
            self.env_type = m.get('envType')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = GetProductEnvironmentsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        return self


class GetProductEnvironmentsShrinkRequest(TeaModel):
    def __init__(self, product_uid=None, env_type=None, platforms_shrink=None):
        self.product_uid = product_uid  # type: str
        self.env_type = env_type  # type: str
        self.platforms_shrink = platforms_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductEnvironmentsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.env_type is not None:
            result['envType'] = self.env_type
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('envType') is not None:
            self.env_type = m.get('envType')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        return self


class GetProductEnvironmentsResponseBodyData(TeaModel):
    def __init__(self, cluster_id=None, created_at=None, description=None, instance_list=None, name=None,
                 product_name=None, product_version=None, uid=None, vendor_config=None, vendor_type=None):
        self.cluster_id = cluster_id  # type: str
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.instance_list = instance_list  # type: str
        self.name = name  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.uid = uid  # type: str
        self.vendor_config = vendor_config  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductEnvironmentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class GetProductEnvironmentsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetProductEnvironmentsResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProductEnvironmentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductEnvironmentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductEnvironmentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductEnvironmentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteComponentResponseBody(TeaModel):
    def __init__(self, err_message=None, success=None, err_code=None):
        self.err_message = err_message  # type: str
        self.success = success  # type: bool
        self.err_code = err_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteComponentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['errCode'] = self.err_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        return self


class DeleteComponentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteComponentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteComponentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductComponentResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, status=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductComponentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteProductComponentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProductComponentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProductComponentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProductComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentWithSnapshotRequest(TeaModel):
    def __init__(self, environment_desc=None, environment_name=None):
        self.environment_desc = environment_desc  # type: str
        self.environment_name = environment_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentWithSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_desc is not None:
            result['environmentDesc'] = self.environment_desc
        if self.environment_name is not None:
            result['environmentName'] = self.environment_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('environmentDesc') is not None:
            self.environment_desc = m.get('environmentDesc')
        if m.get('environmentName') is not None:
            self.environment_name = m.get('environmentName')
        return self


class CreateEnvironmentWithSnapshotResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentWithSnapshotResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateEnvironmentWithSnapshotResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: CreateEnvironmentWithSnapshotResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEnvironmentWithSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateEnvironmentWithSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateEnvironmentWithSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEnvironmentWithSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEnvironmentWithSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentWithSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentResponseBody(TeaModel):
    def __init__(self, err_message=None, success=None, err_code=None):
        self.err_message = err_message  # type: str
        self.success = success  # type: bool
        self.err_code = err_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['errCode'] = self.err_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        return self


class DeleteEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductVersionRequest(TeaModel):
    def __init__(self, compatible_versions=None, description=None, version=None):
        self.compatible_versions = compatible_versions  # type: str
        self.description = description  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_versions is not None:
            result['compatibleVersions'] = self.compatible_versions
        if self.description is not None:
            result['description'] = self.description
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('compatibleVersions') is not None:
            self.compatible_versions = m.get('compatibleVersions')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpdateProductVersionResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateProductVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChildrenComponentVersionParametersListRequest(TeaModel):
    def __init__(self, relation_id=None):
        self.relation_id = relation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChildrenComponentVersionParametersListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_id is not None:
            result['relation_id'] = self.relation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('relation_id') is not None:
            self.relation_id = m.get('relation_id')
        return self


class GetChildrenComponentVersionParametersListResponseBodyDataAnnotations(TeaModel):
    def __init__(self, additional_prop_1=None, additional_prop_2=None, additional_prop_3=None):
        self.additional_prop_1 = additional_prop_1  # type: str
        self.additional_prop_2 = additional_prop_2  # type: str
        self.additional_prop_3 = additional_prop_3  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChildrenComponentVersionParametersListResponseBodyDataAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_prop_1 is not None:
            result['additionalProp1'] = self.additional_prop_1
        if self.additional_prop_2 is not None:
            result['additionalProp2'] = self.additional_prop_2
        if self.additional_prop_3 is not None:
            result['additionalProp3'] = self.additional_prop_3
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalProp1') is not None:
            self.additional_prop_1 = m.get('additionalProp1')
        if m.get('additionalProp2') is not None:
            self.additional_prop_2 = m.get('additionalProp2')
        if m.get('additionalProp3') is not None:
            self.additional_prop_3 = m.get('additionalProp3')
        return self


class GetChildrenComponentVersionParametersListResponseBodyData(TeaModel):
    def __init__(self, annotations=None, category=None, class_=None, description=None, documents=None, name=None,
                 provider=None, uid=None):
        self.annotations = annotations  # type: GetChildrenComponentVersionParametersListResponseBodyDataAnnotations
        self.category = category  # type: str
        self.class_ = class_  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: list[str]
        self.name = name  # type: str
        self.provider = provider  # type: str
        self.uid = uid  # type: str

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super(GetChildrenComponentVersionParametersListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.class_ is not None:
            result['class'] = self.class_
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = GetChildrenComponentVersionParametersListResponseBodyDataAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetChildrenComponentVersionParametersListResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetChildrenComponentVersionParametersListResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetChildrenComponentVersionParametersListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetChildrenComponentVersionParametersListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetChildrenComponentVersionParametersListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetChildrenComponentVersionParametersListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChildrenComponentVersionParametersListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetChildrenComponentVersionParametersListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(self, description=None, name=None, product_name=None, product_version=None,
                 product_version_desc=None, region=None, vpcid=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.product_version_desc = product_version_desc  # type: str
        self.region = region  # type: str
        self.vpcid = vpcid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_desc is not None:
            result['productVersionDesc'] = self.product_version_desc
        if self.region is not None:
            result['region'] = self.region
        if self.vpcid is not None:
            result['vpcid'] = self.vpcid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionDesc') is not None:
            self.product_version_desc = m.get('productVersionDesc')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('vpcid') is not None:
            self.vpcid = m.get('vpcid')
        return self


class CreateSnapshotResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: CreateSnapshotResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLatestVersionDifferencesRequest(TeaModel):
    def __init__(self, pre_version_id=None):
        # 上一个产品版本id
        self.pre_version_id = pre_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLatestVersionDifferencesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pre_version_id is not None:
            result['preVersionID'] = self.pre_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('preVersionID') is not None:
            self.pre_version_id = m.get('preVersionID')
        return self


class GetLatestVersionDifferencesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLatestVersionDifferencesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetLatestVersionDifferencesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLatestVersionDifferencesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLatestVersionDifferencesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLatestVersionDifferencesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentNodeRequest(TeaModel):
    def __init__(self, env_uid=None):
        self.env_uid = env_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnvironmentNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        return self


class DeleteEnvironmentNodeResponseBody(TeaModel):
    def __init__(self, err_message=None, success=None, err_code=None):
        self.err_message = err_message  # type: str
        self.success = success  # type: bool
        self.err_code = err_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnvironmentNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['errCode'] = self.err_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        return self


class DeleteEnvironmentNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEnvironmentNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEnvironmentNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyComponentRequestPlatforms(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyComponentRequestPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ApplyComponentRequest(TeaModel):
    def __init__(self, annotations=None, app_version=None, category=None, component_class=None, description=None,
                 documents=None, images_mapping=None, name=None, namespace=None, orchestration_type=None,
                 orchestration_values=None, package_url=None, parent_component=None, platforms=None, priority=None, provider=None,
                 public=None, readme=None, resources=None, singleton=None, version=None):
        self.annotations = annotations  # type: str
        self.app_version = app_version  # type: str
        self.category = category  # type: str
        self.component_class = component_class  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: str
        self.images_mapping = images_mapping  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.orchestration_type = orchestration_type  # type: str
        self.orchestration_values = orchestration_values  # type: str
        self.package_url = package_url  # type: str
        self.parent_component = parent_component  # type: bool
        self.platforms = platforms  # type: list[ApplyComponentRequestPlatforms]
        self.priority = priority  # type: int
        self.provider = provider  # type: str
        self.public = public  # type: bool
        self.readme = readme  # type: str
        self.resources = resources  # type: str
        self.singleton = singleton  # type: bool
        self.version = version  # type: str

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ApplyComponentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.component_class is not None:
            result['componentClass'] = self.component_class
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['priority'] = self.priority
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('componentClass') is not None:
            self.component_class = m.get('componentClass')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ApplyComponentRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ApplyComponentResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, status=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyComponentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ApplyComponentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ApplyComponentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyComponentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ApplyComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSnapshotInstancesRequest(TeaModel):
    def __init__(self, page_size=None, page_num=None, sort_key=None, sort_direct=None):
        self.page_size = page_size  # type: int
        self.page_num = page_num  # type: int
        self.sort_key = sort_key  # type: str
        self.sort_direct = sort_direct  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSnapshotInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.sort_key is not None:
            result['sortKey'] = self.sort_key
        if self.sort_direct is not None:
            result['sortDirect'] = self.sort_direct
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('sortKey') is not None:
            self.sort_key = m.get('sortKey')
        if m.get('sortDirect') is not None:
            self.sort_direct = m.get('sortDirect')
        return self


class GetSnapshotInstancesResponseBodyDataListAnnotations(TeaModel):
    def __init__(self, additional_prop_1=None, additional_prop_2=None, additional_prop_3=None):
        self.additional_prop_1 = additional_prop_1  # type: str
        self.additional_prop_2 = additional_prop_2  # type: str
        self.additional_prop_3 = additional_prop_3  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSnapshotInstancesResponseBodyDataListAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_prop_1 is not None:
            result['additionalProp1'] = self.additional_prop_1
        if self.additional_prop_2 is not None:
            result['additionalProp2'] = self.additional_prop_2
        if self.additional_prop_3 is not None:
            result['additionalProp3'] = self.additional_prop_3
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalProp1') is not None:
            self.additional_prop_1 = m.get('additionalProp1')
        if m.get('additionalProp2') is not None:
            self.additional_prop_2 = m.get('additionalProp2')
        if m.get('additionalProp3') is not None:
            self.additional_prop_3 = m.get('additionalProp3')
        return self


class GetSnapshotInstancesResponseBodyDataList(TeaModel):
    def __init__(self, annotations=None, cpu=None, ecs_instance_id=None, host_name=None, identifier=None,
                 image_id=None, instance_type=None, internet_bandwidth=None, join_snapshot=None, memory=None,
                 private_ip=None, public_ip=None, root_password=None, storage_total_size=None, uid=None):
        self.annotations = annotations  # type: GetSnapshotInstancesResponseBodyDataListAnnotations
        self.cpu = cpu  # type: int
        self.ecs_instance_id = ecs_instance_id  # type: str
        self.host_name = host_name  # type: str
        self.identifier = identifier  # type: str
        self.image_id = image_id  # type: str
        self.instance_type = instance_type  # type: str
        self.internet_bandwidth = internet_bandwidth  # type: int
        self.join_snapshot = join_snapshot  # type: bool
        self.memory = memory  # type: int
        self.private_ip = private_ip  # type: str
        self.public_ip = public_ip  # type: str
        self.root_password = root_password  # type: str
        self.storage_total_size = storage_total_size  # type: int
        self.uid = uid  # type: str

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super(GetSnapshotInstancesResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.ecs_instance_id is not None:
            result['ecsInstanceID'] = self.ecs_instance_id
        if self.host_name is not None:
            result['hostName'] = self.host_name
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.image_id is not None:
            result['imageID'] = self.image_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.internet_bandwidth is not None:
            result['internetBandwidth'] = self.internet_bandwidth
        if self.join_snapshot is not None:
            result['joinSnapshot'] = self.join_snapshot
        if self.memory is not None:
            result['memory'] = self.memory
        if self.private_ip is not None:
            result['privateIP'] = self.private_ip
        if self.public_ip is not None:
            result['publicIP'] = self.public_ip
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        if self.storage_total_size is not None:
            result['storageTotalSize'] = self.storage_total_size
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = GetSnapshotInstancesResponseBodyDataListAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('ecsInstanceID') is not None:
            self.ecs_instance_id = m.get('ecsInstanceID')
        if m.get('hostName') is not None:
            self.host_name = m.get('hostName')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('imageID') is not None:
            self.image_id = m.get('imageID')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('internetBandwidth') is not None:
            self.internet_bandwidth = m.get('internetBandwidth')
        if m.get('joinSnapshot') is not None:
            self.join_snapshot = m.get('joinSnapshot')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('privateIP') is not None:
            self.private_ip = m.get('privateIP')
        if m.get('publicIP') is not None:
            self.public_ip = m.get('publicIP')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        if m.get('storageTotalSize') is not None:
            self.storage_total_size = m.get('storageTotalSize')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetSnapshotInstancesResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[GetSnapshotInstancesResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSnapshotInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetSnapshotInstancesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetSnapshotInstancesResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetSnapshotInstancesResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSnapshotInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetSnapshotInstancesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetSnapshotInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSnapshotInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSnapshotInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSnapshotInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, name=None, fuzzy=None, instance_status=None, vendor_type=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.name = name  # type: str
        self.fuzzy = fuzzy  # type: str
        self.instance_status = instance_status  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.name is not None:
            result['name'] = self.name
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentsResponseBodyDataListPlatform(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentsResponseBodyDataListPlatform, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListEnvironmentsResponseBodyDataList(TeaModel):
    def __init__(self, created_at=None, description=None, id=None, location=None, name=None, platform=None,
                 product_name=None, product_version=None, product_version_uid=None, uid=None, vendor_type=None):
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: int
        self.location = location  # type: str
        self.name = name  # type: str
        self.platform = platform  # type: ListEnvironmentsResponseBodyDataListPlatform
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.uid = uid  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('platform') is not None:
            temp_model = ListEnvironmentsResponseBodyDataListPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListEnvironmentsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: ListEnvironmentsResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnvironmentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckSLRRequest(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckSLRRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CheckSLRResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, error_code=None, success=None):
        self.data = data  # type: str
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckSLRResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CheckSLRResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckSLRResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckSLRResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductRequest(TeaModel):
    def __init__(self, description=None):
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateProductResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyComponentsRequestChildrenListPlatforms(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyComponentsRequestChildrenListPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ApplyComponentsRequestChildrenList(TeaModel):
    def __init__(self, annotations=None, app_version=None, category=None, component_class=None, description=None,
                 documents=None, images_mapping=None, name=None, namespace=None, orchestration_type=None,
                 orchestration_values=None, package_url=None, parent_component=None, platforms=None, priority=None, provider=None,
                 public=None, readme=None, resources=None, singleton=None, version=None):
        self.annotations = annotations  # type: str
        self.app_version = app_version  # type: str
        self.category = category  # type: str
        self.component_class = component_class  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: str
        self.images_mapping = images_mapping  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.orchestration_type = orchestration_type  # type: str
        self.orchestration_values = orchestration_values  # type: str
        self.package_url = package_url  # type: str
        self.parent_component = parent_component  # type: bool
        self.platforms = platforms  # type: list[ApplyComponentsRequestChildrenListPlatforms]
        self.priority = priority  # type: int
        self.provider = provider  # type: str
        self.public = public  # type: bool
        self.readme = readme  # type: str
        self.resources = resources  # type: str
        self.singleton = singleton  # type: bool
        self.version = version  # type: str

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ApplyComponentsRequestChildrenList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.component_class is not None:
            result['componentClass'] = self.component_class
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_type is not None:
            result['orchestrationType'] = self.orchestration_type
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['priority'] = self.priority
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('componentClass') is not None:
            self.component_class = m.get('componentClass')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationType') is not None:
            self.orchestration_type = m.get('orchestrationType')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ApplyComponentsRequestChildrenListPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ApplyComponentsRequest(TeaModel):
    def __init__(self, children_list=None, component=None):
        self.children_list = children_list  # type: list[ApplyComponentsRequestChildrenList]
        self.component = component  # type: str

    def validate(self):
        if self.children_list:
            for k in self.children_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ApplyComponentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['childrenList'] = []
        if self.children_list is not None:
            for k in self.children_list:
                result['childrenList'].append(k.to_map() if k else None)
        if self.component is not None:
            result['component'] = self.component
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.children_list = []
        if m.get('childrenList') is not None:
            for k in m.get('childrenList'):
                temp_model = ApplyComponentsRequestChildrenList()
                self.children_list.append(temp_model.from_map(k))
        if m.get('component') is not None:
            self.component = m.get('component')
        return self


class ApplyComponentsResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, status=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyComponentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ApplyComponentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ApplyComponentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyComponentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ApplyComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePackageConfigResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePackageConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreatePackageConfigResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: CreatePackageConfigResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreatePackageConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreatePackageConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreatePackageConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreatePackageConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePackageConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePackageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddProductComponentRequest(TeaModel):
    def __init__(self, release_name=None):
        self.release_name = release_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddProductComponentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        return self


class AddProductComponentResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, status=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.status = status  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddProductComponentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddProductComponentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddProductComponentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddProductComponentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddProductComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentsWithSnapshotResponseBodyDataList(TeaModel):
    def __init__(self, created_at=None, description=None, id=None, instance_status=None, name=None,
                 product_name=None, product_version=None, product_version_uid=None, uid=None, vendor_type=None):
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: int
        self.instance_status = instance_status  # type: str
        self.name = name  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.uid = uid  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentsWithSnapshotResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentsWithSnapshotResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListEnvironmentsWithSnapshotResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentsWithSnapshotResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentsWithSnapshotResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentsWithSnapshotResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: ListEnvironmentsWithSnapshotResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentsWithSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentsWithSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentsWithSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnvironmentsWithSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentsWithSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentsWithSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentNodeResponseBodyData(TeaModel):
    def __init__(self, cluster_id=None, created_at=None, description=None, instance_list=None, name=None,
                 product_name=None, product_version=None, uid=None, vendor_config=None, vendor_type=None):
        self.cluster_id = cluster_id  # type: str
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.instance_list = instance_list  # type: str
        self.name = name  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.uid = uid  # type: str
        self.vendor_config = vendor_config  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentNodeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class GetEnvironmentNodeResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetEnvironmentNodeResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnvironmentNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEnvironmentNodeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetEnvironmentNodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnvironmentNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnvironmentNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnvironmentNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSnapshotRequest(TeaModel):
    def __init__(self, description=None, product_name=None, product_version=None, product_version_desc=None,
                 update_key=None):
        self.description = description  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.product_version_desc = product_version_desc  # type: str
        self.update_key = update_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_desc is not None:
            result['productVersionDesc'] = self.product_version_desc
        if self.update_key is not None:
            result['updateKey'] = self.update_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionDesc') is not None:
            self.product_version_desc = m.get('productVersionDesc')
        if m.get('updateKey') is not None:
            self.update_key = m.get('updateKey')
        return self


class UpdateSnapshotResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentAndGenerateVendorConfigHeaders(TeaModel):
    def __init__(self, common_headers=None, client_token=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentAndGenerateVendorConfigHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateEnvironmentAndGenerateVendorConfigRequestPlatform(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentAndGenerateVendorConfigRequestPlatform, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class CreateEnvironmentAndGenerateVendorConfigRequest(TeaModel):
    def __init__(self, env_uid=None, platform=None, product_name=None, product_uid=None, product_version=None,
                 product_version_uid=None, vendor_type=None):
        self.env_uid = env_uid  # type: str
        self.platform = platform  # type: CreateEnvironmentAndGenerateVendorConfigRequestPlatform
        self.product_name = product_name  # type: str
        self.product_uid = product_uid  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        if self.platform:
            self.platform.validate()

    def to_map(self):
        _map = super(CreateEnvironmentAndGenerateVendorConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('platform') is not None:
            temp_model = CreateEnvironmentAndGenerateVendorConfigRequestPlatform()
            self.platform = temp_model.from_map(m['platform'])
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class CreateEnvironmentAndGenerateVendorConfigResponseBodyData(TeaModel):
    def __init__(self, env_uid=None, vendor_config=None):
        self.env_uid = env_uid  # type: str
        self.vendor_config = vendor_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentAndGenerateVendorConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        return self


class CreateEnvironmentAndGenerateVendorConfigResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: CreateEnvironmentAndGenerateVendorConfigResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEnvironmentAndGenerateVendorConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateEnvironmentAndGenerateVendorConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateEnvironmentAndGenerateVendorConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEnvironmentAndGenerateVendorConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEnvironmentAndGenerateVendorConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentAndGenerateVendorConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnvironmentSnapshotRequest(TeaModel):
    def __init__(self, description=None, name=None):
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateEnvironmentSnapshotResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnvironmentSnapshotResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class CreateEnvironmentSnapshotResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: CreateEnvironmentSnapshotResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEnvironmentSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateEnvironmentSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateEnvironmentSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEnvironmentSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEnvironmentSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEnvironmentSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitSnapshotInstanceResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitSnapshotInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class InitSnapshotInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InitSnapshotInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitSnapshotInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InitSnapshotInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductVersionRelatedFoundationVersionRequest(TeaModel):
    def __init__(self, foundation_version_uid=None):
        self.foundation_version_uid = foundation_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductVersionRelatedFoundationVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.foundation_version_uid is not None:
            result['foundationVersionUID'] = self.foundation_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('foundationVersionUID') is not None:
            self.foundation_version_uid = m.get('foundationVersionUID')
        return self


class UpdateProductVersionRelatedFoundationVersionResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProductVersionRelatedFoundationVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateProductVersionRelatedFoundationVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProductVersionRelatedFoundationVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProductVersionRelatedFoundationVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProductVersionRelatedFoundationVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentParamsRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, name=None, fuzzy=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.name = name  # type: str
        self.fuzzy = fuzzy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentParamsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.name is not None:
            result['name'] = self.name
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        return self


class ListEnvironmentParamsResponseBodyDataList(TeaModel):
    def __init__(self, created_at=None, description=None, id=None, name=None, product_name=None,
                 product_version=None, product_version_uid=None, uid=None, vendor_type=None):
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: int
        self.name = name  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str
        self.uid = uid  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentParamsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class ListEnvironmentParamsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListEnvironmentParamsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentParamsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentParamsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentParamsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: ListEnvironmentParamsResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentParamsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentParamsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentParamsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnvironmentParamsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentParamsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentParamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFoundationVersionResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: list[FoundationVersion]
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFoundationVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = FoundationVersion()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetFoundationVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFoundationVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFoundationVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFoundationVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductResponseBody(TeaModel):
    def __init__(self, err_message=None, success=None, err_code=None):
        self.err_message = err_message  # type: str
        self.success = success  # type: bool
        self.err_code = err_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['errCode'] = self.err_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        return self


class DeleteProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentRequest(TeaModel):
    def __init__(self, description=None, location=None, vendor_config=None):
        self.description = description  # type: str
        self.location = location  # type: str
        self.vendor_config = vendor_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.location is not None:
            result['location'] = self.location
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        return self


class UpdateEnvironmentResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateEnvironmentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEnvironmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEnvironmentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnvironmentPackageResponseBodyData(TeaModel):
    def __init__(self, package_url=None):
        self.package_url = package_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnvironmentPackageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        return self


class GetEnvironmentPackageResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetEnvironmentPackageResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnvironmentPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEnvironmentPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetEnvironmentPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnvironmentPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnvironmentPackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnvironmentPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductComponentDetailResponseBodyDataChildrenComponentVersionList(TeaModel):
    def __init__(self, app_version=None, category=None, class_=None, component_name=None, component_uid=None,
                 description=None, documents=None, enable=None, images_mapping=None, namespace=None, orchestration_values=None,
                 package_url=None, parent_component=None, priority=None, product_component_version_uid=None, provider=None,
                 readme=None, resources=None, singleton=None, uid=None, version=None):
        self.app_version = app_version  # type: str
        self.category = category  # type: str
        self.class_ = class_  # type: str
        self.component_name = component_name  # type: str
        self.component_uid = component_uid  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: list[str]
        self.enable = enable  # type: bool
        self.images_mapping = images_mapping  # type: str
        self.namespace = namespace  # type: str
        self.orchestration_values = orchestration_values  # type: str
        self.package_url = package_url  # type: str
        self.parent_component = parent_component  # type: bool
        self.priority = priority  # type: int
        self.product_component_version_uid = product_component_version_uid  # type: str
        self.provider = provider  # type: str
        self.readme = readme  # type: str
        self.resources = resources  # type: str
        self.singleton = singleton  # type: bool
        self.uid = uid  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductComponentDetailResponseBodyDataChildrenComponentVersionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        if self.class_ is not None:
            result['class'] = self.class_
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.enable is not None:
            result['enable'] = self.enable
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.priority is not None:
            result['priority'] = self.priority
        if self.product_component_version_uid is not None:
            result['productComponentVersionUID'] = self.product_component_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('productComponentVersionUID') is not None:
            self.product_component_version_uid = m.get('productComponentVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetProductComponentDetailResponseBodyData(TeaModel):
    def __init__(self, app_version=None, category=None, children_component_version_list=None, class_=None,
                 component_name=None, component_uid=None, description=None, documents=None, enable=None, has_dependency=None,
                 images_mapping=None, namespace=None, orchestration_values=None, package_url=None, parent_component=None,
                 priority=None, product_component_version_uid=None, provider=None, readme=None, resources=None,
                 singleton=None, uid=None, version=None):
        self.app_version = app_version  # type: str
        self.category = category  # type: str
        self.children_component_version_list = children_component_version_list  # type: list[GetProductComponentDetailResponseBodyDataChildrenComponentVersionList]
        self.class_ = class_  # type: str
        self.component_name = component_name  # type: str
        self.component_uid = component_uid  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: list[str]
        self.enable = enable  # type: bool
        self.has_dependency = has_dependency  # type: bool
        self.images_mapping = images_mapping  # type: str
        self.namespace = namespace  # type: str
        self.orchestration_values = orchestration_values  # type: str
        self.package_url = package_url  # type: str
        self.parent_component = parent_component  # type: bool
        self.priority = priority  # type: int
        self.product_component_version_uid = product_component_version_uid  # type: str
        self.provider = provider  # type: str
        self.readme = readme  # type: str
        self.resources = resources  # type: str
        self.singleton = singleton  # type: bool
        self.uid = uid  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.children_component_version_list:
            for k in self.children_component_version_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProductComponentDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.category is not None:
            result['category'] = self.category
        result['childrenComponentVersionList'] = []
        if self.children_component_version_list is not None:
            for k in self.children_component_version_list:
                result['childrenComponentVersionList'].append(k.to_map() if k else None)
        if self.class_ is not None:
            result['class'] = self.class_
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.enable is not None:
            result['enable'] = self.enable
        if self.has_dependency is not None:
            result['hasDependency'] = self.has_dependency
        if self.images_mapping is not None:
            result['imagesMapping'] = self.images_mapping
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.orchestration_values is not None:
            result['orchestrationValues'] = self.orchestration_values
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.parent_component is not None:
            result['parentComponent'] = self.parent_component
        if self.priority is not None:
            result['priority'] = self.priority
        if self.product_component_version_uid is not None:
            result['productComponentVersionUID'] = self.product_component_version_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.readme is not None:
            result['readme'] = self.readme
        if self.resources is not None:
            result['resources'] = self.resources
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('category') is not None:
            self.category = m.get('category')
        self.children_component_version_list = []
        if m.get('childrenComponentVersionList') is not None:
            for k in m.get('childrenComponentVersionList'):
                temp_model = GetProductComponentDetailResponseBodyDataChildrenComponentVersionList()
                self.children_component_version_list.append(temp_model.from_map(k))
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('hasDependency') is not None:
            self.has_dependency = m.get('hasDependency')
        if m.get('imagesMapping') is not None:
            self.images_mapping = m.get('imagesMapping')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('orchestrationValues') is not None:
            self.orchestration_values = m.get('orchestrationValues')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('parentComponent') is not None:
            self.parent_component = m.get('parentComponent')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('productComponentVersionUID') is not None:
            self.product_component_version_uid = m.get('productComponentVersionUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('readme') is not None:
            self.readme = m.get('readme')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetProductComponentDetailResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, success=None):
        self.data = data  # type: GetProductComponentDetailResponseBodyData
        self.err_code = err_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProductComponentDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductComponentDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductComponentDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductComponentDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductComponentDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductComponentDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportEnvironmentNodesRequest(TeaModel):
    def __init__(self, node_list_yaml=None):
        self.node_list_yaml = node_list_yaml  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportEnvironmentNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_list_yaml is not None:
            result['nodeListYaml'] = self.node_list_yaml
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nodeListYaml') is not None:
            self.node_list_yaml = m.get('nodeListYaml')
        return self


class ImportEnvironmentNodesResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportEnvironmentNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ImportEnvironmentNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ImportEnvironmentNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportEnvironmentNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportEnvironmentNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentsRequest(TeaModel):
    def __init__(self, name=None, category=None, page_num=None, page_size=None, fuzzy=None, public=None):
        self.name = name  # type: str
        self.category = category  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.fuzzy = fuzzy  # type: str
        self.public = public  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.category is not None:
            result['category'] = self.category
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.fuzzy is not None:
            result['fuzzy'] = self.fuzzy
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('fuzzy') is not None:
            self.fuzzy = m.get('fuzzy')
        if m.get('public') is not None:
            self.public = m.get('public')
        return self


class ListComponentsResponseBodyDataListAnnotations(TeaModel):
    def __init__(self, annotations=None):
        self.annotations = annotations  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsResponseBodyDataListAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        return self


class ListComponentsResponseBodyDataList(TeaModel):
    def __init__(self, annotations=None, category=None, description=None, documents=None, name=None, provider=None,
                 public=None, singleton=None, source=None, uid=None):
        self.annotations = annotations  # type: ListComponentsResponseBodyDataListAnnotations
        self.category = category  # type: str
        self.description = description  # type: str
        self.documents = documents  # type: str
        self.name = name  # type: str
        self.provider = provider  # type: str
        self.public = public  # type: bool
        self.singleton = singleton  # type: bool
        self.source = source  # type: str
        self.uid = uid  # type: str

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.documents is not None:
            result['documents'] = self.documents
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.public is not None:
            result['public'] = self.public
        if self.singleton is not None:
            result['singleton'] = self.singleton
        if self.source is not None:
            result['source'] = self.source
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = ListComponentsResponseBodyDataListAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('documents') is not None:
            self.documents = m.get('documents')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('singleton') is not None:
            self.singleton = m.get('singleton')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListComponentsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListComponentsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListComponentsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListComponentsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: ListComponentsResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListComponentsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListComponentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListComponentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListComponentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEnvironmentProductVersionHeaders(TeaModel):
    def __init__(self, common_headers=None, client_token=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEnvironmentProductVersionHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddEnvironmentProductVersionRequest(TeaModel):
    def __init__(self, product_name=None, product_uid=None, product_version=None, product_version_uid=None):
        self.product_name = product_name  # type: str
        self.product_uid = product_uid  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEnvironmentProductVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class AddEnvironmentProductVersionResponseBodyData(TeaModel):
    def __init__(self, uid=None):
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEnvironmentProductVersionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class AddEnvironmentProductVersionResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: AddEnvironmentProductVersionResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddEnvironmentProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = AddEnvironmentProductVersionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddEnvironmentProductVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddEnvironmentProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddEnvironmentProductVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddEnvironmentProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionsRequestPlatforms(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductVersionsRequestPlatforms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class ListProductVersionsRequest(TeaModel):
    def __init__(self, released=None, platforms=None):
        self.released = released  # type: bool
        self.platforms = platforms  # type: list[ListProductVersionsRequestPlatforms]

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.released is not None:
            result['released'] = self.released
        result['platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['platforms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('released') is not None:
            self.released = m.get('released')
        self.platforms = []
        if m.get('platforms') is not None:
            for k in m.get('platforms'):
                temp_model = ListProductVersionsRequestPlatforms()
                self.platforms.append(temp_model.from_map(k))
        return self


class ListProductVersionsShrinkRequest(TeaModel):
    def __init__(self, released=None, platforms_shrink=None):
        self.released = released  # type: bool
        self.platforms_shrink = platforms_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductVersionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.released is not None:
            result['released'] = self.released
        if self.platforms_shrink is not None:
            result['platforms'] = self.platforms_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('released') is not None:
            self.released = m.get('released')
        if m.get('platforms') is not None:
            self.platforms_shrink = m.get('platforms')
        return self


class ListProductVersionsResponseBodyDataListAnnotations(TeaModel):
    def __init__(self, additional_prop_1=None, additional_prop_2=None, additional_prop_3=None):
        self.additional_prop_1 = additional_prop_1  # type: str
        self.additional_prop_2 = additional_prop_2  # type: str
        self.additional_prop_3 = additional_prop_3  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductVersionsResponseBodyDataListAnnotations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_prop_1 is not None:
            result['additionalProp1'] = self.additional_prop_1
        if self.additional_prop_2 is not None:
            result['additionalProp2'] = self.additional_prop_2
        if self.additional_prop_3 is not None:
            result['additionalProp3'] = self.additional_prop_3
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('additionalProp1') is not None:
            self.additional_prop_1 = m.get('additionalProp1')
        if m.get('additionalProp2') is not None:
            self.additional_prop_2 = m.get('additionalProp2')
        if m.get('additionalProp3') is not None:
            self.additional_prop_3 = m.get('additionalProp3')
        return self


class ListProductVersionsResponseBodyDataList(TeaModel):
    def __init__(self, annotations=None, description=None, package_url=None, product_name=None, product_uid=None,
                 provider=None, uid=None, version=None):
        self.annotations = annotations  # type: ListProductVersionsResponseBodyDataListAnnotations
        self.description = description  # type: str
        self.package_url = package_url  # type: str
        self.product_name = product_name  # type: str
        self.product_uid = product_uid  # type: str
        self.provider = provider  # type: str
        self.uid = uid  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.annotations:
            self.annotations.validate()

    def to_map(self):
        _map = super(ListProductVersionsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.annotations is not None:
            result['annotations'] = self.annotations.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.package_url is not None:
            result['packageURL'] = self.package_url
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('annotations') is not None:
            temp_model = ListProductVersionsResponseBodyDataListAnnotations()
            self.annotations = temp_model.from_map(m['annotations'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('packageURL') is not None:
            self.package_url = m.get('packageURL')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListProductVersionsResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListProductVersionsResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProductVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListProductVersionsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListProductVersionsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: ListProductVersionsResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListProductVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListProductVersionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListProductVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProductVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChildrenComponentVersionListResponseBodyData(TeaModel):
    def __init__(self, cluster_id=None, created_at=None, description=None, instance_list=None, name=None,
                 product_name=None, product_version=None, uid=None, vendor_config=None, vendor_type=None):
        self.cluster_id = cluster_id  # type: str
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.instance_list = instance_list  # type: str
        self.name = name  # type: str
        self.product_name = product_name  # type: str
        self.product_version = product_version  # type: str
        self.uid = uid  # type: str
        self.vendor_config = vendor_config  # type: str
        self.vendor_type = vendor_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetChildrenComponentVersionListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        if self.name is not None:
            result['name'] = self.name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.uid is not None:
            result['uid'] = self.uid
        if self.vendor_config is not None:
            result['vendorConfig'] = self.vendor_config
        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('vendorConfig') is not None:
            self.vendor_config = m.get('vendorConfig')
        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')
        return self


class GetChildrenComponentVersionListResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetChildrenComponentVersionListResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetChildrenComponentVersionListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetChildrenComponentVersionListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetChildrenComponentVersionListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetChildrenComponentVersionListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetChildrenComponentVersionListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetChildrenComponentVersionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSLRHeaders(TeaModel):
    def __init__(self, common_headers=None, client_token=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSLRHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateSLRResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, error_code=None, success=None):
        self.data = data  # type: str
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSLRResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSLRResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSLRResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSLRResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionRelatedComponentVersionDetailResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: list[ProductComponentRelationDetail]
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProductVersionRelatedComponentVersionDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ProductComponentRelationDetail()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductVersionRelatedComponentVersionDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductVersionRelatedComponentVersionDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductVersionRelatedComponentVersionDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductVersionRelatedComponentVersionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEnvironmentPackageHeaders(TeaModel):
    def __init__(self, common_headers=None, client_token=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEnvironmentPackageHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddEnvironmentPackageRequest(TeaModel):
    def __init__(self, package_type=None):
        self.package_type = package_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEnvironmentPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_type is not None:
            result['packageType'] = self.package_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        return self


class AddEnvironmentPackageResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEnvironmentPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddEnvironmentPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddEnvironmentPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddEnvironmentPackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddEnvironmentPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnvironmentProductVersionRequest(TeaModel):
    def __init__(self, compatible_versions=None, old_product_version=None, old_product_version_uid=None,
                 product_name=None, product_uid=None, product_version=None, product_version_uid=None):
        self.compatible_versions = compatible_versions  # type: str
        self.old_product_version = old_product_version  # type: str
        self.old_product_version_uid = old_product_version_uid  # type: str
        self.product_name = product_name  # type: str
        self.product_uid = product_uid  # type: str
        self.product_version = product_version  # type: str
        self.product_version_uid = product_version_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentProductVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_versions is not None:
            result['compatibleVersions'] = self.compatible_versions
        if self.old_product_version is not None:
            result['oldProductVersion'] = self.old_product_version
        if self.old_product_version_uid is not None:
            result['oldProductVersionUID'] = self.old_product_version_uid
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_uid is not None:
            result['productUID'] = self.product_uid
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.product_version_uid is not None:
            result['productVersionUID'] = self.product_version_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('compatibleVersions') is not None:
            self.compatible_versions = m.get('compatibleVersions')
        if m.get('oldProductVersion') is not None:
            self.old_product_version = m.get('oldProductVersion')
        if m.get('oldProductVersionUID') is not None:
            self.old_product_version_uid = m.get('oldProductVersionUID')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productUID') is not None:
            self.product_uid = m.get('productUID')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('productVersionUID') is not None:
            self.product_version_uid = m.get('productVersionUID')
        return self


class UpdateEnvironmentProductVersionResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnvironmentProductVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateEnvironmentProductVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEnvironmentProductVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEnvironmentProductVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEnvironmentProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionPlatformsResponseBodyDataList(TeaModel):
    def __init__(self, architecture=None, os=None):
        self.architecture = architecture  # type: str
        self.os = os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductVersionPlatformsResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.os is not None:
            result['os'] = self.os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('os') is not None:
            self.os = m.get('os')
        return self


class GetProductVersionPlatformsResponseBodyData(TeaModel):
    def __init__(self, list=None):
        self.list = list  # type: list[GetProductVersionPlatformsResponseBodyDataList]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProductVersionPlatformsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetProductVersionPlatformsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        return self


class GetProductVersionPlatformsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetProductVersionPlatformsResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProductVersionPlatformsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductVersionPlatformsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductVersionPlatformsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductVersionPlatformsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductVersionPlatformsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductVersionPlatformsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveEnvironmentParamRequest(TeaModel):
    def __init__(self, component_uid=None, component_version_uid=None, name=None, param_uid=None, provider=None,
                 release_name=None, scope=None, value=None):
        self.component_uid = component_uid  # type: str
        self.component_version_uid = component_version_uid  # type: str
        self.name = name  # type: str
        self.param_uid = param_uid  # type: str
        self.provider = provider  # type: str
        self.release_name = release_name  # type: str
        self.scope = scope  # type: list[str]
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveEnvironmentParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_uid is not None:
            result['componentUID'] = self.component_uid
        if self.component_version_uid is not None:
            result['componentVersionUID'] = self.component_version_uid
        if self.name is not None:
            result['name'] = self.name
        if self.param_uid is not None:
            result['paramUID'] = self.param_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.release_name is not None:
            result['releaseName'] = self.release_name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentUID') is not None:
            self.component_uid = m.get('componentUID')
        if m.get('componentVersionUID') is not None:
            self.component_version_uid = m.get('componentVersionUID')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('paramUID') is not None:
            self.param_uid = m.get('paramUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SaveEnvironmentParamResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveEnvironmentParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SaveEnvironmentParamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SaveEnvironmentParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveEnvironmentParamResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveEnvironmentParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSnapshotInstanceJoinOptionRequest(TeaModel):
    def __init__(self, join_snapshot=None, root_password=None):
        self.join_snapshot = join_snapshot  # type: bool
        self.root_password = root_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSnapshotInstanceJoinOptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.join_snapshot is not None:
            result['joinSnapshot'] = self.join_snapshot
        if self.root_password is not None:
            result['rootPassword'] = self.root_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('joinSnapshot') is not None:
            self.join_snapshot = m.get('joinSnapshot')
        if m.get('rootPassword') is not None:
            self.root_password = m.get('rootPassword')
        return self


class UpdateSnapshotInstanceJoinOptionResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSnapshotInstanceJoinOptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateSnapshotInstanceJoinOptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSnapshotInstanceJoinOptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSnapshotInstanceJoinOptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSnapshotInstanceJoinOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionResourceResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductVersionResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductVersionResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductVersionResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductVersionResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductVersionResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLicenseRequest(TeaModel):
    def __init__(self, effective_year=None):
        # expire time
        self.effective_year = effective_year  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_year is not None:
            result['effectiveYear'] = self.effective_year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effectiveYear') is not None:
            self.effective_year = m.get('effectiveYear')
        return self


class CreateLicenseResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLicenseResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShareSnapshotRequest(TeaModel):
    def __init__(self, target_provider=None):
        self.target_provider = target_provider  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShareSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_provider is not None:
            result['targetProvider'] = self.target_provider
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('targetProvider') is not None:
            self.target_provider = m.get('targetProvider')
        return self


class ShareSnapshotResponseBodyData(TeaModel):
    def __init__(self, new_snapshot_uid=None):
        self.new_snapshot_uid = new_snapshot_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShareSnapshotResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_snapshot_uid is not None:
            result['newSnapshotUID'] = self.new_snapshot_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('newSnapshotUID') is not None:
            self.new_snapshot_uid = m.get('newSnapshotUID')
        return self


class ShareSnapshotResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: ShareSnapshotResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ShareSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ShareSnapshotResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ShareSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ShareSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ShareSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ShareSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnvironmentParamResponseBody(TeaModel):
    def __init__(self, err_message=None, success=None, err_code=None):
        self.err_message = err_message  # type: str
        self.success = success  # type: bool
        self.err_code = err_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnvironmentParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['errCode'] = self.err_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        return self


class DeleteEnvironmentParamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEnvironmentParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEnvironmentParamResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEnvironmentParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductResponseBodyData(TeaModel):
    def __init__(self, description=None, name=None, provider=None, uid=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.provider = provider  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProductResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetProductResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: GetProductResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteComponentVersionResponseBody(TeaModel):
    def __init__(self, err_message=None, success=None):
        self.err_message = err_message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteComponentVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteComponentVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteComponentVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteComponentVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteComponentVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployEnvironmentProductResponseBody(TeaModel):
    def __init__(self, err_code=None, err_msg=None, success=None):
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployEnvironmentProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployEnvironmentProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeployEnvironmentProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeployEnvironmentProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeployEnvironmentProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitEnvironmentResourceRequest(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitEnvironmentResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyID'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyID') is not None:
            self.access_key_id = m.get('accessKeyID')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        return self


class InitEnvironmentResourceResponseBodyData(TeaModel):
    def __init__(self, status=None):
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitEnvironmentResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class InitEnvironmentResourceResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: InitEnvironmentResourceResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InitEnvironmentResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = InitEnvironmentResourceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class InitEnvironmentResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InitEnvironmentResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitEnvironmentResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InitEnvironmentResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoundationVersionsResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: list[FoundationVersion]
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFoundationVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = FoundationVersion()
                self.data.append(temp_model.from_map(k))
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListFoundationVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFoundationVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFoundationVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFoundationVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvironmentDeployRecordRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentDeployRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListEnvironmentDeployRecordResponseBodyDataList(TeaModel):
    def __init__(self, env_uid=None, provider=None, status=None, uid=None):
        self.env_uid = env_uid  # type: str
        self.provider = provider  # type: str
        self.status = status  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnvironmentDeployRecordResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_uid is not None:
            result['envUID'] = self.env_uid
        if self.provider is not None:
            result['provider'] = self.provider
        if self.status is not None:
            result['status'] = self.status
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('envUID') is not None:
            self.env_uid = m.get('envUID')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnvironmentDeployRecordResponseBodyData(TeaModel):
    def __init__(self, list=None, page_num=None, page_size=None, total=None):
        self.list = list  # type: list[ListEnvironmentDeployRecordResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnvironmentDeployRecordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListEnvironmentDeployRecordResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEnvironmentDeployRecordResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_msg=None, success=None):
        self.data = data  # type: ListEnvironmentDeployRecordResponseBodyData
        self.err_code = err_code  # type: str
        self.err_msg = err_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListEnvironmentDeployRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEnvironmentDeployRecordResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnvironmentDeployRecordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnvironmentDeployRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnvironmentDeployRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnvironmentDeployRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


