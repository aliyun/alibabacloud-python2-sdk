# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AttachPolicyRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, policy_id=None, region_id=None,
                 resource_owner_account=None, target_id=None, target_type=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the tag policy.
        self.policy_id = policy_id  # type: str
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The ID of the object.
        # 
        # >  If you use the Tag Policy feature in single-account mode, this parameter is optional. If you use the Tag Policy feature in multi-account mode, this feature is required.
        self.target_id = target_id  # type: str
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # >  If you use the Tag Policy feature in single-account mode, this parameter is optional. If you use the Tag Policy feature in multi-account mode, this feature is required. The value of this parameter is not case-sensitive.
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class AttachPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachPolicyResponseBody, self).to_map()
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


class AttachPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachPolicyResponse, self).to_map()
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
            temp_model = AttachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCreatedByEnabledRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCreatedByEnabledRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckCreatedByEnabledResponseBody(TeaModel):
    def __init__(self, open_status=None, request_id=None):
        self.open_status = open_status  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCreatedByEnabledResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_status is not None:
            result['OpenStatus'] = self.open_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenStatus') is not None:
            self.open_status = m.get('OpenStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckCreatedByEnabledResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckCreatedByEnabledResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckCreatedByEnabledResponse, self).to_map()
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
            temp_model = CheckCreatedByEnabledResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseCreatedByRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseCreatedByRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CloseCreatedByResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseCreatedByResponseBody, self).to_map()
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


class CloseCreatedByResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloseCreatedByResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseCreatedByResponse, self).to_map()
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
            temp_model = CloseCreatedByResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(self, dry_run=None, owner_account=None, owner_id=None, policy_content=None, policy_desc=None,
                 policy_name=None, region_id=None, resource_owner_account=None, user_type=None):
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   false (default): performs a dry run and performs the actual request.
        # *   true: performs only a dry run.
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The document of the tag policy.
        # 
        # For more information about the syntax of a tag policy, see [Syntax of a tag policy](~~417436~~).
        self.policy_content = policy_content  # type: str
        # The description of the tag policy.
        # 
        # The description must be 0 to 512 characters in length.
        self.policy_desc = policy_desc  # type: str
        # The name of the tag policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and underscores (\_).
        self.policy_name = policy_name  # type: str
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The mode of the Tag Policy feature. Valid values:
        # 
        # *   USER: single-account mode. Set the value to USER if you use an Alibaba Cloud account or a member of a resource directory to call this API operation to create a tag policy for the Alibaba Cloud account or member.
        # *   RD: multi-account mode. Set the value to RD if you use the management account of a resource directory to call this API operation to create a tag policy for the resource directory.
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](~~417434~~).
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content
        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')
        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(self, policy_id=None, policy_name=None, request_id=None):
        # The ID of the tag policy.
        self.policy_id = policy_id  # type: str
        # The name of the tag policy.
        self.policy_name = policy_name  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePolicyResponse, self).to_map()
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
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagsRequestTagKeyValueParamListTagValueParamList(TeaModel):
    def __init__(self, description=None, value=None):
        # The description of the value for tag N.
        # 
        # Valid values of N: 1 to 10.
        self.description = description  # type: str
        # The value of tag N.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. 
        # 
        # Valid values of N: 1 to 10.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagsRequestTagKeyValueParamListTagValueParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTagsRequestTagKeyValueParamList(TeaModel):
    def __init__(self, description=None, key=None, tag_value_param_list=None):
        # The description of the key for tag N.
        # 
        # Valid values of N: 1 to 10.
        self.description = description  # type: str
        # The key of tag N.
        # 
        # The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        # 
        # Valid values of N: 1 to 10.
        self.key = key  # type: str
        # The information about the tag value.
        self.tag_value_param_list = tag_value_param_list  # type: list[CreateTagsRequestTagKeyValueParamListTagValueParamList]

    def validate(self):
        if self.tag_value_param_list:
            for k in self.tag_value_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTagsRequestTagKeyValueParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.key is not None:
            result['Key'] = self.key
        result['TagValueParamList'] = []
        if self.tag_value_param_list is not None:
            for k in self.tag_value_param_list:
                result['TagValueParamList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.tag_value_param_list = []
        if m.get('TagValueParamList') is not None:
            for k in m.get('TagValueParamList'):
                temp_model = CreateTagsRequestTagKeyValueParamListTagValueParamList()
                self.tag_value_param_list.append(temp_model.from_map(k))
        return self


class CreateTagsRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 tag_key_value_param_list=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        # 
        # > Only `cn-hangzhou` is supported.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The information about the tags.
        self.tag_key_value_param_list = tag_key_value_param_list  # type: list[CreateTagsRequestTagKeyValueParamList]

    def validate(self):
        if self.tag_key_value_param_list:
            for k in self.tag_key_value_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        result['TagKeyValueParamList'] = []
        if self.tag_key_value_param_list is not None:
            for k in self.tag_key_value_param_list:
                result['TagKeyValueParamList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        self.tag_key_value_param_list = []
        if m.get('TagKeyValueParamList') is not None:
            for k in m.get('TagKeyValueParamList'):
                temp_model = CreateTagsRequestTagKeyValueParamList()
                self.tag_key_value_param_list.append(temp_model.from_map(k))
        return self


class CreateTagsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagsResponseBody, self).to_map()
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


class CreateTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTagsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTagsResponse, self).to_map()
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
            temp_model = CreateTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, policy_id=None, region_id=None,
                 resource_owner_account=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the tag policy.
        self.policy_id = policy_id  # type: str
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DeletePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyResponseBody, self).to_map()
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


class DeletePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePolicyResponse, self).to_map()
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
            temp_model = DeletePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagRequest(TeaModel):
    def __init__(self, key=None, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 value=None):
        # The tag key.
        # 
        # If no tag value is associated with a tag key, you can specify the `Key` parameter without specifying the Value parameter to delete the tag key. Otherwise, you must specify both the `Key` and `Value` parameters to delete a preset tag.
        self.key = key  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        # 
        # >  Only `cn-hangzhou` is supported.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DeleteTagResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagResponseBody, self).to_map()
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


class DeleteTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTagResponse, self).to_map()
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
            temp_model = DeleteTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        # The supported natural language. Valid values:
        # 
        # *   zh-CN: Chinese (default value)
        # *   en-US: English
        # *   ja: Japanese
        self.accept_language = accept_language  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the region.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The endpoint of the Tag service in the region.
        self.region_endpoint = region_endpoint  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
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
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # The information of the regions.
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
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
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachPolicyRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, policy_id=None, region_id=None,
                 resource_owner_account=None, target_id=None, target_type=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the tag policy.
        self.policy_id = policy_id  # type: str
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The ID of the object.
        # 
        # >  If you use the Tag Policy feature in single-account mode, this parameter is optional. If you use the Tag Policy feature in multi-account mode, this feature is required.
        self.target_id = target_id  # type: str
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # >  If you use the Tag Policy feature in single-account mode, this parameter is optional. If you use the Tag Policy feature in multi-account mode, this feature is required. The value of this parameter is not case-sensitive.
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DetachPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachPolicyResponseBody, self).to_map()
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


class DetachPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachPolicyResponse, self).to_map()
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
            temp_model = DetachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisablePolicyTypeRequest(TeaModel):
    def __init__(self, open_type=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, user_type=None):
        self.open_type = open_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisablePolicyTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_type is not None:
            result['OpenType'] = self.open_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenType') is not None:
            self.open_type = m.get('OpenType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DisablePolicyTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisablePolicyTypeResponseBody, self).to_map()
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


class DisablePolicyTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisablePolicyTypeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisablePolicyTypeResponse, self).to_map()
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
            temp_model = DisablePolicyTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnablePolicyTypeRequest(TeaModel):
    def __init__(self, open_type=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, user_type=None):
        self.open_type = open_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnablePolicyTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_type is not None:
            result['OpenType'] = self.open_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenType') is not None:
            self.open_type = m.get('OpenType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class EnablePolicyTypeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnablePolicyTypeResponseBody, self).to_map()
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


class EnablePolicyTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnablePolicyTypeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnablePolicyTypeResponse, self).to_map()
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
            temp_model = EnablePolicyTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateConfigRuleReportRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 target_id=None, target_type=None, user_type=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The ID of the object.
        self.target_id = target_id  # type: str
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # >  The value of this parameter is not case-sensitive.
        self.target_type = target_type  # type: str
        # The mode of the Tag Policy feature. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](~~417434~~).
        # 
        # >  This parameter is required if the management account of your resource directory is used to enable the Tag Policy feature in both single-account mode and multi-account mode. The value of this parameter is not case-sensitive.
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateConfigRuleReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GenerateConfigRuleReportResponseBody(TeaModel):
    def __init__(self, report_id=None, request_id=None):
        # The ID of the resource non-compliance report.
        self.report_id = report_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateConfigRuleReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateConfigRuleReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateConfigRuleReportResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateConfigRuleReportResponse, self).to_map()
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
            temp_model = GenerateConfigRuleReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRuleReportRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 target_id=None, target_type=None, user_type=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The ID of the object.
        self.target_id = target_id  # type: str
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # >  The value of this parameter is not case-sensitive.
        self.target_type = target_type  # type: str
        # The mode of the Tag Policy feature. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](~~417434~~).
        # 
        # >  The value of this parameter is not case-sensitive.
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConfigRuleReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetConfigRuleReportResponseBodyData(TeaModel):
    def __init__(self, created_time=None, report_id=None, target_id=None, target_type=None):
        # The time when the report was generated. This value is a UNIX timestamp.
        self.created_time = created_time  # type: long
        # The ID of the report.
        self.report_id = report_id  # type: str
        # The ID of the object.
        # 
        # >  This parameter is returned if you set the `TargetType` and `TargetId` parameters in the current request to the same values as the parameters that are configured when you call the [GenerateConfigRuleReport](~~433313~~) operation to generate the report.
        self.target_id = target_id  # type: str
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # >  This parameter is returned if you set the `TargetType` and `TargetId` parameters in the current request to the same values as the parameters that are configured when you call the [GenerateConfigRuleReport](~~433313~~) operation to generate the report.
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConfigRuleReportResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetConfigRuleReportResponseBody(TeaModel):
    def __init__(self, data=None, http_status_code=None, request_id=None, success=None):
        # The basic information of the resource non-compliance report that is last generated.
        self.data = data  # type: GetConfigRuleReportResponseBodyData
        # The HTTP status code.
        self.http_status_code = http_status_code  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetConfigRuleReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetConfigRuleReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConfigRuleReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConfigRuleReportResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConfigRuleReportResponse, self).to_map()
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
            temp_model = GetConfigRuleReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEffectivePolicyRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 target_id=None, target_type=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The ID of the object.
        # 
        # >  If you use the Tag Policy feature in single-account mode, this parameter is optional. If you use the Tag Policy feature in multi-account mode, this feature is required.
        self.target_id = target_id  # type: str
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # >  If you use the Tag Policy feature in single-account mode, this parameter is optional. If you use the Tag Policy feature in multi-account mode, this feature is required. The value of this parameter is not case-sensitive.
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEffectivePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetEffectivePolicyResponseBody(TeaModel):
    def __init__(self, effective_policy=None, request_id=None):
        # The effective tag policy.
        self.effective_policy = effective_policy  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEffectivePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_policy is not None:
            result['EffectivePolicy'] = self.effective_policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EffectivePolicy') is not None:
            self.effective_policy = m.get('EffectivePolicy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEffectivePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEffectivePolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEffectivePolicyResponse, self).to_map()
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
            temp_model = GetEffectivePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, policy_id=None, region_id=None,
                 resource_owner_account=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the tag policy.
        self.policy_id = policy_id  # type: str
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class GetPolicyResponseBodyPolicy(TeaModel):
    def __init__(self, policy_content=None, policy_desc=None, policy_name=None, user_type=None):
        # The document of the tag policy.
        self.policy_content = policy_content  # type: str
        # The description of the tag policy.
        self.policy_desc = policy_desc  # type: str
        # The name of the tag policy.
        self.policy_name = policy_name  # type: str
        # The mode of the Tag Policy feature. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](~~417434~~).
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolicyResponseBodyPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content
        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')
        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetPolicyResponseBody(TeaModel):
    def __init__(self, policy=None, request_id=None):
        # The details of the tag policy.
        self.policy = policy  # type: GetPolicyResponseBodyPolicy
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(GetPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = GetPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPolicyResponse, self).to_map()
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
            temp_model = GetPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyEnableStatusRequest(TeaModel):
    def __init__(self, open_type=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, resource_owner_id=None, user_type=None):
        self.open_type = open_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        # The mode of the Tag Policy feature. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](~~417434~~).
        # 
        # >  The value of this parameter is not case-sensitive.
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolicyEnableStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_type is not None:
            result['OpenType'] = self.open_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenType') is not None:
            self.open_type = m.get('OpenType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetPolicyEnableStatusResponseBodyStatusModels(TeaModel):
    def __init__(self, status=None, user_type=None):
        # The status of the Tag Policy feature. Valid values:
        # 
        # *   PendingEnable: The feature is being enabled.
        # *   Enabled: The feature is enabled.
        # *   Closing: The feature is being disabled.
        # *   Disabled: The feature is disabled.
        self.status = status  # type: str
        # The mode of the Tag Policy feature. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](~~417434~~).
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPolicyEnableStatusResponseBodyStatusModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetPolicyEnableStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status_models=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the Tag Policy feature.
        self.status_models = status_models  # type: list[GetPolicyEnableStatusResponseBodyStatusModels]

    def validate(self):
        if self.status_models:
            for k in self.status_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPolicyEnableStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatusModels'] = []
        if self.status_models is not None:
            for k in self.status_models:
                result['StatusModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.status_models = []
        if m.get('StatusModels') is not None:
            for k in m.get('StatusModels'):
                temp_model = GetPolicyEnableStatusResponseBodyStatusModels()
                self.status_models.append(temp_model.from_map(k))
        return self


class GetPolicyEnableStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPolicyEnableStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPolicyEnableStatusResponse, self).to_map()
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
            temp_model = GetPolicyEnableStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigRulesForTargetRequest(TeaModel):
    def __init__(self, max_result=None, next_token=None, owner_account=None, owner_id=None, policy_type=None,
                 region_id=None, resource_owner_account=None, tag_key=None, target_id=None, target_type=None, user_type=None):
        # The number of entries to return on each page.
        # 
        # Default value: 50. Maximum value: 1000.
        self.max_result = max_result  # type: int
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The use scenario of the tag policy. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   tags: enables tags with specified tag values to be added to resources.
        # *   rg_inherit: enables resources in a resource group to automatically inherit tags from the resource group.
        self.policy_type = policy_type  # type: str
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The tag key. This parameter specifies a filter condition for the query.
        self.tag_key = tag_key  # type: str
        # The ID of the object. This parameter specifies a filter condition for the query.
        self.target_id = target_id  # type: str
        # The type of the object. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # >  The value of this parameter is not case-sensitive.
        self.target_type = target_type  # type: str
        # The mode of the Tag Policy feature. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](~~417434~~).
        # 
        # >  The value of this parameter is not case-sensitive.
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConfigRulesForTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class ListConfigRulesForTargetResponseBodyData(TeaModel):
    def __init__(self, aggregator_id=None, config_rule_id=None, policy_type=None, remediation=None, tag_key=None,
                 tag_value=None, target_id=None, target_type=None):
        # The ID of the account group.
        # 
        # You can use the ID to query the content of the related resource non-compliance report in Cloud Config.
        # 
        # >  This parameter is returned only if you use the Tag Policy feature in multi-account mode.
        self.aggregator_id = aggregator_id  # type: str
        # The ID of the rule.
        self.config_rule_id = config_rule_id  # type: str
        # The use scenario of the tag policy. Valid values:
        # 
        # *   tags: enables tags with specified tag values to be added to resources.
        # *   rg_inherit: enables resources in a resource group to automatically inherit tags from the resource group.
        self.policy_type = policy_type  # type: str
        # Indicates whether automatic remediation is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.remediation = remediation  # type: bool
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value for automatic remediation.
        self.tag_value = tag_value  # type: str
        # The ID of the object.
        self.target_id = target_id  # type: str
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConfigRulesForTargetResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.remediation is not None:
            result['Remediation'] = self.remediation
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('Remediation') is not None:
            self.remediation = m.get('Remediation')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListConfigRulesForTargetResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None, request_id=None):
        # The tag detection tasks.
        self.data = data  # type: list[ListConfigRulesForTargetResponseBodyData]
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConfigRulesForTargetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListConfigRulesForTargetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConfigRulesForTargetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConfigRulesForTargetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConfigRulesForTargetResponse, self).to_map()
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
            temp_model = ListConfigRulesForTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesRequest(TeaModel):
    def __init__(self, max_result=None, next_token=None, owner_account=None, owner_id=None, policy_ids=None,
                 policy_names=None, region_id=None, resource_owner_account=None, user_type=None):
        # The number of entries to return on each page.
        # 
        # Default value: 50. Maximum value: 1000.
        self.max_result = max_result  # type: int
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of a tag policy. This parameter specifies a filter condition for the query.
        self.policy_ids = policy_ids  # type: list[str]
        # The name of a tag policy. This parameter specifies a filter condition for the query.
        self.policy_names = policy_names  # type: list[str]
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The mode of the Tag Policy feature. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](~~417434~~).
        # 
        # >  The value of this parameter is not case-sensitive.
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class ListPoliciesResponseBodyPolicyList(TeaModel):
    def __init__(self, policy_content=None, policy_desc=None, policy_id=None, policy_name=None, user_type=None):
        # The document of the tag policy.
        self.policy_content = policy_content  # type: str
        # The description of the tag policy.
        self.policy_desc = policy_desc  # type: str
        # The ID of the tag policy.
        self.policy_id = policy_id  # type: str
        # The name of the tag policy.
        self.policy_name = policy_name  # type: str
        # The mode of the Tag Policy feature. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](~~417434~~).
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPoliciesResponseBodyPolicyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content
        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')
        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class ListPoliciesResponseBody(TeaModel):
    def __init__(self, next_token=None, policy_list=None, request_id=None):
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token  # type: str
        # The tag policies.
        self.policy_list = policy_list  # type: list[ListPoliciesResponseBodyPolicyList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy_list:
            for k in self.policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PolicyList'] = []
        if self.policy_list is not None:
            for k in self.policy_list:
                result['PolicyList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policy_list = []
        if m.get('PolicyList') is not None:
            for k in m.get('PolicyList'):
                temp_model = ListPoliciesResponseBodyPolicyList()
                self.policy_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPoliciesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPoliciesResponse, self).to_map()
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
            temp_model = ListPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesForTargetRequest(TeaModel):
    def __init__(self, max_result=None, next_token=None, owner_account=None, owner_id=None, region_id=None,
                 resource_owner_account=None, target_id=None, target_type=None):
        # The number of entries to return on each page.
        # 
        # Default value: 50. Maximum value: 1000.
        self.max_result = max_result  # type: int
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The ID of the object. This parameter specifies a filter condition for the query.
        self.target_id = target_id  # type: str
        # The type of the object. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in a resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # >  The value of this parameter is not case-sensitive.
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPoliciesForTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListPoliciesForTargetResponseBodyData(TeaModel):
    def __init__(self, policy_content=None, policy_desc=None, policy_id=None, policy_name=None, user_type=None):
        # The document of the tag policy.
        self.policy_content = policy_content  # type: str
        # The description of the tag policy.
        self.policy_desc = policy_desc  # type: str
        # The ID of the tag policy.
        self.policy_id = policy_id  # type: str
        # The name of the tag policy.
        self.policy_name = policy_name  # type: str
        # The mode of the Tag Policy feature. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](~~417434~~).
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPoliciesForTargetResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content
        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')
        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class ListPoliciesForTargetResponseBody(TeaModel):
    def __init__(self, data=None, next_token=None, request_id=None):
        # The tag policies that are attached to the object.
        self.data = data  # type: list[ListPoliciesForTargetResponseBodyData]
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPoliciesForTargetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPoliciesForTargetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPoliciesForTargetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPoliciesForTargetResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPoliciesForTargetResponse, self).to_map()
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
            temp_model = ListPoliciesForTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesByTagRequestTagFilter(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key. This parameter specifies a filter condition for the query.
        # 
        # The tag key can be a maximum of 128 characters in length. It cannot contain `http://` or `https://` and cannot start with `acs:` or `aliyun`.
        self.key = key  # type: str
        # The tag value. This parameter specifies a filter condition for the query.
        # 
        # The tag value can be a maximum of 128 characters in length. It cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesByTagRequestTagFilter, self).to_map()
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


class ListResourcesByTagRequest(TeaModel):
    def __init__(self, tag_filter=None, fuzzy_type=None, include_all_tags=None, max_result=None, next_token=None,
                 owner_account=None, owner_id=None, region_id=None, resource_owner_account=None, resource_type=None):
        self.tag_filter = tag_filter  # type: ListResourcesByTagRequestTagFilter
        # The type of the query. Valid values:
        # 
        # *   EQUAL: exact match for resources to which the specified tag is added. This is the default value.
        # *   NOT: exact match for resources to which the specified tag is not added.
        self.fuzzy_type = fuzzy_type  # type: str
        # Specifies whether to return the information of tags added to the resources. Valid values:
        # 
        # *   False: does not return the information of tags added to the resources. This is the default value.
        # *   True: returns the information of all tags added to the resources.
        self.include_all_tags = include_all_tags  # type: bool
        # The number of entries to return on each page.
        # 
        # Default value: 50. Maximum value: 1000.
        self.max_result = max_result  # type: int
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        # 
        # For more information about region IDs, see [Endpoints](~~2330902~~).
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The resource type. This parameter specifies a filter condition for the query.
        # 
        # *   If you set the FuzzyType parameter to EQUAL, you can set this parameter to a value obtained from the response of the [ListSupportResourceTypes](~~2330915~~) operation.
        # *   If you set the FuzzyType parameter to NOT, you can set this parameter to a resource type provided in **Types of resources that support queries based on the NOT operator**.
        self.resource_type = resource_type  # type: str

    def validate(self):
        if self.tag_filter:
            self.tag_filter.validate()

    def to_map(self):
        _map = super(ListResourcesByTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter.to_map()
        if self.fuzzy_type is not None:
            result['FuzzyType'] = self.fuzzy_type
        if self.include_all_tags is not None:
            result['IncludeAllTags'] = self.include_all_tags
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagFilter') is not None:
            temp_model = ListResourcesByTagRequestTagFilter()
            self.tag_filter = temp_model.from_map(m['TagFilter'])
        if m.get('FuzzyType') is not None:
            self.fuzzy_type = m.get('FuzzyType')
        if m.get('IncludeAllTags') is not None:
            self.include_all_tags = m.get('IncludeAllTags')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListResourcesByTagResponseBodyResourcesTags(TeaModel):
    def __init__(self, category=None, key=None, value=None):
        # The type of the tag. Valid values:
        # 
        # *   custom
        # *   system
        self.category = category  # type: str
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourcesByTagResponseBodyResourcesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListResourcesByTagResponseBodyResources(TeaModel):
    def __init__(self, resource_id=None, tags=None):
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The information of the tags.
        # 
        # This parameter is returned only if the `IncludeAllTags` parameter is set to `True`.
        self.tags = tags  # type: list[ListResourcesByTagResponseBodyResourcesTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourcesByTagResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListResourcesByTagResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListResourcesByTagResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, resources=None):
        # Indicates whether the `next query` is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the `next query` is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the `token` used to start the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the resources.
        self.resources = resources  # type: list[ListResourcesByTagResponseBodyResources]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourcesByTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListResourcesByTagResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListResourcesByTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourcesByTagResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourcesByTagResponse, self).to_map()
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
            temp_model = ListResourcesByTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSupportResourceTypesRequest(TeaModel):
    def __init__(self, max_result=None, next_token=None, owner_account=None, owner_id=None, product_code=None,
                 region_id=None, resource_owner_account=None, resource_tye=None, show_items=None, support_code=None):
        # The number of entries to return on each page.
        # 
        # Maximum value: 1000. Default value: 50.
        self.max_result = max_result  # type: int
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The service code. This parameter specifies a filter condition for the query.
        # 
        # This parameter is obtained from the response.
        self.product_code = product_code  # type: str
        # The region ID.
        # 
        # For more information about region IDs, see [Endpoints](~~2330902~~).
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The resource type. This parameter specifies a filter condition for the query.
        # 
        # This parameter is obtained from the response.
        self.resource_tye = resource_tye  # type: str
        # Specifies whether to return tag-related capability items. Valid values:
        # 
        # *   true: The system returns tag-related capability items.
        # *   false (default value): The system does not return tag-related capability items.
        self.show_items = show_items  # type: bool
        # The code of the tag-related capability item. This parameter specifies a filter condition for the query.
        # 
        # For more information, see **Tag-related capability items**.
        self.support_code = support_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSupportResourceTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_tye is not None:
            result['ResourceTye'] = self.resource_tye
        if self.show_items is not None:
            result['ShowItems'] = self.show_items
        if self.support_code is not None:
            result['SupportCode'] = self.support_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceTye') is not None:
            self.resource_tye = m.get('ResourceTye')
        if m.get('ShowItems') is not None:
            self.show_items = m.get('ShowItems')
        if m.get('SupportCode') is not None:
            self.support_code = m.get('SupportCode')
        return self


class ListSupportResourceTypesResponseBodySupportResourceTypesSupportItems(TeaModel):
    def __init__(self, support=None, support_code=None, support_details=None):
        # Indicates whether the tag-related capability item is supported. Valid values:
        # 
        # *   true
        # *   false
        self.support = support  # type: bool
        # The code of the tag-related capability item.
        self.support_code = support_code  # type: str
        # The details of the support for the tag-related capability item.
        self.support_details = support_details  # type: list[dict[str, str]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSupportResourceTypesResponseBodySupportResourceTypesSupportItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.support is not None:
            result['Support'] = self.support
        if self.support_code is not None:
            result['SupportCode'] = self.support_code
        if self.support_details is not None:
            result['SupportDetails'] = self.support_details
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Support') is not None:
            self.support = m.get('Support')
        if m.get('SupportCode') is not None:
            self.support_code = m.get('SupportCode')
        if m.get('SupportDetails') is not None:
            self.support_details = m.get('SupportDetails')
        return self


class ListSupportResourceTypesResponseBodySupportResourceTypes(TeaModel):
    def __init__(self, product_code=None, resource_type=None, support_items=None):
        # The service code.
        self.product_code = product_code  # type: str
        # The resource type.
        self.resource_type = resource_type  # type: str
        # The supported tag-related capability items.
        # 
        # >  This parameter is returned only if the `ShowItems` parameter is set to `true`.
        self.support_items = support_items  # type: list[ListSupportResourceTypesResponseBodySupportResourceTypesSupportItems]

    def validate(self):
        if self.support_items:
            for k in self.support_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSupportResourceTypesResponseBodySupportResourceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['SupportItems'] = []
        if self.support_items is not None:
            for k in self.support_items:
                result['SupportItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.support_items = []
        if m.get('SupportItems') is not None:
            for k in m.get('SupportItems'):
                temp_model = ListSupportResourceTypesResponseBodySupportResourceTypesSupportItems()
                self.support_items.append(temp_model.from_map(k))
        return self


class ListSupportResourceTypesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, support_resource_types=None):
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty, all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The supported resource types.
        self.support_resource_types = support_resource_types  # type: list[ListSupportResourceTypesResponseBodySupportResourceTypes]

    def validate(self):
        if self.support_resource_types:
            for k in self.support_resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSupportResourceTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SupportResourceTypes'] = []
        if self.support_resource_types is not None:
            for k in self.support_resource_types:
                result['SupportResourceTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.support_resource_types = []
        if m.get('SupportResourceTypes') is not None:
            for k in m.get('SupportResourceTypes'):
                temp_model = ListSupportResourceTypesResponseBodySupportResourceTypes()
                self.support_resource_types.append(temp_model.from_map(k))
        return self


class ListSupportResourceTypesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSupportResourceTypesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSupportResourceTypesResponse, self).to_map()
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
            temp_model = ListSupportResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequestTagFilter(TeaModel):
    def __init__(self, key=None):
        # The tag key.
        # 
        # This parameter is used together with the `FuzzyType` parameter.
        # 
        # >  This parameter is available only in the China (Shenzhen) and China (Hong Kong) regions.
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysRequestTagFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, tag_filter=None, category=None, fuzzy_type=None, next_token=None, owner_account=None,
                 owner_id=None, page_size=None, query_type=None, region_id=None, resource_owner_account=None,
                 resource_type=None):
        self.tag_filter = tag_filter  # type: ListTagKeysRequestTagFilter
        # The type of the resource tags. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   all (default value)
        # *   custom
        # *   system
        # 
        # >  The value of this parameter is not case-sensitive.
        self.category = category  # type: str
        # The type of the query. Valid values:
        # 
        # *   EQUAL: exact match. This is the default value.
        # *   PREFIX: prefix-based fuzzy match.
        # 
        # >  This parameter is available only in the China (Shenzhen) and China (Hong Kong) regions.
        self.fuzzy_type = fuzzy_type  # type: str
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of tag keys to return on each page.
        # 
        # Maximum value: 1000. Default value: 50.
        self.page_size = page_size  # type: int
        # The category of the tags. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   ResourceTag: resource tags, including custom and system tags. This is the default value.
        # *   MetaTag: preset tags.
        # 
        # >  The value of this parameter is not case-sensitive.
        self.query_type = query_type  # type: str
        # The region ID.
        # 
        # For more information about region IDs, see [Endpoints](~~2330902~~).
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The resource type. This parameter specifies a filter condition for the query.
        # 
        # Format: `ALIYUN::${ProductCode}::${ResourceType}`. All letters in the value of this parameter must be in uppercase.
        # 
        # *   `ProductCode`: the service code. You can set this field to a value obtained from the response of the [ListSupportResourceTypes](~~2330915~~) operation.
        # *   `ResourceType`: the resource type. You can set this field to a value obtained from the response of the [ListSupportResourceTypes](~~2330915~~) operation.
        self.resource_type = resource_type  # type: str

    def validate(self):
        if self.tag_filter:
            self.tag_filter.validate()

    def to_map(self):
        _map = super(ListTagKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter.to_map()
        if self.category is not None:
            result['Category'] = self.category
        if self.fuzzy_type is not None:
            result['FuzzyType'] = self.fuzzy_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagFilter') is not None:
            temp_model = ListTagKeysRequestTagFilter()
            self.tag_filter = temp_model.from_map(m['TagFilter'])
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('FuzzyType') is not None:
            self.fuzzy_type = m.get('FuzzyType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyKeysKey(TeaModel):
    def __init__(self, category=None, description=None, key=None):
        # The type of the resource tag. Valid values:
        # 
        # *   custom
        # *   system
        self.category = category  # type: str
        # The description of the tag key.
        self.description = description  # type: str
        # The tag key.
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysResponseBodyKeysKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.description is not None:
            result['Description'] = self.description
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagKeysResponseBodyKeys(TeaModel):
    def __init__(self, key=None):
        self.key = key  # type: list[ListTagKeysResponseBodyKeysKey]

    def validate(self):
        if self.key:
            for k in self.key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagKeysResponseBodyKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Key'] = []
        if self.key is not None:
            for k in self.key:
                result['Key'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.key = []
        if m.get('Key') is not None:
            for k in m.get('Key'):
                temp_model = ListTagKeysResponseBodyKeysKey()
                self.key.append(temp_model.from_map(k))
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(self, keys=None, next_token=None, request_id=None):
        # The information of the tag keys.
        self.keys = keys  # type: ListTagKeysResponseBodyKeys
        # Indicates whether the next query is required. The value of this parameter may be empty.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.keys:
            self.keys.validate()

    def to_map(self):
        _map = super(ListTagKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Keys') is not None:
            temp_model = ListTagKeysResponseBodyKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagKeysResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagKeysResponse, self).to_map()
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, category=None, next_token=None, owner_account=None, owner_id=None, page_size=None,
                 region_id=None, resource_arn=None, resource_owner_account=None, tags=None):
        # The type of the tag. Valid values:
        # 
        # *   Custom
        # *   System
        # *   All
        # 
        # Default value: All.
        self.category = category  # type: str
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of entries to return on each page.
        # 
        # Maximum value: 1000. Default value: 50.
        self.page_size = page_size  # type: int
        # The region ID.
        # 
        # *   If the resources belong to a service that is centrally deployed, set the value to the region ID of the resources by referring to [Regions supported by tag-related operations on resources of centrally deployed Alibaba Cloud services](~~2579691~~).
        # *   If the resources belong to a service that is not centrally deployed, set the value to the region ID of the resources.
        self.region_id = region_id  # type: str
        # The Alibaba Cloud Resource Name (ARN) of a resource.
        self.resource_arn = resource_arn  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        # The key-value pairs of tags. You can specify 1 to 10 key-value pairs.
        # 
        # If you specify multiple tags, the system queries the resources to which all these tags are added.
        # 
        # Limits:
        # 
        # *   A tag key must be 1 to 128 characters in length.
        # *   A tag value must be 1 to 128 characters in length.
        # *   Tag keys and tag values are case-sensitive.
        # *   Each tag key on a resource can have only one tag value. If you create a tag that has the same key as an existing tag, the value of the existing tag is overwritten.
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListTagResourcesResponseBodyTagResourcesTags(TeaModel):
    def __init__(self, category=None, key=None, value=None):
        # The type of the tag. Valid values:
        # 
        # *   Custom
        # *   System
        self.category = category  # type: str
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, resource_arn=None, tags=None):
        # The ARN of the resource.
        self.resource_arn = resource_arn  # type: str
        # The information of the tags.
        self.tags = tags  # type: list[ListTagResourcesResponseBodyTagResourcesTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        # Indicates whether the `next query` is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the `next query` is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the `token` used to start the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the tags that are added to the resources.
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequestTagFilter(TeaModel):
    def __init__(self, value=None):
        # The tag value.
        # 
        # This parameter is used together with the `FuzzyType` parameter.
        # 
        # >  This parameter is available only in the China (Shenzhen) and China (Hong Kong) regions.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagValuesRequestTagFilter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(self, tag_filter=None, fuzzy_type=None, key=None, next_token=None, owner_account=None,
                 owner_id=None, page_size=None, query_type=None, region_id=None, resource_owner_account=None,
                 resource_type=None):
        self.tag_filter = tag_filter  # type: ListTagValuesRequestTagFilter
        # The type of the query. Valid values:
        # 
        # *   EQUAL: exact match. This is the default value.
        # *   PREFIX: prefix-based fuzzy match.
        # 
        # >  This parameter is available only in the China (Shenzhen) and China (Hong Kong) regions.
        self.fuzzy_type = fuzzy_type  # type: str
        # The tag key. This parameter specifies a filter condition for the query.
        self.key = key  # type: str
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The number of tag values to return on each page.
        # 
        # Maximum value: 1000. Default value: 50.
        self.page_size = page_size  # type: int
        # The category of the tags. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   ResourceTag: resource tags, including custom and system tags. This is the default value.
        # *   MetaTag: preset tags.
        # 
        # >  The value of this parameter is not case-sensitive.
        self.query_type = query_type  # type: str
        # The region ID.
        # 
        # For more information about region IDs, see [Endpoints](~~2330902~~).
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        # The resource type. This parameter specifies a filter condition for the query.
        # 
        # Format: `ALIYUN::${ProductCode}::${ResourceType}`. All letters in the value of this parameter must be in uppercase.
        # 
        # *   `ProductCode`: the service code. You can set this field to a value obtained from the response of the [ListSupportResourceTypes](~~2330915~~) operation.
        # *   `ResourceType`: the resource type. You can set this field to a value obtained from the response of the [ListSupportResourceTypes](~~2330915~~) operation.
        self.resource_type = resource_type  # type: str

    def validate(self):
        if self.tag_filter:
            self.tag_filter.validate()

    def to_map(self):
        _map = super(ListTagValuesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter.to_map()
        if self.fuzzy_type is not None:
            result['FuzzyType'] = self.fuzzy_type
        if self.key is not None:
            result['Key'] = self.key
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagFilter') is not None:
            temp_model = ListTagValuesRequestTagFilter()
            self.tag_filter = temp_model.from_map(m['TagFilter'])
        if m.get('FuzzyType') is not None:
            self.fuzzy_type = m.get('FuzzyType')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagValuesResponseBodyValues(TeaModel):
    def __init__(self, value=None):
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagValuesResponseBodyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, values=None):
        # Indicates whether the next query is required. The value of this parameter may be empty.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the tag values.
        self.values = values  # type: ListTagValuesResponseBodyValues

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        _map = super(ListTagValuesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Values') is not None:
            temp_model = ListTagValuesResponseBodyValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagValuesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagValuesResponse, self).to_map()
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTargetsForPolicyRequest(TeaModel):
    def __init__(self, max_result=None, next_token=None, owner_account=None, owner_id=None, policy_id=None,
                 region_id=None, resource_owner_account=None):
        # The number of entries to return on each page.
        # 
        # Default value: 50. Maximum value: 1000.
        self.max_result = max_result  # type: int
        # The token that is used to start the next query.
        self.next_token = next_token  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The ID of the tag policy.
        self.policy_id = policy_id  # type: str
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTargetsForPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class ListTargetsForPolicyResponseBodyTargets(TeaModel):
    def __init__(self, target_id=None, target_type=None):
        # The ID of the object.
        self.target_id = target_id  # type: str
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        self.target_type = target_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTargetsForPolicyResponseBodyTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListTargetsForPolicyResponseBody(TeaModel):
    def __init__(self, is_rd=None, next_token=None, rd_id=None, request_id=None, targets=None):
        # Indicates whether the object belongs to the resource directory. Valid values:
        # 
        # *   true: The object belongs to the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   false: The object does not belong to the resource directory. This value is available if you use the Tag Policy feature in single-account mode.
        self.is_rd = is_rd  # type: bool
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token  # type: str
        # The ID of the resource directory.
        # 
        # >  This parameter is returned only if you use the Tag Policy feature in multi-account mode.
        self.rd_id = rd_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The objects to which the tag policy is attached.
        self.targets = targets  # type: list[ListTargetsForPolicyResponseBodyTargets]

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTargetsForPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_rd is not None:
            result['IsRd'] = self.is_rd
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.rd_id is not None:
            result['RdId'] = self.rd_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsRd') is not None:
            self.is_rd = m.get('IsRd')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RdId') is not None:
            self.rd_id = m.get('RdId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = ListTargetsForPolicyResponseBodyTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class ListTargetsForPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTargetsForPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTargetsForPolicyResponse, self).to_map()
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
            temp_model = ListTargetsForPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyRequest(TeaModel):
    def __init__(self, dry_run=None, owner_account=None, owner_id=None, policy_content=None, policy_desc=None,
                 policy_id=None, policy_name=None, region_id=None, resource_owner_account=None):
        # Specifies whether to perform a dry run for the request. Valid values:
        # 
        # *   false: The system performs the related operation based on the parameter settings in the request. This is the default value.
        # *   true: The system does not perform the related operation based on the parameter settings in the request but only verifies the parameter settings.
        self.dry_run = dry_run  # type: bool
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The document of the tag policy.
        # 
        # For more information about the syntax of a tag policy, see [Syntax of a tag policy](~~417436~~).
        self.policy_content = policy_content  # type: str
        # The description of the tag policy.
        # 
        # The description must be 0 to 512 characters in length.
        self.policy_desc = policy_desc  # type: str
        # The ID of the tag policy.
        self.policy_id = policy_id  # type: str
        # The name of the tag policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and underscores (\_).
        self.policy_name = policy_name  # type: str
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content
        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')
        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class ModifyPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyResponseBody, self).to_map()
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


class ModifyPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPolicyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPolicyResponse, self).to_map()
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
            temp_model = ModifyPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenCreatedByRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenCreatedByRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class OpenCreatedByResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenCreatedByResponseBody, self).to_map()
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


class OpenCreatedByResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenCreatedByResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenCreatedByResponse, self).to_map()
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
            temp_model = OpenCreatedByResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_arn=None,
                 resource_owner_account=None, tags=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        # 
        # *   If the resources belong to a service that is centrally deployed, set the value to `cn-hangzhou` or to the region ID of the resources by referring to [Regions supported by tag-related operations on resources of centrally deployed Alibaba Cloud services](~~2579691~~).
        # *   If the resources belong to a service that is not centrally deployed, set the value to the region ID of the resources.
        self.region_id = region_id  # type: str
        # The Alibaba Cloud Resource Name (ARN) of a resource.
        self.resource_arn = resource_arn  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        # The key-value pairs of tags. You can specify 1 to 10 key-value pairs.
        # 
        # If you specify multiple tags, the system adds all the tags to the specified resources.
        # 
        # Limits:
        # 
        # *   A tag key must be 1 to 128 characters in length.
        # *   A tag value must be 1 to 128 characters in length.
        # *   Tag keys and tag values are case-sensitive.
        # *   Each tag key on a resource can have only one tag value. If you create a tag that has the same key as an existing tag, the value of the existing tag is overwritten.
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagResourcesResponseBodyFailedResourcesFailedResourceResult(TeaModel):
    def __init__(self, code=None, message=None):
        # The error code.
        self.code = code  # type: str
        # The error message.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBodyFailedResourcesFailedResourceResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class TagResourcesResponseBodyFailedResourcesFailedResource(TeaModel):
    def __init__(self, resource_arn=None, result=None):
        # The ARN of the resource.
        self.resource_arn = resource_arn  # type: str
        # The information about the error.
        self.result = result  # type: TagResourcesResponseBodyFailedResourcesFailedResourceResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(TagResourcesResponseBodyFailedResourcesFailedResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('Result') is not None:
            temp_model = TagResourcesResponseBodyFailedResourcesFailedResourceResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class TagResourcesResponseBodyFailedResources(TeaModel):
    def __init__(self, failed_resource=None):
        self.failed_resource = failed_resource  # type: list[TagResourcesResponseBodyFailedResourcesFailedResource]

    def validate(self):
        if self.failed_resource:
            for k in self.failed_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesResponseBodyFailedResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedResource'] = []
        if self.failed_resource is not None:
            for k in self.failed_resource:
                result['FailedResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.failed_resource = []
        if m.get('FailedResource') is not None:
            for k in m.get('FailedResource'):
                temp_model = TagResourcesResponseBodyFailedResourcesFailedResource()
                self.failed_resource.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, failed_resources=None, request_id=None):
        # The information about the resources to which tags fail to be added.
        # 
        # > 
        # 
        # *   If tags are added to all resources, the value of `FailedResources` is empty.
        # 
        # *   If tags fail to be added to some or all resources, the value of `FailedResources` contains the detailed information about the resources.
        self.failed_resources = failed_resources  # type: TagResourcesResponseBodyFailedResources
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.failed_resources:
            self.failed_resources.validate()

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_resources is not None:
            result['FailedResources'] = self.failed_resources.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedResources') is not None:
            temp_model = TagResourcesResponseBodyFailedResources()
            self.failed_resources = temp_model.from_map(m['FailedResources'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, region_id=None, resource_arn=None,
                 resource_owner_account=None, tag_key=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        # The region ID.
        # 
        # *   If the resources belong to a service that is centrally deployed, set the value to `cn-hangzhou` or to the region ID of the resources by referring to [Regions supported by tag-related operations on resources of centrally deployed Alibaba Cloud services](~~2579691~~).
        # *   If the resources belong to a service that is not centrally deployed, set the value to the region ID of the resources.
        self.region_id = region_id  # type: str
        # The Alibaba Cloud Resource Name (ARN) of a resource.
        self.resource_arn = resource_arn  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        # A tag key.
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBodyFailedResourcesFailedResourceResult(TeaModel):
    def __init__(self, code=None, message=None):
        # The error code.
        self.code = code  # type: str
        # The error message.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBodyFailedResourcesFailedResourceResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UntagResourcesResponseBodyFailedResourcesFailedResource(TeaModel):
    def __init__(self, resource_arn=None, result=None):
        # The ARN of the resource.
        self.resource_arn = resource_arn  # type: str
        # The information about the error.
        self.result = result  # type: UntagResourcesResponseBodyFailedResourcesFailedResourceResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(UntagResourcesResponseBodyFailedResourcesFailedResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('Result') is not None:
            temp_model = UntagResourcesResponseBodyFailedResourcesFailedResourceResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UntagResourcesResponseBodyFailedResources(TeaModel):
    def __init__(self, failed_resource=None):
        self.failed_resource = failed_resource  # type: list[UntagResourcesResponseBodyFailedResourcesFailedResource]

    def validate(self):
        if self.failed_resource:
            for k in self.failed_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UntagResourcesResponseBodyFailedResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedResource'] = []
        if self.failed_resource is not None:
            for k in self.failed_resource:
                result['FailedResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.failed_resource = []
        if m.get('FailedResource') is not None:
            for k in m.get('FailedResource'):
                temp_model = UntagResourcesResponseBodyFailedResourcesFailedResource()
                self.failed_resource.append(temp_model.from_map(k))
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, failed_resources=None, request_id=None):
        # The information about the resources from which tags fail to be removed.
        # 
        # > 
        # 
        # *   If tags are removed from all resources, the value of FailedResources is empty.
        # 
        # *   If tags fail to be removed from some or all resources, the value of FailedResources contains the detailed information about the resources.
        self.failed_resources = failed_resources  # type: UntagResourcesResponseBodyFailedResources
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.failed_resources:
            self.failed_resources.validate()

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_resources is not None:
            result['FailedResources'] = self.failed_resources.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedResources') is not None:
            temp_model = UntagResourcesResponseBodyFailedResources()
            self.failed_resources = temp_model.from_map(m['FailedResources'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


