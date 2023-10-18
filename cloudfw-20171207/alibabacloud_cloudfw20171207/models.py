# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddAddressBookRequestTagList(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The key of the tag.
        self.tag_key = tag_key  # type: str
        # The value of the tag.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAddressBookRequestTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class AddAddressBookRequest(TeaModel):
    def __init__(self, address_list=None, auto_add_tag_ecs=None, description=None, group_name=None, group_type=None,
                 lang=None, source_ip=None, tag_list=None, tag_relation=None):
        # The addresses that you want to add to the address book. Separate multiple addresses with commas (,).
        # 
        # > If you set GroupType to `ip`, `port` or `domain`, you must specify the AddressList parameter.
        # >
        # > * If you set GroupType to `ip`, you must add IP addresses to the address book. Example: 192.0.XX.XX/32, 192.0.XX.XX/24.
        # > * If you set GroupType to `port`, you must add port numbers or port ranges to the address book. Example: 80, 100/200.
        # > * If you set GroupType to `domain`, you must add domain names to the address book. Example: example.com, aliyundoc.com.
        self.address_list = address_list  # type: str
        # Specifies whether to automatically add public IP addresses of ECS instances to the address book if the instances match the specified tags. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no (default)
        self.auto_add_tag_ecs = auto_add_tag_ecs  # type: str
        # The description of the address book.
        self.description = description  # type: str
        # The name of the address book.
        self.group_name = group_name  # type: str
        # The type of the address book. Valid values:
        # 
        # * **ip**: IP address book
        # * **domain**: domain address book
        # * **port**: port address book
        # * **tag**: ECS tag-based address book
        self.group_type = group_type  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str
        # The ECS tags that you want to match.
        self.tag_list = tag_list  # type: list[AddAddressBookRequestTagList]
        # The logical relation among the ECS tags that you want to match. Valid values:
        # 
        # *   **and**: Only the public IP addresses of ECS instances that match all the specified tags can be added to the address book. This is the default value.
        # *   **or**: The public IP addresses of ECS instances that match one of the specified tags can be added to the address book.
        self.tag_relation = tag_relation  # type: str

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddAddressBookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_list is not None:
            result['AddressList'] = self.address_list
        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')
        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = AddAddressBookRequestTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')
        return self


class AddAddressBookResponseBody(TeaModel):
    def __init__(self, group_uuid=None, request_id=None):
        # The UUID of the returned address book.
        self.group_uuid = group_uuid  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAddressBookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddAddressBookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddAddressBookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAddressBookResponse, self).to_map()
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
            temp_model = AddAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddControlPolicyRequest(TeaModel):
    def __init__(self, acl_action=None, application_name=None, application_name_list=None, description=None,
                 dest_port=None, dest_port_group=None, dest_port_type=None, destination=None, destination_type=None,
                 direction=None, end_time=None, ip_version=None, lang=None, new_order=None, proto=None, release=None,
                 repeat_days=None, repeat_end_time=None, repeat_start_time=None, repeat_type=None, source=None, source_ip=None,
                 source_type=None, start_time=None):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action  # type: str
        # The application type supported by the access control policy. Valid values:
        # 
        # *   **FTP**\
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **Memcache**\
        # *   **MongoDB**\
        # *   **MQTT**\
        # *   **MySQL**\
        # *   **RDP**\
        # *   **Redis**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **SSH**\
        # *   **SSL_No_Cert**\
        # *   **SSL**\
        # *   **VNC**\
        # *   **ANY**\
        # 
        # > The value of this parameter is based on the value of Proto. If Proto is set to TCP, you can set ApplicationName to any valid value. If Proto is set to UDP, ICMP, or ANY, you can set ApplicationName only to ANY. You must specify at least one of the ApplicationNameList and ApplicationName parameters.
        self.application_name = application_name  # type: str
        # The application types supported by the access control policy.
        self.application_name_list = application_name_list  # type: list[str]
        # The description of the access control policy.
        self.description = description  # type: str
        # The destination port in the access control policy. Valid values:
        # 
        # *   If Proto is set to ICMP, DestPort is automatically left empty.
        # 
        # > If Proto is set to ICMP, access control does not take effect on the destination port.
        # 
        # *   If Proto is set to TCP, UDP, or ANY and DestPortType is set to group, DestPort is empty.
        # 
        # > If DestPortType is set to group, you do not need to specify the destination port number. All ports on which the access control policy takes effect are included in the destination port address book.
        # 
        # *   If Proto is set to TCP, UDP, or ANY and DestPortType is set to port, the value of DestPort is the destination port number.
        self.dest_port = dest_port  # type: str
        # The name of the destination port address book in the access control policy.
        # 
        # > If DestPortType is set to group, you must specify the name of the destination port address book.
        self.dest_port_group = dest_port_group  # type: str
        # The type of the destination port in the access control policy.
        # 
        # Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type  # type: str
        # The destination address in the access control policy.
        # 
        # Valid values:
        # 
        # *   If DestinationType is set to net, the value of this parameter is a CIDR block.
        # 
        #     Example: 1.2.XX.XX/24
        # 
        # *   If DestinationType is set to group, the value of this parameter is an address book name.
        # 
        #     Example: db_group
        # 
        # *   If DestinationType is set to domain, the value of this parameter is a domain name.
        # 
        #     Example: \*.aliyuncs.com
        # 
        # *   If DestinationType is set to location, the value of this parameter is a location.
        # 
        #     Example: \["BJ11", "ZB"]
        self.destination = destination  # type: str
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        # *   **location**: location
        self.destination_type = destination_type  # type: str
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        self.direction = direction  # type: str
        self.end_time = end_time  # type: long
        # The IP version supported by the access control policy.
        # 
        # Valid values:
        # 
        # *   **4**: IPv4
        # *   **6**: IPv6
        self.ip_version = ip_version  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The priority of the access control policy. The priority value starts from 1. A smaller priority value indicates a higher priority.
        self.new_order = new_order  # type: str
        # The protocol type supported by the access control policy. Valid values:
        # 
        # *   **ANY**\
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        self.proto = proto  # type: str
        # Specifies whether to enable the access control policy. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # *   **true**: enables the access control policy.
        # *   **false**: disables the access control policy.
        self.release = release  # type: str
        self.repeat_days = repeat_days  # type: list[long]
        self.repeat_end_time = repeat_end_time  # type: str
        self.repeat_start_time = repeat_start_time  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy. Valid values:
        # 
        # *   If SourceType is set to net, the value of this parameter is a CIDR block.
        # 
        #     Example: 1.1.XX.XX/24
        # 
        # *   If SourceType is set to group, the value of this parameter is an address book name.
        # 
        #     Example: db_group
        # 
        # *   If SourceType is set to location, the value of this parameter is a location.
        # 
        #     Example: \["BJ11", "ZB"]
        self.source = source  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str
        # The type of the source address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **location**: location
        self.source_type = source_type  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.repeat_end_time is not None:
            result['RepeatEndTime'] = self.repeat_end_time
        if self.repeat_start_time is not None:
            result['RepeatStartTime'] = self.repeat_start_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RepeatEndTime') is not None:
            self.repeat_end_time = m.get('RepeatEndTime')
        if m.get('RepeatStartTime') is not None:
            self.repeat_start_time = m.get('RepeatStartTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class AddControlPolicyResponseBody(TeaModel):
    def __init__(self, acl_uuid=None, request_id=None):
        # The ID of the access control policy that is created on the Internet firewall.
        self.acl_uuid = acl_uuid  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddControlPolicyResponse, self).to_map()
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
            temp_model = AddControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddInstanceMembersRequestMembers(TeaModel):
    def __init__(self, member_desc=None, member_uid=None):
        # The remarks of member that you want to add to Cloud Firewall. The remarks must be 1 to 256 characters in length.
        self.member_desc = member_desc  # type: str
        # The UID of member that you want to add to Cloud Firewall.
        self.member_uid = member_uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddInstanceMembersRequestMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        return self


class AddInstanceMembersRequest(TeaModel):
    def __init__(self, members=None):
        # The members that you want to add to Cloud Firewall.
        self.members = members  # type: list[AddInstanceMembersRequestMembers]

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddInstanceMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = AddInstanceMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        return self


class AddInstanceMembersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddInstanceMembersResponseBody, self).to_map()
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


class AddInstanceMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddInstanceMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddInstanceMembersResponse, self).to_map()
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
            temp_model = AddInstanceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCopyVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None, source_vpc_firewall_id=None, target_vpc_firewall_id=None):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str
        # The ID of the policy group of the source VPC firewall. Valid values:
        # 
        # *   If the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
        # *   If the VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter is the instance ID of the VPC firewall.
        # 
        # >  You can call the [DescribeVpcFirewallAclGroupList](~~159760~~) operation to query the IDs of policy groups.
        self.source_vpc_firewall_id = source_vpc_firewall_id  # type: str
        # The ID of the policy group of the destination VPC firewall. Valid values:
        # 
        # *   If the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance, the value of this parameter is the ID of the CEN instance. The network instance can be a VPC, a VBR, or a CCN instance.
        # *   If the VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter is the instance ID of the VPC firewall.
        # 
        # >  You can call the [DescribeVpcFirewallAclGroupList](~~159760~~) operation to query the IDs of policy groups.
        self.target_vpc_firewall_id = target_vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchCopyVpcFirewallControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source_vpc_firewall_id is not None:
            result['SourceVpcFirewallId'] = self.source_vpc_firewall_id
        if self.target_vpc_firewall_id is not None:
            result['TargetVpcFirewallId'] = self.target_vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SourceVpcFirewallId') is not None:
            self.source_vpc_firewall_id = m.get('SourceVpcFirewallId')
        if m.get('TargetVpcFirewallId') is not None:
            self.target_vpc_firewall_id = m.get('TargetVpcFirewallId')
        return self


class BatchCopyVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchCopyVpcFirewallControlPolicyResponseBody, self).to_map()
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


class BatchCopyVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchCopyVpcFirewallControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchCopyVpcFirewallControlPolicyResponse, self).to_map()
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
            temp_model = BatchCopyVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNatFirewallControlPolicyRequest(TeaModel):
    def __init__(self, acl_action=None, application_name_list=None, description=None, dest_port=None,
                 dest_port_group=None, dest_port_type=None, destination=None, destination_type=None, direction=None,
                 domain_resolve_type=None, end_time=None, ip_version=None, lang=None, nat_gateway_id=None, new_order=None, proto=None,
                 release=None, repeat_days=None, repeat_end_time=None, repeat_start_time=None, repeat_type=None,
                 source=None, source_type=None, start_time=None):
        # The action that Cloud Firewall performs on the traffic.
        # 
        # Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action  # type: str
        # The application types supported by the access control policy.
        self.application_name_list = application_name_list  # type: list[str]
        # The description of the access control policy.
        self.description = description  # type: str
        # The destination port in the access control policy. Valid values:
        # 
        # *   If Proto is set to ICMP, DestPort is automatically left empty.
        # 
        # > If Proto is set to ICMP, access control does not take effect on the destination port.
        # 
        # *   If Proto is set to TCP, UDP, or ANY and DestPortType is set to group, DestPort is empty.
        # 
        # > If DestPortType is set to group, you do not need to specify the destination port number. All ports on which the access control policy takes effect are included in the destination port address book.
        # 
        # *   If Proto is set to TCP, UDP, or ANY and DestPortType is set to port, the value of DestPort is the destination port number.
        self.dest_port = dest_port  # type: str
        # The name of the destination port address book in the access control policy.
        # 
        # > If DestPortType is set to group, you must specify the name of the destination port address book.
        self.dest_port_group = dest_port_group  # type: str
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type  # type: str
        # The destination address in the access control policy.
        # 
        # Valid values:
        # 
        # *   If DestinationType is set to net, the value of this parameter is a CIDR block.
        # 
        #     Example: 1.2.XX.XX/24
        # 
        # *   If DestinationType is set to group, the value of this parameter is an address book.
        # 
        #     Example: db_group
        # 
        # *   If DestinationType is set to domain, the value of this parameter is a domain name.
        # 
        #     Example: \*.aliyuncs.com
        # 
        # *   If DestinationType is set to location, the value of this parameter is a location.
        # 
        #     Example: \["BJ11", "ZB"]
        self.destination = destination  # type: str
        # The type of the destination address in the access control policy.
        # 
        # Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        self.destination_type = destination_type  # type: str
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **out**: outbound traffic
        self.direction = direction  # type: str
        # The domain name resolution method of the access control policy. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **0**: Fully qualified domain name (FQDN)-based resolution
        # *   **1**: Domain Name System (DNS)-based dynamic resolution
        # *   **2**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type  # type: int
        self.end_time = end_time  # type: long
        # The IP version supported by the access control policy. Valid values:
        # 
        # *   **4**: IPv4 (default)
        self.ip_version = ip_version  # type: str
        # The language of the content within the response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id  # type: str
        # The new priority of the access control policy.
        self.new_order = new_order  # type: str
        # The protocol type in the access control policy.
        # 
        # Valid values:
        # 
        # *   ANY: all types of protocols
        # *   TCP
        # *   UDP
        # *   ICMP
        self.proto = proto  # type: str
        # Specifies whether to enable the access control policy. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.release = release  # type: str
        self.repeat_days = repeat_days  # type: list[long]
        self.repeat_end_time = repeat_end_time  # type: str
        self.repeat_start_time = repeat_start_time  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy.
        # 
        # Valid values:
        # 
        # *   If **SourceType** is set to `net`, the value of Source is a CIDR block.
        # 
        #     Example: 10.2.4.0/24
        # 
        # *   If **SourceType** is set to `group`, the value of this parameter must be an address book name.
        # 
        #     Example: db_group
        self.source = source  # type: str
        # The type of the source address in the access control policy.
        # 
        # Valid values:
        # 
        # *   **net**: source CIDR block
        # *   **group**: source address book
        self.source_type = source_type  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNatFirewallControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.domain_resolve_type is not None:
            result['DomainResolveType'] = self.domain_resolve_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.repeat_end_time is not None:
            result['RepeatEndTime'] = self.repeat_end_time
        if self.repeat_start_time is not None:
            result['RepeatStartTime'] = self.repeat_start_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('DomainResolveType') is not None:
            self.domain_resolve_type = m.get('DomainResolveType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RepeatEndTime') is not None:
            self.repeat_end_time = m.get('RepeatEndTime')
        if m.get('RepeatStartTime') is not None:
            self.repeat_start_time = m.get('RepeatStartTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateNatFirewallControlPolicyResponseBody(TeaModel):
    def __init__(self, acl_uuid=None, request_id=None):
        # The UUID of the access control policy.
        # 
        # > If you want to modify an access control policy, you must provide the UUID of the policy. You can call the DescribeNatFirewallControlPolicy operation to query the UUIDs of access control policies.
        self.acl_uuid = acl_uuid  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNatFirewallControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNatFirewallControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNatFirewallControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNatFirewallControlPolicyResponse, self).to_map()
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
            temp_model = CreateNatFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrFirewallV2Request(TeaModel):
    def __init__(self, cen_id=None, firewall_description=None, firewall_name=None, firewall_subnet_cidr=None,
                 firewall_vpc_cidr=None, firewall_vpc_id=None, firewall_vswitch_id=None, lang=None, region_no=None, route_mode=None,
                 tr_attachment_master_cidr=None, tr_attachment_master_zone=None, tr_attachment_slave_cidr=None,
                 tr_attachment_slave_zone=None, transit_router_id=None):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id  # type: str
        # The description of the firewall.
        self.firewall_description = firewall_description  # type: str
        # The name of the firewall.
        self.firewall_name = firewall_name  # type: str
        # The subnet CIDR block of the VPC in which the ENI of the firewall is stored in automatic mode.
        self.firewall_subnet_cidr = firewall_subnet_cidr  # type: str
        # The CIDR block that is allocated to the VPC created for the VPC firewall in automatic mode.
        self.firewall_vpc_cidr = firewall_vpc_cidr  # type: str
        # The ID of the VPC in which the ENI associated with the VPC firewall is created in manual mode.
        self.firewall_vpc_id = firewall_vpc_id  # type: str
        # The ID of the vSwitch that is used to create the ENI in manual mode.
        self.firewall_vswitch_id = firewall_vswitch_id  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The region ID of the route router.
        self.region_no = region_no  # type: str
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode  # type: str
        # The primary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_master_cidr = tr_attachment_master_cidr  # type: str
        self.tr_attachment_master_zone = tr_attachment_master_zone  # type: str
        # The secondary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_slave_cidr = tr_attachment_slave_cidr  # type: str
        self.tr_attachment_slave_zone = tr_attachment_slave_zone  # type: str
        # The ID of the transit router.
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrFirewallV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.firewall_description is not None:
            result['FirewallDescription'] = self.firewall_description
        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name
        if self.firewall_subnet_cidr is not None:
            result['FirewallSubnetCidr'] = self.firewall_subnet_cidr
        if self.firewall_vpc_cidr is not None:
            result['FirewallVpcCidr'] = self.firewall_vpc_cidr
        if self.firewall_vpc_id is not None:
            result['FirewallVpcId'] = self.firewall_vpc_id
        if self.firewall_vswitch_id is not None:
            result['FirewallVswitchId'] = self.firewall_vswitch_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.tr_attachment_master_cidr is not None:
            result['TrAttachmentMasterCidr'] = self.tr_attachment_master_cidr
        if self.tr_attachment_master_zone is not None:
            result['TrAttachmentMasterZone'] = self.tr_attachment_master_zone
        if self.tr_attachment_slave_cidr is not None:
            result['TrAttachmentSlaveCidr'] = self.tr_attachment_slave_cidr
        if self.tr_attachment_slave_zone is not None:
            result['TrAttachmentSlaveZone'] = self.tr_attachment_slave_zone
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('FirewallDescription') is not None:
            self.firewall_description = m.get('FirewallDescription')
        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')
        if m.get('FirewallSubnetCidr') is not None:
            self.firewall_subnet_cidr = m.get('FirewallSubnetCidr')
        if m.get('FirewallVpcCidr') is not None:
            self.firewall_vpc_cidr = m.get('FirewallVpcCidr')
        if m.get('FirewallVpcId') is not None:
            self.firewall_vpc_id = m.get('FirewallVpcId')
        if m.get('FirewallVswitchId') is not None:
            self.firewall_vswitch_id = m.get('FirewallVswitchId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('TrAttachmentMasterCidr') is not None:
            self.tr_attachment_master_cidr = m.get('TrAttachmentMasterCidr')
        if m.get('TrAttachmentMasterZone') is not None:
            self.tr_attachment_master_zone = m.get('TrAttachmentMasterZone')
        if m.get('TrAttachmentSlaveCidr') is not None:
            self.tr_attachment_slave_cidr = m.get('TrAttachmentSlaveCidr')
        if m.get('TrAttachmentSlaveZone') is not None:
            self.tr_attachment_slave_zone = m.get('TrAttachmentSlaveZone')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class CreateTrFirewallV2ResponseBody(TeaModel):
    def __init__(self, firewall_id=None, request_id=None):
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrFirewallV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTrFirewallV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTrFirewallV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTrFirewallV2Response, self).to_map()
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
            temp_model = CreateTrFirewallV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrFirewallV2RoutePolicyRequestDestCandidateList(TeaModel):
    def __init__(self, candidate_id=None, candidate_type=None):
        self.candidate_id = candidate_id  # type: str
        self.candidate_type = candidate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrFirewallV2RoutePolicyRequestDestCandidateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class CreateTrFirewallV2RoutePolicyRequestSrcCandidateList(TeaModel):
    def __init__(self, candidate_id=None, candidate_type=None):
        self.candidate_id = candidate_id  # type: str
        self.candidate_type = candidate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrFirewallV2RoutePolicyRequestSrcCandidateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class CreateTrFirewallV2RoutePolicyRequest(TeaModel):
    def __init__(self, dest_candidate_list=None, firewall_id=None, lang=None, policy_description=None,
                 policy_name=None, policy_type=None, src_candidate_list=None):
        self.dest_candidate_list = dest_candidate_list  # type: list[CreateTrFirewallV2RoutePolicyRequestDestCandidateList]
        self.firewall_id = firewall_id  # type: str
        self.lang = lang  # type: str
        self.policy_description = policy_description  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.src_candidate_list = src_candidate_list  # type: list[CreateTrFirewallV2RoutePolicyRequestSrcCandidateList]

    def validate(self):
        if self.dest_candidate_list:
            for k in self.dest_candidate_list:
                if k:
                    k.validate()
        if self.src_candidate_list:
            for k in self.src_candidate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTrFirewallV2RoutePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DestCandidateList'] = []
        if self.dest_candidate_list is not None:
            for k in self.dest_candidate_list:
                result['DestCandidateList'].append(k.to_map() if k else None)
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        result['SrcCandidateList'] = []
        if self.src_candidate_list is not None:
            for k in self.src_candidate_list:
                result['SrcCandidateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dest_candidate_list = []
        if m.get('DestCandidateList') is not None:
            for k in m.get('DestCandidateList'):
                temp_model = CreateTrFirewallV2RoutePolicyRequestDestCandidateList()
                self.dest_candidate_list.append(temp_model.from_map(k))
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        self.src_candidate_list = []
        if m.get('SrcCandidateList') is not None:
            for k in m.get('SrcCandidateList'):
                temp_model = CreateTrFirewallV2RoutePolicyRequestSrcCandidateList()
                self.src_candidate_list.append(temp_model.from_map(k))
        return self


class CreateTrFirewallV2RoutePolicyShrinkRequest(TeaModel):
    def __init__(self, dest_candidate_list_shrink=None, firewall_id=None, lang=None, policy_description=None,
                 policy_name=None, policy_type=None, src_candidate_list_shrink=None):
        self.dest_candidate_list_shrink = dest_candidate_list_shrink  # type: str
        self.firewall_id = firewall_id  # type: str
        self.lang = lang  # type: str
        self.policy_description = policy_description  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.src_candidate_list_shrink = src_candidate_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrFirewallV2RoutePolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_candidate_list_shrink is not None:
            result['DestCandidateList'] = self.dest_candidate_list_shrink
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.src_candidate_list_shrink is not None:
            result['SrcCandidateList'] = self.src_candidate_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestCandidateList') is not None:
            self.dest_candidate_list_shrink = m.get('DestCandidateList')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('SrcCandidateList') is not None:
            self.src_candidate_list_shrink = m.get('SrcCandidateList')
        return self


class CreateTrFirewallV2RoutePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, tr_firewall_route_policy_id=None):
        self.request_id = request_id  # type: str
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTrFirewallV2RoutePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class CreateTrFirewallV2RoutePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTrFirewallV2RoutePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTrFirewallV2RoutePolicyResponse, self).to_map()
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
            temp_model = CreateTrFirewallV2RoutePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcFirewallCenConfigureRequest(TeaModel):
    def __init__(self, cen_id=None, firewall_switch=None, firewall_vswitch_cidr_block=None,
                 firewall_vpc_cidr_block=None, firewall_vpc_zone_id=None, lang=None, member_uid=None, network_instance_id=None,
                 v_switch_id=None, vpc_firewall_name=None, vpc_region=None):
        # The ID of the CEN instance.
        self.cen_id = cen_id  # type: str
        # Specifies whether to enable the VPC firewall. Valid values:
        # 
        # *   **open**: After you create the VPC firewall, the VPC firewall is automatically enabled. This is the default value.
        # *   **close**: After you create the VPC firewall, the VPC firewall is disabled. You can call the [ModifyVpcFirewallCenSwitchStatus](~~345780~~) operation to manually enable the VPC firewall.
        self.firewall_switch = firewall_switch  # type: str
        # The CIDR block of the vSwitch that is automatically created for the VPC firewall. You must specify a CIDR block for the Cloud_Firewall_VSWITCH VPC that is automatically created for the VPC firewall for traffic redirection. The CIDR block does not conflict with your network plan. The subnet mask of the CIDR block must be less than or equal to 29 bits in length. The CIDR block of the vSwitch must be within the network segment of the VPC.
        # 
        # If you do not specify a value, the CIDR block 10.219.219.216/29 is automatically allocated.
        # 
        # >  This parameter takes effect only when you create a VPC firewall for the first time in the current CEN instance and region.
        self.firewall_vswitch_cidr_block = firewall_vswitch_cidr_block  # type: str
        # The CIDR block of the VPC that is automatically created for the VPC firewall. You must specify a CIDR block for the Cloud_Firewall_VPC VPC that is automatically created for the VPC firewall for traffic redirection. The subnet mask of the CIDR block must be less than or equal to 28 bits in length.
        # 
        # If you do not specify a value, the CIDR block 10.0.0.0/8 is automatically allocated.
        # 
        # >  This parameter takes effect only when you create a VPC firewall for the first time in the current CEN instance and region.
        self.firewall_vpc_cidr_block = firewall_vpc_cidr_block  # type: str
        # The ID of the zone to which the vSwitch belongs. If your service is latency-sensitive, you can specify the same zone for the vSwitch of the firewall and the vSwitch of your business VPC to minimize latency.
        # 
        # If you do not specify a value, a zone is automatically assigned for the vSwitch.
        # 
        # >  This parameter takes effect only when you create a VPC firewall for the first time in the current CEN instance and region. For more information about zones that are supported by each region, see [Query zones](~~36064~~).
        self.firewall_vpc_zone_id = firewall_vpc_zone_id  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The ID of the VPC for which you want to create the VPC firewall.
        self.network_instance_id = network_instance_id  # type: str
        # The ID of the vSwitch that is used to associate with the elastic network interface (ENI) required by the VPC firewall.
        self.v_switch_id = v_switch_id  # type: str
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str
        # The ID of the region to which the VPC belongs.
        # 
        # > For more information about the regions, see [Supported regions](~~195657~~).
        self.vpc_region = vpc_region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcFirewallCenConfigureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch
        if self.firewall_vswitch_cidr_block is not None:
            result['FirewallVSwitchCidrBlock'] = self.firewall_vswitch_cidr_block
        if self.firewall_vpc_cidr_block is not None:
            result['FirewallVpcCidrBlock'] = self.firewall_vpc_cidr_block
        if self.firewall_vpc_zone_id is not None:
            result['FirewallVpcZoneId'] = self.firewall_vpc_zone_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        if self.vpc_region is not None:
            result['VpcRegion'] = self.vpc_region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')
        if m.get('FirewallVSwitchCidrBlock') is not None:
            self.firewall_vswitch_cidr_block = m.get('FirewallVSwitchCidrBlock')
        if m.get('FirewallVpcCidrBlock') is not None:
            self.firewall_vpc_cidr_block = m.get('FirewallVpcCidrBlock')
        if m.get('FirewallVpcZoneId') is not None:
            self.firewall_vpc_zone_id = m.get('FirewallVpcZoneId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        if m.get('VpcRegion') is not None:
            self.vpc_region = m.get('VpcRegion')
        return self


class CreateVpcFirewallCenConfigureResponseBody(TeaModel):
    def __init__(self, request_id=None, vpc_firewall_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcFirewallCenConfigureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class CreateVpcFirewallCenConfigureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVpcFirewallCenConfigureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpcFirewallCenConfigureResponse, self).to_map()
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
            temp_model = CreateVpcFirewallCenConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcFirewallConfigureRequest(TeaModel):
    def __init__(self, firewall_switch=None, lang=None, local_vpc_cidr_table_list=None, local_vpc_id=None,
                 local_vpc_region=None, member_uid=None, peer_vpc_cidr_table_list=None, peer_vpc_id=None, peer_vpc_region=None,
                 vpc_firewall_name=None):
        # The status of the VPC firewall after you create the firewall. Valid values:
        # 
        # *   **open**: After you create the VPC firewall, the firewall is automatically enabled. This is the default value.
        # *   **close**: After you create the VPC firewall, the firewall is not automatically enabled. To enable the firewall, you can call the [ModifyVpcFirewallSwitchStatus](~~342935~~) operation.
        self.firewall_switch = firewall_switch  # type: str
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The CIDR blocks of the local VPC. The value is a JSON string that contains the following parameters:
        # 
        # *   **RouteTableId**: the ID of the route table for the local VPC.
        # *   **RouteEntryList**: The value is a JSON string that contains the DestinationCidr and NextHopInstanceId parameters. The DestinationCidr parameter indicates the destination CIDR block of the local VPC. The NextHopInstanceId parameter indicates the instance ID of the next hop for the local VPC.
        self.local_vpc_cidr_table_list = local_vpc_cidr_table_list  # type: str
        # The ID of the local VPC.
        self.local_vpc_id = local_vpc_id  # type: str
        # The region ID of the local VPC.
        # 
        # >  For more information about regions in which Cloud Firewall is supported, see [Supported regions](~~195657~~).
        self.local_vpc_region = local_vpc_region  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The CIDR blocks of the peer VPC. The value is a JSON string that contains the following parameters:
        # 
        # *   **RouteTableId**: the ID of the route table for the peer VPC.
        # *   **RouteEntryList**: The value is a JSON string that contains the DestinationCidr and NextHopInstanceId parameters. The DestinationCidr parameter indicates the destination CIDR block of the peer VPC. The NextHopInstanceId parameter indicates the instance ID of the next hop for the peer VPC.
        self.peer_vpc_cidr_table_list = peer_vpc_cidr_table_list  # type: str
        # The ID of the peer VPC.
        self.peer_vpc_id = peer_vpc_id  # type: str
        # The region ID of the peer VPC.
        # 
        # >  For more information about regions in which Cloud Firewall is supported, see [Supported regions](~~195657~~).
        self.peer_vpc_region = peer_vpc_region  # type: str
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcFirewallConfigureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.local_vpc_cidr_table_list is not None:
            result['LocalVpcCidrTableList'] = self.local_vpc_cidr_table_list
        if self.local_vpc_id is not None:
            result['LocalVpcId'] = self.local_vpc_id
        if self.local_vpc_region is not None:
            result['LocalVpcRegion'] = self.local_vpc_region
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.peer_vpc_cidr_table_list is not None:
            result['PeerVpcCidrTableList'] = self.peer_vpc_cidr_table_list
        if self.peer_vpc_id is not None:
            result['PeerVpcId'] = self.peer_vpc_id
        if self.peer_vpc_region is not None:
            result['PeerVpcRegion'] = self.peer_vpc_region
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LocalVpcCidrTableList') is not None:
            self.local_vpc_cidr_table_list = m.get('LocalVpcCidrTableList')
        if m.get('LocalVpcId') is not None:
            self.local_vpc_id = m.get('LocalVpcId')
        if m.get('LocalVpcRegion') is not None:
            self.local_vpc_region = m.get('LocalVpcRegion')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PeerVpcCidrTableList') is not None:
            self.peer_vpc_cidr_table_list = m.get('PeerVpcCidrTableList')
        if m.get('PeerVpcId') is not None:
            self.peer_vpc_id = m.get('PeerVpcId')
        if m.get('PeerVpcRegion') is not None:
            self.peer_vpc_region = m.get('PeerVpcRegion')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class CreateVpcFirewallConfigureResponseBody(TeaModel):
    def __init__(self, request_id=None, vpc_firewall_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcFirewallConfigureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class CreateVpcFirewallConfigureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVpcFirewallConfigureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpcFirewallConfigureResponse, self).to_map()
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
            temp_model = CreateVpcFirewallConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(self, acl_action=None, application_name=None, application_name_list=None, description=None,
                 dest_port=None, dest_port_group=None, dest_port_type=None, destination=None, destination_type=None,
                 end_time=None, lang=None, member_uid=None, new_order=None, proto=None, release=None, repeat_days=None,
                 repeat_end_time=None, repeat_start_time=None, repeat_type=None, source=None, source_type=None, start_time=None,
                 vpc_firewall_id=None):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # - **accept**: allows the traffic.
        # - **drop**: blocks the traffic.
        # - **log**: monitors the traffic.
        self.acl_action = acl_action  # type: str
        # The type of the applications that the access control policy supports. Valid values:
        # 
        # - **FTP**\
        # - **HTTP**\
        # - **HTTPS**\
        # - **MySQL**\
        # - **SMTP**\
        # - **SMTPS**\
        # - **RDP**\
        # - **VNC**\
        # - **SSH**\
        # - **Redis**\
        # - **MQTT**\
        # - **MongoDB**\
        # - **Memcache**\
        # - **SSL**\
        # - **ANY**: all types of applications
        self.application_name = application_name  # type: str
        self.application_name_list = application_name_list  # type: list[str]
        # The description of the access control policy.
        self.description = description  # type: str
        # The destination port in the access control policy. 
        # 
        # >  If **DestPortType** is set to `port`, you must specify this parameter.
        self.dest_port = dest_port  # type: str
        # The name of the destination port address book in the access control policy. 
        # 
        # >  If **DestPortType** is set to `group`, you must specify this parameter.
        self.dest_port_group = dest_port_group  # type: str
        # The type of the destination port in the access control policy. Valid values:
        # 
        # - **port**: port
        # - **group**: port address book
        self.dest_port_type = dest_port_type  # type: str
        # The destination address in the access control policy. Valid values:
        # 
        # - If **DestinationType** is set to `net`, the value of **Destination** must be a CIDR block.
        # - If **DestinationType** is set to `group`, the value of **Destination** must be an address book.
        # - If **DestinationType** is set to `domain`, the value of **Destination** must be a domain name.
        self.destination = destination  # type: str
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: CIDR block
        # - **group**: address book
        # - **domain**: domain name
        self.destination_type = destination_type  # type: str
        self.end_time = end_time  # type: long
        # The language of the content within the request and response. Valid values:
        # 
        # - **zh**: Chinese (default)
        # - **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The priority of the access control policy. 
        # 
        # The priority value starts from 1. A smaller priority value indicates a higher priority.
        self.new_order = new_order  # type: str
        # The type of the protocol in the access control policy. Valid values:
        # 
        # - **ANY** (If you are not sure about the protocol type, you can set this parameter to ANY.)
        # - **TCP**\
        # - **UDP**\
        # - **ICMP**\
        self.proto = proto  # type: str
        # Specifies whether to enable the access control policy. By default, an access control policy is enabled after the policy is created. Valid values: 
        # 
        # - **true**: enables the access control policy.
        # - **false**: disables the access control policy.
        self.release = release  # type: str
        self.repeat_days = repeat_days  # type: list[long]
        self.repeat_end_time = repeat_end_time  # type: str
        self.repeat_start_time = repeat_start_time  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy. 
        # 
        # - If SourceType is set to `net`, the value of Source must be a CIDR block.
        # - If SourceType is set to `group`, the value of Source must be an address book.
        self.source = source  # type: str
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: CIDR block
        # - **group**: address book
        self.source_type = source_type  # type: str
        self.start_time = start_time  # type: long
        # The ID of the policy group in which you want to create the access control policy. 
        # 
        # - If a VPC firewall protects the traffic between two VPCs that are connected by using a CEN instance, the value of this parameter must be the ID of the CEN instance.
        # - If a VPC firewall protects the traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter must be the instance ID of the VPC firewall.
        # 
        # >  You can call the [DescribeVpcFirewallAclGroupList](https://www.alibabacloud.com/help/en/cloud-firewall/latest/describevpcfirewallaclgrouplist) operation to query the IDs.
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcFirewallControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.repeat_end_time is not None:
            result['RepeatEndTime'] = self.repeat_end_time
        if self.repeat_start_time is not None:
            result['RepeatStartTime'] = self.repeat_start_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RepeatEndTime') is not None:
            self.repeat_end_time = m.get('RepeatEndTime')
        if m.get('RepeatStartTime') is not None:
            self.repeat_start_time = m.get('RepeatStartTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class CreateVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(self, acl_uuid=None, request_id=None):
        # The ID of the access control policy.
        self.acl_uuid = acl_uuid  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcFirewallControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVpcFirewallControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpcFirewallControlPolicyResponse, self).to_map()
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
            temp_model = CreateVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAddressBookRequest(TeaModel):
    def __init__(self, group_uuid=None, lang=None, source_ip=None):
        # The ID of the address book.
        # 
        # To delete the address book, you must provide the ID of the address book. You can call the DescribeAddressBook operation to query the ID.
        self.group_uuid = group_uuid  # type: str
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAddressBookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteAddressBookResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAddressBookResponseBody, self).to_map()
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


class DeleteAddressBookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAddressBookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAddressBookResponse, self).to_map()
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
            temp_model = DeleteAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteControlPolicyRequest(TeaModel):
    def __init__(self, acl_uuid=None, direction=None, lang=None, source_ip=None):
        # The ID of the access control policy.
        # 
        # To delete an access control policy, you must provide the ID of the policy. You can call the [DescribeControlPolicy](~~138866~~) operation to query the ID.
        self.acl_uuid = acl_uuid  # type: str
        # The direction of the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        self.direction = direction  # type: str
        # The natural language of the request and response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the traffic.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteControlPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteControlPolicyResponseBody, self).to_map()
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


class DeleteControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteControlPolicyResponse, self).to_map()
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
            temp_model = DeleteControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFirewallV2RoutePoliciesRequest(TeaModel):
    def __init__(self, firewall_id=None, lang=None, tr_firewall_route_policy_id=None):
        self.firewall_id = firewall_id  # type: str
        self.lang = lang  # type: str
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFirewallV2RoutePoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class DeleteFirewallV2RoutePoliciesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFirewallV2RoutePoliciesResponseBody, self).to_map()
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


class DeleteFirewallV2RoutePoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFirewallV2RoutePoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFirewallV2RoutePoliciesResponse, self).to_map()
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
            temp_model = DeleteFirewallV2RoutePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceMembersRequest(TeaModel):
    def __init__(self, member_uids=None):
        # The unique identifiers (UID) of members that you want to remove from Cloud Firewall.
        self.member_uids = member_uids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_uids is not None:
            result['MemberUids'] = self.member_uids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberUids') is not None:
            self.member_uids = m.get('MemberUids')
        return self


class DeleteInstanceMembersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceMembersResponseBody, self).to_map()
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


class DeleteInstanceMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceMembersResponse, self).to_map()
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
            temp_model = DeleteInstanceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNatFirewallControlPolicyRequest(TeaModel):
    def __init__(self, acl_uuid=None, direction=None, lang=None, nat_gateway_id=None):
        # The UUID of the access control policy.
        # 
        # To delete an access control policy, you must provide the ID of the policy. You can call the DescribeNatFirewallControlPolicy operation to query the UUIDs of access control policies.
        self.acl_uuid = acl_uuid  # type: str
        # The direction of the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # *   **out**: outbound traffic
        self.direction = direction  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNatFirewallControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        return self


class DeleteNatFirewallControlPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNatFirewallControlPolicyResponseBody, self).to_map()
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


class DeleteNatFirewallControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNatFirewallControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNatFirewallControlPolicyResponse, self).to_map()
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
            temp_model = DeleteNatFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrFirewallV2Request(TeaModel):
    def __init__(self, firewall_id=None, lang=None):
        self.firewall_id = firewall_id  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrFirewallV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DeleteTrFirewallV2ResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTrFirewallV2ResponseBody, self).to_map()
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


class DeleteTrFirewallV2Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTrFirewallV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTrFirewallV2Response, self).to_map()
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
            temp_model = DeleteTrFirewallV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcFirewallCenConfigureRequest(TeaModel):
    def __init__(self, lang=None, member_uid=None, vpc_firewall_id_list=None):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The instance IDs of VPC firewalls.
        self.vpc_firewall_id_list = vpc_firewall_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcFirewallCenConfigureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id_list is not None:
            result['VpcFirewallIdList'] = self.vpc_firewall_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallIdList') is not None:
            self.vpc_firewall_id_list = m.get('VpcFirewallIdList')
        return self


class DeleteVpcFirewallCenConfigureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcFirewallCenConfigureResponseBody, self).to_map()
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


class DeleteVpcFirewallCenConfigureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVpcFirewallCenConfigureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVpcFirewallCenConfigureResponse, self).to_map()
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
            temp_model = DeleteVpcFirewallCenConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcFirewallConfigureRequest(TeaModel):
    def __init__(self, lang=None, member_uid=None, vpc_firewall_id_list=None):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The instance IDs of VPC firewalls.
        self.vpc_firewall_id_list = vpc_firewall_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcFirewallConfigureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id_list is not None:
            result['VpcFirewallIdList'] = self.vpc_firewall_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallIdList') is not None:
            self.vpc_firewall_id_list = m.get('VpcFirewallIdList')
        return self


class DeleteVpcFirewallConfigureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcFirewallConfigureResponseBody, self).to_map()
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


class DeleteVpcFirewallConfigureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVpcFirewallConfigureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVpcFirewallConfigureResponse, self).to_map()
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
            temp_model = DeleteVpcFirewallConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(self, acl_uuid=None, lang=None, vpc_firewall_id=None):
        # The ID of the access control policy. 
        # 
        # To delete an access control policy, you must provide the ID of the policy. You can call the **DescribeVpcFirewallControlPolicy** operation to query the ID.
        self.acl_uuid = acl_uuid  # type: str
        # The natural language of the request and response. Valid values: 
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang  # type: str
        # The ID of the group to which the access control policy belongs. You can call the **DescribeVpcFirewallAclGroupList** operation to query the ID.  
        # 
        # Valid values:
        # 
        # - If the VPC firewall is used to protect a CEN instance, the value of this parameter is the ID of the CEN instance.  
        # 
        # Example: cen-ervw0g12b5jbw****\
        # - If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the ID of the VPC firewall.  
        # 
        # Example: vfw-a42bbb7b887148c9****\
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcFirewallControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DeleteVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcFirewallControlPolicyResponseBody, self).to_map()
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


class DeleteVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVpcFirewallControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVpcFirewallControlPolicyResponse, self).to_map()
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
            temp_model = DeleteVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeACLProtectTrendRequest(TeaModel):
    def __init__(self, end_time=None, lang=None, source_ip=None, start_time=None):
        self.end_time = end_time  # type: str
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeACLProtectTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeACLProtectTrendResponseBodyTrendList(TeaModel):
    def __init__(self, protect_cnt=None, time=None):
        self.protect_cnt = protect_cnt  # type: int
        self.time = time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeACLProtectTrendResponseBodyTrendList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protect_cnt is not None:
            result['ProtectCnt'] = self.protect_cnt
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProtectCnt') is not None:
            self.protect_cnt = m.get('ProtectCnt')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeACLProtectTrendResponseBody(TeaModel):
    def __init__(self, in_protect_cnt=None, inter_vpcprotect_cnt=None, interval=None, out_protect_cnt=None,
                 request_id=None, total_protect_cnt=None, trend_list=None):
        self.in_protect_cnt = in_protect_cnt  # type: long
        self.inter_vpcprotect_cnt = inter_vpcprotect_cnt  # type: long
        self.interval = interval  # type: int
        self.out_protect_cnt = out_protect_cnt  # type: long
        self.request_id = request_id  # type: str
        self.total_protect_cnt = total_protect_cnt  # type: long
        self.trend_list = trend_list  # type: list[DescribeACLProtectTrendResponseBodyTrendList]

    def validate(self):
        if self.trend_list:
            for k in self.trend_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeACLProtectTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_protect_cnt is not None:
            result['InProtectCnt'] = self.in_protect_cnt
        if self.inter_vpcprotect_cnt is not None:
            result['InterVPCProtectCnt'] = self.inter_vpcprotect_cnt
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.out_protect_cnt is not None:
            result['OutProtectCnt'] = self.out_protect_cnt
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_protect_cnt is not None:
            result['TotalProtectCnt'] = self.total_protect_cnt
        result['TrendList'] = []
        if self.trend_list is not None:
            for k in self.trend_list:
                result['TrendList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InProtectCnt') is not None:
            self.in_protect_cnt = m.get('InProtectCnt')
        if m.get('InterVPCProtectCnt') is not None:
            self.inter_vpcprotect_cnt = m.get('InterVPCProtectCnt')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OutProtectCnt') is not None:
            self.out_protect_cnt = m.get('OutProtectCnt')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalProtectCnt') is not None:
            self.total_protect_cnt = m.get('TotalProtectCnt')
        self.trend_list = []
        if m.get('TrendList') is not None:
            for k in m.get('TrendList'):
                temp_model = DescribeACLProtectTrendResponseBodyTrendList()
                self.trend_list.append(temp_model.from_map(k))
        return self


class DescribeACLProtectTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeACLProtectTrendResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeACLProtectTrendResponse, self).to_map()
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
            temp_model = DescribeACLProtectTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAddressBookRequest(TeaModel):
    def __init__(self, contain_port=None, current_page=None, group_type=None, lang=None, page_size=None, query=None):
        # The port that is included in the address book. This parameter takes effect only when the **GroupType** parameter is set to **port**.
        self.contain_port = contain_port  # type: str
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.current_page = current_page  # type: str
        # The type of the address book. Valid values:
        # 
        # * **ip**: IP address book
        # * **domain**: domain address book
        # * **port**: port address book
        # * **tag**: Elastic Compute Service (ECS) tag-based address book
        # * **allCloud**: cloud service address book
        # * **threat**: threat intelligence address book
        # 
        # > If you do not specify a type, the domain address books and ECS tag-based address books are queried.
        self.group_type = group_type  # type: str
        # The language of the content within the request. Valid values:
        # 
        # * **zh**: Chinese (default)
        # * **en**: English
        self.lang = lang  # type: str
        # The number of entries to return on each page.
        # 
        # Default value: 10. Maximum value: 50.
        self.page_size = page_size  # type: str
        # The query condition that is used to search for the address book.
        self.query = query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAddressBookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_port is not None:
            result['ContainPort'] = self.contain_port
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainPort') is not None:
            self.contain_port = m.get('ContainPort')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class DescribeAddressBookResponseBodyAclsTagList(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The key of the ECS tag.
        self.tag_key = tag_key  # type: str
        # The value of the ECS tag.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAddressBookResponseBodyAclsTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeAddressBookResponseBodyAcls(TeaModel):
    def __init__(self, address_list=None, address_list_count=None, auto_add_tag_ecs=None, description=None,
                 group_name=None, group_type=None, group_uuid=None, reference_count=None, tag_list=None, tag_relation=None):
        # The addresses in the address book.
        self.address_list = address_list  # type: list[str]
        # The number of addresses in the address book.
        self.address_list_count = address_list_count  # type: int
        # Indicates whether the public IP addresses of ECS instances are automatically added to the address book if the instances match the specified tags. The setting takes effect on both newly purchased ECS instances whose tag settings are complete and ECS instances whose tag settings are modified. Valid values:
        # 
        # * **1**: yes
        # * **0**: no
        self.auto_add_tag_ecs = auto_add_tag_ecs  # type: int
        # The description of the address book.
        self.description = description  # type: str
        # The name of the address book.
        self.group_name = group_name  # type: str
        # The type of the address book. Valid values:
        # 
        # * **ip**: IP address book
        # * **domain**: domain address book
        # * **port**: port address book
        # * **tag**: ECS tag-based address book
        # * **allCloud**: cloud service address book
        # * **threat**: threat intelligence address book
        self.group_type = group_type  # type: str
        # The unique ID of the address book.
        self.group_uuid = group_uuid  # type: str
        # The number of times that the address book is referenced.
        self.reference_count = reference_count  # type: int
        # The details about the ECS tags that can be automatically added to the address book.
        self.tag_list = tag_list  # type: list[DescribeAddressBookResponseBodyAclsTagList]
        # The logical relationship among ECS tags. Valid values:
        # 
        # * **and**: Only the public IP addresses of ECS instances that match all the specified tags can be added to the address book.
        # * **or**: The public IP addresses of ECS instances that match any of the specified tags can be added to the address book.
        self.tag_relation = tag_relation  # type: str

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAddressBookResponseBodyAcls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_list is not None:
            result['AddressList'] = self.address_list
        if self.address_list_count is not None:
            result['AddressListCount'] = self.address_list_count
        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.reference_count is not None:
            result['ReferenceCount'] = self.reference_count
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')
        if m.get('AddressListCount') is not None:
            self.address_list_count = m.get('AddressListCount')
        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('ReferenceCount') is not None:
            self.reference_count = m.get('ReferenceCount')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = DescribeAddressBookResponseBodyAclsTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')
        return self


class DescribeAddressBookResponseBody(TeaModel):
    def __init__(self, acls=None, page_no=None, page_size=None, request_id=None, total_count=None):
        # The information about the address book.
        self.acls = acls  # type: list[DescribeAddressBookResponseBodyAcls]
        # The page number of the current page.
        self.page_no = page_no  # type: str
        # The number of entries returned per page.
        self.page_size = page_size  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of the returned address books.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.acls:
            for k in self.acls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAddressBookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Acls'] = []
        if self.acls is not None:
            for k in self.acls:
                result['Acls'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acls = []
        if m.get('Acls') is not None:
            for k in m.get('Acls'):
                temp_model = DescribeAddressBookResponseBodyAcls()
                self.acls.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAddressBookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAddressBookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAddressBookResponse, self).to_map()
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
            temp_model = DescribeAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetListRequest(TeaModel):
    def __init__(self, current_page=None, ip_version=None, lang=None, member_uid=None, new_resource_tag=None,
                 page_size=None, region_no=None, resource_type=None, search_item=None, sg_status=None, status=None, type=None,
                 user_type=None):
        # The page number. Valid values: 1 to 50.
        self.current_page = current_page  # type: str
        # The IP version of the asset that is protected by Cloud Firewall. Valid values:
        # 
        # *   **4**: IPv4 (default)
        # *   **6**: IPv6
        self.ip_version = ip_version  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is added to Cloud Firewall.
        self.member_uid = member_uid  # type: long
        # The time when the asset was added. Valid values:
        # 
        # *   **discovered in 1 hour**: within one hour.
        # *   **discovered in 1 day**: within one day.
        # *   **discovered in 7 days**: within seven days.
        self.new_resource_tag = new_resource_tag  # type: str
        # The number of entries per page. Valid values: 1 to 50.
        self.page_size = page_size  # type: str
        # The region ID of your Cloud Firewall.
        # 
        # > For more information about the regions, see [Supported regions](~~195657~~).
        self.region_no = region_no  # type: str
        # The type of the asset. Valid values:
        # 
        # *   **BastionHostEgressIP**: the egress IP address of a bastion host
        # *   **BastionHostIngressIP**: the ingress IP address of a bastion host
        # *   **EcsEIP**: the elastic IP address (EIP) of an Elastic Compute Service (ECS) instance
        # *   **EcsPublicIP**: the public IP address of an ECS instance
        # *   **EIP**: the EIP
        # *   **EniEIP**: the EIP of an elastic network interface (ENI)
        # *   **NatEIP**: the EIP of a NAT gateway
        # *   **SlbEIP**: the EIP of a Server Load Balancer (SLB) instance
        # *   **SlbPublicIP**: the public IP address of an SLB instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **HAVIP**: the high-availability virtual IP address (HAVIP)
        self.resource_type = resource_type  # type: str
        # The instance ID or IP address of the asset.
        self.search_item = search_item  # type: str
        # The status of the security group policy. Valid values:
        # 
        # *   **pass**: delivered
        # *   **block**: undelivered
        # *   **unsupport**: unsupported
        # 
        # > If you do not specify this parameter, the assets on which security group policies in all states take effect are queried.
        self.sg_status = sg_status  # type: str
        # The status of the firewall. Valid values:
        # 
        # *   **open**: The firewall is enabled.
        # *   **opening**: The firewall is being enabled.
        # *   **closed**: The firewall is disabled.
        # *   **closing**: The firewall is being disabled.
        # 
        # > If you do not specify this parameter, the assets that are configured for firewalls in all states are queried.
        self.status = status  # type: str
        # This parameter is deprecated.
        self.type = type  # type: str
        # The edition of Cloud Firewall. Valid values:
        # 
        # *   **buy**: a paid edition (default)
        # *   **free**: Free Edition
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAssetListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.new_resource_tag is not None:
            result['NewResourceTag'] = self.new_resource_tag
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.search_item is not None:
            result['SearchItem'] = self.search_item
        if self.sg_status is not None:
            result['SgStatus'] = self.sg_status
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NewResourceTag') is not None:
            self.new_resource_tag = m.get('NewResourceTag')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SearchItem') is not None:
            self.search_item = m.get('SearchItem')
        if m.get('SgStatus') is not None:
            self.sg_status = m.get('SgStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeAssetListResponseBodyAssets(TeaModel):
    def __init__(self, ali_uid=None, bind_instance_id=None, bind_instance_name=None, create_time_stamp=None,
                 internet_address=None, intranet_address=None, ip_version=None, member_uid=None, name=None, new_resource_tag=None,
                 note=None, protect_status=None, region_id=None, region_status=None, resource_instance_id=None,
                 resource_type=None, risk_level=None, sg_status=None, sg_status_time=None, sync_status=None, type=None):
        # The UID of the Alibaba Cloud account.
        # 
        # >  The value of this parameter indicates the management account to which the member is added.
        self.ali_uid = ali_uid  # type: long
        # The ID of the cloud resource with which the asset is associated.
        self.bind_instance_id = bind_instance_id  # type: str
        # The instance name of the asset.
        self.bind_instance_name = bind_instance_name  # type: str
        # The timestamp when the asset is added to Cloud Firewall.
        self.create_time_stamp = create_time_stamp  # type: str
        # The public IP address of the server.
        self.internet_address = internet_address  # type: str
        # The internal IP address of the server.
        self.intranet_address = intranet_address  # type: str
        # The IP version of the asset that is protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # *   **4**: IPv4
        # *   **6**: IPv6
        self.ip_version = ip_version  # type: int
        # The UID of the member.
        self.member_uid = member_uid  # type: long
        # The instance name of the asset that is protected by Cloud Firewall.
        self.name = name  # type: str
        # The time when the asset was added. Valid values:
        # 
        # *   **discovered in 1 hour**: within one hour.
        # *   **discovered in 1 day**: within one day.
        # *   **discovered in 7 days**: within seven days.
        self.new_resource_tag = new_resource_tag  # type: str
        # The remarks of the asset. Valid values:
        # 
        # *   **REGION_NOT_SUPPORT**: The region is not supported.
        # *   **NETWORK_NOT_SUPPORT**: The network is not supported.
        self.note = note  # type: str
        # The status of the firewall. Valid values:
        # 
        # *   **open**: enabled.
        # *   **opening**: being enabled.
        # *   **closed**: disabled.
        # *   **closing**: being disabled.
        self.protect_status = protect_status  # type: str
        # The ID of the region in which the asset resides.
        self.region_id = region_id  # type: str
        # Indicates whether the firewall is supported in the region in which the asset resides. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status  # type: str
        # The instance ID of the asset.
        self.resource_instance_id = resource_instance_id  # type: str
        # The type of the asset. Valid values:
        # 
        # *   **BastionHostEgressIP**: the egress IP address of a bastion host
        # *   **BastionHostIngressIP**: the ingress IP address of a bastion host
        # *   **EcsEIP**: the elastic IP address (EIP) of an Elastic Compute Service (ECS) instance
        # *   **EcsPublicIP**: the public IP address of an ECS instance
        # *   **EIP**: the EIP
        # *   **EniEIP**: the EIP of an elastic network interface (ENI)
        # *   **NatEIP**: the EIP of a NAT gateway
        # *   **SlbEIP**: the EIP of a Server Load Balancer (SLB) instance
        # *   **SlbPublicIP**: the public IP address of an SLB instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **HAVIP**: the high-availability virtual IP address (HAVIP)
        self.resource_type = resource_type  # type: str
        # The risk level of the asset. Valid values:
        # 
        # *   **low**: low
        # *   **middle**: medium
        # *   **hight**: high
        # 
        # >  The value of this parameter is returned only when the UserType parameter is set to free.
        self.risk_level = risk_level  # type: str
        # The status of the security group policy. Valid values:
        # 
        # *   **pass**: applied
        # *   **block**: not applied
        # *   **unsupport**: unsupported
        self.sg_status = sg_status  # type: str
        # The time when the status of the security group was last checked. The value is a UNIX timestamp. Unit: seconds.
        self.sg_status_time = sg_status_time  # type: long
        # Indicates whether traffic redirection is supported for the asset. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.sync_status = sync_status  # type: str
        # This parameter is deprecated.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAssetListResponseBodyAssets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_name is not None:
            result['BindInstanceName'] = self.bind_instance_name
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.name is not None:
            result['Name'] = self.name
        if self.new_resource_tag is not None:
            result['NewResourceTag'] = self.new_resource_tag
        if self.note is not None:
            result['Note'] = self.note
        if self.protect_status is not None:
            result['ProtectStatus'] = self.protect_status
        if self.region_id is not None:
            result['RegionID'] = self.region_id
        if self.region_status is not None:
            result['RegionStatus'] = self.region_status
        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.sg_status is not None:
            result['SgStatus'] = self.sg_status
        if self.sg_status_time is not None:
            result['SgStatusTime'] = self.sg_status_time
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceName') is not None:
            self.bind_instance_name = m.get('BindInstanceName')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewResourceTag') is not None:
            self.new_resource_tag = m.get('NewResourceTag')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ProtectStatus') is not None:
            self.protect_status = m.get('ProtectStatus')
        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')
        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')
        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SgStatus') is not None:
            self.sg_status = m.get('SgStatus')
        if m.get('SgStatusTime') is not None:
            self.sg_status_time = m.get('SgStatusTime')
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAssetListResponseBody(TeaModel):
    def __init__(self, assets=None, request_id=None, total_count=None):
        # The details about the assets that are protected by Cloud Firewall.
        self.assets = assets  # type: list[DescribeAssetListResponseBodyAssets]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of the assets that are protected by Cloud Firewall.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.assets:
            for k in self.assets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAssetListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Assets'] = []
        if self.assets is not None:
            for k in self.assets:
                result['Assets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.assets = []
        if m.get('Assets') is not None:
            for k in m.get('Assets'):
                temp_model = DescribeAssetListResponseBodyAssets()
                self.assets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAssetListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAssetListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAssetListResponse, self).to_map()
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
            temp_model = DescribeAssetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeControlPolicyRequest(TeaModel):
    def __init__(self, acl_action=None, acl_uuid=None, current_page=None, description=None, destination=None,
                 direction=None, ip_version=None, lang=None, page_size=None, proto=None, release=None, repeat_type=None,
                 source=None):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        # 
        # >  If you do not specify this parameter, access control policies of all action types are queried.
        self.acl_action = acl_action  # type: str
        # The unique ID of the access control policy.
        self.acl_uuid = acl_uuid  # type: str
        # The number of the page to return.
        # 
        # Default value: 1.
        self.current_page = current_page  # type: str
        # The description of the access control policy. Fuzzy match is supported.
        # 
        # >  If you do not specify this parameter, access control policies that have descriptions are queried.
        self.description = description  # type: str
        # The destination address in the access control policy. Fuzzy match is supported. The value of this parameter depends on the value of the DestinationType parameter.
        # 
        # *   If DestinationType is set to `net`, the value of Destination must be a CIDR block. Example: 10.0.3.0/24.
        # *   If DestinationType is set to `domain`, the value of Destination must be a domain name. Example: aliyun.
        # *   If DestinationType is set to `group`, the value of Destination must be the name of an address book. Example: db_group.
        # *   If DestinationType is set to `location`, the value of Destination must be a location. Example: beijing.
        # 
        # >  If you do not specify this parameter, access control policies of all destination address types are queried.
        self.destination = destination  # type: str
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        self.direction = direction  # type: str
        # The IP version of the address in the access control policy. Valid values:
        # 
        # *   **4**: IPv4 (default)
        # *   **6**: IPv6
        self.ip_version = ip_version  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The number of entries to return on each page.
        self.page_size = page_size  # type: str
        # The type of the protocol in the access control policy. Valid values:
        # 
        # * **TCP**\
        # * **UDP**\
        # * **ICMP**\
        # * **ANY**: all types of protocols
        # 
        # >  If you do not specify this parameter, access control policies of all protocol types are queried.
        self.proto = proto  # type: str
        # Specifies whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**: The access control policy is enabled.
        # *   **false**: The access control policy is disabled.
        self.release = release  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy. Fuzzy match is supported. The value of this parameter depends on the value of the SourceType parameter.
        # 
        # *   If SourceType is set to `net`, the value of Source must be a CIDR block. Example: 192.0.XX.XX/24.
        # *   If SourceType is set to `group`, the value of Source must be the name of an address book. Example: db_group. If the db_group address book does not contain addresses, all source addresses are queried.
        # *   If SourceType is set to `location`, the value of Source must be a location. Example: beijing.
        # 
        # >  If you do not specify this parameter, access control policies of all source address types are queried.
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.description is not None:
            result['Description'] = self.description
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeControlPolicyResponseBodyPolicys(TeaModel):
    def __init__(self, acl_action=None, acl_uuid=None, application_id=None, application_name=None,
                 application_name_list=None, create_time=None, description=None, dest_port=None, dest_port_group=None,
                 dest_port_group_ports=None, dest_port_type=None, destination=None, destination_group_cidrs=None,
                 destination_group_type=None, destination_type=None, direction=None, dns_result=None, dns_result_time=None, end_time=None,
                 hit_last_time=None, hit_times=None, ip_version=None, modify_time=None, order=None, proto=None, release=None,
                 repeat_days=None, repeat_end_time=None, repeat_start_time=None, repeat_type=None, source=None,
                 source_group_cidrs=None, source_group_type=None, source_type=None, spread_cnt=None, start_time=None):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action  # type: str
        # The unique ID of the access control policy.
        self.acl_uuid = acl_uuid  # type: str
        # The application ID in the access control policy.
        self.application_id = application_id  # type: str
        # The type of the application that the access control policy supports. Valid values:
        # 
        # *   **FTP**\
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **Memcache**\
        # *   **MongoDB**\
        # *   **MQTT**\
        # *   **MySQL**\
        # *   **RDP**\
        # *   **Redis**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **SSH**\
        # *   **SSL**\
        # *   **VNC**\
        # *   **ANY**: all types of applications
        self.application_name = application_name  # type: str
        # The names of applications.
        self.application_name_list = application_name_list  # type: list[str]
        # The time at which the access control policy was created.
        self.create_time = create_time  # type: long
        # The description of the access control policy.
        self.description = description  # type: str
        # The destination port in the access control policy.
        self.dest_port = dest_port  # type: str
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group  # type: str
        # The ports in the destination port address book.
        self.dest_port_group_ports = dest_port_group_ports  # type: list[str]
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type  # type: str
        # The destination address in the access control policy. The value of this parameter depends on the value of the DestinationType parameter. Valid values:
        # 
        # *   If **DestinationType** is set to **net**, the value of Destination is a CIDR block. Example: 192.0.XX.XX/24.
        # *   If **DestinationType** is set to **domain**, the value of Destination is a domain name. Example: aliyuncs.com.
        # *   If **DestinationType** is set to **group**, the value of Destination is the name of an address book. Example: db_group.
        # *   If **DestinationType** is set to **location**, the value of Destination is a location. For more information about location codes, see [AddControlPolicy](~~138867~~). Example: \["BJ11", "ZB"].
        self.destination = destination  # type: str
        # The CIDR blocks in the destination address book.
        self.destination_group_cidrs = destination_group_cidrs  # type: list[str]
        # The type of the destination address book in the access control policy. Valid values:
        # 
        # *   **ip**: an address book that includes one or more IP addresses
        # *   **tag**: an ECS tag-based address book that includes the IP addresses of the ECS instances with one or more specific tags
        # *   **domain**: an address book that includes one or more domain names
        # *   **threat**: an address book that includes one or more malicious IP addresses or domain names
        # *   **backsrc**: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or WAF instances
        self.destination_group_type = destination_group_type  # type: str
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: destination CIDR block
        # *   **group**: destination address book
        # *   **domain**: destination domain name
        # *   **location**: destination location
        self.destination_type = destination_type  # type: str
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        self.direction = direction  # type: str
        # The DNS resolution result.
        self.dns_result = dns_result  # type: str
        # The timestamp of the DNS resolution result. The value is a UNIX timestamp. Unit: seconds.
        self.dns_result_time = dns_result_time  # type: long
        self.end_time = end_time  # type: long
        # The timestamp when the access control policy was last hit. The value is a UNIX timestamp. Unit: seconds.
        self.hit_last_time = hit_last_time  # type: long
        # The number of hits for the access control policy.
        self.hit_times = hit_times  # type: long
        # The IP version of the address in the access control policy. Valid values:
        # 
        # *   **4**: IPv4
        # *   **6**: IPv6
        self.ip_version = ip_version  # type: int
        # The time at which the access control policy was modified.
        self.modify_time = modify_time  # type: long
        # The priority of the access control policy.
        # 
        # The priority value starts from 1. A small priority value indicates a high priority.
        self.order = order  # type: int
        # The type of the protocol in the access control policy. Valid values:
        # 
        # *   **ANY**\
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        self.proto = proto  # type: str
        # Indicates whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**: The access control policy is enabled.
        # *   **false**: The access control policy is disabled.
        self.release = release  # type: str
        self.repeat_days = repeat_days  # type: list[long]
        self.repeat_end_time = repeat_end_time  # type: str
        self.repeat_start_time = repeat_start_time  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy. Valid values:
        # 
        # *   If **SourceType** is set to `net`, the value of Source is a CIDR block. Example: 192.0.XX.XX/24.
        # *   If **SourceType** is set to `group`, the value of Source is the name of an address book. Example: db_group.
        # *   If **SourceType** is set to `location`, the value of Source is a location. For more information about location codes, see [AddControlPolicy](~~138867~~). Example: \["BJ11", "ZB"].
        self.source = source  # type: str
        # The CIDR blocks in the source address book.
        self.source_group_cidrs = source_group_cidrs  # type: list[str]
        # The type of the source address book in the access control policy. Valid values:
        # 
        # *   **ip**: an address book that includes one or more IP addresses
        # *   **tag**: an Elastic Compute Service (ECS) tag-based address book that includes the IP addresses of the ECS instances with one or more specific tags
        # *   **domain**: an address book that includes one or more domain names
        # *   **threat**: an address book that includes one or more malicious IP addresses or domain names
        # *   **backsrc**: an address book that includes one or more back-to-origin addresses of Anti-DDoS Pro or Anti-DDoS Premium instances or Web Application Firewall (WAF) instances
        self.source_group_type = source_group_type  # type: str
        # The type of the source address in the access control policy. Valid values:
        # 
        # *   **net**: source CIDR block
        # *   **group**: source address book
        # *   **location**: source location
        self.source_type = source_type  # type: str
        # The total quota consumed by the returned access control policies, which is the sum of the quota consumed by each policy.
        # 
        # Quota that is consumed by an access control policy = Number of source CIDR blocks × Number of destination CIDR blocks, destination locations, or IP addresses that are resolved from destination domain names × Number of applications × Number of ports.
        self.spread_cnt = spread_cnt  # type: int
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeControlPolicyResponseBodyPolicys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.dest_port_group_ports is not None:
            result['DestPortGroupPorts'] = self.dest_port_group_ports
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_group_cidrs is not None:
            result['DestinationGroupCidrs'] = self.destination_group_cidrs
        if self.destination_group_type is not None:
            result['DestinationGroupType'] = self.destination_group_type
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.dns_result is not None:
            result['DnsResult'] = self.dns_result
        if self.dns_result_time is not None:
            result['DnsResultTime'] = self.dns_result_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hit_last_time is not None:
            result['HitLastTime'] = self.hit_last_time
        if self.hit_times is not None:
            result['HitTimes'] = self.hit_times
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.order is not None:
            result['Order'] = self.order
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.repeat_end_time is not None:
            result['RepeatEndTime'] = self.repeat_end_time
        if self.repeat_start_time is not None:
            result['RepeatStartTime'] = self.repeat_start_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_group_cidrs is not None:
            result['SourceGroupCidrs'] = self.source_group_cidrs
        if self.source_group_type is not None:
            result['SourceGroupType'] = self.source_group_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.spread_cnt is not None:
            result['SpreadCnt'] = self.spread_cnt
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('DestPortGroupPorts') is not None:
            self.dest_port_group_ports = m.get('DestPortGroupPorts')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationGroupCidrs') is not None:
            self.destination_group_cidrs = m.get('DestinationGroupCidrs')
        if m.get('DestinationGroupType') is not None:
            self.destination_group_type = m.get('DestinationGroupType')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('DnsResult') is not None:
            self.dns_result = m.get('DnsResult')
        if m.get('DnsResultTime') is not None:
            self.dns_result_time = m.get('DnsResultTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HitLastTime') is not None:
            self.hit_last_time = m.get('HitLastTime')
        if m.get('HitTimes') is not None:
            self.hit_times = m.get('HitTimes')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RepeatEndTime') is not None:
            self.repeat_end_time = m.get('RepeatEndTime')
        if m.get('RepeatStartTime') is not None:
            self.repeat_start_time = m.get('RepeatStartTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceGroupCidrs') is not None:
            self.source_group_cidrs = m.get('SourceGroupCidrs')
        if m.get('SourceGroupType') is not None:
            self.source_group_type = m.get('SourceGroupType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpreadCnt') is not None:
            self.spread_cnt = m.get('SpreadCnt')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeControlPolicyResponseBody(TeaModel):
    def __init__(self, page_no=None, page_size=None, policys=None, request_id=None, total_count=None):
        # The page number of the returned page.
        self.page_no = page_no  # type: str
        # The number of entries returned per page.
        self.page_size = page_size  # type: str
        # The details about the access control policy.
        self.policys = policys  # type: list[DescribeControlPolicyResponseBodyPolicys]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of the returned access control policies.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.policys:
            for k in self.policys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Policys'] = []
        if self.policys is not None:
            for k in self.policys:
                result['Policys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.policys = []
        if m.get('Policys') is not None:
            for k in m.get('Policys'):
                temp_model = DescribeControlPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeControlPolicyResponse, self).to_map()
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
            temp_model = DescribeControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefaultIPSConfigRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefaultIPSConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeDefaultIPSConfigResponseBody(TeaModel):
    def __init__(self, ai_rules=None, basic_rules=None, cti_rules=None, enable_all_patch=None, enable_default=None,
                 patch_rules=None, request_id=None, rule_class=None, run_mode=None):
        self.ai_rules = ai_rules  # type: int
        self.basic_rules = basic_rules  # type: int
        self.cti_rules = cti_rules  # type: int
        self.enable_all_patch = enable_all_patch  # type: int
        self.enable_default = enable_default  # type: int
        self.patch_rules = patch_rules  # type: int
        self.request_id = request_id  # type: str
        self.rule_class = rule_class  # type: int
        self.run_mode = run_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefaultIPSConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_rules is not None:
            result['AiRules'] = self.ai_rules
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.cti_rules is not None:
            result['CtiRules'] = self.cti_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.enable_default is not None:
            result['EnableDefault'] = self.enable_default
        if self.patch_rules is not None:
            result['PatchRules'] = self.patch_rules
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AiRules') is not None:
            self.ai_rules = m.get('AiRules')
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('CtiRules') is not None:
            self.cti_rules = m.get('CtiRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('EnableDefault') is not None:
            self.enable_default = m.get('EnableDefault')
        if m.get('PatchRules') is not None:
            self.patch_rules = m.get('PatchRules')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeDefaultIPSConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDefaultIPSConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDefaultIPSConfigResponse, self).to_map()
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
            temp_model = DescribeDefaultIPSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainResolveRequest(TeaModel):
    def __init__(self, domain=None, ip_version=None, lang=None, source_ip=None):
        # The domain name whose DNS record you want to query.
        self.domain = domain  # type: str
        # The IP version of the asset that is protected by Cloud Firewall. Valid values:
        # 
        # *   **4**: IPv4 (default)
        # *   **6**: IPv6
        self.ip_version = ip_version  # type: str
        # The language of the content within the response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainResolveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeDomainResolveResponseBodyResolveResult(TeaModel):
    def __init__(self, ip_addrs=None, update_time=None):
        # The IP address to which the domain name is resolved. Multiple IP addresses are separated by commas (,).
        self.ip_addrs = ip_addrs  # type: str
        # The time when the domain name was resolved. The value of this parameter is a timestamp. Unit: seconds.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainResolveResponseBodyResolveResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_addrs is not None:
            result['IpAddrs'] = self.ip_addrs
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpAddrs') is not None:
            self.ip_addrs = m.get('IpAddrs')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeDomainResolveResponseBody(TeaModel):
    def __init__(self, request_id=None, resolve_result=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The details about the DNS record of the domain name.
        self.resolve_result = resolve_result  # type: DescribeDomainResolveResponseBodyResolveResult

    def validate(self):
        if self.resolve_result:
            self.resolve_result.validate()

    def to_map(self):
        _map = super(DescribeDomainResolveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resolve_result is not None:
            result['ResolveResult'] = self.resolve_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResolveResult') is not None:
            temp_model = DescribeDomainResolveResponseBodyResolveResult()
            self.resolve_result = temp_model.from_map(m['ResolveResult'])
        return self


class DescribeDomainResolveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainResolveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainResolveResponse, self).to_map()
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
            temp_model = DescribeDomainResolveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceMembersRequest(TeaModel):
    def __init__(self, current_page=None, member_desc=None, member_display_name=None, member_uid=None,
                 page_size=None):
        # The page number. Default value: **1**.
        self.current_page = current_page  # type: str
        # The remarks of the member. The remarks must be 1 to 256 characters in length.
        self.member_desc = member_desc  # type: str
        # The name of the member.
        self.member_display_name = member_display_name  # type: str
        # The UID of the member.
        self.member_uid = member_uid  # type: str
        # The number of entries per page.
        # 
        # Default value: **20**.
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc
        if self.member_display_name is not None:
            result['MemberDisplayName'] = self.member_display_name
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')
        if m.get('MemberDisplayName') is not None:
            self.member_display_name = m.get('MemberDisplayName')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeInstanceMembersResponseBodyMembers(TeaModel):
    def __init__(self, create_time=None, member_desc=None, member_display_name=None, member_status=None,
                 member_uid=None, modify_time=None):
        # The time when the member was added to Cloud Firewall. The value is a timestamp. Unit: seconds.
        self.create_time = create_time  # type: int
        # The remarks of the member.
        self.member_desc = member_desc  # type: str
        # The name of the member.
        self.member_display_name = member_display_name  # type: str
        # The status of the member. Valid values:
        # 
        # *   **normal**\
        # *   **deleting**\
        self.member_status = member_status  # type: str
        # The UID of the member.
        self.member_uid = member_uid  # type: long
        # The time when the member was last modified. The value is a timestamp. Unit: seconds.
        self.modify_time = modify_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceMembersResponseBodyMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc
        if self.member_display_name is not None:
            result['MemberDisplayName'] = self.member_display_name
        if self.member_status is not None:
            result['MemberStatus'] = self.member_status
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')
        if m.get('MemberDisplayName') is not None:
            self.member_display_name = m.get('MemberDisplayName')
        if m.get('MemberStatus') is not None:
            self.member_status = m.get('MemberStatus')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class DescribeInstanceMembersResponseBodyPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The page number.
        self.current_page = current_page  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The total number of the members.
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceMembersResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstanceMembersResponseBody(TeaModel):
    def __init__(self, members=None, page_info=None, request_id=None):
        # The information about the member.
        self.members = members  # type: list[DescribeInstanceMembersResponseBodyMembers]
        # The pagination information.
        self.page_info = page_info  # type: DescribeInstanceMembersResponseBodyPageInfo
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(DescribeInstanceMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = DescribeInstanceMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeInstanceMembersResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceMembersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceMembersResponse, self).to_map()
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
            temp_model = DescribeInstanceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInternetOpenIpRequest(TeaModel):
    def __init__(self, assets_instance_id=None, assets_instance_name=None, assets_type=None, current_page=None,
                 end_time=None, lang=None, page_size=None, port=None, public_ip=None, region_no=None, risk_level=None,
                 service_name=None, start_time=None):
        self.assets_instance_id = assets_instance_id  # type: str
        self.assets_instance_name = assets_instance_name  # type: str
        self.assets_type = assets_type  # type: str
        self.current_page = current_page  # type: str
        self.end_time = end_time  # type: str
        self.lang = lang  # type: str
        self.page_size = page_size  # type: str
        self.port = port  # type: str
        self.public_ip = public_ip  # type: str
        self.region_no = region_no  # type: str
        self.risk_level = risk_level  # type: str
        self.service_name = service_name  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInternetOpenIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id
        if self.assets_instance_name is not None:
            result['AssetsInstanceName'] = self.assets_instance_name
        if self.assets_type is not None:
            result['AssetsType'] = self.assets_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.port is not None:
            result['Port'] = self.port
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')
        if m.get('AssetsInstanceName') is not None:
            self.assets_instance_name = m.get('AssetsInstanceName')
        if m.get('AssetsType') is not None:
            self.assets_type = m.get('AssetsType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeInternetOpenIpResponseBodyDataList(TeaModel):
    def __init__(self, acl_recommend_detail=None, assets_instance_id=None, assets_name=None, assets_type=None,
                 detail_num=None, has_acl_recommend=None, port_list=None, public_ip=None, region_no=None, risk_level=None,
                 risk_reason=None, service_name_list=None, traffic_percent_1day=None, traffic_percent_30day=None,
                 traffic_percent_7day=None):
        self.acl_recommend_detail = acl_recommend_detail  # type: str
        self.assets_instance_id = assets_instance_id  # type: str
        self.assets_name = assets_name  # type: str
        self.assets_type = assets_type  # type: str
        self.detail_num = detail_num  # type: int
        self.has_acl_recommend = has_acl_recommend  # type: bool
        self.port_list = port_list  # type: list[str]
        self.public_ip = public_ip  # type: str
        self.region_no = region_no  # type: str
        self.risk_level = risk_level  # type: int
        self.risk_reason = risk_reason  # type: str
        self.service_name_list = service_name_list  # type: list[str]
        self.traffic_percent_1day = traffic_percent_1day  # type: str
        self.traffic_percent_30day = traffic_percent_30day  # type: str
        self.traffic_percent_7day = traffic_percent_7day  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInternetOpenIpResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_recommend_detail is not None:
            result['AclRecommendDetail'] = self.acl_recommend_detail
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id
        if self.assets_name is not None:
            result['AssetsName'] = self.assets_name
        if self.assets_type is not None:
            result['AssetsType'] = self.assets_type
        if self.detail_num is not None:
            result['DetailNum'] = self.detail_num
        if self.has_acl_recommend is not None:
            result['HasAclRecommend'] = self.has_acl_recommend
        if self.port_list is not None:
            result['PortList'] = self.port_list
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.risk_reason is not None:
            result['RiskReason'] = self.risk_reason
        if self.service_name_list is not None:
            result['ServiceNameList'] = self.service_name_list
        if self.traffic_percent_1day is not None:
            result['TrafficPercent1Day'] = self.traffic_percent_1day
        if self.traffic_percent_30day is not None:
            result['TrafficPercent30Day'] = self.traffic_percent_30day
        if self.traffic_percent_7day is not None:
            result['TrafficPercent7Day'] = self.traffic_percent_7day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclRecommendDetail') is not None:
            self.acl_recommend_detail = m.get('AclRecommendDetail')
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')
        if m.get('AssetsName') is not None:
            self.assets_name = m.get('AssetsName')
        if m.get('AssetsType') is not None:
            self.assets_type = m.get('AssetsType')
        if m.get('DetailNum') is not None:
            self.detail_num = m.get('DetailNum')
        if m.get('HasAclRecommend') is not None:
            self.has_acl_recommend = m.get('HasAclRecommend')
        if m.get('PortList') is not None:
            self.port_list = m.get('PortList')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RiskReason') is not None:
            self.risk_reason = m.get('RiskReason')
        if m.get('ServiceNameList') is not None:
            self.service_name_list = m.get('ServiceNameList')
        if m.get('TrafficPercent1Day') is not None:
            self.traffic_percent_1day = m.get('TrafficPercent1Day')
        if m.get('TrafficPercent30Day') is not None:
            self.traffic_percent_30day = m.get('TrafficPercent30Day')
        if m.get('TrafficPercent7Day') is not None:
            self.traffic_percent_7day = m.get('TrafficPercent7Day')
        return self


class DescribeInternetOpenIpResponseBodyPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInternetOpenIpResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInternetOpenIpResponseBody(TeaModel):
    def __init__(self, data_list=None, page_info=None, request_id=None):
        self.data_list = data_list  # type: list[DescribeInternetOpenIpResponseBodyDataList]
        self.page_info = page_info  # type: DescribeInternetOpenIpResponseBodyPageInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(DescribeInternetOpenIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeInternetOpenIpResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeInternetOpenIpResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInternetOpenIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInternetOpenIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInternetOpenIpResponse, self).to_map()
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
            temp_model = DescribeInternetOpenIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInternetTrafficTrendRequest(TeaModel):
    def __init__(self, direction=None, end_time=None, lang=None, source_code=None, source_ip=None,
                 src_private_ip=None, src_public_ip=None, start_time=None, traffic_type=None):
        self.direction = direction  # type: str
        self.end_time = end_time  # type: str
        self.lang = lang  # type: str
        self.source_code = source_code  # type: str
        self.source_ip = source_ip  # type: str
        self.src_private_ip = src_private_ip  # type: str
        self.src_public_ip = src_public_ip  # type: str
        self.start_time = start_time  # type: str
        self.traffic_type = traffic_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInternetTrafficTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_private_ip is not None:
            result['SrcPrivateIP'] = self.src_private_ip
        if self.src_public_ip is not None:
            result['SrcPublicIP'] = self.src_public_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcPrivateIP') is not None:
            self.src_private_ip = m.get('SrcPrivateIP')
        if m.get('SrcPublicIP') is not None:
            self.src_public_ip = m.get('SrcPublicIP')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')
        return self


class DescribeInternetTrafficTrendResponseBodyDataList(TeaModel):
    def __init__(self, in_bps=None, in_bytes=None, in_pps=None, new_conn=None, out_bps=None, out_bytes=None,
                 out_pps=None, session_count=None, time=None, total_bps=None):
        self.in_bps = in_bps  # type: long
        self.in_bytes = in_bytes  # type: long
        self.in_pps = in_pps  # type: long
        self.new_conn = new_conn  # type: long
        self.out_bps = out_bps  # type: long
        self.out_bytes = out_bytes  # type: long
        self.out_pps = out_pps  # type: long
        self.session_count = session_count  # type: long
        self.time = time  # type: int
        self.total_bps = total_bps  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInternetTrafficTrendResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes
        if self.in_pps is not None:
            result['InPps'] = self.in_pps
        if self.new_conn is not None:
            result['NewConn'] = self.new_conn
        if self.out_bps is not None:
            result['OutBps'] = self.out_bps
        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes
        if self.out_pps is not None:
            result['OutPps'] = self.out_pps
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.time is not None:
            result['Time'] = self.time
        if self.total_bps is not None:
            result['TotalBps'] = self.total_bps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')
        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')
        if m.get('NewConn') is not None:
            self.new_conn = m.get('NewConn')
        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')
        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')
        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TotalBps') is not None:
            self.total_bps = m.get('TotalBps')
        return self


class DescribeInternetTrafficTrendResponseBody(TeaModel):
    def __init__(self, avg_in_bps=None, avg_out_bps=None, avg_session=None, avg_total_bps=None, data_list=None,
                 max_bandwidth_time=None, max_in_bps=None, max_out_bps=None, max_session=None, max_total_bps=None, request_id=None,
                 total_bytes=None, total_in_bytes=None, total_out_bytes=None, total_session=None):
        self.avg_in_bps = avg_in_bps  # type: long
        self.avg_out_bps = avg_out_bps  # type: long
        self.avg_session = avg_session  # type: long
        self.avg_total_bps = avg_total_bps  # type: long
        self.data_list = data_list  # type: list[DescribeInternetTrafficTrendResponseBodyDataList]
        self.max_bandwidth_time = max_bandwidth_time  # type: long
        self.max_in_bps = max_in_bps  # type: long
        self.max_out_bps = max_out_bps  # type: long
        self.max_session = max_session  # type: long
        self.max_total_bps = max_total_bps  # type: long
        self.request_id = request_id  # type: str
        self.total_bytes = total_bytes  # type: long
        self.total_in_bytes = total_in_bytes  # type: long
        self.total_out_bytes = total_out_bytes  # type: long
        self.total_session = total_session  # type: long

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInternetTrafficTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_in_bps is not None:
            result['AvgInBps'] = self.avg_in_bps
        if self.avg_out_bps is not None:
            result['AvgOutBps'] = self.avg_out_bps
        if self.avg_session is not None:
            result['AvgSession'] = self.avg_session
        if self.avg_total_bps is not None:
            result['AvgTotalBps'] = self.avg_total_bps
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.max_bandwidth_time is not None:
            result['MaxBandwidthTime'] = self.max_bandwidth_time
        if self.max_in_bps is not None:
            result['MaxInBps'] = self.max_in_bps
        if self.max_out_bps is not None:
            result['MaxOutBps'] = self.max_out_bps
        if self.max_session is not None:
            result['MaxSession'] = self.max_session
        if self.max_total_bps is not None:
            result['MaxTotalBps'] = self.max_total_bps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.total_in_bytes is not None:
            result['TotalInBytes'] = self.total_in_bytes
        if self.total_out_bytes is not None:
            result['TotalOutBytes'] = self.total_out_bytes
        if self.total_session is not None:
            result['TotalSession'] = self.total_session
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgInBps') is not None:
            self.avg_in_bps = m.get('AvgInBps')
        if m.get('AvgOutBps') is not None:
            self.avg_out_bps = m.get('AvgOutBps')
        if m.get('AvgSession') is not None:
            self.avg_session = m.get('AvgSession')
        if m.get('AvgTotalBps') is not None:
            self.avg_total_bps = m.get('AvgTotalBps')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeInternetTrafficTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('MaxBandwidthTime') is not None:
            self.max_bandwidth_time = m.get('MaxBandwidthTime')
        if m.get('MaxInBps') is not None:
            self.max_in_bps = m.get('MaxInBps')
        if m.get('MaxOutBps') is not None:
            self.max_out_bps = m.get('MaxOutBps')
        if m.get('MaxSession') is not None:
            self.max_session = m.get('MaxSession')
        if m.get('MaxTotalBps') is not None:
            self.max_total_bps = m.get('MaxTotalBps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TotalInBytes') is not None:
            self.total_in_bytes = m.get('TotalInBytes')
        if m.get('TotalOutBytes') is not None:
            self.total_out_bytes = m.get('TotalOutBytes')
        if m.get('TotalSession') is not None:
            self.total_session = m.get('TotalSession')
        return self


class DescribeInternetTrafficTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInternetTrafficTrendResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInternetTrafficTrendResponse, self).to_map()
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
            temp_model = DescribeInternetTrafficTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvadeEventListRequest(TeaModel):
    def __init__(self, assets_ip=None, assets_instance_id=None, assets_instance_name=None, current_page=None,
                 end_time=None, event_key=None, event_name=None, event_uuid=None, is_ignore=None, lang=None, member_uid=None,
                 page_size=None, process_status_list=None, risk_level=None, source_ip=None, start_time=None):
        # The IP address of the affected asset.
        self.assets_ip = assets_ip  # type: str
        # The ID of the instance.
        self.assets_instance_id = assets_instance_id  # type: str
        # The name of the instance.
        self.assets_instance_name = assets_instance_name  # type: str
        # The number of the page to return.
        # 
        # Default value: 1.
        self.current_page = current_page  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds. If you do not specify this parameter, the query ends at the current time.
        self.end_time = end_time  # type: str
        # The ID of the breach awareness event.
        self.event_key = event_key  # type: str
        # The name of the breach awareness event.
        self.event_name = event_name  # type: str
        # The UUID of the breach awareness event.
        self.event_uuid = event_uuid  # type: str
        # Specifies whether the breach awareness event is ignored. Valid values:
        # 
        # *   **true**: The breach awareness event is ignored.
        # *   **false**: The breach awareness event is not ignored.
        self.is_ignore = is_ignore  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The ID of the member.
        self.member_uid = member_uid  # type: long
        # The number of entries to return on each page.
        # 
        # Default value: 6. Maximum value: 10.
        self.page_size = page_size  # type: str
        # The handling status of breach awareness events.
        self.process_status_list = process_status_list  # type: list[int]
        # The risk levels.
        self.risk_level = risk_level  # type: list[int]
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds. If you do not specify this parameter, the query starts from 30 days before the current time.
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInvadeEventListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assets_ip is not None:
            result['AssetsIP'] = self.assets_ip
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id
        if self.assets_instance_name is not None:
            result['AssetsInstanceName'] = self.assets_instance_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_key is not None:
            result['EventKey'] = self.event_key
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid
        if self.is_ignore is not None:
            result['IsIgnore'] = self.is_ignore
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.process_status_list is not None:
            result['ProcessStatusList'] = self.process_status_list
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetsIP') is not None:
            self.assets_ip = m.get('AssetsIP')
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')
        if m.get('AssetsInstanceName') is not None:
            self.assets_instance_name = m.get('AssetsInstanceName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventKey') is not None:
            self.event_key = m.get('EventKey')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')
        if m.get('IsIgnore') is not None:
            self.is_ignore = m.get('IsIgnore')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProcessStatusList') is not None:
            self.process_status_list = m.get('ProcessStatusList')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeInvadeEventListResponseBodyEventList(TeaModel):
    def __init__(self, assets_instance_id=None, assets_instance_name=None, assets_type=None, event_key=None,
                 event_name=None, event_src=None, event_uuid=None, first_time=None, is_ignore=None, last_time=None,
                 member_uid=None, private_ip=None, process_status=None, public_ip=None, public_ip_type=None, risk_level=None):
        # The ID of the affected asset.
        self.assets_instance_id = assets_instance_id  # type: str
        # The name of the affected asset.
        self.assets_instance_name = assets_instance_name  # type: str
        # The type of the affected asset. Valid values:
        # 
        # *   **BastionHostIP**: the egress IP address of a bastion host
        # *   **BastionHostIngressIP**: the ingress IP address of a bastion host
        # *   **EcsEIP**: the elastic IP address (EIP) of an Elastic Compute Service (ECS) instance
        # *   **EcsPublicIP**: the public IP address of an ECS instance
        # *   **EIP**: the EIP
        # *   **EniEIP**: the EIP of an elastic network interface (ENI)
        # *   **NatEIP**: the EIP of a NAT gateway
        # *   **SlbEIP**: the EIP of a Server Load Balancer (SLB) instance
        # *   **SlbPublicIP**: the public IP address of an SLB instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **HAVIP**: the high-availability virtual IP address (HAVIP)
        self.assets_type = assets_type  # type: str
        # The ID of the breach awareness event.
        self.event_key = event_key  # type: str
        # The name of the breach awareness event.
        self.event_name = event_name  # type: str
        # The type of the breach awareness event. Valid values:
        # 
        # *   **IPS**: intrusion prevention event
        # *   **offline**: disconnection event
        self.event_src = event_src  # type: str
        # The UUID of the breach awareness event.
        self.event_uuid = event_uuid  # type: str
        # The time when the breach awareness event first occurred. The value is a UNIX timestamp. Unit: seconds.
        self.first_time = first_time  # type: int
        # Indicates whether the breach awareness event is ignored. Valid values:
        # 
        # *   **true**: The breach awareness event is ignored.
        # *   **false**: The breach awareness event is not ignored.
        self.is_ignore = is_ignore  # type: bool
        # The time when the breach awareness event last occurred. The value is a UNIX timestamp. Unit: seconds.
        self.last_time = last_time  # type: int
        # The ID of the member.
        self.member_uid = member_uid  # type: str
        # The private IP address of the affected asset.
        self.private_ip = private_ip  # type: str
        # The handling status of the breach awareness event. Valid values:
        # 
        # *   **0**: unhandled
        # *   **20**: handled
        self.process_status = process_status  # type: int
        # The public IP address of the affected asset.
        self.public_ip = public_ip  # type: str
        # The type of the affected asset. Valid values:
        # 
        # *   **BastionHostIP**: the egress IP address of a bastion host
        # *   **BastionHostIngressIP**: the ingress IP address of a bastion host
        # *   **EcsEIP**: the EIP of an ECS instance
        # *   **EcsPublicIP**: the public IP address of an ECS instance
        # *   **EIP**: the EIP
        # *   **EniEIP**: the EIP of an ENI
        # *   **NatEIP**: the EIP of a NAT gateway
        # *   **SlbEIP**: the EIP of an SLB instance
        # *   **SlbPublicIP**: the public IP address of an SLB instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **HAVIP**: the HAVIP
        self.public_ip_type = public_ip_type  # type: str
        # The risk level. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.risk_level = risk_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInvadeEventListResponseBodyEventList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assets_instance_id is not None:
            result['AssetsInstanceId'] = self.assets_instance_id
        if self.assets_instance_name is not None:
            result['AssetsInstanceName'] = self.assets_instance_name
        if self.assets_type is not None:
            result['AssetsType'] = self.assets_type
        if self.event_key is not None:
            result['EventKey'] = self.event_key
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_src is not None:
            result['EventSrc'] = self.event_src
        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid
        if self.first_time is not None:
            result['FirstTime'] = self.first_time
        if self.is_ignore is not None:
            result['IsIgnore'] = self.is_ignore
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.public_ip_type is not None:
            result['PublicIpType'] = self.public_ip_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetsInstanceId') is not None:
            self.assets_instance_id = m.get('AssetsInstanceId')
        if m.get('AssetsInstanceName') is not None:
            self.assets_instance_name = m.get('AssetsInstanceName')
        if m.get('AssetsType') is not None:
            self.assets_type = m.get('AssetsType')
        if m.get('EventKey') is not None:
            self.event_key = m.get('EventKey')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventSrc') is not None:
            self.event_src = m.get('EventSrc')
        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')
        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')
        if m.get('IsIgnore') is not None:
            self.is_ignore = m.get('IsIgnore')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('PublicIpType') is not None:
            self.public_ip_type = m.get('PublicIpType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class DescribeInvadeEventListResponseBodyPageInfo(TeaModel):
    def __init__(self, current_page=None, page_size=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The total number of breach awareness events.
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInvadeEventListResponseBodyPageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInvadeEventListResponseBody(TeaModel):
    def __init__(self, event_list=None, high_level_percent=None, low_level_percent=None, middle_level_percent=None,
                 page_info=None, request_id=None):
        # An array that consists of breach awareness events.
        self.event_list = event_list  # type: list[DescribeInvadeEventListResponseBodyEventList]
        # The percentage of high-risk events.
        self.high_level_percent = high_level_percent  # type: int
        # The percentage of low-risk events.
        self.low_level_percent = low_level_percent  # type: int
        # The percentage of medium-risk events.
        self.middle_level_percent = middle_level_percent  # type: int
        # The pagination information.
        self.page_info = page_info  # type: DescribeInvadeEventListResponseBodyPageInfo
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super(DescribeInvadeEventListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.high_level_percent is not None:
            result['HighLevelPercent'] = self.high_level_percent
        if self.low_level_percent is not None:
            result['LowLevelPercent'] = self.low_level_percent
        if self.middle_level_percent is not None:
            result['MiddleLevelPercent'] = self.middle_level_percent
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeInvadeEventListResponseBodyEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('HighLevelPercent') is not None:
            self.high_level_percent = m.get('HighLevelPercent')
        if m.get('LowLevelPercent') is not None:
            self.low_level_percent = m.get('LowLevelPercent')
        if m.get('MiddleLevelPercent') is not None:
            self.middle_level_percent = m.get('MiddleLevelPercent')
        if m.get('PageInfo') is not None:
            temp_model = DescribeInvadeEventListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInvadeEventListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInvadeEventListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInvadeEventListResponse, self).to_map()
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
            temp_model = DescribeInvadeEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNatFirewallControlPolicyRequest(TeaModel):
    def __init__(self, acl_action=None, acl_uuid=None, current_page=None, description=None, destination=None,
                 direction=None, lang=None, nat_gateway_id=None, page_size=None, proto=None, release=None, repeat_type=None,
                 source=None):
        # The action that Cloud Firewall performs on the traffic.
        # 
        # Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action  # type: str
        # The UUID of the access control policy.
        self.acl_uuid = acl_uuid  # type: str
        # The page number.
        self.current_page = current_page  # type: str
        # The description of the access control policy. Fuzzy match is supported.
        # 
        # > If you do not specify this parameter, the descriptions of all policies are queried.
        self.description = description  # type: str
        # The destination address in the access control policy. Fuzzy match is supported. The value of this parameter varies based on the value of the DestinationType parameter.
        # 
        # *   If DestinationType is set to `net`, the value of Destination must be a CIDR block. Example: 10.0.3.0/24.
        # *   If DestinationType is set to `domain`, the value of Destination must be a domain name. Example: aliyun.
        # *   If DestinationType is set to `group`, the value of Destination must be the name of an address book. Example: db_group.
        # *   If DestinationType is set to `location`, the value of Destination is a location. For more information about location codes, see [AddControlPolicy](~~474128~~). Example: \["BJ11", "ZB"].
        # 
        # > If you do not specify this parameter, all types of destination addresses are queried.
        self.destination = destination  # type: str
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **out**: outbound traffic
        self.direction = direction  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id  # type: str
        # The number of entries per page. Default value: 10.
        self.page_size = page_size  # type: str
        # The type of the protocol in the access control policy. Valid values:
        # 
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # *   **ANY**: all types of protocols
        # 
        # > If you do not specify this parameter, access control policies of all protocol types are queried.
        self.proto = proto  # type: str
        # Specifies whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.release = release  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy. Fuzzy match is supported. The value of this parameter varies based on the value of the SourceType parameter.
        # 
        # *   If SourceType is set to `net`, the value of Source must be a CIDR block. Example: 192.0.XX.XX/24.
        # *   If SourceType is set to `group`, the value of Source must be the name of an address book. Example: db_group. If the db_group address book does not contain addresses, all source addresses are queried.
        # *   If SourceType is set to `location`, the value of Source must be a location. Example: beijing.
        # 
        # > If you do not specify this parameter, all types of source addresses are queried.
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNatFirewallControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.description is not None:
            result['Description'] = self.description
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeNatFirewallControlPolicyResponseBodyPolicys(TeaModel):
    def __init__(self, acl_action=None, acl_uuid=None, application_name_list=None, create_time=None,
                 description=None, dest_port=None, dest_port_group=None, dest_port_group_ports=None, dest_port_type=None,
                 destination=None, destination_group_cidrs=None, destination_group_type=None, destination_type=None,
                 dns_result=None, dns_result_time=None, domain_resolve_type=None, end_time=None, hit_last_time=None,
                 hit_times=None, modify_time=None, nat_gateway_id=None, order=None, proto=None, release=None, repeat_days=None,
                 repeat_end_time=None, repeat_start_time=None, repeat_type=None, source=None, source_group_cidrs=None,
                 source_group_type=None, source_type=None, spread_cnt=None, start_time=None):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action  # type: str
        # The UUID of the access control policy.
        self.acl_uuid = acl_uuid  # type: str
        # The application names.
        self.application_name_list = application_name_list  # type: list[str]
        # The time at which the access control policy was created.
        self.create_time = create_time  # type: long
        # The description of the access control policy.
        self.description = description  # type: str
        # The destination port in the access control policy.
        self.dest_port = dest_port  # type: str
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group  # type: str
        # The ports in the destination port address book.
        self.dest_port_group_ports = dest_port_group_ports  # type: list[str]
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type  # type: str
        # The destination address in the access control policy. The value of this parameter varies based on the value of the DestinationType parameter. Valid values:
        # 
        # *   If **DestinationType** is set to **net**, the value of Destination is a CIDR block. Example: 192.0.XX.XX/24.
        # *   If **DestinationType** is set to **domain**, the value of Destination is a domain name. Example: aliyuncs.com.
        # *   If **DestinationType** is set to **group**, the value of Destination is the name of an address book. Example: db_group.
        # *   If **DestinationType** is set to **location**, the value of Destination is a location. For more information about location codes, see [AddControlPolicy](~~138867~~). Example: \["BJ11", "ZB"].
        self.destination = destination  # type: str
        # The CIDR blocks in the destination address book.
        self.destination_group_cidrs = destination_group_cidrs  # type: list[str]
        # The type of the destination address book in the access control policy. Valid values:
        # 
        # *   **ip**: an address book that includes one or more CIDR blocks
        # *   **domain**: an address book that includes one or more domain names
        self.destination_group_type = destination_group_type  # type: str
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        # *   **location**\
        self.destination_type = destination_type  # type: str
        # The DNS resolution result.
        self.dns_result = dns_result  # type: str
        # The time of the DNS resolution result. The value is a timestamp. Unit: seconds.
        self.dns_result_time = dns_result_time  # type: long
        # The domain name resolution method of the access control policy. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **1**: Fully qualified domain name (FQDN)-based
        # *   **2**: Domain Name System (DNS)-based
        # *   **3**: FQDN and DNS-based
        self.domain_resolve_type = domain_resolve_type  # type: int
        self.end_time = end_time  # type: long
        # The times when the access control policy was last hit. The value is a timestamp. Unit: seconds.
        self.hit_last_time = hit_last_time  # type: long
        # The number of hits for the access control policy.
        self.hit_times = hit_times  # type: int
        # The time at which the access control policy was modified.
        self.modify_time = modify_time  # type: long
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id  # type: str
        # The priority of the access control policy.
        # 
        # The priority value starts from 1. A smaller priority value indicates a higher priority.
        self.order = order  # type: int
        # The type of the protocol in the access control policy. Valid values:
        # 
        # *   **ANY**\
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        self.proto = proto  # type: str
        # Indicates whether the access control policy is enabled. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.release = release  # type: str
        self.repeat_days = repeat_days  # type: list[long]
        self.repeat_end_time = repeat_end_time  # type: str
        self.repeat_start_time = repeat_start_time  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy. Valid values:
        # 
        # *   If **SourceType** is set to `net`, the value of Source is a CIDR block. Example: 192.0.XX.XX/24.
        # *   If **SourceType** is set to `group`, the value of Source is the name of an address book. Example: db_group.
        # *   If **SourceType** is set to `location`, the value of Source is a location. For more information about location codes, see [AddControlPolicy](~~138867~~). Example: \["BJ11", "ZB"].
        self.source = source  # type: str
        # The CIDR blocks in the source address book.
        self.source_group_cidrs = source_group_cidrs  # type: list[str]
        # The type of the source address book in the access control policy. The value is fixed as **ip**. The value indicates an address book that includes one or more CIDR blocks.
        self.source_group_type = source_group_type  # type: str
        # The type of the source address book in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **location**: location
        self.source_type = source_type  # type: str
        # The total quota consumed by the returned access control policies, which is the sum of the quota consumed by each policy. The quota that is consumed by an access control policy is calculated based on the following formula: Quota that is consumed by an access control policy = Number of source CIDR blocks × Number of destination CIDR blocks, regions, or resolved domain names × *Number of applications* × Number of ports.
        self.spread_cnt = spread_cnt  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNatFirewallControlPolicyResponseBodyPolicys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.dest_port_group_ports is not None:
            result['DestPortGroupPorts'] = self.dest_port_group_ports
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_group_cidrs is not None:
            result['DestinationGroupCidrs'] = self.destination_group_cidrs
        if self.destination_group_type is not None:
            result['DestinationGroupType'] = self.destination_group_type
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.dns_result is not None:
            result['DnsResult'] = self.dns_result
        if self.dns_result_time is not None:
            result['DnsResultTime'] = self.dns_result_time
        if self.domain_resolve_type is not None:
            result['DomainResolveType'] = self.domain_resolve_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hit_last_time is not None:
            result['HitLastTime'] = self.hit_last_time
        if self.hit_times is not None:
            result['HitTimes'] = self.hit_times
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.order is not None:
            result['Order'] = self.order
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.repeat_end_time is not None:
            result['RepeatEndTime'] = self.repeat_end_time
        if self.repeat_start_time is not None:
            result['RepeatStartTime'] = self.repeat_start_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_group_cidrs is not None:
            result['SourceGroupCidrs'] = self.source_group_cidrs
        if self.source_group_type is not None:
            result['SourceGroupType'] = self.source_group_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.spread_cnt is not None:
            result['SpreadCnt'] = self.spread_cnt
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('DestPortGroupPorts') is not None:
            self.dest_port_group_ports = m.get('DestPortGroupPorts')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationGroupCidrs') is not None:
            self.destination_group_cidrs = m.get('DestinationGroupCidrs')
        if m.get('DestinationGroupType') is not None:
            self.destination_group_type = m.get('DestinationGroupType')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DnsResult') is not None:
            self.dns_result = m.get('DnsResult')
        if m.get('DnsResultTime') is not None:
            self.dns_result_time = m.get('DnsResultTime')
        if m.get('DomainResolveType') is not None:
            self.domain_resolve_type = m.get('DomainResolveType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HitLastTime') is not None:
            self.hit_last_time = m.get('HitLastTime')
        if m.get('HitTimes') is not None:
            self.hit_times = m.get('HitTimes')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RepeatEndTime') is not None:
            self.repeat_end_time = m.get('RepeatEndTime')
        if m.get('RepeatStartTime') is not None:
            self.repeat_start_time = m.get('RepeatStartTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceGroupCidrs') is not None:
            self.source_group_cidrs = m.get('SourceGroupCidrs')
        if m.get('SourceGroupType') is not None:
            self.source_group_type = m.get('SourceGroupType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpreadCnt') is not None:
            self.spread_cnt = m.get('SpreadCnt')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeNatFirewallControlPolicyResponseBody(TeaModel):
    def __init__(self, policys=None, request_id=None, total_count=None):
        # The information about the access control policies.
        self.policys = policys  # type: list[DescribeNatFirewallControlPolicyResponseBodyPolicys]
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.policys:
            for k in self.policys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNatFirewallControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policys'] = []
        if self.policys is not None:
            for k in self.policys:
                result['Policys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policys = []
        if m.get('Policys') is not None:
            for k in m.get('Policys'):
                temp_model = DescribeNatFirewallControlPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNatFirewallControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNatFirewallControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNatFirewallControlPolicyResponse, self).to_map()
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
            temp_model = DescribeNatFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNatFirewallPolicyPriorUsedRequest(TeaModel):
    def __init__(self, direction=None, ip_version=None, lang=None, nat_gateway_id=None):
        # The direction of the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # *   **out**: outbound traffic
        self.direction = direction  # type: str
        # The IP version supported by the access control policy. Valid values:
        # 
        # *   **4**: IPv4 (default)
        self.ip_version = ip_version  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNatFirewallPolicyPriorUsedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        return self


class DescribeNatFirewallPolicyPriorUsedResponseBody(TeaModel):
    def __init__(self, end=None, request_id=None, start=None):
        # The lowest priority for the access control policy.
        self.end = end  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The highest priority for the access control policy.
        self.start = start  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNatFirewallPolicyPriorUsedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class DescribeNatFirewallPolicyPriorUsedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNatFirewallPolicyPriorUsedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNatFirewallPolicyPriorUsedResponse, self).to_map()
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
            temp_model = DescribeNatFirewallPolicyPriorUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOutgoingDestinationIPRequest(TeaModel):
    def __init__(self, application_name=None, category_id=None, current_page=None, dst_ip=None, end_time=None,
                 lang=None, order=None, page_size=None, port=None, private_ip=None, public_ip=None, sort=None,
                 start_time=None, tag_id_new=None):
        # The application type in the access control policy. Valid values:
        # 
        # *   **FTP**\
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **Memcache**\
        # *   **MongoDB**\
        # *   **MQTT**\
        # *   **MySQL**\
        # *   **RDP**\
        # *   **Redis**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **SSH**\
        # *   **SSL_No_Cert**\
        # *   **SSL**\
        # *   **VNC**\
        # 
        # >  The value of this parameter depends on the value of Proto. If you set Proto to TCP, you can set ApplicationNameList to any valid value. If you specify both ApplicationNameList and ApplicationName, only the value of ApplicationNameList is used.
        self.application_name = application_name  # type: str
        # The ID of the service to which the destination IP address belongs. This parameter is left empty by default. Valid values:
        # 
        # *   **All**: all services
        # *   **RiskDomain**: risky domain names
        # *   **RiskIP**: risky IP addresses
        # *   **AliYun**: Alibaba Cloud services
        # *   **NotAliYun**: third-party services
        self.category_id = category_id  # type: str
        # The number of the page to return.
        # 
        # Default value: 1.
        self.current_page = current_page  # type: str
        # The destination IP address in the outbound connection that is initiated to access a domain name.
        self.dst_ip = dst_ip  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The order in which you want to sort the queried information. Valid values:
        # 
        # *   **asc**: the ascending order.
        # *   **desc**: the descending order. This is the default value.
        self.order = order  # type: str
        # The number of entries to return on each page.
        # 
        # Default value: 6. Maximum value: 10.
        self.page_size = page_size  # type: str
        # The port number.
        self.port = port  # type: str
        # The private IP address of the ECS instance that initiates the outbound connection.
        self.private_ip = private_ip  # type: str
        # The public IP address of the Elastic Compute Service (ECS) instance that initiates the outbound connection.
        self.public_ip = public_ip  # type: str
        # The field based on which you want to sort the queried information. Valid values:
        # 
        # *   **SessionCount**: the number of requests. This is the default value.
        # *   **TotalBytes**: the total volume of traffic.
        self.sort = sort  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: str
        # The ID of the tag. Valid values:
        # 
        # *   **AliYun**: Alibaba Cloud service
        # *   **RiskDomain**: risky domain name
        # *   **RiskIP**: risky IP address
        # *   **TrustedDomain**: trusted website
        # *   **AliPay**: Alipay
        # *   **DingDing**: DingTalk
        # *   **WeChat**: WeChat
        # *   **QQ**: Tencent QQ
        # *   **SecurityService**: security service
        # *   **Microsoft**: Microsoft
        # *   **Amazon**: Amazon Web Services (AWS)
        # *   **Pan**: cloud disk
        # *   **Map**: map
        # *   **Code**: code hosting
        # *   **SystemService**: system service
        # *   **Taobao**: Taobao
        # *   **Google**: Google
        # *   **ThirdPartyService**: third-party service
        # *   **FirstFlow**: the first time
        # *   **Downloader**: malicious download
        # *   **Alexa Top1M**: popular website
        # *   **Miner**: mining pool
        # *   **Intelligence**: threat intelligence
        # *   **DDoS**: DDoS trojan
        # *   **Ransomware**: ransomware
        # *   **Spyware**: spyware
        # *   **Rogue**: rogue software
        # *   **Botnet**: botnet
        # *   **Suspicious**: suspicious website
        # *   **C\&C**: command and control (C\&C)
        # *   **Gang**: gang
        # *   **CVE**: Common Vulnerabilities and Exposures (CVE)
        # *   **Backdoor**: webshell
        # *   **Phishing**: phishing website
        # *   **APT**: advanced persistent threat (APT) attack
        # *   **Supply Chain Attack**: supply chain attack
        # *   **Malicious software**: malware
        self.tag_id_new = tag_id_new  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOutgoingDestinationIPRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.port is not None:
            result['Port'] = self.port
        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_id_new is not None:
            result['TagIdNew'] = self.tag_id_new
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagIdNew') is not None:
            self.tag_id_new = m.get('TagIdNew')
        return self


class DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList(TeaModel):
    def __init__(self, address_group_name=None, address_group_uuid=None):
        # The name of the address book.
        self.address_group_name = address_group_name  # type: str
        # The UUID of the address book.
        self.address_group_uuid = address_group_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_group_name is not None:
            result['AddressGroupName'] = self.address_group_name
        if self.address_group_uuid is not None:
            result['AddressGroupUUID'] = self.address_group_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressGroupName') is not None:
            self.address_group_name = m.get('AddressGroupName')
        if m.get('AddressGroupUUID') is not None:
            self.address_group_uuid = m.get('AddressGroupUUID')
        return self


class DescribeOutgoingDestinationIPResponseBodyDstIPListApplicationPortList(TeaModel):
    def __init__(self, application_name=None, port=None):
        # The application type in the access control policy. Valid values:
        # 
        # *   **FTP**\
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **Memcache**\
        # *   **MongoDB**\
        # *   **MQTT**\
        # *   **MySQL**\
        # *   **RDP**\
        # *   **Redis**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **SSH**\
        # *   **SSL_No_Cert**\
        # *   **SSL**\
        # *   **VNC**\
        # 
        # >  The value of this parameter depends on the value of Proto. If you set Proto to TCP, you can set ApplicationNameList to any valid value. If you specify both ApplicationNameList and ApplicationName, only the value of ApplicationNameList is used.
        self.application_name = application_name  # type: str
        # The port of the application.
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOutgoingDestinationIPResponseBodyDstIPListApplicationPortList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeOutgoingDestinationIPResponseBodyDstIPListTagList(TeaModel):
    def __init__(self, class_id=None, risk_level=None, tag_describe=None, tag_id=None, tag_name=None):
        # The type of the tag. Valid values:
        # 
        # *   **Suspicious**\
        # *   **Malicious**\
        # *   **Trusted**\
        self.class_id = class_id  # type: str
        # The risk level. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.risk_level = risk_level  # type: int
        # The description of the tag.
        self.tag_describe = tag_describe  # type: str
        # The ID of the tag.
        self.tag_id = tag_id  # type: str
        # The name of the tag.
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOutgoingDestinationIPResponseBodyDstIPListTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_describe is not None:
            result['TagDescribe'] = self.tag_describe
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagDescribe') is not None:
            self.tag_describe = m.get('TagDescribe')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DescribeOutgoingDestinationIPResponseBodyDstIPList(TeaModel):
    def __init__(self, acl_coverage=None, acl_recommend_detail=None, acl_status=None, address_group_list=None,
                 application_port_list=None, category_class_id=None, category_id=None, category_name=None, dst_ip=None, group_name=None,
                 has_acl=None, has_acl_recommend=None, in_bytes=None, is_mark_normal=None, out_bytes=None, rule_id=None,
                 rule_name=None, security_reason=None, security_suggest=None, session_count=None, tag_list=None,
                 total_bytes=None):
        # Indicates whether an access control policy is configured. Valid values:
        # 
        # *   **Uncovered**: No access control policies are configured.
        # *   **FullCoverage**: An access control policy is configured.
        self.acl_coverage = acl_coverage  # type: str
        # The suggestion in an access control policy.
        self.acl_recommend_detail = acl_recommend_detail  # type: str
        # The state of the access control policy. Valid values:
        # 
        # *   **Normal**: healthy
        # *   **Abnormal**: unhealthy
        self.acl_status = acl_status  # type: str
        # The information about the address book.
        self.address_group_list = address_group_list  # type: list[DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList]
        # An array that consists of application ports.
        self.application_port_list = application_port_list  # type: list[DescribeOutgoingDestinationIPResponseBodyDstIPListApplicationPortList]
        # The type of the tag. Valid values:
        # 
        # *   **Suspicious**\
        # *   **Malicious**\
        # *   **Trusted**\
        self.category_class_id = category_class_id  # type: str
        # The ID of the service to which the destination IP address belongs. Valid values:
        # 
        # *   **Aliyun**: Alibaba Cloud services
        # *   **NotAliyun**: third-party services
        self.category_id = category_id  # type: str
        # The type of the service to which the destination IP address belongs. Valid values:
        # 
        # *   **Alibaba Cloud services**\
        # *   **third-party services**\
        self.category_name = category_name  # type: str
        # The destination IP address in the outbound connection that is initiated to access a domain name.
        self.dst_ip = dst_ip  # type: str
        # The name of the group to which the access control policy belongs.
        self.group_name = group_name  # type: str
        # Indicates whether an access control policy is configured. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_acl = has_acl  # type: str
        # Indicates whether an access control policy is recommended. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_acl_recommend = has_acl_recommend  # type: bool
        # The inbound traffic. Unit: bytes.
        self.in_bytes = in_bytes  # type: long
        # Indicates whether the destination IP address is added to a whitelist. Valid values:
        # 
        # *   **true**: added
        # *   **false**: not added
        self.is_mark_normal = is_mark_normal  # type: bool
        # The outbound traffic. Unit: bytes.
        self.out_bytes = out_bytes  # type: long
        # The UUID of the access control policy.
        self.rule_id = rule_id  # type: str
        # The name of the access control policy.
        self.rule_name = rule_name  # type: str
        # The reason why the domain name is secure.
        self.security_reason = security_reason  # type: str
        # The suggestion to handle the traffic of the domain name in outbound connections. Valid values:
        # 
        # *   **pass**: allow
        # *   **alert**: deny
        # *   **drop**: monitor
        self.security_suggest = security_suggest  # type: str
        # The number of requests.
        self.session_count = session_count  # type: long
        # The tags.
        self.tag_list = tag_list  # type: list[DescribeOutgoingDestinationIPResponseBodyDstIPListTagList]
        # The total volume of traffic. Unit: bytes.
        self.total_bytes = total_bytes  # type: str

    def validate(self):
        if self.address_group_list:
            for k in self.address_group_list:
                if k:
                    k.validate()
        if self.application_port_list:
            for k in self.application_port_list:
                if k:
                    k.validate()
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOutgoingDestinationIPResponseBodyDstIPList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_coverage is not None:
            result['AclCoverage'] = self.acl_coverage
        if self.acl_recommend_detail is not None:
            result['AclRecommendDetail'] = self.acl_recommend_detail
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        result['AddressGroupList'] = []
        if self.address_group_list is not None:
            for k in self.address_group_list:
                result['AddressGroupList'].append(k.to_map() if k else None)
        result['ApplicationPortList'] = []
        if self.application_port_list is not None:
            for k in self.application_port_list:
                result['ApplicationPortList'].append(k.to_map() if k else None)
        if self.category_class_id is not None:
            result['CategoryClassId'] = self.category_class_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.has_acl is not None:
            result['HasAcl'] = self.has_acl
        if self.has_acl_recommend is not None:
            result['HasAclRecommend'] = self.has_acl_recommend
        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes
        if self.is_mark_normal is not None:
            result['IsMarkNormal'] = self.is_mark_normal
        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.security_reason is not None:
            result['SecurityReason'] = self.security_reason
        if self.security_suggest is not None:
            result['SecuritySuggest'] = self.security_suggest
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclCoverage') is not None:
            self.acl_coverage = m.get('AclCoverage')
        if m.get('AclRecommendDetail') is not None:
            self.acl_recommend_detail = m.get('AclRecommendDetail')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        self.address_group_list = []
        if m.get('AddressGroupList') is not None:
            for k in m.get('AddressGroupList'):
                temp_model = DescribeOutgoingDestinationIPResponseBodyDstIPListAddressGroupList()
                self.address_group_list.append(temp_model.from_map(k))
        self.application_port_list = []
        if m.get('ApplicationPortList') is not None:
            for k in m.get('ApplicationPortList'):
                temp_model = DescribeOutgoingDestinationIPResponseBodyDstIPListApplicationPortList()
                self.application_port_list.append(temp_model.from_map(k))
        if m.get('CategoryClassId') is not None:
            self.category_class_id = m.get('CategoryClassId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HasAcl') is not None:
            self.has_acl = m.get('HasAcl')
        if m.get('HasAclRecommend') is not None:
            self.has_acl_recommend = m.get('HasAclRecommend')
        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')
        if m.get('IsMarkNormal') is not None:
            self.is_mark_normal = m.get('IsMarkNormal')
        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SecurityReason') is not None:
            self.security_reason = m.get('SecurityReason')
        if m.get('SecuritySuggest') is not None:
            self.security_suggest = m.get('SecuritySuggest')
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = DescribeOutgoingDestinationIPResponseBodyDstIPListTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        return self


class DescribeOutgoingDestinationIPResponseBody(TeaModel):
    def __init__(self, dst_iplist=None, request_id=None, total_count=None):
        # The destination IP addresses in outbound connections.
        self.dst_iplist = dst_iplist  # type: list[DescribeOutgoingDestinationIPResponseBodyDstIPList]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of destination IP addresses in outbound connections.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.dst_iplist:
            for k in self.dst_iplist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOutgoingDestinationIPResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DstIPList'] = []
        if self.dst_iplist is not None:
            for k in self.dst_iplist:
                result['DstIPList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dst_iplist = []
        if m.get('DstIPList') is not None:
            for k in m.get('DstIPList'):
                temp_model = DescribeOutgoingDestinationIPResponseBodyDstIPList()
                self.dst_iplist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOutgoingDestinationIPResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOutgoingDestinationIPResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOutgoingDestinationIPResponse, self).to_map()
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
            temp_model = DescribeOutgoingDestinationIPResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOutgoingDomainRequest(TeaModel):
    def __init__(self, category_id=None, current_page=None, domain=None, end_time=None, lang=None, order=None,
                 page_size=None, public_ip=None, sort=None, start_time=None, tag_id_new=None):
        # The type of the service. This parameter is empty by default. Valid values:
        # 
        # *   **All**: all services
        # *   **RiskDomain**: risky domain names
        # *   **RiskIP**: risky IP addresses
        # *   **AliYun**: Alibaba Cloud services
        # *   **NotAliYun**: third-party services
        self.category_id = category_id  # type: str
        # The number of the page to return.
        # 
        # Default value: 1.
        self.current_page = current_page  # type: str
        # The domain name in outbound connections.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: str
        # The language of the content within the request. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The order in which you want to sort the query results. Valid values:
        # 
        # *   **asc**: the ascending order.
        # *   **desc**: the descending order. This is the default value.
        self.order = order  # type: str
        # The number of entries to return on each page.
        # 
        # Default value: 6. Maximum value: 100.
        self.page_size = page_size  # type: str
        # The public IP address of the Elastic Compute Service (ECS) instance that initiates outbound connections.
        self.public_ip = public_ip  # type: str
        # The field based on which you want to sort the query results. Valid values:
        # 
        # *   **SessionCount**: the number of requests. This is the default value.
        # *   **TotalBytes**: the total volume of traffic.
        self.sort = sort  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: str
        # The ID of the tag. Valid values:
        # 
        # *   **AliYun**: Alibaba Cloud service
        # *   **RiskDomain**: risky domain name
        # *   **RiskIP**: risky IP address
        # *   **TrustedDomain**: trusted website
        # *   **AliPay**: Alipay
        # *   **DingDing**: DingTalk
        # *   **WeChat**: WeChat
        # *   **QQ**: Tencent QQ
        # *   **SecurityService**: security service
        # *   **Microsoft**: Microsoft
        # *   **Amazon**: Amazon Web Services (AWS)
        # *   **Pan**: cloud disk
        # *   **Map**: map
        # *   **Code**: code hosting
        # *   **SystemService**: system service
        # *   **Taobao**: Taobao
        # *   **Google**: Google
        # *   **ThirdPartyService**: third-party service
        # *   **FirstFlow**: the first time when an outbound connection is initiated
        # *   **Downloader**: malicious download
        # *   **Alexa Top1M**: popular website
        # *   **Miner**: mining pool
        # *   **Intelligence**: threat intelligence
        # *   **DDoS**: DDoS trojan
        # *   **Ransomware**: ransomware
        # *   **Spyware**: spyware
        # *   **Rogue**: rogue software
        # *   **Botnet**: botnet
        # *   **Suspicious**: suspicious website
        # *   **C\&C**: command and control (C\&C)
        # *   **Gang**: gang
        # *   **CVE**: Common Vulnerabilities and Exposures (CVE)
        # *   **Backdoor**: webshell
        # *   **Phishing**: phishing website
        # *   **APT**: advanced persistent threat (APT) attack
        # *   **Supply Chain Attack**: supply chain attack
        # *   **Malicious software**: malware
        self.tag_id_new = tag_id_new  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOutgoingDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_id_new is not None:
            result['TagIdNew'] = self.tag_id_new
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagIdNew') is not None:
            self.tag_id_new = m.get('TagIdNew')
        return self


class DescribeOutgoingDomainResponseBodyDomainListTagList(TeaModel):
    def __init__(self, class_id=None, risk_level=None, tag_describe=None, tag_id=None, tag_name=None):
        # The type of the tag. Valid values:
        # 
        # *   **Suspicious**\
        # *   **Malicious**\
        # *   **Trusted**\
        self.class_id = class_id  # type: str
        # The risk level. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.risk_level = risk_level  # type: int
        # The description of the tag.
        self.tag_describe = tag_describe  # type: str
        # The ID of the tag.
        self.tag_id = tag_id  # type: str
        # The name of the tag.
        self.tag_name = tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOutgoingDomainResponseBodyDomainListTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.tag_describe is not None:
            result['TagDescribe'] = self.tag_describe
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('TagDescribe') is not None:
            self.tag_describe = m.get('TagDescribe')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DescribeOutgoingDomainResponseBodyDomainList(TeaModel):
    def __init__(self, acl_coverage=None, acl_recommend_detail=None, acl_status=None, address_group_name=None,
                 address_group_uuid=None, business=None, category_class_id=None, category_id=None, category_name=None, domain=None,
                 group_name=None, has_acl=None, has_acl_recommend=None, in_bytes=None, is_mark_normal=None, organization=None,
                 out_bytes=None, rule_id=None, rule_name=None, security_reason=None, security_suggest=None,
                 session_count=None, tag_list=None, total_bytes=None):
        # Indicates whether an access control policy is configured. Valid values:
        # 
        # *   **Uncovered**: no
        # *   **FullCoverage**: yes
        self.acl_coverage = acl_coverage  # type: str
        # The suggestion in an access control policy.
        self.acl_recommend_detail = acl_recommend_detail  # type: str
        # The state of the access control policy. Valid values:
        # 
        # *   **normal**: healthy
        # *   **abnormal**: unhealthy
        self.acl_status = acl_status  # type: str
        # The name of the address book.
        self.address_group_name = address_group_name  # type: str
        # The UUID of the address book.
        self.address_group_uuid = address_group_uuid  # type: str
        # The website service.
        self.business = business  # type: str
        # The type of the tag. Valid values:
        # 
        # *   **Suspicious**\
        # *   **Malicious**\
        # *   **Trusted**\
        self.category_class_id = category_class_id  # type: str
        # The type ID of the service to which the domain name belongs. Valid values:
        # 
        # *   **Aliyun**: Alibaba Cloud services
        # *   **NotAliyun**: third-party services
        self.category_id = category_id  # type: str
        # The type of the service to which the domain name belongs. Valid values:
        # 
        # *   **Alibaba Cloud services**\
        # *   **Third-party services**\
        self.category_name = category_name  # type: str
        # The domain name in outbound connections.
        self.domain = domain  # type: str
        # The name of the group to which the access control policy belongs.
        self.group_name = group_name  # type: str
        # Indicates whether an `access control policy` is configured for the domain name. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_acl = has_acl  # type: str
        # Indicates whether an access control policy is recommended. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_acl_recommend = has_acl_recommend  # type: bool
        # The volume of inbound traffic.
        self.in_bytes = in_bytes  # type: long
        # Indicates whether the domain name is marked as normal. Valid values:
        # 
        # *   **true**: normal
        # *   **false**: abnormal
        self.is_mark_normal = is_mark_normal  # type: bool
        # The name of the organization.
        self.organization = organization  # type: str
        # The volume of outbound traffic.
        self.out_bytes = out_bytes  # type: long
        # The ID of the access control policy.
        self.rule_id = rule_id  # type: str
        # The name of the access control policy.
        self.rule_name = rule_name  # type: str
        # The reason why the domain name is secure.
        self.security_reason = security_reason  # type: str
        # The suggestion to handle the traffic of the domain name in outbound connections. Valid values:
        # 
        # *   **pass**: allow
        # *   **alert**: monitor
        # *   **drop**: deny
        self.security_suggest = security_suggest  # type: str
        # The number of requests.
        self.session_count = session_count  # type: long
        # An array that consists of tags.
        self.tag_list = tag_list  # type: list[DescribeOutgoingDomainResponseBodyDomainListTagList]
        # The total volume of traffic. Unit: bytes.
        self.total_bytes = total_bytes  # type: str

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOutgoingDomainResponseBodyDomainList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_coverage is not None:
            result['AclCoverage'] = self.acl_coverage
        if self.acl_recommend_detail is not None:
            result['AclRecommendDetail'] = self.acl_recommend_detail
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.address_group_name is not None:
            result['AddressGroupName'] = self.address_group_name
        if self.address_group_uuid is not None:
            result['AddressGroupUUID'] = self.address_group_uuid
        if self.business is not None:
            result['Business'] = self.business
        if self.category_class_id is not None:
            result['CategoryClassId'] = self.category_class_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.has_acl is not None:
            result['HasAcl'] = self.has_acl
        if self.has_acl_recommend is not None:
            result['HasAclRecommend'] = self.has_acl_recommend
        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes
        if self.is_mark_normal is not None:
            result['IsMarkNormal'] = self.is_mark_normal
        if self.organization is not None:
            result['Organization'] = self.organization
        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.security_reason is not None:
            result['SecurityReason'] = self.security_reason
        if self.security_suggest is not None:
            result['SecuritySuggest'] = self.security_suggest
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclCoverage') is not None:
            self.acl_coverage = m.get('AclCoverage')
        if m.get('AclRecommendDetail') is not None:
            self.acl_recommend_detail = m.get('AclRecommendDetail')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('AddressGroupName') is not None:
            self.address_group_name = m.get('AddressGroupName')
        if m.get('AddressGroupUUID') is not None:
            self.address_group_uuid = m.get('AddressGroupUUID')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CategoryClassId') is not None:
            self.category_class_id = m.get('CategoryClassId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HasAcl') is not None:
            self.has_acl = m.get('HasAcl')
        if m.get('HasAclRecommend') is not None:
            self.has_acl_recommend = m.get('HasAclRecommend')
        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')
        if m.get('IsMarkNormal') is not None:
            self.is_mark_normal = m.get('IsMarkNormal')
        if m.get('Organization') is not None:
            self.organization = m.get('Organization')
        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SecurityReason') is not None:
            self.security_reason = m.get('SecurityReason')
        if m.get('SecuritySuggest') is not None:
            self.security_suggest = m.get('SecuritySuggest')
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = DescribeOutgoingDomainResponseBodyDomainListTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        return self


class DescribeOutgoingDomainResponseBody(TeaModel):
    def __init__(self, domain_list=None, request_id=None, total_count=None):
        # An array that consists of the domain names in outbound connections.
        self.domain_list = domain_list  # type: list[DescribeOutgoingDomainResponseBodyDomainList]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of the domain names in outbound connections.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.domain_list:
            for k in self.domain_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOutgoingDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainList'] = []
        if self.domain_list is not None:
            for k in self.domain_list:
                result['DomainList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_list = []
        if m.get('DomainList') is not None:
            for k in m.get('DomainList'):
                temp_model = DescribeOutgoingDomainResponseBodyDomainList()
                self.domain_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOutgoingDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOutgoingDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOutgoingDomainResponse, self).to_map()
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
            temp_model = DescribeOutgoingDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyAdvancedConfigRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None):
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyAdvancedConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribePolicyAdvancedConfigResponseBody(TeaModel):
    def __init__(self, internet_switch=None, request_id=None):
        # Indicates whether the strict mode is enabled for the access control policy. Valid values:
        # 
        # *   **on**: The strict mode is enabled.
        # *   **off**: The strict mode is disabled.
        self.internet_switch = internet_switch  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyAdvancedConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_switch is not None:
            result['InternetSwitch'] = self.internet_switch
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InternetSwitch') is not None:
            self.internet_switch = m.get('InternetSwitch')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePolicyAdvancedConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePolicyAdvancedConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyAdvancedConfigResponse, self).to_map()
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
            temp_model = DescribePolicyAdvancedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyPriorUsedRequest(TeaModel):
    def __init__(self, direction=None, ip_version=None, lang=None, source_ip=None):
        # The direction of the traffic to which the access control policy applies.
        # 
        # Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        self.direction = direction  # type: str
        # The IP version of the asset that is protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # *   **4**: IPv4 (default)
        # *   **6**: IPv6
        self.ip_version = ip_version  # type: str
        # The natural language of the request and response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyPriorUsedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribePolicyPriorUsedResponseBody(TeaModel):
    def __init__(self, end=None, request_id=None, start=None):
        # The lowest priority of existing access control policies.
        # 
        # >  The value -1 indicates the lowest priority.
        self.end = end  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The highest priority of existing access control policies.
        # 
        # >  The value 0 indicates the highest priority.
        self.start = start  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyPriorUsedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class DescribePolicyPriorUsedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePolicyPriorUsedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyPriorUsedResponse, self).to_map()
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
            temp_model = DescribePolicyPriorUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskEventGroupRequest(TeaModel):
    def __init__(self, attack_app=None, attack_type=None, buy_version=None, current_page=None, data_type=None,
                 direction=None, dst_ip=None, dst_network_instance_id=None, end_time=None, event_name=None,
                 firewall_type=None, lang=None, no_location=None, order=None, page_size=None, rule_result=None, rule_source=None,
                 sort=None, src_ip=None, src_network_instance_id=None, start_time=None, vul_level=None):
        # The names of attacked applications. Set the value in the `["AttackApp1","AttackApp2"]` format.
        self.attack_app = attack_app  # type: list[str]
        # The attack type of the intrusion events. Valid values:
        # 
        # *   **1**: suspicious connection
        # *   **2**: command execution
        # *   **3**: brute-force attack
        # *   **4**: scanning
        # *   **5**: others
        # *   **6**: information leak
        # *   **7**: DoS attack
        # *   **8**: buffer overflow attack
        # *   **9**: web attack
        # *   **10**: trojan backdoor
        # *   **11**: computer worm
        # *   **12**: mining
        # *   **13**: reverse shell
        # 
        # > If you do not specify this parameter, the intrusion events of all attack types are queried.
        self.attack_type = attack_type  # type: str
        # The edition of Cloud Firewall that you purchase. Valid values:
        # 
        # *   **2**: Premium Edition
        # *   **3**: Enterprise Edition
        # *   **4**: Ultimate Edition
        # *   **10**: Cloud Firewall that uses the pay-as-you-go billing method
        self.buy_version = buy_version  # type: long
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page  # type: str
        # The type of the risk events.\
        # Set the value to **session**, which indicates intrusion events.
        self.data_type = data_type  # type: str
        # The direction of the traffic for the intrusion events. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        # 
        # > If you do not specify this parameter, the intrusion events that are recorded for both inbound and outbound traffic are queried.
        self.direction = direction  # type: str
        # The destination IP address to query. If you specify this parameter, all intrusion events with the specified destination IP address are queried.
        self.dst_ip = dst_ip  # type: str
        # The ID of the destination VPC.
        # 
        # > If the FirewallType parameter is set to VpcFirewall, you must specify this parameter.
        self.dst_network_instance_id = dst_network_instance_id  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: str
        # The name of the intrusion event.
        self.event_name = event_name  # type: str
        # The type of the firewall. Valid values:
        # 
        # *   **VpcFirewall**: virtual private cloud (VPC) firewall
        # *   **InternetFirewall**: Internet firewall (default)
        self.firewall_type = firewall_type  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # Specifies whether to query the information about the geographical locations of IP addresses.
        # 
        # *   **true**: does not query the information about the geographical locations of IP addresses.
        # *   **false**: queries the information about the geographical locations of IP addresses. This is the default value.
        self.no_location = no_location  # type: str
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **asc**: the ascending order.
        # *   **desc**: the descending order. This is the default value.
        self.order = order  # type: str
        # The number of entries to return on each page.
        # 
        # Default value: **6**. Maximum value: **10**.
        self.page_size = page_size  # type: str
        # The status of the firewall. Valid values:
        # 
        # *   **1**: alerting
        # *   **2**: blocking
        # 
        # > If you do not specify this parameter, all intrusion events that are detected by the firewall are queried, regardless of the firewall status.
        self.rule_result = rule_result  # type: str
        # The module of the rule that is used to detect the intrusion events. Valid values:
        # 
        # *   **1**: basic protection
        # *   **2**: virtual patching
        # *   **4**: threat intelligence
        # 
        # > If you do not specify this parameter, the intrusion events that are detected by all rules are queried.
        self.rule_source = rule_source  # type: str
        # The field based on which you want to sort the results. Valid values:
        # 
        # *   **VulLevel**: The results are sorted based on the risk level field. This is the default value.
        # *   **LastTime**: The results are sorted based on the most recent occurrence time.
        self.sort = sort  # type: str
        # The source IP address to query. If you specify this parameter, all intrusion events with the specified source IP address are queried.
        self.src_ip = src_ip  # type: str
        # The ID of the source VPC.
        # 
        # > If the FirewallType parameter is set to VpcFirewall, you must specify this parameter.
        self.src_network_instance_id = src_network_instance_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: str
        # The risk level of the intrusion events. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        # 
        # > If you do not specify this parameter, the intrusion events that are at all risk levels are queried.
        self.vul_level = vul_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskEventGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.buy_version is not None:
            result['BuyVersion'] = self.buy_version
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.dst_network_instance_id is not None:
            result['DstNetworkInstanceId'] = self.dst_network_instance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.no_location is not None:
            result['NoLocation'] = self.no_location
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_network_instance_id is not None:
            result['SrcNetworkInstanceId'] = self.src_network_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('BuyVersion') is not None:
            self.buy_version = m.get('BuyVersion')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('DstNetworkInstanceId') is not None:
            self.dst_network_instance_id = m.get('DstNetworkInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NoLocation') is not None:
            self.no_location = m.get('NoLocation')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcNetworkInstanceId') is not None:
            self.src_network_instance_id = m.get('SrcNetworkInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')
        return self


class DescribeRiskEventGroupResponseBodyDataListIPLocationInfo(TeaModel):
    def __init__(self, city_id=None, city_name=None, country_id=None, country_name=None):
        # The ID of the city to which the IP address belongs.
        self.city_id = city_id  # type: str
        # The name of the city to which the IP address belongs.
        self.city_name = city_name  # type: str
        # The ID of the country to which the IP address belongs.
        self.country_id = country_id  # type: str
        # The name of the country to which the IP address belongs.
        self.country_name = country_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskEventGroupResponseBodyDataListIPLocationInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_id is not None:
            result['CityId'] = self.city_id
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.country_name is not None:
            result['CountryName'] = self.country_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')
        return self


class DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList(TeaModel):
    def __init__(self, region_no=None, resource_instance_id=None, resource_instance_name=None,
                 resource_private_ip=None):
        # The ID of the region to which the private IP address belongs.
        self.region_no = region_no  # type: str
        # The ID of the instance that uses the private IP address.
        self.resource_instance_id = resource_instance_id  # type: str
        # The name of the instance that uses the private IP address.
        self.resource_instance_name = resource_instance_name  # type: str
        # The private IP address.
        self.resource_private_ip = resource_private_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id
        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name
        if self.resource_private_ip is not None:
            result['ResourcePrivateIP'] = self.resource_private_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')
        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')
        if m.get('ResourcePrivateIP') is not None:
            self.resource_private_ip = m.get('ResourcePrivateIP')
        return self


class DescribeRiskEventGroupResponseBodyDataListVpcDstInfo(TeaModel):
    def __init__(self, ecs_instance_id=None, ecs_instance_name=None, network_instance_id=None,
                 network_instance_name=None, region_no=None):
        # The ID of the ECS instance.
        self.ecs_instance_id = ecs_instance_id  # type: str
        # The name of the ECS instance.
        self.ecs_instance_name = ecs_instance_name  # type: str
        # The ID of the VPC.
        self.network_instance_id = network_instance_id  # type: str
        # The name of the VPC.
        self.network_instance_name = network_instance_name  # type: str
        # The ID of the region in which the destination VPC resides.
        self.region_no = region_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskEventGroupResponseBodyDataListVpcDstInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        return self


class DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo(TeaModel):
    def __init__(self, ecs_instance_id=None, ecs_instance_name=None, network_instance_id=None,
                 network_instance_name=None, region_no=None):
        # The ID of the ECS instance.
        self.ecs_instance_id = ecs_instance_id  # type: str
        # The name of the ECS instance.
        self.ecs_instance_name = ecs_instance_name  # type: str
        # The ID of the VPC.
        self.network_instance_id = network_instance_id  # type: str
        # The name of the VPC.
        self.network_instance_name = network_instance_name  # type: str
        # The ID of the region in which the source VPC resides.
        self.region_no = region_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        return self


class DescribeRiskEventGroupResponseBodyDataList(TeaModel):
    def __init__(self, attack_app=None, attack_type=None, description=None, direction=None, dst_ip=None,
                 event_count=None, event_id=None, event_name=None, first_event_time=None, iplocation_info=None,
                 last_event_time=None, resource_private_iplist=None, resource_type=None, rule_id=None, rule_result=None,
                 rule_source=None, src_ip=None, src_iptag=None, src_private_iplist=None, tag=None, vpc_dst_info=None,
                 vpc_src_info=None, vul_level=None):
        # The name of the attacked application.
        self.attack_app = attack_app  # type: str
        # The attack type of the intrusion event. Valid values:
        # 
        # *   **1**: suspicious connection
        # *   **2**: command execution
        # *   **3**: brute-force attack
        # *   **4**: scanning
        # *   **5**: others
        # *   **6**: information leak
        # *   **7**: DoS attack
        # *   **8**: buffer overflow attack
        # *   **9**: web attack
        # *   **10**: trojan backdoor
        # *   **11**: computer worm
        # *   **12**: mining
        # *   **13**: reverse shell
        self.attack_type = attack_type  # type: int
        # The description of the intrusion event.
        self.description = description  # type: str
        # The direction of the traffic for the intrusion event. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        self.direction = direction  # type: str
        # The destination IP address that is included in the intrusion event.
        self.dst_ip = dst_ip  # type: str
        # The number of intrusion events.
        self.event_count = event_count  # type: int
        # The ID of the intrusion event.
        self.event_id = event_id  # type: str
        # The name of the intrusion event.
        self.event_name = event_name  # type: str
        # The time when the intrusion event was first detected. The value is a UNIX timestamp. Unit: seconds.
        self.first_event_time = first_event_time  # type: int
        # The geographical information about the IP address. The value is a struct that contains the following parameters: **CityId**, **CityName**, **CountryId**, and **CountryName**.\
        # ****************\
        self.iplocation_info = iplocation_info  # type: DescribeRiskEventGroupResponseBodyDataListIPLocationInfo
        # The time when the intrusion event was last detected. The value is a UNIX timestamp. Unit: seconds.
        self.last_event_time = last_event_time  # type: int
        # The information about the private IP address in the intrusion event. The value is an array that contains the following parameters: **RegionNo**, **ResourceInstanceId**, **ResourceInstanceName**, and **ResourcePrivateIP**.\
        # ****************\
        self.resource_private_iplist = resource_private_iplist  # type: list[DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList]
        # The type of the public IP address in the intrusion event. Valid values:
        # 
        # *   **EIP**: the elastic IP address (EIP)
        # *   **EcsPublicIP**: the public IP address of an Elastic Compute Service (ECS) instance
        # *   **EcsEIP**: the EIP of an ECS instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **NatEIP**: the EIP of a NAT gateway
        self.resource_type = resource_type  # type: str
        # The ID of the rule that is used to detect the intrusion event.
        self.rule_id = rule_id  # type: str
        # The status of the firewall. Valid values:
        # 
        # *   **1**: alerting
        # *   **2**: blocking
        self.rule_result = rule_result  # type: int
        # The module of the rule that is used to detect the intrusion event. Valid values:
        # 
        # *   **1**: basic protection
        # *   **2**: virtual patching
        # *   **4**: threat intelligence
        self.rule_source = rule_source  # type: int
        # The source IP address that is included in the intrusion event.
        self.src_ip = src_ip  # type: str
        # The tag added to the source IP address. The tag helps identify whether the source IP address is a back-to-origin IP address for a cloud service.
        self.src_iptag = src_iptag  # type: str
        # An array that consists of the source private IP addresses in the intrusion event.
        self.src_private_iplist = src_private_iplist  # type: list[str]
        # The tag added to the threat intelligence that is provided for major events.
        self.tag = tag  # type: str
        # The information about the destination VPC of the intrusion event. The value is a struct that contains the following parameters: **EcsInstanceId**, **EcsInstanceName**, **NetworkInstanceId**, **NetworkInstanceName**, and **RegionNo**.\
        # ********************\
        self.vpc_dst_info = vpc_dst_info  # type: DescribeRiskEventGroupResponseBodyDataListVpcDstInfo
        # The information about the source VPC of the intrusion event. The value is a struct that contains the following parameters: **EcsInstanceId**, **EcsInstanceName**, **NetworkInstanceId**, **NetworkInstanceName**, and **RegionNo**.\
        # ********************\
        self.vpc_src_info = vpc_src_info  # type: DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo
        # The risk level of the intrusion event. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        self.vul_level = vul_level  # type: int

    def validate(self):
        if self.iplocation_info:
            self.iplocation_info.validate()
        if self.resource_private_iplist:
            for k in self.resource_private_iplist:
                if k:
                    k.validate()
        if self.vpc_dst_info:
            self.vpc_dst_info.validate()
        if self.vpc_src_info:
            self.vpc_src_info.validate()

    def to_map(self):
        _map = super(DescribeRiskEventGroupResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.description is not None:
            result['Description'] = self.description
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.event_count is not None:
            result['EventCount'] = self.event_count
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.first_event_time is not None:
            result['FirstEventTime'] = self.first_event_time
        if self.iplocation_info is not None:
            result['IPLocationInfo'] = self.iplocation_info.to_map()
        if self.last_event_time is not None:
            result['LastEventTime'] = self.last_event_time
        result['ResourcePrivateIPList'] = []
        if self.resource_private_iplist is not None:
            for k in self.resource_private_iplist:
                result['ResourcePrivateIPList'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_iptag is not None:
            result['SrcIPTag'] = self.src_iptag
        if self.src_private_iplist is not None:
            result['SrcPrivateIPList'] = self.src_private_iplist
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.vpc_dst_info is not None:
            result['VpcDstInfo'] = self.vpc_dst_info.to_map()
        if self.vpc_src_info is not None:
            result['VpcSrcInfo'] = self.vpc_src_info.to_map()
        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('FirstEventTime') is not None:
            self.first_event_time = m.get('FirstEventTime')
        if m.get('IPLocationInfo') is not None:
            temp_model = DescribeRiskEventGroupResponseBodyDataListIPLocationInfo()
            self.iplocation_info = temp_model.from_map(m['IPLocationInfo'])
        if m.get('LastEventTime') is not None:
            self.last_event_time = m.get('LastEventTime')
        self.resource_private_iplist = []
        if m.get('ResourcePrivateIPList') is not None:
            for k in m.get('ResourcePrivateIPList'):
                temp_model = DescribeRiskEventGroupResponseBodyDataListResourcePrivateIPList()
                self.resource_private_iplist.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcIPTag') is not None:
            self.src_iptag = m.get('SrcIPTag')
        if m.get('SrcPrivateIPList') is not None:
            self.src_private_iplist = m.get('SrcPrivateIPList')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('VpcDstInfo') is not None:
            temp_model = DescribeRiskEventGroupResponseBodyDataListVpcDstInfo()
            self.vpc_dst_info = temp_model.from_map(m['VpcDstInfo'])
        if m.get('VpcSrcInfo') is not None:
            temp_model = DescribeRiskEventGroupResponseBodyDataListVpcSrcInfo()
            self.vpc_src_info = temp_model.from_map(m['VpcSrcInfo'])
        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')
        return self


class DescribeRiskEventGroupResponseBody(TeaModel):
    def __init__(self, data_list=None, request_id=None, total_count=None):
        # An array that consists of the details of the intrusion events.
        self.data_list = data_list  # type: list[DescribeRiskEventGroupResponseBodyDataList]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of risk events.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRiskEventGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeRiskEventGroupResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRiskEventGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRiskEventGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRiskEventGroupResponse, self).to_map()
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
            temp_model = DescribeRiskEventGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskEventPayloadRequest(TeaModel):
    def __init__(self, dst_ip=None, dst_vpc_id=None, end_time=None, firewall_type=None, public_ip=None, src_ip=None,
                 src_vpc_id=None, start_time=None, uuid=None):
        # The destination IP address to query. If you specify this parameter, all intrusion events with the specified destination IP address are queried.
        self.dst_ip = dst_ip  # type: str
        # The ID of the destination VPC to query. If you specify this parameter, all intrusion events that contain the specified ID of the destination VPC are queried.
        self.dst_vpc_id = dst_vpc_id  # type: str
        # The end of the time range to query. The value is a timestamp. Unit: seconds.
        self.end_time = end_time  # type: str
        # The type of the firewall. Valid values:
        # 
        # *   **VpcFirewall**: virtual private cloud (VPC) firewall
        # *   **InternetFirewall** (default): Internet firewall
        self.firewall_type = firewall_type  # type: str
        # The public IP address. If you specify this parameter, all intrusion events that contain the specified public IP address are queried.
        self.public_ip = public_ip  # type: str
        # The source IP address to query. If you specify this parameter, all intrusion events from the specified source IP address are queried.
        self.src_ip = src_ip  # type: str
        # The ID of the source VPC to query. If you specify this parameter, all intrusion events that contain the specified ID of the source VPC are queried.
        self.src_vpc_id = src_vpc_id  # type: str
        # The beginning of the time range to query. The value is a timestamp. Unit: seconds.
        self.start_time = start_time  # type: str
        # The UUID of the intrusion event.
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskEventPayloadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.dst_vpc_id is not None:
            result['DstVpcId'] = self.dst_vpc_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_vpc_id is not None:
            result['SrcVpcId'] = self.src_vpc_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uuid is not None:
            result['UUID'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('DstVpcId') is not None:
            self.dst_vpc_id = m.get('DstVpcId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcVpcId') is not None:
            self.src_vpc_id = m.get('SrcVpcId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        return self


class DescribeRiskEventPayloadResponseBody(TeaModel):
    def __init__(self, dst_ip=None, dst_port=None, dst_vpc_id=None, payload=None, payload_len=None, proto=None,
                 real_ip=None, request_id=None, src_ip=None, src_port=None, src_vpc_id=None, xforward_for=None):
        # The destination IP address of the intrusion event.
        self.dst_ip = dst_ip  # type: str
        # The destination port of the intrusion event.
        self.dst_port = dst_port  # type: int
        # The destination VPC ID of the intrusion event.
        self.dst_vpc_id = dst_vpc_id  # type: str
        # The attack payload of the intrusion event.
        self.payload = payload  # type: str
        # The length of the attack payload of the intrusion event.
        self.payload_len = payload_len  # type: int
        # The protocol type of intrusion event. Valid values:
        # 
        # *   **TCP**\
        # *   **UDP**\
        self.proto = proto  # type: str
        # The HTTP X-Real-IP field.
        self.real_ip = real_ip  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The source IP address of the intrusion event.
        self.src_ip = src_ip  # type: str
        # The source port of the intrusion event.
        self.src_port = src_port  # type: int
        # The source VPC ID of the intrusion event.
        self.src_vpc_id = src_vpc_id  # type: str
        # The HTTP X-Forwarded-For field.
        self.xforward_for = xforward_for  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRiskEventPayloadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_vpc_id is not None:
            result['DstVpcId'] = self.dst_vpc_id
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.payload_len is not None:
            result['PayloadLen'] = self.payload_len
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.real_ip is not None:
            result['RealIp'] = self.real_ip
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_port is not None:
            result['SrcPort'] = self.src_port
        if self.src_vpc_id is not None:
            result['SrcVpcId'] = self.src_vpc_id
        if self.xforward_for is not None:
            result['XForwardFor'] = self.xforward_for
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstVpcId') is not None:
            self.dst_vpc_id = m.get('DstVpcId')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('PayloadLen') is not None:
            self.payload_len = m.get('PayloadLen')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('RealIp') is not None:
            self.real_ip = m.get('RealIp')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')
        if m.get('SrcVpcId') is not None:
            self.src_vpc_id = m.get('SrcVpcId')
        if m.get('XForwardFor') is not None:
            self.xforward_for = m.get('XForwardFor')
        return self


class DescribeRiskEventPayloadResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRiskEventPayloadResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRiskEventPayloadResponse, self).to_map()
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
            temp_model = DescribeRiskEventPayloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrFirewallPolicyBackUpAssociationListRequest(TeaModel):
    def __init__(self, firewall_id=None, lang=None, tr_firewall_route_policy_id=None):
        self.firewall_id = firewall_id  # type: str
        self.lang = lang  # type: str
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallPolicyBackUpAssociationListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class DescribeTrFirewallPolicyBackUpAssociationListResponseBodyPolicyAssociationBackupConfigs(TeaModel):
    def __init__(self, candidate_id=None, candidate_name=None, candidate_type=None, current_route_table_id=None,
                 original_route_table_id=None):
        self.candidate_id = candidate_id  # type: str
        self.candidate_name = candidate_name  # type: str
        self.candidate_type = candidate_type  # type: str
        self.current_route_table_id = current_route_table_id  # type: str
        self.original_route_table_id = original_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallPolicyBackUpAssociationListResponseBodyPolicyAssociationBackupConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_name is not None:
            result['CandidateName'] = self.candidate_name
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        if self.current_route_table_id is not None:
            result['CurrentRouteTableId'] = self.current_route_table_id
        if self.original_route_table_id is not None:
            result['OriginalRouteTableId'] = self.original_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateName') is not None:
            self.candidate_name = m.get('CandidateName')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        if m.get('CurrentRouteTableId') is not None:
            self.current_route_table_id = m.get('CurrentRouteTableId')
        if m.get('OriginalRouteTableId') is not None:
            self.original_route_table_id = m.get('OriginalRouteTableId')
        return self


class DescribeTrFirewallPolicyBackUpAssociationListResponseBody(TeaModel):
    def __init__(self, policy_association_backup_configs=None, request_id=None):
        self.policy_association_backup_configs = policy_association_backup_configs  # type: list[DescribeTrFirewallPolicyBackUpAssociationListResponseBodyPolicyAssociationBackupConfigs]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy_association_backup_configs:
            for k in self.policy_association_backup_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallPolicyBackUpAssociationListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyAssociationBackupConfigs'] = []
        if self.policy_association_backup_configs is not None:
            for k in self.policy_association_backup_configs:
                result['PolicyAssociationBackupConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policy_association_backup_configs = []
        if m.get('PolicyAssociationBackupConfigs') is not None:
            for k in m.get('PolicyAssociationBackupConfigs'):
                temp_model = DescribeTrFirewallPolicyBackUpAssociationListResponseBodyPolicyAssociationBackupConfigs()
                self.policy_association_backup_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTrFirewallPolicyBackUpAssociationListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTrFirewallPolicyBackUpAssociationListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallPolicyBackUpAssociationListResponse, self).to_map()
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
            temp_model = DescribeTrFirewallPolicyBackUpAssociationListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrFirewallV2RoutePolicyListRequest(TeaModel):
    def __init__(self, current_page=None, firewall_id=None, lang=None, page_size=None, policy_id=None):
        self.current_page = current_page  # type: int
        self.firewall_id = firewall_id  # type: str
        self.lang = lang  # type: str
        self.page_size = page_size  # type: int
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallV2RoutePolicyListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesDestCandidateList(TeaModel):
    def __init__(self, candidate_id=None, candidate_type=None):
        self.candidate_id = candidate_id  # type: str
        self.candidate_type = candidate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesDestCandidateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesSrcCandidateList(TeaModel):
    def __init__(self, candidate_id=None, candidate_type=None):
        self.candidate_id = candidate_id  # type: str
        self.candidate_type = candidate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesSrcCandidateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePolicies(TeaModel):
    def __init__(self, dest_candidate_list=None, policy_description=None, policy_name=None, policy_status=None,
                 policy_type=None, src_candidate_list=None, tr_firewall_route_policy_id=None):
        self.dest_candidate_list = dest_candidate_list  # type: list[DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesDestCandidateList]
        self.policy_description = policy_description  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_status = policy_status  # type: str
        self.policy_type = policy_type  # type: str
        self.src_candidate_list = src_candidate_list  # type: list[DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesSrcCandidateList]
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id  # type: str

    def validate(self):
        if self.dest_candidate_list:
            for k in self.dest_candidate_list:
                if k:
                    k.validate()
        if self.src_candidate_list:
            for k in self.src_candidate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DestCandidateList'] = []
        if self.dest_candidate_list is not None:
            for k in self.dest_candidate_list:
                result['DestCandidateList'].append(k.to_map() if k else None)
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        result['SrcCandidateList'] = []
        if self.src_candidate_list is not None:
            for k in self.src_candidate_list:
                result['SrcCandidateList'].append(k.to_map() if k else None)
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dest_candidate_list = []
        if m.get('DestCandidateList') is not None:
            for k in m.get('DestCandidateList'):
                temp_model = DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesDestCandidateList()
                self.dest_candidate_list.append(temp_model.from_map(k))
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        self.src_candidate_list = []
        if m.get('SrcCandidateList') is not None:
            for k in m.get('SrcCandidateList'):
                temp_model = DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesSrcCandidateList()
                self.src_candidate_list.append(temp_model.from_map(k))
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class DescribeTrFirewallV2RoutePolicyListResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, tr_firewall_route_policies=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str
        self.tr_firewall_route_policies = tr_firewall_route_policies  # type: list[DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePolicies]

    def validate(self):
        if self.tr_firewall_route_policies:
            for k in self.tr_firewall_route_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallV2RoutePolicyListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TrFirewallRoutePolicies'] = []
        if self.tr_firewall_route_policies is not None:
            for k in self.tr_firewall_route_policies:
                result['TrFirewallRoutePolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tr_firewall_route_policies = []
        if m.get('TrFirewallRoutePolicies') is not None:
            for k in m.get('TrFirewallRoutePolicies'):
                temp_model = DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePolicies()
                self.tr_firewall_route_policies.append(temp_model.from_map(k))
        return self


class DescribeTrFirewallV2RoutePolicyListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTrFirewallV2RoutePolicyListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallV2RoutePolicyListResponse, self).to_map()
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
            temp_model = DescribeTrFirewallV2RoutePolicyListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrFirewallsV2DetailRequest(TeaModel):
    def __init__(self, firewall_id=None, lang=None):
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallsV2DetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeTrFirewallsV2DetailResponseBody(TeaModel):
    def __init__(self, cen_id=None, firewall_description=None, firewall_eni_id=None, firewall_eni_vpc_id=None,
                 firewall_eni_vswitch_id=None, firewall_id=None, firewall_name=None, firewall_status=None, firewall_subnet_cidr=None,
                 firewall_switch_status=None, firewall_vpc_cidr=None, region_no=None, request_id=None, route_mode=None,
                 tr_attachment_master_cidr=None, tr_attachment_slave_cidr=None, transit_router_id=None):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id  # type: str
        # The description of the VPC firewall.
        self.firewall_description = firewall_description  # type: str
        # The ID of the Elastic Network Interface (ENI) with which the VPC firewall is associated.
        self.firewall_eni_id = firewall_eni_id  # type: str
        # The ID of the VPC to which the ENI is attached.
        self.firewall_eni_vpc_id = firewall_eni_vpc_id  # type: str
        # The ID of the vSwitch with which the ENI is associated.
        self.firewall_eni_vswitch_id = firewall_eni_vswitch_id  # type: str
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id  # type: str
        # The name of the VPC firewall.
        self.firewall_name = firewall_name  # type: str
        # The status of the VPC firewall. Valid values:
        # 
        # *   Creating
        # *   Deleting
        # *   Ready
        self.firewall_status = firewall_status  # type: str
        # The subnet CIDR block of the VPC in which the ENI of the firewall is stored in automatic mode.
        self.firewall_subnet_cidr = firewall_subnet_cidr  # type: str
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not created.
        # *   **configured**: The VPC firewall is created but is not enabled.
        # *   **creating**: The VPC firewall is being created.
        # *   **opening**: The VPC firewall is being enabled.
        # *   **deleting**: The VPC firewall is being deleted.
        # 
        # > If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status  # type: str
        # The CIDR block that is allocated to the VPC created for the VPC firewall in automatic mode.
        self.firewall_vpc_cidr = firewall_vpc_cidr  # type: str
        # The region ID of the transit router.
        self.region_no = region_no  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode  # type: str
        # The primary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_master_cidr = tr_attachment_master_cidr  # type: str
        # The secondary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_slave_cidr = tr_attachment_slave_cidr  # type: str
        # The ID of the transit router.
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallsV2DetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.firewall_description is not None:
            result['FirewallDescription'] = self.firewall_description
        if self.firewall_eni_id is not None:
            result['FirewallEniId'] = self.firewall_eni_id
        if self.firewall_eni_vpc_id is not None:
            result['FirewallEniVpcId'] = self.firewall_eni_vpc_id
        if self.firewall_eni_vswitch_id is not None:
            result['FirewallEniVswitchId'] = self.firewall_eni_vswitch_id
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name
        if self.firewall_status is not None:
            result['FirewallStatus'] = self.firewall_status
        if self.firewall_subnet_cidr is not None:
            result['FirewallSubnetCidr'] = self.firewall_subnet_cidr
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.firewall_vpc_cidr is not None:
            result['FirewallVpcCidr'] = self.firewall_vpc_cidr
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.tr_attachment_master_cidr is not None:
            result['TrAttachmentMasterCidr'] = self.tr_attachment_master_cidr
        if self.tr_attachment_slave_cidr is not None:
            result['TrAttachmentSlaveCidr'] = self.tr_attachment_slave_cidr
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('FirewallDescription') is not None:
            self.firewall_description = m.get('FirewallDescription')
        if m.get('FirewallEniId') is not None:
            self.firewall_eni_id = m.get('FirewallEniId')
        if m.get('FirewallEniVpcId') is not None:
            self.firewall_eni_vpc_id = m.get('FirewallEniVpcId')
        if m.get('FirewallEniVswitchId') is not None:
            self.firewall_eni_vswitch_id = m.get('FirewallEniVswitchId')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')
        if m.get('FirewallStatus') is not None:
            self.firewall_status = m.get('FirewallStatus')
        if m.get('FirewallSubnetCidr') is not None:
            self.firewall_subnet_cidr = m.get('FirewallSubnetCidr')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('FirewallVpcCidr') is not None:
            self.firewall_vpc_cidr = m.get('FirewallVpcCidr')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('TrAttachmentMasterCidr') is not None:
            self.tr_attachment_master_cidr = m.get('TrAttachmentMasterCidr')
        if m.get('TrAttachmentSlaveCidr') is not None:
            self.tr_attachment_slave_cidr = m.get('TrAttachmentSlaveCidr')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class DescribeTrFirewallsV2DetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTrFirewallsV2DetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallsV2DetailResponse, self).to_map()
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
            temp_model = DescribeTrFirewallsV2DetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrFirewallsV2ListRequest(TeaModel):
    def __init__(self, cen_id=None, current_page=None, firewall_id=None, firewall_name=None,
                 firewall_switch_status=None, lang=None, owner_id=None, page_size=None, region_no=None, route_mode=None,
                 transit_router_id=None):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id  # type: str
        # The page number. Default value: **1**.
        self.current_page = current_page  # type: int
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id  # type: str
        # The name of the VPC firewall.
        self.firewall_name = firewall_name  # type: str
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not created.
        # *   **configured**: The VPC firewall is created but is not enabled.
        # *   **creating**: The VPC firewall is being created.
        # *   **opening**: The VPC firewall is being enabled.
        # *   **deleting**: The VPC firewall is being deleted.
        # 
        # >  If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        self.owner_id = owner_id  # type: str
        # The number of entries per page. Default value: 10.
        self.page_size = page_size  # type: int
        # The region ID of the transit router.
        self.region_no = region_no  # type: str
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        # 
        # >  If you do not specify this parameter, VPC firewalls in all routing modes are queried.
        self.route_mode = route_mode  # type: str
        # The ID of the transit router.
        self.transit_router_id = transit_router_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallsV2ListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        return self


class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsIpsConfig(TeaModel):
    def __init__(self, basic_rules=None, enable_all_patch=None, run_mode=None):
        # Indicates whether basic protection is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules  # type: int
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch  # type: int
        # The mode of the IPS. Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsIpsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsProtectedResource(TeaModel):
    def __init__(self, count=None, peer_tr_list=None, vbr_list=None, vpc_list=None, vpn_list=None):
        # The number of protected resources.
        self.count = count  # type: int
        # The protected peer transit routers.
        self.peer_tr_list = peer_tr_list  # type: list[str]
        # The protected virtual border routers (VBRs).
        self.vbr_list = vbr_list  # type: list[str]
        # The protected VPCs.
        self.vpc_list = vpc_list  # type: list[str]
        # The protected VPN gateways.
        self.vpn_list = vpn_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsProtectedResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.peer_tr_list is not None:
            result['PeerTrList'] = self.peer_tr_list
        if self.vbr_list is not None:
            result['VbrList'] = self.vbr_list
        if self.vpc_list is not None:
            result['VpcList'] = self.vpc_list
        if self.vpn_list is not None:
            result['VpnList'] = self.vpn_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PeerTrList') is not None:
            self.peer_tr_list = m.get('PeerTrList')
        if m.get('VbrList') is not None:
            self.vbr_list = m.get('VbrList')
        if m.get('VpcList') is not None:
            self.vpc_list = m.get('VpcList')
        if m.get('VpnList') is not None:
            self.vpn_list = m.get('VpnList')
        return self


class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsUnprotectedResource(TeaModel):
    def __init__(self, count=None, peer_tr_list=None, vbr_list=None, vpc_list=None, vpn_list=None):
        # The number of unprotected resources.
        self.count = count  # type: int
        # The unprotected peer transit routers.
        self.peer_tr_list = peer_tr_list  # type: list[str]
        # The unprotected VBRs.
        self.vbr_list = vbr_list  # type: list[str]
        # The unprotected VPCs.
        self.vpc_list = vpc_list  # type: list[str]
        # The unprotected VPN gateways.
        self.vpn_list = vpn_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsUnprotectedResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.peer_tr_list is not None:
            result['PeerTrList'] = self.peer_tr_list
        if self.vbr_list is not None:
            result['VbrList'] = self.vbr_list
        if self.vpc_list is not None:
            result['VpcList'] = self.vpc_list
        if self.vpn_list is not None:
            result['VpnList'] = self.vpn_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PeerTrList') is not None:
            self.peer_tr_list = m.get('PeerTrList')
        if m.get('VbrList') is not None:
            self.vbr_list = m.get('VbrList')
        if m.get('VpcList') is not None:
            self.vpc_list = m.get('VpcList')
        if m.get('VpnList') is not None:
            self.vpn_list = m.get('VpnList')
        return self


class DescribeTrFirewallsV2ListResponseBodyVpcTrFirewalls(TeaModel):
    def __init__(self, cen_id=None, cen_name=None, firewall_id=None, firewall_switch_status=None, ips_config=None,
                 owner_id=None, precheck_status=None, protected_resource=None, region_no=None, region_status=None,
                 result_code=None, route_mode=None, transit_router_id=None, unprotected_resource=None, vpc_firewall_name=None):
        # The ID of the CEN instance.
        self.cen_id = cen_id  # type: str
        # The name of the CEN instance.
        self.cen_name = cen_name  # type: str
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id  # type: str
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not created.
        # *   **configured**: The VPC firewall is created but is not enabled.
        # *   **creating**: The VPC firewall is being created.
        # *   **opening**: The VPC firewall is being enabled.
        # *   **deleting**: The VPC firewall is being deleted.
        # 
        # >  If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status  # type: str
        # The information about the intrusion prevention system (IPS) configuration.
        self.ips_config = ips_config  # type: DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsIpsConfig
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id  # type: long
        # Indicates whether the VPC firewall can be automatically enabled. Valid values:
        # 
        # *   **passed**: yes
        # *   **failed**: no
        # *   **unknown**\
        self.precheck_status = precheck_status  # type: str
        # The protected resources.
        self.protected_resource = protected_resource  # type: DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsProtectedResource
        # The region ID of the transit router.
        self.region_no = region_no  # type: str
        # Indicates whether you can create a VPC firewall in a specified region. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status  # type: str
        # The result code of the operation that creates the VPC firewall. Valid values:
        # 
        # *   **RegionDisable**: VPC Firewall is not supported in the region of the network instance. You cannot create a VPC firewall for the network instance.
        # *   **Empty string**: You can create a VPC firewall for the network instance.
        self.result_code = result_code  # type: str
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode  # type: str
        # The ID of the transit router.
        self.transit_router_id = transit_router_id  # type: str
        # The unprotected resources.
        self.unprotected_resource = unprotected_resource  # type: DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsUnprotectedResource
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str

    def validate(self):
        if self.ips_config:
            self.ips_config.validate()
        if self.protected_resource:
            self.protected_resource.validate()
        if self.unprotected_resource:
            self.unprotected_resource.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallsV2ListResponseBodyVpcTrFirewalls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_name is not None:
            result['CenName'] = self.cen_name
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.ips_config is not None:
            result['IpsConfig'] = self.ips_config.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status
        if self.protected_resource is not None:
            result['ProtectedResource'] = self.protected_resource.to_map()
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.region_status is not None:
            result['RegionStatus'] = self.region_status
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.unprotected_resource is not None:
            result['UnprotectedResource'] = self.unprotected_resource.to_map()
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenName') is not None:
            self.cen_name = m.get('CenName')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('IpsConfig') is not None:
            temp_model = DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsIpsConfig()
            self.ips_config = temp_model.from_map(m['IpsConfig'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PrecheckStatus') is not None:
            self.precheck_status = m.get('PrecheckStatus')
        if m.get('ProtectedResource') is not None:
            temp_model = DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsProtectedResource()
            self.protected_resource = temp_model.from_map(m['ProtectedResource'])
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('UnprotectedResource') is not None:
            temp_model = DescribeTrFirewallsV2ListResponseBodyVpcTrFirewallsUnprotectedResource()
            self.unprotected_resource = temp_model.from_map(m['UnprotectedResource'])
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeTrFirewallsV2ListResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, vpc_tr_firewalls=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: str
        # The VPC firewalls.
        self.vpc_tr_firewalls = vpc_tr_firewalls  # type: list[DescribeTrFirewallsV2ListResponseBodyVpcTrFirewalls]

    def validate(self):
        if self.vpc_tr_firewalls:
            for k in self.vpc_tr_firewalls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallsV2ListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VpcTrFirewalls'] = []
        if self.vpc_tr_firewalls is not None:
            for k in self.vpc_tr_firewalls:
                result['VpcTrFirewalls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vpc_tr_firewalls = []
        if m.get('VpcTrFirewalls') is not None:
            for k in m.get('VpcTrFirewalls'):
                temp_model = DescribeTrFirewallsV2ListResponseBodyVpcTrFirewalls()
                self.vpc_tr_firewalls.append(temp_model.from_map(k))
        return self


class DescribeTrFirewallsV2ListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTrFirewallsV2ListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallsV2ListResponse, self).to_map()
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
            temp_model = DescribeTrFirewallsV2ListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrFirewallsV2RouteListRequest(TeaModel):
    def __init__(self, current_page=None, firewall_id=None, lang=None, page_size=None,
                 tr_firewall_route_policy_id=None):
        self.current_page = current_page  # type: str
        self.firewall_id = firewall_id  # type: str
        self.lang = lang  # type: str
        self.page_size = page_size  # type: str
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallsV2RouteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class DescribeTrFirewallsV2RouteListResponseBodyFirewallRouteDetailList(TeaModel):
    def __init__(self, tr_firewall_route_destination=None, tr_firewall_route_nexthop=None,
                 tr_firewall_route_policy_id=None, tr_firewall_route_table_id=None):
        self.tr_firewall_route_destination = tr_firewall_route_destination  # type: str
        self.tr_firewall_route_nexthop = tr_firewall_route_nexthop  # type: str
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id  # type: str
        self.tr_firewall_route_table_id = tr_firewall_route_table_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrFirewallsV2RouteListResponseBodyFirewallRouteDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tr_firewall_route_destination is not None:
            result['TrFirewallRouteDestination'] = self.tr_firewall_route_destination
        if self.tr_firewall_route_nexthop is not None:
            result['TrFirewallRouteNexthop'] = self.tr_firewall_route_nexthop
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        if self.tr_firewall_route_table_id is not None:
            result['TrFirewallRouteTableId'] = self.tr_firewall_route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrFirewallRouteDestination') is not None:
            self.tr_firewall_route_destination = m.get('TrFirewallRouteDestination')
        if m.get('TrFirewallRouteNexthop') is not None:
            self.tr_firewall_route_nexthop = m.get('TrFirewallRouteNexthop')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        if m.get('TrFirewallRouteTableId') is not None:
            self.tr_firewall_route_table_id = m.get('TrFirewallRouteTableId')
        return self


class DescribeTrFirewallsV2RouteListResponseBody(TeaModel):
    def __init__(self, firewall_route_detail_list=None, request_id=None):
        self.firewall_route_detail_list = firewall_route_detail_list  # type: list[DescribeTrFirewallsV2RouteListResponseBodyFirewallRouteDetailList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.firewall_route_detail_list:
            for k in self.firewall_route_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallsV2RouteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FirewallRouteDetailList'] = []
        if self.firewall_route_detail_list is not None:
            for k in self.firewall_route_detail_list:
                result['FirewallRouteDetailList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.firewall_route_detail_list = []
        if m.get('FirewallRouteDetailList') is not None:
            for k in m.get('FirewallRouteDetailList'):
                temp_model = DescribeTrFirewallsV2RouteListResponseBodyFirewallRouteDetailList()
                self.firewall_route_detail_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTrFirewallsV2RouteListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTrFirewallsV2RouteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTrFirewallsV2RouteListResponse, self).to_map()
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
            temp_model = DescribeTrFirewallsV2RouteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserAssetIPTrafficInfoRequest(TeaModel):
    def __init__(self, asset_ip=None, lang=None, traffic_time=None):
        # The IP address of the asset.
        self.asset_ip = asset_ip  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The point in time to query. The value is a UNIX timestamp. Unit: seconds.
        self.traffic_time = traffic_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserAssetIPTrafficInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_ip is not None:
            result['AssetIP'] = self.asset_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.traffic_time is not None:
            result['TrafficTime'] = self.traffic_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetIP') is not None:
            self.asset_ip = m.get('AssetIP')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('TrafficTime') is not None:
            self.traffic_time = m.get('TrafficTime')
        return self


class DescribeUserAssetIPTrafficInfoResponseBody(TeaModel):
    def __init__(self, end_time=None, in_bps=None, in_pps=None, new_conn=None, out_bps=None, out_pps=None,
                 request_id=None, session_count=None, start_time=None):
        # The end of the time range that is queried. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The network throughput, which indicates the inbound traffic rate. Unit: bit/s.
        self.in_bps = in_bps  # type: long
        # The network throughput, which indicates the inbound packet rate. Unit: packets per second (pps).
        self.in_pps = in_pps  # type: long
        # The number of new connections.
        self.new_conn = new_conn  # type: long
        # The network throughput, which indicates the outbound traffic rate. Unit: bit/s.
        self.out_bps = out_bps  # type: long
        # The network throughput, which indicates the outbound packet rate. Unit: pps.
        self.out_pps = out_pps  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of requests.
        self.session_count = session_count  # type: long
        # The beginning of the time range that is queried. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserAssetIPTrafficInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.in_pps is not None:
            result['InPps'] = self.in_pps
        if self.new_conn is not None:
            result['NewConn'] = self.new_conn
        if self.out_bps is not None:
            result['OutBps'] = self.out_bps
        if self.out_pps is not None:
            result['OutPps'] = self.out_pps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')
        if m.get('NewConn') is not None:
            self.new_conn = m.get('NewConn')
        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')
        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeUserAssetIPTrafficInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserAssetIPTrafficInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserAssetIPTrafficInfoResponse, self).to_map()
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
            temp_model = DescribeUserAssetIPTrafficInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserIPSWhitelistRequest(TeaModel):
    def __init__(self, lang=None, source_ip=None):
        self.lang = lang  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserIPSWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeUserIPSWhitelistResponseBodyIpv6Whitelists(TeaModel):
    def __init__(self, direction=None, list_type=None, list_value=None, white_list_value=None, white_type=None):
        self.direction = direction  # type: long
        self.list_type = list_type  # type: long
        self.list_value = list_value  # type: str
        self.white_list_value = white_list_value  # type: list[str]
        self.white_type = white_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserIPSWhitelistResponseBodyIpv6Whitelists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.list_type is not None:
            result['ListType'] = self.list_type
        if self.list_value is not None:
            result['ListValue'] = self.list_value
        if self.white_list_value is not None:
            result['WhiteListValue'] = self.white_list_value
        if self.white_type is not None:
            result['WhiteType'] = self.white_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')
        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')
        if m.get('WhiteListValue') is not None:
            self.white_list_value = m.get('WhiteListValue')
        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')
        return self


class DescribeUserIPSWhitelistResponseBodyWhitelists(TeaModel):
    def __init__(self, direction=None, list_type=None, list_value=None, white_list_value=None, white_type=None):
        self.direction = direction  # type: long
        self.list_type = list_type  # type: long
        self.list_value = list_value  # type: str
        self.white_list_value = white_list_value  # type: list[str]
        self.white_type = white_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserIPSWhitelistResponseBodyWhitelists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.list_type is not None:
            result['ListType'] = self.list_type
        if self.list_value is not None:
            result['ListValue'] = self.list_value
        if self.white_list_value is not None:
            result['WhiteListValue'] = self.white_list_value
        if self.white_type is not None:
            result['WhiteType'] = self.white_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')
        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')
        if m.get('WhiteListValue') is not None:
            self.white_list_value = m.get('WhiteListValue')
        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')
        return self


class DescribeUserIPSWhitelistResponseBody(TeaModel):
    def __init__(self, ipv_6whitelists=None, request_id=None, whitelists=None):
        self.ipv_6whitelists = ipv_6whitelists  # type: list[DescribeUserIPSWhitelistResponseBodyIpv6Whitelists]
        self.request_id = request_id  # type: str
        self.whitelists = whitelists  # type: list[DescribeUserIPSWhitelistResponseBodyWhitelists]

    def validate(self):
        if self.ipv_6whitelists:
            for k in self.ipv_6whitelists:
                if k:
                    k.validate()
        if self.whitelists:
            for k in self.whitelists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserIPSWhitelistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Ipv6Whitelists'] = []
        if self.ipv_6whitelists is not None:
            for k in self.ipv_6whitelists:
                result['Ipv6Whitelists'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Whitelists'] = []
        if self.whitelists is not None:
            for k in self.whitelists:
                result['Whitelists'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ipv_6whitelists = []
        if m.get('Ipv6Whitelists') is not None:
            for k in m.get('Ipv6Whitelists'):
                temp_model = DescribeUserIPSWhitelistResponseBodyIpv6Whitelists()
                self.ipv_6whitelists.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.whitelists = []
        if m.get('Whitelists') is not None:
            for k in m.get('Whitelists'):
                temp_model = DescribeUserIPSWhitelistResponseBodyWhitelists()
                self.whitelists.append(temp_model.from_map(k))
        return self


class DescribeUserIPSWhitelistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserIPSWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserIPSWhitelistResponse, self).to_map()
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
            temp_model = DescribeUserIPSWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallAclGroupListRequest(TeaModel):
    def __init__(self, current_page=None, firewall_configure_status=None, lang=None, page_size=None):
        # The number of the page to return. Default value: 1.
        self.current_page = current_page  # type: str
        # Specifies whether VPC firewalls are configured. Valid values:
        # 
        # *   **notconfigured**: VPC firewalls are not configured.
        # *   **configured**: VPC firewalls are configured.
        # *   If this parameter is left empty, all policy groups of access control policies are queried.
        self.firewall_configure_status = firewall_configure_status  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The number of entries to return on each page. Maximum value: 50.
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallAclGroupListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_configure_status is not None:
            result['FirewallConfigureStatus'] = self.firewall_configure_status
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallConfigureStatus') is not None:
            self.firewall_configure_status = m.get('FirewallConfigureStatus')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeVpcFirewallAclGroupListResponseBodyAclGroupList(TeaModel):
    def __init__(self, acl_group_id=None, acl_group_name=None, acl_rule_count=None, member_uid=None):
        # The ID of the policy group.
        # 
        # Valid values:
        # 
        # *   If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance.
        # 
        #     Example: cen-ervw0g12b5jbw\*\*\*\*\
        # 
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the ID of the VPC firewall instance.
        # 
        #     Example: vfw-a42bbb7b887148c9\*\*\*\*\
        self.acl_group_id = acl_group_id  # type: str
        # The name of the policy group. Valid values:
        # 
        # *   If the VPC firewall is used to protect a CEN instance, the value of this parameter is the name of the CEN instance.
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the name of the VPC firewall instance.
        self.acl_group_name = acl_group_name  # type: str
        self.acl_rule_count = acl_rule_count  # type: int
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallAclGroupListResponseBodyAclGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_group_id is not None:
            result['AclGroupId'] = self.acl_group_id
        if self.acl_group_name is not None:
            result['AclGroupName'] = self.acl_group_name
        if self.acl_rule_count is not None:
            result['AclRuleCount'] = self.acl_rule_count
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclGroupId') is not None:
            self.acl_group_id = m.get('AclGroupId')
        if m.get('AclGroupName') is not None:
            self.acl_group_name = m.get('AclGroupName')
        if m.get('AclRuleCount') is not None:
            self.acl_rule_count = m.get('AclRuleCount')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        return self


class DescribeVpcFirewallAclGroupListResponseBody(TeaModel):
    def __init__(self, acl_group_list=None, request_id=None, total_count=None):
        # An array that consists of the information about the policy group.
        self.acl_group_list = acl_group_list  # type: list[DescribeVpcFirewallAclGroupListResponseBodyAclGroupList]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of the policy groups that are returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.acl_group_list:
            for k in self.acl_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallAclGroupListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclGroupList'] = []
        if self.acl_group_list is not None:
            for k in self.acl_group_list:
                result['AclGroupList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acl_group_list = []
        if m.get('AclGroupList') is not None:
            for k in m.get('AclGroupList'):
                temp_model = DescribeVpcFirewallAclGroupListResponseBodyAclGroupList()
                self.acl_group_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeVpcFirewallAclGroupListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVpcFirewallAclGroupListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallAclGroupListResponse, self).to_map()
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
            temp_model = DescribeVpcFirewallAclGroupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallCenDetailRequest(TeaModel):
    def __init__(self, lang=None, network_instance_id=None, vpc_firewall_id=None):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The ID of the VPC for which the VPC firewall is created.
        self.network_instance_id = network_instance_id  # type: str
        # The instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallCenList](~~345777~~) operation to query the instance IDs of VPC firewalls.
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallCenDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallCenDetailResponseBodyFirewallVpc(TeaModel):
    def __init__(self, allow_configuration=None, vpc_cidr=None, vpc_id=None, vswitch_cidr=None, vswitch_id=None,
                 zone_id=None):
        # Indicates whether you can specify a CIDR block when you create a VPC firewall for a Basic Edition transit router of a CEN instance. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.allow_configuration = allow_configuration  # type: int
        # The CIDR block of the VPC.
        self.vpc_cidr = vpc_cidr  # type: str
        # The VPC ID.
        self.vpc_id = vpc_id  # type: str
        # The CIDR block of the vSwitch.
        self.vswitch_cidr = vswitch_cidr  # type: str
        # The vSwitch ID.
        self.vswitch_id = vswitch_id  # type: str
        # The zone ID.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallCenDetailResponseBodyFirewallVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_configuration is not None:
            result['AllowConfiguration'] = self.allow_configuration
        if self.vpc_cidr is not None:
            result['VpcCidr'] = self.vpc_cidr
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_cidr is not None:
            result['VswitchCidr'] = self.vswitch_cidr
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowConfiguration') is not None:
            self.allow_configuration = m.get('AllowConfiguration')
        if m.get('VpcCidr') is not None:
            self.vpc_cidr = m.get('VpcCidr')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchCidr') is not None:
            self.vswitch_cidr = m.get('VswitchCidr')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList(TeaModel):
    def __init__(self, eni_id=None, eni_private_ip_address=None, eni_vswitch_id=None):
        # The ID of the ENI that belongs to the VPC.
        self.eni_id = eni_id  # type: str
        # The private IP address of the ENI that belongs to the VPC.
        self.eni_private_ip_address = eni_private_ip_address  # type: str
        # The ID of the vSwitch to which the ENI is connected.
        self.eni_vswitch_id = eni_vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.eni_private_ip_address is not None:
            result['EniPrivateIpAddress'] = self.eni_private_ip_address
        if self.eni_vswitch_id is not None:
            result['EniVSwitchId'] = self.eni_vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('EniPrivateIpAddress') is not None:
            self.eni_private_ip_address = m.get('EniPrivateIpAddress')
        if m.get('EniVSwitchId') is not None:
            self.eni_vswitch_id = m.get('EniVSwitchId')
        return self


class DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(self, destination_cidr=None, next_hop_instance_id=None):
        # The destination CIDR block of the VPC.
        self.destination_cidr = destination_cidr  # type: str
        # The instance ID of the next hop for the VPC.
        self.next_hop_instance_id = next_hop_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableList(TeaModel):
    def __init__(self, route_entry_list=None, route_table_id=None):
        # The route entries for the VPC.
        self.route_entry_list = route_entry_list  # type: list[DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList]
        # The route table ID of the VPC.
        self.route_table_id = route_table_id  # type: str

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallCenDetailResponseBodyLocalVpc(TeaModel):
    def __init__(self, attachment_id=None, attachment_name=None, defend_cidr_list=None, eni_list=None,
                 manual_vswitch_id=None, network_instance_id=None, network_instance_name=None, network_instance_type=None,
                 owner_id=None, region_no=None, route_mode=None, support_manual_mode=None, transit_router_id=None,
                 transit_router_type=None, vpc_cidr_table_list=None, vpc_id=None, vpc_name=None):
        # The ID of the connection between two network instances.
        self.attachment_id = attachment_id  # type: str
        # The name of the connection between two network instances.
        self.attachment_name = attachment_name  # type: str
        # An array consisting of the CIDR blocks that are protected by the VPC firewall.
        self.defend_cidr_list = defend_cidr_list  # type: list[str]
        # The Elastic Network Interfaces (ENIs).
        self.eni_list = eni_list  # type: list[DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList]
        # The ID of the specified vSwitch when the routing mode is manual.
        self.manual_vswitch_id = manual_vswitch_id  # type: str
        # The ID of the VPC for which the VPC firewall is created.
        self.network_instance_id = network_instance_id  # type: str
        # The name of the network instance.
        self.network_instance_name = network_instance_name  # type: str
        # The type of the network instance. The value is fixed as **VPC**.
        self.network_instance_type = network_instance_type  # type: str
        # The UID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id  # type: str
        # The ID of the region in which the VPC resides.
        self.region_no = region_no  # type: str
        # The routing mode. Valid values:
        # 
        # *   auto: automatic mode
        # *   manual: manual mode
        self.route_mode = route_mode  # type: str
        # Indicates whether the manual routing mode is supported. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.support_manual_mode = support_manual_mode  # type: str
        # The instance ID of the CEN transit router.
        self.transit_router_id = transit_router_id  # type: str
        # The edition of the CEN transit router. Valid values:
        # 
        # *   **Basic**: Basic Edition
        # *   **Enterprise**: Enterprise Edition
        self.transit_router_type = transit_router_type  # type: str
        # An array that consists of the CIDR blocks of the VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list  # type: list[DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableList]
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The name of the VPC.
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.eni_list:
            for k in self.eni_list:
                if k:
                    k.validate()
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallCenDetailResponseBodyLocalVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.defend_cidr_list is not None:
            result['DefendCidrList'] = self.defend_cidr_list
        result['EniList'] = []
        if self.eni_list is not None:
            for k in self.eni_list:
                result['EniList'].append(k.to_map() if k else None)
        if self.manual_vswitch_id is not None:
            result['ManualVSwitchId'] = self.manual_vswitch_id
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name
        if self.network_instance_type is not None:
            result['NetworkInstanceType'] = self.network_instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.support_manual_mode is not None:
            result['SupportManualMode'] = self.support_manual_mode
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('DefendCidrList') is not None:
            self.defend_cidr_list = m.get('DefendCidrList')
        self.eni_list = []
        if m.get('EniList') is not None:
            for k in m.get('EniList'):
                temp_model = DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList()
                self.eni_list.append(temp_model.from_map(k))
        if m.get('ManualVSwitchId') is not None:
            self.manual_vswitch_id = m.get('ManualVSwitchId')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')
        if m.get('NetworkInstanceType') is not None:
            self.network_instance_type = m.get('NetworkInstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('SupportManualMode') is not None:
            self.support_manual_mode = m.get('SupportManualMode')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallCenDetailResponseBody(TeaModel):
    def __init__(self, connect_type=None, firewall_switch_status=None, firewall_vpc=None, local_vpc=None,
                 request_id=None, vpc_firewall_id=None, vpc_firewall_name=None):
        # The connection type of the VPC firewall. The value is fixed as **cen**, which indicates CEN instances.
        self.connect_type = connect_type  # type: str
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: enabled
        # *   **closed**: disabled
        # *   **notconfigured**: not configured
        self.firewall_switch_status = firewall_switch_status  # type: str
        # The VPC that is automatically created for the firewall.
        self.firewall_vpc = firewall_vpc  # type: DescribeVpcFirewallCenDetailResponseBodyFirewallVpc
        # The details about the VPC.
        self.local_vpc = local_vpc  # type: DescribeVpcFirewallCenDetailResponseBodyLocalVpc
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id  # type: str
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str

    def validate(self):
        if self.firewall_vpc:
            self.firewall_vpc.validate()
        if self.local_vpc:
            self.local_vpc.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallCenDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.firewall_vpc is not None:
            result['FirewallVpc'] = self.firewall_vpc.to_map()
        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('FirewallVpc') is not None:
            temp_model = DescribeVpcFirewallCenDetailResponseBodyFirewallVpc()
            self.firewall_vpc = temp_model.from_map(m['FirewallVpc'])
        if m.get('LocalVpc') is not None:
            temp_model = DescribeVpcFirewallCenDetailResponseBodyLocalVpc()
            self.local_vpc = temp_model.from_map(m['LocalVpc'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeVpcFirewallCenDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVpcFirewallCenDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallCenDetailResponse, self).to_map()
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
            temp_model = DescribeVpcFirewallCenDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallCenListRequest(TeaModel):
    def __init__(self, cen_id=None, current_page=None, firewall_switch_status=None, lang=None, member_uid=None,
                 network_instance_id=None, owner_id=None, page_size=None, region_no=None, route_mode=None, transit_router_type=None,
                 vpc_firewall_id=None, vpc_firewall_name=None):
        # The ID of the CEN instance.
        self.cen_id = cen_id  # type: str
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.current_page = current_page  # type: str
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        # *   **configured**: The VPC firewall is configured but is not enabled.
        # 
        # > If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account. The member is also an Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The ID of the network instance.
        self.network_instance_id = network_instance_id  # type: str
        self.owner_id = owner_id  # type: str
        # The number of entries to return on each page.
        # 
        # Default value: 10. Maximum value: 50.
        self.page_size = page_size  # type: str
        # The region ID of the VPC.
        # 
        # > For more information about the regions, see [Supported regions](~~195657~~).
        self.region_no = region_no  # type: str
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **auto**: automatic mode
        # *   **manual**: manual mode
        # 
        # > If you do not specify this parameter, VPC firewalls in all routing modes are queried.
        self.route_mode = route_mode  # type: str
        # The type of the transit router. Valid values:
        # 
        # *   **Basic**: Basic Edition transit router
        # *   **Enterprise**: Enterprise Edition transit router
        self.transit_router_type = transit_router_type  # type: str
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id  # type: str
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallCenListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewallsIpsConfig(TeaModel):
    def __init__(self, basic_rules=None, enable_all_patch=None, run_mode=None):
        # Indicates whether basic protection is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules  # type: int
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch  # type: int
        # The mode of the IPS. Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallCenListResponseBodyVpcFirewallsIpsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(self, destination_cidr=None, next_hop_instance_id=None):
        # The destination CIDR block of the VPC.
        self.destination_cidr = destination_cidr  # type: str
        # The instance ID of the next hop for the VPC.
        self.next_hop_instance_id = next_hop_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList(TeaModel):
    def __init__(self, route_entry_list=None, route_table_id=None):
        # An array that consists of the route entries for the VPC.
        self.route_entry_list = route_entry_list  # type: list[DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList]
        # The route table ID of the VPC.
        self.route_table_id = route_table_id  # type: str

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpc(TeaModel):
    def __init__(self, authorization_status=None, defend_cidr_list=None, manual_vswitch_id=None,
                 network_instance_id=None, network_instance_name=None, network_instance_type=None, owner_id=None, region_no=None,
                 route_mode=None, support_manual_mode=None, transit_router_type=None, vpc_cidr_table_list=None, vpc_id=None,
                 vpc_name=None):
        # Indicates whether the VPC is granted the required permissions. The value is fixed as **authorized**, which indicates that the VPC is granted the required permissions.
        self.authorization_status = authorization_status  # type: str
        # An array consisting of the CIDR blocks that are protected by the VPC firewall.
        self.defend_cidr_list = defend_cidr_list  # type: list[str]
        # The ID of the specified vSwitch when the routing mode is manual.
        self.manual_vswitch_id = manual_vswitch_id  # type: str
        # The ID of the network instance.
        self.network_instance_id = network_instance_id  # type: str
        # The name of the network instance.
        self.network_instance_name = network_instance_name  # type: str
        # The type of the network instance. Valid values:
        # 
        # *   **VPC**\
        # *   **VBR**\
        # *   **CCN**\
        self.network_instance_type = network_instance_type  # type: str
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id  # type: long
        # The region ID of the VPC.
        self.region_no = region_no  # type: str
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **auto**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode  # type: str
        # Indicates whether the manual routing mode is supported. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.support_manual_mode = support_manual_mode  # type: str
        # The edition of the CEN transit router. Valid values:
        # 
        # *   **Basic**: Basic Edition transit router
        # *   **Enterprise**: Enterprise Edition transit router
        self.transit_router_type = transit_router_type  # type: str
        # An array that consists of the CIDR blocks of the VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list  # type: list[DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList]
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str
        # The name of the VPC.
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_status is not None:
            result['AuthorizationStatus'] = self.authorization_status
        if self.defend_cidr_list is not None:
            result['DefendCidrList'] = self.defend_cidr_list
        if self.manual_vswitch_id is not None:
            result['ManualVSwitchId'] = self.manual_vswitch_id
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id
        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name
        if self.network_instance_type is not None:
            result['NetworkInstanceType'] = self.network_instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode
        if self.support_manual_mode is not None:
            result['SupportManualMode'] = self.support_manual_mode
        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationStatus') is not None:
            self.authorization_status = m.get('AuthorizationStatus')
        if m.get('DefendCidrList') is not None:
            self.defend_cidr_list = m.get('DefendCidrList')
        if m.get('ManualVSwitchId') is not None:
            self.manual_vswitch_id = m.get('ManualVSwitchId')
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')
        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')
        if m.get('NetworkInstanceType') is not None:
            self.network_instance_type = m.get('NetworkInstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')
        if m.get('SupportManualMode') is not None:
            self.support_manual_mode = m.get('SupportManualMode')
        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallCenListResponseBodyVpcFirewalls(TeaModel):
    def __init__(self, cen_id=None, cen_name=None, connect_type=None, firewall_switch_status=None, ips_config=None,
                 local_vpc=None, member_uid=None, precheck_status=None, region_status=None, result_code=None,
                 vpc_firewall_id=None, vpc_firewall_name=None):
        # The ID of the CEN instance.
        self.cen_id = cen_id  # type: str
        # The name of the CEN instance.
        self.cen_name = cen_name  # type: str
        # The connection type of the VPC firewall. The value is fixed as cen, which indicates a CEN instance.
        self.connect_type = connect_type  # type: str
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        self.firewall_switch_status = firewall_switch_status  # type: str
        # The information about the intrusion prevention system (IPS) configuration.
        self.ips_config = ips_config  # type: DescribeVpcFirewallCenListResponseBodyVpcFirewallsIpsConfig
        # The details about the VPC.
        self.local_vpc = local_vpc  # type: DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpc
        # The UID of the member that is manged by your Alibaba Cloud account. The member is also an Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # Indicates whether the VPC firewall can be automatically enabled to protect VPC traffic based on route learning. Valid values:
        # 
        # *   **passed**: The VPC firewall can be automatically enabled.
        # *   **failed**: The VPC firewall cannot be automatically enabled.
        # *   **unknown**: The VPC firewall is in an unknown state.
        self.precheck_status = precheck_status  # type: str
        # Indicates whether you can create a VPC firewall in a specified region. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status  # type: str
        # The result code of the operation that creates the VPC firewall. Valid values:
        # 
        # *   **Unauthorized**: Cloud Firewall is not authorized to access the VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **RegionDisable**: VPC Firewall is not supported in the region of the VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **OpsDisable**: You are not allowed to create the VPC firewall.
        # *   **VbrNotSupport**: The VPC firewall cannot be created for a VBR that is attached to the CEN instance.
        # *   Empty string: You can create a VPC firewall for the network instance.
        self.result_code = result_code  # type: str
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id  # type: str
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str

    def validate(self):
        if self.ips_config:
            self.ips_config.validate()
        if self.local_vpc:
            self.local_vpc.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallCenListResponseBodyVpcFirewalls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_name is not None:
            result['CenName'] = self.cen_name
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.ips_config is not None:
            result['IpsConfig'] = self.ips_config.to_map()
        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status
        if self.region_status is not None:
            result['RegionStatus'] = self.region_status
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenName') is not None:
            self.cen_name = m.get('CenName')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('IpsConfig') is not None:
            temp_model = DescribeVpcFirewallCenListResponseBodyVpcFirewallsIpsConfig()
            self.ips_config = temp_model.from_map(m['IpsConfig'])
        if m.get('LocalVpc') is not None:
            temp_model = DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpc()
            self.local_vpc = temp_model.from_map(m['LocalVpc'])
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PrecheckStatus') is not None:
            self.precheck_status = m.get('PrecheckStatus')
        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeVpcFirewallCenListResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, vpc_firewalls=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of VPC firewalls.
        self.total_count = total_count  # type: int
        # An array that consists of the details about the VPC firewall.
        self.vpc_firewalls = vpc_firewalls  # type: list[DescribeVpcFirewallCenListResponseBodyVpcFirewalls]

    def validate(self):
        if self.vpc_firewalls:
            for k in self.vpc_firewalls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallCenListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VpcFirewalls'] = []
        if self.vpc_firewalls is not None:
            for k in self.vpc_firewalls:
                result['VpcFirewalls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vpc_firewalls = []
        if m.get('VpcFirewalls') is not None:
            for k in m.get('VpcFirewalls'):
                temp_model = DescribeVpcFirewallCenListResponseBodyVpcFirewalls()
                self.vpc_firewalls.append(temp_model.from_map(k))
        return self


class DescribeVpcFirewallCenListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVpcFirewallCenListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallCenListResponse, self).to_map()
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
            temp_model = DescribeVpcFirewallCenListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(self, acl_action=None, acl_uuid=None, current_page=None, description=None, destination=None,
                 lang=None, member_uid=None, page_size=None, proto=None, release=None, repeat_type=None, source=None,
                 vpc_firewall_id=None):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: blocks the traffic.
        # *   **log**: monitors the traffic.
        # 
        # > If you do not specify this parameter, access control policies are queried based on all actions.
        self.acl_action = acl_action  # type: str
        # The unique ID of the access control policy.
        self.acl_uuid = acl_uuid  # type: str
        # The number of the page to return.
        self.current_page = current_page  # type: str
        # The description of the access control policy. Fuzzy match is supported.
        self.description = description  # type: str
        # The destination address in the access control policy. Fuzzy match is supported.
        # 
        # > The value of this parameter can be a CIDR block or an address book name.
        self.destination = destination  # type: str
        # The language of the content within the request and response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The number of entries to return on each page.
        # 
        # Maximum value: 50.
        self.page_size = page_size  # type: str
        # The protocol type in the access control policy. Valid values:
        # 
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # *   **ANY**: all protocol types
        # 
        # > If you do not specify this parameter, access control policies of all protocol types are queried.
        self.proto = proto  # type: str
        # Specifies whether the access control policy is enabled. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # *   **true**: The access control policy is enabled.
        # *   **false**: The access control policy is disabled.
        self.release = release  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy. Fuzzy match is supported.
        # 
        # > The value of this parameter can be a CIDR block or an address book name.
        self.source = source  # type: str
        # The instance ID of the VPC firewall. Valid values:
        # 
        # *   If the VPC firewall protects the traffic between two VPCs that are connected by using a CEN instance, the value of this parameter must be the ID of the CEN instance.
        # *   If the VPC firewall protects the traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter must be the instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallAclGroupList](~~159760~~) operation to query the ID.
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.description is not None:
            result['Description'] = self.description
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallControlPolicyResponseBodyPolicys(TeaModel):
    def __init__(self, acl_action=None, acl_uuid=None, application_id=None, application_name=None,
                 application_name_list=None, create_time=None, description=None, dest_port=None, dest_port_group=None,
                 dest_port_group_ports=None, dest_port_type=None, destination=None, destination_group_cidrs=None,
                 destination_group_type=None, destination_type=None, end_time=None, hit_last_time=None, hit_times=None, member_uid=None,
                 modify_time=None, order=None, proto=None, release=None, repeat_days=None, repeat_end_time=None,
                 repeat_start_time=None, repeat_type=None, source=None, source_group_cidrs=None, source_group_type=None,
                 source_type=None, spread_cnt=None, start_time=None):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: blocks the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action  # type: str
        # The unique ID of the access control policy.
        self.acl_uuid = acl_uuid  # type: str
        # The application ID in the access control policy.
        self.application_id = application_id  # type: str
        # The application type in the access control policy. Valid values:
        # 
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **MySQL**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **RDP**\
        # *   **VNC**\
        # *   **SSH**\
        # *   **Redis**\
        # *   **MQTT**\
        # *   **MongoDB**\
        # *   **Memcache**\
        # *   **SSL**\
        # *   **ANY**: all application types
        self.application_name = application_name  # type: str
        self.application_name_list = application_name_list  # type: list[str]
        self.create_time = create_time  # type: long
        # The description of the access control policy.
        self.description = description  # type: str
        # The destination port in the access control policy.
        self.dest_port = dest_port  # type: str
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group  # type: str
        # An array that consists of the ports in the destination port address book of the access control policy.
        self.dest_port_group_ports = dest_port_group_ports  # type: list[str]
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type  # type: str
        # The destination address in the access control policy. Valid values:
        # 
        # *   If **DestinationType** is set to `net`, the value of this parameter is a CIDR block.
        # *   If **DestinationType** is set to `domain`, the value of this parameter is a domain name.
        # *   If **DestinationType** is set to `group`, the value of this parameter is an address book name.
        self.destination = destination  # type: str
        # An array that consists of the CIDR blocks in the destination address book of the access control policy.
        self.destination_group_cidrs = destination_group_cidrs  # type: list[str]
        # The type of the destination address book in the access control policy. Valid values:
        # 
        # *   **ip**: an address book that includes one or more CIDR blocks
        # *   **domain**: an address book that includes one or more domain names
        self.destination_group_type = destination_group_type  # type: str
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        self.destination_type = destination_type  # type: str
        self.end_time = end_time  # type: long
        self.hit_last_time = hit_last_time  # type: long
        # The number of hits for the access control policy.
        self.hit_times = hit_times  # type: long
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        self.modify_time = modify_time  # type: long
        # The priority of the access control policy.
        # 
        # The priority value starts from 1. A smaller priority value indicates a higher priority.
        self.order = order  # type: int
        # The protocol type in the access control policy. Valid values:
        # 
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # *   **ANY**: all protocol types
        self.proto = proto  # type: str
        # Indicates whether the access control policy is enabled. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # *   **true**: The access control policy is enabled.
        # *   **false**: The access control policy is disabled.
        self.release = release  # type: str
        self.repeat_days = repeat_days  # type: list[long]
        self.repeat_end_time = repeat_end_time  # type: str
        self.repeat_start_time = repeat_start_time  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy. Valid values:
        # 
        # *   If **SourceType** is set to `net`, the value of this parameter is a CIDR block.
        # *   If **SourceType** is set to `group`, the value of this parameter is an address book name.
        self.source = source  # type: str
        # An array that consists of the CIDR blocks in the source address book of the access control policy.
        self.source_group_cidrs = source_group_cidrs  # type: list[str]
        # The type of the source address in the access control policy. The value is fixed as **ip**. The value indicates an address book that includes one or more CIDR blocks.
        self.source_group_type = source_group_type  # type: str
        # The type of the source address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        self.source_type = source_type  # type: str
        self.spread_cnt = spread_cnt  # type: long
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallControlPolicyResponseBodyPolicys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.dest_port_group_ports is not None:
            result['DestPortGroupPorts'] = self.dest_port_group_ports
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_group_cidrs is not None:
            result['DestinationGroupCidrs'] = self.destination_group_cidrs
        if self.destination_group_type is not None:
            result['DestinationGroupType'] = self.destination_group_type
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hit_last_time is not None:
            result['HitLastTime'] = self.hit_last_time
        if self.hit_times is not None:
            result['HitTimes'] = self.hit_times
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.order is not None:
            result['Order'] = self.order
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.repeat_end_time is not None:
            result['RepeatEndTime'] = self.repeat_end_time
        if self.repeat_start_time is not None:
            result['RepeatStartTime'] = self.repeat_start_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_group_cidrs is not None:
            result['SourceGroupCidrs'] = self.source_group_cidrs
        if self.source_group_type is not None:
            result['SourceGroupType'] = self.source_group_type
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.spread_cnt is not None:
            result['SpreadCnt'] = self.spread_cnt
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('DestPortGroupPorts') is not None:
            self.dest_port_group_ports = m.get('DestPortGroupPorts')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationGroupCidrs') is not None:
            self.destination_group_cidrs = m.get('DestinationGroupCidrs')
        if m.get('DestinationGroupType') is not None:
            self.destination_group_type = m.get('DestinationGroupType')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HitLastTime') is not None:
            self.hit_last_time = m.get('HitLastTime')
        if m.get('HitTimes') is not None:
            self.hit_times = m.get('HitTimes')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RepeatEndTime') is not None:
            self.repeat_end_time = m.get('RepeatEndTime')
        if m.get('RepeatStartTime') is not None:
            self.repeat_start_time = m.get('RepeatStartTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceGroupCidrs') is not None:
            self.source_group_cidrs = m.get('SourceGroupCidrs')
        if m.get('SourceGroupType') is not None:
            self.source_group_type = m.get('SourceGroupType')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SpreadCnt') is not None:
            self.spread_cnt = m.get('SpreadCnt')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(self, policys=None, request_id=None, total_count=None):
        # The information about the access control policies.
        self.policys = policys  # type: list[DescribeVpcFirewallControlPolicyResponseBodyPolicys]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of access control policies returned.
        self.total_count = total_count  # type: str

    def validate(self):
        if self.policys:
            for k in self.policys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallControlPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policys'] = []
        if self.policys is not None:
            for k in self.policys:
                result['Policys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policys = []
        if m.get('Policys') is not None:
            for k in m.get('Policys'):
                temp_model = DescribeVpcFirewallControlPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVpcFirewallControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallControlPolicyResponse, self).to_map()
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
            temp_model = DescribeVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallDefaultIPSConfigRequest(TeaModel):
    def __init__(self, member_uid=None, vpc_firewall_id=None):
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The instance ID of the VPC firewall. Valid values:
        # 
        # *   If the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. You can call the [DescribeVpcFirewallCenList](~~345777~~) operation to query the IDs of CEN instances.
        # *   If the VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter is the instance ID of the VPC firewall. You can call the [DescribeVpcFirewallList](~~342932~~) operation to query the instance IDs of VPC firewalls.
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallDefaultIPSConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallDefaultIPSConfigResponseBody(TeaModel):
    def __init__(self, basic_rules=None, enable_all_patch=None, request_id=None, run_mode=None):
        # Indicates whether basic policies are enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules  # type: int
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The mode of the intrusion prevention system (IPS). Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallDefaultIPSConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeVpcFirewallDefaultIPSConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVpcFirewallDefaultIPSConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallDefaultIPSConfigResponse, self).to_map()
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
            temp_model = DescribeVpcFirewallDefaultIPSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallDetailRequest(TeaModel):
    def __init__(self, lang=None, local_vpc_id=None, peer_vpc_id=None, vpc_firewall_id=None):
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The ID of the local VPC.
        self.local_vpc_id = local_vpc_id  # type: str
        # The ID of the peer VPC.
        self.peer_vpc_id = peer_vpc_id  # type: str
        # The instance ID of the VPC firewall.
        # 
        # >  You can call the [DescribeVpcFirewallList](~~342932~~) operation to query the instance IDs of VPC firewalls.
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.local_vpc_id is not None:
            result['LocalVpcId'] = self.local_vpc_id
        if self.peer_vpc_id is not None:
            result['PeerVpcId'] = self.peer_vpc_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LocalVpcId') is not None:
            self.local_vpc_id = m.get('LocalVpcId')
        if m.get('PeerVpcId') is not None:
            self.peer_vpc_id = m.get('PeerVpcId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(self, destination_cidr=None, next_hop_instance_id=None):
        # The destination CIDR block of the local VPC.
        self.destination_cidr = destination_cidr  # type: str
        # The instance ID of the next hop for the local VPC.
        self.next_hop_instance_id = next_hop_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableList(TeaModel):
    def __init__(self, route_entry_list=None, route_table_id=None):
        # The route entries of the local VPC.
        self.route_entry_list = route_entry_list  # type: list[DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList]
        # The ID of the route table for the local VPC.
        self.route_table_id = route_table_id  # type: str

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallDetailResponseBodyLocalVpc(TeaModel):
    def __init__(self, eni_id=None, eni_private_ip_address=None, region_no=None, router_interface_id=None,
                 vpc_cidr_table_list=None, vpc_id=None, vpc_name=None):
        # The ID of the ENI for the local VPC.
        self.eni_id = eni_id  # type: str
        # The private IP address of the elastic network interface (ENI) for the local VPC.
        self.eni_private_ip_address = eni_private_ip_address  # type: str
        # The region ID of the local VPC.
        self.region_no = region_no  # type: str
        # The router interface ID of the local VPC.
        self.router_interface_id = router_interface_id  # type: str
        # The CIDR blocks of the local VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list  # type: list[DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableList]
        # The ID of the local VPC.
        self.vpc_id = vpc_id  # type: str
        # The name of the local VPC.
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallDetailResponseBodyLocalVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.eni_private_ip_address is not None:
            result['EniPrivateIpAddress'] = self.eni_private_ip_address
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('EniPrivateIpAddress') is not None:
            self.eni_private_ip_address = m.get('EniPrivateIpAddress')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(self, destination_cidr=None, next_hop_instance_id=None):
        # The destination CIDR block of the peer VPC.
        self.destination_cidr = destination_cidr  # type: str
        # The instance ID of the next hop for the peer VPC.
        self.next_hop_instance_id = next_hop_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableListRouteEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableList(TeaModel):
    def __init__(self, route_entry_list=None, route_table_id=None):
        # The route entries of the peer VPC.
        self.route_entry_list = route_entry_list  # type: list[DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableListRouteEntryList]
        # The ID of the route table for the peer VPC.
        self.route_table_id = route_table_id  # type: str

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallDetailResponseBodyPeerVpc(TeaModel):
    def __init__(self, eni_id=None, eni_private_ip_address=None, region_no=None, router_interface_id=None,
                 vpc_cidr_table_list=None, vpc_id=None, vpc_name=None):
        # The ID of the ENI for the peer VPC.
        self.eni_id = eni_id  # type: str
        # The private IP address of the ENI for the peer VPC.
        self.eni_private_ip_address = eni_private_ip_address  # type: str
        # The region ID of the peer VPC.
        self.region_no = region_no  # type: str
        # The router interface ID of the peer VPC.
        self.router_interface_id = router_interface_id  # type: str
        # The CIDR blocks of the peer VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list  # type: list[DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableList]
        # The ID of the peer VPC.
        self.vpc_id = vpc_id  # type: str
        # The name of the peer VPC.
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallDetailResponseBodyPeerVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.eni_private_ip_address is not None:
            result['EniPrivateIpAddress'] = self.eni_private_ip_address
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('EniPrivateIpAddress') is not None:
            self.eni_private_ip_address = m.get('EniPrivateIpAddress')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallDetailResponseBody(TeaModel):
    def __init__(self, bandwidth=None, connect_type=None, firewall_switch_status=None, local_vpc=None,
                 member_uid=None, peer_vpc=None, request_id=None, vpc_firewall_id=None, vpc_firewall_name=None):
        # The bandwidth of the Express Connect circuit. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: int
        # The connection type of the VPC firewall. The value is fixed as **expressconnect**, which indicates Express Connect circuits.
        self.connect_type = connect_type  # type: str
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        # *   **configured**: The VPC firewall is configured.
        self.firewall_switch_status = firewall_switch_status  # type: str
        # The details about the local VPC.
        self.local_vpc = local_vpc  # type: DescribeVpcFirewallDetailResponseBodyLocalVpc
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The details about the peer VPC.
        self.peer_vpc = peer_vpc  # type: DescribeVpcFirewallDetailResponseBodyPeerVpc
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id  # type: str
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str

    def validate(self):
        if self.local_vpc:
            self.local_vpc.validate()
        if self.peer_vpc:
            self.peer_vpc.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.peer_vpc is not None:
            result['PeerVpc'] = self.peer_vpc.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('LocalVpc') is not None:
            temp_model = DescribeVpcFirewallDetailResponseBodyLocalVpc()
            self.local_vpc = temp_model.from_map(m['LocalVpc'])
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PeerVpc') is not None:
            temp_model = DescribeVpcFirewallDetailResponseBodyPeerVpc()
            self.peer_vpc = temp_model.from_map(m['PeerVpc'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeVpcFirewallDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVpcFirewallDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallDetailResponse, self).to_map()
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
            temp_model = DescribeVpcFirewallDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallListRequest(TeaModel):
    def __init__(self, connect_sub_type=None, current_page=None, firewall_switch_status=None, lang=None,
                 member_uid=None, page_size=None, peer_uid=None, region_no=None, vpc_firewall_id=None, vpc_firewall_name=None,
                 vpc_id=None):
        # The sub-type of the connection. Valid values:
        # 
        # *   **vpc2vpc**: Express Connect connection
        # *   **vpcpeer**: peer connection
        self.connect_sub_type = connect_sub_type  # type: str
        # The number of the page to return.
        # 
        # Pages start from page **1**. Default value: **1**.
        self.current_page = current_page  # type: str
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        # *   **configured**: The VPC firewall is configured.
        # 
        # > If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The number of entries to return on each page.
        # 
        # Default value: **10**.**** Maximum value: **50**.
        self.page_size = page_size  # type: str
        # The UID of the Alibaba Cloud account to which the peer VPC belongs.
        self.peer_uid = peer_uid  # type: str
        # The region ID of the VPC.
        # 
        # > For more information about the regions, see [Supported regions](~~195657~~).
        self.region_no = region_no  # type: str
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id  # type: str
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_sub_type is not None:
            result['ConnectSubType'] = self.connect_sub_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.peer_uid is not None:
            result['PeerUid'] = self.peer_uid
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectSubType') is not None:
            self.connect_sub_type = m.get('ConnectSubType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PeerUid') is not None:
            self.peer_uid = m.get('PeerUid')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig(TeaModel):
    def __init__(self, basic_rules=None, enable_all_patch=None, run_mode=None):
        # Indicates whether basic protection is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules  # type: int
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch  # type: int
        # The mode of the IPS. Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(self, destination_cidr=None, next_hop_instance_id=None):
        # The destination CIDR block of the local VPC.
        self.destination_cidr = destination_cidr  # type: str
        # The instance ID of the next hop for the local VPC.
        self.next_hop_instance_id = next_hop_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList(TeaModel):
    def __init__(self, route_entry_list=None, route_table_id=None):
        # An array that consists of the route entries of the local VPC.
        self.route_entry_list = route_entry_list  # type: list[DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList]
        # The ID of the route table for the local VPC.
        self.route_table_id = route_table_id  # type: str

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc(TeaModel):
    def __init__(self, authorization_status=None, owner_id=None, region_no=None, vpc_cidr_table_list=None,
                 vpc_id=None, vpc_name=None):
        # Indicates whether Cloud Firewall is authorized to access the local VPC. The value is fixed as authorized, which indicates that Cloud Firewall is authorized to access the local VPC.
        self.authorization_status = authorization_status  # type: str
        # The UID of the Alibaba Cloud account to which the local VPC belongs.
        self.owner_id = owner_id  # type: long
        # The region ID of the local VPC.
        self.region_no = region_no  # type: str
        # An array that consists of the CIDR blocks of the local VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list  # type: list[DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList]
        # The ID of the local VPC.
        self.vpc_id = vpc_id  # type: str
        # The name of the local VPC.
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_status is not None:
            result['AuthorizationStatus'] = self.authorization_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationStatus') is not None:
            self.authorization_status = m.get('AuthorizationStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableListRouteEntryList(TeaModel):
    def __init__(self, destination_cidr=None, next_hop_instance_id=None):
        # The destination CIDR block of the peer VPC.
        self.destination_cidr = destination_cidr  # type: str
        # The instance ID of the next hop for the peer VPC.
        self.next_hop_instance_id = next_hop_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableListRouteEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableList(TeaModel):
    def __init__(self, route_entry_list=None, route_table_id=None):
        # An array that consists of the route entries of the peer VPC.
        self.route_entry_list = route_entry_list  # type: list[DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableListRouteEntryList]
        # The ID of the route table for the peer VPC.
        self.route_table_id = route_table_id  # type: str

    def validate(self):
        if self.route_entry_list:
            for k in self.route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k in self.route_entry_list:
                result['RouteEntryList'].append(k.to_map() if k else None)
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k in m.get('RouteEntryList'):
                temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k))
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc(TeaModel):
    def __init__(self, authorization_status=None, owner_id=None, region_no=None, vpc_cidr_table_list=None,
                 vpc_id=None, vpc_name=None):
        # Indicates whether Cloud Firewall is authorized to access the peer VPC. The value is fixed as **authorized**, which indicates that Cloud Firewall is authorized to access the peer VPC.
        self.authorization_status = authorization_status  # type: str
        # The UID of the Alibaba Cloud account to which the peer VPC belongs.
        self.owner_id = owner_id  # type: long
        # The region ID of the peer VPC.
        self.region_no = region_no  # type: str
        # An array that consists of the CIDR blocks of the peer VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list  # type: list[DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableList]
        # The ID of the peer VPC.
        self.vpc_id = vpc_id  # type: str
        # The name of the peer VPC.
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        if self.vpc_cidr_table_list:
            for k in self.vpc_cidr_table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_status is not None:
            result['AuthorizationStatus'] = self.authorization_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizationStatus') is not None:
            self.authorization_status = m.get('AuthorizationStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k in m.get('VpcCidrTableList'):
                temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcFirewallListResponseBodyVpcFirewalls(TeaModel):
    def __init__(self, bandwidth=None, connect_sub_type=None, connect_type=None, firewall_switch_status=None,
                 ips_config=None, local_vpc=None, member_uid=None, peer_vpc=None, region_status=None, result_code=None,
                 vpc_firewall_id=None, vpc_firewall_name=None):
        # The bandwidth of the Express Connect circuit. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: int
        # The sub-type of the connection. Valid values:
        # 
        # *   **vpc2vpc**: Express Connect connection
        # *   **vpcpeer**: peer connection
        self.connect_sub_type = connect_sub_type  # type: str
        # The connection type of the VPC firewall. The value is fixed as **expressconnect**, which indicates an Express Connect connection.
        self.connect_type = connect_type  # type: str
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        self.firewall_switch_status = firewall_switch_status  # type: str
        # The information about the intrusion prevention system (IPS) configuration.
        self.ips_config = ips_config  # type: DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig
        # The details about the local VPC.
        self.local_vpc = local_vpc  # type: DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The details about the peer VPC.
        self.peer_vpc = peer_vpc  # type: DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc
        # Indicates whether you can create a VPC firewall in a specified region. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status  # type: str
        # The result code of the operation that creates the VPC firewall. Valid values:
        # 
        # *   **Unauthorized**: Cloud Firewall is not authorized to access a VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **RegionDisable**: VPC Firewall is not supported in the region of a VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **Empty string**: You can create a VPC firewall for the network instance.
        self.result_code = result_code  # type: str
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id  # type: str
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str

    def validate(self):
        if self.ips_config:
            self.ips_config.validate()
        if self.local_vpc:
            self.local_vpc.validate()
        if self.peer_vpc:
            self.peer_vpc.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallListResponseBodyVpcFirewalls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connect_sub_type is not None:
            result['ConnectSubType'] = self.connect_sub_type
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status
        if self.ips_config is not None:
            result['IpsConfig'] = self.ips_config.to_map()
        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.peer_vpc is not None:
            result['PeerVpc'] = self.peer_vpc.to_map()
        if self.region_status is not None:
            result['RegionStatus'] = self.region_status
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectSubType') is not None:
            self.connect_sub_type = m.get('ConnectSubType')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')
        if m.get('IpsConfig') is not None:
            temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig()
            self.ips_config = temp_model.from_map(m['IpsConfig'])
        if m.get('LocalVpc') is not None:
            temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc()
            self.local_vpc = temp_model.from_map(m['LocalVpc'])
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PeerVpc') is not None:
            temp_model = DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc()
            self.peer_vpc = temp_model.from_map(m['PeerVpc'])
        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class DescribeVpcFirewallListResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, vpc_firewalls=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of VPC firewalls.
        self.total_count = total_count  # type: int
        # An array that consists of the details about the VPC firewall.
        self.vpc_firewalls = vpc_firewalls  # type: list[DescribeVpcFirewallListResponseBodyVpcFirewalls]

    def validate(self):
        if self.vpc_firewalls:
            for k in self.vpc_firewalls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VpcFirewalls'] = []
        if self.vpc_firewalls is not None:
            for k in self.vpc_firewalls:
                result['VpcFirewalls'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vpc_firewalls = []
        if m.get('VpcFirewalls') is not None:
            for k in m.get('VpcFirewalls'):
                temp_model = DescribeVpcFirewallListResponseBodyVpcFirewalls()
                self.vpc_firewalls.append(temp_model.from_map(k))
        return self


class DescribeVpcFirewallListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVpcFirewallListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallListResponse, self).to_map()
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
            temp_model = DescribeVpcFirewallListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcFirewallPolicyPriorUsedRequest(TeaModel):
    def __init__(self, lang=None, vpc_firewall_id=None):
        # The natural language of the request and response. 
        # 
        # Valid values:
        # 
        # - **zh**: Chinese (default)
        # - **en**: English
        self.lang = lang  # type: str
        # The ID of the policy group to which the access control policy belongs. You can call the DescribeVpcFirewallAclGroupList operation to query the ID.  
        # 
        # Valid values:
        # 
        # - If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance.  
        # 
        # Example: cen-ervw0g12b5jbw****\
        # - If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the ID of the VPC firewall instance.  
        # 
        # Example: vfw-a42bbb7b887148c9****\
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallPolicyPriorUsedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class DescribeVpcFirewallPolicyPriorUsedResponseBody(TeaModel):
    def __init__(self, end=None, request_id=None, start=None):
        # The lowest priority for the access control policy.
        self.end = end  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The highest priority for the access control policy.
        self.start = start  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcFirewallPolicyPriorUsedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class DescribeVpcFirewallPolicyPriorUsedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVpcFirewallPolicyPriorUsedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVpcFirewallPolicyPriorUsedResponse, self).to_map()
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
            temp_model = DescribeVpcFirewallPolicyPriorUsedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulnerabilityProtectedListRequest(TeaModel):
    def __init__(self, attack_type=None, buy_version=None, current_page=None, end_time=None, lang=None,
                 member_uid=None, order=None, page_size=None, sort_key=None, source_ip=None, start_time=None, user_type=None,
                 vuln_cve_name=None, vuln_level=None, vuln_resource=None, vuln_status=None, vuln_type=None):
        # The attack type of the intrusion event. Valid values:
        # 
        # *   **1**: suspicious connection
        # *   **2**: command execution
        # *   **3**: brute-force attack
        # *   **4**: scanning
        # *   **5**: others
        # *   **6**: information leakage
        # *   **7**: DoS attack
        # *   **8**: buffer overflow attack
        # *   **9**: web attack
        # *   **10**: webshell
        # *   **11**: computer worm
        # *   **12**: mining
        # *   **13**: reverse shell
        # 
        # > If you do not specify this parameter, the intrusion events of all attack types are queried.
        self.attack_type = attack_type  # type: str
        # The edition of Cloud Firewall.
        self.buy_version = buy_version  # type: long
        # The number of the page to return. Default value: 1.
        self.current_page = current_page  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The order in which you want to sort the queried information. Valid values:
        # 
        # *   **asc**: the ascending order.
        # *   **desc**: the descending order. This is the default value.
        self.order = order  # type: str
        # The number of entries to return on each page. Maximum value: 50.
        self.page_size = page_size  # type: str
        # The sorting basis. Set the value to **attackCnt**, which indicates the number of attacks.
        self.sort_key = sort_key  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: str
        # The type of the user. Set the value to **buy**, which indicates user of a paid edition of Cloud Firewall.
        self.user_type = user_type  # type: str
        # The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability.
        self.vuln_cve_name = vuln_cve_name  # type: str
        # The risk level of the vulnerability. Valid values:
        # 
        # *   **high**\
        # *   **medium**\
        # *   **low**\
        self.vuln_level = vuln_level  # type: str
        # The number of assets that are affected by the vulnerability.
        self.vuln_resource = vuln_resource  # type: str
        # The status of vulnerability protection. Valid values:
        # 
        # *   **partProtected**: partially protected
        # *   **protected**: protected
        # *   **unProtected**: unprotected
        self.vuln_status = vuln_status  # type: str
        # The type of the vulnerability. Valid values:
        # 
        # *   **App**: application vulnerability
        # *   **emg**: urgent vulnerability
        # *   **cms**: Web-CMS vulnerability
        self.vuln_type = vuln_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVulnerabilityProtectedListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.buy_version is not None:
            result['BuyVersion'] = self.buy_version
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.order is not None:
            result['Order'] = self.order
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.vuln_cve_name is not None:
            result['VulnCveName'] = self.vuln_cve_name
        if self.vuln_level is not None:
            result['VulnLevel'] = self.vuln_level
        if self.vuln_resource is not None:
            result['VulnResource'] = self.vuln_resource
        if self.vuln_status is not None:
            result['VulnStatus'] = self.vuln_status
        if self.vuln_type is not None:
            result['VulnType'] = self.vuln_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('BuyVersion') is not None:
            self.buy_version = m.get('BuyVersion')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('VulnCveName') is not None:
            self.vuln_cve_name = m.get('VulnCveName')
        if m.get('VulnLevel') is not None:
            self.vuln_level = m.get('VulnLevel')
        if m.get('VulnResource') is not None:
            self.vuln_resource = m.get('VulnResource')
        if m.get('VulnStatus') is not None:
            self.vuln_status = m.get('VulnStatus')
        if m.get('VulnType') is not None:
            self.vuln_type = m.get('VulnType')
        return self


class DescribeVulnerabilityProtectedListResponseBodyVulnListResourceList(TeaModel):
    def __init__(self, eip=None, internet_ip=None, intranet_ip=None, region_id=None, resource_id=None,
                 resource_name=None, resource_type=None, vuln_status=None):
        # The elastic IP address (EIP) that is associated with the instance.
        self.eip = eip  # type: str
        # The public IP address of the instance.
        self.internet_ip = internet_ip  # type: str
        # The private IP address of the instance.
        self.intranet_ip = intranet_ip  # type: str
        # The ID of the region in which Cloud Firewall is supported.
        # 
        # > For more information about the regions, see [Supported regions](~~195657~~).
        self.region_id = region_id  # type: str
        # The ID of the instance.
        self.resource_id = resource_id  # type: str
        # The name of the instance.
        self.resource_name = resource_name  # type: str
        # The type of the asset. Valid values:
        # 
        # *   **SLB**\
        # *   **EIP**\
        # *   **ECS**\
        self.resource_type = resource_type  # type: str
        # The status of vulnerability protection. Valid values:
        # 
        # *   **partProtected**: partially protected
        # *   **protected**: protected
        # *   **unProtected**: unprotected
        self.vuln_status = vuln_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVulnerabilityProtectedListResponseBodyVulnListResourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.vuln_status is not None:
            result['VulnStatus'] = self.vuln_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('VulnStatus') is not None:
            self.vuln_status = m.get('VulnStatus')
        return self


class DescribeVulnerabilityProtectedListResponseBodyVulnList(TeaModel):
    def __init__(self, attack_cnt=None, attack_type=None, basic_rule_ids=None, cve_id=None, first_time=None,
                 highlight_tag=None, last_time=None, member_uid=None, need_open_basic_rule=None, need_open_basic_rule_uuids=None,
                 need_open_run_mode=None, need_open_virtual_patche=None, need_open_virtual_patche_uuids=None, need_rule_class=None,
                 resource_cnt=None, resource_list=None, virtual_patche_ids=None, vuln_key=None, vuln_level=None, vuln_name=None,
                 vuln_status=None, vuln_type=None):
        # The number of vulnerabilities.
        self.attack_cnt = attack_cnt  # type: int
        # The attack type of the intrusion event. Valid values:
        # 
        # *   **1**: suspicious connection
        # *   **2**: command execution
        # *   **3**: brute-force attack
        # *   **4**: scanning
        # *   **5**: others
        # *   **6**: information leakage
        # *   **7**: DoS attack
        # *   **8**: buffer overflow attack
        # *   **9**: web attack
        # *   **10**: webshell
        # *   **11**: computer worm
        # *   **12**: mining
        # *   **13**: reverse shell
        # 
        # > If no attack type is specified, the intrusion events of all attack types are queried.
        self.attack_type = attack_type  # type: int
        # The IDs of associated basic protection policies.
        self.basic_rule_ids = basic_rule_ids  # type: str
        # The CVE IDs.
        self.cve_id = cve_id  # type: str
        # The time when the first attack was launched.
        self.first_time = first_time  # type: long
        # Indicates whether you need to pay special attention to the vulnerability. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.highlight_tag = highlight_tag  # type: int
        # The time when the last attack was launched.
        self.last_time = last_time  # type: long
        self.member_uid = member_uid  # type: str
        # The status of basic protection. Valid values:
        # 
        # *   **false**: enabled
        # *   **false**: disabled
        # 
        # > If the value of this parameter is true, you must configure the intrusion prevention feature when you enable protection.
        self.need_open_basic_rule = need_open_basic_rule  # type: bool
        # The UUIDs of the basic protection policies for which you want to set the Current Action parameter to Block.
        self.need_open_basic_rule_uuids = need_open_basic_rule_uuids  # type: str
        # Indicates whether the intrusion prevention feature needs to be configured when you enable protection. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.need_open_run_mode = need_open_run_mode  # type: bool
        # The status of virtual patching. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        # 
        # > If the value of this parameter is true, you must configure the intrusion prevention feature when you enable protection.
        self.need_open_virtual_patche = need_open_virtual_patche  # type: bool
        # The UUIDs of the virtual patching policies for which you want to set the Current Action parameter to Block.
        self.need_open_virtual_patche_uuids = need_open_virtual_patche_uuids  # type: str
        # The Rule Group that you want to specify. Valid values:
        # 
        # *   **1**: Loose (default)
        # *   **2**: Medium
        # *   **3**: Strict
        self.need_rule_class = need_rule_class  # type: int
        # The number of assets on which vulnerabilities are detected.
        self.resource_cnt = resource_cnt  # type: int
        # An array consisting of the assets on which vulnerabilities are detected.
        self.resource_list = resource_list  # type: list[DescribeVulnerabilityProtectedListResponseBodyVulnListResourceList]
        # The IDs of associated virtual patching policies.
        self.virtual_patche_ids = virtual_patche_ids  # type: str
        # The code of the vulnerability.
        self.vuln_key = vuln_key  # type: str
        # The risk level of the vulnerability. Valid values:
        # 
        # *   **high**\
        # *   **medium**\
        # *   **low**\
        self.vuln_level = vuln_level  # type: str
        # The name of the vulnerability.
        self.vuln_name = vuln_name  # type: str
        # The status of vulnerability protection. Valid values:
        # 
        # *   **partProtected**: partially protected
        # *   **protected**: protected
        # *   **unProtected**: unprotected
        self.vuln_status = vuln_status  # type: str
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: Windows vulnerability
        # *   **cms**: Web-CMS vulnerability
        # *   **App**: application vulnerability
        self.vuln_type = vuln_type  # type: str

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVulnerabilityProtectedListResponseBodyVulnList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_cnt is not None:
            result['AttackCnt'] = self.attack_cnt
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.basic_rule_ids is not None:
            result['BasicRuleIds'] = self.basic_rule_ids
        if self.cve_id is not None:
            result['CveId'] = self.cve_id
        if self.first_time is not None:
            result['FirstTime'] = self.first_time
        if self.highlight_tag is not None:
            result['HighlightTag'] = self.highlight_tag
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.need_open_basic_rule is not None:
            result['NeedOpenBasicRule'] = self.need_open_basic_rule
        if self.need_open_basic_rule_uuids is not None:
            result['NeedOpenBasicRuleUuids'] = self.need_open_basic_rule_uuids
        if self.need_open_run_mode is not None:
            result['NeedOpenRunMode'] = self.need_open_run_mode
        if self.need_open_virtual_patche is not None:
            result['NeedOpenVirtualPatche'] = self.need_open_virtual_patche
        if self.need_open_virtual_patche_uuids is not None:
            result['NeedOpenVirtualPatcheUuids'] = self.need_open_virtual_patche_uuids
        if self.need_rule_class is not None:
            result['NeedRuleClass'] = self.need_rule_class
        if self.resource_cnt is not None:
            result['ResourceCnt'] = self.resource_cnt
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.virtual_patche_ids is not None:
            result['VirtualPatcheIds'] = self.virtual_patche_ids
        if self.vuln_key is not None:
            result['VulnKey'] = self.vuln_key
        if self.vuln_level is not None:
            result['VulnLevel'] = self.vuln_level
        if self.vuln_name is not None:
            result['VulnName'] = self.vuln_name
        if self.vuln_status is not None:
            result['VulnStatus'] = self.vuln_status
        if self.vuln_type is not None:
            result['VulnType'] = self.vuln_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackCnt') is not None:
            self.attack_cnt = m.get('AttackCnt')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('BasicRuleIds') is not None:
            self.basic_rule_ids = m.get('BasicRuleIds')
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')
        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')
        if m.get('HighlightTag') is not None:
            self.highlight_tag = m.get('HighlightTag')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NeedOpenBasicRule') is not None:
            self.need_open_basic_rule = m.get('NeedOpenBasicRule')
        if m.get('NeedOpenBasicRuleUuids') is not None:
            self.need_open_basic_rule_uuids = m.get('NeedOpenBasicRuleUuids')
        if m.get('NeedOpenRunMode') is not None:
            self.need_open_run_mode = m.get('NeedOpenRunMode')
        if m.get('NeedOpenVirtualPatche') is not None:
            self.need_open_virtual_patche = m.get('NeedOpenVirtualPatche')
        if m.get('NeedOpenVirtualPatcheUuids') is not None:
            self.need_open_virtual_patche_uuids = m.get('NeedOpenVirtualPatcheUuids')
        if m.get('NeedRuleClass') is not None:
            self.need_rule_class = m.get('NeedRuleClass')
        if m.get('ResourceCnt') is not None:
            self.resource_cnt = m.get('ResourceCnt')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = DescribeVulnerabilityProtectedListResponseBodyVulnListResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('VirtualPatcheIds') is not None:
            self.virtual_patche_ids = m.get('VirtualPatcheIds')
        if m.get('VulnKey') is not None:
            self.vuln_key = m.get('VulnKey')
        if m.get('VulnLevel') is not None:
            self.vuln_level = m.get('VulnLevel')
        if m.get('VulnName') is not None:
            self.vuln_name = m.get('VulnName')
        if m.get('VulnStatus') is not None:
            self.vuln_status = m.get('VulnStatus')
        if m.get('VulnType') is not None:
            self.vuln_type = m.get('VulnType')
        return self


class DescribeVulnerabilityProtectedListResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, vuln_list=None, zero_resource_count=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of vulnerabilities that are detected by Cloud Firewall.
        self.total_count = total_count  # type: int
        # An array that consists of the information about the vulnerabilities.
        self.vuln_list = vuln_list  # type: list[DescribeVulnerabilityProtectedListResponseBodyVulnList]
        # The number of assets on which no vulnerabilities are detected.
        self.zero_resource_count = zero_resource_count  # type: int

    def validate(self):
        if self.vuln_list:
            for k in self.vuln_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVulnerabilityProtectedListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VulnList'] = []
        if self.vuln_list is not None:
            for k in self.vuln_list:
                result['VulnList'].append(k.to_map() if k else None)
        if self.zero_resource_count is not None:
            result['ZeroResourceCount'] = self.zero_resource_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vuln_list = []
        if m.get('VulnList') is not None:
            for k in m.get('VulnList'):
                temp_model = DescribeVulnerabilityProtectedListResponseBodyVulnList()
                self.vuln_list.append(temp_model.from_map(k))
        if m.get('ZeroResourceCount') is not None:
            self.zero_resource_count = m.get('ZeroResourceCount')
        return self


class DescribeVulnerabilityProtectedListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVulnerabilityProtectedListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVulnerabilityProtectedListResponse, self).to_map()
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
            temp_model = DescribeVulnerabilityProtectedListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAddressBookRequestTagList(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The key of ECS tag N that you want to match.
        self.tag_key = tag_key  # type: str
        # The value of ECS tag N that you want to match.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAddressBookRequestTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ModifyAddressBookRequest(TeaModel):
    def __init__(self, address_list=None, auto_add_tag_ecs=None, description=None, group_name=None, group_uuid=None,
                 lang=None, source_ip=None, tag_list=None, tag_relation=None):
        # The addresses in the address book. Separate multiple addresses with commas (,). If you set GroupType to **ip**, **port**, or **domain**, you must specify this parameter.
        # 
        # *   If you set GroupType to **ip**, you must specify IP addresses for the address book. Example: 1.2.XX.XX/32,1.2.XX.XX/24.
        # *   If you set GroupType to **port**, you must specify port numbers or port ranges for the address book. Example: 80/80,100/200.
        # *   If you set GroupType to **domain**, you must specify domain names for the address book. Example: demo1.aliyun.com,demo2.aliyun.com.
        self.address_list = address_list  # type: str
        # Specifies whether to automatically add public IP addresses of Elastic Compute Service (ECS) instances to the address book if the instances match the specified tags. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.auto_add_tag_ecs = auto_add_tag_ecs  # type: str
        # The description of the address book.
        self.description = description  # type: str
        # The name of the address book.
        self.group_name = group_name  # type: str
        # The ID of the address book.
        # 
        # >  To modify the address book, you must provide the ID of the address book. You can call the [DescribeAddressBook](~~138869~~) operation to query the ID.
        self.group_uuid = group_uuid  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str
        # The ECS tags that you want to match.
        self.tag_list = tag_list  # type: list[ModifyAddressBookRequestTagList]
        # The logical relationship among ECS tags. Valid values:
        # 
        # *   **and**: Only the public IP addresses of ECS instances that match all the specified tags can be added to the address book.
        # *   **or**: The public IP addresses of ECS instances that match one of the specified tags can be added to the address book.
        self.tag_relation = tag_relation  # type: str

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyAddressBookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_list is not None:
            result['AddressList'] = self.address_list
        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')
        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = ModifyAddressBookRequestTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')
        return self


class ModifyAddressBookResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAddressBookResponseBody, self).to_map()
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


class ModifyAddressBookResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAddressBookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAddressBookResponse, self).to_map()
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
            temp_model = ModifyAddressBookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyControlPolicyRequest(TeaModel):
    def __init__(self, acl_action=None, acl_uuid=None, application_name=None, application_name_list=None,
                 description=None, dest_port=None, dest_port_group=None, dest_port_type=None, destination=None,
                 destination_type=None, direction=None, end_time=None, lang=None, proto=None, release=None, repeat_days=None,
                 repeat_end_time=None, repeat_start_time=None, repeat_type=None, source=None, source_type=None, start_time=None):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action  # type: str
        # The ID of the access control policy.
        # 
        # >  If you want to modify the configurations of an access control policy, you must provide the ID of the policy. You can call the [DescribeControlPolicy](~~138866~~) operation to query the ID.
        self.acl_uuid = acl_uuid  # type: str
        # The type of the application that the access control policy supports. Valid values:
        # 
        # *   **ANY**\
        # *   **HTTP**\
        # *   **HTTPS**\
        # *   **MySQL**\
        # *   **SMTP**\
        # *   **SMTPS**\
        # *   **RDP**\
        # *   **VNC**\
        # *   **SSH**\
        # *   **Redis**\
        # *   **MQTT**\
        # *   **MongoDB**\
        # *   **Memcache**\
        # *   **SSL**\
        # 
        # >  The value **ANY** indicates all types of applications.
        self.application_name = application_name  # type: str
        # The application names. You can specify multiple application names.
        self.application_name_list = application_name_list  # type: list[str]
        # The description of the access control policy.
        self.description = description  # type: str
        # The destination port in the access control policy.
        self.dest_port = dest_port  # type: str
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group  # type: str
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type  # type: str
        # The destination address in the access control policy.
        # 
        # *   If **DestinationType** is set to net, the value of **Destination** is a CIDR block. Example: 1.2.XX.XX/24
        # *   If **DestinationType** is set to group, the value of **Destination** is an address book. Example: db_group
        # *   If **DestinationType** is set to domain, the value of **Destination** is a domain name. Example: \*.aliyuncs.com
        # *   If **DestinationType** is set to location, the value of **Destination** is a location. For more information about the location codes, see the "AddControlPolicy" topic. Example: \["BJ11", "ZB"]
        self.destination = destination  # type: str
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: destination CIDR block
        # *   **group**: destination address book
        # *   **domain**: destination domain name
        # *   **location**: destination location
        self.destination_type = destination_type  # type: str
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        self.direction = direction  # type: str
        self.end_time = end_time  # type: long
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The type of the protocol in the access control policy. Valid values:
        # 
        # *   **ANY**\
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # 
        # >  The value **ANY** indicates all types of protocols.
        self.proto = proto  # type: str
        # The status of the access control policy. Valid values:
        # 
        # *   true: enabled
        # *   false: disabled
        self.release = release  # type: str
        self.repeat_days = repeat_days  # type: list[long]
        self.repeat_end_time = repeat_end_time  # type: str
        self.repeat_start_time = repeat_start_time  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy.
        # 
        # *   If **SourceType** is set to net, the value of **Source** is a CIDR block. Example: 1.2.XX.XX/24
        # *   If **SourceType** is set to group, the value of **Source** is an address book. Example: db_group
        # *   If **SourceType** is set to location, the value of **Source** is a location. For more information about the location codes, see the "AddControlPolicy" topic. Example: \["BJ11", "ZB"]
        self.source = source  # type: str
        # The type of the source address in the access control policy. Valid values:
        # 
        # *   **net**: source CIDR block
        # *   **group**: source address book
        # *   **location**: source location
        self.source_type = source_type  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.repeat_end_time is not None:
            result['RepeatEndTime'] = self.repeat_end_time
        if self.repeat_start_time is not None:
            result['RepeatStartTime'] = self.repeat_start_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RepeatEndTime') is not None:
            self.repeat_end_time = m.get('RepeatEndTime')
        if m.get('RepeatStartTime') is not None:
            self.repeat_start_time = m.get('RepeatStartTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ModifyControlPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyControlPolicyResponseBody, self).to_map()
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


class ModifyControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyControlPolicyResponse, self).to_map()
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
            temp_model = ModifyControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyControlPolicyPositionRequest(TeaModel):
    def __init__(self, direction=None, lang=None, new_order=None, old_order=None, source_ip=None):
        # The direction of the traffic to which the IPv4 access control policy applies. Valid values:
        # 
        # *   in: inbound traffic
        # *   out: outbound traffic
        self.direction = direction  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   zh: Chinese (default)
        # *   en: English
        self.lang = lang  # type: str
        # The new priority of the IPv4 access control policy.
        # 
        # You must specify a numeric value for this parameter. The value 1 indicates the highest priority. A larger value indicates a lower priority.
        # 
        # >  The value of this parameter must be within the priority range of existing IPv4 access control policies. Otherwise, an error occurs when you call this operation.
        # 
        # We recommend that you first call the [DescribePolicyPriorUsed](~~138862~~) operation to query the priority range of existing IPv4 access control policies that apply to the traffic of the specified direction.
        self.new_order = new_order  # type: str
        # The original priority of the IPv4 access control policy.
        self.old_order = old_order  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyControlPolicyPositionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.old_order is not None:
            result['OldOrder'] = self.old_order
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('OldOrder') is not None:
            self.old_order = m.get('OldOrder')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ModifyControlPolicyPositionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyControlPolicyPositionResponseBody, self).to_map()
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


class ModifyControlPolicyPositionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyControlPolicyPositionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyControlPolicyPositionResponse, self).to_map()
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
            temp_model = ModifyControlPolicyPositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefaultIPSConfigRequest(TeaModel):
    def __init__(self, ai_rules=None, basic_rules=None, cti_rules=None, enable_all_patch=None, enable_default=None,
                 lang=None, patch_rules=None, rule_class=None, run_mode=None, source_ip=None):
        self.ai_rules = ai_rules  # type: str
        self.basic_rules = basic_rules  # type: str
        self.cti_rules = cti_rules  # type: str
        self.enable_all_patch = enable_all_patch  # type: str
        self.enable_default = enable_default  # type: str
        self.lang = lang  # type: str
        self.patch_rules = patch_rules  # type: str
        self.rule_class = rule_class  # type: str
        self.run_mode = run_mode  # type: str
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefaultIPSConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_rules is not None:
            result['AiRules'] = self.ai_rules
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.cti_rules is not None:
            result['CtiRules'] = self.cti_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.enable_default is not None:
            result['EnableDefault'] = self.enable_default
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.patch_rules is not None:
            result['PatchRules'] = self.patch_rules
        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AiRules') is not None:
            self.ai_rules = m.get('AiRules')
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('CtiRules') is not None:
            self.cti_rules = m.get('CtiRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('EnableDefault') is not None:
            self.enable_default = m.get('EnableDefault')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PatchRules') is not None:
            self.patch_rules = m.get('PatchRules')
        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ModifyDefaultIPSConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefaultIPSConfigResponseBody, self).to_map()
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


class ModifyDefaultIPSConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDefaultIPSConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDefaultIPSConfigResponse, self).to_map()
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
            temp_model = ModifyDefaultIPSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFirewallV2RoutePolicySwitchRequest(TeaModel):
    def __init__(self, firewall_id=None, lang=None, should_recover=None, tr_firewall_route_policy_id=None,
                 tr_firewall_route_policy_switch_status=None):
        self.firewall_id = firewall_id  # type: str
        self.lang = lang  # type: str
        self.should_recover = should_recover  # type: str
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id  # type: str
        self.tr_firewall_route_policy_switch_status = tr_firewall_route_policy_switch_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFirewallV2RoutePolicySwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.should_recover is not None:
            result['ShouldRecover'] = self.should_recover
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        if self.tr_firewall_route_policy_switch_status is not None:
            result['TrFirewallRoutePolicySwitchStatus'] = self.tr_firewall_route_policy_switch_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ShouldRecover') is not None:
            self.should_recover = m.get('ShouldRecover')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        if m.get('TrFirewallRoutePolicySwitchStatus') is not None:
            self.tr_firewall_route_policy_switch_status = m.get('TrFirewallRoutePolicySwitchStatus')
        return self


class ModifyFirewallV2RoutePolicySwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFirewallV2RoutePolicySwitchResponseBody, self).to_map()
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


class ModifyFirewallV2RoutePolicySwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFirewallV2RoutePolicySwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFirewallV2RoutePolicySwitchResponse, self).to_map()
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
            temp_model = ModifyFirewallV2RoutePolicySwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMemberAttributesRequestMembers(TeaModel):
    def __init__(self, member_desc=None, member_uid=None):
        # The remarks of the member in Cloud Firewall.
        self.member_desc = member_desc  # type: str
        # The UID of the member in Cloud Firewall.
        self.member_uid = member_uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMemberAttributesRequestMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        return self


