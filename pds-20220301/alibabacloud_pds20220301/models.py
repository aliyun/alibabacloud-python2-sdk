# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AccountLinkInfo(TeaModel):
    def __init__(self, authentication_type=None, created_at=None, display_name=None, domain_id=None, extra=None,
                 identity=None, user_id=None):
        self.authentication_type = authentication_type  # type: str
        self.created_at = created_at  # type: long
        self.display_name = display_name  # type: str
        self.domain_id = domain_id  # type: str
        self.extra = extra  # type: str
        self.identity = identity  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccountLinkInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_type is not None:
            result['authentication_type'] = self.authentication_type
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.display_name is not None:
            result['display_name'] = self.display_name
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authentication_type') is not None:
            self.authentication_type = m.get('authentication_type')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class Activity(TeaModel):
    def __init__(self, activity_id=None, device=None, drive_id=None, event_type=None, latest_event_time=None,
                 resource_category=None, resource_list=None, total_resource_count=None, user_id=None):
        self.activity_id = activity_id  # type: str
        self.device = device  # type: str
        self.drive_id = drive_id  # type: str
        self.event_type = event_type  # type: int
        self.latest_event_time = latest_event_time  # type: str
        self.resource_category = resource_category  # type: int
        self.resource_list = resource_list  # type: list[dict[str, any]]
        self.total_resource_count = total_resource_count  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Activity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['activity_id'] = self.activity_id
        if self.device is not None:
            result['device'] = self.device
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.event_type is not None:
            result['event_type'] = self.event_type
        if self.latest_event_time is not None:
            result['latest_event_time'] = self.latest_event_time
        if self.resource_category is not None:
            result['resource_category'] = self.resource_category
        if self.resource_list is not None:
            result['resource_list'] = self.resource_list
        if self.total_resource_count is not None:
            result['total_resource_count'] = self.total_resource_count
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('activity_id') is not None:
            self.activity_id = m.get('activity_id')
        if m.get('device') is not None:
            self.device = m.get('device')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('event_type') is not None:
            self.event_type = m.get('event_type')
        if m.get('latest_event_time') is not None:
            self.latest_event_time = m.get('latest_event_time')
        if m.get('resource_category') is not None:
            self.resource_category = m.get('resource_category')
        if m.get('resource_list') is not None:
            self.resource_list = m.get('resource_list')
        if m.get('total_resource_count') is not None:
            self.total_resource_count = m.get('total_resource_count')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class Address(TeaModel):
    def __init__(self, city=None, country=None, district=None, province=None, township=None):
        self.city = city  # type: str
        self.country = country  # type: str
        self.district = district  # type: str
        self.province = province  # type: str
        self.township = township  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Address, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['city'] = self.city
        if self.country is not None:
            result['country'] = self.country
        if self.district is not None:
            result['district'] = self.district
        if self.province is not None:
            result['province'] = self.province
        if self.township is not None:
            result['township'] = self.township
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('township') is not None:
            self.township = m.get('township')
        return self


