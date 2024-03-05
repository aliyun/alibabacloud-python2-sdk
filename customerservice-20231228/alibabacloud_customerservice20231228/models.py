# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DataValue(TeaModel):
    def __init__(self, doc_id=None, name=None, file_name=None, url=None, upload_time=None, order_id=None,
                 apply_id=None):
        self.doc_id = doc_id  # type: long
        self.name = name  # type: str
        self.file_name = file_name  # type: str
        self.url = url  # type: str
        self.upload_time = upload_time  # type: str
        self.order_id = order_id  # type: str
        self.apply_id = apply_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.name is not None:
            result['name'] = self.name
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.url is not None:
            result['url'] = self.url
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.apply_id is not None:
            result['applyId'] = self.apply_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('applyId') is not None:
            self.apply_id = m.get('applyId')
        return self


class GetDownloadUrlRequest(TeaModel):
    def __init__(self, file_id=None, file_key=None, free_order_apply_code=None, order_id=None, scene=None):
        self.file_id = file_id  # type: long
        self.file_key = file_key  # type: str
        self.free_order_apply_code = free_order_apply_code  # type: str
        self.order_id = order_id  # type: str
        self.scene = scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDownloadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_key is not None:
            result['fileKey'] = self.file_key
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileKey') is not None:
            self.file_key = m.get('fileKey')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class GetDownloadUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDownloadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDownloadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDownloadUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDownloadUrlResponse, self).to_map()
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
            temp_model = GetDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseSupportPlanDetailRequest(TeaModel):
    def __init__(self, free_order_apply_codes=None, order_ids=None):
        self.free_order_apply_codes = free_order_apply_codes  # type: list[str]
        self.order_ids = order_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.free_order_apply_codes is not None:
            result['freeOrderApplyCodes'] = self.free_order_apply_codes
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('freeOrderApplyCodes') is not None:
            self.free_order_apply_codes = m.get('freeOrderApplyCodes')
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataDingGroups(TeaModel):
    def __init__(self, main_ding_department_id=None, main_ding_group_id=None, main_ding_group_name=None,
                 sub_ding_department_id=None, sub_ding_group_id=None, sub_ding_group_name=None):
        self.main_ding_department_id = main_ding_department_id  # type: str
        self.main_ding_group_id = main_ding_group_id  # type: str
        self.main_ding_group_name = main_ding_group_name  # type: str
        self.sub_ding_department_id = sub_ding_department_id  # type: str
        self.sub_ding_group_id = sub_ding_group_id  # type: str
        self.sub_ding_group_name = sub_ding_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataDingGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.main_ding_department_id is not None:
            result['mainDingDepartmentId'] = self.main_ding_department_id
        if self.main_ding_group_id is not None:
            result['mainDingGroupId'] = self.main_ding_group_id
        if self.main_ding_group_name is not None:
            result['mainDingGroupName'] = self.main_ding_group_name
        if self.sub_ding_department_id is not None:
            result['subDingDepartmentId'] = self.sub_ding_department_id
        if self.sub_ding_group_id is not None:
            result['subDingGroupId'] = self.sub_ding_group_id
        if self.sub_ding_group_name is not None:
            result['subDingGroupName'] = self.sub_ding_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('mainDingDepartmentId') is not None:
            self.main_ding_department_id = m.get('mainDingDepartmentId')
        if m.get('mainDingGroupId') is not None:
            self.main_ding_group_id = m.get('mainDingGroupId')
        if m.get('mainDingGroupName') is not None:
            self.main_ding_group_name = m.get('mainDingGroupName')
        if m.get('subDingDepartmentId') is not None:
            self.sub_ding_department_id = m.get('subDingDepartmentId')
        if m.get('subDingGroupId') is not None:
            self.sub_ding_group_id = m.get('subDingGroupId')
        if m.get('subDingGroupName') is not None:
            self.sub_ding_group_name = m.get('subDingGroupName')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataDocs(TeaModel):
    def __init__(self, doc_id=None, file_name=None, free_order_apply_code=None, name=None, order_id=None,
                 upload_time=None, url=None):
        self.doc_id = doc_id  # type: long
        self.file_name = file_name  # type: str
        self.free_order_apply_code = free_order_apply_code  # type: str
        self.name = name  # type: str
        self.order_id = order_id  # type: str
        self.upload_time = upload_time  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataDocs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.name is not None:
            result['name'] = self.name
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesDocNode(TeaModel):
    def __init__(self, doc_id=None, doc_name=None, doc_submit_time=None, file_name=None, free_order_apply_code=None,
                 order_id=None):
        self.doc_id = doc_id  # type: long
        self.doc_name = doc_name  # type: str
        self.doc_submit_time = doc_submit_time  # type: str
        self.file_name = file_name  # type: str
        self.free_order_apply_code = free_order_apply_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataNodesDocNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.doc_name is not None:
            result['docName'] = self.doc_name
        if self.doc_submit_time is not None:
            result['docSubmitTime'] = self.doc_submit_time
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('docName') is not None:
            self.doc_name = m.get('docName')
        if m.get('docSubmitTime') is not None:
            self.doc_submit_time = m.get('docSubmitTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesFinishNode(TeaModel):
    def __init__(self, finish_time=None):
        self.finish_time = finish_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataNodesFinishNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderAuditNode(TeaModel):
    def __init__(self, audit_time=None, status=None, status_name=None):
        self.audit_time = audit_time  # type: str
        self.status = status  # type: str
        self.status_name = status_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderAuditNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_time is not None:
            result['auditTime'] = self.audit_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_name is not None:
            result['statusName'] = self.status_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auditTime') is not None:
            self.audit_time = m.get('auditTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusName') is not None:
            self.status_name = m.get('statusName')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderNode(TeaModel):
    def __init__(self, apply_time=None, uid=None):
        self.apply_time = apply_time  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesOrderNode(TeaModel):
    def __init__(self, pay_time=None, uid=None):
        self.pay_time = pay_time  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataNodesOrderNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodesServiceImplementation(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataNodesServiceImplementation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataNodes(TeaModel):
    def __init__(self, doc_node=None, finish_node=None, free_order_audit_node=None, free_order_node=None, name=None,
                 order_date=None, order_node=None, service_implementation=None, status=None):
        self.doc_node = doc_node  # type: GetEnterpriseSupportPlanDetailResponseBodyDataNodesDocNode
        self.finish_node = finish_node  # type: GetEnterpriseSupportPlanDetailResponseBodyDataNodesFinishNode
        self.free_order_audit_node = free_order_audit_node  # type: GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderAuditNode
        self.free_order_node = free_order_node  # type: GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderNode
        self.name = name  # type: str
        self.order_date = order_date  # type: long
        self.order_node = order_node  # type: GetEnterpriseSupportPlanDetailResponseBodyDataNodesOrderNode
        self.service_implementation = service_implementation  # type: GetEnterpriseSupportPlanDetailResponseBodyDataNodesServiceImplementation
        self.status = status  # type: int

    def validate(self):
        if self.doc_node:
            self.doc_node.validate()
        if self.finish_node:
            self.finish_node.validate()
        if self.free_order_audit_node:
            self.free_order_audit_node.validate()
        if self.free_order_node:
            self.free_order_node.validate()
        if self.order_node:
            self.order_node.validate()
        if self.service_implementation:
            self.service_implementation.validate()

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_node is not None:
            result['docNode'] = self.doc_node.to_map()
        if self.finish_node is not None:
            result['finishNode'] = self.finish_node.to_map()
        if self.free_order_audit_node is not None:
            result['freeOrderAuditNode'] = self.free_order_audit_node.to_map()
        if self.free_order_node is not None:
            result['freeOrderNode'] = self.free_order_node.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.order_date is not None:
            result['orderDate'] = self.order_date
        if self.order_node is not None:
            result['orderNode'] = self.order_node.to_map()
        if self.service_implementation is not None:
            result['serviceImplementation'] = self.service_implementation.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docNode') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesDocNode()
            self.doc_node = temp_model.from_map(m['docNode'])
        if m.get('finishNode') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesFinishNode()
            self.finish_node = temp_model.from_map(m['finishNode'])
        if m.get('freeOrderAuditNode') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderAuditNode()
            self.free_order_audit_node = temp_model.from_map(m['freeOrderAuditNode'])
        if m.get('freeOrderNode') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesFreeOrderNode()
            self.free_order_node = temp_model.from_map(m['freeOrderNode'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderDate') is not None:
            self.order_date = m.get('orderDate')
        if m.get('orderNode') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesOrderNode()
            self.order_node = temp_model.from_map(m['orderNode'])
        if m.get('serviceImplementation') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodesServiceImplementation()
            self.service_implementation = temp_model.from_map(m['serviceImplementation'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataServiceItemsOperateList(TeaModel):
    def __init__(self, name=None, name_1=None):
        self.name = name  # type: str
        self.name_1 = name_1  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataServiceItemsOperateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.name_1 is not None:
            result['name1'] = self.name_1
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('name1') is not None:
            self.name_1 = m.get('name1')
        return self


class GetEnterpriseSupportPlanDetailResponseBodyDataServiceItems(TeaModel):
    def __init__(self, content=None, desc=None, name=None, operate_list=None):
        self.content = content  # type: str
        self.desc = desc  # type: str
        self.name = name  # type: str
        self.operate_list = operate_list  # type: list[GetEnterpriseSupportPlanDetailResponseBodyDataServiceItemsOperateList]

    def validate(self):
        if self.operate_list:
            for k in self.operate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyDataServiceItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.desc is not None:
            result['desc'] = self.desc
        if self.name is not None:
            result['name'] = self.name
        result['operateList'] = []
        if self.operate_list is not None:
            for k in self.operate_list:
                result['operateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.operate_list = []
        if m.get('operateList') is not None:
            for k in m.get('operateList'):
                temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataServiceItemsOperateList()
                self.operate_list.append(temp_model.from_map(k))
        return self


class GetEnterpriseSupportPlanDetailResponseBodyData(TeaModel):
    def __init__(self, can_apply_free_order=None, customer_id=None, ding_groups=None, docs=None, end_time=None,
                 first_pay_time=None, free_order_apply_code=None, free_order_apply_id=None, free_order_apply_time=None,
                 free_order_approved_time=None, free_order_expect_start_time=None, instance_id=None, nodes=None, order_ids=None,
                 service_items=None, service_name=None, service_status=None, service_status_name=None, service_type=None,
                 sort_time=None, start_time=None, task_num=None):
        self.can_apply_free_order = can_apply_free_order  # type: bool
        self.customer_id = customer_id  # type: long
        self.ding_groups = ding_groups  # type: list[GetEnterpriseSupportPlanDetailResponseBodyDataDingGroups]
        self.docs = docs  # type: list[GetEnterpriseSupportPlanDetailResponseBodyDataDocs]
        self.end_time = end_time  # type: str
        self.first_pay_time = first_pay_time  # type: str
        self.free_order_apply_code = free_order_apply_code  # type: str
        self.free_order_apply_id = free_order_apply_id  # type: long
        self.free_order_apply_time = free_order_apply_time  # type: str
        self.free_order_approved_time = free_order_approved_time  # type: str
        self.free_order_expect_start_time = free_order_expect_start_time  # type: str
        self.instance_id = instance_id  # type: str
        self.nodes = nodes  # type: list[GetEnterpriseSupportPlanDetailResponseBodyDataNodes]
        self.order_ids = order_ids  # type: list[long]
        self.service_items = service_items  # type: list[GetEnterpriseSupportPlanDetailResponseBodyDataServiceItems]
        self.service_name = service_name  # type: str
        self.service_status = service_status  # type: str
        self.service_status_name = service_status_name  # type: str
        self.service_type = service_type  # type: str
        self.sort_time = sort_time  # type: str
        self.start_time = start_time  # type: str
        self.task_num = task_num  # type: long

    def validate(self):
        if self.ding_groups:
            for k in self.ding_groups:
                if k:
                    k.validate()
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.service_items:
            for k in self.service_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_apply_free_order is not None:
            result['canApplyFreeOrder'] = self.can_apply_free_order
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        result['dingGroups'] = []
        if self.ding_groups is not None:
            for k in self.ding_groups:
                result['dingGroups'].append(k.to_map() if k else None)
        result['docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['docs'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.first_pay_time is not None:
            result['firstPayTime'] = self.first_pay_time
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.free_order_apply_id is not None:
            result['freeOrderApplyId'] = self.free_order_apply_id
        if self.free_order_apply_time is not None:
            result['freeOrderApplyTime'] = self.free_order_apply_time
        if self.free_order_approved_time is not None:
            result['freeOrderApprovedTime'] = self.free_order_approved_time
        if self.free_order_expect_start_time is not None:
            result['freeOrderExpectStartTime'] = self.free_order_expect_start_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        result['serviceItems'] = []
        if self.service_items is not None:
            for k in self.service_items:
                result['serviceItems'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.service_status_name is not None:
            result['serviceStatusName'] = self.service_status_name
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.sort_time is not None:
            result['sortTime'] = self.sort_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.task_num is not None:
            result['taskNum'] = self.task_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('canApplyFreeOrder') is not None:
            self.can_apply_free_order = m.get('canApplyFreeOrder')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        self.ding_groups = []
        if m.get('dingGroups') is not None:
            for k in m.get('dingGroups'):
                temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataDingGroups()
                self.ding_groups.append(temp_model.from_map(k))
        self.docs = []
        if m.get('docs') is not None:
            for k in m.get('docs'):
                temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataDocs()
                self.docs.append(temp_model.from_map(k))
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('firstPayTime') is not None:
            self.first_pay_time = m.get('firstPayTime')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('freeOrderApplyId') is not None:
            self.free_order_apply_id = m.get('freeOrderApplyId')
        if m.get('freeOrderApplyTime') is not None:
            self.free_order_apply_time = m.get('freeOrderApplyTime')
        if m.get('freeOrderApprovedTime') is not None:
            self.free_order_approved_time = m.get('freeOrderApprovedTime')
        if m.get('freeOrderExpectStartTime') is not None:
            self.free_order_expect_start_time = m.get('freeOrderExpectStartTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.nodes = []
        if m.get('nodes') is not None:
            for k in m.get('nodes'):
                temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        self.service_items = []
        if m.get('serviceItems') is not None:
            for k in m.get('serviceItems'):
                temp_model = GetEnterpriseSupportPlanDetailResponseBodyDataServiceItems()
                self.service_items.append(temp_model.from_map(k))
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('serviceStatusName') is not None:
            self.service_status_name = m.get('serviceStatusName')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('sortTime') is not None:
            self.sort_time = m.get('sortTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('taskNum') is not None:
            self.task_num = m.get('taskNum')
        return self


class GetEnterpriseSupportPlanDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetEnterpriseSupportPlanDetailResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetEnterpriseSupportPlanDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetEnterpriseSupportPlanDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEnterpriseSupportPlanDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnterpriseSupportPlanDetailResponse, self).to_map()
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
            temp_model = GetEnterpriseSupportPlanDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPreViewUrlRequest(TeaModel):
    def __init__(self, apply_code=None, file_id=None, file_key=None, order_id=None, scene=None):
        self.apply_code = apply_code  # type: str
        self.file_id = file_id  # type: long
        self.file_key = file_key  # type: str
        self.order_id = order_id  # type: str
        self.scene = scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPreViewUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_code is not None:
            result['applyCode'] = self.apply_code
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_key is not None:
            result['fileKey'] = self.file_key
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileKey') is not None:
            self.file_key = m.get('fileKey')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class GetPreViewUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPreViewUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPreViewUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPreViewUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPreViewUrlResponse, self).to_map()
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
            temp_model = GetPreViewUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceDetailRequest(TeaModel):
    def __init__(self, apply_code=None):
        self.apply_code = apply_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_code is not None:
            result['applyCode'] = self.apply_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')
        return self


class GetServiceDetailResponseBodyDataAppointments(TeaModel):
    def __init__(self, huhang_id=None, purchase_code=None, purchase_desc=None, support_days=None, travel_days=None):
        self.huhang_id = huhang_id  # type: long
        self.purchase_code = purchase_code  # type: int
        self.purchase_desc = purchase_desc  # type: str
        self.support_days = support_days  # type: int
        self.travel_days = travel_days  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataAppointments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.huhang_id is not None:
            result['huhangId'] = self.huhang_id
        if self.purchase_code is not None:
            result['purchaseCode'] = self.purchase_code
        if self.purchase_desc is not None:
            result['purchaseDesc'] = self.purchase_desc
        if self.support_days is not None:
            result['supportDays'] = self.support_days
        if self.travel_days is not None:
            result['travelDays'] = self.travel_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('huhangId') is not None:
            self.huhang_id = m.get('huhangId')
        if m.get('purchaseCode') is not None:
            self.purchase_code = m.get('purchaseCode')
        if m.get('purchaseDesc') is not None:
            self.purchase_desc = m.get('purchaseDesc')
        if m.get('supportDays') is not None:
            self.support_days = m.get('supportDays')
        if m.get('travelDays') is not None:
            self.travel_days = m.get('travelDays')
        return self


class GetServiceDetailResponseBodyDataPayOrders(TeaModel):
    def __init__(self, amount=None, compass_commodity_code=None, compass_commodity_name=None, creator_emp_id=None,
                 gmt_create=None, gmt_modified=None, id=None, modifier_emp_id=None, operate=None, order_detail=None,
                 order_id=None, original_price=None, pay_amount=None, pay_time=None, product_name=None, rene_wal_url=None,
                 service_content_map=None, status=None, status_str=None, support_days=None, uid=None, url=None):
        self.amount = amount  # type: str
        self.compass_commodity_code = compass_commodity_code  # type: str
        self.compass_commodity_name = compass_commodity_name  # type: str
        self.creator_emp_id = creator_emp_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.operate = operate  # type: dict[str, any]
        self.order_detail = order_detail  # type: any
        self.order_id = order_id  # type: long
        self.original_price = original_price  # type: float
        self.pay_amount = pay_amount  # type: float
        self.pay_time = pay_time  # type: str
        self.product_name = product_name  # type: str
        self.rene_wal_url = rene_wal_url  # type: str
        self.service_content_map = service_content_map  # type: dict[str, any]
        self.status = status  # type: int
        self.status_str = status_str  # type: str
        self.support_days = support_days  # type: int
        self.uid = uid  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPayOrders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.compass_commodity_code is not None:
            result['compassCommodityCode'] = self.compass_commodity_code
        if self.compass_commodity_name is not None:
            result['compassCommodityName'] = self.compass_commodity_name
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.operate is not None:
            result['operate'] = self.operate
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.original_price is not None:
            result['originalPrice'] = self.original_price
        if self.pay_amount is not None:
            result['payAmount'] = self.pay_amount
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.rene_wal_url is not None:
            result['reneWalUrl'] = self.rene_wal_url
        if self.service_content_map is not None:
            result['serviceContentMap'] = self.service_content_map
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_days is not None:
            result['supportDays'] = self.support_days
        if self.uid is not None:
            result['uid'] = self.uid
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('compassCommodityCode') is not None:
            self.compass_commodity_code = m.get('compassCommodityCode')
        if m.get('compassCommodityName') is not None:
            self.compass_commodity_name = m.get('compassCommodityName')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('operate') is not None:
            self.operate = m.get('operate')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('originalPrice') is not None:
            self.original_price = m.get('originalPrice')
        if m.get('payAmount') is not None:
            self.pay_amount = m.get('payAmount')
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('reneWalUrl') is not None:
            self.rene_wal_url = m.get('reneWalUrl')
        if m.get('serviceContentMap') is not None:
            self.service_content_map = m.get('serviceContentMap')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportDays') is not None:
            self.support_days = m.get('supportDays')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersApplyFileVOList(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersApplyFileVOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersExtList(TeaModel):
    def __init__(self, key_code=None, name=None, value=None, view=None):
        self.key_code = key_code  # type: str
        self.name = name  # type: str
        self.value = value  # type: any
        self.view = view  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersExtList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformanceNodeDTOS(TeaModel):
    def __init__(self, display=None, extend_info=None, index=None, node_name=None, status=None):
        self.display = display  # type: bool
        self.extend_info = extend_info  # type: any
        self.index = index  # type: int
        self.node_name = node_name  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersPerformanceNodeDTOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksApplyFileVOList(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksApplyFileVOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksExtList(TeaModel):
    def __init__(self, key_code=None, name=None, value=None, view=None):
        self.key_code = key_code  # type: str
        self.name = name  # type: str
        self.value = value  # type: any
        self.view = view  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksExtList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksPerformanceNodeDTOS(TeaModel):
    def __init__(self, display=None, extend_info=None, index=None, node_name=None, status=None):
        self.display = display  # type: bool
        self.extend_info = extend_info  # type: any
        self.index = index  # type: int
        self.node_name = node_name  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksPerformanceNodeDTOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceMonthReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceMonthReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceSchemes(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceSchemes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksTamEngineers(TeaModel):
    def __init__(self, creator_emp_id=None, gmt_create=None, gmt_modified=None, hr_status=None, id=None,
                 last_name=None, modifier_emp_id=None, name=None, nick_name_en=None, realm_id=None, workid=None):
        self.creator_emp_id = creator_emp_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.hr_status = hr_status  # type: str
        self.id = id  # type: long
        self.last_name = last_name  # type: str
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.name = name  # type: str
        self.nick_name_en = nick_name_en  # type: str
        self.realm_id = realm_id  # type: long
        self.workid = workid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksTamEngineers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacks(TeaModel):
    def __init__(self, apply_file_volist=None, appointment_code=None, appointment_end_time=None,
                 appointment_id=None, appointment_pass_time=None, appointment_time=None, commodity_desc=None, creator_emp_id=None,
                 cycle_service=None, ext_list=None, gmt_create=None, gmt_modified=None, id=None,
                 merge_solution_and_reporter_one_step=None, modifier_emp_id=None, order_detail=None, order_id=None, performance_node_dtos=None,
                 purchase_pack_code=None, service_apply_id=None, service_month_reports=None, service_reports=None,
                 service_schemes=None, status=None, status_str=None, support_time=None, tam_engineers=None):
        self.apply_file_volist = apply_file_volist  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksApplyFileVOList]
        self.appointment_code = appointment_code  # type: str
        self.appointment_end_time = appointment_end_time  # type: long
        self.appointment_id = appointment_id  # type: str
        self.appointment_pass_time = appointment_pass_time  # type: long
        self.appointment_time = appointment_time  # type: long
        self.commodity_desc = commodity_desc  # type: str
        self.creator_emp_id = creator_emp_id  # type: str
        self.cycle_service = cycle_service  # type: bool
        self.ext_list = ext_list  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksExtList]
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step  # type: bool
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.order_detail = order_detail  # type: any
        self.order_id = order_id  # type: long
        self.performance_node_dtos = performance_node_dtos  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksPerformanceNodeDTOS]
        self.purchase_pack_code = purchase_pack_code  # type: int
        self.service_apply_id = service_apply_id  # type: long
        self.service_month_reports = service_month_reports  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceMonthReports]
        self.service_reports = service_reports  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceReports]
        self.service_schemes = service_schemes  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceSchemes]
        self.status = status  # type: int
        self.status_str = status_str  # type: str
        self.support_time = support_time  # type: list[long]
        self.tam_engineers = tam_engineers  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksTamEngineers]

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacksTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersServiceMonthReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersServiceMonthReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersServiceReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersServiceReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersServiceSchemes(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersServiceSchemes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrdersTamEngineers(TeaModel):
    def __init__(self, creator_emp_id=None, gmt_create=None, gmt_modified=None, hr_status=None, id=None,
                 last_name=None, modifier_emp_id=None, name=None, nick_name_en=None, realm_id=None, workid=None):
        self.creator_emp_id = creator_emp_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.hr_status = hr_status  # type: str
        self.id = id  # type: long
        self.last_name = last_name  # type: str
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.name = name  # type: str
        self.nick_name_en = nick_name_en  # type: str
        self.realm_id = realm_id  # type: long
        self.workid = workid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrdersTamEngineers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class GetServiceDetailResponseBodyDataPerformanceOrders(TeaModel):
    def __init__(self, apply_file_volist=None, appointment_code=None, appointment_end_time=None,
                 appointment_id=None, appointment_pass_time=None, appointment_time=None, commodity_desc=None, creator_emp_id=None,
                 cycle_service=None, ext_list=None, gmt_create=None, gmt_modified=None, id=None,
                 merge_solution_and_reporter_one_step=None, modifier_emp_id=None, order_detail=None, order_id=None, pack_count=None, pack_details=None,
                 performance_node_dtos=None, performance_packs=None, purchase_pack_code=None, service_apply_id=None,
                 service_month_reports=None, service_reports=None, service_schemes=None, status=None, status_str=None, support_time=None,
                 tam_engineers=None):
        self.apply_file_volist = apply_file_volist  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersApplyFileVOList]
        self.appointment_code = appointment_code  # type: str
        self.appointment_end_time = appointment_end_time  # type: long
        self.appointment_id = appointment_id  # type: str
        self.appointment_pass_time = appointment_pass_time  # type: long
        self.appointment_time = appointment_time  # type: long
        self.commodity_desc = commodity_desc  # type: str
        self.creator_emp_id = creator_emp_id  # type: str
        self.cycle_service = cycle_service  # type: bool
        self.ext_list = ext_list  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersExtList]
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step  # type: bool
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.order_detail = order_detail  # type: any
        self.order_id = order_id  # type: long
        self.pack_count = pack_count  # type: int
        self.pack_details = pack_details  # type: list[dict[str, any]]
        self.performance_node_dtos = performance_node_dtos  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersPerformanceNodeDTOS]
        self.performance_packs = performance_packs  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacks]
        self.purchase_pack_code = purchase_pack_code  # type: int
        self.service_apply_id = service_apply_id  # type: long
        self.service_month_reports = service_month_reports  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersServiceMonthReports]
        self.service_reports = service_reports  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersServiceReports]
        self.service_schemes = service_schemes  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersServiceSchemes]
        self.status = status  # type: int
        self.status_str = status_str  # type: str
        self.support_time = support_time  # type: list[long]
        self.tam_engineers = tam_engineers  # type: list[GetServiceDetailResponseBodyDataPerformanceOrdersTamEngineers]

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.performance_packs:
            for k in self.performance_packs:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformanceOrders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.pack_count is not None:
            result['packCount'] = self.pack_count
        if self.pack_details is not None:
            result['packDetails'] = self.pack_details
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        result['performancePacks'] = []
        if self.performance_packs is not None:
            for k in self.performance_packs:
                result['performancePacks'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('packCount') is not None:
            self.pack_count = m.get('packCount')
        if m.get('packDetails') is not None:
            self.pack_details = m.get('packDetails')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        self.performance_packs = []
        if m.get('performancePacks') is not None:
            for k in m.get('performancePacks'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersPerformancePacks()
                self.performance_packs.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrdersTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class GetServiceDetailResponseBodyDataPerformancePacksApplyFileVOList(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformancePacksApplyFileVOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksExtList(TeaModel):
    def __init__(self, key_code=None, name=None, value=None, view=None):
        self.key_code = key_code  # type: str
        self.name = name  # type: str
        self.value = value  # type: any
        self.view = view  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformancePacksExtList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksPerformanceNodeDTOS(TeaModel):
    def __init__(self, display=None, extend_info=None, index=None, node_name=None, status=None):
        self.display = display  # type: bool
        self.extend_info = extend_info  # type: any
        self.index = index  # type: int
        self.node_name = node_name  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformancePacksPerformanceNodeDTOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksServiceMonthReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformancePacksServiceMonthReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksServiceReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformancePacksServiceReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksServiceSchemes(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformancePacksServiceSchemes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyDataPerformancePacksTamEngineers(TeaModel):
    def __init__(self, creator_emp_id=None, gmt_create=None, gmt_modified=None, hr_status=None, id=None,
                 last_name=None, modifier_emp_id=None, name=None, nick_name_en=None, realm_id=None, workid=None):
        self.creator_emp_id = creator_emp_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.hr_status = hr_status  # type: str
        self.id = id  # type: long
        self.last_name = last_name  # type: str
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.name = name  # type: str
        self.nick_name_en = nick_name_en  # type: str
        self.realm_id = realm_id  # type: long
        self.workid = workid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformancePacksTamEngineers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class GetServiceDetailResponseBodyDataPerformancePacks(TeaModel):
    def __init__(self, apply_file_volist=None, appointment_code=None, appointment_end_time=None,
                 appointment_id=None, appointment_pass_time=None, appointment_time=None, commodity_desc=None, creator_emp_id=None,
                 cycle_service=None, ext_list=None, gmt_create=None, gmt_modified=None, id=None,
                 merge_solution_and_reporter_one_step=None, modifier_emp_id=None, order_detail=None, order_id=None, performance_node_dtos=None,
                 purchase_pack_code=None, service_apply_id=None, service_month_reports=None, service_reports=None,
                 service_schemes=None, status=None, status_str=None, support_time=None, tam_engineers=None):
        self.apply_file_volist = apply_file_volist  # type: list[GetServiceDetailResponseBodyDataPerformancePacksApplyFileVOList]
        self.appointment_code = appointment_code  # type: str
        self.appointment_end_time = appointment_end_time  # type: long
        self.appointment_id = appointment_id  # type: str
        self.appointment_pass_time = appointment_pass_time  # type: long
        self.appointment_time = appointment_time  # type: long
        self.commodity_desc = commodity_desc  # type: str
        self.creator_emp_id = creator_emp_id  # type: str
        self.cycle_service = cycle_service  # type: bool
        self.ext_list = ext_list  # type: list[GetServiceDetailResponseBodyDataPerformancePacksExtList]
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step  # type: bool
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.order_detail = order_detail  # type: any
        self.order_id = order_id  # type: long
        self.performance_node_dtos = performance_node_dtos  # type: list[GetServiceDetailResponseBodyDataPerformancePacksPerformanceNodeDTOS]
        self.purchase_pack_code = purchase_pack_code  # type: int
        self.service_apply_id = service_apply_id  # type: long
        self.service_month_reports = service_month_reports  # type: list[GetServiceDetailResponseBodyDataPerformancePacksServiceMonthReports]
        self.service_reports = service_reports  # type: list[GetServiceDetailResponseBodyDataPerformancePacksServiceReports]
        self.service_schemes = service_schemes  # type: list[GetServiceDetailResponseBodyDataPerformancePacksServiceSchemes]
        self.status = status  # type: int
        self.status_str = status_str  # type: str
        self.support_time = support_time  # type: list[long]
        self.tam_engineers = tam_engineers  # type: list[GetServiceDetailResponseBodyDataPerformancePacksTamEngineers]

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataPerformancePacks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacksTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class GetServiceDetailResponseBodyDataServiceReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyDataServiceReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetServiceDetailResponseBodyData(TeaModel):
    def __init__(self, applier_id=None, apply_code=None, apply_time=None, appointments=None, buy_url=None,
                 creator_emp_id=None, customer_name=None, cycle_service=None, executed_count=None, finish_count=None,
                 form_map=None, gmt_create=None, gmt_modified=None, id=None, merge_solution_and_reporter_one_step=None,
                 modifier_emp_id=None, pack_details=None, pay_orders=None, pay_url=None, performance_orders=None,
                 performance_packs=None, rene_wal_url=None, service_code=None, service_name=None, service_reports=None,
                 service_time_range=None, status=None, status_code=None, status_str=None, term_of_validity=None, total_pack=None,
                 type=None, use_pack=None):
        self.applier_id = applier_id  # type: str
        self.apply_code = apply_code  # type: str
        self.apply_time = apply_time  # type: long
        self.appointments = appointments  # type: list[GetServiceDetailResponseBodyDataAppointments]
        self.buy_url = buy_url  # type: str
        self.creator_emp_id = creator_emp_id  # type: str
        self.customer_name = customer_name  # type: str
        self.cycle_service = cycle_service  # type: bool
        self.executed_count = executed_count  # type: long
        self.finish_count = finish_count  # type: long
        self.form_map = form_map  # type: dict[str, any]
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step  # type: bool
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.pack_details = pack_details  # type: list[dict[str, any]]
        self.pay_orders = pay_orders  # type: list[GetServiceDetailResponseBodyDataPayOrders]
        self.pay_url = pay_url  # type: str
        self.performance_orders = performance_orders  # type: list[GetServiceDetailResponseBodyDataPerformanceOrders]
        self.performance_packs = performance_packs  # type: list[GetServiceDetailResponseBodyDataPerformancePacks]
        self.rene_wal_url = rene_wal_url  # type: str
        self.service_code = service_code  # type: str
        self.service_name = service_name  # type: str
        self.service_reports = service_reports  # type: list[GetServiceDetailResponseBodyDataServiceReports]
        self.service_time_range = service_time_range  # type: list[long]
        self.status = status  # type: str
        self.status_code = status_code  # type: int
        self.status_str = status_str  # type: str
        self.term_of_validity = term_of_validity  # type: str
        self.total_pack = total_pack  # type: int
        self.type = type  # type: str
        self.use_pack = use_pack  # type: long

    def validate(self):
        if self.appointments:
            for k in self.appointments:
                if k:
                    k.validate()
        if self.pay_orders:
            for k in self.pay_orders:
                if k:
                    k.validate()
        if self.performance_orders:
            for k in self.performance_orders:
                if k:
                    k.validate()
        if self.performance_packs:
            for k in self.performance_packs:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applier_id is not None:
            result['applierId'] = self.applier_id
        if self.apply_code is not None:
            result['applyCode'] = self.apply_code
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        result['appointments'] = []
        if self.appointments is not None:
            for k in self.appointments:
                result['appointments'].append(k.to_map() if k else None)
        if self.buy_url is not None:
            result['buyUrl'] = self.buy_url
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.customer_name is not None:
            result['customerName'] = self.customer_name
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        if self.executed_count is not None:
            result['executedCount'] = self.executed_count
        if self.finish_count is not None:
            result['finishCount'] = self.finish_count
        if self.form_map is not None:
            result['formMap'] = self.form_map
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.pack_details is not None:
            result['packDetails'] = self.pack_details
        result['payOrders'] = []
        if self.pay_orders is not None:
            for k in self.pay_orders:
                result['payOrders'].append(k.to_map() if k else None)
        if self.pay_url is not None:
            result['payUrl'] = self.pay_url
        result['performanceOrders'] = []
        if self.performance_orders is not None:
            for k in self.performance_orders:
                result['performanceOrders'].append(k.to_map() if k else None)
        result['performancePacks'] = []
        if self.performance_packs is not None:
            for k in self.performance_packs:
                result['performancePacks'].append(k.to_map() if k else None)
        if self.rene_wal_url is not None:
            result['reneWalUrl'] = self.rene_wal_url
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        if self.service_time_range is not None:
            result['serviceTimeRange'] = self.service_time_range
        if self.status is not None:
            result['status'] = self.status
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.term_of_validity is not None:
            result['termOfValidity'] = self.term_of_validity
        if self.total_pack is not None:
            result['totalPack'] = self.total_pack
        if self.type is not None:
            result['type'] = self.type
        if self.use_pack is not None:
            result['usePack'] = self.use_pack
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applierId') is not None:
            self.applier_id = m.get('applierId')
        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        self.appointments = []
        if m.get('appointments') is not None:
            for k in m.get('appointments'):
                temp_model = GetServiceDetailResponseBodyDataAppointments()
                self.appointments.append(temp_model.from_map(k))
        if m.get('buyUrl') is not None:
            self.buy_url = m.get('buyUrl')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('customerName') is not None:
            self.customer_name = m.get('customerName')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        if m.get('executedCount') is not None:
            self.executed_count = m.get('executedCount')
        if m.get('finishCount') is not None:
            self.finish_count = m.get('finishCount')
        if m.get('formMap') is not None:
            self.form_map = m.get('formMap')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('packDetails') is not None:
            self.pack_details = m.get('packDetails')
        self.pay_orders = []
        if m.get('payOrders') is not None:
            for k in m.get('payOrders'):
                temp_model = GetServiceDetailResponseBodyDataPayOrders()
                self.pay_orders.append(temp_model.from_map(k))
        if m.get('payUrl') is not None:
            self.pay_url = m.get('payUrl')
        self.performance_orders = []
        if m.get('performanceOrders') is not None:
            for k in m.get('performanceOrders'):
                temp_model = GetServiceDetailResponseBodyDataPerformanceOrders()
                self.performance_orders.append(temp_model.from_map(k))
        self.performance_packs = []
        if m.get('performancePacks') is not None:
            for k in m.get('performancePacks'):
                temp_model = GetServiceDetailResponseBodyDataPerformancePacks()
                self.performance_packs.append(temp_model.from_map(k))
        if m.get('reneWalUrl') is not None:
            self.rene_wal_url = m.get('reneWalUrl')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = GetServiceDetailResponseBodyDataServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        if m.get('serviceTimeRange') is not None:
            self.service_time_range = m.get('serviceTimeRange')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('termOfValidity') is not None:
            self.term_of_validity = m.get('termOfValidity')
        if m.get('totalPack') is not None:
            self.total_pack = m.get('totalPack')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('usePack') is not None:
            self.use_pack = m.get('usePack')
        return self


class GetServiceDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetServiceDetailResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetServiceDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetServiceDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetServiceDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServiceDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceDetailResponse, self).to_map()
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
            temp_model = GetServiceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetYunQiTaskByRecordIdRequest(TeaModel):
    def __init__(self, record_id=None):
        self.record_id = record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetYunQiTaskByRecordIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['recordId'] = self.record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        return self


class GetYunQiTaskByRecordIdResponseBodyData(TeaModel):
    def __init__(self, chat_id=None, create_time=None, creator_name=None, end_time=None, evaluation_star=None,
                 important=None, main_ding_department_id=None, main_ding_group_id=None, main_ding_group_name=None,
                 product_name=None, record_id=None, status=None, sub_ding_department_id=None, sub_ding_group_id=None,
                 sub_ding_group_name=None, title=None):
        self.chat_id = chat_id  # type: str
        self.create_time = create_time  # type: long
        self.creator_name = creator_name  # type: str
        self.end_time = end_time  # type: long
        self.evaluation_star = evaluation_star  # type: int
        self.important = important  # type: str
        self.main_ding_department_id = main_ding_department_id  # type: str
        self.main_ding_group_id = main_ding_group_id  # type: str
        self.main_ding_group_name = main_ding_group_name  # type: str
        self.product_name = product_name  # type: str
        self.record_id = record_id  # type: str
        self.status = status  # type: str
        self.sub_ding_department_id = sub_ding_department_id  # type: str
        self.sub_ding_group_id = sub_ding_group_id  # type: str
        self.sub_ding_group_name = sub_ding_group_name  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetYunQiTaskByRecordIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.evaluation_star is not None:
            result['evaluationStar'] = self.evaluation_star
        if self.important is not None:
            result['important'] = self.important
        if self.main_ding_department_id is not None:
            result['mainDingDepartmentId'] = self.main_ding_department_id
        if self.main_ding_group_id is not None:
            result['mainDingGroupId'] = self.main_ding_group_id
        if self.main_ding_group_name is not None:
            result['mainDingGroupName'] = self.main_ding_group_name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.status is not None:
            result['status'] = self.status
        if self.sub_ding_department_id is not None:
            result['subDingDepartmentId'] = self.sub_ding_department_id
        if self.sub_ding_group_id is not None:
            result['subDingGroupId'] = self.sub_ding_group_id
        if self.sub_ding_group_name is not None:
            result['subDingGroupName'] = self.sub_ding_group_name
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('evaluationStar') is not None:
            self.evaluation_star = m.get('evaluationStar')
        if m.get('important') is not None:
            self.important = m.get('important')
        if m.get('mainDingDepartmentId') is not None:
            self.main_ding_department_id = m.get('mainDingDepartmentId')
        if m.get('mainDingGroupId') is not None:
            self.main_ding_group_id = m.get('mainDingGroupId')
        if m.get('mainDingGroupName') is not None:
            self.main_ding_group_name = m.get('mainDingGroupName')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subDingDepartmentId') is not None:
            self.sub_ding_department_id = m.get('subDingDepartmentId')
        if m.get('subDingGroupId') is not None:
            self.sub_ding_group_id = m.get('subDingGroupId')
        if m.get('subDingGroupName') is not None:
            self.sub_ding_group_name = m.get('subDingGroupName')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetYunQiTaskByRecordIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetYunQiTaskByRecordIdResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetYunQiTaskByRecordIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetYunQiTaskByRecordIdResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetYunQiTaskByRecordIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetYunQiTaskByRecordIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetYunQiTaskByRecordIdResponse, self).to_map()
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
            temp_model = GetYunQiTaskByRecordIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDocsGroupByYearRequest(TeaModel):
    def __init__(self, apply_codes=None, file_name_keyword=None, order_ids=None, product_code=None, scene=None):
        self.apply_codes = apply_codes  # type: list[str]
        self.file_name_keyword = file_name_keyword  # type: str
        self.order_ids = order_ids  # type: list[long]
        self.product_code = product_code  # type: str
        self.scene = scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDocsGroupByYearRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_codes is not None:
            result['applyCodes'] = self.apply_codes
        if self.file_name_keyword is not None:
            result['fileNameKeyword'] = self.file_name_keyword
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applyCodes') is not None:
            self.apply_codes = m.get('applyCodes')
        if m.get('fileNameKeyword') is not None:
            self.file_name_keyword = m.get('fileNameKeyword')
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class ListDocsGroupByYearResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: dict[str, list[DataValue]]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for v in self.data.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(ListDocsGroupByYearResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = {}
        if self.data is not None:
            for k, v in self.data.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['data'][k] = l1
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = {}
        if m.get('data') is not None:
            for k, v in m.get('data').items():
                l1 = []
                for k1 in v:
                    temp_model = DataValue()
                    l1.append(temp_model.from_map(k1))
                self.data['k'] = l1
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListDocsGroupByYearResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDocsGroupByYearResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDocsGroupByYearResponse, self).to_map()
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
            temp_model = ListDocsGroupByYearResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnterpriseSupportPlanRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanRequest, self).to_map()
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


class ListEnterpriseSupportPlanResponseBodyDataDocs(TeaModel):
    def __init__(self, doc_id=None, file_name=None, free_order_apply_code=None, name=None, order_id=None,
                 upload_time=None, url=None):
        self.doc_id = doc_id  # type: long
        self.file_name = file_name  # type: str
        self.free_order_apply_code = free_order_apply_code  # type: str
        self.name = name  # type: str
        self.order_id = order_id  # type: str
        self.upload_time = upload_time  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBodyDataDocs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.name is not None:
            result['name'] = self.name
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesDocNode(TeaModel):
    def __init__(self, doc_id=None, doc_name=None, doc_submit_time=None, file_name=None, free_order_apply_code=None,
                 order_id=None):
        self.doc_id = doc_id  # type: long
        self.doc_name = doc_name  # type: str
        self.doc_submit_time = doc_submit_time  # type: str
        self.file_name = file_name  # type: str
        self.free_order_apply_code = free_order_apply_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBodyDataNodesDocNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.doc_name is not None:
            result['docName'] = self.doc_name
        if self.doc_submit_time is not None:
            result['docSubmitTime'] = self.doc_submit_time
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('docName') is not None:
            self.doc_name = m.get('docName')
        if m.get('docSubmitTime') is not None:
            self.doc_submit_time = m.get('docSubmitTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesFinishNode(TeaModel):
    def __init__(self, finish_time=None):
        self.finish_time = finish_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBodyDataNodesFinishNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderAuditNode(TeaModel):
    def __init__(self, audit_time=None, status=None, status_name=None):
        self.audit_time = audit_time  # type: str
        self.status = status  # type: str
        self.status_name = status_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderAuditNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_time is not None:
            result['auditTime'] = self.audit_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_name is not None:
            result['statusName'] = self.status_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auditTime') is not None:
            self.audit_time = m.get('auditTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusName') is not None:
            self.status_name = m.get('statusName')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderNode(TeaModel):
    def __init__(self, apply_time=None, uid=None):
        self.apply_time = apply_time  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesOrderNode(TeaModel):
    def __init__(self, pay_time=None, uid=None):
        self.pay_time = pay_time  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBodyDataNodesOrderNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodesServiceImplementation(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBodyDataNodesServiceImplementation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListEnterpriseSupportPlanResponseBodyDataNodes(TeaModel):
    def __init__(self, doc_node=None, finish_node=None, free_order_audit_node=None, free_order_node=None, name=None,
                 order_date=None, order_node=None, service_implementation=None, status=None):
        self.doc_node = doc_node  # type: ListEnterpriseSupportPlanResponseBodyDataNodesDocNode
        self.finish_node = finish_node  # type: ListEnterpriseSupportPlanResponseBodyDataNodesFinishNode
        self.free_order_audit_node = free_order_audit_node  # type: ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderAuditNode
        self.free_order_node = free_order_node  # type: ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderNode
        self.name = name  # type: str
        self.order_date = order_date  # type: long
        self.order_node = order_node  # type: ListEnterpriseSupportPlanResponseBodyDataNodesOrderNode
        self.service_implementation = service_implementation  # type: ListEnterpriseSupportPlanResponseBodyDataNodesServiceImplementation
        self.status = status  # type: int

    def validate(self):
        if self.doc_node:
            self.doc_node.validate()
        if self.finish_node:
            self.finish_node.validate()
        if self.free_order_audit_node:
            self.free_order_audit_node.validate()
        if self.free_order_node:
            self.free_order_node.validate()
        if self.order_node:
            self.order_node.validate()
        if self.service_implementation:
            self.service_implementation.validate()

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBodyDataNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_node is not None:
            result['docNode'] = self.doc_node.to_map()
        if self.finish_node is not None:
            result['finishNode'] = self.finish_node.to_map()
        if self.free_order_audit_node is not None:
            result['freeOrderAuditNode'] = self.free_order_audit_node.to_map()
        if self.free_order_node is not None:
            result['freeOrderNode'] = self.free_order_node.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.order_date is not None:
            result['orderDate'] = self.order_date
        if self.order_node is not None:
            result['orderNode'] = self.order_node.to_map()
        if self.service_implementation is not None:
            result['serviceImplementation'] = self.service_implementation.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docNode') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesDocNode()
            self.doc_node = temp_model.from_map(m['docNode'])
        if m.get('finishNode') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesFinishNode()
            self.finish_node = temp_model.from_map(m['finishNode'])
        if m.get('freeOrderAuditNode') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderAuditNode()
            self.free_order_audit_node = temp_model.from_map(m['freeOrderAuditNode'])
        if m.get('freeOrderNode') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesFreeOrderNode()
            self.free_order_node = temp_model.from_map(m['freeOrderNode'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderDate') is not None:
            self.order_date = m.get('orderDate')
        if m.get('orderNode') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesOrderNode()
            self.order_node = temp_model.from_map(m['orderNode'])
        if m.get('serviceImplementation') is not None:
            temp_model = ListEnterpriseSupportPlanResponseBodyDataNodesServiceImplementation()
            self.service_implementation = temp_model.from_map(m['serviceImplementation'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListEnterpriseSupportPlanResponseBodyDataOperateInfos(TeaModel):
    def __init__(self, can_click=None, text=None, url=None):
        self.can_click = can_click  # type: bool
        self.text = text  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBodyDataOperateInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_click is not None:
            result['canClick'] = self.can_click
        if self.text is not None:
            result['text'] = self.text
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('canClick') is not None:
            self.can_click = m.get('canClick')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEnterpriseSupportPlanResponseBodyData(TeaModel):
    def __init__(self, can_apply_free_order=None, customer_id=None, docs=None, end_time=None, first_pay_time=None,
                 free_order_apply_code=None, free_order_apply_id=None, free_order_apply_time=None, free_order_approved_time=None,
                 free_order_expect_start_time=None, instance_id=None, nodes=None, operate_infos=None, order_ids=None, service_name=None,
                 service_status=None, service_status_name=None, service_type=None, sort_time=None, start_time=None, task_num=None):
        self.can_apply_free_order = can_apply_free_order  # type: bool
        self.customer_id = customer_id  # type: long
        self.docs = docs  # type: list[ListEnterpriseSupportPlanResponseBodyDataDocs]
        self.end_time = end_time  # type: str
        self.first_pay_time = first_pay_time  # type: str
        self.free_order_apply_code = free_order_apply_code  # type: str
        self.free_order_apply_id = free_order_apply_id  # type: long
        self.free_order_apply_time = free_order_apply_time  # type: str
        self.free_order_approved_time = free_order_approved_time  # type: str
        self.free_order_expect_start_time = free_order_expect_start_time  # type: str
        self.instance_id = instance_id  # type: str
        self.nodes = nodes  # type: list[ListEnterpriseSupportPlanResponseBodyDataNodes]
        self.operate_infos = operate_infos  # type: list[ListEnterpriseSupportPlanResponseBodyDataOperateInfos]
        self.order_ids = order_ids  # type: list[long]
        self.service_name = service_name  # type: str
        self.service_status = service_status  # type: str
        self.service_status_name = service_status_name  # type: str
        self.service_type = service_type  # type: str
        self.sort_time = sort_time  # type: str
        self.start_time = start_time  # type: str
        self.task_num = task_num  # type: long

    def validate(self):
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.operate_infos:
            for k in self.operate_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_apply_free_order is not None:
            result['canApplyFreeOrder'] = self.can_apply_free_order
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        result['docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['docs'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.first_pay_time is not None:
            result['firstPayTime'] = self.first_pay_time
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.free_order_apply_id is not None:
            result['freeOrderApplyId'] = self.free_order_apply_id
        if self.free_order_apply_time is not None:
            result['freeOrderApplyTime'] = self.free_order_apply_time
        if self.free_order_approved_time is not None:
            result['freeOrderApprovedTime'] = self.free_order_approved_time
        if self.free_order_expect_start_time is not None:
            result['freeOrderExpectStartTime'] = self.free_order_expect_start_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        result['operateInfos'] = []
        if self.operate_infos is not None:
            for k in self.operate_infos:
                result['operateInfos'].append(k.to_map() if k else None)
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.service_status_name is not None:
            result['serviceStatusName'] = self.service_status_name
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.sort_time is not None:
            result['sortTime'] = self.sort_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.task_num is not None:
            result['taskNum'] = self.task_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('canApplyFreeOrder') is not None:
            self.can_apply_free_order = m.get('canApplyFreeOrder')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        self.docs = []
        if m.get('docs') is not None:
            for k in m.get('docs'):
                temp_model = ListEnterpriseSupportPlanResponseBodyDataDocs()
                self.docs.append(temp_model.from_map(k))
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('firstPayTime') is not None:
            self.first_pay_time = m.get('firstPayTime')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('freeOrderApplyId') is not None:
            self.free_order_apply_id = m.get('freeOrderApplyId')
        if m.get('freeOrderApplyTime') is not None:
            self.free_order_apply_time = m.get('freeOrderApplyTime')
        if m.get('freeOrderApprovedTime') is not None:
            self.free_order_approved_time = m.get('freeOrderApprovedTime')
        if m.get('freeOrderExpectStartTime') is not None:
            self.free_order_expect_start_time = m.get('freeOrderExpectStartTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.nodes = []
        if m.get('nodes') is not None:
            for k in m.get('nodes'):
                temp_model = ListEnterpriseSupportPlanResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k))
        self.operate_infos = []
        if m.get('operateInfos') is not None:
            for k in m.get('operateInfos'):
                temp_model = ListEnterpriseSupportPlanResponseBodyDataOperateInfos()
                self.operate_infos.append(temp_model.from_map(k))
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('serviceStatusName') is not None:
            self.service_status_name = m.get('serviceStatusName')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('sortTime') is not None:
            self.sort_time = m.get('sortTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('taskNum') is not None:
            self.task_num = m.get('taskNum')
        return self


class ListEnterpriseSupportPlanResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListEnterpriseSupportPlanResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListEnterpriseSupportPlanResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnterpriseSupportPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEnterpriseSupportPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanResponse, self).to_map()
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
            temp_model = ListEnterpriseSupportPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnterpriseSupportPlanSimpleRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleRequest, self).to_map()
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


class ListEnterpriseSupportPlanSimpleResponseBodyDataDocs(TeaModel):
    def __init__(self, doc_id=None, file_name=None, free_order_apply_code=None, name=None, order_id=None,
                 upload_time=None, url=None):
        self.doc_id = doc_id  # type: long
        self.file_name = file_name  # type: str
        self.free_order_apply_code = free_order_apply_code  # type: str
        self.name = name  # type: str
        self.order_id = order_id  # type: str
        self.upload_time = upload_time  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponseBodyDataDocs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.name is not None:
            result['name'] = self.name
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesDocNode(TeaModel):
    def __init__(self, doc_id=None, doc_name=None, doc_submit_time=None, file_name=None, free_order_apply_code=None,
                 order_id=None):
        self.doc_id = doc_id  # type: long
        self.doc_name = doc_name  # type: str
        self.doc_submit_time = doc_submit_time  # type: str
        self.file_name = file_name  # type: str
        self.free_order_apply_code = free_order_apply_code  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponseBodyDataNodesDocNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.doc_name is not None:
            result['docName'] = self.doc_name
        if self.doc_submit_time is not None:
            result['docSubmitTime'] = self.doc_submit_time
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('docName') is not None:
            self.doc_name = m.get('docName')
        if m.get('docSubmitTime') is not None:
            self.doc_submit_time = m.get('docSubmitTime')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFinishNode(TeaModel):
    def __init__(self, finish_time=None):
        self.finish_time = finish_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFinishNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderAuditNode(TeaModel):
    def __init__(self, audit_time=None, status=None, status_name=None):
        self.audit_time = audit_time  # type: str
        self.status = status  # type: str
        self.status_name = status_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderAuditNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_time is not None:
            result['auditTime'] = self.audit_time
        if self.status is not None:
            result['status'] = self.status
        if self.status_name is not None:
            result['statusName'] = self.status_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auditTime') is not None:
            self.audit_time = m.get('auditTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusName') is not None:
            self.status_name = m.get('statusName')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderNode(TeaModel):
    def __init__(self, apply_time=None, uid=None):
        self.apply_time = apply_time  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesOrderNode(TeaModel):
    def __init__(self, pay_time=None, uid=None):
        self.pay_time = pay_time  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponseBodyDataNodesOrderNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodesServiceImplementation(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponseBodyDataNodesServiceImplementation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyDataNodes(TeaModel):
    def __init__(self, doc_node=None, finish_node=None, free_order_audit_node=None, free_order_node=None, name=None,
                 order_date=None, order_node=None, service_implementation=None, status=None):
        self.doc_node = doc_node  # type: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesDocNode
        self.finish_node = finish_node  # type: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFinishNode
        self.free_order_audit_node = free_order_audit_node  # type: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderAuditNode
        self.free_order_node = free_order_node  # type: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderNode
        self.name = name  # type: str
        self.order_date = order_date  # type: long
        self.order_node = order_node  # type: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesOrderNode
        self.service_implementation = service_implementation  # type: ListEnterpriseSupportPlanSimpleResponseBodyDataNodesServiceImplementation
        self.status = status  # type: int

    def validate(self):
        if self.doc_node:
            self.doc_node.validate()
        if self.finish_node:
            self.finish_node.validate()
        if self.free_order_audit_node:
            self.free_order_audit_node.validate()
        if self.free_order_node:
            self.free_order_node.validate()
        if self.order_node:
            self.order_node.validate()
        if self.service_implementation:
            self.service_implementation.validate()

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponseBodyDataNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_node is not None:
            result['docNode'] = self.doc_node.to_map()
        if self.finish_node is not None:
            result['finishNode'] = self.finish_node.to_map()
        if self.free_order_audit_node is not None:
            result['freeOrderAuditNode'] = self.free_order_audit_node.to_map()
        if self.free_order_node is not None:
            result['freeOrderNode'] = self.free_order_node.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.order_date is not None:
            result['orderDate'] = self.order_date
        if self.order_node is not None:
            result['orderNode'] = self.order_node.to_map()
        if self.service_implementation is not None:
            result['serviceImplementation'] = self.service_implementation.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docNode') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesDocNode()
            self.doc_node = temp_model.from_map(m['docNode'])
        if m.get('finishNode') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFinishNode()
            self.finish_node = temp_model.from_map(m['finishNode'])
        if m.get('freeOrderAuditNode') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderAuditNode()
            self.free_order_audit_node = temp_model.from_map(m['freeOrderAuditNode'])
        if m.get('freeOrderNode') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesFreeOrderNode()
            self.free_order_node = temp_model.from_map(m['freeOrderNode'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('orderDate') is not None:
            self.order_date = m.get('orderDate')
        if m.get('orderNode') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesOrderNode()
            self.order_node = temp_model.from_map(m['orderNode'])
        if m.get('serviceImplementation') is not None:
            temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodesServiceImplementation()
            self.service_implementation = temp_model.from_map(m['serviceImplementation'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListEnterpriseSupportPlanSimpleResponseBodyData(TeaModel):
    def __init__(self, can_apply_free_order=None, customer_id=None, docs=None, end_time=None, first_pay_time=None,
                 free_order_apply_code=None, free_order_apply_id=None, free_order_apply_time=None, free_order_approved_time=None,
                 free_order_expect_start_time=None, instance_id=None, nodes=None, order_ids=None, service_name=None, service_status=None,
                 service_status_name=None, service_type=None, sort_time=None, start_time=None, task_num=None):
        self.can_apply_free_order = can_apply_free_order  # type: bool
        self.customer_id = customer_id  # type: long
        self.docs = docs  # type: list[ListEnterpriseSupportPlanSimpleResponseBodyDataDocs]
        self.end_time = end_time  # type: str
        self.first_pay_time = first_pay_time  # type: str
        self.free_order_apply_code = free_order_apply_code  # type: str
        self.free_order_apply_id = free_order_apply_id  # type: long
        self.free_order_apply_time = free_order_apply_time  # type: str
        self.free_order_approved_time = free_order_approved_time  # type: str
        self.free_order_expect_start_time = free_order_expect_start_time  # type: str
        self.instance_id = instance_id  # type: str
        self.nodes = nodes  # type: list[ListEnterpriseSupportPlanSimpleResponseBodyDataNodes]
        self.order_ids = order_ids  # type: list[long]
        self.service_name = service_name  # type: str
        self.service_status = service_status  # type: str
        self.service_status_name = service_status_name  # type: str
        self.service_type = service_type  # type: str
        self.sort_time = sort_time  # type: str
        self.start_time = start_time  # type: str
        self.task_num = task_num  # type: long

    def validate(self):
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_apply_free_order is not None:
            result['canApplyFreeOrder'] = self.can_apply_free_order
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        result['docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['docs'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.first_pay_time is not None:
            result['firstPayTime'] = self.first_pay_time
        if self.free_order_apply_code is not None:
            result['freeOrderApplyCode'] = self.free_order_apply_code
        if self.free_order_apply_id is not None:
            result['freeOrderApplyId'] = self.free_order_apply_id
        if self.free_order_apply_time is not None:
            result['freeOrderApplyTime'] = self.free_order_apply_time
        if self.free_order_approved_time is not None:
            result['freeOrderApprovedTime'] = self.free_order_approved_time
        if self.free_order_expect_start_time is not None:
            result['freeOrderExpectStartTime'] = self.free_order_expect_start_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        result['nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.service_status_name is not None:
            result['serviceStatusName'] = self.service_status_name
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.sort_time is not None:
            result['sortTime'] = self.sort_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.task_num is not None:
            result['taskNum'] = self.task_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('canApplyFreeOrder') is not None:
            self.can_apply_free_order = m.get('canApplyFreeOrder')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        self.docs = []
        if m.get('docs') is not None:
            for k in m.get('docs'):
                temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataDocs()
                self.docs.append(temp_model.from_map(k))
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('firstPayTime') is not None:
            self.first_pay_time = m.get('firstPayTime')
        if m.get('freeOrderApplyCode') is not None:
            self.free_order_apply_code = m.get('freeOrderApplyCode')
        if m.get('freeOrderApplyId') is not None:
            self.free_order_apply_id = m.get('freeOrderApplyId')
        if m.get('freeOrderApplyTime') is not None:
            self.free_order_apply_time = m.get('freeOrderApplyTime')
        if m.get('freeOrderApprovedTime') is not None:
            self.free_order_approved_time = m.get('freeOrderApprovedTime')
        if m.get('freeOrderExpectStartTime') is not None:
            self.free_order_expect_start_time = m.get('freeOrderExpectStartTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        self.nodes = []
        if m.get('nodes') is not None:
            for k in m.get('nodes'):
                temp_model = ListEnterpriseSupportPlanSimpleResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('serviceStatusName') is not None:
            self.service_status_name = m.get('serviceStatusName')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('sortTime') is not None:
            self.sort_time = m.get('sortTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('taskNum') is not None:
            self.task_num = m.get('taskNum')
        return self


class ListEnterpriseSupportPlanSimpleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListEnterpriseSupportPlanSimpleResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListEnterpriseSupportPlanSimpleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnterpriseSupportPlanSimpleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEnterpriseSupportPlanSimpleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnterpriseSupportPlanSimpleResponse, self).to_map()
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
            temp_model = ListEnterpriseSupportPlanSimpleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceApplyRequest(TeaModel):
    def __init__(self, apply_type=None, end_date=None, page_num=None, page_size=None, product_code=None,
                 start_date=None, status=None):
        self.apply_type = apply_type  # type: list[str]
        self.end_date = end_date  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.product_code = product_code  # type: int
        self.start_date = start_date  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_type is not None:
            result['applyType'] = self.apply_type
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applyType') is not None:
            self.apply_type = m.get('applyType')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListServiceApplyResponseBodyDataListAppointments(TeaModel):
    def __init__(self, huhang_id=None, purchase_code=None, purchase_desc=None, support_days=None, travel_days=None):
        self.huhang_id = huhang_id  # type: long
        self.purchase_code = purchase_code  # type: int
        self.purchase_desc = purchase_desc  # type: str
        self.support_days = support_days  # type: int
        self.travel_days = travel_days  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListAppointments, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.huhang_id is not None:
            result['huhangId'] = self.huhang_id
        if self.purchase_code is not None:
            result['purchaseCode'] = self.purchase_code
        if self.purchase_desc is not None:
            result['purchaseDesc'] = self.purchase_desc
        if self.support_days is not None:
            result['supportDays'] = self.support_days
        if self.travel_days is not None:
            result['travelDays'] = self.travel_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('huhangId') is not None:
            self.huhang_id = m.get('huhangId')
        if m.get('purchaseCode') is not None:
            self.purchase_code = m.get('purchaseCode')
        if m.get('purchaseDesc') is not None:
            self.purchase_desc = m.get('purchaseDesc')
        if m.get('supportDays') is not None:
            self.support_days = m.get('supportDays')
        if m.get('travelDays') is not None:
            self.travel_days = m.get('travelDays')
        return self


class ListServiceApplyResponseBodyDataListPayOrders(TeaModel):
    def __init__(self, amount=None, compass_commodity_code=None, compass_commodity_name=None, creator_emp_id=None,
                 gmt_create=None, gmt_modified=None, id=None, modifier_emp_id=None, operate=None, order_detail=None,
                 order_id=None, original_price=None, pay_amount=None, pay_time=None, product_name=None, rene_wal_url=None,
                 service_content_map=None, status=None, status_str=None, support_days=None, uid=None, url=None):
        self.amount = amount  # type: str
        self.compass_commodity_code = compass_commodity_code  # type: str
        self.compass_commodity_name = compass_commodity_name  # type: str
        self.creator_emp_id = creator_emp_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.operate = operate  # type: dict[str, any]
        self.order_detail = order_detail  # type: any
        self.order_id = order_id  # type: long
        self.original_price = original_price  # type: float
        self.pay_amount = pay_amount  # type: float
        self.pay_time = pay_time  # type: str
        self.product_name = product_name  # type: str
        self.rene_wal_url = rene_wal_url  # type: str
        self.service_content_map = service_content_map  # type: dict[str, any]
        self.status = status  # type: int
        self.status_str = status_str  # type: str
        self.support_days = support_days  # type: int
        self.uid = uid  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPayOrders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.compass_commodity_code is not None:
            result['compassCommodityCode'] = self.compass_commodity_code
        if self.compass_commodity_name is not None:
            result['compassCommodityName'] = self.compass_commodity_name
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.operate is not None:
            result['operate'] = self.operate
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.original_price is not None:
            result['originalPrice'] = self.original_price
        if self.pay_amount is not None:
            result['payAmount'] = self.pay_amount
        if self.pay_time is not None:
            result['payTime'] = self.pay_time
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.rene_wal_url is not None:
            result['reneWalUrl'] = self.rene_wal_url
        if self.service_content_map is not None:
            result['serviceContentMap'] = self.service_content_map
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_days is not None:
            result['supportDays'] = self.support_days
        if self.uid is not None:
            result['uid'] = self.uid
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('compassCommodityCode') is not None:
            self.compass_commodity_code = m.get('compassCommodityCode')
        if m.get('compassCommodityName') is not None:
            self.compass_commodity_name = m.get('compassCommodityName')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('operate') is not None:
            self.operate = m.get('operate')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('originalPrice') is not None:
            self.original_price = m.get('originalPrice')
        if m.get('payAmount') is not None:
            self.pay_amount = m.get('payAmount')
        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('reneWalUrl') is not None:
            self.rene_wal_url = m.get('reneWalUrl')
        if m.get('serviceContentMap') is not None:
            self.service_content_map = m.get('serviceContentMap')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportDays') is not None:
            self.support_days = m.get('supportDays')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersApplyFileVOList(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersApplyFileVOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersExtList(TeaModel):
    def __init__(self, key_code=None, name=None, value=None, view=None):
        self.key_code = key_code  # type: str
        self.name = name  # type: str
        self.value = value  # type: any
        self.view = view  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersExtList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformanceNodeDTOS(TeaModel):
    def __init__(self, display=None, extend_info=None, index=None, node_name=None, status=None):
        self.display = display  # type: bool
        self.extend_info = extend_info  # type: any
        self.index = index  # type: int
        self.node_name = node_name  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersPerformanceNodeDTOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksApplyFileVOList(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksApplyFileVOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksExtList(TeaModel):
    def __init__(self, key_code=None, name=None, value=None, view=None):
        self.key_code = key_code  # type: str
        self.name = name  # type: str
        self.value = value  # type: any
        self.view = view  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksExtList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksPerformanceNodeDTOS(TeaModel):
    def __init__(self, display=None, extend_info=None, index=None, node_name=None, status=None):
        self.display = display  # type: bool
        self.extend_info = extend_info  # type: any
        self.index = index  # type: int
        self.node_name = node_name  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksPerformanceNodeDTOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceMonthReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceMonthReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceSchemes(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceSchemes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksTamEngineers(TeaModel):
    def __init__(self, creator_emp_id=None, gmt_create=None, gmt_modified=None, hr_status=None, id=None,
                 last_name=None, modifier_emp_id=None, name=None, nick_name_en=None, realm_id=None, workid=None):
        self.creator_emp_id = creator_emp_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.hr_status = hr_status  # type: str
        self.id = id  # type: long
        self.last_name = last_name  # type: str
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.name = name  # type: str
        self.nick_name_en = nick_name_en  # type: str
        self.realm_id = realm_id  # type: long
        self.workid = workid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksTamEngineers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacks(TeaModel):
    def __init__(self, apply_file_volist=None, appointment_code=None, appointment_end_time=None,
                 appointment_id=None, appointment_pass_time=None, appointment_time=None, commodity_desc=None, creator_emp_id=None,
                 cycle_service=None, ext_list=None, gmt_create=None, gmt_modified=None, id=None,
                 merge_solution_and_reporter_one_step=None, modifier_emp_id=None, ntm_commodity_code=None, order_detail=None, order_id=None,
                 performance_node_dtos=None, purchase_pack_code=None, service_apply_id=None, service_month_reports=None,
                 service_reports=None, service_schemes=None, status=None, status_str=None, support_time=None, tam_engineers=None):
        self.apply_file_volist = apply_file_volist  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksApplyFileVOList]
        self.appointment_code = appointment_code  # type: str
        self.appointment_end_time = appointment_end_time  # type: long
        self.appointment_id = appointment_id  # type: str
        self.appointment_pass_time = appointment_pass_time  # type: long
        self.appointment_time = appointment_time  # type: long
        self.commodity_desc = commodity_desc  # type: str
        self.creator_emp_id = creator_emp_id  # type: str
        self.cycle_service = cycle_service  # type: bool
        self.ext_list = ext_list  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksExtList]
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step  # type: bool
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.ntm_commodity_code = ntm_commodity_code  # type: str
        self.order_detail = order_detail  # type: any
        self.order_id = order_id  # type: long
        self.performance_node_dtos = performance_node_dtos  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksPerformanceNodeDTOS]
        self.purchase_pack_code = purchase_pack_code  # type: int
        self.service_apply_id = service_apply_id  # type: long
        self.service_month_reports = service_month_reports  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceMonthReports]
        self.service_reports = service_reports  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceReports]
        self.service_schemes = service_schemes  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceSchemes]
        self.status = status  # type: int
        self.status_str = status_str  # type: str
        self.support_time = support_time  # type: list[long]
        self.tam_engineers = tam_engineers  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksTamEngineers]

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.ntm_commodity_code is not None:
            result['ntmCommodityCode'] = self.ntm_commodity_code
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('ntmCommodityCode') is not None:
            self.ntm_commodity_code = m.get('ntmCommodityCode')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersServiceMonthReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersServiceMonthReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersServiceReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersServiceReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersServiceSchemes(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersServiceSchemes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrdersTamEngineers(TeaModel):
    def __init__(self, creator_emp_id=None, gmt_create=None, gmt_modified=None, hr_status=None, id=None,
                 last_name=None, modifier_emp_id=None, name=None, nick_name_en=None, realm_id=None, workid=None):
        self.creator_emp_id = creator_emp_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.hr_status = hr_status  # type: str
        self.id = id  # type: long
        self.last_name = last_name  # type: str
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.name = name  # type: str
        self.nick_name_en = nick_name_en  # type: str
        self.realm_id = realm_id  # type: long
        self.workid = workid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrdersTamEngineers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class ListServiceApplyResponseBodyDataListPerformanceOrders(TeaModel):
    def __init__(self, apply_file_volist=None, appointment_code=None, appointment_end_time=None,
                 appointment_id=None, appointment_pass_time=None, appointment_time=None, commodity_desc=None, creator_emp_id=None,
                 cycle_service=None, ext_list=None, gmt_create=None, gmt_modified=None, id=None,
                 merge_solution_and_reporter_one_step=None, modifier_emp_id=None, ntm_commodity_code=None, order_detail=None, order_id=None,
                 pack_count=None, pack_details=None, performance_node_dtos=None, performance_packs=None,
                 purchase_pack_code=None, service_apply_id=None, service_month_reports=None, service_reports=None,
                 service_schemes=None, status=None, status_str=None, support_time=None, tam_engineers=None):
        self.apply_file_volist = apply_file_volist  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersApplyFileVOList]
        self.appointment_code = appointment_code  # type: str
        self.appointment_end_time = appointment_end_time  # type: long
        self.appointment_id = appointment_id  # type: str
        self.appointment_pass_time = appointment_pass_time  # type: long
        self.appointment_time = appointment_time  # type: long
        self.commodity_desc = commodity_desc  # type: str
        self.creator_emp_id = creator_emp_id  # type: str
        self.cycle_service = cycle_service  # type: bool
        self.ext_list = ext_list  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersExtList]
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step  # type: bool
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.ntm_commodity_code = ntm_commodity_code  # type: str
        self.order_detail = order_detail  # type: any
        self.order_id = order_id  # type: long
        self.pack_count = pack_count  # type: int
        self.pack_details = pack_details  # type: list[dict[str, any]]
        self.performance_node_dtos = performance_node_dtos  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformanceNodeDTOS]
        self.performance_packs = performance_packs  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacks]
        self.purchase_pack_code = purchase_pack_code  # type: int
        self.service_apply_id = service_apply_id  # type: long
        self.service_month_reports = service_month_reports  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersServiceMonthReports]
        self.service_reports = service_reports  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersServiceReports]
        self.service_schemes = service_schemes  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersServiceSchemes]
        self.status = status  # type: int
        self.status_str = status_str  # type: str
        self.support_time = support_time  # type: list[long]
        self.tam_engineers = tam_engineers  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrdersTamEngineers]

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.performance_packs:
            for k in self.performance_packs:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformanceOrders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.ntm_commodity_code is not None:
            result['ntmCommodityCode'] = self.ntm_commodity_code
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.pack_count is not None:
            result['packCount'] = self.pack_count
        if self.pack_details is not None:
            result['packDetails'] = self.pack_details
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        result['performancePacks'] = []
        if self.performance_packs is not None:
            for k in self.performance_packs:
                result['performancePacks'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('ntmCommodityCode') is not None:
            self.ntm_commodity_code = m.get('ntmCommodityCode')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('packCount') is not None:
            self.pack_count = m.get('packCount')
        if m.get('packDetails') is not None:
            self.pack_details = m.get('packDetails')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        self.performance_packs = []
        if m.get('performancePacks') is not None:
            for k in m.get('performancePacks'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacks()
                self.performance_packs.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrdersTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksApplyFileVOList(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformancePacksApplyFileVOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksExtList(TeaModel):
    def __init__(self, key_code=None, name=None, value=None, view=None):
        self.key_code = key_code  # type: str
        self.name = name  # type: str
        self.value = value  # type: any
        self.view = view  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformancePacksExtList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_code is not None:
            result['keyCode'] = self.key_code
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.view is not None:
            result['view'] = self.view
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('view') is not None:
            self.view = m.get('view')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksPerformanceNodeDTOS(TeaModel):
    def __init__(self, display=None, extend_info=None, index=None, node_name=None, status=None):
        self.display = display  # type: bool
        self.extend_info = extend_info  # type: any
        self.index = index  # type: int
        self.node_name = node_name  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformancePacksPerformanceNodeDTOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['display'] = self.display
        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info
        if self.index is not None:
            result['index'] = self.index
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')
        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksServiceMonthReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformancePacksServiceMonthReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksServiceReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformancePacksServiceReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksServiceSchemes(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformancePacksServiceSchemes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacksTamEngineers(TeaModel):
    def __init__(self, creator_emp_id=None, gmt_create=None, gmt_modified=None, hr_status=None, id=None,
                 last_name=None, modifier_emp_id=None, name=None, nick_name_en=None, realm_id=None, workid=None):
        self.creator_emp_id = creator_emp_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.hr_status = hr_status  # type: str
        self.id = id  # type: long
        self.last_name = last_name  # type: str
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.name = name  # type: str
        self.nick_name_en = nick_name_en  # type: str
        self.realm_id = realm_id  # type: long
        self.workid = workid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformancePacksTamEngineers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status
        if self.id is not None:
            result['id'] = self.id
        if self.last_name is not None:
            result['lastName'] = self.last_name
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en
        if self.realm_id is not None:
            result['realmId'] = self.realm_id
        if self.workid is not None:
            result['workid'] = self.workid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')
        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')
        if m.get('workid') is not None:
            self.workid = m.get('workid')
        return self


class ListServiceApplyResponseBodyDataListPerformancePacks(TeaModel):
    def __init__(self, apply_file_volist=None, appointment_code=None, appointment_end_time=None,
                 appointment_id=None, appointment_pass_time=None, appointment_time=None, commodity_desc=None, creator_emp_id=None,
                 cycle_service=None, ext_list=None, gmt_create=None, gmt_modified=None, id=None,
                 merge_solution_and_reporter_one_step=None, modifier_emp_id=None, ntm_commodity_code=None, order_detail=None, order_id=None,
                 performance_node_dtos=None, purchase_pack_code=None, service_apply_id=None, service_month_reports=None,
                 service_reports=None, service_schemes=None, status=None, status_str=None, support_time=None, tam_engineers=None):
        self.apply_file_volist = apply_file_volist  # type: list[ListServiceApplyResponseBodyDataListPerformancePacksApplyFileVOList]
        self.appointment_code = appointment_code  # type: str
        self.appointment_end_time = appointment_end_time  # type: long
        self.appointment_id = appointment_id  # type: str
        self.appointment_pass_time = appointment_pass_time  # type: long
        self.appointment_time = appointment_time  # type: long
        self.commodity_desc = commodity_desc  # type: str
        self.creator_emp_id = creator_emp_id  # type: str
        self.cycle_service = cycle_service  # type: bool
        self.ext_list = ext_list  # type: list[ListServiceApplyResponseBodyDataListPerformancePacksExtList]
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step  # type: bool
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.ntm_commodity_code = ntm_commodity_code  # type: str
        self.order_detail = order_detail  # type: any
        self.order_id = order_id  # type: long
        self.performance_node_dtos = performance_node_dtos  # type: list[ListServiceApplyResponseBodyDataListPerformancePacksPerformanceNodeDTOS]
        self.purchase_pack_code = purchase_pack_code  # type: int
        self.service_apply_id = service_apply_id  # type: long
        self.service_month_reports = service_month_reports  # type: list[ListServiceApplyResponseBodyDataListPerformancePacksServiceMonthReports]
        self.service_reports = service_reports  # type: list[ListServiceApplyResponseBodyDataListPerformancePacksServiceReports]
        self.service_schemes = service_schemes  # type: list[ListServiceApplyResponseBodyDataListPerformancePacksServiceSchemes]
        self.status = status  # type: int
        self.status_str = status_str  # type: str
        self.support_time = support_time  # type: list[long]
        self.tam_engineers = tam_engineers  # type: list[ListServiceApplyResponseBodyDataListPerformancePacksTamEngineers]

    def validate(self):
        if self.apply_file_volist:
            for k in self.apply_file_volist:
                if k:
                    k.validate()
        if self.ext_list:
            for k in self.ext_list:
                if k:
                    k.validate()
        if self.performance_node_dtos:
            for k in self.performance_node_dtos:
                if k:
                    k.validate()
        if self.service_month_reports:
            for k in self.service_month_reports:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()
        if self.service_schemes:
            for k in self.service_schemes:
                if k:
                    k.validate()
        if self.tam_engineers:
            for k in self.tam_engineers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListPerformancePacks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k in self.apply_file_volist:
                result['applyFileVOList'].append(k.to_map() if k else None)
        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code
        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time
        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time
        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        result['extList'] = []
        if self.ext_list is not None:
            for k in self.ext_list:
                result['extList'].append(k.to_map() if k else None)
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.ntm_commodity_code is not None:
            result['ntmCommodityCode'] = self.ntm_commodity_code
        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail
        if self.order_id is not None:
            result['orderId'] = self.order_id
        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k.to_map() if k else None)
        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k in self.service_month_reports:
                result['serviceMonthReports'].append(k.to_map() if k else None)
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k in self.service_schemes:
                result['serviceSchemes'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.support_time is not None:
            result['supportTime'] = self.support_time
        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k in self.tam_engineers:
                result['tamEngineers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k in m.get('applyFileVOList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k))
        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')
        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')
        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')
        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        self.ext_list = []
        if m.get('extList') is not None:
            for k in m.get('extList'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksExtList()
                self.ext_list.append(temp_model.from_map(k))
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('ntmCommodityCode') is not None:
            self.ntm_commodity_code = m.get('ntmCommodityCode')
        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k in m.get('performanceNodeDTOS'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k))
        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k in m.get('serviceMonthReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k))
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k in m.get('serviceSchemes'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')
        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k in m.get('tamEngineers'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacksTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k))
        return self


class ListServiceApplyResponseBodyDataListServiceReports(TeaModel):
    def __init__(self, appointment_id=None, batch_group=None, customer_id=None, file_name=None, file_type=None,
                 gmt_create=None, gmt_modified=None, id=None, remarke=None, service_apply_id=None, status=None, url=None):
        self.appointment_id = appointment_id  # type: str
        self.batch_group = batch_group  # type: str
        self.customer_id = customer_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.remarke = remarke  # type: str
        self.service_apply_id = service_apply_id  # type: long
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataListServiceReports, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id
        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group
        if self.customer_id is not None:
            result['customerId'] = self.customer_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.remarke is not None:
            result['remarke'] = self.remarke
        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')
        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')
        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')
        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListServiceApplyResponseBodyDataList(TeaModel):
    def __init__(self, applier_id=None, apply_code=None, apply_component_details=None, apply_time=None,
                 appointments=None, buy_url=None, creator_emp_id=None, customer_name=None, cycle_service=None,
                 executed_count=None, finish_count=None, gmt_create=None, gmt_modified=None, id=None,
                 merge_solution_and_reporter_one_step=None, modifier_emp_id=None, pack_details=None, pay_orders=None, pay_url=None,
                 performance_orders=None, performance_packs=None, rene_wal_url=None, service_code=None, service_name=None,
                 service_reports=None, service_time_range=None, status=None, status_code=None, status_str=None,
                 term_of_validity=None, total_pack=None, type=None, use_pack=None):
        self.applier_id = applier_id  # type: str
        self.apply_code = apply_code  # type: str
        self.apply_component_details = apply_component_details  # type: list[list[str]]
        self.apply_time = apply_time  # type: long
        self.appointments = appointments  # type: list[ListServiceApplyResponseBodyDataListAppointments]
        self.buy_url = buy_url  # type: str
        self.creator_emp_id = creator_emp_id  # type: str
        self.customer_name = customer_name  # type: str
        self.cycle_service = cycle_service  # type: bool
        self.executed_count = executed_count  # type: long
        self.finish_count = finish_count  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step  # type: bool
        self.modifier_emp_id = modifier_emp_id  # type: str
        self.pack_details = pack_details  # type: list[dict[str, any]]
        self.pay_orders = pay_orders  # type: list[ListServiceApplyResponseBodyDataListPayOrders]
        self.pay_url = pay_url  # type: str
        self.performance_orders = performance_orders  # type: list[ListServiceApplyResponseBodyDataListPerformanceOrders]
        self.performance_packs = performance_packs  # type: list[ListServiceApplyResponseBodyDataListPerformancePacks]
        self.rene_wal_url = rene_wal_url  # type: str
        self.service_code = service_code  # type: str
        self.service_name = service_name  # type: str
        self.service_reports = service_reports  # type: list[ListServiceApplyResponseBodyDataListServiceReports]
        self.service_time_range = service_time_range  # type: list[long]
        self.status = status  # type: str
        self.status_code = status_code  # type: int
        self.status_str = status_str  # type: str
        self.term_of_validity = term_of_validity  # type: str
        self.total_pack = total_pack  # type: int
        self.type = type  # type: str
        self.use_pack = use_pack  # type: long

    def validate(self):
        if self.appointments:
            for k in self.appointments:
                if k:
                    k.validate()
        if self.pay_orders:
            for k in self.pay_orders:
                if k:
                    k.validate()
        if self.performance_orders:
            for k in self.performance_orders:
                if k:
                    k.validate()
        if self.performance_packs:
            for k in self.performance_packs:
                if k:
                    k.validate()
        if self.service_reports:
            for k in self.service_reports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applier_id is not None:
            result['applierId'] = self.applier_id
        if self.apply_code is not None:
            result['applyCode'] = self.apply_code
        if self.apply_component_details is not None:
            result['applyComponentDetails'] = self.apply_component_details
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        result['appointments'] = []
        if self.appointments is not None:
            for k in self.appointments:
                result['appointments'].append(k.to_map() if k else None)
        if self.buy_url is not None:
            result['buyUrl'] = self.buy_url
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id
        if self.customer_name is not None:
            result['customerName'] = self.customer_name
        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service
        if self.executed_count is not None:
            result['executedCount'] = self.executed_count
        if self.finish_count is not None:
            result['finishCount'] = self.finish_count
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step
        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id
        if self.pack_details is not None:
            result['packDetails'] = self.pack_details
        result['payOrders'] = []
        if self.pay_orders is not None:
            for k in self.pay_orders:
                result['payOrders'].append(k.to_map() if k else None)
        if self.pay_url is not None:
            result['payUrl'] = self.pay_url
        result['performanceOrders'] = []
        if self.performance_orders is not None:
            for k in self.performance_orders:
                result['performanceOrders'].append(k.to_map() if k else None)
        result['performancePacks'] = []
        if self.performance_packs is not None:
            for k in self.performance_packs:
                result['performancePacks'].append(k.to_map() if k else None)
        if self.rene_wal_url is not None:
            result['reneWalUrl'] = self.rene_wal_url
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        result['serviceReports'] = []
        if self.service_reports is not None:
            for k in self.service_reports:
                result['serviceReports'].append(k.to_map() if k else None)
        if self.service_time_range is not None:
            result['serviceTimeRange'] = self.service_time_range
        if self.status is not None:
            result['status'] = self.status
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.status_str is not None:
            result['statusStr'] = self.status_str
        if self.term_of_validity is not None:
            result['termOfValidity'] = self.term_of_validity
        if self.total_pack is not None:
            result['totalPack'] = self.total_pack
        if self.type is not None:
            result['type'] = self.type
        if self.use_pack is not None:
            result['usePack'] = self.use_pack
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applierId') is not None:
            self.applier_id = m.get('applierId')
        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')
        if m.get('applyComponentDetails') is not None:
            self.apply_component_details = m.get('applyComponentDetails')
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        self.appointments = []
        if m.get('appointments') is not None:
            for k in m.get('appointments'):
                temp_model = ListServiceApplyResponseBodyDataListAppointments()
                self.appointments.append(temp_model.from_map(k))
        if m.get('buyUrl') is not None:
            self.buy_url = m.get('buyUrl')
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')
        if m.get('customerName') is not None:
            self.customer_name = m.get('customerName')
        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')
        if m.get('executedCount') is not None:
            self.executed_count = m.get('executedCount')
        if m.get('finishCount') is not None:
            self.finish_count = m.get('finishCount')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')
        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')
        if m.get('packDetails') is not None:
            self.pack_details = m.get('packDetails')
        self.pay_orders = []
        if m.get('payOrders') is not None:
            for k in m.get('payOrders'):
                temp_model = ListServiceApplyResponseBodyDataListPayOrders()
                self.pay_orders.append(temp_model.from_map(k))
        if m.get('payUrl') is not None:
            self.pay_url = m.get('payUrl')
        self.performance_orders = []
        if m.get('performanceOrders') is not None:
            for k in m.get('performanceOrders'):
                temp_model = ListServiceApplyResponseBodyDataListPerformanceOrders()
                self.performance_orders.append(temp_model.from_map(k))
        self.performance_packs = []
        if m.get('performancePacks') is not None:
            for k in m.get('performancePacks'):
                temp_model = ListServiceApplyResponseBodyDataListPerformancePacks()
                self.performance_packs.append(temp_model.from_map(k))
        if m.get('reneWalUrl') is not None:
            self.rene_wal_url = m.get('reneWalUrl')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k in m.get('serviceReports'):
                temp_model = ListServiceApplyResponseBodyDataListServiceReports()
                self.service_reports.append(temp_model.from_map(k))
        if m.get('serviceTimeRange') is not None:
            self.service_time_range = m.get('serviceTimeRange')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')
        if m.get('termOfValidity') is not None:
            self.term_of_validity = m.get('termOfValidity')
        if m.get('totalPack') is not None:
            self.total_pack = m.get('totalPack')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('usePack') is not None:
            self.use_pack = m.get('usePack')
        return self


class ListServiceApplyResponseBodyData(TeaModel):
    def __init__(self, extend=None, list=None, page_num=None, page_size=None, total=None):
        self.extend = extend  # type: any
        self.list = list  # type: list[ListServiceApplyResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceApplyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend is not None:
            result['extend'] = self.extend
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
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListServiceApplyResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListServiceApplyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListServiceApplyResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListServiceApplyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListServiceApplyResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListServiceApplyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServiceApplyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceApplyResponse, self).to_map()
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
            temp_model = ListServiceApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListYunQiTaskByUidRequest(TeaModel):
    def __init__(self, create_time_end=None, create_time_start=None, free_order_apply_codes=None,
                 free_order_apply_ids=None, order_ids=None, page_num=None, page_size=None, status_list=None):
        self.create_time_end = create_time_end  # type: long
        self.create_time_start = create_time_start  # type: long
        self.free_order_apply_codes = free_order_apply_codes  # type: list[str]
        self.free_order_apply_ids = free_order_apply_ids  # type: list[long]
        self.order_ids = order_ids  # type: list[long]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.status_list = status_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListYunQiTaskByUidRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_end is not None:
            result['createTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['createTimeStart'] = self.create_time_start
        if self.free_order_apply_codes is not None:
            result['freeOrderApplyCodes'] = self.free_order_apply_codes
        if self.free_order_apply_ids is not None:
            result['freeOrderApplyIds'] = self.free_order_apply_ids
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status_list is not None:
            result['statusList'] = self.status_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTimeEnd') is not None:
            self.create_time_end = m.get('createTimeEnd')
        if m.get('createTimeStart') is not None:
            self.create_time_start = m.get('createTimeStart')
        if m.get('freeOrderApplyCodes') is not None:
            self.free_order_apply_codes = m.get('freeOrderApplyCodes')
        if m.get('freeOrderApplyIds') is not None:
            self.free_order_apply_ids = m.get('freeOrderApplyIds')
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')
        return self


class ListYunQiTaskByUidResponseBodyDataList(TeaModel):
    def __init__(self, chat_id=None, create_time=None, creator_name=None, end_time=None, evaluation_star=None,
                 important=None, main_ding_department_id=None, main_ding_group_id=None, main_ding_group_name=None,
                 product_name=None, record_id=None, status=None, sub_ding_department_id=None, sub_ding_group_id=None,
                 sub_ding_group_name=None, title=None):
        self.chat_id = chat_id  # type: str
        self.create_time = create_time  # type: long
        self.creator_name = creator_name  # type: str
        self.end_time = end_time  # type: long
        self.evaluation_star = evaluation_star  # type: int
        self.important = important  # type: str
        self.main_ding_department_id = main_ding_department_id  # type: str
        self.main_ding_group_id = main_ding_group_id  # type: str
        self.main_ding_group_name = main_ding_group_name  # type: str
        self.product_name = product_name  # type: str
        self.record_id = record_id  # type: str
        self.status = status  # type: str
        self.sub_ding_department_id = sub_ding_department_id  # type: str
        self.sub_ding_group_id = sub_ding_group_id  # type: str
        self.sub_ding_group_name = sub_ding_group_name  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListYunQiTaskByUidResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_id is not None:
            result['chatId'] = self.chat_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.evaluation_star is not None:
            result['evaluationStar'] = self.evaluation_star
        if self.important is not None:
            result['important'] = self.important
        if self.main_ding_department_id is not None:
            result['mainDingDepartmentId'] = self.main_ding_department_id
        if self.main_ding_group_id is not None:
            result['mainDingGroupId'] = self.main_ding_group_id
        if self.main_ding_group_name is not None:
            result['mainDingGroupName'] = self.main_ding_group_name
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.status is not None:
            result['status'] = self.status
        if self.sub_ding_department_id is not None:
            result['subDingDepartmentId'] = self.sub_ding_department_id
        if self.sub_ding_group_id is not None:
            result['subDingGroupId'] = self.sub_ding_group_id
        if self.sub_ding_group_name is not None:
            result['subDingGroupName'] = self.sub_ding_group_name
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('evaluationStar') is not None:
            self.evaluation_star = m.get('evaluationStar')
        if m.get('important') is not None:
            self.important = m.get('important')
        if m.get('mainDingDepartmentId') is not None:
            self.main_ding_department_id = m.get('mainDingDepartmentId')
        if m.get('mainDingGroupId') is not None:
            self.main_ding_group_id = m.get('mainDingGroupId')
        if m.get('mainDingGroupName') is not None:
            self.main_ding_group_name = m.get('mainDingGroupName')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subDingDepartmentId') is not None:
            self.sub_ding_department_id = m.get('subDingDepartmentId')
        if m.get('subDingGroupId') is not None:
            self.sub_ding_group_id = m.get('subDingGroupId')
        if m.get('subDingGroupName') is not None:
            self.sub_ding_group_name = m.get('subDingGroupName')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListYunQiTaskByUidResponseBodyData(TeaModel):
    def __init__(self, extend=None, list=None, page_num=None, page_size=None, total=None):
        self.extend = extend  # type: any
        self.list = list  # type: list[ListYunQiTaskByUidResponseBodyDataList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListYunQiTaskByUidResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend is not None:
            result['extend'] = self.extend
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
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = ListYunQiTaskByUidResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListYunQiTaskByUidResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListYunQiTaskByUidResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListYunQiTaskByUidResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListYunQiTaskByUidResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListYunQiTaskByUidResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListYunQiTaskByUidResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListYunQiTaskByUidResponse, self).to_map()
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
            temp_model = ListYunQiTaskByUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MarkFileReadedRequest(TeaModel):
    def __init__(self, apply_code=None, file_id=None, order_id=None, scene=None):
        self.apply_code = apply_code  # type: str
        self.file_id = file_id  # type: long
        self.order_id = order_id  # type: str
        self.scene = scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkFileReadedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_code is not None:
            result['applyCode'] = self.apply_code
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.scene is not None:
            result['scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        return self


class MarkFileReadedResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(MarkFileReadedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class MarkFileReadedResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MarkFileReadedResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MarkFileReadedResponse, self).to_map()
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
            temp_model = MarkFileReadedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