class ModifyInstanceMemberAttributesRequest(TeaModel):
    def __init__(self, members=None):
        # The members that to be modified.
        self.members = members  # type: list[ModifyInstanceMemberAttributesRequestMembers]

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyInstanceMemberAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = ModifyInstanceMemberAttributesRequestMembers()
                self.members.append(temp_model.from_map(k))
        return self


class ModifyInstanceMemberAttributesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceMemberAttributesResponseBody, self).to_map()
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


class ModifyInstanceMemberAttributesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceMemberAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceMemberAttributesResponse, self).to_map()
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
            temp_model = ModifyInstanceMemberAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNatFirewallControlPolicyRequest(TeaModel):
    def __init__(self, acl_action=None, acl_uuid=None, application_name_list=None, description=None, dest_port=None,
                 dest_port_group=None, dest_port_type=None, destination=None, destination_type=None, domain_resolve_type=None,
                 end_time=None, lang=None, nat_gateway_id=None, proto=None, release=None, repeat_days=None,
                 repeat_end_time=None, repeat_start_time=None, repeat_type=None, source=None, source_type=None, start_time=None):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: denies the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action  # type: str
        # The UUID of the access control policy.
        # 
        # To modify the configurations of an access control policy, you must provide the UUID of the policy. You can call the DescribeNatFirewallControlPolicy operation to query the UUIDs of access control policies.
        self.acl_uuid = acl_uuid  # type: str
        # The name of the application.
        self.application_name_list = application_name_list  # type: list[str]
        # The description of the access control policy. Fuzzy match is supported.
        # 
        # > If you do not specify this parameter, the descriptions of all policies are queried.
        self.description = description  # type: str
        # The destination port in the access control policy.
        # 
        # > If **DestPortType** is set to `port`, you must specify this parameter.
        self.dest_port = dest_port  # type: str
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group  # type: str
        # The type of the destination port in the access control policy. Valid values:
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type  # type: str
        # The destination address in the access control policy.
        # 
        # *   If **DestinationType** is set to net, the value of **Destination** is a CIDR block. Example: 1.2.3.4/24
        # *   If **DestinationType** is set to group, the value of **Destination** is an address book. Example: db_group
        # *   If **DestinationType** is set to domain, the value of **Destination** is a domain name. Example: \*.aliyuncs.com
        # *   If **DestinationType** is set to location, the value of **Destination** is a location. For more information about the location codes, see the "AddControlPolicy" topic. Example: \["BJ11", "ZB"]
        self.destination = destination  # type: str
        # The type of the destination address in the access control policy. Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        # *   **location**\
        self.destination_type = destination_type  # type: str
        # The domain name resolution method of the access control policy. By default, an access control policy is enabled after it is created. Valid values:
        # 
        # *   **0**: Fully qualified domain name (FQDN)-based resolution
        # *   **1**: Domain Name System (DNS)-based dynamic resolution
        # *   **2**: FQDN and DNS-based dynamic resolution
        self.domain_resolve_type = domain_resolve_type  # type: str
        self.end_time = end_time  # type: long
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id  # type: str
        # The protocol type supported by the access control policy. Valid values:
        # 
        # *   **ANY**\
        # *   **TCP**\
        # *   **UDP**\
        # *   **ICMP**\
        # 
        # > The value **ANY** indicates all types of protocols.
        self.proto = proto  # type: str
        # The status of the access control policy. Valid values:
        # 
        # *   true: enabled
        # *   false: disabled
        self.release = release  # type: str
        self.repeat_days = repeat_days  # type: list[long]
        self.repeat_end_time = repeat_end_time  # type: str
        self.repeat_start_time = repeat_start_time  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy.
        # 
        # Valid values:
        # 
        # *   If **SourceType** is set to `net`, the value of Source is a CIDR block.
        # 
        #     Example: 10.2.4.0/24
        # 
        # *   If **SourceType** is set to `group`, the value of this parameter is an address book.
        # 
        #     Example: db_group
        self.source = source  # type: str
        # The type of the source address in the access control policy.
        # 
        # Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        self.source_type = source_type  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNatFirewallControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.domain_resolve_type is not None:
            result['DomainResolveType'] = self.domain_resolve_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.repeat_end_time is not None:
            result['RepeatEndTime'] = self.repeat_end_time
        if self.repeat_start_time is not None:
            result['RepeatStartTime'] = self.repeat_start_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('DomainResolveType') is not None:
            self.domain_resolve_type = m.get('DomainResolveType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RepeatEndTime') is not None:
            self.repeat_end_time = m.get('RepeatEndTime')
        if m.get('RepeatStartTime') is not None:
            self.repeat_start_time = m.get('RepeatStartTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ModifyNatFirewallControlPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNatFirewallControlPolicyResponseBody, self).to_map()
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


class ModifyNatFirewallControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyNatFirewallControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNatFirewallControlPolicyResponse, self).to_map()
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
            temp_model = ModifyNatFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNatFirewallControlPolicyPositionRequest(TeaModel):
    def __init__(self, acl_uuid=None, lang=None, nat_gateway_id=None, new_order=None):
        # The UUID of the access control policy.
        self.acl_uuid = acl_uuid  # type: str
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id  # type: str
        # The new priority of the IPv4 access control policy. You must specify a numeric value for this parameter. The value 1 indicates the highest priority. A larger value indicates a lower priority.
        # 
        # > Make sure that the value of this parameter is within the priority range of existing IPv4 access control policies. Otherwise, an error occurs when you call this operation.
        # 
        # Before you call this operation, we recommend that you call the DescribeNatFirewallPolicyPriorUsed operation to query the priority range of the IPv4 access control policies in the specified traffic direction.
        self.new_order = new_order  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNatFirewallControlPolicyPositionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        return self


class ModifyNatFirewallControlPolicyPositionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNatFirewallControlPolicyPositionResponseBody, self).to_map()
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


class ModifyNatFirewallControlPolicyPositionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyNatFirewallControlPolicyPositionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNatFirewallControlPolicyPositionResponse, self).to_map()
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
            temp_model = ModifyNatFirewallControlPolicyPositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyAdvancedConfigRequest(TeaModel):
    def __init__(self, internet_switch=None, lang=None, source_ip=None):
        # Specifies whether to enable the strict mode for the access control policy. Valid values:
        # 
        # *   **on**: enables the strict mode.
        # *   **off**: disables the strict mode.
        self.internet_switch = internet_switch  # type: str
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyAdvancedConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_switch is not None:
            result['InternetSwitch'] = self.internet_switch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InternetSwitch') is not None:
            self.internet_switch = m.get('InternetSwitch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ModifyPolicyAdvancedConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyAdvancedConfigResponseBody, self).to_map()
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


class ModifyPolicyAdvancedConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPolicyAdvancedConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPolicyAdvancedConfigResponse, self).to_map()
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
            temp_model = ModifyPolicyAdvancedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTrFirewallV2ConfigurationRequest(TeaModel):
    def __init__(self, firewall_id=None, firewall_name=None, lang=None):
        self.firewall_id = firewall_id  # type: str
        self.firewall_name = firewall_name  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTrFirewallV2ConfigurationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ModifyTrFirewallV2ConfigurationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTrFirewallV2ConfigurationResponseBody, self).to_map()
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


