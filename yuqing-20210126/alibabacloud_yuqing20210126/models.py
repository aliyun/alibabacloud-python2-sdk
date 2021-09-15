# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ReportNotifyRecord(TeaModel):
    def __init__(self, conf=None, cp_id=None, gmt_create_timestamp=None, gmt_create_format=None,
                 gmt_modified_timestamp=None, id=None, share_key=None, subject=None, success=None, type=None, uid_create=None,
                 uname_create=None, valid=None):
        # 配置： 如图片宽度/接收人/抄送人等
        self.conf = conf  # type: str
        # 自定义页面id
        self.cp_id = cp_id  # type: long
        # 创建时间，毫秒
        self.gmt_create_timestamp = gmt_create_timestamp  # type: long
        # 格式化的创建时间
        self.gmt_create_format = gmt_create_format  # type: str
        # 修改时间，毫秒
        self.gmt_modified_timestamp = gmt_modified_timestamp  # type: long
        # 记录id
        self.id = id  # type: long
        # cpId对应的共享key，用于共享报告
        self.share_key = share_key  # type: str
        # 主题
        self.subject = subject  # type: str
        # 是否成功的标志，1表示成功，否则表示不成功
        self.success = success  # type: long
        # 类型： 如邮件、钉钉等
        self.type = type  # type: long
        # 创建人id
        self.uid_create = uid_create  # type: str
        # 创建人名字
        self.uname_create = uname_create  # type: str
        # 状态，1为生效，0为失效。
        self.valid = valid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportNotifyRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conf is not None:
            result['conf'] = self.conf
        if self.cp_id is not None:
            result['cpId'] = self.cp_id
        if self.gmt_create_timestamp is not None:
            result['gmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_create_format is not None:
            result['gmtCreateFormat'] = self.gmt_create_format
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.id is not None:
            result['id'] = self.id
        if self.share_key is not None:
            result['shareKey'] = self.share_key
        if self.subject is not None:
            result['subject'] = self.subject
        if self.success is not None:
            result['success'] = self.success
        if self.type is not None:
            result['type'] = self.type
        if self.uid_create is not None:
            result['uidCreate'] = self.uid_create
        if self.uname_create is not None:
            result['unameCreate'] = self.uname_create
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('conf') is not None:
            self.conf = m.get('conf')
        if m.get('cpId') is not None:
            self.cp_id = m.get('cpId')
        if m.get('gmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('gmtCreateTimestamp')
        if m.get('gmtCreateFormat') is not None:
            self.gmt_create_format = m.get('gmtCreateFormat')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('shareKey') is not None:
            self.share_key = m.get('shareKey')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uidCreate') is not None:
            self.uid_create = m.get('uidCreate')
        if m.get('unameCreate') is not None:
            self.uname_create = m.get('unameCreate')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class FinanceEvent(TeaModel):
    def __init__(self, entity_area=None, entity_id=None, entity_name=None, entity_relevance_score=None,
                 entity_summary=None, entity_type=None, event_code=None, event_id=None, event_name=None, entity_crn=None):
        # 实体地理位置
        self.entity_area = entity_area  # type: str
        # 实体ID
        self.entity_id = entity_id  # type: str
        # 实体名称
        self.entity_name = entity_name  # type: str
        # 实体相关度得分
        self.entity_relevance_score = entity_relevance_score  # type: str
        # 实体的事件摘要描述
        self.entity_summary = entity_summary  # type: str
        # 实体类型，枚举值
        self.entity_type = entity_type  # type: str
        # 事件码
        self.event_code = event_code  # type: long
        # 事件id
        self.event_id = event_id  # type: str
        # 事件名称
        self.event_name = event_name  # type: str
        # 实体唯一id，统一社会信用代码
        self.entity_crn = entity_crn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinanceEvent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_area is not None:
            result['entityArea'] = self.entity_area
        if self.entity_id is not None:
            result['entityId'] = self.entity_id
        if self.entity_name is not None:
            result['entityName'] = self.entity_name
        if self.entity_relevance_score is not None:
            result['entityRelevanceScore'] = self.entity_relevance_score
        if self.entity_summary is not None:
            result['entitySummary'] = self.entity_summary
        if self.entity_type is not None:
            result['entityType'] = self.entity_type
        if self.event_code is not None:
            result['eventCode'] = self.event_code
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.event_name is not None:
            result['eventName'] = self.event_name
        if self.entity_crn is not None:
            result['entityCrn'] = self.entity_crn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('entityArea') is not None:
            self.entity_area = m.get('entityArea')
        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')
        if m.get('entityName') is not None:
            self.entity_name = m.get('entityName')
        if m.get('entityRelevanceScore') is not None:
            self.entity_relevance_score = m.get('entityRelevanceScore')
        if m.get('entitySummary') is not None:
            self.entity_summary = m.get('entitySummary')
        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')
        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')
        if m.get('entityCrn') is not None:
            self.entity_crn = m.get('entityCrn')
        return self


class YuqingHotspotMessage(TeaModel):
    def __init__(self, crawler_time_fmt=None, doc_content=None, doc_id=None, doc_title=None, doc_url=None,
                 first_exist_timestamp=None, first_hot_value=None, first_rank=None, hot_value=None, hotspot_type=None,
                 last_exist_timestamp=None, last_rank=None, max_hot_value=None, max_rank=None, media_sub_type=None, media_type=None,
                 rank=None, reads_count=None, total_exist_timestamp=None, comments_count=None, discusses_count=None,
                 original_count=None, video_count=None, followers_count=None, screen_name=None, user_id=None, category=None):
        # 爬虫爬取的时间
        self.crawler_time_fmt = crawler_time_fmt  # type: str
        # 内容，热榜数据中存在着文章，热文就是有内容的
        self.doc_content = doc_content  # type: str
        # 文档id
        self.doc_id = doc_id  # type: str
        # 标题，例如话题的标题就是话题本身
        self.doc_title = doc_title  # type: str
        # 链接地址
        self.doc_url = doc_url  # type: str
        # 第一次上榜的时间
        self.first_exist_timestamp = first_exist_timestamp  # type: long
        # 首次上榜热度
        self.first_hot_value = first_hot_value  # type: long
        # 首次上榜排名
        self.first_rank = first_rank  # type: int
        # 热度值
        self.hot_value = hot_value  # type: long
        # 热搜内容类型
        self.hotspot_type = hotspot_type  # type: str
        # 最后一次上榜的时间
        self.last_exist_timestamp = last_exist_timestamp  # type: long
        # 下榜排名
        self.last_rank = last_rank  # type: int
        # 最大的热度值
        self.max_hot_value = max_hot_value  # type: long
        # 在榜单中的最高排名
        self.max_rank = max_rank  # type: int
        # 渠道子类型
        self.media_sub_type = media_sub_type  # type: str
        # 渠道类型
        self.media_type = media_type  # type: str
        # 热搜在热搜榜的位置
        self.rank = rank  # type: int
        # 阅读数
        self.reads_count = reads_count  # type: long
        # 在榜总时间
        self.total_exist_timestamp = total_exist_timestamp  # type: long
        # 评论数
        self.comments_count = comments_count  # type: long
        # 讨论数
        self.discusses_count = discusses_count  # type: long
        # 原创人数
        self.original_count = original_count  # type: long
        # 视频量
        self.video_count = video_count  # type: long
        # 跟随量
        self.followers_count = followers_count  # type: long
        # 用户名
        self.screen_name = screen_name  # type: str
        # 用户id
        self.user_id = user_id  # type: str
        # 分类
        self.category = category  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(YuqingHotspotMessage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crawler_time_fmt is not None:
            result['crawlerTimeFmt'] = self.crawler_time_fmt
        if self.doc_content is not None:
            result['docContent'] = self.doc_content
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.doc_title is not None:
            result['docTitle'] = self.doc_title
        if self.doc_url is not None:
            result['docUrl'] = self.doc_url
        if self.first_exist_timestamp is not None:
            result['firstExistTimestamp'] = self.first_exist_timestamp
        if self.first_hot_value is not None:
            result['firstHotValue'] = self.first_hot_value
        if self.first_rank is not None:
            result['firstRank'] = self.first_rank
        if self.hot_value is not None:
            result['hotValue'] = self.hot_value
        if self.hotspot_type is not None:
            result['hotspotType'] = self.hotspot_type
        if self.last_exist_timestamp is not None:
            result['lastExistTimestamp'] = self.last_exist_timestamp
        if self.last_rank is not None:
            result['lastRank'] = self.last_rank
        if self.max_hot_value is not None:
            result['maxHotValue'] = self.max_hot_value
        if self.max_rank is not None:
            result['maxRank'] = self.max_rank
        if self.media_sub_type is not None:
            result['mediaSubType'] = self.media_sub_type
        if self.media_type is not None:
            result['mediaType'] = self.media_type
        if self.rank is not None:
            result['rank'] = self.rank
        if self.reads_count is not None:
            result['readsCount'] = self.reads_count
        if self.total_exist_timestamp is not None:
            result['totalExistTimestamp'] = self.total_exist_timestamp
        if self.comments_count is not None:
            result['commentsCount'] = self.comments_count
        if self.discusses_count is not None:
            result['discussesCount'] = self.discusses_count
        if self.original_count is not None:
            result['originalCount'] = self.original_count
        if self.video_count is not None:
            result['videoCount'] = self.video_count
        if self.followers_count is not None:
            result['followersCount'] = self.followers_count
        if self.screen_name is not None:
            result['screenName'] = self.screen_name
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.category is not None:
            result['category'] = self.category
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('crawlerTimeFmt') is not None:
            self.crawler_time_fmt = m.get('crawlerTimeFmt')
        if m.get('docContent') is not None:
            self.doc_content = m.get('docContent')
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('docTitle') is not None:
            self.doc_title = m.get('docTitle')
        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')
        if m.get('firstExistTimestamp') is not None:
            self.first_exist_timestamp = m.get('firstExistTimestamp')
        if m.get('firstHotValue') is not None:
            self.first_hot_value = m.get('firstHotValue')
        if m.get('firstRank') is not None:
            self.first_rank = m.get('firstRank')
        if m.get('hotValue') is not None:
            self.hot_value = m.get('hotValue')
        if m.get('hotspotType') is not None:
            self.hotspot_type = m.get('hotspotType')
        if m.get('lastExistTimestamp') is not None:
            self.last_exist_timestamp = m.get('lastExistTimestamp')
        if m.get('lastRank') is not None:
            self.last_rank = m.get('lastRank')
        if m.get('maxHotValue') is not None:
            self.max_hot_value = m.get('maxHotValue')
        if m.get('maxRank') is not None:
            self.max_rank = m.get('maxRank')
        if m.get('mediaSubType') is not None:
            self.media_sub_type = m.get('mediaSubType')
        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')
        if m.get('rank') is not None:
            self.rank = m.get('rank')
        if m.get('readsCount') is not None:
            self.reads_count = m.get('readsCount')
        if m.get('totalExistTimestamp') is not None:
            self.total_exist_timestamp = m.get('totalExistTimestamp')
        if m.get('commentsCount') is not None:
            self.comments_count = m.get('commentsCount')
        if m.get('discussesCount') is not None:
            self.discusses_count = m.get('discussesCount')
        if m.get('originalCount') is not None:
            self.original_count = m.get('originalCount')
        if m.get('videoCount') is not None:
            self.video_count = m.get('videoCount')
        if m.get('followersCount') is not None:
            self.followers_count = m.get('followersCount')
        if m.get('screenName') is not None:
            self.screen_name = m.get('screenName')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('category') is not None:
            self.category = m.get('category')
        return self


class HotspotSearchCondition(TeaModel):
    def __init__(self, query_without_keyword=None, sort_by_direction=None, page_now=None, page_size=None,
                 sort_by=None, enable_keyword_highlight=None, media_type=None, media_sub_type=None,
                 crawler_time_start_filter=None, crawler_time_end_filter=None, pos_keywords=None, title_including_words_idx=None,
                 active=None):
        # 默认false，表示需要指定关键词来查询
        self.query_without_keyword = query_without_keyword  # type: bool
        # 排序方式： 正序(+)、倒序(-)
        self.sort_by_direction = sort_by_direction  # type: str
        # 当前页
        self.page_now = page_now  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 排序字段
        self.sort_by = sort_by  # type: str
        # 是否要进行关键词高亮显示
        self.enable_keyword_highlight = enable_keyword_highlight  # type: bool
        # 媒体类型：热搜、热榜还是话题
        self.media_type = media_type  # type: str
        # 媒体子类型：头条热搜，微博热搜
        self.media_sub_type = media_sub_type  # type: str
        # 爬取时间的最小值（含）
        self.crawler_time_start_filter = crawler_time_start_filter  # type: long
        # 爬取时间的最大值（不含）
        self.crawler_time_end_filter = crawler_time_end_filter  # type: long
        # 关键词
        self.pos_keywords = pos_keywords  # type: str
        # 标题包含词
        self.title_including_words_idx = title_including_words_idx  # type: str
        # 是否在榜
        self.active = active  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(HotspotSearchCondition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_without_keyword is not None:
            result['queryWithoutKeyword'] = self.query_without_keyword
        if self.sort_by_direction is not None:
            result['sortByDirection'] = self.sort_by_direction
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.enable_keyword_highlight is not None:
            result['enableKeywordHighlight'] = self.enable_keyword_highlight
        if self.media_type is not None:
            result['mediaType'] = self.media_type
        if self.media_sub_type is not None:
            result['mediaSubType'] = self.media_sub_type
        if self.crawler_time_start_filter is not None:
            result['crawlerTimeStartFilter'] = self.crawler_time_start_filter
        if self.crawler_time_end_filter is not None:
            result['crawlerTimeEndFilter'] = self.crawler_time_end_filter
        if self.pos_keywords is not None:
            result['posKeywords'] = self.pos_keywords
        if self.title_including_words_idx is not None:
            result['titleIncludingWordsIdx'] = self.title_including_words_idx
        if self.active is not None:
            result['active'] = self.active
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('queryWithoutKeyword') is not None:
            self.query_without_keyword = m.get('queryWithoutKeyword')
        if m.get('sortByDirection') is not None:
            self.sort_by_direction = m.get('sortByDirection')
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('enableKeywordHighlight') is not None:
            self.enable_keyword_highlight = m.get('enableKeywordHighlight')
        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')
        if m.get('mediaSubType') is not None:
            self.media_sub_type = m.get('mediaSubType')
        if m.get('crawlerTimeStartFilter') is not None:
            self.crawler_time_start_filter = m.get('crawlerTimeStartFilter')
        if m.get('crawlerTimeEndFilter') is not None:
            self.crawler_time_end_filter = m.get('crawlerTimeEndFilter')
        if m.get('posKeywords') is not None:
            self.pos_keywords = m.get('posKeywords')
        if m.get('titleIncludingWordsIdx') is not None:
            self.title_including_words_idx = m.get('titleIncludingWordsIdx')
        if m.get('active') is not None:
            self.active = m.get('active')
        return self


class YuqingMessage(TeaModel):
    def __init__(self, doc_id=None, advertisement=None, alipay_account=None, at_author_names=None,
                 author_avatar_url=None, author_followers_count=None, author_friends_count=None, author_id=None, author_name=None,
                 author_profile_url=None, author_statuses_count=None, author_verify_type=None, bkz=None, content_audio_text=None,
                 content_audio_urls=None, content_emotion_type=None, content_image_text=None, content_image_urls=None,
                 content_video_text=None, content_video_urls=None, doc_create_time=None, doc_publish_time=None,
                 doc_answers_count=None, doc_areas=None, doc_comments_count=None, doc_content=None, doc_content_brief=None,
                 doc_content_sign=None, doc_focus_article_count=None, doc_likes_count=None, doc_message_type=None,
                 doc_parent_id=None, doc_reads_count=None, doc_reposts_count=None, doc_self_content_sign=None, doc_title=None,
                 doc_title_brief=None, doc_url=None, doc_user_define_json=None, emotion_score=None, entity_alias=None,
                 entity_relevancy_score=None, eroticism=None, eroticism_score_fmt=None, gambling=None, highlight_ass_keywords=None,
                 highlight_keywords=None, highlight_pos_keywords=None, image_count=None, media_hosts=None, media_influence_level=None,
                 media_influence_score=None, media_name=None, media_propagation_score=None, media_qun_name=None, media_res_city=None,
                 media_res_country=None, media_res_province=None, media_type=None, original_media=None, relevance_score_fmt=None,
                 similar_number=None, spam=None, weibo_comment_id=None, weibo_mid=None, ue_emotion_score=None, finance_events=None,
                 app_store_app_score=None, app_store_app_name=None, app_store_name=None):
        # 舆情文章唯一ID
        self.doc_id = doc_id  # type: str
        # 广告
        self.advertisement = advertisement  # type: bool
        # 2088账号
        self.alipay_account = alipay_account  # type: long
        # 被at的用户名列表
        self.at_author_names = at_author_names  # type: list[str]
        # 用户头像地址
        self.author_avatar_url = author_avatar_url  # type: str
        # 作者粉丝数
        self.author_followers_count = author_followers_count  # type: long
        # 作者好友数
        self.author_friends_count = author_friends_count  # type: long
        # 外部平台作者id
        self.author_id = author_id  # type: str
        # 作者名称
        self.author_name = author_name  # type: str
        # 个人主页地址
        self.author_profile_url = author_profile_url  # type: str
        # 发布微博数
        self.author_statuses_count = author_statuses_count  # type: long
        # 作者认证类型
        self.author_verify_type = author_verify_type  # type: str
        # 敏感暴恐政
        self.bkz = bkz  # type: bool
        # 音频识别出来的文字
        self.content_audio_text = content_audio_text  # type: str
        # 音频地址
        self.content_audio_urls = content_audio_urls  # type: str
        # 情感的正负面，-1代表负面，1代表非负面
        self.content_emotion_type = content_emotion_type  # type: int
        # 从图片识别出来文字
        self.content_image_text = content_image_text  # type: str
        # 内容中的图片列表
        self.content_image_urls = content_image_urls  # type: str
        # 视频识别出来的文字
        self.content_video_text = content_video_text  # type: str
        # 视频地址
        self.content_video_urls = content_video_urls  # type: str
        # 舆情文章入库时间戳
        self.doc_create_time = doc_create_time  # type: long
        # 舆情文章的发布时间戳
        self.doc_publish_time = doc_publish_time  # type: long
        # 回答数
        self.doc_answers_count = doc_answers_count  # type: long
        # 新闻用内容提取的地名,微博用用户的地名,映射归一化
        self.doc_areas = doc_areas  # type: list[str]
        # 文章评论数
        self.doc_comments_count = doc_comments_count  # type: long
        # 舆情消息内容
        self.doc_content = doc_content  # type: str
        # 文章内容概要，无Html标签，最长保留200个字
        self.doc_content_brief = doc_content_brief  # type: str
        # 文章内容签名，如果是转发微博或者其他有父内容的doc，计算的是父文章的得分。一般用于去重，相同的doc_content_sign说明内容相同
        self.doc_content_sign = doc_content_sign  # type: str
        # 文章的关注数
        self.doc_focus_article_count = doc_focus_article_count  # type: long
        # 文章点赞数
        self.doc_likes_count = doc_likes_count  # type: long
        # 舆情消息类型:转发,评论/回复, 原文,群聊等
        self.doc_message_type = doc_message_type  # type: str
        # 父文章DocID, 比如转发微博的父Id是源微博DocId
        self.doc_parent_id = doc_parent_id  # type: str
        # 阅读数
        self.doc_reads_count = doc_reads_count  # type: long
        # 转载数
        self.doc_reposts_count = doc_reposts_count  # type: long
        # 文章自身的内容签名，转发微博计算的是转发内容的contentSign，与父微博无关
        self.doc_self_content_sign = doc_self_content_sign  # type: str
        # 文章的标题
        self.doc_title = doc_title  # type: str
        # 文章标题，无Html标签
        self.doc_title_brief = doc_title_brief  # type: str
        # 原文链接
        self.doc_url = doc_url  # type: str
        # 业务自定义字段透传docUserDefineJson
        self.doc_user_define_json = doc_user_define_json  # type: str
        # 情感得分
        self.emotion_score = emotion_score  # type: str
        # 实体别名
        self.entity_alias = entity_alias  # type: str
        # 实体相关度得分，0-1,两位小数
        self.entity_relevancy_score = entity_relevancy_score  # type: str
        # 是否色情内容
        self.eroticism = eroticism  # type: bool
        # 内容的暴恐政色得分，0-10，值越大说明内容越敏感
        self.eroticism_score_fmt = eroticism_score_fmt  # type: str
        # 是否涉及赌博
        self.gambling = gambling  # type: bool
        # 如果查询条件中有搭配词，那么这个字段存储文章中命中的搭配词列表
        self.highlight_ass_keywords = highlight_ass_keywords  # type: list[str]
        # 在指定关键词、搭配词的情况下，返回文章内命中的词列表
        self.highlight_keywords = highlight_keywords  # type: list[str]
        # 如果查询条件中有关键词，那么这个字段保存文章中命中的关键词列表
        self.highlight_pos_keywords = highlight_pos_keywords  # type: list[str]
        # 文章内容中的图片个数
        self.image_count = image_count  # type: long
        # 站点来源host列表
        self.media_hosts = media_hosts  # type: list[str]
        # 媒体影响力等级，0-4，值越大影响力越大
        self.media_influence_level = media_influence_level  # type: int
        # 媒体影响力 0-10,两位小数
        self.media_influence_score = media_influence_score  # type: str
        # 媒体名称
        self.media_name = media_name  # type: str
        # 媒体传播得分，0-10,两位小数
        self.media_propagation_score = media_propagation_score  # type: str
        # IM软件群聊天名称
        self.media_qun_name = media_qun_name  # type: str
        # 媒体地域信息: 城市
        self.media_res_city = media_res_city  # type: str
        # 媒体地域信息: 国家
        self.media_res_country = media_res_country  # type: str
        # 媒体地域信息: 省份
        self.media_res_province = media_res_province  # type: str
        # 媒体类型，枚举值
        self.media_type = media_type  # type: str
        # 疑似首发媒体列表
        self.original_media = original_media  # type: list[str]
        # 关键词/搭配词与文章内容的相关性得分，0-10分，值越大相关性越高
        self.relevance_score_fmt = relevance_score_fmt  # type: str
        # 相似文章数
        self.similar_number = similar_number  # type: int
        # 是否垃圾内容
        self.spam = spam  # type: bool
        # 微博评论的外部ID
        self.weibo_comment_id = weibo_comment_id  # type: str
        # 微博外部ID
        self.weibo_mid = weibo_mid  # type: str
        # 用户情感分值
        self.ue_emotion_score = ue_emotion_score  # type: str
        # 舆情文章提取出来的金融事件列表
        self.finance_events = finance_events  # type: list[FinanceEvent]
        # appstore应用评分
        self.app_store_app_score = app_store_app_score  # type: long
        # 应用名称
        self.app_store_app_name = app_store_app_name  # type: str
        # 应用市场名称
        self.app_store_name = app_store_name  # type: str

    def validate(self):
        if self.finance_events:
            for k in self.finance_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(YuqingMessage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.advertisement is not None:
            result['advertisement'] = self.advertisement
        if self.alipay_account is not None:
            result['alipayAccount'] = self.alipay_account
        if self.at_author_names is not None:
            result['atAuthorNames'] = self.at_author_names
        if self.author_avatar_url is not None:
            result['authorAvatarUrl'] = self.author_avatar_url
        if self.author_followers_count is not None:
            result['authorFollowersCount'] = self.author_followers_count
        if self.author_friends_count is not None:
            result['authorFriendsCount'] = self.author_friends_count
        if self.author_id is not None:
            result['authorId'] = self.author_id
        if self.author_name is not None:
            result['authorName'] = self.author_name
        if self.author_profile_url is not None:
            result['authorProfileUrl'] = self.author_profile_url
        if self.author_statuses_count is not None:
            result['authorStatusesCount'] = self.author_statuses_count
        if self.author_verify_type is not None:
            result['authorVerifyType'] = self.author_verify_type
        if self.bkz is not None:
            result['bkz'] = self.bkz
        if self.content_audio_text is not None:
            result['contentAudioText'] = self.content_audio_text
        if self.content_audio_urls is not None:
            result['contentAudioUrls'] = self.content_audio_urls
        if self.content_emotion_type is not None:
            result['contentEmotionType'] = self.content_emotion_type
        if self.content_image_text is not None:
            result['contentImageText'] = self.content_image_text
        if self.content_image_urls is not None:
            result['contentImageUrls'] = self.content_image_urls
        if self.content_video_text is not None:
            result['contentVideoText'] = self.content_video_text
        if self.content_video_urls is not None:
            result['contentVideoUrls'] = self.content_video_urls
        if self.doc_create_time is not None:
            result['docCreateTime'] = self.doc_create_time
        if self.doc_publish_time is not None:
            result['docPublishTime'] = self.doc_publish_time
        if self.doc_answers_count is not None:
            result['docAnswersCount'] = self.doc_answers_count
        if self.doc_areas is not None:
            result['docAreas'] = self.doc_areas
        if self.doc_comments_count is not None:
            result['docCommentsCount'] = self.doc_comments_count
        if self.doc_content is not None:
            result['docContent'] = self.doc_content
        if self.doc_content_brief is not None:
            result['docContentBrief'] = self.doc_content_brief
        if self.doc_content_sign is not None:
            result['docContentSign'] = self.doc_content_sign
        if self.doc_focus_article_count is not None:
            result['docFocusArticleCount'] = self.doc_focus_article_count
        if self.doc_likes_count is not None:
            result['docLikesCount'] = self.doc_likes_count
        if self.doc_message_type is not None:
            result['docMessageType'] = self.doc_message_type
        if self.doc_parent_id is not None:
            result['docParentId'] = self.doc_parent_id
        if self.doc_reads_count is not None:
            result['docReadsCount'] = self.doc_reads_count
        if self.doc_reposts_count is not None:
            result['docRepostsCount'] = self.doc_reposts_count
        if self.doc_self_content_sign is not None:
            result['docSelfContentSign'] = self.doc_self_content_sign
        if self.doc_title is not None:
            result['docTitle'] = self.doc_title
        if self.doc_title_brief is not None:
            result['docTitleBrief'] = self.doc_title_brief
        if self.doc_url is not None:
            result['docUrl'] = self.doc_url
        if self.doc_user_define_json is not None:
            result['docUserDefineJson'] = self.doc_user_define_json
        if self.emotion_score is not None:
            result['emotionScore'] = self.emotion_score
        if self.entity_alias is not None:
            result['entityAlias'] = self.entity_alias
        if self.entity_relevancy_score is not None:
            result['entityRelevancyScore'] = self.entity_relevancy_score
        if self.eroticism is not None:
            result['eroticism'] = self.eroticism
        if self.eroticism_score_fmt is not None:
            result['eroticismScoreFmt'] = self.eroticism_score_fmt
        if self.gambling is not None:
            result['gambling'] = self.gambling
        if self.highlight_ass_keywords is not None:
            result['highlightAssKeywords'] = self.highlight_ass_keywords
        if self.highlight_keywords is not None:
            result['highlightKeywords'] = self.highlight_keywords
        if self.highlight_pos_keywords is not None:
            result['highlightPosKeywords'] = self.highlight_pos_keywords
        if self.image_count is not None:
            result['imageCount'] = self.image_count
        if self.media_hosts is not None:
            result['mediaHosts'] = self.media_hosts
        if self.media_influence_level is not None:
            result['mediaInfluenceLevel'] = self.media_influence_level
        if self.media_influence_score is not None:
            result['mediaInfluenceScore'] = self.media_influence_score
        if self.media_name is not None:
            result['mediaName'] = self.media_name
        if self.media_propagation_score is not None:
            result['mediaPropagationScore'] = self.media_propagation_score
        if self.media_qun_name is not None:
            result['mediaQunName'] = self.media_qun_name
        if self.media_res_city is not None:
            result['mediaResCity'] = self.media_res_city
        if self.media_res_country is not None:
            result['mediaResCountry'] = self.media_res_country
        if self.media_res_province is not None:
            result['mediaResProvince'] = self.media_res_province
        if self.media_type is not None:
            result['mediaType'] = self.media_type
        if self.original_media is not None:
            result['originalMedia'] = self.original_media
        if self.relevance_score_fmt is not None:
            result['relevanceScoreFmt'] = self.relevance_score_fmt
        if self.similar_number is not None:
            result['similarNumber'] = self.similar_number
        if self.spam is not None:
            result['spam'] = self.spam
        if self.weibo_comment_id is not None:
            result['weiboCommentId'] = self.weibo_comment_id
        if self.weibo_mid is not None:
            result['weiboMid'] = self.weibo_mid
        if self.ue_emotion_score is not None:
            result['ueEmotionScore'] = self.ue_emotion_score
        result['financeEvents'] = []
        if self.finance_events is not None:
            for k in self.finance_events:
                result['financeEvents'].append(k.to_map() if k else None)
        if self.app_store_app_score is not None:
            result['appStoreAppScore'] = self.app_store_app_score
        if self.app_store_app_name is not None:
            result['appStoreAppName'] = self.app_store_app_name
        if self.app_store_name is not None:
            result['appStoreName'] = self.app_store_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('advertisement') is not None:
            self.advertisement = m.get('advertisement')
        if m.get('alipayAccount') is not None:
            self.alipay_account = m.get('alipayAccount')
        if m.get('atAuthorNames') is not None:
            self.at_author_names = m.get('atAuthorNames')
        if m.get('authorAvatarUrl') is not None:
            self.author_avatar_url = m.get('authorAvatarUrl')
        if m.get('authorFollowersCount') is not None:
            self.author_followers_count = m.get('authorFollowersCount')
        if m.get('authorFriendsCount') is not None:
            self.author_friends_count = m.get('authorFriendsCount')
        if m.get('authorId') is not None:
            self.author_id = m.get('authorId')
        if m.get('authorName') is not None:
            self.author_name = m.get('authorName')
        if m.get('authorProfileUrl') is not None:
            self.author_profile_url = m.get('authorProfileUrl')
        if m.get('authorStatusesCount') is not None:
            self.author_statuses_count = m.get('authorStatusesCount')
        if m.get('authorVerifyType') is not None:
            self.author_verify_type = m.get('authorVerifyType')
        if m.get('bkz') is not None:
            self.bkz = m.get('bkz')
        if m.get('contentAudioText') is not None:
            self.content_audio_text = m.get('contentAudioText')
        if m.get('contentAudioUrls') is not None:
            self.content_audio_urls = m.get('contentAudioUrls')
        if m.get('contentEmotionType') is not None:
            self.content_emotion_type = m.get('contentEmotionType')
        if m.get('contentImageText') is not None:
            self.content_image_text = m.get('contentImageText')
        if m.get('contentImageUrls') is not None:
            self.content_image_urls = m.get('contentImageUrls')
        if m.get('contentVideoText') is not None:
            self.content_video_text = m.get('contentVideoText')
        if m.get('contentVideoUrls') is not None:
            self.content_video_urls = m.get('contentVideoUrls')
        if m.get('docCreateTime') is not None:
            self.doc_create_time = m.get('docCreateTime')
        if m.get('docPublishTime') is not None:
            self.doc_publish_time = m.get('docPublishTime')
        if m.get('docAnswersCount') is not None:
            self.doc_answers_count = m.get('docAnswersCount')
        if m.get('docAreas') is not None:
            self.doc_areas = m.get('docAreas')
        if m.get('docCommentsCount') is not None:
            self.doc_comments_count = m.get('docCommentsCount')
        if m.get('docContent') is not None:
            self.doc_content = m.get('docContent')
        if m.get('docContentBrief') is not None:
            self.doc_content_brief = m.get('docContentBrief')
        if m.get('docContentSign') is not None:
            self.doc_content_sign = m.get('docContentSign')
        if m.get('docFocusArticleCount') is not None:
            self.doc_focus_article_count = m.get('docFocusArticleCount')
        if m.get('docLikesCount') is not None:
            self.doc_likes_count = m.get('docLikesCount')
        if m.get('docMessageType') is not None:
            self.doc_message_type = m.get('docMessageType')
        if m.get('docParentId') is not None:
            self.doc_parent_id = m.get('docParentId')
        if m.get('docReadsCount') is not None:
            self.doc_reads_count = m.get('docReadsCount')
        if m.get('docRepostsCount') is not None:
            self.doc_reposts_count = m.get('docRepostsCount')
        if m.get('docSelfContentSign') is not None:
            self.doc_self_content_sign = m.get('docSelfContentSign')
        if m.get('docTitle') is not None:
            self.doc_title = m.get('docTitle')
        if m.get('docTitleBrief') is not None:
            self.doc_title_brief = m.get('docTitleBrief')
        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')
        if m.get('docUserDefineJson') is not None:
            self.doc_user_define_json = m.get('docUserDefineJson')
        if m.get('emotionScore') is not None:
            self.emotion_score = m.get('emotionScore')
        if m.get('entityAlias') is not None:
            self.entity_alias = m.get('entityAlias')
        if m.get('entityRelevancyScore') is not None:
            self.entity_relevancy_score = m.get('entityRelevancyScore')
        if m.get('eroticism') is not None:
            self.eroticism = m.get('eroticism')
        if m.get('eroticismScoreFmt') is not None:
            self.eroticism_score_fmt = m.get('eroticismScoreFmt')
        if m.get('gambling') is not None:
            self.gambling = m.get('gambling')
        if m.get('highlightAssKeywords') is not None:
            self.highlight_ass_keywords = m.get('highlightAssKeywords')
        if m.get('highlightKeywords') is not None:
            self.highlight_keywords = m.get('highlightKeywords')
        if m.get('highlightPosKeywords') is not None:
            self.highlight_pos_keywords = m.get('highlightPosKeywords')
        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')
        if m.get('mediaHosts') is not None:
            self.media_hosts = m.get('mediaHosts')
        if m.get('mediaInfluenceLevel') is not None:
            self.media_influence_level = m.get('mediaInfluenceLevel')
        if m.get('mediaInfluenceScore') is not None:
            self.media_influence_score = m.get('mediaInfluenceScore')
        if m.get('mediaName') is not None:
            self.media_name = m.get('mediaName')
        if m.get('mediaPropagationScore') is not None:
            self.media_propagation_score = m.get('mediaPropagationScore')
        if m.get('mediaQunName') is not None:
            self.media_qun_name = m.get('mediaQunName')
        if m.get('mediaResCity') is not None:
            self.media_res_city = m.get('mediaResCity')
        if m.get('mediaResCountry') is not None:
            self.media_res_country = m.get('mediaResCountry')
        if m.get('mediaResProvince') is not None:
            self.media_res_province = m.get('mediaResProvince')
        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')
        if m.get('originalMedia') is not None:
            self.original_media = m.get('originalMedia')
        if m.get('relevanceScoreFmt') is not None:
            self.relevance_score_fmt = m.get('relevanceScoreFmt')
        if m.get('similarNumber') is not None:
            self.similar_number = m.get('similarNumber')
        if m.get('spam') is not None:
            self.spam = m.get('spam')
        if m.get('weiboCommentId') is not None:
            self.weibo_comment_id = m.get('weiboCommentId')
        if m.get('weiboMid') is not None:
            self.weibo_mid = m.get('weiboMid')
        if m.get('ueEmotionScore') is not None:
            self.ue_emotion_score = m.get('ueEmotionScore')
        self.finance_events = []
        if m.get('financeEvents') is not None:
            for k in m.get('financeEvents'):
                temp_model = FinanceEvent()
                self.finance_events.append(temp_model.from_map(k))
        if m.get('appStoreAppScore') is not None:
            self.app_store_app_score = m.get('appStoreAppScore')
        if m.get('appStoreAppName') is not None:
            self.app_store_app_name = m.get('appStoreAppName')
        if m.get('appStoreName') is not None:
            self.app_store_name = m.get('appStoreName')
        return self


class Project(TeaModel):
    def __init__(self, ass_keywords=None, default_filter_id=None, ext_criteria=None, id=None, name=None,
                 neg_keywords=None, pid=None, pos_keywords=None, project_group_id=None, project_type=None,
                 project_type_name=None, sub_project_ids=None, team_id=None, valid=None, gmt_create_timestamp=None,
                 gmt_modified_timestamp=None, uname_create=None, uid_create=None, uname_modified=None, uid_modified=None):
        # 搭配词
        self.ass_keywords = ass_keywords  # type: str
        # 项目的默认过滤模板ID
        self.default_filter_id = default_filter_id  # type: long
        # 高级用法，非关键词配置，如at用户，标题排除词。
        self.ext_criteria = ext_criteria  # type: str
        # 舆情项目ID
        self.id = id  # type: long
        # 项目名称
        self.name = name  # type: str
        # 排除词
        self.neg_keywords = neg_keywords  # type: str
        # 项目父ID，如果没有父项目则为0
        self.pid = pid  # type: long
        # 项目关键词
        self.pos_keywords = pos_keywords  # type: str
        # 项目归属分组ID，0代表没有分组
        self.project_group_id = project_group_id  # type: long
        # 0:通用舆情项目，1：金融舆情项目
        self.project_type = project_type  # type: long
        # 舆情项目类型名称
        self.project_type_name = project_type_name  # type: str
        # 项目的子项目ID列表
        self.sub_project_ids = sub_project_ids  # type: list[long]
        # 团队id
        self.team_id = team_id  # type: long
        # 状态，1为生效，0为失效。
        self.valid = valid  # type: long
        # 项目创建时间，毫秒
        self.gmt_create_timestamp = gmt_create_timestamp  # type: long
        # 项目修改时间，毫秒
        self.gmt_modified_timestamp = gmt_modified_timestamp  # type: long
        # 项目创建人名称
        self.uname_create = uname_create  # type: str
        # 项目创建人uid
        self.uid_create = uid_create  # type: str
        # 项目修改人名称
        self.uname_modified = uname_modified  # type: str
        # 项目修改人uid
        self.uid_modified = uid_modified  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Project, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ass_keywords is not None:
            result['assKeywords'] = self.ass_keywords
        if self.default_filter_id is not None:
            result['defaultFilterId'] = self.default_filter_id
        if self.ext_criteria is not None:
            result['extCriteria'] = self.ext_criteria
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.neg_keywords is not None:
            result['negKeywords'] = self.neg_keywords
        if self.pid is not None:
            result['pid'] = self.pid
        if self.pos_keywords is not None:
            result['posKeywords'] = self.pos_keywords
        if self.project_group_id is not None:
            result['projectGroupId'] = self.project_group_id
        if self.project_type is not None:
            result['projectType'] = self.project_type
        if self.project_type_name is not None:
            result['projectTypeName'] = self.project_type_name
        if self.sub_project_ids is not None:
            result['subProjectIds'] = self.sub_project_ids
        if self.team_id is not None:
            result['teamId'] = self.team_id
        if self.valid is not None:
            result['valid'] = self.valid
        if self.gmt_create_timestamp is not None:
            result['gmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.uname_create is not None:
            result['unameCreate'] = self.uname_create
        if self.uid_create is not None:
            result['uidCreate'] = self.uid_create
        if self.uname_modified is not None:
            result['unameModified'] = self.uname_modified
        if self.uid_modified is not None:
            result['uidModified'] = self.uid_modified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assKeywords') is not None:
            self.ass_keywords = m.get('assKeywords')
        if m.get('defaultFilterId') is not None:
            self.default_filter_id = m.get('defaultFilterId')
        if m.get('extCriteria') is not None:
            self.ext_criteria = m.get('extCriteria')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('negKeywords') is not None:
            self.neg_keywords = m.get('negKeywords')
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        if m.get('posKeywords') is not None:
            self.pos_keywords = m.get('posKeywords')
        if m.get('projectGroupId') is not None:
            self.project_group_id = m.get('projectGroupId')
        if m.get('projectType') is not None:
            self.project_type = m.get('projectType')
        if m.get('projectTypeName') is not None:
            self.project_type_name = m.get('projectTypeName')
        if m.get('subProjectIds') is not None:
            self.sub_project_ids = m.get('subProjectIds')
        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        if m.get('gmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('gmtCreateTimestamp')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('unameCreate') is not None:
            self.uname_create = m.get('unameCreate')
        if m.get('uidCreate') is not None:
            self.uid_create = m.get('uidCreate')
        if m.get('unameModified') is not None:
            self.uname_modified = m.get('unameModified')
        if m.get('uidModified') is not None:
            self.uid_modified = m.get('uidModified')
        return self


class BizTagTree(TeaModel):
    def __init__(self, gmt_create_timestamp=None, gmt_modified_timestamp=None, id=None, name=None, parent_id=None,
                 status=None, tag_id_path=None, tag_name_path=None, uid_create=None, uid_modified=None, uname_create=None,
                 uname_modified=None):
        # 创建时间，毫秒
        self.gmt_create_timestamp = gmt_create_timestamp  # type: long
        # 修改时间，毫秒
        self.gmt_modified_timestamp = gmt_modified_timestamp  # type: long
        # 标签id
        self.id = id  # type: long
        # 标签名字
        self.name = name  # type: str
        # 父亲id
        self.parent_id = parent_id  # type: long
        # 标签状态，1表示激活，0表示不激活
        self.status = status  # type: long
        # 标签节点树
        self.tag_id_path = tag_id_path  # type: str
        # 标签节点名字树
        self.tag_name_path = tag_name_path  # type: str
        # 创建人id
        self.uid_create = uid_create  # type: str
        # 修改人id
        self.uid_modified = uid_modified  # type: str
        # 创建人名字
        self.uname_create = uname_create  # type: str
        # 修改人名字
        self.uname_modified = uname_modified  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BizTagTree, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_timestamp is not None:
            result['gmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.status is not None:
            result['status'] = self.status
        if self.tag_id_path is not None:
            result['tagIdPath'] = self.tag_id_path
        if self.tag_name_path is not None:
            result['tagNamePath'] = self.tag_name_path
        if self.uid_create is not None:
            result['uidCreate'] = self.uid_create
        if self.uid_modified is not None:
            result['uidModified'] = self.uid_modified
        if self.uname_create is not None:
            result['unameCreate'] = self.uname_create
        if self.uname_modified is not None:
            result['unameModified'] = self.uname_modified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('gmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('gmtCreateTimestamp')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tagIdPath') is not None:
            self.tag_id_path = m.get('tagIdPath')
        if m.get('tagNamePath') is not None:
            self.tag_name_path = m.get('tagNamePath')
        if m.get('uidCreate') is not None:
            self.uid_create = m.get('uidCreate')
        if m.get('uidModified') is not None:
            self.uid_modified = m.get('uidModified')
        if m.get('unameCreate') is not None:
            self.uname_create = m.get('unameCreate')
        if m.get('unameModified') is not None:
            self.uname_modified = m.get('unameModified')
        return self


class SearchCondition(TeaModel):
    def __init__(self, project_id=None, filter_id=None, ass_keywords_idx=None,
                 author_followers_count_max_filter=None, author_followers_count_min_filter=None, author_name_idx=None,
                 author_verify_type_filter=None, comments_count_max_filter=None, comments_count_min_filter=None,
                 content_length_max_filter=None, content_length_min_filter=None, doc_answers_count_max_filter=None,
                 doc_answers_count_min_filter=None, doc_area_idx=None, doc_content_sign_idx=None, doc_create_time_end_filter=None,
                 doc_create_time_start_filter=None, doc_publish_time_end_filter=None, doc_publish_time_start_filter=None,
                 duplicate_removal=None, emotion_score_max_filter=None, emotion_score_min_filter=None, exclude_author_name_idx=None,
                 excluding_media_hosts_filter=None, excluding_media_pool_ids_filter=None, likes_count_max_filter=None,
                 likes_count_min_filter=None, media_hosts_filter=None, media_influence_score_max_filter=None,
                 media_influence_score_min_filter=None, media_pool_ids_filter=None, media_propagation_score_max_filter=None,
                 media_propagation_score_min_filter=None, media_type_filter=None, message_type_filter=None, neg_keywords_idx=None, page_now=None,
                 page_size=None, pos_keywords_idx=None, primary_key_idx=None, reads_count_max_filter=None,
                 reads_count_min_filter=None, relevance_score_max_filter=None, relevance_score_min_filter=None,
                 reposts_count_max_filter=None, reposts_count_min_filter=None, reprint_from_filter=None, title_excluding_words_idx=None,
                 title_including_words_idx=None, used_index_mode_switch=None, eroticism_filter=None, gambling_filter=None, bkz_filter=None,
                 advertisement_filter=None, illegal_advertisement_filter=None, spam_filter=None, suspicion_spam_filter=None,
                 biz_tags_idx=None, alipay_account_filter=None, doc_update_time_end_filter=None,
                 doc_update_time_start_filter=None, enable_keyword_highlight=None, finance_entity_area_filter=None, entity_name=None,
                 finance_entity_relevance_score_max_filter=None, finance_entity_relevance_score_min_filter=None, finance_event_code_filter=None,
                 parent_ids_idx=None, sort_by_direction=None, sort_by=None, hotspot_title_idx=None):
        # 舆情项目Id
        self.project_id = project_id  # type: long
        # 舆情筛选模板Id
        self.filter_id = filter_id  # type: long
        # 搭配词，json字符串数组
        self.ass_keywords_idx = ass_keywords_idx  # type: str
        # 粉丝数上限
        self.author_followers_count_max_filter = author_followers_count_max_filter  # type: long
        # 粉丝数下限
        self.author_followers_count_min_filter = author_followers_count_min_filter  # type: long
        # 指定用户名，多个用户用英文逗号隔开
        self.author_name_idx = author_name_idx  # type: str
        # 作者认证类型，多个用,隔开
        self.author_verify_type_filter = author_verify_type_filter  # type: str
        # 评论数上限
        self.comments_count_max_filter = comments_count_max_filter  # type: long
        # 评论数下限
        self.comments_count_min_filter = comments_count_min_filter  # type: long
        # 内容长度上限
        self.content_length_max_filter = content_length_max_filter  # type: long
        # 内容长度下限
        self.content_length_min_filter = content_length_min_filter  # type: long
        # 答案数上限
        self.doc_answers_count_max_filter = doc_answers_count_max_filter  # type: long
        # 答案数下限
        self.doc_answers_count_min_filter = doc_answers_count_min_filter  # type: long
        # 提级地域
        self.doc_area_idx = doc_area_idx  # type: str
        # 相似文章索引Id,，多个用英文逗号隔开
        self.doc_content_sign_idx = doc_content_sign_idx  # type: str
        # 创建时间戳上限
        self.doc_create_time_end_filter = doc_create_time_end_filter  # type: long
        # 创建时间戳下限
        self.doc_create_time_start_filter = doc_create_time_start_filter  # type: long
        # 发布时间戳上限
        self.doc_publish_time_end_filter = doc_publish_time_end_filter  # type: long
        # 发布时间戳下限
        self.doc_publish_time_start_filter = doc_publish_time_start_filter  # type: long
        # 返回的数据是否去重，默认true
        self.duplicate_removal = duplicate_removal  # type: bool
        # 情感分值上限，范围-10~10
        self.emotion_score_max_filter = emotion_score_max_filter  # type: float
        # 情感分值下限，范围-10~10
        self.emotion_score_min_filter = emotion_score_min_filter  # type: float
        # 排除指定用户名，多个用户用英文逗号隔开
        self.exclude_author_name_idx = exclude_author_name_idx  # type: str
        # 排除指定Host
        self.excluding_media_hosts_filter = excluding_media_hosts_filter  # type: str
        # 排除指定媒体库ids，媒体库在舆情平台上定义
        self.excluding_media_pool_ids_filter = excluding_media_pool_ids_filter  # type: str
        # 点赞数上限
        self.likes_count_max_filter = likes_count_max_filter  # type: long
        # 点赞数下限
        self.likes_count_min_filter = likes_count_min_filter  # type: long
        # 指定Host
        self.media_hosts_filter = media_hosts_filter  # type: str
        # 媒体影响分上限
        self.media_influence_score_max_filter = media_influence_score_max_filter  # type: float
        # 媒体影响分下限
        self.media_influence_score_min_filter = media_influence_score_min_filter  # type: float
        # 指定媒体库ids，媒体库在舆情平台上定义
        self.media_pool_ids_filter = media_pool_ids_filter  # type: str
        # 媒体传播分上限取值范围：0-10分
        self.media_propagation_score_max_filter = media_propagation_score_max_filter  # type: float
        # 媒体传播分下限取值范围：0-10分
        self.media_propagation_score_min_filter = media_propagation_score_min_filter  # type: float
        # 枚举字符串如：WEIBO-WEIBO
        self.media_type_filter = media_type_filter  # type: str
        # 枚举字符串如：COMMENT
        self.message_type_filter = message_type_filter  # type: str
        # 排除关键词
        self.neg_keywords_idx = neg_keywords_idx  # type: str
        # 指定页码
        self.page_now = page_now  # type: int
        # 指定每页大小，最大50
        self.page_size = page_size  # type: int
        # 格式同AssKeywordsIdx，如果指定了AssKeywordsIdx，两者要同时满足。
        self.pos_keywords_idx = pos_keywords_idx  # type: str
        # 舆情文章id，支持多值
        self.primary_key_idx = primary_key_idx  # type: str
        # 阅读数上限
        self.reads_count_max_filter = reads_count_max_filter  # type: long
        # 阅读数下限
        self.reads_count_min_filter = reads_count_min_filter  # type: long
        # 相关性分上限
        self.relevance_score_max_filter = relevance_score_max_filter  # type: float
        # 相关性分下限
        self.relevance_score_min_filter = relevance_score_min_filter  # type: float
        # 转发数上限
        self.reposts_count_max_filter = reposts_count_max_filter  # type: long
        # 转发数下限
        self.reposts_count_min_filter = reposts_count_min_filter  # type: long
        # 文章转载来源名称
        self.reprint_from_filter = reprint_from_filter  # type: str
        # 标题不包含的关键词
        self.title_excluding_words_idx = title_excluding_words_idx  # type: str
        # 标题包含的关键词
        self.title_including_words_idx = title_including_words_idx  # type: str
        # 指定索引模式,KEYWORD|CREATE_TIME
        self.used_index_mode_switch = used_index_mode_switch  # type: str
        # 色情取值true or false
        self.eroticism_filter = eroticism_filter  # type: bool
        # 赌博取值true or false
        self.gambling_filter = gambling_filter  # type: bool
        # 暴恐政取值true or false
        self.bkz_filter = bkz_filter  # type: bool
        # 广告取值true or false
        self.advertisement_filter = advertisement_filter  # type: bool
        # 违规广告取值true or false
        self.illegal_advertisement_filter = illegal_advertisement_filter  # type: bool
        # 垃圾取值true or false
        self.spam_filter = spam_filter  # type: bool
        # 疑似垃圾取值true or false
        self.suspicion_spam_filter = suspicion_spam_filter  # type: bool
        # 业务自定义标签字段过滤
        self.biz_tags_idx = biz_tags_idx  # type: str
        # 支付宝内部的2088账号
        self.alipay_account_filter = alipay_account_filter  # type: str
        # 文章更新时间上限
        self.doc_update_time_end_filter = doc_update_time_end_filter  # type: long
        # 更新时间戳下限
        self.doc_update_time_start_filter = doc_update_time_start_filter  # type: long
        # 是否要进行关键词高亮显示
        self.enable_keyword_highlight = enable_keyword_highlight  # type: bool
        # 实体所在地，主要指的是公司
        self.finance_entity_area_filter = finance_entity_area_filter  # type: str
        # 公司全名称
        self.entity_name = entity_name  # type: str
        # 实体关联度得分上限
        self.finance_entity_relevance_score_max_filter = finance_entity_relevance_score_max_filter  # type: float
        # 实体关联度得分下限
        self.finance_entity_relevance_score_min_filter = finance_entity_relevance_score_min_filter  # type: float
        # 金融事件id，支持多个
        self.finance_event_code_filter = finance_event_code_filter  # type: str
        # 父文章docId
        self.parent_ids_idx = parent_ids_idx  # type: str
        # 如'+'是升序，'-'是降序
        self.sort_by_direction = sort_by_direction  # type: str
        # 排序字段枚举
        self.sort_by = sort_by  # type: str
        # 热搜标题倒排
        self.hotspot_title_idx = hotspot_title_idx  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchCondition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.filter_id is not None:
            result['filterId'] = self.filter_id
        if self.ass_keywords_idx is not None:
            result['assKeywordsIdx'] = self.ass_keywords_idx
        if self.author_followers_count_max_filter is not None:
            result['authorFollowersCountMaxFilter'] = self.author_followers_count_max_filter
        if self.author_followers_count_min_filter is not None:
            result['authorFollowersCountMinFilter'] = self.author_followers_count_min_filter
        if self.author_name_idx is not None:
            result['authorNameIdx'] = self.author_name_idx
        if self.author_verify_type_filter is not None:
            result['authorVerifyTypeFilter'] = self.author_verify_type_filter
        if self.comments_count_max_filter is not None:
            result['commentsCountMaxFilter'] = self.comments_count_max_filter
        if self.comments_count_min_filter is not None:
            result['commentsCountMinFilter'] = self.comments_count_min_filter
        if self.content_length_max_filter is not None:
            result['contentLengthMaxFilter'] = self.content_length_max_filter
        if self.content_length_min_filter is not None:
            result['contentLengthMinFilter'] = self.content_length_min_filter
        if self.doc_answers_count_max_filter is not None:
            result['docAnswersCountMaxFilter'] = self.doc_answers_count_max_filter
        if self.doc_answers_count_min_filter is not None:
            result['docAnswersCountMinFilter'] = self.doc_answers_count_min_filter
        if self.doc_area_idx is not None:
            result['docAreaIdx'] = self.doc_area_idx
        if self.doc_content_sign_idx is not None:
            result['docContentSignIdx'] = self.doc_content_sign_idx
        if self.doc_create_time_end_filter is not None:
            result['docCreateTimeEndFilter'] = self.doc_create_time_end_filter
        if self.doc_create_time_start_filter is not None:
            result['docCreateTimeStartFilter'] = self.doc_create_time_start_filter
        if self.doc_publish_time_end_filter is not None:
            result['docPublishTimeEndFilter'] = self.doc_publish_time_end_filter
        if self.doc_publish_time_start_filter is not None:
            result['docPublishTimeStartFilter'] = self.doc_publish_time_start_filter
        if self.duplicate_removal is not None:
            result['duplicateRemoval'] = self.duplicate_removal
        if self.emotion_score_max_filter is not None:
            result['emotionScoreMaxFilter'] = self.emotion_score_max_filter
        if self.emotion_score_min_filter is not None:
            result['emotionScoreMinFilter'] = self.emotion_score_min_filter
        if self.exclude_author_name_idx is not None:
            result['excludeAuthorNameIdx'] = self.exclude_author_name_idx
        if self.excluding_media_hosts_filter is not None:
            result['excludingMediaHostsFilter'] = self.excluding_media_hosts_filter
        if self.excluding_media_pool_ids_filter is not None:
            result['excludingMediaPoolIdsFilter'] = self.excluding_media_pool_ids_filter
        if self.likes_count_max_filter is not None:
            result['likesCountMaxFilter'] = self.likes_count_max_filter
        if self.likes_count_min_filter is not None:
            result['likesCountMinFilter'] = self.likes_count_min_filter
        if self.media_hosts_filter is not None:
            result['mediaHostsFilter'] = self.media_hosts_filter
        if self.media_influence_score_max_filter is not None:
            result['mediaInfluenceScoreMaxFilter'] = self.media_influence_score_max_filter
        if self.media_influence_score_min_filter is not None:
            result['mediaInfluenceScoreMinFilter'] = self.media_influence_score_min_filter
        if self.media_pool_ids_filter is not None:
            result['mediaPoolIdsFilter'] = self.media_pool_ids_filter
        if self.media_propagation_score_max_filter is not None:
            result['mediaPropagationScoreMaxFilter'] = self.media_propagation_score_max_filter
        if self.media_propagation_score_min_filter is not None:
            result['mediaPropagationScoreMinFilter'] = self.media_propagation_score_min_filter
        if self.media_type_filter is not None:
            result['mediaTypeFilter'] = self.media_type_filter
        if self.message_type_filter is not None:
            result['messageTypeFilter'] = self.message_type_filter
        if self.neg_keywords_idx is not None:
            result['negKeywordsIdx'] = self.neg_keywords_idx
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.pos_keywords_idx is not None:
            result['posKeywordsIdx'] = self.pos_keywords_idx
        if self.primary_key_idx is not None:
            result['primaryKeyIdx'] = self.primary_key_idx
        if self.reads_count_max_filter is not None:
            result['readsCountMaxFilter'] = self.reads_count_max_filter
        if self.reads_count_min_filter is not None:
            result['readsCountMinFilter'] = self.reads_count_min_filter
        if self.relevance_score_max_filter is not None:
            result['relevanceScoreMaxFilter'] = self.relevance_score_max_filter
        if self.relevance_score_min_filter is not None:
            result['relevanceScoreMinFilter'] = self.relevance_score_min_filter
        if self.reposts_count_max_filter is not None:
            result['repostsCountMaxFilter'] = self.reposts_count_max_filter
        if self.reposts_count_min_filter is not None:
            result['repostsCountMinFilter'] = self.reposts_count_min_filter
        if self.reprint_from_filter is not None:
            result['reprintFromFilter'] = self.reprint_from_filter
        if self.title_excluding_words_idx is not None:
            result['titleExcludingWordsIdx'] = self.title_excluding_words_idx
        if self.title_including_words_idx is not None:
            result['titleIncludingWordsIdx'] = self.title_including_words_idx
        if self.used_index_mode_switch is not None:
            result['usedIndexModeSwitch'] = self.used_index_mode_switch
        if self.eroticism_filter is not None:
            result['eroticismFilter'] = self.eroticism_filter
        if self.gambling_filter is not None:
            result['gamblingFilter'] = self.gambling_filter
        if self.bkz_filter is not None:
            result['bkzFilter'] = self.bkz_filter
        if self.advertisement_filter is not None:
            result['advertisementFilter'] = self.advertisement_filter
        if self.illegal_advertisement_filter is not None:
            result['illegalAdvertisementFilter'] = self.illegal_advertisement_filter
        if self.spam_filter is not None:
            result['spamFilter'] = self.spam_filter
        if self.suspicion_spam_filter is not None:
            result['suspicionSpamFilter'] = self.suspicion_spam_filter
        if self.biz_tags_idx is not None:
            result['bizTagsIdx'] = self.biz_tags_idx
        if self.alipay_account_filter is not None:
            result['alipayAccountFilter'] = self.alipay_account_filter
        if self.doc_update_time_end_filter is not None:
            result['docUpdateTimeEndFilter'] = self.doc_update_time_end_filter
        if self.doc_update_time_start_filter is not None:
            result['docUpdateTimeStartFilter'] = self.doc_update_time_start_filter
        if self.enable_keyword_highlight is not None:
            result['enableKeywordHighlight'] = self.enable_keyword_highlight
        if self.finance_entity_area_filter is not None:
            result['financeEntityAreaFilter'] = self.finance_entity_area_filter
        if self.entity_name is not None:
            result['entityName'] = self.entity_name
        if self.finance_entity_relevance_score_max_filter is not None:
            result['financeEntityRelevanceScoreMaxFilter'] = self.finance_entity_relevance_score_max_filter
        if self.finance_entity_relevance_score_min_filter is not None:
            result['financeEntityRelevanceScoreMinFilter'] = self.finance_entity_relevance_score_min_filter
        if self.finance_event_code_filter is not None:
            result['financeEventCodeFilter'] = self.finance_event_code_filter
        if self.parent_ids_idx is not None:
            result['parentIdsIdx'] = self.parent_ids_idx
        if self.sort_by_direction is not None:
            result['sortByDirection'] = self.sort_by_direction
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.hotspot_title_idx is not None:
            result['hotspotTitleIdx'] = self.hotspot_title_idx
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('filterId') is not None:
            self.filter_id = m.get('filterId')
        if m.get('assKeywordsIdx') is not None:
            self.ass_keywords_idx = m.get('assKeywordsIdx')
        if m.get('authorFollowersCountMaxFilter') is not None:
            self.author_followers_count_max_filter = m.get('authorFollowersCountMaxFilter')
        if m.get('authorFollowersCountMinFilter') is not None:
            self.author_followers_count_min_filter = m.get('authorFollowersCountMinFilter')
        if m.get('authorNameIdx') is not None:
            self.author_name_idx = m.get('authorNameIdx')
        if m.get('authorVerifyTypeFilter') is not None:
            self.author_verify_type_filter = m.get('authorVerifyTypeFilter')
        if m.get('commentsCountMaxFilter') is not None:
            self.comments_count_max_filter = m.get('commentsCountMaxFilter')
        if m.get('commentsCountMinFilter') is not None:
            self.comments_count_min_filter = m.get('commentsCountMinFilter')
        if m.get('contentLengthMaxFilter') is not None:
            self.content_length_max_filter = m.get('contentLengthMaxFilter')
        if m.get('contentLengthMinFilter') is not None:
            self.content_length_min_filter = m.get('contentLengthMinFilter')
        if m.get('docAnswersCountMaxFilter') is not None:
            self.doc_answers_count_max_filter = m.get('docAnswersCountMaxFilter')
        if m.get('docAnswersCountMinFilter') is not None:
            self.doc_answers_count_min_filter = m.get('docAnswersCountMinFilter')
        if m.get('docAreaIdx') is not None:
            self.doc_area_idx = m.get('docAreaIdx')
        if m.get('docContentSignIdx') is not None:
            self.doc_content_sign_idx = m.get('docContentSignIdx')
        if m.get('docCreateTimeEndFilter') is not None:
            self.doc_create_time_end_filter = m.get('docCreateTimeEndFilter')
        if m.get('docCreateTimeStartFilter') is not None:
            self.doc_create_time_start_filter = m.get('docCreateTimeStartFilter')
        if m.get('docPublishTimeEndFilter') is not None:
            self.doc_publish_time_end_filter = m.get('docPublishTimeEndFilter')
        if m.get('docPublishTimeStartFilter') is not None:
            self.doc_publish_time_start_filter = m.get('docPublishTimeStartFilter')
        if m.get('duplicateRemoval') is not None:
            self.duplicate_removal = m.get('duplicateRemoval')
        if m.get('emotionScoreMaxFilter') is not None:
            self.emotion_score_max_filter = m.get('emotionScoreMaxFilter')
        if m.get('emotionScoreMinFilter') is not None:
            self.emotion_score_min_filter = m.get('emotionScoreMinFilter')
        if m.get('excludeAuthorNameIdx') is not None:
            self.exclude_author_name_idx = m.get('excludeAuthorNameIdx')
        if m.get('excludingMediaHostsFilter') is not None:
            self.excluding_media_hosts_filter = m.get('excludingMediaHostsFilter')
        if m.get('excludingMediaPoolIdsFilter') is not None:
            self.excluding_media_pool_ids_filter = m.get('excludingMediaPoolIdsFilter')
        if m.get('likesCountMaxFilter') is not None:
            self.likes_count_max_filter = m.get('likesCountMaxFilter')
        if m.get('likesCountMinFilter') is not None:
            self.likes_count_min_filter = m.get('likesCountMinFilter')
        if m.get('mediaHostsFilter') is not None:
            self.media_hosts_filter = m.get('mediaHostsFilter')
        if m.get('mediaInfluenceScoreMaxFilter') is not None:
            self.media_influence_score_max_filter = m.get('mediaInfluenceScoreMaxFilter')
        if m.get('mediaInfluenceScoreMinFilter') is not None:
            self.media_influence_score_min_filter = m.get('mediaInfluenceScoreMinFilter')
        if m.get('mediaPoolIdsFilter') is not None:
            self.media_pool_ids_filter = m.get('mediaPoolIdsFilter')
        if m.get('mediaPropagationScoreMaxFilter') is not None:
            self.media_propagation_score_max_filter = m.get('mediaPropagationScoreMaxFilter')
        if m.get('mediaPropagationScoreMinFilter') is not None:
            self.media_propagation_score_min_filter = m.get('mediaPropagationScoreMinFilter')
        if m.get('mediaTypeFilter') is not None:
            self.media_type_filter = m.get('mediaTypeFilter')
        if m.get('messageTypeFilter') is not None:
            self.message_type_filter = m.get('messageTypeFilter')
        if m.get('negKeywordsIdx') is not None:
            self.neg_keywords_idx = m.get('negKeywordsIdx')
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('posKeywordsIdx') is not None:
            self.pos_keywords_idx = m.get('posKeywordsIdx')
        if m.get('primaryKeyIdx') is not None:
            self.primary_key_idx = m.get('primaryKeyIdx')
        if m.get('readsCountMaxFilter') is not None:
            self.reads_count_max_filter = m.get('readsCountMaxFilter')
        if m.get('readsCountMinFilter') is not None:
            self.reads_count_min_filter = m.get('readsCountMinFilter')
        if m.get('relevanceScoreMaxFilter') is not None:
            self.relevance_score_max_filter = m.get('relevanceScoreMaxFilter')
        if m.get('relevanceScoreMinFilter') is not None:
            self.relevance_score_min_filter = m.get('relevanceScoreMinFilter')
        if m.get('repostsCountMaxFilter') is not None:
            self.reposts_count_max_filter = m.get('repostsCountMaxFilter')
        if m.get('repostsCountMinFilter') is not None:
            self.reposts_count_min_filter = m.get('repostsCountMinFilter')
        if m.get('reprintFromFilter') is not None:
            self.reprint_from_filter = m.get('reprintFromFilter')
        if m.get('titleExcludingWordsIdx') is not None:
            self.title_excluding_words_idx = m.get('titleExcludingWordsIdx')
        if m.get('titleIncludingWordsIdx') is not None:
            self.title_including_words_idx = m.get('titleIncludingWordsIdx')
        if m.get('usedIndexModeSwitch') is not None:
            self.used_index_mode_switch = m.get('usedIndexModeSwitch')
        if m.get('eroticismFilter') is not None:
            self.eroticism_filter = m.get('eroticismFilter')
        if m.get('gamblingFilter') is not None:
            self.gambling_filter = m.get('gamblingFilter')
        if m.get('bkzFilter') is not None:
            self.bkz_filter = m.get('bkzFilter')
        if m.get('advertisementFilter') is not None:
            self.advertisement_filter = m.get('advertisementFilter')
        if m.get('illegalAdvertisementFilter') is not None:
            self.illegal_advertisement_filter = m.get('illegalAdvertisementFilter')
        if m.get('spamFilter') is not None:
            self.spam_filter = m.get('spamFilter')
        if m.get('suspicionSpamFilter') is not None:
            self.suspicion_spam_filter = m.get('suspicionSpamFilter')
        if m.get('bizTagsIdx') is not None:
            self.biz_tags_idx = m.get('bizTagsIdx')
        if m.get('alipayAccountFilter') is not None:
            self.alipay_account_filter = m.get('alipayAccountFilter')
        if m.get('docUpdateTimeEndFilter') is not None:
            self.doc_update_time_end_filter = m.get('docUpdateTimeEndFilter')
        if m.get('docUpdateTimeStartFilter') is not None:
            self.doc_update_time_start_filter = m.get('docUpdateTimeStartFilter')
        if m.get('enableKeywordHighlight') is not None:
            self.enable_keyword_highlight = m.get('enableKeywordHighlight')
        if m.get('financeEntityAreaFilter') is not None:
            self.finance_entity_area_filter = m.get('financeEntityAreaFilter')
        if m.get('entityName') is not None:
            self.entity_name = m.get('entityName')
        if m.get('financeEntityRelevanceScoreMaxFilter') is not None:
            self.finance_entity_relevance_score_max_filter = m.get('financeEntityRelevanceScoreMaxFilter')
        if m.get('financeEntityRelevanceScoreMinFilter') is not None:
            self.finance_entity_relevance_score_min_filter = m.get('financeEntityRelevanceScoreMinFilter')
        if m.get('financeEventCodeFilter') is not None:
            self.finance_event_code_filter = m.get('financeEventCodeFilter')
        if m.get('parentIdsIdx') is not None:
            self.parent_ids_idx = m.get('parentIdsIdx')
        if m.get('sortByDirection') is not None:
            self.sort_by_direction = m.get('sortByDirection')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('hotspotTitleIdx') is not None:
            self.hotspot_title_idx = m.get('hotspotTitleIdx')
        return self


class Filter(TeaModel):
    def __init__(self, id=None, gmt_create_timestamp=None, gmt_modified_timestamp=None, valid=None, name=None,
                 criteria=None, filter_group_id=None):
        # 筛选模板id
        self.id = id  # type: long
        # 创建日期，毫秒
        self.gmt_create_timestamp = gmt_create_timestamp  # type: long
        # 修改时间，毫秒
        self.gmt_modified_timestamp = gmt_modified_timestamp  # type: long
        # 状态。1：有效，0：无效
        self.valid = valid  # type: long
        # 筛选模板名称
        self.name = name  # type: str
        # 筛选模板配置内容
        self.criteria = criteria  # type: str
        # 筛选模板所属id
        self.filter_group_id = filter_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(Filter, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.gmt_create_timestamp is not None:
            result['gmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.valid is not None:
            result['valid'] = self.valid
        if self.name is not None:
            result['name'] = self.name
        if self.criteria is not None:
            result['criteria'] = self.criteria
        if self.filter_group_id is not None:
            result['filterGroupId'] = self.filter_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('gmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('gmtCreateTimestamp')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('criteria') is not None:
            self.criteria = m.get('criteria')
        if m.get('filterGroupId') is not None:
            self.filter_group_id = m.get('filterGroupId')
        return self


class StatisticPoint(TeaModel):
    def __init__(self, key=None, value=None):
        # 聚合字段结果值
        self.key = key  # type: str
        # 聚合结果值
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(StatisticPoint, self).to_map()
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


class ProjectGroup(TeaModel):
    def __init__(self, gmt_create_timestamp=None, gmt_modified_timestamp=None, id=None, name=None, parent_id=None,
                 project_group_type=None, uid_create=None, uname_create=None, valid=None):
        # 项目分组创建时间
        self.gmt_create_timestamp = gmt_create_timestamp  # type: long
        # 项目分组修改时间
        self.gmt_modified_timestamp = gmt_modified_timestamp  # type: long
        # 项目分组id，唯一标识项目分组
        self.id = id  # type: long
        # 项目分组名称
        self.name = name  # type: str
        # 父项目分组id，0为默认值，表示无父项目分组
        self.parent_id = parent_id  # type: long
        # 项目分组类型，0表示通用舆情，2表示金融舆情
        self.project_group_type = project_group_type  # type: long
        # 项目创建人uid
        self.uid_create = uid_create  # type: str
        # 项目分组创建人名称
        self.uname_create = uname_create  # type: str
        # 是否有效，1表示有效，0表示无效
        self.valid = valid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProjectGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_timestamp is not None:
            result['gmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.project_group_type is not None:
            result['projectGroupType'] = self.project_group_type
        if self.uid_create is not None:
            result['uidCreate'] = self.uid_create
        if self.uname_create is not None:
            result['unameCreate'] = self.uname_create
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('gmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('gmtCreateTimestamp')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('projectGroupType') is not None:
            self.project_group_type = m.get('projectGroupType')
        if m.get('uidCreate') is not None:
            self.uid_create = m.get('uidCreate')
        if m.get('unameCreate') is not None:
            self.uname_create = m.get('unameCreate')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class AlarmData(TeaModel):
    def __init__(self, alarm_level=None, alarm_msg_id=None, alarm_rule_id=None, alarm_rule_name=None,
                 alarm_timestamp=None, author_name=None, content=None, doc_id_str=None, doc_media_type=None,
                 gmt_modified_timestamp=None, media_name=None, memos=None, modifier_name=None, modifier_out_no=None, project_id=None,
                 project_name=None, self_content_sign_str=None, source_url=None, state=None, tags=None, title=None, type=None,
                 message=None):
        # 预警规则等级
        self.alarm_level = alarm_level  # type: str
        # 舆情消息id
        self.alarm_msg_id = alarm_msg_id  # type: long
        # 预警规则id
        self.alarm_rule_id = alarm_rule_id  # type: long
        # 预警规则名称
        self.alarm_rule_name = alarm_rule_name  # type: str
        # 预警时间
        self.alarm_timestamp = alarm_timestamp  # type: long
        # 舆情作者名字
        self.author_name = author_name  # type: str
        # 舆情内容（不完整）
        self.content = content  # type: str
        # 舆情文章唯一id
        self.doc_id_str = doc_id_str  # type: str
        # 舆情消息类型
        self.doc_media_type = doc_media_type  # type: str
        # 最后更新时间
        self.gmt_modified_timestamp = gmt_modified_timestamp  # type: long
        # 媒体名字
        self.media_name = media_name  # type: str
        # 备注列表
        self.memos = memos  # type: list[str]
        # 最后修改舆情的用户名称
        self.modifier_name = modifier_name  # type: str
        # 员工工号
        self.modifier_out_no = modifier_out_no  # type: str
        # 项目id
        self.project_id = project_id  # type: long
        # 舆情命中的预警项目名称
        self.project_name = project_name  # type: str
        # 文章签名
        self.self_content_sign_str = self_content_sign_str  # type: str
        # url地址
        self.source_url = source_url  # type: str
        # 预警消息状态
        self.state = state  # type: str
        # 预警的标签列表
        self.tags = tags  # type: list[str]
        # 舆情标题
        self.title = title  # type: str
        # 预警规则类型，枚举值
        self.type = type  # type: str
        # 舆情消息体
        self.message = message  # type: YuqingMessage

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super(AlarmData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_level is not None:
            result['alarmLevel'] = self.alarm_level
        if self.alarm_msg_id is not None:
            result['alarmMsgId'] = self.alarm_msg_id
        if self.alarm_rule_id is not None:
            result['alarmRuleId'] = self.alarm_rule_id
        if self.alarm_rule_name is not None:
            result['alarmRuleName'] = self.alarm_rule_name
        if self.alarm_timestamp is not None:
            result['alarmTimestamp'] = self.alarm_timestamp
        if self.author_name is not None:
            result['authorName'] = self.author_name
        if self.content is not None:
            result['content'] = self.content
        if self.doc_id_str is not None:
            result['docIdStr'] = self.doc_id_str
        if self.doc_media_type is not None:
            result['docMediaType'] = self.doc_media_type
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.media_name is not None:
            result['mediaName'] = self.media_name
        if self.memos is not None:
            result['memos'] = self.memos
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.modifier_out_no is not None:
            result['modifierOutNo'] = self.modifier_out_no
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.self_content_sign_str is not None:
            result['selfContentSignStr'] = self.self_content_sign_str
        if self.source_url is not None:
            result['sourceUrl'] = self.source_url
        if self.state is not None:
            result['state'] = self.state
        if self.tags is not None:
            result['tags'] = self.tags
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alarmLevel') is not None:
            self.alarm_level = m.get('alarmLevel')
        if m.get('alarmMsgId') is not None:
            self.alarm_msg_id = m.get('alarmMsgId')
        if m.get('alarmRuleId') is not None:
            self.alarm_rule_id = m.get('alarmRuleId')
        if m.get('alarmRuleName') is not None:
            self.alarm_rule_name = m.get('alarmRuleName')
        if m.get('alarmTimestamp') is not None:
            self.alarm_timestamp = m.get('alarmTimestamp')
        if m.get('authorName') is not None:
            self.author_name = m.get('authorName')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('docIdStr') is not None:
            self.doc_id_str = m.get('docIdStr')
        if m.get('docMediaType') is not None:
            self.doc_media_type = m.get('docMediaType')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('mediaName') is not None:
            self.media_name = m.get('mediaName')
        if m.get('memos') is not None:
            self.memos = m.get('memos')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('modifierOutNo') is not None:
            self.modifier_out_no = m.get('modifierOutNo')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('selfContentSignStr') is not None:
            self.self_content_sign_str = m.get('selfContentSignStr')
        if m.get('sourceUrl') is not None:
            self.source_url = m.get('sourceUrl')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('message') is not None:
            temp_model = YuqingMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class AlarmQueryCondition(TeaModel):
    def __init__(self, alarm_rule_id=None, doc_ids=None, doc_media_type=None, end_time=None, ids=None, levels=None,
                 page_now=None, page_size=None, projec_ids=None, start_time=None, status=None, tag_ids=None, type=None,
                 is_query_update_time=None):
        # 规则id列表
        self.alarm_rule_id = alarm_rule_id  # type: list[long]
        # 舆情消息id列表
        self.doc_ids = doc_ids  # type: list[long]
        # 查询数据的消息类型
        self.doc_media_type = doc_media_type  # type: list[str]
        # 查询结束时间,毫秒
        self.end_time = end_time  # type: long
        # 预警id列表
        self.ids = ids  # type: list[long]
        # 预警等级过滤列表
        self.levels = levels  # type: list[str]
        # 当前页
        self.page_now = page_now  # type: long
        # 分页大小
        self.page_size = page_size  # type: long
        # 舆情项目id
        self.projec_ids = projec_ids  # type: list[long]
        # 查询开始时间,毫秒
        self.start_time = start_time  # type: long
        # 预警状态列表
        self.status = status  # type: list[str]
        # 标签id列表
        self.tag_ids = tag_ids  # type: list[long]
        # 预警规则类型
        self.type = type  # type: str
        # 是否使用更新时间作为筛选
        self.is_query_update_time = is_query_update_time  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AlarmQueryCondition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_rule_id is not None:
            result['alarmRuleId'] = self.alarm_rule_id
        if self.doc_ids is not None:
            result['docIds'] = self.doc_ids
        if self.doc_media_type is not None:
            result['docMediaType'] = self.doc_media_type
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.ids is not None:
            result['ids'] = self.ids
        if self.levels is not None:
            result['levels'] = self.levels
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.projec_ids is not None:
            result['projecIds'] = self.projec_ids
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.tag_ids is not None:
            result['tagIds'] = self.tag_ids
        if self.type is not None:
            result['type'] = self.type
        if self.is_query_update_time is not None:
            result['isQueryUpdateTime'] = self.is_query_update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alarmRuleId') is not None:
            self.alarm_rule_id = m.get('alarmRuleId')
        if m.get('docIds') is not None:
            self.doc_ids = m.get('docIds')
        if m.get('docMediaType') is not None:
            self.doc_media_type = m.get('docMediaType')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('levels') is not None:
            self.levels = m.get('levels')
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projecIds') is not None:
            self.projec_ids = m.get('projecIds')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tagIds') is not None:
            self.tag_ids = m.get('tagIds')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('isQueryUpdateTime') is not None:
            self.is_query_update_time = m.get('isQueryUpdateTime')
        return self


class QueryAlarmDataListRequest(TeaModel):
    def __init__(self, alarm_query=None, order_by_key=None, team_hash_id=None, request_id=None):
        self.alarm_query = alarm_query  # type: AlarmQueryCondition
        # 排序方式
        self.order_by_key = order_by_key  # type: str
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.alarm_query:
            self.alarm_query.validate()

    def to_map(self):
        _map = super(QueryAlarmDataListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_query is not None:
            result['alarmQuery'] = self.alarm_query.to_map()
        if self.order_by_key is not None:
            result['orderByKey'] = self.order_by_key
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alarmQuery') is not None:
            temp_model = AlarmQueryCondition()
            self.alarm_query = temp_model.from_map(m['alarmQuery'])
        if m.get('orderByKey') is not None:
            self.order_by_key = m.get('orderByKey')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryAlarmDataListResponseBody(TeaModel):
    def __init__(self, request_id=None, pages=None, total_count=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 预警列表
        self.pages = pages  # type: list[AlarmData]
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.pages:
            for k in self.pages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryAlarmDataListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['pages'] = []
        if self.pages is not None:
            for k in self.pages:
                result['pages'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.pages = []
        if m.get('pages') is not None:
            for k in m.get('pages'):
                temp_model = AlarmData()
                self.pages.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryAlarmDataListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAlarmDataListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAlarmDataListResponse, self).to_map()
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
            temp_model = QueryAlarmDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotspotMessageRequest(TeaModel):
    def __init__(self, hotspot_search_condition=None, team_hash_id=None, request_id=None):
        # 热搜查询参数
        self.hotspot_search_condition = hotspot_search_condition  # type: HotspotSearchCondition
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.hotspot_search_condition:
            self.hotspot_search_condition.validate()

    def to_map(self):
        _map = super(ListHotspotMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hotspot_search_condition is not None:
            result['hotspotSearchCondition'] = self.hotspot_search_condition.to_map()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('hotspotSearchCondition') is not None:
            temp_model = HotspotSearchCondition()
            self.hotspot_search_condition = temp_model.from_map(m['hotspotSearchCondition'])
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListHotspotMessageResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, hotspot_messages=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 总条数
        self.total_count = total_count  # type: long
        # 热搜结果信息列表数组
        self.hotspot_messages = hotspot_messages  # type: list[YuqingHotspotMessage]

    def validate(self):
        if self.hotspot_messages:
            for k in self.hotspot_messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotspotMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['hotspotMessages'] = []
        if self.hotspot_messages is not None:
            for k in self.hotspot_messages:
                result['hotspotMessages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.hotspot_messages = []
        if m.get('hotspotMessages') is not None:
            for k in m.get('hotspotMessages'):
                temp_model = YuqingHotspotMessage()
                self.hotspot_messages.append(temp_model.from_map(k))
        return self


class ListHotspotMessageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHotspotMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotspotMessageResponse, self).to_map()
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
            temp_model = ListHotspotMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAnalysisComponentResultRequest(TeaModel):
    def __init__(self, analysis_id=None, team_hash_id=None, request_id=None):
        # 分析任务Id
        self.analysis_id = analysis_id  # type: long
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAnalysisComponentResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetAnalysisComponentResultResponseBody(TeaModel):
    def __init__(self, request_id=None, result_json=None, analysis_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 任务结果json。参考opinion.analysis.component.query的result_json
        self.result_json = result_json  # type: str
        # 任务Id
        self.analysis_id = analysis_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAnalysisComponentResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result_json is not None:
            result['resultJson'] = self.result_json
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resultJson') is not None:
            self.result_json = m.get('resultJson')
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        return self


class GetAnalysisComponentResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAnalysisComponentResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAnalysisComponentResultResponse, self).to_map()
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
            temp_model = GetAnalysisComponentResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageDetailRequest(TeaModel):
    def __init__(self, doc_id=None, team_hash_id=None, request_id=None):
        # 舆情文章Id
        self.doc_id = doc_id  # type: str
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMessageDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetMessageDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 舆情消息体
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMessageDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetMessageDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMessageDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMessageDetailResponse, self).to_map()
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
            temp_model = GetMessageDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, create_user_id=None, create_user_name=None, project=None, team_hash_id=None, request_id=None):
        # 创建者uid
        self.create_user_id = create_user_id  # type: str
        # 创建者名称
        self.create_user_name = create_user_name  # type: str
        # 舆情项目对象
        self.project = project  # type: Project
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_user_id is not None:
            result['createUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['createUserName'] = self.create_user_name
        if self.project is not None:
            result['project'] = self.project.to_map()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createUserId') is not None:
            self.create_user_id = m.get('createUserId')
        if m.get('createUserName') is not None:
            self.create_user_name = m.get('createUserName')
        if m.get('project') is not None:
            temp_model = Project()
            self.project = temp_model.from_map(m['project'])
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        # 舆情项目id
        self.id = id  # type: long
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectListRequest(TeaModel):
    def __init__(self, page_now=None, page_size=None, project_group_id=None, project_id=None, team_hash_id=None,
                 request_id=None):
        # 当前页数，从1开始
        self.page_now = page_now  # type: long
        # 分页大小
        self.page_size = page_size  # type: long
        # 所属项目分组id
        self.project_group_id = project_group_id  # type: long
        # 指定舆情项目id
        self.project_id = project_id  # type: long
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryProjectListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_group_id is not None:
            result['projectGroupId'] = self.project_group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectGroupId') is not None:
            self.project_group_id = m.get('projectGroupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryProjectListResponseBody(TeaModel):
    def __init__(self, request_id=None, project_list=None, total_count=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 舆情项目列表,参考Project对象
        self.project_list = project_list  # type: list[Project]
        # 总记录数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.project_list:
            for k in self.project_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryProjectListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['projectList'] = []
        if self.project_list is not None:
            for k in self.project_list:
                result['projectList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.project_list = []
        if m.get('projectList') is not None:
            for k in m.get('projectList'):
                temp_model = Project()
                self.project_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryProjectListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryProjectListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryProjectListResponse, self).to_map()
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
            temp_model = QueryProjectListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagNodesRequest(TeaModel):
    def __init__(self, team_hash_id=None, request_id=None):
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTagNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryTagNodesResponseBody(TeaModel):
    def __init__(self, request_id=None, biz_tag_tree_list=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 标签列表
        self.biz_tag_tree_list = biz_tag_tree_list  # type: list[BizTagTree]

    def validate(self):
        if self.biz_tag_tree_list:
            for k in self.biz_tag_tree_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTagNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['bizTagTreeList'] = []
        if self.biz_tag_tree_list is not None:
            for k in self.biz_tag_tree_list:
                result['bizTagTreeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.biz_tag_tree_list = []
        if m.get('bizTagTreeList') is not None:
            for k in m.get('bizTagTreeList'):
                temp_model = BizTagTree()
                self.biz_tag_tree_list.append(temp_model.from_map(k))
        return self


class QueryTagNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTagNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTagNodesResponse, self).to_map()
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
            temp_model = QueryTagNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReportNotifiesRequest(TeaModel):
    def __init__(self, cp_id=None, create_end_timestamp=None, create_start_timestamp=None, page_now=None,
                 page_size=None, subject=None, type=None, team_hash_id=None, request_id=None):
        # 自定义页面id
        self.cp_id = cp_id  # type: long
        # 创建截止时间,毫秒
        self.create_end_timestamp = create_end_timestamp  # type: long
        # 创建开始时间，毫秒
        self.create_start_timestamp = create_start_timestamp  # type: long
        # 当前页数，从1开始
        self.page_now = page_now  # type: long
        # 分页大小
        self.page_size = page_size  # type: long
        # 主题
        self.subject = subject  # type: str
        # 类型： 如邮件、钉钉等
        self.type = type  # type: long
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryReportNotifiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cp_id is not None:
            result['cpId'] = self.cp_id
        if self.create_end_timestamp is not None:
            result['createEndTimestamp'] = self.create_end_timestamp
        if self.create_start_timestamp is not None:
            result['createStartTimestamp'] = self.create_start_timestamp
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.subject is not None:
            result['subject'] = self.subject
        if self.type is not None:
            result['type'] = self.type
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cpId') is not None:
            self.cp_id = m.get('cpId')
        if m.get('createEndTimestamp') is not None:
            self.create_end_timestamp = m.get('createEndTimestamp')
        if m.get('createStartTimestamp') is not None:
            self.create_start_timestamp = m.get('createStartTimestamp')
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryReportNotifiesResponseBody(TeaModel):
    def __init__(self, request_id=None, report_notify_record_list=None, total_count=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 报告历史发送信息
        self.report_notify_record_list = report_notify_record_list  # type: list[ReportNotifyRecord]
        # 总数量
        self.total_count = total_count  # type: long

    def validate(self):
        if self.report_notify_record_list:
            for k in self.report_notify_record_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryReportNotifiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['reportNotifyRecordList'] = []
        if self.report_notify_record_list is not None:
            for k in self.report_notify_record_list:
                result['reportNotifyRecordList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.report_notify_record_list = []
        if m.get('reportNotifyRecordList') is not None:
            for k in m.get('reportNotifyRecordList'):
                temp_model = ReportNotifyRecord()
                self.report_notify_record_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryReportNotifiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryReportNotifiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryReportNotifiesResponse, self).to_map()
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
            temp_model = QueryReportNotifiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(self, id=None, modified_user_id=None, modified_user_name=None, team_hash_id=None, request_id=None):
        # 舆情项目id
        self.id = id  # type: long
        # 修改人uid
        self.modified_user_id = modified_user_id  # type: str
        # 修改人名称
        self.modified_user_name = modified_user_name  # type: str
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.modified_user_id is not None:
            result['modifiedUserId'] = self.modified_user_id
        if self.modified_user_name is not None:
            result['modifiedUserName'] = self.modified_user_name
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifiedUserId') is not None:
            self.modified_user_id = m.get('modifiedUserId')
        if m.get('modifiedUserName') is not None:
            self.modified_user_name = m.get('modifiedUserName')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        # 被删除的项目id
        self.id = id  # type: long
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProjectResponse, self).to_map()
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFilterListRequest(TeaModel):
    def __init__(self, page_now=None, page_size=None, filter_id=None, team_hash_id=None, request_id=None):
        # 当前查询的第几页，从1开始
        self.page_now = page_now  # type: long
        # 查询每页的数据量
        self.page_size = page_size  # type: long
        # 指定筛选模板id查询
        self.filter_id = filter_id  # type: long
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFilterListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.filter_id is not None:
            result['filterId'] = self.filter_id
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('filterId') is not None:
            self.filter_id = m.get('filterId')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryFilterListResponseBody(TeaModel):
    def __init__(self, request_id=None, filters=None, total_count=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 筛选模板列表。
        self.filters = filters  # type: list[Filter]
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFilterListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['filters'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.filters = []
        if m.get('filters') is not None:
            for k in m.get('filters'):
                temp_model = Filter()
                self.filters.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryFilterListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryFilterListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFilterListResponse, self).to_map()
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
            temp_model = QueryFilterListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AggregateSearchYuqingRequest(TeaModel):
    def __init__(self, search_condition=None, aggregate_function=None, group_by_key=None, group_limits=None,
                 team_hash_id=None, request_id=None):
        # 查询舆情条件
        self.search_condition = search_condition  # type: SearchCondition
        # 聚合函数
        self.aggregate_function = aggregate_function  # type: str
        # 聚合字段名字,枚举值
        self.group_by_key = group_by_key  # type: str
        # 聚合结果条数
        self.group_limits = group_limits  # type: long
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.search_condition:
            self.search_condition.validate()

    def to_map(self):
        _map = super(AggregateSearchYuqingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_condition is not None:
            result['searchCondition'] = self.search_condition.to_map()
        if self.aggregate_function is not None:
            result['aggregateFunction'] = self.aggregate_function
        if self.group_by_key is not None:
            result['groupByKey'] = self.group_by_key
        if self.group_limits is not None:
            result['groupLimits'] = self.group_limits
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('searchCondition') is not None:
            temp_model = SearchCondition()
            self.search_condition = temp_model.from_map(m['searchCondition'])
        if m.get('aggregateFunction') is not None:
            self.aggregate_function = m.get('aggregateFunction')
        if m.get('groupByKey') is not None:
            self.group_by_key = m.get('groupByKey')
        if m.get('groupLimits') is not None:
            self.group_limits = m.get('groupLimits')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AggregateSearchYuqingResponseBody(TeaModel):
    def __init__(self, request_id=None, agg_result_list=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 聚合结果列表
        self.agg_result_list = agg_result_list  # type: list[StatisticPoint]

    def validate(self):
        if self.agg_result_list:
            for k in self.agg_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AggregateSearchYuqingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['aggResultList'] = []
        if self.agg_result_list is not None:
            for k in self.agg_result_list:
                result['aggResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.agg_result_list = []
        if m.get('aggResultList') is not None:
            for k in m.get('aggResultList'):
                temp_model = StatisticPoint()
                self.agg_result_list.append(temp_model.from_map(k))
        return self


class AggregateSearchYuqingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AggregateSearchYuqingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AggregateSearchYuqingResponse, self).to_map()
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
            temp_model = AggregateSearchYuqingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAnalysisComponentRequest(TeaModel):
    def __init__(self, analyse_type=None, search_condition=None, team_hash_id=None, request_id=None):
        # 分析任务类型名称，具体可以填写的值可以在舆情平台查看
        self.analyse_type = analyse_type  # type: str
        # 搜索舆情条件
        self.search_condition = search_condition  # type: SearchCondition
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.search_condition:
            self.search_condition.validate()

    def to_map(self):
        _map = super(QueryAnalysisComponentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyse_type is not None:
            result['analyseType'] = self.analyse_type
        if self.search_condition is not None:
            result['searchCondition'] = self.search_condition.to_map()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('analyseType') is not None:
            self.analyse_type = m.get('analyseType')
        if m.get('searchCondition') is not None:
            temp_model = SearchCondition()
            self.search_condition = temp_model.from_map(m['searchCondition'])
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryAnalysisComponentResponseBody(TeaModel):
    def __init__(self, request_id=None, analysis_id=None, result_json=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 分析任务Id，用于查询这个任务对应的结果。如果是快速完成类型的分析，会直接返回结果。如果无结果返回，业务方可以根据这个id轮询查询结果。
        self.analysis_id = analysis_id  # type: long
        # 分析任务返回的结果json字符串，不同分析任务返回的json格式不一样。
        self.result_json = result_json  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAnalysisComponentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        if self.result_json is not None:
            result['resultJson'] = self.result_json
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        if m.get('resultJson') is not None:
            self.result_json = m.get('resultJson')
        return self


class QueryAnalysisComponentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAnalysisComponentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAnalysisComponentResponse, self).to_map()
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
            temp_model = QueryAnalysisComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePropagationRequest(TeaModel):
    def __init__(self, weibo_urls=None, team_hash_id=None, request_id=None):
        # 微博源地址
        self.weibo_urls = weibo_urls  # type: list[str]
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePropagationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.weibo_urls is not None:
            result['weiboUrls'] = self.weibo_urls
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('weiboUrls') is not None:
            self.weibo_urls = m.get('weiboUrls')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdatePropagationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePropagationResponseBody, self).to_map()
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


class UpdatePropagationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePropagationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePropagationResponse, self).to_map()
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
            temp_model = UpdatePropagationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListYuqingMessagesRequest(TeaModel):
    def __init__(self, search_condition=None, team_hash_id=None, request_id=None):
        # 查询过滤参数，多个过滤参数之间是且的关系。例如:过滤实例名称为i-a123、i-b123，且实例状态为Stopped：&Filter.1.Name=InstanceName&Filter.1.Value.1=i-a123&Filter.1.Value.2=i-b123&Filter.2.Name=Status&Filter.2.Value=Stopped。
        self.search_condition = search_condition  # type: SearchCondition
        # 舆情团队HashId
        self.team_hash_id = team_hash_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.search_condition:
            self.search_condition.validate()

    def to_map(self):
        _map = super(ListYuqingMessagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_condition is not None:
            result['searchCondition'] = self.search_condition.to_map()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('searchCondition') is not None:
            temp_model = SearchCondition()
            self.search_condition = temp_model.from_map(m['searchCondition'])
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListYuqingMessagesResponseBody(TeaModel):
    def __init__(self, yuqing_messages=None, total_count=None, request_id=None):
        # 数组，返回示例目录。
        self.yuqing_messages = yuqing_messages  # type: list[YuqingMessage]
        # 总记录数。
        self.total_count = total_count  # type: long
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.yuqing_messages:
            for k in self.yuqing_messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListYuqingMessagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['yuqingMessages'] = []
        if self.yuqing_messages is not None:
            for k in self.yuqing_messages:
                result['yuqingMessages'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.yuqing_messages = []
        if m.get('yuqingMessages') is not None:
            for k in m.get('yuqingMessages'):
                temp_model = YuqingMessage()
                self.yuqing_messages.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListYuqingMessagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListYuqingMessagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListYuqingMessagesResponse, self).to_map()
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
            temp_model = ListYuqingMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