class AddressGroup(TeaModel):
    def __init__(self, address_detail=None, count=None, cover_file_id=None, cover_url=None, location=None, name=None):
        self.address_detail = address_detail  # type: Address
        self.count = count  # type: long
        self.cover_file_id = cover_file_id  # type: str
        self.cover_url = cover_url  # type: str
        self.location = location  # type: str
        self.name = name  # type: str

    def validate(self):
        if self.address_detail:
            self.address_detail.validate()

    def to_map(self):
        _map = super(AddressGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['address_detail'] = self.address_detail.to_map()
        if self.count is not None:
            result['count'] = self.count
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.cover_url is not None:
            result['cover_url'] = self.cover_url
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('address_detail') is not None:
            temp_model = Address()
            self.address_detail = temp_model.from_map(m['address_detail'])
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')
        if m.get('cover_url') is not None:
            self.cover_url = m.get('cover_url')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class Drive(TeaModel):
    def __init__(self, created_at=None, creator=None, description=None, domain_id=None, drive_id=None,
                 drive_name=None, drive_type=None, owner=None, owner_type=None, status=None, total_size=None, used_size=None):
        self.created_at = created_at  # type: str
        self.creator = creator  # type: str
        self.description = description  # type: str
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str
        self.drive_name = drive_name  # type: str
        self.drive_type = drive_type  # type: str
        self.owner = owner  # type: str
        self.owner_type = owner_type  # type: str
        self.status = status  # type: str
        self.total_size = total_size  # type: long
        self.used_size = used_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(Drive, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.drive_type is not None:
            result['drive_type'] = self.drive_type
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.status is not None:
            result['status'] = self.status
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.used_size is not None:
            result['used_size'] = self.used_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')
        return self


class FaceGroupGroupCoverFaceBoundary(TeaModel):
    def __init__(self, height=None, left=None, top=None, width=None):
        self.height = height  # type: int
        self.left = left  # type: int
        self.top = top  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(FaceGroupGroupCoverFaceBoundary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['height'] = self.height
        if self.left is not None:
            result['left'] = self.left
        if self.top is not None:
            result['top'] = self.top
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('left') is not None:
            self.left = m.get('left')
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class FaceGroup(TeaModel):
    def __init__(self, created_at=None, group_cover_face_boundary=None, group_cover_file_id=None,
                 group_cover_height=None, group_cover_url=None, group_cover_width=None, group_id=None, group_name=None,
                 image_count=None, remarks=None, updated_at=None):
        self.created_at = created_at  # type: str
        self.group_cover_face_boundary = group_cover_face_boundary  # type: FaceGroupGroupCoverFaceBoundary
        self.group_cover_file_id = group_cover_file_id  # type: str
        self.group_cover_height = group_cover_height  # type: long
        self.group_cover_url = group_cover_url  # type: str
        self.group_cover_width = group_cover_width  # type: long
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.image_count = image_count  # type: long
        self.remarks = remarks  # type: str
        self.updated_at = updated_at  # type: str

    def validate(self):
        if self.group_cover_face_boundary:
            self.group_cover_face_boundary.validate()

    def to_map(self):
        _map = super(FaceGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.group_cover_face_boundary is not None:
            result['group_cover_face_boundary'] = self.group_cover_face_boundary.to_map()
        if self.group_cover_file_id is not None:
            result['group_cover_file_id'] = self.group_cover_file_id
        if self.group_cover_height is not None:
            result['group_cover_height'] = self.group_cover_height
        if self.group_cover_url is not None:
            result['group_cover_url'] = self.group_cover_url
        if self.group_cover_width is not None:
            result['group_cover_width'] = self.group_cover_width
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.image_count is not None:
            result['image_count'] = self.image_count
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('group_cover_face_boundary') is not None:
            temp_model = FaceGroupGroupCoverFaceBoundary()
            self.group_cover_face_boundary = temp_model.from_map(m['group_cover_face_boundary'])
        if m.get('group_cover_file_id') is not None:
            self.group_cover_file_id = m.get('group_cover_file_id')
        if m.get('group_cover_height') is not None:
            self.group_cover_height = m.get('group_cover_height')
        if m.get('group_cover_url') is not None:
            self.group_cover_url = m.get('group_cover_url')
        if m.get('group_cover_width') is not None:
            self.group_cover_width = m.get('group_cover_width')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('image_count') is not None:
            self.image_count = m.get('image_count')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class File(TeaModel):
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, file_extension=None,
                 file_id=None, hidden=None, labels=None, local_created_at=None, local_modified_at=None, name=None,
                 parent_file_id=None, revision_id=None, size=None, starred=None, status=None, thumbnail=None, trashed_at=None,
                 type=None, updated_at=None, upload_id=None):
        self.category = category  # type: str
        self.content_hash = content_hash  # type: str
        self.content_hash_name = content_hash_name  # type: str
        self.content_type = content_type  # type: str
        self.crc_64hash = crc_64hash  # type: str
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.domain_id = domain_id  # type: str
        self.download_url = download_url  # type: str
        self.drive_id = drive_id  # type: str
        self.file_extension = file_extension  # type: str
        self.file_id = file_id  # type: str
        self.hidden = hidden  # type: bool
        self.labels = labels  # type: str
        self.local_created_at = local_created_at  # type: str
        self.local_modified_at = local_modified_at  # type: str
        self.name = name  # type: str
        self.parent_file_id = parent_file_id  # type: str
        self.revision_id = revision_id  # type: str
        self.size = size  # type: long
        self.starred = starred  # type: bool
        self.status = status  # type: str
        self.thumbnail = thumbnail  # type: str
        self.trashed_at = trashed_at  # type: str
        self.type = type  # type: str
        self.updated_at = updated_at  # type: str
        self.upload_id = upload_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(File, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.labels is not None:
            result['labels'] = self.labels
        if self.local_created_at is not None:
            result['local_created_at'] = self.local_created_at
        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        if self.size is not None:
            result['size'] = self.size
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('local_created_at') is not None:
            self.local_created_at = m.get('local_created_at')
        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class FilePermissionMember(TeaModel):
    def __init__(self, action_list=None, disinherit_sub_group=None, expire_time=None, identity=None, role_id=None):
        self.action_list = action_list  # type: list[str]
        self.disinherit_sub_group = disinherit_sub_group  # type: bool
        self.expire_time = expire_time  # type: long
        self.identity = identity  # type: Identity
        self.role_id = role_id  # type: str

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super(FilePermissionMember, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_list is not None:
            result['action_list'] = self.action_list
        if self.disinherit_sub_group is not None:
            result['disinherit_sub_group'] = self.disinherit_sub_group
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        if self.role_id is not None:
            result['role_id'] = self.role_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')
        if m.get('disinherit_sub_group') is not None:
            self.disinherit_sub_group = m.get('disinherit_sub_group')
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        return self


class FileStreamInfo(TeaModel):
    def __init__(self, content_hash=None, content_hash_name=None, content_md_5=None, part_info_list=None,
                 pre_hash=None, proof_code=None, proof_version=None, size=None):
        self.content_hash = content_hash  # type: str
        self.content_hash_name = content_hash_name  # type: str
        self.content_md_5 = content_md_5  # type: str
        self.part_info_list = part_info_list  # type: UploadPartInfo
        self.pre_hash = pre_hash  # type: str
        self.proof_code = proof_code  # type: str
        self.proof_version = proof_version  # type: str
        self.size = size  # type: long

    def validate(self):
        if self.part_info_list:
            self.part_info_list.validate()

    def to_map(self):
        _map = super(FileStreamInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.part_info_list is not None:
            result['part_info_list'] = self.part_info_list.to_map()
        if self.pre_hash is not None:
            result['pre_hash'] = self.pre_hash
        if self.proof_code is not None:
            result['proof_code'] = self.proof_code
        if self.proof_version is not None:
            result['proof_version'] = self.proof_version
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('part_info_list') is not None:
            temp_model = UploadPartInfo()
            self.part_info_list = temp_model.from_map(m['part_info_list'])
        if m.get('pre_hash') is not None:
            self.pre_hash = m.get('pre_hash')
        if m.get('proof_code') is not None:
            self.proof_code = m.get('proof_code')
        if m.get('proof_version') is not None:
            self.proof_version = m.get('proof_version')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class Group(TeaModel):
    def __init__(self, created_at=None, creator=None, description=None, domain_id=None, group_id=None,
                 group_name=None, updated_at=None):
        self.created_at = created_at  # type: long
        self.creator = creator  # type: str
        self.description = description  # type: str
        self.domain_id = domain_id  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.updated_at = updated_at  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(Group, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class Identity(TeaModel):
    def __init__(self, identity_id=None, identity_type=None):
        self.identity_id = identity_id  # type: str
        self.identity_type = identity_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Identity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_id is not None:
            result['identity_id'] = self.identity_id
        if self.identity_type is not None:
            result['identity_type'] = self.identity_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')
        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')
        return self


class ImageMediaMetadata(TeaModel):
    def __init__(self, height=None, taken_at=None, width=None):
        self.height = height  # type: long
        self.taken_at = taken_at  # type: str
        self.width = width  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageMediaMetadata, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['height'] = self.height
        if self.taken_at is not None:
            result['taken_at'] = self.taken_at
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('taken_at') is not None:
            self.taken_at = m.get('taken_at')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class ImageTag(TeaModel):
    def __init__(self, count=None, cover_file_category=None, cover_file_id=None, cover_overall_score=None,
                 cover_tag_confidence=None, cover_url=None, name=None):
        self.count = count  # type: long
        self.cover_file_category = cover_file_category  # type: str
        self.cover_file_id = cover_file_id  # type: str
        self.cover_overall_score = cover_overall_score  # type: float
        self.cover_tag_confidence = cover_tag_confidence  # type: float
        self.cover_url = cover_url  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImageTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.cover_file_category is not None:
            result['cover_file_category'] = self.cover_file_category
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.cover_overall_score is not None:
            result['cover_overall_score'] = self.cover_overall_score
        if self.cover_tag_confidence is not None:
            result['cover_tag_confidence'] = self.cover_tag_confidence
        if self.cover_url is not None:
            result['cover_url'] = self.cover_url
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cover_file_category') is not None:
            self.cover_file_category = m.get('cover_file_category')
        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')
        if m.get('cover_overall_score') is not None:
            self.cover_overall_score = m.get('cover_overall_score')
        if m.get('cover_tag_confidence') is not None:
            self.cover_tag_confidence = m.get('cover_tag_confidence')
        if m.get('cover_url') is not None:
            self.cover_url = m.get('cover_url')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class JWTPayload(TeaModel):
    def __init__(self, aud=None, auto_create=None, exp=None, iat=None, iss=None, jti=None, nbf=None, sub=None,
                 sub_type=None):
        self.aud = aud  # type: str
        self.auto_create = auto_create  # type: bool
        self.exp = exp  # type: long
        self.iat = iat  # type: long
        self.iss = iss  # type: str
        self.jti = jti  # type: str
        self.nbf = nbf  # type: long
        self.sub = sub  # type: str
        self.sub_type = sub_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JWTPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aud is not None:
            result['aud'] = self.aud
        if self.auto_create is not None:
            result['auto_create'] = self.auto_create
        if self.exp is not None:
            result['exp'] = self.exp
        if self.iat is not None:
            result['iat'] = self.iat
        if self.iss is not None:
            result['iss'] = self.iss
        if self.jti is not None:
            result['jti'] = self.jti
        if self.nbf is not None:
            result['nbf'] = self.nbf
        if self.sub is not None:
            result['sub'] = self.sub
        if self.sub_type is not None:
            result['sub_type'] = self.sub_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aud') is not None:
            self.aud = m.get('aud')
        if m.get('auto_create') is not None:
            self.auto_create = m.get('auto_create')
        if m.get('exp') is not None:
            self.exp = m.get('exp')
        if m.get('iat') is not None:
            self.iat = m.get('iat')
        if m.get('iss') is not None:
            self.iss = m.get('iss')
        if m.get('jti') is not None:
            self.jti = m.get('jti')
        if m.get('nbf') is not None:
            self.nbf = m.get('nbf')
        if m.get('sub') is not None:
            self.sub = m.get('sub')
        if m.get('sub_type') is not None:
            self.sub_type = m.get('sub_type')
        return self


class Revision(TeaModel):
    def __init__(self, content_hash=None, content_hash_name=None, crc_64hash=None, created_at=None, domain_id=None,
                 download_url=None, drive_id=None, file_extension=None, file_id=None, is_latest_version=None, keep_forever=None,
                 revision_description=None, revision_id=None, revision_name=None, revision_version=None, size=None, thumbnail=None,
                 updated_at=None, url=None):
        self.content_hash = content_hash  # type: str
        self.content_hash_name = content_hash_name  # type: str
        self.crc_64hash = crc_64hash  # type: str
        self.created_at = created_at  # type: str
        self.domain_id = domain_id  # type: str
        self.download_url = download_url  # type: str
        self.drive_id = drive_id  # type: str
        self.file_extension = file_extension  # type: str
        self.file_id = file_id  # type: str
        self.is_latest_version = is_latest_version  # type: bool
        self.keep_forever = keep_forever  # type: bool
        self.revision_description = revision_description  # type: str
        self.revision_id = revision_id  # type: str
        self.revision_name = revision_name  # type: str
        self.revision_version = revision_version  # type: long
        self.size = size  # type: long
        self.thumbnail = thumbnail  # type: str
        self.updated_at = updated_at  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Revision, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.is_latest_version is not None:
            result['is_latest_version'] = self.is_latest_version
        if self.keep_forever is not None:
            result['keep_forever'] = self.keep_forever
        if self.revision_description is not None:
            result['revision_description'] = self.revision_description
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        if self.revision_name is not None:
            result['revision_name'] = self.revision_name
        if self.revision_version is not None:
            result['revision_version'] = self.revision_version
        if self.size is not None:
            result['size'] = self.size
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('is_latest_version') is not None:
            self.is_latest_version = m.get('is_latest_version')
        if m.get('keep_forever') is not None:
            self.keep_forever = m.get('keep_forever')
        if m.get('revision_description') is not None:
            self.revision_description = m.get('revision_description')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        if m.get('revision_name') is not None:
            self.revision_name = m.get('revision_name')
        if m.get('revision_version') is not None:
            self.revision_version = m.get('revision_version')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ShareLink(TeaModel):
    def __init__(self, access_count=None, created_at=None, creator=None, description=None, disable_download=None,
                 disable_preview=None, disable_save=None, download_count=None, download_limit=None, drive_id=None, expiration=None,
                 expired=None, file_id_list=None, preview_count=None, preview_limit=None, report_count=None,
                 save_count=None, save_limit=None, share_id=None, share_name=None, share_pwd=None, status=None, updated_at=None,
                 video_preview_count=None):
        self.access_count = access_count  # type: long
        self.created_at = created_at  # type: str
        self.creator = creator  # type: str
        self.description = description  # type: str
        self.disable_download = disable_download  # type: bool
        self.disable_preview = disable_preview  # type: bool
        self.disable_save = disable_save  # type: bool
        self.download_count = download_count  # type: long
        self.download_limit = download_limit  # type: long
        self.drive_id = drive_id  # type: str
        self.expiration = expiration  # type: str
        self.expired = expired  # type: bool
        self.file_id_list = file_id_list  # type: str
        self.preview_count = preview_count  # type: long
        self.preview_limit = preview_limit  # type: long
        self.report_count = report_count  # type: long
        self.save_count = save_count  # type: long
        self.save_limit = save_limit  # type: long
        self.share_id = share_id  # type: str
        self.share_name = share_name  # type: str
        self.share_pwd = share_pwd  # type: str
        self.status = status  # type: str
        self.updated_at = updated_at  # type: str
        self.video_preview_count = video_preview_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShareLink, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_count is not None:
            result['access_count'] = self.access_count
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.disable_download is not None:
            result['disable_download'] = self.disable_download
        if self.disable_preview is not None:
            result['disable_preview'] = self.disable_preview
        if self.disable_save is not None:
            result['disable_save'] = self.disable_save
        if self.download_count is not None:
            result['download_count'] = self.download_count
        if self.download_limit is not None:
            result['download_limit'] = self.download_limit
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.expired is not None:
            result['expired'] = self.expired
        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list
        if self.preview_count is not None:
            result['preview_count'] = self.preview_count
        if self.preview_limit is not None:
            result['preview_limit'] = self.preview_limit
        if self.report_count is not None:
            result['report_count'] = self.report_count
        if self.save_count is not None:
            result['save_count'] = self.save_count
        if self.save_limit is not None:
            result['save_limit'] = self.save_limit
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.video_preview_count is not None:
            result['video_preview_count'] = self.video_preview_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('access_count') is not None:
            self.access_count = m.get('access_count')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('disable_download') is not None:
            self.disable_download = m.get('disable_download')
        if m.get('disable_preview') is not None:
            self.disable_preview = m.get('disable_preview')
        if m.get('disable_save') is not None:
            self.disable_save = m.get('disable_save')
        if m.get('download_count') is not None:
            self.download_count = m.get('download_count')
        if m.get('download_limit') is not None:
            self.download_limit = m.get('download_limit')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')
        if m.get('preview_count') is not None:
            self.preview_count = m.get('preview_count')
        if m.get('preview_limit') is not None:
            self.preview_limit = m.get('preview_limit')
        if m.get('report_count') is not None:
            self.report_count = m.get('report_count')
        if m.get('save_count') is not None:
            self.save_count = m.get('save_count')
        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('video_preview_count') is not None:
            self.video_preview_count = m.get('video_preview_count')
        return self


class SystemTag(TeaModel):
    def __init__(self, confidence=None, name=None, parent_name=None, source=None, tag_level=None):
        self.confidence = confidence  # type: float
        self.name = name  # type: str
        self.parent_name = parent_name  # type: str
        self.source = source  # type: str
        self.tag_level = tag_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SystemTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['confidence'] = self.confidence
        if self.name is not None:
            result['name'] = self.name
        if self.parent_name is not None:
            result['parent_name'] = self.parent_name
        if self.source is not None:
            result['source'] = self.source
        if self.tag_level is not None:
            result['tag_level'] = self.tag_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_name') is not None:
            self.parent_name = m.get('parent_name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('tag_level') is not None:
            self.tag_level = m.get('tag_level')
        return self


class Token(TeaModel):
    def __init__(self, access_token=None, avatar=None, default_drive_id=None, device_id=None, device_name=None,
                 domain_id=None, expire_time=None, expires_in=None, is_first_login=None, nick_name=None, refresh_token=None,
                 role=None, status=None, token_type=None, user_id=None, user_name=None):
        self.access_token = access_token  # type: str
        self.avatar = avatar  # type: str
        self.default_drive_id = default_drive_id  # type: str
        self.device_id = device_id  # type: str
        self.device_name = device_name  # type: str
        self.domain_id = domain_id  # type: str
        self.expire_time = expire_time  # type: str
        self.expires_in = expires_in  # type: long
        self.is_first_login = is_first_login  # type: bool
        self.nick_name = nick_name  # type: str
        self.refresh_token = refresh_token  # type: str
        self.role = role  # type: str
        self.status = status  # type: str
        self.token_type = token_type  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Token, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.device_id is not None:
            result['device_id'] = self.device_id
        if self.device_name is not None:
            result['device_name'] = self.device_name
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.is_first_login is not None:
            result['is_first_login'] = self.is_first_login
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.token_type is not None:
            result['token_type'] = self.token_type
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('device_id') is not None:
            self.device_id = m.get('device_id')
        if m.get('device_name') is not None:
            self.device_name = m.get('device_name')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('is_first_login') is not None:
            self.is_first_login = m.get('is_first_login')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('token_type') is not None:
            self.token_type = m.get('token_type')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class UploadPartInfoParallelSha1Ctx(TeaModel):
    def __init__(self, h=None, part_offset=None):
        self.h = h  # type: list[long]
        self.part_offset = part_offset  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadPartInfoParallelSha1Ctx, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['h'] = self.h
        if self.part_offset is not None:
            result['part_offset'] = self.part_offset
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')
        if m.get('part_offset') is not None:
            self.part_offset = m.get('part_offset')
        return self


class UploadPartInfo(TeaModel):
    def __init__(self, etag=None, internal_upload_url=None, parallel_sha_1ctx=None, part_number=None,
                 part_size=None, upload_url=None):
        self.etag = etag  # type: str
        self.internal_upload_url = internal_upload_url  # type: str
        self.parallel_sha_1ctx = parallel_sha_1ctx  # type: UploadPartInfoParallelSha1Ctx
        self.part_number = part_number  # type: int
        self.part_size = part_size  # type: long
        self.upload_url = upload_url  # type: str

    def validate(self):
        if self.parallel_sha_1ctx:
            self.parallel_sha_1ctx.validate()

    def to_map(self):
        _map = super(UploadPartInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['etag'] = self.etag
        if self.internal_upload_url is not None:
            result['internal_upload_url'] = self.internal_upload_url
        if self.parallel_sha_1ctx is not None:
            result['parallel_sha1_ctx'] = self.parallel_sha_1ctx.to_map()
        if self.part_number is not None:
            result['part_number'] = self.part_number
        if self.part_size is not None:
            result['part_size'] = self.part_size
        if self.upload_url is not None:
            result['upload_url'] = self.upload_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        if m.get('internal_upload_url') is not None:
            self.internal_upload_url = m.get('internal_upload_url')
        if m.get('parallel_sha1_ctx') is not None:
            temp_model = UploadPartInfoParallelSha1Ctx()
            self.parallel_sha_1ctx = temp_model.from_map(m['parallel_sha1_ctx'])
        if m.get('part_number') is not None:
            self.part_number = m.get('part_number')
        if m.get('part_size') is not None:
            self.part_size = m.get('part_size')
        if m.get('upload_url') is not None:
            self.upload_url = m.get('upload_url')
        return self


class User(TeaModel):
    def __init__(self, avatar=None, created_at=None, creator=None, default_drive_id=None, description=None,
                 domain_id=None, email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None,
                 user_data=None, user_id=None, user_name=None):
        self.avatar = avatar  # type: str
        self.created_at = created_at  # type: long
        self.creator = creator  # type: str
        self.default_drive_id = default_drive_id  # type: str
        self.description = description  # type: str
        self.domain_id = domain_id  # type: str
        self.email = email  # type: str
        self.nick_name = nick_name  # type: str
        self.phone = phone  # type: str
        self.role = role  # type: str
        self.status = status  # type: str
        self.updated_at = updated_at  # type: long
        self.user_data = user_data  # type: dict[str, str]
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(User, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.email is not None:
            result['email'] = self.email
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class UserTag(TeaModel):
    def __init__(self, value=None, key=None):
        self.value = value  # type: str
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UserTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class VideoMediaMetadata(TeaModel):
    def __init__(self, duration=None, taken_at=None):
        self.duration = duration  # type: str
        self.taken_at = taken_at  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoMediaMetadata, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.taken_at is not None:
            result['taken_at'] = self.taken_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('taken_at') is not None:
            self.taken_at = m.get('taken_at')
        return self


class VideoPreviewPlayInfoLiveTranscodingTaskList(TeaModel):
    def __init__(self, keep_original_resolution=None, status=None, template_id=None, url=None):
        self.keep_original_resolution = keep_original_resolution  # type: bool
        self.status = status  # type: str
        self.template_id = template_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoPreviewPlayInfoLiveTranscodingTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_original_resolution is not None:
            result['keep_original_resolution'] = self.keep_original_resolution
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['template_id'] = self.template_id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keep_original_resolution') is not None:
            self.keep_original_resolution = m.get('keep_original_resolution')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class VideoPreviewPlayInfoMeta(TeaModel):
    def __init__(self, duration=None, height=None, width=None):
        self.duration = duration  # type: float
        self.height = height  # type: long
        self.width = width  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoPreviewPlayInfoMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class VideoPreviewPlayInfo(TeaModel):
    def __init__(self, category=None, live_transcoding_task_list=None, meta=None):
        self.category = category  # type: str
        self.live_transcoding_task_list = live_transcoding_task_list  # type: list[VideoPreviewPlayInfoLiveTranscodingTaskList]
        self.meta = meta  # type: VideoPreviewPlayInfoMeta

    def validate(self):
        if self.live_transcoding_task_list:
            for k in self.live_transcoding_task_list:
                if k:
                    k.validate()
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super(VideoPreviewPlayInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['live_transcoding_task_list'] = []
        if self.live_transcoding_task_list is not None:
            for k in self.live_transcoding_task_list:
                result['live_transcoding_task_list'].append(k.to_map() if k else None)
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.live_transcoding_task_list = []
        if m.get('live_transcoding_task_list') is not None:
            for k in m.get('live_transcoding_task_list'):
                temp_model = VideoPreviewPlayInfoLiveTranscodingTaskList()
                self.live_transcoding_task_list.append(temp_model.from_map(k))
        if m.get('meta') is not None:
            temp_model = VideoPreviewPlayInfoMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class VideoPreviewPlayMetaLiveTranscodingTaskList(TeaModel):
    def __init__(self, keep_original_resolution=None, status=None, template_id=None):
        self.keep_original_resolution = keep_original_resolution  # type: bool
        self.status = status  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoPreviewPlayMetaLiveTranscodingTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_original_resolution is not None:
            result['keep_original_resolution'] = self.keep_original_resolution
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keep_original_resolution') is not None:
            self.keep_original_resolution = m.get('keep_original_resolution')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        return self


class VideoPreviewPlayMetaMeta(TeaModel):
    def __init__(self, duration=None, height=None, width=None):
        self.duration = duration  # type: float
        self.height = height  # type: long
        self.width = width  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoPreviewPlayMetaMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class VideoPreviewPlayMeta(TeaModel):
    def __init__(self, category=None, live_transcoding_task_list=None, meta=None):
        self.category = category  # type: str
        self.live_transcoding_task_list = live_transcoding_task_list  # type: list[VideoPreviewPlayMetaLiveTranscodingTaskList]
        self.meta = meta  # type: VideoPreviewPlayMetaMeta

    def validate(self):
        if self.live_transcoding_task_list:
            for k in self.live_transcoding_task_list:
                if k:
                    k.validate()
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super(VideoPreviewPlayMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['live_transcoding_task_list'] = []
        if self.live_transcoding_task_list is not None:
            for k in self.live_transcoding_task_list:
                result['live_transcoding_task_list'].append(k.to_map() if k else None)
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.live_transcoding_task_list = []
        if m.get('live_transcoding_task_list') is not None:
            for k in m.get('live_transcoding_task_list'):
                temp_model = VideoPreviewPlayMetaLiveTranscodingTaskList()
                self.live_transcoding_task_list.append(temp_model.from_map(k))
        if m.get('meta') is not None:
            temp_model = VideoPreviewPlayMetaMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class AuthorizeRequest(TeaModel):
    def __init__(self, client_id=None, hide_consent=None, login_type=None, redirect_uri=None, response_type=None,
                 scope=None, state=None):
        self.client_id = client_id  # type: str
        self.hide_consent = hide_consent  # type: bool
        self.login_type = login_type  # type: str
        self.redirect_uri = redirect_uri  # type: str
        self.response_type = response_type  # type: str
        self.scope = scope  # type: list[str]
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.hide_consent is not None:
            result['hide_consent'] = self.hide_consent
        if self.login_type is not None:
            result['login_type'] = self.login_type
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.response_type is not None:
            result['response_type'] = self.response_type
        if self.scope is not None:
            result['scope'] = self.scope
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('hide_consent') is not None:
            self.hide_consent = m.get('hide_consent')
        if m.get('login_type') is not None:
            self.login_type = m.get('login_type')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('response_type') is not None:
            self.response_type = m.get('response_type')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class AuthorizeShrinkRequest(TeaModel):
    def __init__(self, client_id=None, hide_consent=None, login_type=None, redirect_uri=None, response_type=None,
                 scope_shrink=None, state=None):
        self.client_id = client_id  # type: str
        self.hide_consent = hide_consent  # type: bool
        self.login_type = login_type  # type: str
        self.redirect_uri = redirect_uri  # type: str
        self.response_type = response_type  # type: str
        self.scope_shrink = scope_shrink  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.hide_consent is not None:
            result['hide_consent'] = self.hide_consent
        if self.login_type is not None:
            result['login_type'] = self.login_type
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.response_type is not None:
            result['response_type'] = self.response_type
        if self.scope_shrink is not None:
            result['scope'] = self.scope_shrink
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('hide_consent') is not None:
            self.hide_consent = m.get('hide_consent')
        if m.get('login_type') is not None:
            self.login_type = m.get('login_type')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('response_type') is not None:
            self.response_type = m.get('response_type')
        if m.get('scope') is not None:
            self.scope_shrink = m.get('scope')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class AuthorizeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(AuthorizeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class BatchRequestRequests(TeaModel):
    def __init__(self, body=None, headers=None, id=None, method=None, url=None):
        self.body = body  # type: dict[str, str]
        self.headers = headers  # type: dict[str, str]
        self.id = id  # type: str
        self.method = method  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchRequestRequests, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.headers is not None:
            result['headers'] = self.headers
        if self.id is not None:
            result['id'] = self.id
        if self.method is not None:
            result['method'] = self.method
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class BatchRequest(TeaModel):
    def __init__(self, requests=None, resource=None):
        self.requests = requests  # type: list[BatchRequestRequests]
        self.resource = resource  # type: str

    def validate(self):
        if self.requests:
            for k in self.requests:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['requests'] = []
        if self.requests is not None:
            for k in self.requests:
                result['requests'].append(k.to_map() if k else None)
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.requests = []
        if m.get('requests') is not None:
            for k in m.get('requests'):
                temp_model = BatchRequestRequests()
                self.requests.append(temp_model.from_map(k))
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class BatchResponseBodyResponses(TeaModel):
    def __init__(self, body=None, id=None, status=None):
        self.body = body  # type: dict[str, str]
        self.id = id  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchResponseBodyResponses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.id is not None:
            result['id'] = self.id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class BatchResponseBody(TeaModel):
    def __init__(self, responses=None):
        self.responses = responses  # type: list[BatchResponseBodyResponses]

    def validate(self):
        if self.responses:
            for k in self.responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['responses'] = []
        if self.responses is not None:
            for k in self.responses:
                result['responses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.responses = []
        if m.get('responses') is not None:
            for k in m.get('responses'):
                temp_model = BatchResponseBodyResponses()
                self.responses.append(temp_model.from_map(k))
        return self


class BatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchResponse, self).to_map()
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
            temp_model = BatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelShareLinkRequest(TeaModel):
    def __init__(self, share_id=None):
        self.share_id = share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelShareLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class CancelShareLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(CancelShareLinkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ClearRecyclebinRequest(TeaModel):
    def __init__(self, drive_id=None):
        self.drive_id = drive_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearRecyclebinRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class ClearRecyclebinResponseBody(TeaModel):
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None):
        self.async_task_id = async_task_id  # type: str
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearRecyclebinResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class ClearRecyclebinResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ClearRecyclebinResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClearRecyclebinResponse, self).to_map()
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
            temp_model = ClearRecyclebinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteFileRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, upload_id=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.upload_id = upload_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompleteFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class CompleteFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: File

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CompleteFileResponse, self).to_map()
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
            temp_model = File()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyFileRequest(TeaModel):
    def __init__(self, auto_rename=None, drive_id=None, file_id=None, to_parent_file_id=None):
        self.auto_rename = auto_rename  # type: bool
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.to_parent_file_id = to_parent_file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_rename is not None:
            result['auto_rename'] = self.auto_rename
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.to_parent_file_id is not None:
            result['to_parent_file_id'] = self.to_parent_file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('auto_rename') is not None:
            self.auto_rename = m.get('auto_rename')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('to_parent_file_id') is not None:
            self.to_parent_file_id = m.get('to_parent_file_id')
        return self


class CopyFileResponseBody(TeaModel):
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_id=None):
        self.async_task_id = async_task_id  # type: str
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CopyFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class CopyFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CopyFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CopyFileResponse, self).to_map()
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
            temp_model = CopyFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDriveRequest(TeaModel):
    def __init__(self, default=None, description=None, drive_name=None, drive_type=None, owner=None, owner_type=None,
                 status=None, total_size=None):
        self.default = default  # type: bool
        self.description = description  # type: str
        self.drive_name = drive_name  # type: str
        self.drive_type = drive_type  # type: str
        self.owner = owner  # type: str
        self.owner_type = owner_type  # type: str
        self.status = status  # type: str
        self.total_size = total_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDriveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default is not None:
            result['default'] = self.default
        if self.description is not None:
            result['description'] = self.description
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.drive_type is not None:
            result['drive_type'] = self.drive_type
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.status is not None:
            result['status'] = self.status
        if self.total_size is not None:
            result['total_size'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        return self


class CreateDriveResponseBody(TeaModel):
    def __init__(self, domain_id=None, drive_id=None):
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDriveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class CreateDriveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDriveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDriveResponse, self).to_map()
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
            temp_model = CreateDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileRequestPartInfoList(TeaModel):
    def __init__(self, part_number=None):
        self.part_number = part_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileRequestPartInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.part_number is not None:
            result['part_number'] = self.part_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('part_number') is not None:
            self.part_number = m.get('part_number')
        return self


class CreateFileRequest(TeaModel):
    def __init__(self, check_name_mode=None, content_hash=None, content_hash_name=None, content_type=None,
                 description=None, drive_id=None, file_id=None, hidden=None, image_media_metadata=None, local_created_at=None,
                 local_modified_at=None, name=None, parallel_upload=None, parent_file_id=None, part_info_list=None, pre_hash=None,
                 share_id=None, size=None, type=None, user_tags=None, video_media_metadata=None):
        self.check_name_mode = check_name_mode  # type: str
        self.content_hash = content_hash  # type: str
        self.content_hash_name = content_hash_name  # type: str
        self.content_type = content_type  # type: str
        self.description = description  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.hidden = hidden  # type: bool
        self.image_media_metadata = image_media_metadata  # type: ImageMediaMetadata
        self.local_created_at = local_created_at  # type: str
        self.local_modified_at = local_modified_at  # type: str
        self.name = name  # type: str
        self.parallel_upload = parallel_upload  # type: bool
        self.parent_file_id = parent_file_id  # type: str
        self.part_info_list = part_info_list  # type: list[CreateFileRequestPartInfoList]
        self.pre_hash = pre_hash  # type: str
        self.share_id = share_id  # type: str
        self.size = size  # type: long
        self.type = type  # type: str
        self.user_tags = user_tags  # type: list[UserTag]
        self.video_media_metadata = video_media_metadata  # type: VideoMediaMetadata

    def validate(self):
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.user_tags:
            for k in self.user_tags:
                if k:
                    k.validate()
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        _map = super(CreateFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.local_created_at is not None:
            result['local_created_at'] = self.local_created_at
        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at
        if self.name is not None:
            result['name'] = self.name
        if self.parallel_upload is not None:
            result['parallel_upload'] = self.parallel_upload
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.pre_hash is not None:
            result['pre_hash'] = self.pre_hash
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        result['user_tags'] = []
        if self.user_tags is not None:
            for k in self.user_tags:
                result['user_tags'].append(k.to_map() if k else None)
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('image_media_metadata') is not None:
            temp_model = ImageMediaMetadata()
            self.image_media_metadata = temp_model.from_map(m['image_media_metadata'])
        if m.get('local_created_at') is not None:
            self.local_created_at = m.get('local_created_at')
        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parallel_upload') is not None:
            self.parallel_upload = m.get('parallel_upload')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = CreateFileRequestPartInfoList()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('pre_hash') is not None:
            self.pre_hash = m.get('pre_hash')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        self.user_tags = []
        if m.get('user_tags') is not None:
            for k in m.get('user_tags'):
                temp_model = UserTag()
                self.user_tags.append(temp_model.from_map(k))
        if m.get('video_media_metadata') is not None:
            temp_model = VideoMediaMetadata()
            self.video_media_metadata = temp_model.from_map(m['video_media_metadata'])
        return self


class CreateFileResponseBody(TeaModel):
    def __init__(self, domain_id=None, drive_id=None, exist=None, file_id=None, file_name=None, parent_file_id=None,
                 part_info_list=None, rapid_upload=None, status=None, type=None, upload_id=None):
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str
        self.exist = exist  # type: bool
        self.file_id = file_id  # type: str
        self.file_name = file_name  # type: str
        self.parent_file_id = parent_file_id  # type: str
        self.part_info_list = part_info_list  # type: list[UploadPartInfo]
        self.rapid_upload = rapid_upload  # type: bool
        self.status = status  # type: str
        self.type = type  # type: str
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.exist is not None:
            result['exist'] = self.exist
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.rapid_upload is not None:
            result['rapid_upload'] = self.rapid_upload
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('exist') is not None:
            self.exist = m.get('exist')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('rapid_upload') is not None:
            self.rapid_upload = m.get('rapid_upload')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class CreateFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFileResponse, self).to_map()
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
            temp_model = CreateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(self, description=None, group_name=None, is_root=None, parent_group_id=None):
        self.description = description  # type: str
        self.group_name = group_name  # type: str
        self.is_root = is_root  # type: bool
        self.parent_group_id = parent_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.is_root is not None:
            result['is_root'] = self.is_root
        if self.parent_group_id is not None:
            result['parent_group_id'] = self.parent_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('is_root') is not None:
            self.is_root = m.get('is_root')
        if m.get('parent_group_id') is not None:
            self.parent_group_id = m.get('parent_group_id')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Group

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupResponse, self).to_map()
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
            temp_model = Group()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateShareLinkRequest(TeaModel):
    def __init__(self, description=None, disable_download=None, disable_preview=None, disable_save=None,
                 download_limit=None, drive_id=None, expiration=None, file_id_list=None, preview_limit=None, save_limit=None,
                 share_name=None, share_pwd=None, user_id=None):
        self.description = description  # type: str
        self.disable_download = disable_download  # type: bool
        self.disable_preview = disable_preview  # type: bool
        self.disable_save = disable_save  # type: bool
        self.download_limit = download_limit  # type: long
        self.drive_id = drive_id  # type: str
        self.expiration = expiration  # type: str
        self.file_id_list = file_id_list  # type: list[str]
        self.preview_limit = preview_limit  # type: long
        self.save_limit = save_limit  # type: long
        self.share_name = share_name  # type: str
        self.share_pwd = share_pwd  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateShareLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.disable_download is not None:
            result['disable_download'] = self.disable_download
        if self.disable_preview is not None:
            result['disable_preview'] = self.disable_preview
        if self.disable_save is not None:
            result['disable_save'] = self.disable_save
        if self.download_limit is not None:
            result['download_limit'] = self.download_limit
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list
        if self.preview_limit is not None:
            result['preview_limit'] = self.preview_limit
        if self.save_limit is not None:
            result['save_limit'] = self.save_limit
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('disable_download') is not None:
            self.disable_download = m.get('disable_download')
        if m.get('disable_preview') is not None:
            self.disable_preview = m.get('disable_preview')
        if m.get('disable_save') is not None:
            self.disable_save = m.get('disable_save')
        if m.get('download_limit') is not None:
            self.download_limit = m.get('download_limit')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')
        if m.get('preview_limit') is not None:
            self.preview_limit = m.get('preview_limit')
        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CreateShareLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ShareLink

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateShareLinkResponse, self).to_map()
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
            temp_model = ShareLink()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequestGroupInfoList(TeaModel):
    def __init__(self, group_id=None):
        self.group_id = group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserRequestGroupInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class CreateUserRequest(TeaModel):
    def __init__(self, avatar=None, description=None, email=None, group_info_list=None, nick_name=None, phone=None,
                 role=None, status=None, user_data=None, user_id=None, user_name=None):
        self.avatar = avatar  # type: str
        self.description = description  # type: str
        self.email = email  # type: str
        self.group_info_list = group_info_list  # type: list[CreateUserRequestGroupInfoList]
        self.nick_name = nick_name  # type: str
        self.phone = phone  # type: str
        self.role = role  # type: str
        self.status = status  # type: str
        self.user_data = user_data  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        if self.group_info_list:
            for k in self.group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.description is not None:
            result['description'] = self.description
        if self.email is not None:
            result['email'] = self.email
        result['group_info_list'] = []
        if self.group_info_list is not None:
            for k in self.group_info_list:
                result['group_info_list'].append(k.to_map() if k else None)
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('email') is not None:
            self.email = m.get('email')
        self.group_info_list = []
        if m.get('group_info_list') is not None:
            for k in m.get('group_info_list'):
                temp_model = CreateUserRequestGroupInfoList()
                self.group_info_list.append(temp_model.from_map(k))
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(self, avatar=None, created_at=None, creator=None, default_drive_id=None, description=None,
                 domain_id=None, email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None,
                 user_data=None, user_id=None, user_name=None):
        self.avatar = avatar  # type: str
        self.created_at = created_at  # type: long
        self.creator = creator  # type: str
        self.default_drive_id = default_drive_id  # type: str
        self.description = description  # type: str
        self.domain_id = domain_id  # type: str
        self.email = email  # type: str
        self.nick_name = nick_name  # type: str
        self.phone = phone  # type: str
        self.role = role  # type: str
        self.status = status  # type: str
        self.updated_at = updated_at  # type: long
        self.user_data = user_data  # type: dict[str, str]
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.email is not None:
            result['email'] = self.email
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class CreateUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserResponse, self).to_map()
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
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDriveRequest(TeaModel):
    def __init__(self, drive_id=None):
        self.drive_id = drive_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDriveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class DeleteDriveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteDriveResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteFileRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class DeleteFileResponseBody(TeaModel):
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_id=None):
        self.async_task_id = async_task_id  # type: str
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class DeleteFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFileResponse, self).to_map()
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(self, group_id=None):
        self.group_id = group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class DeleteGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteRevisionRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, revision_id=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.revision_id = revision_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class DeleteRevisionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteRevisionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DeleteUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeltaGetLastCursorRequest(TeaModel):
    def __init__(self, drive_id=None, sync_root_id=None):
        self.drive_id = drive_id  # type: str
        self.sync_root_id = sync_root_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeltaGetLastCursorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.sync_root_id is not None:
            result['sync_root_id'] = self.sync_root_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('sync_root_id') is not None:
            self.sync_root_id = m.get('sync_root_id')
        return self


class DeltaGetLastCursorResponseBody(TeaModel):
    def __init__(self, cursor=None):
        self.cursor = cursor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeltaGetLastCursorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        return self


class DeltaGetLastCursorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeltaGetLastCursorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeltaGetLastCursorResponse, self).to_map()
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
            temp_model = DeltaGetLastCursorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadFileRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, image_thumbnail_process=None, office_thumbnail_process=None,
                 video_thumbnail_process=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        self.office_thumbnail_process = office_thumbnail_process  # type: str
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.office_thumbnail_process is not None:
            result['office_thumbnail_process'] = self.office_thumbnail_process
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('office_thumbnail_process') is not None:
            self.office_thumbnail_process = m.get('office_thumbnail_process')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class DownloadFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(DownloadFileResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class FileAddPermissionRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, member_list=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.member_list = member_list  # type: list[FilePermissionMember]

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FileAddPermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['member_list'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['member_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.member_list = []
        if m.get('member_list') is not None:
            for k in m.get('member_list'):
                temp_model = FilePermissionMember()
                self.member_list.append(temp_model.from_map(k))
        return self


class FileAddPermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(FileAddPermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class FileDeleteUserTagsRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, key_list=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.key_list = key_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(FileDeleteUserTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.key_list is not None:
            result['key_list'] = self.key_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('key_list') is not None:
            self.key_list = m.get('key_list')
        return self


class FileDeleteUserTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(FileDeleteUserTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class FileListPermissionRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FileListPermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class FileListPermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: list[FilePermissionMember]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FileListPermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = FilePermissionMember()
                self.body.append(temp_model.from_map(k))
        return self


class FilePutUserTagsRequestUserTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilePutUserTagsRequestUserTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class FilePutUserTagsRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, user_tags=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.user_tags = user_tags  # type: list[FilePutUserTagsRequestUserTags]

    def validate(self):
        if self.user_tags:
            for k in self.user_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FilePutUserTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['user_tags'] = []
        if self.user_tags is not None:
            for k in self.user_tags:
                result['user_tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.user_tags = []
        if m.get('user_tags') is not None:
            for k in m.get('user_tags'):
                temp_model = FilePutUserTagsRequestUserTags()
                self.user_tags.append(temp_model.from_map(k))
        return self


class FilePutUserTagsResponseBody(TeaModel):
    def __init__(self, file_id=None):
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilePutUserTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class FilePutUserTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FilePutUserTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FilePutUserTagsResponse, self).to_map()
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
            temp_model = FilePutUserTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FileRemovePermissionRequestMemberList(TeaModel):
    def __init__(self, identity=None, role_id=None):
        self.identity = identity  # type: Identity
        self.role_id = role_id  # type: str

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super(FileRemovePermissionRequestMemberList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        if self.role_id is not None:
            result['role_id'] = self.role_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        return self


class FileRemovePermissionRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, member_list=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.member_list = member_list  # type: list[FileRemovePermissionRequestMemberList]

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FileRemovePermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['member_list'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['member_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.member_list = []
        if m.get('member_list') is not None:
            for k in m.get('member_list'):
                temp_model = FileRemovePermissionRequestMemberList()
                self.member_list.append(temp_model.from_map(k))
        return self


class FileRemovePermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(FileRemovePermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetAsyncTaskRequest(TeaModel):
    def __init__(self, async_task_id=None):
        self.async_task_id = async_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        return self


class GetAsyncTaskResponseBody(TeaModel):
    def __init__(self, async_task_id=None, consumed_process=None, err_code=None, message=None, status=None,
                 total_process=None, url=None):
        self.async_task_id = async_task_id  # type: str
        self.consumed_process = consumed_process  # type: long
        self.err_code = err_code  # type: long
        self.message = message  # type: str
        self.status = status  # type: str
        self.total_process = total_process  # type: long
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.consumed_process is not None:
            result['consumed_process'] = self.consumed_process
        if self.err_code is not None:
            result['err_code'] = self.err_code
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        if self.total_process is not None:
            result['total_process'] = self.total_process
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('consumed_process') is not None:
            self.consumed_process = m.get('consumed_process')
        if m.get('err_code') is not None:
            self.err_code = m.get('err_code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_process') is not None:
            self.total_process = m.get('total_process')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetAsyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAsyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncTaskResponse, self).to_map()
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
            temp_model = GetAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultDriveRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultDriveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetDefaultDriveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Drive

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDefaultDriveResponse, self).to_map()
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
            temp_model = Drive()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDownloadUrlRequest(TeaModel):
    def __init__(self, drive_id=None, expire_sec=None, file_id=None, file_name=None):
        self.drive_id = drive_id  # type: str
        self.expire_sec = expire_sec  # type: int
        self.file_id = file_id  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDownloadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_name is not None:
            result['file_name'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        return self


class GetDownloadUrlResponseBody(TeaModel):
    def __init__(self, cdn_url=None, content_hash=None, content_hash_name=None, crc_64hash=None, expiration=None,
                 internal_url=None, size=None, url=None):
        self.cdn_url = cdn_url  # type: str
        self.content_hash = content_hash  # type: str
        self.content_hash_name = content_hash_name  # type: str
        self.crc_64hash = crc_64hash  # type: str
        self.expiration = expiration  # type: str
        self.internal_url = internal_url  # type: str
        self.size = size  # type: long
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDownloadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_url is not None:
            result['cdn_url'] = self.cdn_url
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.internal_url is not None:
            result['internal_url'] = self.internal_url
        if self.size is not None:
            result['size'] = self.size
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cdn_url') is not None:
            self.cdn_url = m.get('cdn_url')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('internal_url') is not None:
            self.internal_url = m.get('internal_url')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetDownloadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDownloadUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class GetDriveRequest(TeaModel):
    def __init__(self, drive_id=None):
        self.drive_id = drive_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDriveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class GetDriveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Drive

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDriveResponse, self).to_map()
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
            temp_model = Drive()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileRequest(TeaModel):
    def __init__(self, drive_id=None, fields=None, file_id=None, url_expire_sec=None):
        self.drive_id = drive_id  # type: str
        self.fields = fields  # type: str
        self.file_id = file_id  # type: str
        self.url_expire_sec = url_expire_sec  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        return self


class GetFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: File

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFileResponse, self).to_map()
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
            temp_model = File()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(self, group_id=None):
        self.group_id = group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class GetGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Group

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGroupResponse, self).to_map()
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
            temp_model = Group()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLinkInfoRequest(TeaModel):
    def __init__(self, extra=None, identity=None, type=None):
        self.extra = extra  # type: str
        self.identity = identity  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLinkInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetLinkInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AccountLinkInfo

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLinkInfoResponse, self).to_map()
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
            temp_model = AccountLinkInfo()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLinkInfoByUserIdRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLinkInfoByUserIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetLinkInfoByUserIdResponseBody(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[AccountLinkInfo]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLinkInfoByUserIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = AccountLinkInfo()
                self.items.append(temp_model.from_map(k))
        return self


class GetLinkInfoByUserIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLinkInfoByUserIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLinkInfoByUserIdResponse, self).to_map()
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
            temp_model = GetLinkInfoByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRevisionRequest(TeaModel):
    def __init__(self, drive_id=None, fields=None, file_id=None, revision_id=None, url_expire_sec=None):
        self.drive_id = drive_id  # type: str
        self.fields = fields  # type: str
        self.file_id = file_id  # type: str
        self.revision_id = revision_id  # type: str
        self.url_expire_sec = url_expire_sec  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        return self


class GetRevisionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Revision

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRevisionResponse, self).to_map()
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
            temp_model = Revision()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareLinkRequest(TeaModel):
    def __init__(self, share_id=None):
        self.share_id = share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetShareLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetShareLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ShareLink

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetShareLinkResponse, self).to_map()
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
            temp_model = ShareLink()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareLinkByAnonymousRequest(TeaModel):
    def __init__(self, share_id=None):
        self.share_id = share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetShareLinkByAnonymousRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetShareLinkByAnonymousResponseBody(TeaModel):
    def __init__(self, access_count=None, avatar=None, creator_id=None, creator_name=None, creator_phone=None,
                 disable_download=None, disable_preview=None, disable_save=None, download_count=None, download_limit=None,
                 expiration=None, preview_count=None, preview_limit=None, report_count=None, save_count=None,
                 save_download_limit=None, save_limit=None, share_name=None, updated_at=None, video_preview_count=None):
        self.access_count = access_count  # type: long
        self.avatar = avatar  # type: str
        self.creator_id = creator_id  # type: str
        self.creator_name = creator_name  # type: str
        self.creator_phone = creator_phone  # type: str
        self.disable_download = disable_download  # type: bool
        self.disable_preview = disable_preview  # type: bool
        self.disable_save = disable_save  # type: bool
        self.download_count = download_count  # type: long
        self.download_limit = download_limit  # type: long
        self.expiration = expiration  # type: str
        self.preview_count = preview_count  # type: long
        self.preview_limit = preview_limit  # type: long
        self.report_count = report_count  # type: long
        self.save_count = save_count  # type: long
        self.save_download_limit = save_download_limit  # type: long
        self.save_limit = save_limit  # type: long
        self.share_name = share_name  # type: str
        self.updated_at = updated_at  # type: str
        self.video_preview_count = video_preview_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetShareLinkByAnonymousResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_count is not None:
            result['access_count'] = self.access_count
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.creator_id is not None:
            result['creator_id'] = self.creator_id
        if self.creator_name is not None:
            result['creator_name'] = self.creator_name
        if self.creator_phone is not None:
            result['creator_phone'] = self.creator_phone
        if self.disable_download is not None:
            result['disable_download'] = self.disable_download
        if self.disable_preview is not None:
            result['disable_preview'] = self.disable_preview
        if self.disable_save is not None:
            result['disable_save'] = self.disable_save
        if self.download_count is not None:
            result['download_count'] = self.download_count
        if self.download_limit is not None:
            result['download_limit'] = self.download_limit
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.preview_count is not None:
            result['preview_count'] = self.preview_count
        if self.preview_limit is not None:
            result['preview_limit'] = self.preview_limit
        if self.report_count is not None:
            result['report_count'] = self.report_count
        if self.save_count is not None:
            result['save_count'] = self.save_count
        if self.save_download_limit is not None:
            result['save_download_limit'] = self.save_download_limit
        if self.save_limit is not None:
            result['save_limit'] = self.save_limit
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.video_preview_count is not None:
            result['video_preview_count'] = self.video_preview_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('access_count') is not None:
            self.access_count = m.get('access_count')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('creator_id') is not None:
            self.creator_id = m.get('creator_id')
        if m.get('creator_name') is not None:
            self.creator_name = m.get('creator_name')
        if m.get('creator_phone') is not None:
            self.creator_phone = m.get('creator_phone')
        if m.get('disable_download') is not None:
            self.disable_download = m.get('disable_download')
        if m.get('disable_preview') is not None:
            self.disable_preview = m.get('disable_preview')
        if m.get('disable_save') is not None:
            self.disable_save = m.get('disable_save')
        if m.get('download_count') is not None:
            self.download_count = m.get('download_count')
        if m.get('download_limit') is not None:
            self.download_limit = m.get('download_limit')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('preview_count') is not None:
            self.preview_count = m.get('preview_count')
        if m.get('preview_limit') is not None:
            self.preview_limit = m.get('preview_limit')
        if m.get('report_count') is not None:
            self.report_count = m.get('report_count')
        if m.get('save_count') is not None:
            self.save_count = m.get('save_count')
        if m.get('save_download_limit') is not None:
            self.save_download_limit = m.get('save_download_limit')
        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('video_preview_count') is not None:
            self.video_preview_count = m.get('video_preview_count')
        return self


class GetShareLinkByAnonymousResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetShareLinkByAnonymousResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetShareLinkByAnonymousResponse, self).to_map()
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
            temp_model = GetShareLinkByAnonymousResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareLinkTokenRequest(TeaModel):
    def __init__(self, expire_sec=None, share_id=None, share_pwd=None):
        self.expire_sec = expire_sec  # type: int
        self.share_id = share_id  # type: str
        self.share_pwd = share_pwd  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetShareLinkTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        return self


class GetShareLinkTokenResponseBody(TeaModel):
    def __init__(self, expires_in=None, share_token=None):
        self.expires_in = expires_in  # type: long
        self.share_token = share_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetShareLinkTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.share_token is not None:
            result['share_token'] = self.share_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('share_token') is not None:
            self.share_token = m.get('share_token')
        return self


class GetShareLinkTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetShareLinkTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetShareLinkTokenResponse, self).to_map()
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
            temp_model = GetShareLinkTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadUrlRequestPartInfoListParallelSha1Ctx(TeaModel):
    def __init__(self, h=None, part_offset=None):
        self.h = h  # type: list[long]
        self.part_offset = part_offset  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUploadUrlRequestPartInfoListParallelSha1Ctx, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['h'] = self.h
        if self.part_offset is not None:
            result['part_offset'] = self.part_offset
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')
        if m.get('part_offset') is not None:
            self.part_offset = m.get('part_offset')
        return self


class GetUploadUrlRequestPartInfoList(TeaModel):
    def __init__(self, parallel_sha_1ctx=None, part_number=None):
        self.parallel_sha_1ctx = parallel_sha_1ctx  # type: GetUploadUrlRequestPartInfoListParallelSha1Ctx
        self.part_number = part_number  # type: int

    def validate(self):
        if self.parallel_sha_1ctx:
            self.parallel_sha_1ctx.validate()

    def to_map(self):
        _map = super(GetUploadUrlRequestPartInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parallel_sha_1ctx is not None:
            result['parallel_sha1_ctx'] = self.parallel_sha_1ctx.to_map()
        if self.part_number is not None:
            result['part_number'] = self.part_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('parallel_sha1_ctx') is not None:
            temp_model = GetUploadUrlRequestPartInfoListParallelSha1Ctx()
            self.parallel_sha_1ctx = temp_model.from_map(m['parallel_sha1_ctx'])
        if m.get('part_number') is not None:
            self.part_number = m.get('part_number')
        return self


class GetUploadUrlRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, part_info_list=None, share_id=None, upload_id=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.part_info_list = part_info_list  # type: list[GetUploadUrlRequestPartInfoList]
        self.share_id = share_id  # type: str
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUploadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = GetUploadUrlRequestPartInfoList()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class GetUploadUrlResponseBody(TeaModel):
    def __init__(self, create_at=None, domain_id=None, drive_id=None, file_id=None, part_info_list=None,
                 upload_id=None):
        self.create_at = create_at  # type: str
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.part_info_list = part_info_list  # type: list[UploadPartInfo]
        self.upload_id = upload_id  # type: str

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUploadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_at is not None:
            result['create_at'] = self.create_at
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('create_at') is not None:
            self.create_at = m.get('create_at')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class GetUploadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUploadUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUploadUrlResponse, self).to_map()
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
            temp_model = GetUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: User

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResponse, self).to_map()
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
            temp_model = User()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoPreviewPlayInfoRequest(TeaModel):
    def __init__(self, category=None, drive_id=None, file_id=None, get_without_url=None, share_id=None,
                 template_id=None):
        self.category = category  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.get_without_url = get_without_url  # type: bool
        self.share_id = share_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoPreviewPlayInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.get_without_url is not None:
            result['get_without_url'] = self.get_without_url
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('get_without_url') is not None:
            self.get_without_url = m.get('get_without_url')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        return self


class GetVideoPreviewPlayInfoResponseBody(TeaModel):
    def __init__(self, domain_id=None, drive_id=None, file_id=None, share_id=None, video_preview_play_info=None):
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.share_id = share_id  # type: str
        self.video_preview_play_info = video_preview_play_info  # type: VideoPreviewPlayInfo

    def validate(self):
        if self.video_preview_play_info:
            self.video_preview_play_info.validate()

    def to_map(self):
        _map = super(GetVideoPreviewPlayInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.video_preview_play_info is not None:
            result['video_preview_play_info'] = self.video_preview_play_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('video_preview_play_info') is not None:
            temp_model = VideoPreviewPlayInfo()
            self.video_preview_play_info = temp_model.from_map(m['video_preview_play_info'])
        return self


class GetVideoPreviewPlayInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVideoPreviewPlayInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoPreviewPlayInfoResponse, self).to_map()
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
            temp_model = GetVideoPreviewPlayInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoPreviewPlayMetaRequest(TeaModel):
    def __init__(self, category=None, drive_id=None, file_id=None, share_id=None):
        self.category = category  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.share_id = share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoPreviewPlayMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetVideoPreviewPlayMetaResponseBody(TeaModel):
    def __init__(self, domain_id=None, drive_id=None, file_id=None, share_id=None, video_preview_play_meta=None):
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.share_id = share_id  # type: str
        self.video_preview_play_meta = video_preview_play_meta  # type: VideoPreviewPlayMeta

    def validate(self):
        if self.video_preview_play_meta:
            self.video_preview_play_meta.validate()

    def to_map(self):
        _map = super(GetVideoPreviewPlayMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.video_preview_play_meta is not None:
            result['video_preview_play_meta'] = self.video_preview_play_meta.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('video_preview_play_meta') is not None:
            temp_model = VideoPreviewPlayMeta()
            self.video_preview_play_meta = temp_model.from_map(m['video_preview_play_meta'])
        return self


class GetVideoPreviewPlayMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVideoPreviewPlayMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoPreviewPlayMetaResponse, self).to_map()
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
            temp_model = GetVideoPreviewPlayMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportUserRequest(TeaModel):
    def __init__(self, authentication_display_name=None, authentication_type=None, auto_create_drive=None,
                 drive_total_size=None, extra=None, identity=None, nick_name=None, parent_group_id=None):
        self.authentication_display_name = authentication_display_name  # type: str
        self.authentication_type = authentication_type  # type: str
        self.auto_create_drive = auto_create_drive  # type: bool
        self.drive_total_size = drive_total_size  # type: long
        self.extra = extra  # type: str
        self.identity = identity  # type: str
        self.nick_name = nick_name  # type: str
        self.parent_group_id = parent_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_display_name is not None:
            result['authentication_display_name'] = self.authentication_display_name
        if self.authentication_type is not None:
            result['authentication_type'] = self.authentication_type
        if self.auto_create_drive is not None:
            result['auto_create_drive'] = self.auto_create_drive
        if self.drive_total_size is not None:
            result['drive_total_size'] = self.drive_total_size
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.parent_group_id is not None:
            result['parent_group_id'] = self.parent_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authentication_display_name') is not None:
            self.authentication_display_name = m.get('authentication_display_name')
        if m.get('authentication_type') is not None:
            self.authentication_type = m.get('authentication_type')
        if m.get('auto_create_drive') is not None:
            self.auto_create_drive = m.get('auto_create_drive')
        if m.get('drive_total_size') is not None:
            self.drive_total_size = m.get('drive_total_size')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('parent_group_id') is not None:
            self.parent_group_id = m.get('parent_group_id')
        return self


class ImportUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: User

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportUserResponse, self).to_map()
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
            temp_model = User()
            self.body = temp_model.from_map(m['body'])
        return self


class LinkAccountRequest(TeaModel):
    def __init__(self, extra=None, identity=None, type=None, user_id=None):
        self.extra = extra  # type: str
        self.identity = identity  # type: str
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LinkAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class LinkAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Token

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LinkAccountResponse, self).to_map()
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
            temp_model = Token()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAddressGroupsRequest(TeaModel):
    def __init__(self, drive_id=None, image_thumbnail_process=None, limit=None, marker=None,
                 video_thumbnail_process=None):
        self.drive_id = drive_id  # type: str
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        self.limit = limit  # type: int
        self.marker = marker  # type: str
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAddressGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ListAddressGroupsResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[AddressGroup]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAddressGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = AddressGroup()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListAddressGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAddressGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAddressGroupsResponse, self).to_map()
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
            temp_model = ListAddressGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeltaRequest(TeaModel):
    def __init__(self, cursor=None, drive_id=None, limit=None, sync_root_id=None):
        self.cursor = cursor  # type: str
        self.drive_id = drive_id  # type: str
        self.limit = limit  # type: int
        self.sync_root_id = sync_root_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeltaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.sync_root_id is not None:
            result['sync_root_id'] = self.sync_root_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('sync_root_id') is not None:
            self.sync_root_id = m.get('sync_root_id')
        return self