class ModifyTrFirewallV2ConfigurationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTrFirewallV2ConfigurationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTrFirewallV2ConfigurationResponse, self).to_map()
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
            temp_model = ModifyTrFirewallV2ConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTrFirewallV2RoutePolicyScopeRequestDestCandidateList(TeaModel):
    def __init__(self, candidate_id=None, candidate_type=None):
        self.candidate_id = candidate_id  # type: str
        self.candidate_type = candidate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTrFirewallV2RoutePolicyScopeRequestDestCandidateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class ModifyTrFirewallV2RoutePolicyScopeRequestSrcCandidateList(TeaModel):
    def __init__(self, candidate_id=None, candidate_type=None):
        self.candidate_id = candidate_id  # type: str
        self.candidate_type = candidate_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTrFirewallV2RoutePolicyScopeRequestSrcCandidateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id
        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')
        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')
        return self


class ModifyTrFirewallV2RoutePolicyScopeRequest(TeaModel):
    def __init__(self, dest_candidate_list=None, firewall_id=None, lang=None, src_candidate_list=None,
                 tr_firewall_route_policy_id=None):
        self.dest_candidate_list = dest_candidate_list  # type: list[ModifyTrFirewallV2RoutePolicyScopeRequestDestCandidateList]
        self.firewall_id = firewall_id  # type: str
        self.lang = lang  # type: str
        self.src_candidate_list = src_candidate_list  # type: list[ModifyTrFirewallV2RoutePolicyScopeRequestSrcCandidateList]
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id  # type: str

    def validate(self):
        if self.dest_candidate_list:
            for k in self.dest_candidate_list:
                if k:
                    k.validate()
        if self.src_candidate_list:
            for k in self.src_candidate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyTrFirewallV2RoutePolicyScopeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DestCandidateList'] = []
        if self.dest_candidate_list is not None:
            for k in self.dest_candidate_list:
                result['DestCandidateList'].append(k.to_map() if k else None)
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        result['SrcCandidateList'] = []
        if self.src_candidate_list is not None:
            for k in self.src_candidate_list:
                result['SrcCandidateList'].append(k.to_map() if k else None)
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dest_candidate_list = []
        if m.get('DestCandidateList') is not None:
            for k in m.get('DestCandidateList'):
                temp_model = ModifyTrFirewallV2RoutePolicyScopeRequestDestCandidateList()
                self.dest_candidate_list.append(temp_model.from_map(k))
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        self.src_candidate_list = []
        if m.get('SrcCandidateList') is not None:
            for k in m.get('SrcCandidateList'):
                temp_model = ModifyTrFirewallV2RoutePolicyScopeRequestSrcCandidateList()
                self.src_candidate_list.append(temp_model.from_map(k))
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class ModifyTrFirewallV2RoutePolicyScopeShrinkRequest(TeaModel):
    def __init__(self, dest_candidate_list_shrink=None, firewall_id=None, lang=None,
                 src_candidate_list_shrink=None, tr_firewall_route_policy_id=None):
        self.dest_candidate_list_shrink = dest_candidate_list_shrink  # type: str
        self.firewall_id = firewall_id  # type: str
        self.lang = lang  # type: str
        self.src_candidate_list_shrink = src_candidate_list_shrink  # type: str
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTrFirewallV2RoutePolicyScopeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_candidate_list_shrink is not None:
            result['DestCandidateList'] = self.dest_candidate_list_shrink
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.src_candidate_list_shrink is not None:
            result['SrcCandidateList'] = self.src_candidate_list_shrink
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestCandidateList') is not None:
            self.dest_candidate_list_shrink = m.get('DestCandidateList')
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SrcCandidateList') is not None:
            self.src_candidate_list_shrink = m.get('SrcCandidateList')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class ModifyTrFirewallV2RoutePolicyScopeResponseBody(TeaModel):
    def __init__(self, request_id=None, tr_firewall_route_policy_id=None):
        self.request_id = request_id  # type: str
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTrFirewallV2RoutePolicyScopeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')
        return self


