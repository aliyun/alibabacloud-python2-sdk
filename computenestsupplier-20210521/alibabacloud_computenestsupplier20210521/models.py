# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateArtifactRequestArtifactProperty(TeaModel):
    def __init__(self, commodity_code=None, commodity_version=None, file_script_metadata=None, image_id=None,
                 region_id=None, script_metadata=None, url=None):
        self.commodity_code = commodity_code  # type: str
        self.commodity_version = commodity_version  # type: str
        self.file_script_metadata = file_script_metadata  # type: str
        self.image_id = image_id  # type: str
        self.region_id = region_id  # type: str
        self.script_metadata = script_metadata  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateArtifactRequestArtifactProperty, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_version is not None:
            result['CommodityVersion'] = self.commodity_version
        if self.file_script_metadata is not None:
            result['FileScriptMetadata'] = self.file_script_metadata
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.script_metadata is not None:
            result['ScriptMetadata'] = self.script_metadata
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityVersion') is not None:
            self.commodity_version = m.get('CommodityVersion')
        if m.get('FileScriptMetadata') is not None:
            self.file_script_metadata = m.get('FileScriptMetadata')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScriptMetadata') is not None:
            self.script_metadata = m.get('ScriptMetadata')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateArtifactRequest(TeaModel):
    def __init__(self, artifact_id=None, artifact_property=None, artifact_type=None, description=None, name=None,
                 support_region_ids=None, version_name=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_property = artifact_property  # type: CreateArtifactRequestArtifactProperty
        self.artifact_type = artifact_type  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.support_region_ids = support_region_ids  # type: list[str]
        self.version_name = version_name  # type: str

    def validate(self):
        if self.artifact_property:
            self.artifact_property.validate()

    def to_map(self):
        _map = super(CreateArtifactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property.to_map()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            temp_model = CreateArtifactRequestArtifactProperty()
            self.artifact_property = temp_model.from_map(m['ArtifactProperty'])
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateArtifactShrinkRequest(TeaModel):
    def __init__(self, artifact_id=None, artifact_property_shrink=None, artifact_type=None, description=None,
                 name=None, support_region_ids=None, version_name=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_property_shrink = artifact_property_shrink  # type: str
        self.artifact_type = artifact_type  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.support_region_ids = support_region_ids  # type: list[str]
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateArtifactShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property_shrink is not None:
            result['ArtifactProperty'] = self.artifact_property_shrink
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property_shrink = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateArtifactResponseBody(TeaModel):
    def __init__(self, artifact_id=None, artifact_property=None, artifact_type=None, artifact_version=None,
                 description=None, gmt_modified=None, max_version=None, name=None, request_id=None, status=None,
                 support_region_ids=None, version_name=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_property = artifact_property  # type: str
        self.artifact_type = artifact_type  # type: str
        self.artifact_version = artifact_version  # type: str
        self.description = description  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.max_version = max_version  # type: long
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.support_region_ids = support_region_ids  # type: str
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateArtifactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateArtifactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateArtifactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateArtifactResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteArtifactRequest(TeaModel):
    def __init__(self, artifact_id=None, artifact_version=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_version = artifact_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteArtifactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        return self


class DeleteArtifactResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteArtifactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteArtifactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteArtifactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteArtifactResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactRequest(TeaModel):
    def __init__(self, artifact_id=None, artifact_version=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_version = artifact_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        return self


class GetArtifactResponseBody(TeaModel):
    def __init__(self, artifact_id=None, artifact_property=None, artifact_type=None, artifact_version=None,
                 description=None, gmt_modified=None, max_version=None, name=None, progress=None, request_id=None, status=None,
                 support_region_ids=None, version_name=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_property = artifact_property  # type: str
        self.artifact_type = artifact_type  # type: str
        self.artifact_version = artifact_version  # type: str
        self.description = description  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.max_version = max_version  # type: long
        self.name = name  # type: str
        self.progress = progress  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.support_region_ids = support_region_ids  # type: str
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetArtifactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetArtifactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetArtifactResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactRepositoryCredentialsRequest(TeaModel):
    def __init__(self, artifact_type=None, deploy_region_id=None):
        self.artifact_type = artifact_type  # type: str
        self.deploy_region_id = deploy_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactRepositoryCredentialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        return self


class GetArtifactRepositoryCredentialsResponseBodyAvailableResources(TeaModel):
    def __init__(self, path=None, region_id=None, repository_name=None):
        self.path = path  # type: str
        self.region_id = region_id  # type: str
        self.repository_name = repository_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactRepositoryCredentialsResponseBodyAvailableResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repository_name is not None:
            result['RepositoryName'] = self.repository_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepositoryName') is not None:
            self.repository_name = m.get('RepositoryName')
        return self


class GetArtifactRepositoryCredentialsResponseBodyCredentials(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, password=None, security_token=None,
                 username=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.password = password  # type: str
        self.security_token = security_token  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetArtifactRepositoryCredentialsResponseBodyCredentials, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.password is not None:
            result['Password'] = self.password
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetArtifactRepositoryCredentialsResponseBody(TeaModel):
    def __init__(self, available_resources=None, credentials=None, expire_date=None, request_id=None):
        self.available_resources = available_resources  # type: list[GetArtifactRepositoryCredentialsResponseBodyAvailableResources]
        self.credentials = credentials  # type: GetArtifactRepositoryCredentialsResponseBodyCredentials
        self.expire_date = expire_date  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.available_resources:
            for k in self.available_resources:
                if k:
                    k.validate()
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        _map = super(GetArtifactRepositoryCredentialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableResources'] = []
        if self.available_resources is not None:
            for k in self.available_resources:
                result['AvailableResources'].append(k.to_map() if k else None)
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_resources = []
        if m.get('AvailableResources') is not None:
            for k in m.get('AvailableResources'):
                temp_model = GetArtifactRepositoryCredentialsResponseBodyAvailableResources()
                self.available_resources.append(temp_model.from_map(k))
        if m.get('Credentials') is not None:
            temp_model = GetArtifactRepositoryCredentialsResponseBodyCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetArtifactRepositoryCredentialsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetArtifactRepositoryCredentialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetArtifactRepositoryCredentialsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetArtifactRepositoryCredentialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceInstanceRequest(TeaModel):
    def __init__(self, region_id=None, service_instance_id=None):
        self.region_id = region_id  # type: str
        self.service_instance_id = service_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs(TeaModel):
    def __init__(self, endpoint_ips=None, ingress_endpoint_status=None, network_service_status=None,
                 security_groups=None, v_switches=None, vpc_id=None):
        self.endpoint_ips = endpoint_ips  # type: list[str]
        self.ingress_endpoint_status = ingress_endpoint_status  # type: str
        self.network_service_status = network_service_status  # type: str
        self.security_groups = security_groups  # type: list[str]
        self.v_switches = v_switches  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_ips is not None:
            result['EndpointIps'] = self.endpoint_ips
        if self.ingress_endpoint_status is not None:
            result['IngressEndpointStatus'] = self.ingress_endpoint_status
        if self.network_service_status is not None:
            result['NetworkServiceStatus'] = self.network_service_status
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointIps') is not None:
            self.endpoint_ips = m.get('EndpointIps')
        if m.get('IngressEndpointStatus') is not None:
            self.ingress_endpoint_status = m.get('IngressEndpointStatus')
        if m.get('NetworkServiceStatus') is not None:
            self.network_service_status = m.get('NetworkServiceStatus')
        if m.get('SecurityGroups') is not None:
            self.security_groups = m.get('SecurityGroups')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections(TeaModel):
    def __init__(self, connection_configs=None, endpoint_id=None, endpoint_service_id=None, private_zone_name=None):
        self.connection_configs = connection_configs  # type: list[GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs]
        self.endpoint_id = endpoint_id  # type: str
        self.endpoint_service_id = endpoint_service_id  # type: str
        self.private_zone_name = private_zone_name  # type: str

    def validate(self):
        if self.connection_configs:
            for k in self.connection_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionConfigs'] = []
        if self.connection_configs is not None:
            for k in self.connection_configs:
                result['ConnectionConfigs'].append(k.to_map() if k else None)
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_service_id is not None:
            result['EndpointServiceId'] = self.endpoint_service_id
        if self.private_zone_name is not None:
            result['PrivateZoneName'] = self.private_zone_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connection_configs = []
        if m.get('ConnectionConfigs') is not None:
            for k in m.get('ConnectionConfigs'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs()
                self.connection_configs.append(temp_model.from_map(k))
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointServiceId') is not None:
            self.endpoint_service_id = m.get('EndpointServiceId')
        if m.get('PrivateZoneName') is not None:
            self.private_zone_name = m.get('PrivateZoneName')
        return self


class GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections(TeaModel):
    def __init__(self, endpoint_id=None, endpoint_service_id=None):
        self.endpoint_id = endpoint_id  # type: str
        self.endpoint_service_id = endpoint_service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_service_id is not None:
            result['EndpointServiceId'] = self.endpoint_service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointServiceId') is not None:
            self.endpoint_service_id = m.get('EndpointServiceId')
        return self


class GetServiceInstanceResponseBodyNetworkConfig(TeaModel):
    def __init__(self, endpoint_id=None, endpoint_service_id=None, private_vpc_connections=None,
                 reverse_private_vpc_connections=None):
        self.endpoint_id = endpoint_id  # type: str
        self.endpoint_service_id = endpoint_service_id  # type: str
        self.private_vpc_connections = private_vpc_connections  # type: list[GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections]
        self.reverse_private_vpc_connections = reverse_private_vpc_connections  # type: list[GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections]

    def validate(self):
        if self.private_vpc_connections:
            for k in self.private_vpc_connections:
                if k:
                    k.validate()
        if self.reverse_private_vpc_connections:
            for k in self.reverse_private_vpc_connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyNetworkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_service_id is not None:
            result['EndpointServiceId'] = self.endpoint_service_id
        result['PrivateVpcConnections'] = []
        if self.private_vpc_connections is not None:
            for k in self.private_vpc_connections:
                result['PrivateVpcConnections'].append(k.to_map() if k else None)
        result['ReversePrivateVpcConnections'] = []
        if self.reverse_private_vpc_connections is not None:
            for k in self.reverse_private_vpc_connections:
                result['ReversePrivateVpcConnections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointServiceId') is not None:
            self.endpoint_service_id = m.get('EndpointServiceId')
        self.private_vpc_connections = []
        if m.get('PrivateVpcConnections') is not None:
            for k in m.get('PrivateVpcConnections'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections()
                self.private_vpc_connections.append(temp_model.from_map(k))
        self.reverse_private_vpc_connections = []
        if m.get('ReversePrivateVpcConnections') is not None:
            for k in m.get('ReversePrivateVpcConnections'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections()
                self.reverse_private_vpc_connections.append(temp_model.from_map(k))
        return self


class GetServiceInstanceResponseBodyServiceServiceInfos(TeaModel):
    def __init__(self, image=None, locale=None, name=None, short_description=None):
        self.image = image  # type: str
        self.locale = locale  # type: str
        self.name = name  # type: str
        self.short_description = short_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyServiceServiceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class GetServiceInstanceResponseBodyService(TeaModel):
    def __init__(self, deploy_metadata=None, deploy_type=None, publish_time=None, service_doc_url=None,
                 service_id=None, service_infos=None, service_product_url=None, service_type=None, status=None,
                 supplier_name=None, supplier_url=None, version=None, version_name=None):
        self.deploy_metadata = deploy_metadata  # type: str
        self.deploy_type = deploy_type  # type: str
        self.publish_time = publish_time  # type: str
        self.service_doc_url = service_doc_url  # type: str
        self.service_id = service_id  # type: str
        self.service_infos = service_infos  # type: list[GetServiceInstanceResponseBodyServiceServiceInfos]
        self.service_product_url = service_product_url  # type: str
        self.service_type = service_type  # type: str
        self.status = status  # type: str
        self.supplier_name = supplier_name  # type: str
        self.supplier_url = supplier_url  # type: str
        self.version = version  # type: str
        self.version_name = version_name  # type: str

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyService, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.service_doc_url is not None:
            result['ServiceDocUrl'] = self.service_doc_url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_product_url is not None:
            result['ServiceProductUrl'] = self.service_product_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.version is not None:
            result['Version'] = self.version
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('ServiceDocUrl') is not None:
            self.service_doc_url = m.get('ServiceDocUrl')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceInstanceResponseBodyServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceProductUrl') is not None:
            self.service_product_url = m.get('ServiceProductUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetServiceInstanceResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceInstanceResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetServiceInstanceResponseBody(TeaModel):
    def __init__(self, create_time=None, enable_instance_ops=None, end_time=None, is_operated=None,
                 license_metadata=None, name=None, network_config=None, operated_service_instance_id=None, operation_end_time=None,
                 operation_start_time=None, outputs=None, parameters=None, pay_type=None, progress=None, request_id=None, resources=None,
                 service=None, service_instance_id=None, service_type=None, source=None, status=None, status_detail=None,
                 supplier_uid=None, tags=None, template_name=None, update_time=None, user_id=None):
        self.create_time = create_time  # type: str
        self.enable_instance_ops = enable_instance_ops  # type: bool
        self.end_time = end_time  # type: str
        self.is_operated = is_operated  # type: bool
        self.license_metadata = license_metadata  # type: str
        self.name = name  # type: str
        self.network_config = network_config  # type: GetServiceInstanceResponseBodyNetworkConfig
        self.operated_service_instance_id = operated_service_instance_id  # type: str
        self.operation_end_time = operation_end_time  # type: str
        self.operation_start_time = operation_start_time  # type: str
        self.outputs = outputs  # type: str
        self.parameters = parameters  # type: str
        self.pay_type = pay_type  # type: str
        self.progress = progress  # type: long
        self.request_id = request_id  # type: str
        self.resources = resources  # type: str
        self.service = service  # type: GetServiceInstanceResponseBodyService
        self.service_instance_id = service_instance_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.status_detail = status_detail  # type: str
        self.supplier_uid = supplier_uid  # type: long
        self.tags = tags  # type: list[GetServiceInstanceResponseBodyTags]
        self.template_name = template_name  # type: str
        self.update_time = update_time  # type: str
        self.user_id = user_id  # type: long

    def validate(self):
        if self.network_config:
            self.network_config.validate()
        if self.service:
            self.service.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_operated is not None:
            result['IsOperated'] = self.is_operated
        if self.license_metadata is not None:
            result['LicenseMetadata'] = self.license_metadata
        if self.name is not None:
            result['Name'] = self.name
        if self.network_config is not None:
            result['NetworkConfig'] = self.network_config.to_map()
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.supplier_uid is not None:
            result['SupplierUid'] = self.supplier_uid
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsOperated') is not None:
            self.is_operated = m.get('IsOperated')
        if m.get('LicenseMetadata') is not None:
            self.license_metadata = m.get('LicenseMetadata')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkConfig') is not None:
            temp_model = GetServiceInstanceResponseBodyNetworkConfig()
            self.network_config = temp_model.from_map(m['NetworkConfig'])
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Service') is not None:
            temp_model = GetServiceInstanceResponseBodyService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('SupplierUid') is not None:
            self.supplier_uid = m.get('SupplierUid')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetServiceInstanceResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetServiceInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServiceInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactVersionsRequest(TeaModel):
    def __init__(self, artifact_id=None, max_result=None, next_token=None):
        self.artifact_id = artifact_id  # type: str
        self.max_result = max_result  # type: str
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListArtifactVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListArtifactVersionsResponseBodyArtifacts(TeaModel):
    def __init__(self, artifact_id=None, artifact_property=None, artifact_type=None, artifact_version=None,
                 gmt_create=None, gmt_modified=None, image_delivery=None, progress=None, result_file=None,
                 security_audit_result=None, status=None, support_region_ids=None, version_name=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_property = artifact_property  # type: str
        self.artifact_type = artifact_type  # type: str
        self.artifact_version = artifact_version  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.image_delivery = image_delivery  # type: dict[str, str]
        self.progress = progress  # type: str
        self.result_file = result_file  # type: str
        self.security_audit_result = security_audit_result  # type: str
        self.status = status  # type: str
        self.support_region_ids = support_region_ids  # type: str
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListArtifactVersionsResponseBodyArtifacts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_delivery is not None:
            result['ImageDelivery'] = self.image_delivery
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.result_file is not None:
            result['ResultFile'] = self.result_file
        if self.security_audit_result is not None:
            result['SecurityAuditResult'] = self.security_audit_result
        if self.status is not None:
            result['Status'] = self.status
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageDelivery') is not None:
            self.image_delivery = m.get('ImageDelivery')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ResultFile') is not None:
            self.result_file = m.get('ResultFile')
        if m.get('SecurityAuditResult') is not None:
            self.security_audit_result = m.get('SecurityAuditResult')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class ListArtifactVersionsResponseBody(TeaModel):
    def __init__(self, artifacts=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.artifacts = artifacts  # type: list[ListArtifactVersionsResponseBodyArtifacts]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.artifacts:
            for k in self.artifacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListArtifactVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Artifacts'] = []
        if self.artifacts is not None:
            for k in self.artifacts:
                result['Artifacts'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.artifacts = []
        if m.get('Artifacts') is not None:
            for k in m.get('Artifacts'):
                temp_model = ListArtifactVersionsResponseBodyArtifacts()
                self.artifacts.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListArtifactVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListArtifactVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListArtifactVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListArtifactVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactsRequestFilter(TeaModel):
    def __init__(self, name=None, values=None):
        self.name = name  # type: str
        self.values = values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListArtifactsRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListArtifactsRequest(TeaModel):
    def __init__(self, filter=None, max_results=None, next_token=None):
        self.filter = filter  # type: list[ListArtifactsRequestFilter]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListArtifactsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListArtifactsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListArtifactsResponseBodyArtifacts(TeaModel):
    def __init__(self, artifact_id=None, artifact_type=None, description=None, gmt_modified=None, max_version=None,
                 name=None, status=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_type = artifact_type  # type: str
        self.description = description  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.max_version = max_version  # type: str
        self.name = name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListArtifactsResponseBodyArtifacts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListArtifactsResponseBody(TeaModel):
    def __init__(self, artifacts=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.artifacts = artifacts  # type: list[ListArtifactsResponseBodyArtifacts]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.artifacts:
            for k in self.artifacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListArtifactsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Artifacts'] = []
        if self.artifacts is not None:
            for k in self.artifacts:
                result['Artifacts'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.artifacts = []
        if m.get('Artifacts') is not None:
            for k in m.get('Artifacts'):
                temp_model = ListArtifactsResponseBodyArtifacts()
                self.artifacts.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListArtifactsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListArtifactsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListArtifactsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListArtifactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstancesRequestFilter(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServiceInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServiceInstancesRequest(TeaModel):
    def __init__(self, filter=None, max_results=None, next_token=None, region_id=None, tag=None):
        self.filter = filter  # type: list[ListServiceInstancesRequestFilter]
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.tag = tag  # type: list[ListServiceInstancesRequestTag]

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceInstancesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServiceInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos(TeaModel):
    def __init__(self, image=None, locale=None, name=None, short_description=None):
        self.image = image  # type: str
        self.locale = locale  # type: str
        self.name = name  # type: str
        self.short_description = short_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class ListServiceInstancesResponseBodyServiceInstancesService(TeaModel):
    def __init__(self, deploy_metadata=None, deploy_type=None, publish_time=None, service_id=None,
                 service_infos=None, service_type=None, status=None, supplier_name=None, supplier_url=None, version=None,
                 version_name=None):
        self.deploy_metadata = deploy_metadata  # type: str
        self.deploy_type = deploy_type  # type: str
        self.publish_time = publish_time  # type: str
        self.service_id = service_id  # type: str
        self.service_infos = service_infos  # type: list[ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos]
        self.service_type = service_type  # type: str
        self.status = status  # type: str
        self.supplier_name = supplier_name  # type: str
        self.supplier_url = supplier_url  # type: str
        self.version = version  # type: str
        self.version_name = version_name  # type: str

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstancesService, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.version is not None:
            result['Version'] = self.version
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class ListServiceInstancesResponseBodyServiceInstancesTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstancesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServiceInstancesResponseBodyServiceInstances(TeaModel):
    def __init__(self, create_time=None, enable_instance_ops=None, end_time=None, is_operated=None, name=None,
                 operated_service_instance_id=None, operation_end_time=None, operation_start_time=None, parameters=None, pay_type=None,
                 progress=None, service=None, service_instance_id=None, service_type=None, source=None, status=None,
                 status_detail=None, tags=None, template_name=None, update_time=None, user_id=None):
        self.create_time = create_time  # type: str
        self.enable_instance_ops = enable_instance_ops  # type: bool
        self.end_time = end_time  # type: str
        self.is_operated = is_operated  # type: bool
        self.name = name  # type: str
        self.operated_service_instance_id = operated_service_instance_id  # type: str
        self.operation_end_time = operation_end_time  # type: str
        self.operation_start_time = operation_start_time  # type: str
        self.parameters = parameters  # type: str
        self.pay_type = pay_type  # type: str
        self.progress = progress  # type: long
        self.service = service  # type: ListServiceInstancesResponseBodyServiceInstancesService
        self.service_instance_id = service_instance_id  # type: str
        self.service_type = service_type  # type: str
        self.source = source  # type: str
        self.status = status  # type: str
        self.status_detail = status_detail  # type: str
        self.tags = tags  # type: list[ListServiceInstancesResponseBodyServiceInstancesTags]
        self.template_name = template_name  # type: str
        self.update_time = update_time  # type: str
        self.user_id = user_id  # type: long

    def validate(self):
        if self.service:
            self.service.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponseBodyServiceInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_operated is not None:
            result['IsOperated'] = self.is_operated
        if self.name is not None:
            result['Name'] = self.name
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsOperated') is not None:
            self.is_operated = m.get('IsOperated')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Service') is not None:
            temp_model = ListServiceInstancesResponseBodyServiceInstancesService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListServiceInstancesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, service_instances=None, total_count=None):
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.service_instances = service_instances  # type: list[ListServiceInstancesResponseBodyServiceInstances]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.service_instances:
            for k in self.service_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceInstances'] = []
        if self.service_instances is not None:
            for k in self.service_instances:
                result['ServiceInstances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_instances = []
        if m.get('ServiceInstances') is not None:
            for k in m.get('ServiceInstances'):
                temp_model = ListServiceInstancesResponseBodyServiceInstances()
                self.service_instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServiceInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceUsagesRequestFilter(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceUsagesRequestFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServiceUsagesRequest(TeaModel):
    def __init__(self, filter=None, max_results=None, next_token=None):
        self.filter = filter  # type: list[ListServiceUsagesRequestFilter]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceUsagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceUsagesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListServiceUsagesResponseBodyServiceUsagesUserInformation(TeaModel):
    def __init__(self, company=None, country=None, email_address=None, industry=None, name=None, source=None,
                 telephone=None, title=None):
        self.company = company  # type: str
        self.country = country  # type: str
        self.email_address = email_address  # type: str
        self.industry = industry  # type: str
        self.name = name  # type: str
        self.source = source  # type: str
        self.telephone = telephone  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceUsagesResponseBodyServiceUsagesUserInformation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company is not None:
            result['Company'] = self.company
        if self.country is not None:
            result['Country'] = self.country
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        if self.telephone is not None:
            result['Telephone'] = self.telephone
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Company') is not None:
            self.company = m.get('Company')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListServiceUsagesResponseBodyServiceUsages(TeaModel):
    def __init__(self, comments=None, create_time=None, service_id=None, service_name=None, status=None,
                 supplier_name=None, update_time=None, user_ali_uid=None, user_information=None):
        self.comments = comments  # type: str
        self.create_time = create_time  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.status = status  # type: str
        self.supplier_name = supplier_name  # type: str
        self.update_time = update_time  # type: str
        self.user_ali_uid = user_ali_uid  # type: long
        self.user_information = user_information  # type: ListServiceUsagesResponseBodyServiceUsagesUserInformation

    def validate(self):
        if self.user_information:
            self.user_information.validate()

    def to_map(self):
        _map = super(ListServiceUsagesResponseBodyServiceUsages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid
        if self.user_information is not None:
            result['UserInformation'] = self.user_information.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')
        if m.get('UserInformation') is not None:
            temp_model = ListServiceUsagesResponseBodyServiceUsagesUserInformation()
            self.user_information = temp_model.from_map(m['UserInformation'])
        return self


class ListServiceUsagesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, service_usages=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.service_usages = service_usages  # type: list[ListServiceUsagesResponseBodyServiceUsages]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.service_usages:
            for k in self.service_usages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceUsagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceUsages'] = []
        if self.service_usages is not None:
            for k in self.service_usages:
                result['ServiceUsages'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_usages = []
        if m.get('ServiceUsages') is not None:
            for k in m.get('ServiceUsages'):
                temp_model = ListServiceUsagesResponseBodyServiceUsages()
                self.service_usages.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceUsagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServiceUsagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceUsagesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceUsagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseArtifactRequest(TeaModel):
    def __init__(self, artifact_id=None):
        self.artifact_id = artifact_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseArtifactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        return self


class ReleaseArtifactResponseBody(TeaModel):
    def __init__(self, artifact_id=None, artifact_property=None, artifact_type=None, artifact_version=None,
                 description=None, gmt_modified=None, request_id=None, status=None, version_name=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_property = artifact_property  # type: str
        self.artifact_type = artifact_type  # type: str
        self.artifact_version = artifact_version  # type: str
        self.description = description  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseArtifactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class ReleaseArtifactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseArtifactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseArtifactResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateArtifactRequestArtifactProperty(TeaModel):
    def __init__(self, commodity_code=None, commodity_version=None, file_script_metadata=None, image_id=None,
                 region_id=None, script_metadata=None, url=None):
        self.commodity_code = commodity_code  # type: str
        self.commodity_version = commodity_version  # type: str
        self.file_script_metadata = file_script_metadata  # type: str
        self.image_id = image_id  # type: str
        self.region_id = region_id  # type: str
        self.script_metadata = script_metadata  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateArtifactRequestArtifactProperty, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_version is not None:
            result['CommodityVersion'] = self.commodity_version
        if self.file_script_metadata is not None:
            result['FileScriptMetadata'] = self.file_script_metadata
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.script_metadata is not None:
            result['ScriptMetadata'] = self.script_metadata
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityVersion') is not None:
            self.commodity_version = m.get('CommodityVersion')
        if m.get('FileScriptMetadata') is not None:
            self.file_script_metadata = m.get('FileScriptMetadata')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScriptMetadata') is not None:
            self.script_metadata = m.get('ScriptMetadata')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateArtifactRequest(TeaModel):
    def __init__(self, artifact_id=None, artifact_property=None, description=None, support_region_ids=None,
                 version_name=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_property = artifact_property  # type: UpdateArtifactRequestArtifactProperty
        self.description = description  # type: str
        self.support_region_ids = support_region_ids  # type: list[str]
        self.version_name = version_name  # type: str

    def validate(self):
        if self.artifact_property:
            self.artifact_property.validate()

    def to_map(self):
        _map = super(UpdateArtifactRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            temp_model = UpdateArtifactRequestArtifactProperty()
            self.artifact_property = temp_model.from_map(m['ArtifactProperty'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateArtifactShrinkRequest(TeaModel):
    def __init__(self, artifact_id=None, artifact_property_shrink=None, description=None, support_region_ids=None,
                 version_name=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_property_shrink = artifact_property_shrink  # type: str
        self.description = description  # type: str
        self.support_region_ids = support_region_ids  # type: list[str]
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateArtifactShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property_shrink is not None:
            result['ArtifactProperty'] = self.artifact_property_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property_shrink = m.get('ArtifactProperty')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateArtifactResponseBody(TeaModel):
    def __init__(self, artifact_id=None, artifact_property=None, artifact_type=None, artifact_version=None,
                 description=None, gmt_modified=None, request_id=None, status=None, support_region_ids=None, version_name=None):
        self.artifact_id = artifact_id  # type: str
        self.artifact_property = artifact_property  # type: str
        self.artifact_type = artifact_type  # type: str
        self.artifact_version = artifact_version  # type: str
        self.description = description  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.support_region_ids = support_region_ids  # type: str
        self.version_name = version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateArtifactResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_id is not None:
            result['ArtifactId'] = self.artifact_id
        if self.artifact_property is not None:
            result['ArtifactProperty'] = self.artifact_property
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.artifact_version is not None:
            result['ArtifactVersion'] = self.artifact_version
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.support_region_ids is not None:
            result['SupportRegionIds'] = self.support_region_ids
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArtifactId') is not None:
            self.artifact_id = m.get('ArtifactId')
        if m.get('ArtifactProperty') is not None:
            self.artifact_property = m.get('ArtifactProperty')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('ArtifactVersion') is not None:
            self.artifact_version = m.get('ArtifactVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportRegionIds') is not None:
            self.support_region_ids = m.get('SupportRegionIds')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateArtifactResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateArtifactResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateArtifactResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