class ListDeltaResponseBodyItems(TeaModel):
    def __init__(self, file=None, file_id=None, op=None):
        self.file = file  # type: File
        self.file_id = file_id  # type: str
        self.op = op  # type: str

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        _map = super(ListDeltaResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file is not None:
            result['file'] = self.file.to_map()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.op is not None:
            result['op'] = self.op
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('file') is not None:
            temp_model = File()
            self.file = temp_model.from_map(m['file'])
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('op') is not None:
            self.op = m.get('op')
        return self


class ListDeltaResponseBody(TeaModel):
    def __init__(self, cursor=None, has_more=None, items=None):
        self.cursor = cursor  # type: str
        self.has_more = has_more  # type: bool
        self.items = items  # type: list[ListDeltaResponseBodyItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeltaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.has_more is not None:
            result['has_more'] = self.has_more
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('has_more') is not None:
            self.has_more = m.get('has_more')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ListDeltaResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListDeltaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeltaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeltaResponse, self).to_map()
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
            temp_model = ListDeltaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDriveRequest(TeaModel):
    def __init__(self, limit=None, marker=None, owner=None, owner_type=None):
        self.limit = limit  # type: int
        self.marker = marker  # type: str
        self.owner = owner  # type: str
        self.owner_type = owner_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDriveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        return self


class ListDriveResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[Drive]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDriveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Drive()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListDriveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDriveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDriveResponse, self).to_map()
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
            temp_model = ListDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFacegroupsRequest(TeaModel):
    def __init__(self, drive_id=None, limit=None, marker=None, remarks=None):
        self.drive_id = drive_id  # type: str
        self.limit = limit  # type: int
        self.marker = marker  # type: str
        self.remarks = remarks  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFacegroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.remarks is not None:
            result['remarks'] = self.remarks
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        return self


class ListFacegroupsResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[FaceGroup]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFacegroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = FaceGroup()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListFacegroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFacegroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFacegroupsResponse, self).to_map()
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
            temp_model = ListFacegroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileRequest(TeaModel):
    def __init__(self, category=None, drive_id=None, fields=None, limit=None, marker=None, order_by=None,
                 order_direction=None, parent_file_id=None, status=None, type=None):
        self.category = category  # type: str
        self.drive_id = drive_id  # type: str
        self.fields = fields  # type: str
        self.limit = limit  # type: int
        self.marker = marker  # type: str
        self.order_by = order_by  # type: str
        self.order_direction = order_direction  # type: str
        self.parent_file_id = parent_file_id  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.order_direction is not None:
            result['order_direction'] = self.order_direction
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListFileResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[File]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = File()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFileResponse, self).to_map()
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
            temp_model = ListFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupRequest(TeaModel):
    def __init__(self, limit=None, marker=None):
        self.limit = limit  # type: str
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListGroupResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[Group]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Group()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupResponse, self).to_map()
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
            temp_model = ListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMyDrivesRequest(TeaModel):
    def __init__(self, limit=None, marker=None):
        self.limit = limit  # type: int
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMyDrivesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListMyDrivesResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[Drive]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMyDrivesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Drive()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListMyDrivesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListMyDrivesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMyDrivesResponse, self).to_map()
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
            temp_model = ListMyDrivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecyclebinRequest(TeaModel):
    def __init__(self, drive_id=None, fields=None, limit=None, marker=None):
        self.drive_id = drive_id  # type: str
        self.fields = fields  # type: str
        self.limit = limit  # type: int
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRecyclebinRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListRecyclebinResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[File]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRecyclebinResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = File()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListRecyclebinResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRecyclebinResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRecyclebinResponse, self).to_map()
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
            temp_model = ListRecyclebinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRevisionRequest(TeaModel):
    def __init__(self, drive_id=None, fields=None, file_id=None, limit=None, marker=None):
        self.drive_id = drive_id  # type: str
        self.fields = fields  # type: str
        self.file_id = file_id  # type: str
        self.limit = limit  # type: long
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListRevisionResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[Revision]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRevisionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Revision()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListRevisionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRevisionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRevisionResponse, self).to_map()
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
            temp_model = ListRevisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShareLinkRequest(TeaModel):
    def __init__(self, creator=None, include_cancelled=None, limit=None, marker=None, order_by=None,
                 order_direction=None):
        self.creator = creator  # type: str
        self.include_cancelled = include_cancelled  # type: bool
        self.limit = limit  # type: int
        self.marker = marker  # type: str
        self.order_by = order_by  # type: str
        self.order_direction = order_direction  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListShareLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.include_cancelled is not None:
            result['include_cancelled'] = self.include_cancelled
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.order_direction is not None:
            result['order_direction'] = self.order_direction
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('include_cancelled') is not None:
            self.include_cancelled = m.get('include_cancelled')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')
        return self


class ListShareLinkResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[ShareLink]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListShareLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ShareLink()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListShareLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListShareLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListShareLinkResponse, self).to_map()
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
            temp_model = ListShareLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(self, drive_id=None, image_thumbnail_process=None, video_thumbnail_process=None):
        self.drive_id = drive_id  # type: str
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(self, tags=None):
        self.tags = tags  # type: list[ImageTag]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ImageTag()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagsResponse, self).to_map()
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
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUploadedPartsRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, limit=None, part_number_marker=None, share_id=None,
                 upload_id=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.limit = limit  # type: int
        self.part_number_marker = part_number_marker  # type: int
        self.share_id = share_id  # type: str
        self.upload_id = upload_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUploadedPartsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.part_number_marker is not None:
            result['part_number_marker'] = self.part_number_marker
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('part_number_marker') is not None:
            self.part_number_marker = m.get('part_number_marker')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class ListUploadedPartsResponseBody(TeaModel):
    def __init__(self, file_id=None, next_part_number_marker=None, parallel_upload=None, upload_id=None,
                 uploaded_parts=None):
        self.file_id = file_id  # type: str
        self.next_part_number_marker = next_part_number_marker  # type: str
        self.parallel_upload = parallel_upload  # type: bool
        self.upload_id = upload_id  # type: str
        self.uploaded_parts = uploaded_parts  # type: list[UploadPartInfo]

    def validate(self):
        if self.uploaded_parts:
            for k in self.uploaded_parts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUploadedPartsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.next_part_number_marker is not None:
            result['next_part_number_marker'] = self.next_part_number_marker
        if self.parallel_upload is not None:
            result['parallel_upload'] = self.parallel_upload
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        result['uploaded_parts'] = []
        if self.uploaded_parts is not None:
            for k in self.uploaded_parts:
                result['uploaded_parts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('next_part_number_marker') is not None:
            self.next_part_number_marker = m.get('next_part_number_marker')
        if m.get('parallel_upload') is not None:
            self.parallel_upload = m.get('parallel_upload')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        self.uploaded_parts = []
        if m.get('uploaded_parts') is not None:
            for k in m.get('uploaded_parts'):
                temp_model = UploadPartInfo()
                self.uploaded_parts.append(temp_model.from_map(k))
        return self


class ListUploadedPartsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUploadedPartsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUploadedPartsResponse, self).to_map()
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
            temp_model = ListUploadedPartsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserRequest(TeaModel):
    def __init__(self, limit=None, marker=None):
        self.limit = limit  # type: int
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListUserResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[User]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = User()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserResponse, self).to_map()
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
            temp_model = ListUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveFileRequest(TeaModel):
    def __init__(self, check_name_mode=None, drive_id=None, file_id=None, to_parent_file_id=None):
        self.check_name_mode = check_name_mode  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.to_parent_file_id = to_parent_file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.to_parent_file_id is not None:
            result['to_parent_file_id'] = self.to_parent_file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('to_parent_file_id') is not None:
            self.to_parent_file_id = m.get('to_parent_file_id')
        return self