class ModifyTrFirewallV2RoutePolicyScopeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTrFirewallV2RoutePolicyScopeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTrFirewallV2RoutePolicyScopeResponse, self).to_map()
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
            temp_model = ModifyTrFirewallV2RoutePolicyScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserIPSWhitelistRequest(TeaModel):
    def __init__(self, direction=None, ip_version=None, lang=None, list_type=None, list_value=None, source_ip=None,
                 white_type=None):
        self.direction = direction  # type: long
        self.ip_version = ip_version  # type: str
        self.lang = lang  # type: str
        self.list_type = list_type  # type: long
        self.list_value = list_value  # type: str
        self.source_ip = source_ip  # type: str
        self.white_type = white_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserIPSWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.list_type is not None:
            result['ListType'] = self.list_type
        if self.list_value is not None:
            result['ListValue'] = self.list_value
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.white_type is not None:
            result['WhiteType'] = self.white_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')
        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')
        return self


class ModifyUserIPSWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserIPSWhitelistResponseBody, self).to_map()
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


class ModifyUserIPSWhitelistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyUserIPSWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyUserIPSWhitelistResponse, self).to_map()
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
            temp_model = ModifyUserIPSWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallCenConfigureRequest(TeaModel):
    def __init__(self, lang=None, member_uid=None, vpc_firewall_id=None, vpc_firewall_name=None):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallCenList](~~345777~~) operation to query the instance IDs of VPC firewalls.
        self.vpc_firewall_id = vpc_firewall_id  # type: str
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallCenConfigureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class ModifyVpcFirewallCenConfigureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallCenConfigureResponseBody, self).to_map()
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


class ModifyVpcFirewallCenConfigureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyVpcFirewallCenConfigureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVpcFirewallCenConfigureResponse, self).to_map()
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
            temp_model = ModifyVpcFirewallCenConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallCenSwitchStatusRequest(TeaModel):
    def __init__(self, firewall_switch=None, lang=None, member_uid=None, vpc_firewall_id=None):
        # Specifies whether to enable the VPC firewall. Valid values:
        # 
        # *   **open**: yes
        # *   **close**: no
        self.firewall_switch = firewall_switch  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallCenList](~~345777~~) operation to query the instance IDs of VPC firewalls.
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallCenSwitchStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class ModifyVpcFirewallCenSwitchStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallCenSwitchStatusResponseBody, self).to_map()
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


class ModifyVpcFirewallCenSwitchStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyVpcFirewallCenSwitchStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVpcFirewallCenSwitchStatusResponse, self).to_map()
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
            temp_model = ModifyVpcFirewallCenSwitchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallConfigureRequest(TeaModel):
    def __init__(self, lang=None, local_vpc_cidr_table_list=None, member_uid=None, peer_vpc_cidr_table_list=None,
                 vpc_firewall_id=None, vpc_firewall_name=None):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The CIDR blocks of the local VPC. The value is a JSON string that contains the following parameters:
        # 
        # *   **RouteTableId**: the ID of the route table for the local VPC.
        # *   **RouteEntryList**: The value is a JSON string that contains the DestinationCidr and NextHopInstanceId parameters. The DestinationCidr parameter indicates the destination CIDR block of the local VPC. The NextHopInstanceId parameter indicates the instance ID of the next hop for the local VPC.
        # 
        # > You can call the [DescribeVpcFirewallDetail](~~342892~~) operation to query the CIDR blocks of local VPCs for VPC firewalls.
        self.local_vpc_cidr_table_list = local_vpc_cidr_table_list  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The CIDR blocks of the peer VPC. The value is a JSON string that contains the following parameters:
        # 
        # *   **RouteTableId**: the ID of the route table for the peer VPC.
        # *   **RouteEntryList**: The value is a JSON string that contains the DestinationCidr and NextHopInstanceId parameters. The DestinationCidr parameter indicates the destination CIDR block of the peer VPC. The NextHopInstanceId parameter indicates the instance ID of the next hop for the peer VPC.
        # 
        # > You can call the [DescribeVpcFirewallDetail](~~342892~~) operation to query the CIDR blocks of peer VPCs for VPC firewalls.
        self.peer_vpc_cidr_table_list = peer_vpc_cidr_table_list  # type: str
        # The instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallList](~~342932~~) operation to query the instance IDs of VPC firewalls.
        self.vpc_firewall_id = vpc_firewall_id  # type: str
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallConfigureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.local_vpc_cidr_table_list is not None:
            result['LocalVpcCidrTableList'] = self.local_vpc_cidr_table_list
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.peer_vpc_cidr_table_list is not None:
            result['PeerVpcCidrTableList'] = self.peer_vpc_cidr_table_list
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LocalVpcCidrTableList') is not None:
            self.local_vpc_cidr_table_list = m.get('LocalVpcCidrTableList')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PeerVpcCidrTableList') is not None:
            self.peer_vpc_cidr_table_list = m.get('PeerVpcCidrTableList')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')
        return self


class ModifyVpcFirewallConfigureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallConfigureResponseBody, self).to_map()
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


class ModifyVpcFirewallConfigureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyVpcFirewallConfigureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVpcFirewallConfigureResponse, self).to_map()
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
            temp_model = ModifyVpcFirewallConfigureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallControlPolicyRequest(TeaModel):
    def __init__(self, acl_action=None, acl_uuid=None, application_name=None, application_name_list=None,
                 description=None, dest_port=None, dest_port_group=None, dest_port_type=None, destination=None,
                 destination_type=None, end_time=None, lang=None, proto=None, release=None, repeat_days=None, repeat_end_time=None,
                 repeat_start_time=None, repeat_type=None, source=None, source_type=None, start_time=None, vpc_firewall_id=None):
        # The action that Cloud Firewall performs on the traffic.
        # 
        # Valid values:
        # 
        # *   **accept**: allows the traffic.
        # *   **drop**: blocks the traffic.
        # *   **log**: monitors the traffic.
        self.acl_action = acl_action  # type: str
        # The unique ID of the access control policy.
        # 
        # If you want to modify the configurations of an access control policy, you must provide the unique ID of the policy. You can call the [DescribeVpcFirewallControlPolicy](~~159758~~) operation to query the ID.
        self.acl_uuid = acl_uuid  # type: str
        # The application type in the access control policy.
        # 
        # Valid values:
        # 
        # *   ANY
        # *   FTP
        # *   HTTP
        # *   HTTPS
        # *   MySQL
        # *   SMTP
        # *   SMTPS
        # *   RDP
        # *   VNC
        # *   SSH
        # *   Redis
        # *   MQTT
        # *   MongoDB
        # *   Memcache
        # *   SSL
        # *   ANY: all application types
        self.application_name = application_name  # type: str
        self.application_name_list = application_name_list  # type: list[str]
        # The description of the access control policy.
        self.description = description  # type: str
        # The destination port in the access control policy.
        self.dest_port = dest_port  # type: str
        # The name of the destination port address book in the access control policy.
        self.dest_port_group = dest_port_group  # type: str
        # The type of the destination port in the access control policy.
        # 
        # *   **port**: port
        # *   **group**: port address book
        self.dest_port_type = dest_port_type  # type: str
        # The destination address in the access control policy.
        # 
        # *   If **DestinationType** is set to `net`, the value of this parameter must be a CIDR block.
        # 
        #     Example: 10.2.3.0/24
        # 
        # *   If **DestinationType** is set to `group`, the value of this parameter must be an address book name.
        # 
        #     Example: db_group
        # 
        # *   If **DestinationType** is set to `domain`, the value of this parameter must be a domain name.
        # 
        #     Example: \*.aliyuncs.com
        self.destination = destination  # type: str
        # The type of the destination address in the access control policy.
        # 
        # Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        # *   **domain**: domain name
        self.destination_type = destination_type  # type: str
        self.end_time = end_time  # type: long
        # The language of the content within the response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The protocol type in the access control policy.
        # 
        # Valid values:
        # 
        # *   ANY: all protocol types
        # *   TCP
        # *   UDP
        # *   ICMP
        self.proto = proto  # type: str
        # Specifies whether to enable the access control policy. By default, an access control policy is enabled after the policy is created. Valid values:
        # 
        # *   **true**: enables the access control policy.
        # *   **false**: disables the access control policy.
        self.release = release  # type: str
        self.repeat_days = repeat_days  # type: list[long]
        self.repeat_end_time = repeat_end_time  # type: str
        self.repeat_start_time = repeat_start_time  # type: str
        self.repeat_type = repeat_type  # type: str
        # The source address in the access control policy.
        # 
        # Valid values:
        # 
        # *   If **SourceType** is set to `net`, the value of this parameter must be a CIDR block.
        # 
        #     Example: 10.2.4.0/24
        # 
        # *   If **SourceType** is set to `group`, the value of this parameter must be an address book name.
        # 
        #     Example: db_group
        self.source = source  # type: str
        # The type of the source address in the access control policy.
        # 
        # Valid values:
        # 
        # *   **net**: CIDR block
        # *   **group**: address book
        self.source_type = source_type  # type: str
        self.start_time = start_time  # type: long
        # The instance ID of the VPC firewall. You can call the [DescribeVpcFirewallAclGroupList](~~159760~~) operation to query the ID.
        # 
        # *   If the VPC firewall is used to protect a CEN instance, the value of this parameter must be the ID of the CEN instance.
        # 
        #     Example: cen-ervw0g12b5jbw\*\*\*\*\
        # 
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter must be the instance ID of the VPC firewall.
        # 
        #     Example: vfw-a42bbb7b887148c9\*\*\*\*\
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallControlPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list
        if self.description is not None:
            result['Description'] = self.description
        if self.dest_port is not None:
            result['DestPort'] = self.dest_port
        if self.dest_port_group is not None:
            result['DestPortGroup'] = self.dest_port_group
        if self.dest_port_type is not None:
            result['DestPortType'] = self.dest_port_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.proto is not None:
            result['Proto'] = self.proto
        if self.release is not None:
            result['Release'] = self.release
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.repeat_end_time is not None:
            result['RepeatEndTime'] = self.repeat_end_time
        if self.repeat_start_time is not None:
            result['RepeatStartTime'] = self.repeat_start_time
        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestPort') is not None:
            self.dest_port = m.get('DestPort')
        if m.get('DestPortGroup') is not None:
            self.dest_port_group = m.get('DestPortGroup')
        if m.get('DestPortType') is not None:
            self.dest_port_type = m.get('DestPortType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Proto') is not None:
            self.proto = m.get('Proto')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RepeatEndTime') is not None:
            self.repeat_end_time = m.get('RepeatEndTime')
        if m.get('RepeatStartTime') is not None:
            self.repeat_start_time = m.get('RepeatStartTime')
        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class ModifyVpcFirewallControlPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallControlPolicyResponseBody, self).to_map()
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


class ModifyVpcFirewallControlPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyVpcFirewallControlPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVpcFirewallControlPolicyResponse, self).to_map()
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
            temp_model = ModifyVpcFirewallControlPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallControlPolicyPositionRequest(TeaModel):
    def __init__(self, acl_uuid=None, lang=None, new_order=None, old_order=None, vpc_firewall_id=None):
        # The UUID of the access control policy.
        # 
        # If you want to modify the configurations of an access control policy, you must provide the UUID of the policy. You can call the [DescribeVpcFirewallControlPolicy](~~159758~~) operation to query the UUID.
        self.acl_uuid = acl_uuid  # type: str
        # The language of the content within the request and the response.
        # 
        # Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The new priority of the access control policy.
        self.new_order = new_order  # type: str
        # The original priority of the access control policy.
        # 
        # > This parameter is not recommended. We recommend that you use the AclUuid parameter to specify the policy that you want to modify.
        self.old_order = old_order  # type: str
        # The ID of the group to which the access control policy belongs. You can call the [DescribeVpcFirewallAclGroupList](~~159760~~) operation to query the ID.
        # 
        # Valid values:
        # 
        # *   If the VPC firewall is used to protect a CEN instance, the value of this parameter must be the ID of the CEN instance.
        # 
        #     Example: cen-ervw0g12b5jbw\*\*\*\*\
        # 
        # *   If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter must be the instance ID of the VPC firewall.
        # 
        #     Example: vfw-a42bbb7b887148c9\*\*\*\*\
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallControlPolicyPositionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.new_order is not None:
            result['NewOrder'] = self.new_order
        if self.old_order is not None:
            result['OldOrder'] = self.old_order
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')
        if m.get('OldOrder') is not None:
            self.old_order = m.get('OldOrder')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class ModifyVpcFirewallControlPolicyPositionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallControlPolicyPositionResponseBody, self).to_map()
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


class ModifyVpcFirewallControlPolicyPositionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyVpcFirewallControlPolicyPositionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVpcFirewallControlPolicyPositionResponse, self).to_map()
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
            temp_model = ModifyVpcFirewallControlPolicyPositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallDefaultIPSConfigRequest(TeaModel):
    def __init__(self, basic_rules=None, enable_all_patch=None, lang=None, member_uid=None, run_mode=None,
                 source_ip=None, vpc_firewall_id=None):
        # Specifies whether to enable basic protection. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules  # type: str
        # Specifies whether to enable virtual patching. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The mode of the intrusion prevention system (IPS). Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str
        # The instance ID of the VPC firewall. Valid values:
        # 
        # *   If the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. You can call the [DescribeVpcFirewallCenList](~~345777~~) operation to query the IDs of CEN instances.
        # *   If the VPC firewall protects mutual access traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter is the ID of the VPC firewall. You can call the [DescribeVpcFirewallList](~~342932~~) operation to query the instance IDs of VPC firewalls.
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallDefaultIPSConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules
        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')
        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class ModifyVpcFirewallDefaultIPSConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallDefaultIPSConfigResponseBody, self).to_map()
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


class ModifyVpcFirewallDefaultIPSConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyVpcFirewallDefaultIPSConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVpcFirewallDefaultIPSConfigResponse, self).to_map()
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
            temp_model = ModifyVpcFirewallDefaultIPSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcFirewallSwitchStatusRequest(TeaModel):
    def __init__(self, firewall_switch=None, lang=None, member_uid=None, vpc_firewall_id=None):
        # Specifies whether to enable the VPC firewall. Valid values:
        # 
        # *   **open**: yes
        # *   **close**: no
        self.firewall_switch = firewall_switch  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid  # type: str
        # The instance ID of the VPC firewall.
        # 
        # > You can call the [DescribeVpcFirewallList](~~342932~~) operation to query the instance IDs of VPC firewalls.
        self.vpc_firewall_id = vpc_firewall_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallSwitchStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')
        return self


class ModifyVpcFirewallSwitchStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcFirewallSwitchStatusResponseBody, self).to_map()
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


class ModifyVpcFirewallSwitchStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyVpcFirewallSwitchStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVpcFirewallSwitchStatusResponse, self).to_map()
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
            temp_model = ModifyVpcFirewallSwitchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutDisableAllFwSwitchRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, source_ip=None):
        # The instance ID of your Cloud Firewall.
        self.instance_id = instance_id  # type: str
        # The natural language of the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutDisableAllFwSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class PutDisableAllFwSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutDisableAllFwSwitchResponseBody, self).to_map()
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


class PutDisableAllFwSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutDisableAllFwSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutDisableAllFwSwitchResponse, self).to_map()
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
            temp_model = PutDisableAllFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutDisableFwSwitchRequest(TeaModel):
    def __init__(self, ipaddr_list=None, lang=None, region_list=None, resource_type_list=None, source_ip=None):
        # The IP addresses.
        # 
        # >  You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.ipaddr_list = ipaddr_list  # type: list[str]
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The regions.
        # 
        # >  You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.region_list = region_list  # type: list[str]
        # The types of the assets.
        # 
        # > You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.resource_type_list = resource_type_list  # type: list[str]
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutDisableFwSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipaddr_list is not None:
            result['IpaddrList'] = self.ipaddr_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_list is not None:
            result['RegionList'] = self.region_list
        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpaddrList') is not None:
            self.ipaddr_list = m.get('IpaddrList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')
        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class PutDisableFwSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutDisableFwSwitchResponseBody, self).to_map()
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


class PutDisableFwSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutDisableFwSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutDisableFwSwitchResponse, self).to_map()
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
            temp_model = PutDisableFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEnableAllFwSwitchRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, source_ip=None):
        # The instance ID of your Cloud Firewall.
        self.instance_id = instance_id  # type: str
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang  # type: str
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutEnableAllFwSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class PutEnableAllFwSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutEnableAllFwSwitchResponseBody, self).to_map()
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


class PutEnableAllFwSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutEnableAllFwSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutEnableAllFwSwitchResponse, self).to_map()
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
            temp_model = PutEnableAllFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutEnableFwSwitchRequest(TeaModel):
    def __init__(self, ipaddr_list=None, lang=None, region_list=None, resource_type_list=None, source_ip=None):
        # The IP addresses.
        # 
        # > You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.ipaddr_list = ipaddr_list  # type: list[str]
        # The language of the content within the response.
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str
        # The regions.
        # 
        # > You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.region_list = region_list  # type: list[str]
        # The types of the assets.
        # 
        # Valid values:
        # 
        # *   BastionHostIP: the egress IP address of a bastion host
        # *   BastionHostIngressIP: the ingress IP address of a bastion host
        # *   EcsEIP: the elastic IP address (EIP) of an Elastic Compute Service (ECS) instance
        # *   EcsPublicIP: the public IP address of an ECS instance
        # *   EIP: the EIP
        # *   EniEIP: the EIP of an elastic network interface (ENI)
        # *   NatEIP: the EIP of a NAT gateway
        # *   SlbEIP: the EIP of a Server Load Balancer (SLB) instance
        # *   SlbPublicIP: the public IP address of an SLB instance
        # *   NatPublicIP: the public IP address of a NAT gateway
        # *   HAVIP: the high-availability virtual IP address (HAVIP)
        # 
        # > You must specify at least one of the IpaddrList, RegionList, and ResourceTypeList parameters.
        self.resource_type_list = resource_type_list  # type: list[str]
        # The source IP address of the request.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutEnableFwSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipaddr_list is not None:
            result['IpaddrList'] = self.ipaddr_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_list is not None:
            result['RegionList'] = self.region_list
        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpaddrList') is not None:
            self.ipaddr_list = m.get('IpaddrList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')
        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class PutEnableFwSwitchResponseBodyAbnormalResourceStatusList(TeaModel):
    def __init__(self, msg=None, resource=None, status=None):
        # The message displayed when the asset is not synchronized to Cloud Firewall. Valid values:
        # 
        # *   cloudfirewall do not sync this ip address: This IP address is not synchronized to Cloud Firewall.
        self.msg = msg  # type: str
        # The IP address of the asset.
        self.resource = resource  # type: str
        # The status of the asset when it is not synchronized to Cloud Firewall. Valid values:
        # 
        # *   ip_not_sync: The asset is not synchronized.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutEnableFwSwitchResponseBodyAbnormalResourceStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PutEnableFwSwitchResponseBody(TeaModel):
    def __init__(self, abnormal_resource_status_list=None, request_id=None):
        # The status information of the asset when it is not synchronized to Cloud Firewall.
        self.abnormal_resource_status_list = abnormal_resource_status_list  # type: list[PutEnableFwSwitchResponseBodyAbnormalResourceStatusList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.abnormal_resource_status_list:
            for k in self.abnormal_resource_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PutEnableFwSwitchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AbnormalResourceStatusList'] = []
        if self.abnormal_resource_status_list is not None:
            for k in self.abnormal_resource_status_list:
                result['AbnormalResourceStatusList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.abnormal_resource_status_list = []
        if m.get('AbnormalResourceStatusList') is not None:
            for k in m.get('AbnormalResourceStatusList'):
                temp_model = PutEnableFwSwitchResponseBodyAbnormalResourceStatusList()
                self.abnormal_resource_status_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutEnableFwSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutEnableFwSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutEnableFwSwitchResponse, self).to_map()
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
            temp_model = PutEnableFwSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetVpcFirewallRuleHitCountRequest(TeaModel):
    def __init__(self, acl_uuid=None, lang=None):
        # The ID of the access control policy.
        self.acl_uuid = acl_uuid  # type: str
        # The natural language of the request and response. 
        # 
        # Valid values:
        # 
        # - **zh**: Chinese (default)
        # - **en**: English
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetVpcFirewallRuleHitCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ResetVpcFirewallRuleHitCountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetVpcFirewallRuleHitCountResponseBody, self).to_map()
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


class ResetVpcFirewallRuleHitCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetVpcFirewallRuleHitCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetVpcFirewallRuleHitCountResponse, self).to_map()
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
            temp_model = ResetVpcFirewallRuleHitCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