class MoveFileResponseBody(TeaModel):
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, exist=None, file_id=None):
        self.async_task_id = async_task_id  # type: str
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str
        self.exist = exist  # type: bool
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.exist is not None:
            result['exist'] = self.exist
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('exist') is not None:
            self.exist = m.get('exist')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class MoveFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MoveFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveFileResponse, self).to_map()
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
            temp_model = MoveFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ParseKeywordsRequest(TeaModel):
    def __init__(self, keywords=None):
        self.keywords = keywords  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ParseKeywordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords is not None:
            result['keywords'] = self.keywords
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')
        return self


class ParseKeywordsResponseBodyTimeRange(TeaModel):
    def __init__(self, end=None, start=None):
        self.end = end  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ParseKeywordsResponseBodyTimeRange, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ParseKeywordsResponseBody(TeaModel):
    def __init__(self, address_line=None, tags=None, time_range=None):
        self.address_line = address_line  # type: str
        self.tags = tags  # type: list[SystemTag]
        self.time_range = time_range  # type: ParseKeywordsResponseBodyTimeRange

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        _map = super(ParseKeywordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_line is not None:
            result['address_line'] = self.address_line
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.time_range is not None:
            result['time_range'] = self.time_range.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('address_line') is not None:
            self.address_line = m.get('address_line')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = SystemTag()
                self.tags.append(temp_model.from_map(k))
        if m.get('time_range') is not None:
            temp_model = ParseKeywordsResponseBodyTimeRange()
            self.time_range = temp_model.from_map(m['time_range'])
        return self


class ParseKeywordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ParseKeywordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ParseKeywordsResponse, self).to_map()
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
            temp_model = ParseKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFaceGroupFileRequest(TeaModel):
    def __init__(self, drive_id=None, face_group_id=None, file_id=None):
        self.drive_id = drive_id  # type: str
        self.face_group_id = face_group_id  # type: str
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveFaceGroupFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.face_group_id is not None:
            result['face_group_id'] = self.face_group_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('face_group_id') is not None:
            self.face_group_id = m.get('face_group_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class RemoveFaceGroupFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(RemoveFaceGroupFileResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class RestoreFileRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class RestoreFileResponseBody(TeaModel):
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_id=None):
        self.async_task_id = async_task_id  # type: str
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class RestoreFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestoreFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestoreFileResponse, self).to_map()
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
            temp_model = RestoreFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreRevisionRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, revision_id=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.revision_id = revision_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class RestoreRevisionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Revision

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestoreRevisionResponse, self).to_map()
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
            temp_model = Revision()
            self.body = temp_model.from_map(m['body'])
        return self


class ScanFileRequest(TeaModel):
    def __init__(self, drive_id=None, fields=None, limit=None, marker=None):
        self.drive_id = drive_id  # type: str
        self.fields = fields  # type: str
        self.limit = limit  # type: int
        self.marker = marker  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScanFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ScanFileResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[File]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ScanFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = File()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ScanFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ScanFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScanFileResponse, self).to_map()
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
            temp_model = ScanFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAddressGroupsRequest(TeaModel):
    def __init__(self, address_level=None, address_names=None, br_geo_point=None, drive_id=None,
                 image_thumbnail_process=None, tl_geo_point=None, video_thumbnail_process=None):
        self.address_level = address_level  # type: str
        self.address_names = address_names  # type: list[str]
        self.br_geo_point = br_geo_point  # type: str
        self.drive_id = drive_id  # type: str
        self.image_thumbnail_process = image_thumbnail_process  # type: str
        self.tl_geo_point = tl_geo_point  # type: str
        self.video_thumbnail_process = video_thumbnail_process  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchAddressGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_level is not None:
            result['address_level'] = self.address_level
        if self.address_names is not None:
            result['address_names'] = self.address_names
        if self.br_geo_point is not None:
            result['br_geo_point'] = self.br_geo_point
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.tl_geo_point is not None:
            result['tl_geo_point'] = self.tl_geo_point
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('address_level') is not None:
            self.address_level = m.get('address_level')
        if m.get('address_names') is not None:
            self.address_names = m.get('address_names')
        if m.get('br_geo_point') is not None:
            self.br_geo_point = m.get('br_geo_point')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('tl_geo_point') is not None:
            self.tl_geo_point = m.get('tl_geo_point')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class SearchAddressGroupsResponseBody(TeaModel):
    def __init__(self, items=None):
        self.items = items  # type: list[AddressGroup]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchAddressGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = AddressGroup()
                self.items.append(temp_model.from_map(k))
        return self


class SearchAddressGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchAddressGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchAddressGroupsResponse, self).to_map()
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
            temp_model = SearchAddressGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchDriveRequest(TeaModel):
    def __init__(self, drive_name=None, limit=None, marker=None, owner=None, owner_type=None):
        self.drive_name = drive_name  # type: str
        self.limit = limit  # type: int
        self.marker = marker  # type: str
        self.owner = owner  # type: str
        self.owner_type = owner_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchDriveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        return self


class SearchDriveResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[Drive]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchDriveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Drive()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class SearchDriveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchDriveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchDriveResponse, self).to_map()
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
            temp_model = SearchDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFileRequest(TeaModel):
    def __init__(self, drive_id=None, limit=None, marker=None, order_by=None, query=None, return_total_count=None):
        self.drive_id = drive_id  # type: str
        self.limit = limit  # type: int
        self.marker = marker  # type: str
        self.order_by = order_by  # type: str
        self.query = query  # type: str
        self.return_total_count = return_total_count  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.query is not None:
            result['query'] = self.query
        if self.return_total_count is not None:
            result['return_total_count'] = self.return_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('return_total_count') is not None:
            self.return_total_count = m.get('return_total_count')
        return self


class SearchFileResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None, total_count=None):
        self.items = items  # type: list[File]
        self.next_marker = next_marker  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = File()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class SearchFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchFileResponse, self).to_map()
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
            temp_model = SearchFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchShareLinkRequest(TeaModel):
    def __init__(self, creators=None, limit=None, marker=None, order_by=None, order_direction=None, query=None,
                 return_total_count=None):
        self.creators = creators  # type: list[str]
        self.limit = limit  # type: int
        self.marker = marker  # type: str
        self.order_by = order_by  # type: str
        self.order_direction = order_direction  # type: str
        self.query = query  # type: str
        self.return_total_count = return_total_count  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchShareLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creators is not None:
            result['creators'] = self.creators
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.order_direction is not None:
            result['order_direction'] = self.order_direction
        if self.query is not None:
            result['query'] = self.query
        if self.return_total_count is not None:
            result['return_total_count'] = self.return_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creators') is not None:
            self.creators = m.get('creators')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('return_total_count') is not None:
            self.return_total_count = m.get('return_total_count')
        return self


class SearchShareLinkResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None, total_count=None):
        self.items = items  # type: list[ShareLink]
        self.next_marker = next_marker  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchShareLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ShareLink()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class SearchShareLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchShareLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchShareLinkResponse, self).to_map()
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
            temp_model = SearchShareLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchUserRequest(TeaModel):
    def __init__(self, email=None, limit=None, marker=None, nick_name=None, nick_name_for_fuzzy=None, phone=None,
                 role=None, status=None, user_name=None):
        self.email = email  # type: str
        self.limit = limit  # type: int
        self.marker = marker  # type: str
        self.nick_name = nick_name  # type: str
        self.nick_name_for_fuzzy = nick_name_for_fuzzy  # type: str
        self.phone = phone  # type: str
        self.role = role  # type: str
        self.status = status  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.nick_name_for_fuzzy is not None:
            result['nick_name_for_fuzzy'] = self.nick_name_for_fuzzy
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('nick_name_for_fuzzy') is not None:
            self.nick_name_for_fuzzy = m.get('nick_name_for_fuzzy')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class SearchUserResponseBody(TeaModel):
    def __init__(self, items=None, next_marker=None):
        self.items = items  # type: list[User]
        self.next_marker = next_marker  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = User()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class SearchUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchUserResponse, self).to_map()
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
            temp_model = SearchUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TokenRequest(TeaModel):
    def __init__(self, assertion=None, client_id=None, client_secret=None, code=None, grant_type=None,
                 redirect_uri=None, refresh_token=None):
        self.assertion = assertion  # type: str
        self.client_id = client_id  # type: str
        self.client_secret = client_secret  # type: str
        self.code = code  # type: str
        self.grant_type = grant_type  # type: str
        self.redirect_uri = redirect_uri  # type: str
        self.refresh_token = refresh_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assertion is not None:
            result['assertion'] = self.assertion
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.client_secret is not None:
            result['client_secret'] = self.client_secret
        if self.code is not None:
            result['code'] = self.code
        if self.grant_type is not None:
            result['grant_type'] = self.grant_type
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assertion') is not None:
            self.assertion = m.get('assertion')
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('grant_type') is not None:
            self.grant_type = m.get('grant_type')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        return self


class TokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Token

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TokenResponse, self).to_map()
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
            temp_model = Token()
            self.body = temp_model.from_map(m['body'])
        return self


class TrashFileRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TrashFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class TrashFileResponseBody(TeaModel):
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_id=None):
        self.async_task_id = async_task_id  # type: str
        self.domain_id = domain_id  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TrashFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class TrashFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TrashFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TrashFileResponse, self).to_map()
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
            temp_model = TrashFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDriveRequest(TeaModel):
    def __init__(self, description=None, drive_id=None, drive_name=None, status=None, total_size=None):
        self.description = description  # type: str
        self.drive_id = drive_id  # type: str
        self.drive_name = drive_name  # type: str
        self.status = status  # type: str
        self.total_size = total_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateDriveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.status is not None:
            result['status'] = self.status
        if self.total_size is not None:
            result['total_size'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        return self


class UpdateDriveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Drive

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateDriveResponse, self).to_map()
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
            temp_model = Drive()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFacegroupRequest(TeaModel):
    def __init__(self, drive_id=None, group_cover_face_id=None, group_id=None, group_name=None, remarks=None):
        self.drive_id = drive_id  # type: str
        self.group_cover_face_id = group_cover_face_id  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.remarks = remarks  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFacegroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.group_cover_face_id is not None:
            result['group_cover_face_id'] = self.group_cover_face_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('group_cover_face_id') is not None:
            self.group_cover_face_id = m.get('group_cover_face_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        return self


class UpdateFacegroupResponseBody(TeaModel):
    def __init__(self, drive_id=None, group_id=None):
        self.drive_id = drive_id  # type: str
        self.group_id = group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFacegroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class UpdateFacegroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFacegroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFacegroupResponse, self).to_map()
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
            temp_model = UpdateFacegroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileRequest(TeaModel):
    def __init__(self, check_name_mode=None, description=None, drive_id=None, file_id=None, hidden=None, labels=None,
                 local_modified_at=None, name=None, starred=None):
        self.check_name_mode = check_name_mode  # type: str
        self.description = description  # type: str
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.hidden = hidden  # type: bool
        self.labels = labels  # type: list[str]
        self.local_modified_at = local_modified_at  # type: str
        self.name = name  # type: str
        self.starred = starred  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.labels is not None:
            result['labels'] = self.labels
        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at
        if self.name is not None:
            result['name'] = self.name
        if self.starred is not None:
            result['starred'] = self.starred
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        return self


class UpdateFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: File

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFileResponse, self).to_map()
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
            temp_model = File()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(self, description=None, group_id=None, group_name=None):
        self.description = description  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Group

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupResponse, self).to_map()
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
            temp_model = Group()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRevisionRequest(TeaModel):
    def __init__(self, drive_id=None, file_id=None, keep_forever=None, revision_description=None, revision_id=None):
        self.drive_id = drive_id  # type: str
        self.file_id = file_id  # type: str
        self.keep_forever = keep_forever  # type: bool
        self.revision_description = revision_description  # type: str
        self.revision_id = revision_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRevisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.keep_forever is not None:
            result['keep_forever'] = self.keep_forever
        if self.revision_description is not None:
            result['revision_description'] = self.revision_description
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('keep_forever') is not None:
            self.keep_forever = m.get('keep_forever')
        if m.get('revision_description') is not None:
            self.revision_description = m.get('revision_description')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class UpdateRevisionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Revision

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRevisionResponse, self).to_map()
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
            temp_model = Revision()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateShareLinkRequest(TeaModel):
    def __init__(self, description=None, disable_download=None, disable_preview=None, disable_save=None,
                 download_count=None, download_limit=None, expiration=None, preview_count=None, preview_limit=None,
                 report_count=None, save_count=None, save_limit=None, share_id=None, share_name=None, share_pwd=None, status=None,
                 video_preview_count=None):
        self.description = description  # type: str
        self.disable_download = disable_download  # type: bool
        self.disable_preview = disable_preview  # type: bool
        self.disable_save = disable_save  # type: bool
        self.download_count = download_count  # type: long
        self.download_limit = download_limit  # type: long
        self.expiration = expiration  # type: str
        self.preview_count = preview_count  # type: long
        self.preview_limit = preview_limit  # type: long
        self.report_count = report_count  # type: long
        self.save_count = save_count  # type: long
        self.save_limit = save_limit  # type: long
        self.share_id = share_id  # type: str
        self.share_name = share_name  # type: str
        self.share_pwd = share_pwd  # type: str
        self.status = status  # type: str
        self.video_preview_count = video_preview_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateShareLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.disable_download is not None:
            result['disable_download'] = self.disable_download
        if self.disable_preview is not None:
            result['disable_preview'] = self.disable_preview
        if self.disable_save is not None:
            result['disable_save'] = self.disable_save
        if self.download_count is not None:
            result['download_count'] = self.download_count
        if self.download_limit is not None:
            result['download_limit'] = self.download_limit
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.preview_count is not None:
            result['preview_count'] = self.preview_count
        if self.preview_limit is not None:
            result['preview_limit'] = self.preview_limit
        if self.report_count is not None:
            result['report_count'] = self.report_count
        if self.save_count is not None:
            result['save_count'] = self.save_count
        if self.save_limit is not None:
            result['save_limit'] = self.save_limit
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.status is not None:
            result['status'] = self.status
        if self.video_preview_count is not None:
            result['video_preview_count'] = self.video_preview_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('disable_download') is not None:
            self.disable_download = m.get('disable_download')
        if m.get('disable_preview') is not None:
            self.disable_preview = m.get('disable_preview')
        if m.get('disable_save') is not None:
            self.disable_save = m.get('disable_save')
        if m.get('download_count') is not None:
            self.download_count = m.get('download_count')
        if m.get('download_limit') is not None:
            self.download_limit = m.get('download_limit')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('preview_count') is not None:
            self.preview_count = m.get('preview_count')
        if m.get('preview_limit') is not None:
            self.preview_limit = m.get('preview_limit')
        if m.get('report_count') is not None:
            self.report_count = m.get('report_count')
        if m.get('save_count') is not None:
            self.save_count = m.get('save_count')
        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('video_preview_count') is not None:
            self.video_preview_count = m.get('video_preview_count')
        return self


class UpdateShareLinkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ShareLink

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateShareLinkResponse, self).to_map()
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
            temp_model = ShareLink()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequestGroupInfoList(TeaModel):
    def __init__(self, group_id=None):
        self.group_id = group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserRequestGroupInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class UpdateUserRequest(TeaModel):
    def __init__(self, avatar=None, description=None, email=None, group_info_list=None, nick_name=None, phone=None,
                 role=None, status=None, user_data=None, user_id=None):
        self.avatar = avatar  # type: str
        self.description = description  # type: str
        self.email = email  # type: str
        self.group_info_list = group_info_list  # type: list[UpdateUserRequestGroupInfoList]
        self.nick_name = nick_name  # type: str
        self.phone = phone  # type: str
        self.role = role  # type: str
        self.status = status  # type: str
        self.user_data = user_data  # type: dict[str, str]
        self.user_id = user_id  # type: str

    def validate(self):
        if self.group_info_list:
            for k in self.group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.description is not None:
            result['description'] = self.description
        if self.email is not None:
            result['email'] = self.email
        result['group_info_list'] = []
        if self.group_info_list is not None:
            for k in self.group_info_list:
                result['group_info_list'].append(k.to_map() if k else None)
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('email') is not None:
            self.email = m.get('email')
        self.group_info_list = []
        if m.get('group_info_list') is not None:
            for k in m.get('group_info_list'):
                temp_model = UpdateUserRequestGroupInfoList()
                self.group_info_list.append(temp_model.from_map(k))
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: User

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserResponse, self).to_map()
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
            temp_model = User()
            self.body = temp_model.from_map(m['body'])
        return self


