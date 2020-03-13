

# kfBoss
class ResKfBoss(object):
	RES_TABLE = "kfBoss"
	__slots__ = ("id","fbId","mstId","name","localpet","remotepet","touchReward","shieldReward","killReward","min","max","baoxiangReward","cost","makeShield",)

    def __init__(self):
		
			# id 跨服boss表
			self.id = 0
		
			# fbId 副本id
			self.fbId = 0
		
			# mstId 怪物id
			self.mstId = 0
		
			# name 怪物名字
			self.name = ""
		
			# localpet 本服协助宠物池
			self.localpet = []
		
			# remotepet 跨服协助宠物池
			self.remotepet = []
		
			# touchReward 触碰奖励
			self.touchReward = 0
		
			# shieldReward 破盾奖励
			self.shieldReward = []
		
			# killReward 击杀奖励
			self.killReward = []
		
			# min 宝箱最小数量
			self.min = 0
		
			# max 宝箱最大数量
			self.max = 0
		
			# baoxiangReward 宝箱
			self.baoxiangReward = []
		
			# cost 复活材料
			self.cost = []
		
			# makeShield 生成盾百分比点
			self.makeShield = []
		

    def load_from_json(self, data):
		
			# id 跨服boss表
			self.id = data.get("id",0)
		
			# fbId 副本id
			self.fbId = data.get("fbId",0)
		
			# mstId 怪物id
			self.mstId = data.get("mstId",0)
		
			# name 怪物名字
			self.name = data.get("name","")
		
			# localpet 本服协助宠物池
			self.localpet = data.get("localpet",[])
		
			# remotepet 跨服协助宠物池
			self.remotepet = data.get("remotepet",[])
		
			# touchReward 触碰奖励
			self.touchReward = data.get("touchReward",0)
		
			# shieldReward 破盾奖励
			self.shieldReward = data.get("shieldReward",[])
		
			# killReward 击杀奖励
			self.killReward = data.get("killReward",[])
		
			# min 宝箱最小数量
			self.min = data.get("min",0)
		
			# max 宝箱最大数量
			self.max = data.get("max",0)
		
			# baoxiangReward 宝箱
			self.baoxiangReward = data.get("baoxiangReward",[])
		
			# cost 复活材料
			self.cost = data.get("cost",[])
		
			# makeShield 生成盾百分比点
			self.makeShield = data.get("makeShield",[])
		

# grBoss
class ResGrBoss(object):
	RES_TABLE = "grBoss"
	__slots__ = ("id","fbId","mstId","bgIcon",)

    def __init__(self):
		
			# id 个人boss表
			self.id = 0
		
			# fbId 副本id
			self.fbId = 0
		
			# mstId 怪物id
			self.mstId = 0
		
			# bgIcon 背景图
			self.bgIcon = ""
		

    def load_from_json(self, data):
		
			# id 个人boss表
			self.id = data.get("id",0)
		
			# fbId 副本id
			self.fbId = data.get("fbId",0)
		
			# mstId 怪物id
			self.mstId = data.get("mstId",0)
		
			# bgIcon 背景图
			self.bgIcon = data.get("bgIcon","")
		

# kfbossrank
class ResKfbossrank(object):
	RES_TABLE = "kfbossrank"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id 跨服boss排行
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 跨服boss排行
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# ywBoss
class ResYwBoss(object):
	RES_TABLE = "ywBoss"
	__slots__ = ("id","actDesc","refreshDesc","fbId","mstId","stTime","endTime","interval","runaway","occupy","cost","bgIcon","refresh","refresh2","spec",)

    def __init__(self):
		
			# id 野外boss表
			self.id = 0
		
			# actDesc 活动说明
			self.actDesc = ""
		
			# refreshDesc 刷新说明
			self.refreshDesc = ""
		
			# fbId 副本id
			self.fbId = 0
		
			# mstId 怪物id
			self.mstId = 0
		
			# stTime boss开启时间
			self.stTime = ""
		
			# endTime boss结束时间
			self.endTime = ""
		
			# interval boss间隔时间(秒)
			self.interval = 0
		
			# runaway boss逃跑时间(秒)
			self.runaway = 0
		
			# occupy boss占领时间(秒)
			self.occupy = 0
		
			# cost 进入消耗
			self.cost = []
		
			# bgIcon 背景图
			self.bgIcon = ""
		
			# refresh boss刷新时间
			self.refresh = []
		
			# refresh2 boss刷新时间（客户端用）
			self.refresh2 = []
		
			# spec 是否特殊
			self.spec = 0
		

    def load_from_json(self, data):
		
			# id 野外boss表
			self.id = data.get("id",0)
		
			# actDesc 活动说明
			self.actDesc = data.get("actDesc","")
		
			# refreshDesc 刷新说明
			self.refreshDesc = data.get("refreshDesc","")
		
			# fbId 副本id
			self.fbId = data.get("fbId",0)
		
			# mstId 怪物id
			self.mstId = data.get("mstId",0)
		
			# stTime boss开启时间
			self.stTime = data.get("stTime","")
		
			# endTime boss结束时间
			self.endTime = data.get("endTime","")
		
			# interval boss间隔时间(秒)
			self.interval = data.get("interval",0)
		
			# runaway boss逃跑时间(秒)
			self.runaway = data.get("runaway",0)
		
			# occupy boss占领时间(秒)
			self.occupy = data.get("occupy",0)
		
			# cost 进入消耗
			self.cost = data.get("cost",[])
		
			# bgIcon 背景图
			self.bgIcon = data.get("bgIcon","")
		
			# refresh boss刷新时间
			self.refresh = data.get("refresh",[])
		
			# refresh2 boss刷新时间（客户端用）
			self.refresh2 = data.get("refresh2",[])
		
			# spec 是否特殊
			self.spec = data.get("spec",0)
		

# qmBoss
class ResQmBoss(object):
	RES_TABLE = "qmBoss"
	__slots__ = ("id","fbId","mstId","cdtime","relive","tzReward","killReward","rankfirstReward","rankReward","cost1","cost2","cost3","cost4","cost5","bgIcon",)

    def __init__(self):
		
			# id 全民boss表
			self.id = 0
		
			# fbId 副本id
			self.fbId = 0
		
			# mstId 怪物id
			self.mstId = 0
		
			# cdtime 复活CD（秒）
			self.cdtime = 0
		
			# relive 是否可手动复活
			self.relive = 0
		
			# tzReward 挑战奖励
			self.tzReward = 0
		
			# killReward 击杀奖励
			self.killReward = 0
		
			# rankfirstReward 排名第一奖励
			self.rankfirstReward = 0
		
			# rankReward 其他排名奖励
			self.rankReward = 0
		
			# cost1 复活材料1
			self.cost1 = []
		
			# cost2 复活材料2
			self.cost2 = []
		
			# cost3 复活材料3
			self.cost3 = []
		
			# cost4 复活材料4
			self.cost4 = []
		
			# cost5 复活材料5
			self.cost5 = []
		
			# bgIcon 背景图
			self.bgIcon = ""
		

    def load_from_json(self, data):
		
			# id 全民boss表
			self.id = data.get("id",0)
		
			# fbId 副本id
			self.fbId = data.get("fbId",0)
		
			# mstId 怪物id
			self.mstId = data.get("mstId",0)
		
			# cdtime 复活CD（秒）
			self.cdtime = data.get("cdtime",0)
		
			# relive 是否可手动复活
			self.relive = data.get("relive",0)
		
			# tzReward 挑战奖励
			self.tzReward = data.get("tzReward",0)
		
			# killReward 击杀奖励
			self.killReward = data.get("killReward",0)
		
			# rankfirstReward 排名第一奖励
			self.rankfirstReward = data.get("rankfirstReward",0)
		
			# rankReward 其他排名奖励
			self.rankReward = data.get("rankReward",0)
		
			# cost1 复活材料1
			self.cost1 = data.get("cost1",[])
		
			# cost2 复活材料2
			self.cost2 = data.get("cost2",[])
		
			# cost3 复活材料3
			self.cost3 = data.get("cost3",[])
		
			# cost4 复活材料4
			self.cost4 = data.get("cost4",[])
		
			# cost5 复活材料5
			self.cost5 = data.get("cost5",[])
		
			# bgIcon 背景图
			self.bgIcon = data.get("bgIcon","")
		

# ssjBoss
class ResSsjBoss(object):
	RES_TABLE = "ssjBoss"
	__slots__ = ("id","grade","group","lv","fbId","mstId","bgIcon","firstReward","mailId",)

    def __init__(self):
		
			# id 生死劫boss表
			self.id = 0
		
			# grade 难道
			self.grade = 0
		
			# group 章数
			self.group = 0
		
			# lv 劫数
			self.lv = 0
		
			# fbId 副本id
			self.fbId = 0
		
			# mstId 怪物id
			self.mstId = 0
		
			# bgIcon 背景图
			self.bgIcon = ""
		
			# firstReward 全服首通奖励
			self.firstReward = []
		
			# mailId 全服首通邮件模板id
			self.mailId = 0
		

    def load_from_json(self, data):
		
			# id 生死劫boss表
			self.id = data.get("id",0)
		
			# grade 难道
			self.grade = data.get("grade",0)
		
			# group 章数
			self.group = data.get("group",0)
		
			# lv 劫数
			self.lv = data.get("lv",0)
		
			# fbId 副本id
			self.fbId = data.get("fbId",0)
		
			# mstId 怪物id
			self.mstId = data.get("mstId",0)
		
			# bgIcon 背景图
			self.bgIcon = data.get("bgIcon","")
		
			# firstReward 全服首通奖励
			self.firstReward = data.get("firstReward",[])
		
			# mailId 全服首通邮件模板id
			self.mailId = data.get("mailId",0)
		

# guildSxBar
class ResGuildSxBar(object):
	RES_TABLE = "guildSxBar"
	__slots__ = ("id","num","reward",)

    def __init__(self):
		
			# id 帮会上香进度奖励
			self.id = 0
		
			# num 目标值
			self.num = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 帮会上香进度奖励
			self.id = data.get("id",0)
		
			# num 目标值
			self.num = data.get("num",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# guildlv
class ResGuildlv(object):
	RES_TABLE = "guildlv"
	__slots__ = ("lv","fund","deputybossnum","peoplenum","vip","cost","skillMax","guildSxNum","sxMaxNum","exchange","CityS","CityM","CityL",)

    def __init__(self):
		
			# lv 帮会表
			self.lv = 0
		
			# fund 资金
			self.fund = 0
		
			# deputybossnum 副帮人数
			self.deputybossnum = 0
		
			# peoplenum 人数
			self.peoplenum = 0
		
			# vip 创建vip等级条件
			self.vip = 0
		
			# cost 创建消耗
			self.cost = []
		
			# skillMax 帮会技能等级上限
			self.skillMax = 0
		
			# guildSxNum 帮会上香最大次数
			self.guildSxNum = 0
		
			# sxMaxNum 帮会最大香火值
			self.sxMaxNum = 0
		
			# exchange 帮会兑换
			self.exchange = []
		
			# CityS 能占领城市级别上限
			self.CityS = 0
		
			# CityM 能占领城市级别上限
			self.CityM = 0
		
			# CityL 能占领城市级别上限
			self.CityL = 0
		

    def load_from_json(self, data):
		
			# lv 帮会表
			self.lv = data.get("lv",0)
		
			# fund 资金
			self.fund = data.get("fund",0)
		
			# deputybossnum 副帮人数
			self.deputybossnum = data.get("deputybossnum",0)
		
			# peoplenum 人数
			self.peoplenum = data.get("peoplenum",0)
		
			# vip 创建vip等级条件
			self.vip = data.get("vip",0)
		
			# cost 创建消耗
			self.cost = data.get("cost",[])
		
			# skillMax 帮会技能等级上限
			self.skillMax = data.get("skillMax",0)
		
			# guildSxNum 帮会上香最大次数
			self.guildSxNum = data.get("guildSxNum",0)
		
			# sxMaxNum 帮会最大香火值
			self.sxMaxNum = data.get("sxMaxNum",0)
		
			# exchange 帮会兑换
			self.exchange = data.get("exchange",[])
		
			# CityS 能占领城市级别上限
			self.CityS = data.get("CityS",0)
		
			# CityM 能占领城市级别上限
			self.CityM = data.get("CityM",0)
		
			# CityL 能占领城市级别上限
			self.CityL = data.get("CityL",0)
		

# guildSx
class ResGuildSx(object):
	RES_TABLE = "guildSx"
	__slots__ = ("id","addExp","addNum","cost","reward",)

    def __init__(self):
		
			# id 帮会上香
			self.id = 0
		
			# addExp 增加帮会资金
			self.addExp = 0
		
			# addNum 增加香火值
			self.addNum = 0
		
			# cost 消耗
			self.cost = []
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 帮会上香
			self.id = data.get("id",0)
		
			# addExp 增加帮会资金
			self.addExp = data.get("addExp",0)
		
			# addNum 增加香火值
			self.addNum = data.get("addNum",0)
		
			# cost 消耗
			self.cost = data.get("cost",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# guildBarr
class ResGuildBarr(object):
	RES_TABLE = "guildBarr"
	__slots__ = ("id","lv","barrId","mstId",)

    def __init__(self):
		
			# id 帮会副本表
			self.id = 0
		
			# lv 帮会开放等级
			self.lv = 0
		
			# barrId 副本id
			self.barrId = 0
		
			# mstId 怪物id(形象展示）
			self.mstId = 0
		

    def load_from_json(self, data):
		
			# id 帮会副本表
			self.id = data.get("id",0)
		
			# lv 帮会开放等级
			self.lv = data.get("lv",0)
		
			# barrId 副本id
			self.barrId = data.get("barrId",0)
		
			# mstId 怪物id(形象展示）
			self.mstId = data.get("mstId",0)
		

# guildTask
class ResGuildTask(object):
	RES_TABLE = "guildTask"
	__slots__ = ("id","type","condition","minLv","maxLv","resetCost","finishCost","rewardArrayint2","arg1","arg2",)

    def __init__(self):
		
			# id 帮会任务表
			self.id = 0
		
			# type 类型
			self.type = 0
		
			# condition 条件
			self.condition = 0
		
			# minLv 帮会最小等级
			self.minLv = 0
		
			# maxLv 帮会最大等级
			self.maxLv = 0
		
			# resetCost 任务重置消耗
			self.resetCost = []
		
			# finishCost 一键完成消耗
			self.finishCost = []
		
			# rewardArrayint2 奖励）
			self.rewardArrayint2 = []
		
			# arg1 参数1
			self.arg1 = ""
		
			# arg2 参数2
			self.arg2 = ""
		

    def load_from_json(self, data):
		
			# id 帮会任务表
			self.id = data.get("id",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# condition 条件
			self.condition = data.get("condition",0)
		
			# minLv 帮会最小等级
			self.minLv = data.get("minLv",0)
		
			# maxLv 帮会最大等级
			self.maxLv = data.get("maxLv",0)
		
			# resetCost 任务重置消耗
			self.resetCost = data.get("resetCost",[])
		
			# finishCost 一键完成消耗
			self.finishCost = data.get("finishCost",[])
		
			# rewardArrayint2 奖励）
			self.rewardArrayint2 = data.get("rewardArrayint2",[])
		
			# arg1 参数1
			self.arg1 = data.get("arg1","")
		
			# arg2 参数2
			self.arg2 = data.get("arg2","")
		

# guildAct
class ResGuildAct(object):
	RES_TABLE = "guildAct"
	__slots__ = ("id","exp","attr","reward",)

    def __init__(self):
		
			# id 帮会活跃表
			self.id = 0
		
			# exp 升级经验
			self.exp = 0
		
			# attr 属性
			self.attr = []
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 帮会活跃表
			self.id = data.get("id",0)
		
			# exp 升级经验
			self.exp = data.get("exp",0)
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# guildSkill
class ResGuildSkill(object):
	RES_TABLE = "guildSkill"
	__slots__ = ("id","skillId","lv","cost","attr",)

    def __init__(self):
		
			# id 帮会技能表
			self.id = 0
		
			# skillId 技能id
			self.skillId = 0
		
			# lv 技能等级
			self.lv = 0
		
			# cost 升级消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 帮会技能表
			self.id = data.get("id",0)
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		
			# lv 技能等级
			self.lv = data.get("lv",0)
		
			# cost 升级消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		

# bujibao
class ResBujibao(object):
	RES_TABLE = "bujibao"
	__slots__ = ("id","openDay","lastDay","offday","limit","bgImg","onceTitle","onceText","onceReward","dailyTitle","dailyText","mailDay","dailyReward","desc","oldPrice","newPrice","costStr","chargeId",)

    def __init__(self):
		
			# id 补给包
			self.id = 0
		
			# openDay 开服第X天开启
			self.openDay = 0
		
			# lastDay 持续天数
			self.lastDay = 0
		
			# offday 休息几天
			self.offday = 0
		
			# limit 限购
			self.limit = 0
		
			# bgImg 名稱圖標背景图决定了价格显示的颜色
			self.bgImg = ""
		
			# onceTitle 一次邮件模板标题
			self.onceTitle = ""
		
			# onceText 一次邮件模板内容
			self.onceText = ""
		
			# onceReward 一次邮件奖励
			self.onceReward = []
		
			# dailyTitle 每天邮件模板标题
			self.dailyTitle = ""
		
			# dailyText 每天邮件模板内容
			self.dailyText = ""
		
			# mailDay 每天邮件持续天数
			self.mailDay = 0
		
			# dailyReward 每天邮件奖励
			self.dailyReward = []
		
			# desc 背后说明
			self.desc = ""
		
			# oldPrice 原價1钻石
			self.oldPrice = ""
		
			# newPrice 当前价格
			self.newPrice = ""
		
			# costStr 按钮价格
			self.costStr = ""
		
			# chargeId 直購關聯充值id
			self.chargeId = []
		

    def load_from_json(self, data):
		
			# id 补给包
			self.id = data.get("id",0)
		
			# openDay 开服第X天开启
			self.openDay = data.get("openDay",0)
		
			# lastDay 持续天数
			self.lastDay = data.get("lastDay",0)
		
			# offday 休息几天
			self.offday = data.get("offday",0)
		
			# limit 限购
			self.limit = data.get("limit",0)
		
			# bgImg 名稱圖標背景图决定了价格显示的颜色
			self.bgImg = data.get("bgImg","")
		
			# onceTitle 一次邮件模板标题
			self.onceTitle = data.get("onceTitle","")
		
			# onceText 一次邮件模板内容
			self.onceText = data.get("onceText","")
		
			# onceReward 一次邮件奖励
			self.onceReward = data.get("onceReward",[])
		
			# dailyTitle 每天邮件模板标题
			self.dailyTitle = data.get("dailyTitle","")
		
			# dailyText 每天邮件模板内容
			self.dailyText = data.get("dailyText","")
		
			# mailDay 每天邮件持续天数
			self.mailDay = data.get("mailDay",0)
		
			# dailyReward 每天邮件奖励
			self.dailyReward = data.get("dailyReward",[])
		
			# desc 背后说明
			self.desc = data.get("desc","")
		
			# oldPrice 原價1钻石
			self.oldPrice = data.get("oldPrice","")
		
			# newPrice 当前价格
			self.newPrice = data.get("newPrice","")
		
			# costStr 按钮价格
			self.costStr = data.get("costStr","")
		
			# chargeId 直購關聯充值id
			self.chargeId = data.get("chargeId",[])
		

# dailyLeichongGift
class ResDailyLeichongGift(object):
	RES_TABLE = "dailyLeichongGift"
	__slots__ = ("id","rmb","reward",)

    def __init__(self):
		
			# id 每日充值礼包表
			self.id = 0
		
			# rmb 充值金额(分）
			self.rmb = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 每日充值礼包表
			self.id = data.get("id",0)
		
			# rmb 充值金额(分）
			self.rmb = data.get("rmb",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# singleCharge
class ResSingleCharge(object):
	RES_TABLE = "singleCharge"
	__slots__ = ("id","start","end","limit","chargeId","desc","reward",)

    def __init__(self):
		
			# id 每日單筆充值表
			self.id = 0
		
			# start 開服第x天開啟
			self.start = 0
		
			# end 開服第x天結束
			self.end = 0
		
			# limit 每日限制領取次數
			self.limit = 0
		
			# chargeId 關聯充值id
			self.chargeId = []
		
			# desc 活動說明
			self.desc = ""
		
			# reward 獎勵繁体
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 每日單筆充值表
			self.id = data.get("id",0)
		
			# start 開服第x天開啟
			self.start = data.get("start",0)
		
			# end 開服第x天結束
			self.end = data.get("end",0)
		
			# limit 每日限制領取次數
			self.limit = data.get("limit",0)
		
			# chargeId 關聯充值id
			self.chargeId = data.get("chargeId",[])
		
			# desc 活動說明
			self.desc = data.get("desc","")
		
			# reward 獎勵繁体
			self.reward = data.get("reward",[])
		

# jrhl
class ResJrhl(object):
	RES_TABLE = "jrhl"
	__slots__ = ("id","rmb","reward",)

    def __init__(self):
		
			# id 今日豪礼表
			self.id = 0
		
			# rmb 充值金额
			self.rmb = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 今日豪礼表
			self.id = data.get("id",0)
		
			# rmb 充值金额
			self.rmb = data.get("rmb",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# zclb
class ResZclb(object):
	RES_TABLE = "zclb"
	__slots__ = ("id","showit","reward","attr","chargeid",)

    def __init__(self):
		
			# id 直冲礼包
			self.id = 0
		
			# showit 显示
			self.showit = 0
		
			# reward 奖励
			self.reward = []
		
			# attr 属性
			self.attr = []
		
			# chargeid 充值id
			self.chargeid = []
		

    def load_from_json(self, data):
		
			# id 直冲礼包
			self.id = data.get("id",0)
		
			# showit 显示
			self.showit = data.get("showit",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# chargeid 充值id
			self.chargeid = data.get("chargeid",[])
		

# limitJitianfanliDayReward
class ResLimitJitianfanliDayReward(object):
	RES_TABLE = "limitJitianfanliDayReward"
	__slots__ = ("id","cycleId","day","reward",)

    def __init__(self):
		
			# id 限时积天返利天奖励表
			self.id = 0
		
			# cycleId 周期
			self.cycleId = 0
		
			# day 天数
			self.day = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 限时积天返利天奖励表
			self.id = data.get("id",0)
		
			# cycleId 周期
			self.cycleId = data.get("cycleId",0)
		
			# day 天数
			self.day = data.get("day",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# zsyj
class ResZsyj(object):
	RES_TABLE = "zsyj"
	__slots__ = ("id","rmb","reward",)

    def __init__(self):
		
			# id 直升一阶表
			self.id = 0
		
			# rmb 充值金额
			self.rmb = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 直升一阶表
			self.id = data.get("id",0)
		
			# rmb 充值金额
			self.rmb = data.get("rmb",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# schd
class ResSchd(object):
	RES_TABLE = "schd"
	__slots__ = ("id","rmb","reward",)

    def __init__(self):
		
			# id 首充活动
			self.id = 0
		
			# rmb 充值金额（分）
			self.rmb = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 首充活动
			self.id = data.get("id",0)
		
			# rmb 充值金额（分）
			self.rmb = data.get("rmb",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# limitJitianfanli
class ResLimitJitianfanli(object):
	RES_TABLE = "limitJitianfanli"
	__slots__ = ("id","payMoney","superReward","skin",)

    def __init__(self):
		
			# id 限时积天返利表周期号
			self.id = 0
		
			# payMoney 充值需求
			self.payMoney = 0
		
			# superReward 超级大奖
			self.superReward = []
		
			# skin 皮肤
			self.skin = ""
		

    def load_from_json(self, data):
		
			# id 限时积天返利表周期号
			self.id = data.get("id",0)
		
			# payMoney 充值需求
			self.payMoney = data.get("payMoney",0)
		
			# superReward 超级大奖
			self.superReward = data.get("superReward",[])
		
			# skin 皮肤
			self.skin = data.get("skin","")
		

# todayChargeActivity
class ResTodayChargeActivity(object):
	RES_TABLE = "todayChargeActivity"
	__slots__ = ("id","cycle","page","days","empty","next","reward","rmb",)

    def __init__(self):
		
			# id 今日充值活动
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# page 分页
			self.page = 0
		
			# days 活动天数
			self.days = 0
		
			# empty 是否空挡
			self.empty = 0
		
			# next 下一档期
			self.next = 0
		
			# reward 奖励
			self.reward = []
		
			# rmb 需求金额（分）
			self.rmb = 0
		

    def load_from_json(self, data):
		
			# id 今日充值活动
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# page 分页
			self.page = data.get("page",0)
		
			# days 活动天数
			self.days = data.get("days",0)
		
			# empty 是否空挡
			self.empty = data.get("empty",0)
		
			# next 下一档期
			self.next = data.get("next",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# rmb 需求金额（分）
			self.rmb = data.get("rmb",0)
		

# daylyPersonCharge
class ResDaylyPersonCharge(object):
	RES_TABLE = "daylyPersonCharge"
	__slots__ = ("id","group","day","jump","reward","show",)

    def __init__(self):
		
			# id 天天返利
			self.id = 0
		
			# group 组号
			self.group = 0
		
			# day 天数
			self.day = 0
		
			# jump 领取后跳转组
			self.jump = 0
		
			# reward 奖励
			self.reward = []
		
			# show 展示标记
			self.show = 0
		

    def load_from_json(self, data):
		
			# id 天天返利
			self.id = data.get("id",0)
		
			# group 组号
			self.group = data.get("group",0)
		
			# day 天数
			self.day = data.get("day",0)
		
			# jump 领取后跳转组
			self.jump = data.get("jump",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# show 展示标记
			self.show = data.get("show",0)
		

# todayChargeReward
class ResTodayChargeReward(object):
	RES_TABLE = "todayChargeReward"
	__slots__ = ("id","reward","rmb","actid",)

    def __init__(self):
		
			# id 今日充值赠送
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# rmb 需求金额（分）
			self.rmb = 0
		
			# actid 关联活动id
			self.actid = 0
		

    def load_from_json(self, data):
		
			# id 今日充值赠送
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# rmb 需求金额（分）
			self.rmb = data.get("rmb",0)
		
			# actid 关联活动id
			self.actid = data.get("actid",0)
		

# ChargeSign
class ResChargeSign(object):
	RES_TABLE = "ChargeSign"
	__slots__ = ("id","dayAndCycle","reward",)

    def __init__(self):
		
			# id 每日充值基拉祈
			self.id = 0
		
			# dayAndCycle 天数-周期
			self.dayAndCycle = []
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 每日充值基拉祈
			self.id = data.get("id",0)
		
			# dayAndCycle 天数-周期
			self.dayAndCycle = data.get("dayAndCycle",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# dailyChargeGift
class ResDailyChargeGift(object):
	RES_TABLE = "dailyChargeGift"
	__slots__ = ("id","sort","rmb","reward",)

    def __init__(self):
		
			# id 每日充值基拉祈
			self.id = 0
		
			# sort 序号
			self.sort = 0
		
			# rmb 充值金额(分）
			self.rmb = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 每日充值基拉祈
			self.id = data.get("id",0)
		
			# sort 序号
			self.sort = data.get("sort",0)
		
			# rmb 充值金额(分）
			self.rmb = data.get("rmb",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# jitianfanli
class ResJitianfanli(object):
	RES_TABLE = "jitianfanli"
	__slots__ = ("id","payMoney","superReward","nextId","isEmtpy","skin",)

    def __init__(self):
		
			# id 积天返利表
			self.id = 0
		
			# payMoney 充值需求
			self.payMoney = 0
		
			# superReward 超级大奖
			self.superReward = []
		
			# nextId 下一期
			self.nextId = 0
		
			# isEmtpy 空挡
			self.isEmtpy = 0
		
			# skin 皮肤
			self.skin = ""
		

    def load_from_json(self, data):
		
			# id 积天返利表
			self.id = data.get("id",0)
		
			# payMoney 充值需求
			self.payMoney = data.get("payMoney",0)
		
			# superReward 超级大奖
			self.superReward = data.get("superReward",[])
		
			# nextId 下一期
			self.nextId = data.get("nextId",0)
		
			# isEmtpy 空挡
			self.isEmtpy = data.get("isEmtpy",0)
		
			# skin 皮肤
			self.skin = data.get("skin","")
		

# jitianfanliDayReward
class ResJitianfanliDayReward(object):
	RES_TABLE = "jitianfanliDayReward"
	__slots__ = ("id","cycleId","day","reward",)

    def __init__(self):
		
			# id 积天返利天奖励表
			self.id = 0
		
			# cycleId 周期
			self.cycleId = 0
		
			# day 天数
			self.day = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 积天返利天奖励表
			self.id = data.get("id",0)
		
			# cycleId 周期
			self.cycleId = data.get("cycleId",0)
		
			# day 天数
			self.day = data.get("day",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# charge
class ResCharge(object):
	RES_TABLE = "charge"
	__slots__ = ("id","name","sort","type","platformId","os","xianshituisonglibao","discount","limit","firstChargeFlag","dbscEnable","dbscReward","tlreward","dbscTitle","dbscIcon","dbscBtn","ValImage","diamondMining","rmb","exp","superRebateVal","leichongrmb","leichongrmbhefu","itemId","zclb","dayreward","vip","desc","reward","zuanshirmb","kfreward","actId","zmlbid","bzbid",)

    def __init__(self):
		
			# id 充值表
			self.id = 0
		
			# name 名字
			self.name = ""
		
			# sort 排序
			self.sort = 0
		
			# type 类型
			self.type = 0
		
			# platformId 平台
			self.platformId = 0
		
			# os 系统类型
			self.os = 0
		
			# xianshituisonglibao 限时推送礼包id
			self.xianshituisonglibao = 0
		
			# discount 打折标签
			self.discount = 0
		
			# limit 限购次数
			self.limit = 0
		
			# firstChargeFlag 后续出现(0批之后出现1批之后出现备注现在支持01)
			self.firstChargeFlag = 0
		
			# dbscEnable 单笔首充是否开启
			self.dbscEnable = 0
		
			# dbscReward 单笔首充奖励后端
			self.dbscReward = []
		
			# tlreward 首充限时活动商品内容（后端使用）
			self.tlreward = []
		
			# dbscTitle 单笔首充图片标题
			self.dbscTitle = ""
		
			# dbscIcon 单笔首充图标
			self.dbscIcon = ""
		
			# dbscBtn 单笔首充按钮样式id
			self.dbscBtn = 0
		
			# ValImage 超值返利图片
			self.ValImage = ""
		
			# diamondMining 钻石挖矿（单位：分）
			self.diamondMining = 0
		
			# rmb 人名币（单位：分）
			self.rmb = 0
		
			# exp 增加VIP经验
			self.exp = 0
		
			# superRebateVal 超级返利积分
			self.superRebateVal = 0
		
			# leichongrmb 增加金额数单位是分
			self.leichongrmb = 0
		
			# leichongrmbhefu 累充RMB合服
			self.leichongrmbhefu = 0
		
			# itemId 平台道具id
			self.itemId = []
		
			# zclb 直冲礼包id
			self.zclb = 0
		
			# dayreward 每天首充送
			self.dayreward = []
		
			# vip vip需求
			self.vip = 0
		
			# desc 售价描述
			self.desc = ""
		
			# reward 商品内容
			self.reward = []
		
			# zuanshirmb 累计钻石购买个数
填写就增加
			self.zuanshirmb = 0
		
			# kfreward 开服赠送
			self.kfreward = []
		
			# actId 活动id(关联活动的表来判断这个充值id是否是活动类型和开放时间)0或空不是活动只能在类型type7
			self.actId = 0
		
			# zmlbid 周末礼包关联id
			self.zmlbid = 0
		
			# bzbid 关联功能id
			self.bzbid = 0
		

    def load_from_json(self, data):
		
			# id 充值表
			self.id = data.get("id",0)
		
			# name 名字
			self.name = data.get("name","")
		
			# sort 排序
			self.sort = data.get("sort",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# platformId 平台
			self.platformId = data.get("platformId",0)
		
			# os 系统类型
			self.os = data.get("os",0)
		
			# xianshituisonglibao 限时推送礼包id
			self.xianshituisonglibao = data.get("xianshituisonglibao",0)
		
			# discount 打折标签
			self.discount = data.get("discount",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# firstChargeFlag 后续出现(0批之后出现1批之后出现备注现在支持01)
			self.firstChargeFlag = data.get("firstChargeFlag",0)
		
			# dbscEnable 单笔首充是否开启
			self.dbscEnable = data.get("dbscEnable",0)
		
			# dbscReward 单笔首充奖励后端
			self.dbscReward = data.get("dbscReward",[])
		
			# tlreward 首充限时活动商品内容（后端使用）
			self.tlreward = data.get("tlreward",[])
		
			# dbscTitle 单笔首充图片标题
			self.dbscTitle = data.get("dbscTitle","")
		
			# dbscIcon 单笔首充图标
			self.dbscIcon = data.get("dbscIcon","")
		
			# dbscBtn 单笔首充按钮样式id
			self.dbscBtn = data.get("dbscBtn",0)
		
			# ValImage 超值返利图片
			self.ValImage = data.get("ValImage","")
		
			# diamondMining 钻石挖矿（单位：分）
			self.diamondMining = data.get("diamondMining",0)
		
			# rmb 人名币（单位：分）
			self.rmb = data.get("rmb",0)
		
			# exp 增加VIP经验
			self.exp = data.get("exp",0)
		
			# superRebateVal 超级返利积分
			self.superRebateVal = data.get("superRebateVal",0)
		
			# leichongrmb 增加金额数单位是分
			self.leichongrmb = data.get("leichongrmb",0)
		
			# leichongrmbhefu 累充RMB合服
			self.leichongrmbhefu = data.get("leichongrmbhefu",0)
		
			# itemId 平台道具id
			self.itemId = data.get("itemId",[])
		
			# zclb 直冲礼包id
			self.zclb = data.get("zclb",0)
		
			# dayreward 每天首充送
			self.dayreward = data.get("dayreward",[])
		
			# vip vip需求
			self.vip = data.get("vip",0)
		
			# desc 售价描述
			self.desc = data.get("desc","")
		
			# reward 商品内容
			self.reward = data.get("reward",[])
		
			# zuanshirmb 累计钻石购买个数
填写就增加
			self.zuanshirmb = data.get("zuanshirmb",0)
		
			# kfreward 开服赠送
			self.kfreward = data.get("kfreward",[])
		
			# actId 活动id(关联活动的表来判断这个充值id是否是活动类型和开放时间)0或空不是活动只能在类型type7
			self.actId = data.get("actId",0)
		
			# zmlbid 周末礼包关联id
			self.zmlbid = data.get("zmlbid",0)
		
			# bzbid 关联功能id
			self.bzbid = data.get("bzbid",0)
		

# petlv
class ResPetlv(object):
	RES_TABLE = "petlv"
	__slots__ = ("id","exp","upbreak","cost","Attr",)

    def __init__(self):
		
			# id 宠物等级表
			self.id = 0
		
			# exp 升阶经验
			self.exp = 0
		
			# upbreak 是否突破
			self.upbreak = 0
		
			# cost 升阶消耗
			self.cost = []
		
			# Attr 当前等级额外添加属性
			self.Attr = []
		

    def load_from_json(self, data):
		
			# id 宠物等级表
			self.id = data.get("id",0)
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# upbreak 是否突破
			self.upbreak = data.get("upbreak",0)
		
			# cost 升阶消耗
			self.cost = data.get("cost",[])
		
			# Attr 当前等级额外添加属性
			self.Attr = data.get("Attr",[])
		

# petwashstar
class ResPetwashstar(object):
	RES_TABLE = "petwashstar"
	__slots__ = ("id","cnt",)

    def __init__(self):
		
			# id 宠物洗练星级表
			self.id = 0
		
			# cnt 升星需要次数
			self.cnt = 0
		

    def load_from_json(self, data):
		
			# id 宠物洗练星级表
			self.id = data.get("id",0)
		
			# cnt 升星需要次数
			self.cnt = data.get("cnt",0)
		

# petteamtype
class ResPetteamtype(object):
	RES_TABLE = "petteamtype"
	__slots__ = ("id","limit","unshow","addobj","addAttr",)

    def __init__(self):
		
			# id 羁绊组合
			self.id = 0
		
			# limit 对应条件
			self.limit = []
		
			# unshow 屏蔽骚操作
			self.unshow = 0
		
			# addobj 增益对象
			self.addobj = []
		
			# addAttr 增加属性
			self.addAttr = []
		

    def load_from_json(self, data):
		
			# id 羁绊组合
			self.id = data.get("id",0)
		
			# limit 对应条件
			self.limit = data.get("limit",[])
		
			# unshow 屏蔽骚操作
			self.unshow = data.get("unshow",0)
		
			# addobj 增益对象
			self.addobj = data.get("addobj",[])
		
			# addAttr 增加属性
			self.addAttr = data.get("addAttr",[])
		

# pet
class ResPet(object):
	RES_TABLE = "pet"
	__slots__ = ("id","washSatr","passiveSkillIds","passiveSkillCnt","peculiaritySkillIds","cost","catchItemid","baseAttr","isShowSpec","eatExp","eatAttr","isSpec","mutexList","teamType","mark","maskImg","practiceSkillIds",)

    def __init__(self):
		
			# id 宠物表
			self.id = 0
		
			# washSatr 默认洗练星级
			self.washSatr = 0
		
			# passiveSkillIds 初始被动技能id列表
			self.passiveSkillIds = []
		
			# passiveSkillCnt 初始被动技能数
			self.passiveSkillCnt = 0
		
			# peculiaritySkillIds 特质技能id列表(0:没有技能1:占坑其余:技能Id有技能备注:5星以下的不填就好)
			self.peculiaritySkillIds = []
		
			# cost 激活材料
			self.cost = []
		
			# catchItemid 抓捕时掉落的卡片道具
			self.catchItemid = 0
		
			# baseAttr 基础属性
			self.baseAttr = []
		
			# isShowSpec 稀有属性标识
			self.isShowSpec = 0
		
			# eatExp 吃卡经验
			self.eatExp = 0
		
			# eatAttr 吃卡属性
			self.eatAttr = []
		
			# isSpec 是否特典宠物
			self.isSpec = 0
		
			# mutexList 上阵互斥宠物列表
			self.mutexList = []
		
			# teamType 羁绊类型
			self.teamType = 0
		
			# mark 类型标识
			self.mark = 0
		
			# maskImg 类型标识图标
			self.maskImg = []
		
			# practiceSkillIds 可洗练特性
			self.practiceSkillIds = []
		

    def load_from_json(self, data):
		
			# id 宠物表
			self.id = data.get("id",0)
		
			# washSatr 默认洗练星级
			self.washSatr = data.get("washSatr",0)
		
			# passiveSkillIds 初始被动技能id列表
			self.passiveSkillIds = data.get("passiveSkillIds",[])
		
			# passiveSkillCnt 初始被动技能数
			self.passiveSkillCnt = data.get("passiveSkillCnt",0)
		
			# peculiaritySkillIds 特质技能id列表(0:没有技能1:占坑其余:技能Id有技能备注:5星以下的不填就好)
			self.peculiaritySkillIds = data.get("peculiaritySkillIds",[])
		
			# cost 激活材料
			self.cost = data.get("cost",[])
		
			# catchItemid 抓捕时掉落的卡片道具
			self.catchItemid = data.get("catchItemid",0)
		
			# baseAttr 基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# isShowSpec 稀有属性标识
			self.isShowSpec = data.get("isShowSpec",0)
		
			# eatExp 吃卡经验
			self.eatExp = data.get("eatExp",0)
		
			# eatAttr 吃卡属性
			self.eatAttr = data.get("eatAttr",[])
		
			# isSpec 是否特典宠物
			self.isSpec = data.get("isSpec",0)
		
			# mutexList 上阵互斥宠物列表
			self.mutexList = data.get("mutexList",[])
		
			# teamType 羁绊类型
			self.teamType = data.get("teamType",0)
		
			# mark 类型标识
			self.mark = data.get("mark",0)
		
			# maskImg 类型标识图标
			self.maskImg = data.get("maskImg",[])
		
			# practiceSkillIds 可洗练特性
			self.practiceSkillIds = data.get("practiceSkillIds",[])
		

# petalbum
class ResPetalbum(object):
	RES_TABLE = "petalbum"
	__slots__ = ("id","eleType","eleVal","need","attr","lv",)

    def __init__(self):
		
			# id 宠物图鉴表
			self.id = 0
		
			# eleType 五行属性类型
			self.eleType = 0
		
			# eleVal 五行属性值
			self.eleVal = 0
		
			# need 需求数量
			self.need = 0
		
			# attr 属性
			self.attr = []
		
			# lv 说明
			self.lv = 0
		

    def load_from_json(self, data):
		
			# id 宠物图鉴表
			self.id = data.get("id",0)
		
			# eleType 五行属性类型
			self.eleType = data.get("eleType",0)
		
			# eleVal 五行属性值
			self.eleVal = data.get("eleVal",0)
		
			# need 需求数量
			self.need = data.get("need",0)
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# lv 说明
			self.lv = data.get("lv",0)
		

# petSpecAlbum
class ResPetSpecAlbum(object):
	RES_TABLE = "petSpecAlbum"
	__slots__ = ("id","need","attr","attr2","lv",)

    def __init__(self):
		
			# id 特典宠物图鉴表
			self.id = 0
		
			# need 需求数量
			self.need = 0
		
			# attr 总属性
			self.attr = []
		
			# attr2 每一阶属性
			self.attr2 = []
		
			# lv 说明
			self.lv = 0
		

    def load_from_json(self, data):
		
			# id 特典宠物图鉴表
			self.id = data.get("id",0)
		
			# need 需求数量
			self.need = data.get("need",0)
		
			# attr 总属性
			self.attr = data.get("attr",[])
		
			# attr2 每一阶属性
			self.attr2 = data.get("attr2",[])
		
			# lv 说明
			self.lv = data.get("lv",0)
		

# petSpecialTask
class ResPetSpecialTask(object):
	RES_TABLE = "petSpecialTask"
	__slots__ = ("id","albumNum","type","poolId","rate","actId","roleLv","taskList","cost","reward",)

    def __init__(self):
		
			# id 特典宠物任务
			self.id = 0
		
			# albumNum 图鉴数量限制
			self.albumNum = 0
		
			# type 类型
			self.type = 0
		
			# poolId 池子
			self.poolId = 0
		
			# rate 权重
			self.rate = 0
		
			# actId 活动id
			self.actId = 0
		
			# roleLv 角色等级
			self.roleLv = 0
		
			# taskList 任务列表
			self.taskList = []
		
			# cost 花费道具
			self.cost = []
		
			# reward 获得奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 特典宠物任务
			self.id = data.get("id",0)
		
			# albumNum 图鉴数量限制
			self.albumNum = data.get("albumNum",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# poolId 池子
			self.poolId = data.get("poolId",0)
		
			# rate 权重
			self.rate = data.get("rate",0)
		
			# actId 活动id
			self.actId = data.get("actId",0)
		
			# roleLv 角色等级
			self.roleLv = data.get("roleLv",0)
		
			# taskList 任务列表
			self.taskList = data.get("taskList",[])
		
			# cost 花费道具
			self.cost = data.get("cost",[])
		
			# reward 获得奖励
			self.reward = data.get("reward",[])
		

# title
class ResTitle(object):
	RES_TABLE = "title"
	__slots__ = ("id","type","typeName","bg","attr","cost",)

    def __init__(self):
		
			# id 称号表
			self.id = 0
		
			# type 类型
			self.type = 0
		
			# typeName 类型名
			self.typeName = ""
		
			# bg 底图
			self.bg = ""
		
			# attr 属性
			self.attr = []
		
			# cost 消耗道具
			self.cost = []
		

    def load_from_json(self, data):
		
			# id 称号表
			self.id = data.get("id",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# typeName 类型名
			self.typeName = data.get("typeName","")
		
			# bg 底图
			self.bg = data.get("bg","")
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		

# petzizhi
class ResPetzizhi(object):
	RES_TABLE = "petzizhi"
	__slots__ = ("id","petId","lv","name","rollbackCost","cost","costCnt","cost2","attr","additionAddr","baseAttr","oldCostCnt",)

    def __init__(self):
		
			# id 宠物资质表
			self.id = 0
		
			# petId 宠物id
			self.petId = 0
		
			# lv 等级
			self.lv = 0
		
			# name 名称
			self.name = ""
		
			# rollbackCost 资质退还消耗
			self.rollbackCost = []
		
			# cost 升阶消耗道具id
			self.cost = 0
		
			# costCnt 资质升阶需求数量
			self.costCnt = 0
		
			# cost2 升阶消耗道具id(万能卡)
			self.cost2 = 0
		
			# attr 每张卡片属性加成
			self.attr = []
		
			# additionAddr 资质升级额外加成
			self.additionAddr = []
		
			# baseAttr 当前等级加满属性加成
			self.baseAttr = []
		
			# oldCostCnt 旧版资质升阶需卡数量
			self.oldCostCnt = 0
		

    def load_from_json(self, data):
		
			# id 宠物资质表
			self.id = data.get("id",0)
		
			# petId 宠物id
			self.petId = data.get("petId",0)
		
			# lv 等级
			self.lv = data.get("lv",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# rollbackCost 资质退还消耗
			self.rollbackCost = data.get("rollbackCost",[])
		
			# cost 升阶消耗道具id
			self.cost = data.get("cost",0)
		
			# costCnt 资质升阶需求数量
			self.costCnt = data.get("costCnt",0)
		
			# cost2 升阶消耗道具id(万能卡)
			self.cost2 = data.get("cost2",0)
		
			# attr 每张卡片属性加成
			self.attr = data.get("attr",[])
		
			# additionAddr 资质升级额外加成
			self.additionAddr = data.get("additionAddr",[])
		
			# baseAttr 当前等级加满属性加成
			self.baseAttr = data.get("baseAttr",[])
		
			# oldCostCnt 旧版资质升阶需卡数量
			self.oldCostCnt = data.get("oldCostCnt",0)
		

# wingskin
class ResWingskin(object):
	RES_TABLE = "wingskin"
	__slots__ = ("id","name","type","typeName","bg","attr","cost","offX","offY","scale",)

    def __init__(self):
		
			# id 翅膀皮肤表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# type 类型
			self.type = 0
		
			# typeName 类型名
			self.typeName = ""
		
			# bg 底图
			self.bg = ""
		
			# attr 属性
			self.attr = []
		
			# cost 消耗道具
			self.cost = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		

    def load_from_json(self, data):
		
			# id 翅膀皮肤表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# type 类型
			self.type = data.get("type",0)
		
			# typeName 类型名
			self.typeName = data.get("typeName","")
		
			# bg 底图
			self.bg = data.get("bg","")
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		

# wing
class ResWing(object):
	RES_TABLE = "wing"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","defeVal","hpVal","skillLvLimit","actSkill","jjreward","offX","offY","scale","effectTip",)

    def __init__(self):
		
			# id 翅膀表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# defeVal 防御继承（千分比）
			self.defeVal = 0
		
			# hpVal 血量继承（千分比）
			self.hpVal = 0
		
			# skillLvLimit 百变怪技能上限
			self.skillLvLimit = 0
		
			# actSkill 激活增幅器技能
			self.actSkill = 0
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# effectTip 特效升级提示
			self.effectTip = ""
		

    def load_from_json(self, data):
		
			# id 翅膀表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# defeVal 防御继承（千分比）
			self.defeVal = data.get("defeVal",0)
		
			# hpVal 血量继承（千分比）
			self.hpVal = data.get("hpVal",0)
		
			# skillLvLimit 百变怪技能上限
			self.skillLvLimit = data.get("skillLvLimit",0)
		
			# actSkill 激活增幅器技能
			self.actSkill = data.get("actSkill",0)
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# effectTip 特效升级提示
			self.effectTip = data.get("effectTip","")
		

# wingskill
class ResWingskill(object):
	RES_TABLE = "wingskill"
	__slots__ = ("id","skillId","lv","name","cost","attr","icon",)

    def __init__(self):
		
			# id 翅膀技能表
			self.id = 0
		
			# skillId 技能id
			self.skillId = 0
		
			# lv 技能等级
			self.lv = 0
		
			# name 名称
			self.name = ""
		
			# cost 升级消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		
			# icon 图标
			self.icon = ""
		

    def load_from_json(self, data):
		
			# id 翅膀技能表
			self.id = data.get("id",0)
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		
			# lv 技能等级
			self.lv = data.get("lv",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# cost 升级消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# icon 图标
			self.icon = data.get("icon","")
		

# petwash
class ResPetwash(object):
	RES_TABLE = "petwash"
	__slots__ = ("id","petId","star","passiveSkillIds",)

    def __init__(self):
		
			# id 宠物洗练表
			self.id = 0
		
			# petId 宠物id
			self.petId = 0
		
			# star 洗练星级
			self.star = 0
		
			# passiveSkillIds 被动技能id列表
			self.passiveSkillIds = []
		

    def load_from_json(self, data):
		
			# id 宠物洗练表
			self.id = data.get("id",0)
		
			# petId 宠物id
			self.petId = data.get("petId",0)
		
			# star 洗练星级
			self.star = data.get("star",0)
		
			# passiveSkillIds 被动技能id列表
			self.passiveSkillIds = data.get("passiveSkillIds",[])
		

# danyao
class ResDanyao(object):
	RES_TABLE = "danyao"
	__slots__ = ("key","itemId","attr",)

    def __init__(self):
		
			# key 类型
			self.key = 0
		
			# itemId 丹药表
			self.itemId = 0
		
			# attr 增加属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# key 类型
			self.key = data.get("key",0)
		
			# itemId 丹药表
			self.itemId = data.get("itemId",0)
		
			# attr 增加属性
			self.attr = data.get("attr",[])
		

# exchange
class ResExchange(object):
	RES_TABLE = "exchange"
	__slots__ = ("id","type","itemId","equipId","num","cost",)

    def __init__(self):
		
			# id 兑换表
			self.id = 0
		
			# type 标签类型
			self.type = 0
		
			# itemId 物品ID
			self.itemId = 0
		
			# equipId 装备id
			self.equipId = 0
		
			# num 数量
			self.num = 0
		
			# cost 消耗物品
			self.cost = []
		

    def load_from_json(self, data):
		
			# id 兑换表
			self.id = data.get("id",0)
		
			# type 标签类型
			self.type = data.get("type",0)
		
			# itemId 物品ID
			self.itemId = data.get("itemId",0)
		
			# equipId 装备id
			self.equipId = data.get("equipId",0)
		
			# num 数量
			self.num = data.get("num",0)
		
			# cost 消耗物品
			self.cost = data.get("cost",[])
		

# errorTip
class ResErrorTip(object):
	RES_TABLE = "errorTip"
	__slots__ = ("id","content",)

    def __init__(self):
		
			# id 错误代码
			self.id = 0
		
			# content 错误文本
			self.content = ""
		

    def load_from_json(self, data):
		
			# id 错误代码
			self.id = data.get("id",0)
		
			# content 错误文本
			self.content = data.get("content","")
		

# petevolve
class ResPetevolve(object):
	RES_TABLE = "petevolve"
	__slots__ = ("id","petId","evolveLv","name","albumPos","specAlbumPos","evolveStep","needLv","needTalentLv","cost","mainSkillId","quality","attr","damageAddClient","damageAdd","type","skillAddCnt","skillAdd","maxPit","offX","offY","scale","notice","attrValue","atkValue","hpValue","defValue","speedValue","atkRate","hpRate","defRate","speedRate","eleType","eleVal","oriType","specType",)

    def __init__(self):
		
			# id 进化表
			self.id = 0
		
			# petId 宠物id
			self.petId = 0
		
			# evolveLv 进化阶数
			self.evolveLv = 0
		
			# name 名称
			self.name = ""
		
			# albumPos 图鉴位置(行列)
			self.albumPos = []
		
			# specAlbumPos 特典图鉴位置(行列)
			self.specAlbumPos = []
		
			# evolveStep 当前形态进阶数
			self.evolveStep = 0
		
			# needLv 需要等级
			self.needLv = 0
		
			# needTalentLv 需要等级
			self.needTalentLv = 0
		
			# cost 进化消耗
			self.cost = []
		
			# mainSkillId 主动技能id
			self.mainSkillId = 0
		
			# quality 品质
			self.quality = 0
		
			# attr 额外属性
			self.attr = []
		
			# damageAddClient 客户端威力显示(需要除10000)
			self.damageAddClient = 0
		
			# damageAdd 当前技能伤害率增加（千分比）
			self.damageAdd = 0
		
			# type 宠物类型
			self.type = 0
		
			# skillAddCnt 被动技能增加数量
			self.skillAddCnt = 0
		
			# skillAdd 增加被动技能ID
			self.skillAdd = []
		
			# maxPit 最大特效坑位
			self.maxPit = 0
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# notice 进化需要广告填1
			self.notice = 0
		
			# attrValue 总属性继承千分比
			self.attrValue = 0
		
			# atkValue 攻击种族值
			self.atkValue = 0
		
			# hpValue 血量种族值
			self.hpValue = 0
		
			# defValue 防御种族值
			self.defValue = 0
		
			# speedValue 速度种族值
			self.speedValue = 0
		
			# atkRate 攻击继承千分比
			self.atkRate = 0
		
			# hpRate 血量继承千分比
			self.hpRate = 0
		
			# defRate 防御继承千分比
			self.defRate = 0
		
			# speedRate 速度继承千分比
			self.speedRate = 0
		
			# eleType 五行属性类型
			self.eleType = 0
		
			# eleVal 五行属性值
			self.eleVal = 0
		
			# oriType 定位类型
			self.oriType = 0
		
			# specType 种族类型
			self.specType = 0
		

    def load_from_json(self, data):
		
			# id 进化表
			self.id = data.get("id",0)
		
			# petId 宠物id
			self.petId = data.get("petId",0)
		
			# evolveLv 进化阶数
			self.evolveLv = data.get("evolveLv",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# albumPos 图鉴位置(行列)
			self.albumPos = data.get("albumPos",[])
		
			# specAlbumPos 特典图鉴位置(行列)
			self.specAlbumPos = data.get("specAlbumPos",[])
		
			# evolveStep 当前形态进阶数
			self.evolveStep = data.get("evolveStep",0)
		
			# needLv 需要等级
			self.needLv = data.get("needLv",0)
		
			# needTalentLv 需要等级
			self.needTalentLv = data.get("needTalentLv",0)
		
			# cost 进化消耗
			self.cost = data.get("cost",[])
		
			# mainSkillId 主动技能id
			self.mainSkillId = data.get("mainSkillId",0)
		
			# quality 品质
			self.quality = data.get("quality",0)
		
			# attr 额外属性
			self.attr = data.get("attr",[])
		
			# damageAddClient 客户端威力显示(需要除10000)
			self.damageAddClient = data.get("damageAddClient",0)
		
			# damageAdd 当前技能伤害率增加（千分比）
			self.damageAdd = data.get("damageAdd",0)
		
			# type 宠物类型
			self.type = data.get("type",0)
		
			# skillAddCnt 被动技能增加数量
			self.skillAddCnt = data.get("skillAddCnt",0)
		
			# skillAdd 增加被动技能ID
			self.skillAdd = data.get("skillAdd",[])
		
			# maxPit 最大特效坑位
			self.maxPit = data.get("maxPit",0)
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# notice 进化需要广告填1
			self.notice = data.get("notice",0)
		
			# attrValue 总属性继承千分比
			self.attrValue = data.get("attrValue",0)
		
			# atkValue 攻击种族值
			self.atkValue = data.get("atkValue",0)
		
			# hpValue 血量种族值
			self.hpValue = data.get("hpValue",0)
		
			# defValue 防御种族值
			self.defValue = data.get("defValue",0)
		
			# speedValue 速度种族值
			self.speedValue = data.get("speedValue",0)
		
			# atkRate 攻击继承千分比
			self.atkRate = data.get("atkRate",0)
		
			# hpRate 血量继承千分比
			self.hpRate = data.get("hpRate",0)
		
			# defRate 防御继承千分比
			self.defRate = data.get("defRate",0)
		
			# speedRate 速度继承千分比
			self.speedRate = data.get("speedRate",0)
		
			# eleType 五行属性类型
			self.eleType = data.get("eleType",0)
		
			# eleVal 五行属性值
			self.eleVal = data.get("eleVal",0)
		
			# oriType 定位类型
			self.oriType = data.get("oriType",0)
		
			# specType 种族类型
			self.specType = data.get("specType",0)
		

# transport
class ResTransport(object):
	RES_TABLE = "transport"
	__slots__ = ("id","srcMapId","type","name","srcPosx","srcPosy","DesMapId","name2","desPosx","desPosy","validRange","iconId","hide",)

    def __init__(self):
		
			# id 传送表
			self.id = 0
		
			# srcMapId 源传送地图ID
			self.srcMapId = 0
		
			# type 类型
			self.type = 0
		
			# name 地图名称
			self.name = ""
		
			# srcPosx 源传送点X坐标
			self.srcPosx = 0
		
			# srcPosy 源传送点Y坐标
			self.srcPosy = 0
		
			# DesMapId 目标传送地图ID
			self.DesMapId = 0
		
			# name2 目标地图名称
			self.name2 = ""
		
			# desPosx 目标传送地图X坐标
			self.desPosx = 0
		
			# desPosy 目标传送地图Y坐标
			self.desPosy = 0
		
			# validRange 有效半径
			self.validRange = 0
		
			# iconId 资源ID
			self.iconId = 0
		
			# hide 前端隐藏传送点
			self.hide = 0
		

    def load_from_json(self, data):
		
			# id 传送表
			self.id = data.get("id",0)
		
			# srcMapId 源传送地图ID
			self.srcMapId = data.get("srcMapId",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# name 地图名称
			self.name = data.get("name","")
		
			# srcPosx 源传送点X坐标
			self.srcPosx = data.get("srcPosx",0)
		
			# srcPosy 源传送点Y坐标
			self.srcPosy = data.get("srcPosy",0)
		
			# DesMapId 目标传送地图ID
			self.DesMapId = data.get("DesMapId",0)
		
			# name2 目标地图名称
			self.name2 = data.get("name2","")
		
			# desPosx 目标传送地图X坐标
			self.desPosx = data.get("desPosx",0)
		
			# desPosy 目标传送地图Y坐标
			self.desPosy = data.get("desPosy",0)
		
			# validRange 有效半径
			self.validRange = data.get("validRange",0)
		
			# iconId 资源ID
			self.iconId = data.get("iconId",0)
		
			# hide 前端隐藏传送点
			self.hide = data.get("hide",0)
		

# catch
class ResCatch(object):
	RES_TABLE = "catch"
	__slots__ = ("id","openDay","minLv","maxLv","odds","greenSuss","blueSuss","purpleSuss","green","blue","purple","pets",)

    def __init__(self):
		
			# id 抓捕表
		
			# openDay 开服天数
			self.openDay = 0
		
			# minLv 最小等级
			self.minLv = 0
		
			# maxLv 最大等级
			self.maxLv = 0
		
			# odds 概率
			self.odds = []
		
			# greenSuss 绿色成功率
			self.greenSuss = 0
		
			# blueSuss 蓝色成功率
			self.blueSuss = 0
		
			# purpleSuss 紫色成功率
			self.purpleSuss = 0
		
			# green 绿色宠物ID…（多个）
			self.green = []
		
			# blue 蓝色宠物ID…（多个）
			self.blue = []
		
			# purple 紫色宠物ID…（多个）
			self.purple = []
		
			# pets 必定是需先激活的宠物ID
			self.pets = []
		

    def load_from_json(self, data):
		
			# id 抓捕表
		
			# openDay 开服天数
			self.openDay = data.get("openDay",0)
		
			# minLv 最小等级
			self.minLv = data.get("minLv",0)
		
			# maxLv 最大等级
			self.maxLv = data.get("maxLv",0)
		
			# odds 概率
			self.odds = data.get("odds",[])
		
			# greenSuss 绿色成功率
			self.greenSuss = data.get("greenSuss",0)
		
			# blueSuss 蓝色成功率
			self.blueSuss = data.get("blueSuss",0)
		
			# purpleSuss 紫色成功率
			self.purpleSuss = data.get("purpleSuss",0)
		
			# green 绿色宠物ID…（多个）
			self.green = data.get("green",[])
		
			# blue 蓝色宠物ID…（多个）
			self.blue = data.get("blue",[])
		
			# purple 紫色宠物ID…（多个）
			self.purple = data.get("purple",[])
		
			# pets 必定是需先激活的宠物ID
			self.pets = data.get("pets",[])
		

# groupPKwinReward
class ResGroupPKwinReward(object):
	RES_TABLE = "groupPKwinReward"
	__slots__ = ("id","win","reward",)

    def __init__(self):
		
			# id 对决赛每日胜场目标
			self.id = 0
		
			# win 胜利数
			self.win = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 对决赛每日胜场目标
			self.id = data.get("id",0)
		
			# win 胜利数
			self.win = data.get("win",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# groupPKLevel
class ResGroupPKLevel(object):
	RES_TABLE = "groupPKLevel"
	__slots__ = ("id","name","stScore","endScore","upReward","endReward","reduceScore","winReward",)

    def __init__(self):
		
			# id 对决赛段位
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# stScore 开始积分
			self.stScore = 0
		
			# endScore 结束积分
			self.endScore = 0
		
			# upReward 段位晋升奖励(历史首次
			self.upReward = []
		
			# endReward 段位结算奖励（每周结算）
			self.endReward = []
		
			# reduceScore 段位降级下降积分
			self.reduceScore = 0
		
			# winReward 胜利获得奖励id
			self.winReward = 0
		

    def load_from_json(self, data):
		
			# id 对决赛段位
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# stScore 开始积分
			self.stScore = data.get("stScore",0)
		
			# endScore 结束积分
			self.endScore = data.get("endScore",0)
		
			# upReward 段位晋升奖励(历史首次
			self.upReward = data.get("upReward",[])
		
			# endReward 段位结算奖励（每周结算）
			self.endReward = data.get("endReward",[])
		
			# reduceScore 段位降级下降积分
			self.reduceScore = data.get("reduceScore",0)
		
			# winReward 胜利获得奖励id
			self.winReward = data.get("winReward",0)
		

# worldmap
class ResWorldmap(object):
	RES_TABLE = "worldmap"
	__slots__ = ("id","lvMode","name","lv","interval","icon","meetList","spIdArr","petIdArr","desc",)

    def __init__(self):
		
			# id 世界地图表
			self.id = 0
		
			# lvMode 难度等级
			self.lvMode = 0
		
			# name 名称
			self.name = ""
		
			# lv 进入等级
			self.lv = 0
		
			# interval 遇怪间隔时间
			self.interval = 0
		
			# icon 图标
			self.icon = ""
		
			# meetList 挂机可遭遇怪id
			self.meetList = []
		
			# spIdArr 世界地图碎片图标道具id
			self.spIdArr = []
		
			# petIdArr 提示宠物道具ID
			self.petIdArr = []
		
			# desc 提示说明
			self.desc = ""
		

    def load_from_json(self, data):
		
			# id 世界地图表
			self.id = data.get("id",0)
		
			# lvMode 难度等级
			self.lvMode = data.get("lvMode",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# lv 进入等级
			self.lv = data.get("lv",0)
		
			# interval 遇怪间隔时间
			self.interval = data.get("interval",0)
		
			# icon 图标
			self.icon = data.get("icon","")
		
			# meetList 挂机可遭遇怪id
			self.meetList = data.get("meetList",[])
		
			# spIdArr 世界地图碎片图标道具id
			self.spIdArr = data.get("spIdArr",[])
		
			# petIdArr 提示宠物道具ID
			self.petIdArr = data.get("petIdArr",[])
		
			# desc 提示说明
			self.desc = data.get("desc","")
		

# scene
class ResScene(object):
	RES_TABLE = "scene"
	__slots__ = ("id","name","type","resId","posx","posy","dir","zkfmPos","npc",)

    def __init__(self):
		
			# id 场景表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# type 类型
			self.type = 0
		
			# resId 地图资源(障碍)
			self.resId = 0
		
			# posx 出生点X坐标
			self.posx = 0
		
			# posy 出生点Y坐标
			self.posy = 0
		
			# dir 出生点方向
			self.dir = 0
		
			# zkfmPos 钟馗伏魔坐标
			self.zkfmPos = []
		
			# npc npc列表
			self.npc = []
		

    def load_from_json(self, data):
		
			# id 场景表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# type 类型
			self.type = data.get("type",0)
		
			# resId 地图资源(障碍)
			self.resId = data.get("resId",0)
		
			# posx 出生点X坐标
			self.posx = data.get("posx",0)
		
			# posy 出生点Y坐标
			self.posy = data.get("posy",0)
		
			# dir 出生点方向
			self.dir = data.get("dir",0)
		
			# zkfmPos 钟馗伏魔坐标
			self.zkfmPos = data.get("zkfmPos",[])
		
			# npc npc列表
			self.npc = data.get("npc",[])
		

# groupPKfinalscore
class ResGroupPKfinalscore(object):
	RES_TABLE = "groupPKfinalscore"
	__slots__ = ("id","win","loss","maxcall","winReward","lossReward",)

    def __init__(self):
		
			# id 对决赛决赛积分
			self.id = 0
		
			# win 胜利积分
			self.win = 0
		
			# loss 失败积分
			self.loss = 0
		
			# maxcall 打call上限
			self.maxcall = 0
		
			# winReward 赛程奖励（胜利）
			self.winReward = []
		
			# lossReward 赛程奖励（失败）
			self.lossReward = []
		

    def load_from_json(self, data):
		
			# id 对决赛决赛积分
			self.id = data.get("id",0)
		
			# win 胜利积分
			self.win = data.get("win",0)
		
			# loss 失败积分
			self.loss = data.get("loss",0)
		
			# maxcall 打call上限
			self.maxcall = data.get("maxcall",0)
		
			# winReward 赛程奖励（胜利）
			self.winReward = data.get("winReward",[])
		
			# lossReward 赛程奖励（失败）
			self.lossReward = data.get("lossReward",[])
		

# groupPKMatch
class ResGroupPKMatch(object):
	RES_TABLE = "groupPKMatch"
	__slots__ = ("id","type","stScore","endScore","winScore",)

    def __init__(self):
		
			# id 对决赛匹配
			self.id = 0
		
			# type 分组
			self.type = 0
		
			# stScore 积分差(起始)
			self.stScore = 0
		
			# endScore 积分差(结束)
			self.endScore = 0
		
			# winScore 击败获得
			self.winScore = 0
		

    def load_from_json(self, data):
		
			# id 对决赛匹配
			self.id = data.get("id",0)
		
			# type 分组
			self.type = data.get("type",0)
		
			# stScore 积分差(起始)
			self.stScore = data.get("stScore",0)
		
			# endScore 积分差(结束)
			self.endScore = data.get("endScore",0)
		
			# winScore 击败获得
			self.winScore = data.get("winScore",0)
		

# groupPKfinalRankReward
class ResGroupPKfinalRankReward(object):
	RES_TABLE = "groupPKfinalRankReward"
	__slots__ = ("id","stRank","endRank","reward",)

    def __init__(self):
		
			# id 对决赛决赛排名奖励
			self.id = 0
		
			# stRank 开始排名
			self.stRank = 0
		
			# endRank 结束排名
			self.endRank = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 对决赛决赛排名奖励
			self.id = data.get("id",0)
		
			# stRank 开始排名
			self.stRank = data.get("stRank",0)
		
			# endRank 结束排名
			self.endRank = data.get("endRank",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# levelContestRank3
class ResLevelContestRank3(object):
	RES_TABLE = "levelContestRank3"
	__slots__ = ("id","min","max","barrierId","monster","name","fa",)

    def __init__(self):
		
			# id 段位赛3
			self.id = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# barrierId 副本id
			self.barrierId = 0
		
			# monster 电脑显示模型id
			self.monster = []
		
			# name 电脑名称
			self.name = ""
		
			# fa 战力
			self.fa = 0
		

    def load_from_json(self, data):
		
			# id 段位赛3
			self.id = data.get("id",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# barrierId 副本id
			self.barrierId = data.get("barrierId",0)
		
			# monster 电脑显示模型id
			self.monster = data.get("monster",[])
		
			# name 电脑名称
			self.name = data.get("name","")
		
			# fa 战力
			self.fa = data.get("fa",0)
		

# levelContestRank2
class ResLevelContestRank2(object):
	RES_TABLE = "levelContestRank2"
	__slots__ = ("id","min","max","barrierId","monster","name","fa",)

    def __init__(self):
		
			# id 段位赛2
			self.id = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# barrierId 副本id
			self.barrierId = 0
		
			# monster 电脑显示模型id
			self.monster = []
		
			# name 电脑名称
			self.name = ""
		
			# fa 战力
			self.fa = 0
		

    def load_from_json(self, data):
		
			# id 段位赛2
			self.id = data.get("id",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# barrierId 副本id
			self.barrierId = data.get("barrierId",0)
		
			# monster 电脑显示模型id
			self.monster = data.get("monster",[])
		
			# name 电脑名称
			self.name = data.get("name","")
		
			# fa 战力
			self.fa = data.get("fa",0)
		

# levelContestRankReward1
class ResLevelContestRankReward1(object):
	RES_TABLE = "levelContestRankReward1"
	__slots__ = ("id","min","max","rankReward",)

    def __init__(self):
		
			# id 段位赛排名奖励1
			self.id = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# rankReward 排名奖励
			self.rankReward = []
		

    def load_from_json(self, data):
		
			# id 段位赛排名奖励1
			self.id = data.get("id",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# rankReward 排名奖励
			self.rankReward = data.get("rankReward",[])
		

# levelContestRankReward4
class ResLevelContestRankReward4(object):
	RES_TABLE = "levelContestRankReward4"
	__slots__ = ("id","min","max","rankReward",)

    def __init__(self):
		
			# id 段位赛排名奖励4
			self.id = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# rankReward 排名奖励
			self.rankReward = []
		

    def load_from_json(self, data):
		
			# id 段位赛排名奖励4
			self.id = data.get("id",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# rankReward 排名奖励
			self.rankReward = data.get("rankReward",[])
		

# levelContestConst
class ResLevelContestConst(object):
	RES_TABLE = "levelContestConst"
	__slots__ = ("id","name","icon","color","totalNum","upNeed","upOpenDay","copyIdList","bossName","avatarIdList","upDesc",)

    def __init__(self):
		
			# id 段位常量
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# icon 图标
			self.icon = ""
		
			# color 对应颜色
			self.color = ""
		
			# totalNum 排行榜人数
			self.totalNum = 0
		
			# upNeed 前几名可以参与晋级赛
			self.upNeed = 0
		
			# upOpenDay 开服第几天开启晋级
			self.upOpenDay = 0
		
			# copyIdList 晋级赛副本id
			self.copyIdList = []
		
			# bossName 馆主名
			self.bossName = []
		
			# avatarIdList 馆主AvatarId
			self.avatarIdList = []
		
			# upDesc 晋级流程描述
			self.upDesc = ""
		

    def load_from_json(self, data):
		
			# id 段位常量
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# icon 图标
			self.icon = data.get("icon","")
		
			# color 对应颜色
			self.color = data.get("color","")
		
			# totalNum 排行榜人数
			self.totalNum = data.get("totalNum",0)
		
			# upNeed 前几名可以参与晋级赛
			self.upNeed = data.get("upNeed",0)
		
			# upOpenDay 开服第几天开启晋级
			self.upOpenDay = data.get("upOpenDay",0)
		
			# copyIdList 晋级赛副本id
			self.copyIdList = data.get("copyIdList",[])
		
			# bossName 馆主名
			self.bossName = data.get("bossName",[])
		
			# avatarIdList 馆主AvatarId
			self.avatarIdList = data.get("avatarIdList",[])
		
			# upDesc 晋级流程描述
			self.upDesc = data.get("upDesc","")
		

# levelContestRank4
class ResLevelContestRank4(object):
	RES_TABLE = "levelContestRank4"
	__slots__ = ("id","min","max","barrierId","monster","name","fa",)

    def __init__(self):
		
			# id 段位赛4
			self.id = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# barrierId 副本id
			self.barrierId = 0
		
			# monster 电脑显示模型id
			self.monster = []
		
			# name 电脑名称
			self.name = ""
		
			# fa 战力
			self.fa = 0
		

    def load_from_json(self, data):
		
			# id 段位赛4
			self.id = data.get("id",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# barrierId 副本id
			self.barrierId = data.get("barrierId",0)
		
			# monster 电脑显示模型id
			self.monster = data.get("monster",[])
		
			# name 电脑名称
			self.name = data.get("name","")
		
			# fa 战力
			self.fa = data.get("fa",0)
		

# levelContestRankReward3
class ResLevelContestRankReward3(object):
	RES_TABLE = "levelContestRankReward3"
	__slots__ = ("id","min","max","rankReward",)

    def __init__(self):
		
			# id 段位赛排名奖励3
			self.id = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# rankReward 排名奖励
			self.rankReward = []
		

    def load_from_json(self, data):
		
			# id 段位赛排名奖励3
			self.id = data.get("id",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# rankReward 排名奖励
			self.rankReward = data.get("rankReward",[])
		

# levelContestRank1
class ResLevelContestRank1(object):
	RES_TABLE = "levelContestRank1"
	__slots__ = ("id","min","max","barrierId","monster","name","fa",)

    def __init__(self):
		
			# id 段位赛1
			self.id = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# barrierId 副本id
			self.barrierId = 0
		
			# monster 电脑显示模型id
			self.monster = []
		
			# name 电脑名称
			self.name = ""
		
			# fa 战力
			self.fa = 0
		

    def load_from_json(self, data):
		
			# id 段位赛1
			self.id = data.get("id",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# barrierId 副本id
			self.barrierId = data.get("barrierId",0)
		
			# monster 电脑显示模型id
			self.monster = data.get("monster",[])
		
			# name 电脑名称
			self.name = data.get("name","")
		
			# fa 战力
			self.fa = data.get("fa",0)
		

# levelContestScoreReward
class ResLevelContestScoreReward(object):
	RES_TABLE = "levelContestScoreReward"
	__slots__ = ("id","need","reward",)

    def __init__(self):
		
			# id 段位赛积分奖励
			self.id = 0
		
			# need 积分达到
			self.need = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 段位赛积分奖励
			self.id = data.get("id",0)
		
			# need 积分达到
			self.need = data.get("need",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# levelContestRankReward5
class ResLevelContestRankReward5(object):
	RES_TABLE = "levelContestRankReward5"
	__slots__ = ("id","min","max","rankReward",)

    def __init__(self):
		
			# id 段位赛排名奖励5
			self.id = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# rankReward 排名奖励
			self.rankReward = []
		

    def load_from_json(self, data):
		
			# id 段位赛排名奖励5
			self.id = data.get("id",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# rankReward 排名奖励
			self.rankReward = data.get("rankReward",[])
		

# levelContestRankReward2
class ResLevelContestRankReward2(object):
	RES_TABLE = "levelContestRankReward2"
	__slots__ = ("id","min","max","rankReward",)

    def __init__(self):
		
			# id 段位赛排名奖励2
			self.id = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# rankReward 排名奖励
			self.rankReward = []
		

    def load_from_json(self, data):
		
			# id 段位赛排名奖励2
			self.id = data.get("id",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# rankReward 排名奖励
			self.rankReward = data.get("rankReward",[])
		

# playerLevelGift
class ResPlayerLevelGift(object):
	RES_TABLE = "playerLevelGift"
	__slots__ = ("id","level","type","last","reward1","cost1","chargeId1","reward2","cost2","chargeId2","reward3","cost3","chargeId3",)

    def __init__(self):
		
			# id 玩家等级礼包
			self.id = 0
		
			# level 需求等级
			self.level = 0
		
			# type 面板类型
			self.type = 0
		
			# last 持续时间(秒)
			self.last = 0
		
			# reward1 奖励1
			self.reward1 = []
		
			# cost1 花费1
			self.cost1 = []
		
			# chargeId1 直购关联充值id1
			self.chargeId1 = []
		
			# reward2 奖励2
			self.reward2 = []
		
			# cost2 花费2
			self.cost2 = []
		
			# chargeId2 直购关联充值id2
			self.chargeId2 = []
		
			# reward3 奖励3
			self.reward3 = []
		
			# cost3 花费3
			self.cost3 = []
		
			# chargeId3 直购关联充值id3
			self.chargeId3 = []
		

    def load_from_json(self, data):
		
			# id 玩家等级礼包
			self.id = data.get("id",0)
		
			# level 需求等级
			self.level = data.get("level",0)
		
			# type 面板类型
			self.type = data.get("type",0)
		
			# last 持续时间(秒)
			self.last = data.get("last",0)
		
			# reward1 奖励1
			self.reward1 = data.get("reward1",[])
		
			# cost1 花费1
			self.cost1 = data.get("cost1",[])
		
			# chargeId1 直购关联充值id1
			self.chargeId1 = data.get("chargeId1",[])
		
			# reward2 奖励2
			self.reward2 = data.get("reward2",[])
		
			# cost2 花费2
			self.cost2 = data.get("cost2",[])
		
			# chargeId2 直购关联充值id2
			self.chargeId2 = data.get("chargeId2",[])
		
			# reward3 奖励3
			self.reward3 = data.get("reward3",[])
		
			# cost3 花费3
			self.cost3 = data.get("cost3",[])
		
			# chargeId3 直购关联充值id3
			self.chargeId3 = data.get("chargeId3",[])
		

# chargeHaoli
class ResChargeHaoli(object):
	RES_TABLE = "chargeHaoli"
	__slots__ = ("id","reward","btnName","chargeId","bg",)

    def __init__(self):
		
			# id id
			self.id = 0
		
			# reward 奖励1
			self.reward = []
		
			# btnName 花费1
			self.btnName = ""
		
			# chargeId 直购关联充值id
			self.chargeId = []
		
			# bg 背景图
			self.bg = ""
		

    def load_from_json(self, data):
		
			# id id
			self.id = data.get("id",0)
		
			# reward 奖励1
			self.reward = data.get("reward",[])
		
			# btnName 花费1
			self.btnName = data.get("btnName","")
		
			# chargeId 直购关联充值id
			self.chargeId = data.get("chargeId",[])
		
			# bg 背景图
			self.bg = data.get("bg","")
		

# examAnswerPoint
class ResExamAnswerPoint(object):
	RES_TABLE = "examAnswerPoint"
	__slots__ = ("id","correct","interval","point",)

    def __init__(self):
		
			# id 得分表
			self.id = 0
		
			# correct 正确
			self.correct = 0
		
			# interval 用时
			self.interval = 0
		
			# point 分数
			self.point = 0
		

    def load_from_json(self, data):
		
			# id 得分表
			self.id = data.get("id",0)
		
			# correct 正确
			self.correct = data.get("correct",0)
		
			# interval 用时
			self.interval = data.get("interval",0)
		
			# point 分数
			self.point = data.get("point",0)
		

# examQuestionPool
class ResExamQuestionPool(object):
	RES_TABLE = "examQuestionPool"
	__slots__ = ("id","correct","question","options",)

    def __init__(self):
		
			# id 题库表
			self.id = 0
		
			# correct 正确答案
			self.correct = 0
		
			# question 题目
			self.question = ""
		
			# options 选项
			self.options = []
		

    def load_from_json(self, data):
		
			# id 题库表
			self.id = data.get("id",0)
		
			# correct 正确答案
			self.correct = data.get("correct",0)
		
			# question 题目
			self.question = data.get("question","")
		
			# options 选项
			self.options = data.get("options",[])
		

# examRankReward
class ResExamRankReward(object):
	RES_TABLE = "examRankReward"
	__slots__ = ("id","rank","reward",)

    def __init__(self):
		
			# id 答题奖励表
			self.id = 0
		
			# rank 排名
			self.rank = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 答题奖励表
			self.id = data.get("id",0)
		
			# rank 排名
			self.rank = data.get("rank",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# mapSub
class ResMapSub(object):
	RES_TABLE = "mapSub"
	__slots__ = ("id","lv","mapId","chapter","section","passDesc","passReward","star","mstList","formation","smallReward","mstId","bossBarrId","sceneId","offexp","offcoin","onlineBindDiamond","onlineCoin","offequip","offpet",)

    def __init__(self):
		
			# id 关卡表
			self.id = 0
		
			# lv 等级难度
			self.lv = 0
		
			# mapId 世界地图id
			self.mapId = 0
		
			# chapter 章
			self.chapter = 0
		
			# section 节
			self.section = 0
		
			# passDesc 通关奖励说明
			self.passDesc = ""
		
			# passReward 通关奖励
			self.passReward = []
		
			# star 需要星星数
			self.star = 0
		
			# mstList 小怪列表
			self.mstList = []
		
			# formation 阵型
			self.formation = []
		
			# smallReward 小怪固定奖励
			self.smallReward = []
		
			# mstId boss怪物id
			self.mstId = 0
		
			# bossBarrId boss副本id
			self.bossBarrId = 0
		
			# sceneId 所属场景
			self.sceneId = 0
		
			# offexp 离线经验
			self.offexp = 0
		
			# offcoin 离线金币
			self.offcoin = 0
		
			# onlineBindDiamond 挂机收益绑钻
			self.onlineBindDiamond = 0
		
			# onlineCoin 挂机收益金币
			self.onlineCoin = 0
		
			# offequip 离线装备概率
			self.offequip = []
		
			# offpet 离线宠物碎片概率
			self.offpet = []
		

    def load_from_json(self, data):
		
			# id 关卡表
			self.id = data.get("id",0)
		
			# lv 等级难度
			self.lv = data.get("lv",0)
		
			# mapId 世界地图id
			self.mapId = data.get("mapId",0)
		
			# chapter 章
			self.chapter = data.get("chapter",0)
		
			# section 节
			self.section = data.get("section",0)
		
			# passDesc 通关奖励说明
			self.passDesc = data.get("passDesc","")
		
			# passReward 通关奖励
			self.passReward = data.get("passReward",[])
		
			# star 需要星星数
			self.star = data.get("star",0)
		
			# mstList 小怪列表
			self.mstList = data.get("mstList",[])
		
			# formation 阵型
			self.formation = data.get("formation",[])
		
			# smallReward 小怪固定奖励
			self.smallReward = data.get("smallReward",[])
		
			# mstId boss怪物id
			self.mstId = data.get("mstId",0)
		
			# bossBarrId boss副本id
			self.bossBarrId = data.get("bossBarrId",0)
		
			# sceneId 所属场景
			self.sceneId = data.get("sceneId",0)
		
			# offexp 离线经验
			self.offexp = data.get("offexp",0)
		
			# offcoin 离线金币
			self.offcoin = data.get("offcoin",0)
		
			# onlineBindDiamond 挂机收益绑钻
			self.onlineBindDiamond = data.get("onlineBindDiamond",0)
		
			# onlineCoin 挂机收益金币
			self.onlineCoin = data.get("onlineCoin",0)
		
			# offequip 离线装备概率
			self.offequip = data.get("offequip",[])
		
			# offpet 离线宠物碎片概率
			self.offpet = data.get("offpet",[])
		

# item
class ResItem(object):
	RES_TABLE = "item"
	__slots__ = ("id","name","sortValue","type","subType","page","quality","use","useTip","useAuto","donate","iconId","compound","showCompoundNum","rewardId","selectReward","checkPet","roleLvReward","xiedaiReward","arg1","arg2","arg3","timeType","timeArg","leftTopStr","leftBotStr","costTips","chatId",)

    def __init__(self):
		
			# id 道具表
			self.id = 0
		
			# name 
			self.name = ""
		
			# sortValue 排序
			self.sortValue = 0
		
			# type 类型
			self.type = 0
		
			# subType 子类型
			self.subType = 0
		
			# page 分页
			self.page = 0
		
			# quality 品质
			self.quality = 0
		
			# use 能否使用
			self.use = 0
		
			# useTip 使用是否弹使用成功
			self.useTip = 0
		
			# useAuto 是否自动使用
			self.useAuto = 0
		
			# donate 能否帮会捐献
			self.donate = 0
		
			# iconId 显示压标图片
			self.iconId = 0
		
			# compound 物品合成
			self.compound = []
		
			# showCompoundNum 物品合成是否显示10/4
			self.showCompoundNum = 0
		
			# rewardId 奖励id
			self.rewardId = 0
		
			# selectReward 可选奖励
			self.selectReward = []
		
			# checkPet N选一判断宠物
			self.checkPet = 0
		
			# roleLvReward 等级宝箱奖励
			self.roleLvReward = []
		
			# xiedaiReward 携带品宝箱奖励
			self.xiedaiReward = []
		
			# arg1 通用参数1
			self.arg1 = ""
		
			# arg2 通用参数2
			self.arg2 = ""
		
			# arg3 通用参数3
			self.arg3 = ""
		
			# timeType 限时类型
			self.timeType = 0
		
			# timeArg 限时参数
			self.timeArg = ""
		
			# leftTopStr 道具图标左上角文字压标
			self.leftTopStr = ""
		
			# leftBotStr 道具图标左下角文字压标
			self.leftBotStr = ""
		
			# costTips 消耗材料不足提示文字
			self.costTips = ""
		
			# chatId 广播ID
			self.chatId = 0
		

    def load_from_json(self, data):
		
			# id 道具表
			self.id = data.get("id",0)
		
			# name 
			self.name = data.get("name","")
		
			# sortValue 排序
			self.sortValue = data.get("sortValue",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# subType 子类型
			self.subType = data.get("subType",0)
		
			# page 分页
			self.page = data.get("page",0)
		
			# quality 品质
			self.quality = data.get("quality",0)
		
			# use 能否使用
			self.use = data.get("use",0)
		
			# useTip 使用是否弹使用成功
			self.useTip = data.get("useTip",0)
		
			# useAuto 是否自动使用
			self.useAuto = data.get("useAuto",0)
		
			# donate 能否帮会捐献
			self.donate = data.get("donate",0)
		
			# iconId 显示压标图片
			self.iconId = data.get("iconId",0)
		
			# compound 物品合成
			self.compound = data.get("compound",[])
		
			# showCompoundNum 物品合成是否显示10/4
			self.showCompoundNum = data.get("showCompoundNum",0)
		
			# rewardId 奖励id
			self.rewardId = data.get("rewardId",0)
		
			# selectReward 可选奖励
			self.selectReward = data.get("selectReward",[])
		
			# checkPet N选一判断宠物
			self.checkPet = data.get("checkPet",0)
		
			# roleLvReward 等级宝箱奖励
			self.roleLvReward = data.get("roleLvReward",[])
		
			# xiedaiReward 携带品宝箱奖励
			self.xiedaiReward = data.get("xiedaiReward",[])
		
			# arg1 通用参数1
			self.arg1 = data.get("arg1","")
		
			# arg2 通用参数2
			self.arg2 = data.get("arg2","")
		
			# arg3 通用参数3
			self.arg3 = data.get("arg3","")
		
			# timeType 限时类型
			self.timeType = data.get("timeType",0)
		
			# timeArg 限时参数
			self.timeArg = data.get("timeArg","")
		
			# leftTopStr 道具图标左上角文字压标
			self.leftTopStr = data.get("leftTopStr","")
		
			# leftBotStr 道具图标左下角文字压标
			self.leftBotStr = data.get("leftBotStr","")
		
			# costTips 消耗材料不足提示文字
			self.costTips = data.get("costTips","")
		
			# chatId 广播ID
			self.chatId = data.get("chatId",0)
		

# pavilion
class ResPavilion(object):
	RES_TABLE = "pavilion"
	__slots__ = ("id","name","area","areaName","eleType","increase","decrease","unlockTask","attr","firstRewardId","firstRewardShow","rewardId","rewardShow","challengeList","iconImg","lockTitle","beforeDesc","bossFaceId","unlockName","afterDesc","titleName","eleTips","sceneId","sceneList","mapDesc1","mapDesc2","mapDesc3","leavewordWin","leavewordLose","leaderId","emebleId","emeblesort","actYskj","YsManifesto",)

    def __init__(self):
		
			# id 道馆表
			self.id = 0
		
			# name 道馆名称
			self.name = ""
		
			# area 所属地区
			self.area = 0
		
			# areaName 所属地区名称
			self.areaName = ""
		
			# eleType 元素类型
			self.eleType = 0
		
			# increase 属性增益
			self.increase = 0
		
			# decrease 属性减益
			self.decrease = 0
		
			# unlockTask 解锁任务列表
			self.unlockTask = []
		
			# attr 首通属性奖励
			self.attr = []
		
			# firstRewardId 首通奖励id
			self.firstRewardId = 0
		
			# firstRewardShow 首通客户端奖励展示
			self.firstRewardShow = []
		
			# rewardId 扫荡奖励id
			self.rewardId = 0
		
			# rewardShow 扫荡奖励展示
			self.rewardShow = []
		
			# challengeList 挑战副本列表
			self.challengeList = []
		
			# iconImg 道馆图片
			self.iconImg = ""
		
			# lockTitle 解锁前台头
			self.lockTitle = ""
		
			# beforeDesc 解锁前说明
			self.beforeDesc = ""
		
			# bossFaceId 解锁形象怪物表
			self.bossFaceId = 0
		
			# unlockName 解锁人物名字
			self.unlockName = ""
		
			# afterDesc 解锁后说明
			self.afterDesc = ""
		
			# titleName 解锁道馆名字
			self.titleName = ""
		
			# eleTips 属性提示
			self.eleTips = ""
		
			# sceneId 地图场景id
			self.sceneId = 0
		
			# sceneList 坐标
			self.sceneList = []
		
			# mapDesc1 地图小黑版
			self.mapDesc1 = ""
		
			# mapDesc2 地图小黑版
			self.mapDesc2 = ""
		
			# mapDesc3 地图小黑版
			self.mapDesc3 = ""
		
			# leavewordWin 遗言win
			self.leavewordWin = ""
		
			# leavewordLose 遗言lose
			self.leavewordLose = ""
		
			# leaderId 馆主副本id
			self.leaderId = 0
		
			# emebleId 勋章id
			self.emebleId = 0
		
			# emeblesort 勋章排行
			self.emeblesort = 0
		
			# actYskj 激活异兽空间第几层(0或者不填未不激活
			self.actYskj = 0
		
			# YsManifesto 开启异兽空间的垃圾话
			self.YsManifesto = ""
		

    def load_from_json(self, data):
		
			# id 道馆表
			self.id = data.get("id",0)
		
			# name 道馆名称
			self.name = data.get("name","")
		
			# area 所属地区
			self.area = data.get("area",0)
		
			# areaName 所属地区名称
			self.areaName = data.get("areaName","")
		
			# eleType 元素类型
			self.eleType = data.get("eleType",0)
		
			# increase 属性增益
			self.increase = data.get("increase",0)
		
			# decrease 属性减益
			self.decrease = data.get("decrease",0)
		
			# unlockTask 解锁任务列表
			self.unlockTask = data.get("unlockTask",[])
		
			# attr 首通属性奖励
			self.attr = data.get("attr",[])
		
			# firstRewardId 首通奖励id
			self.firstRewardId = data.get("firstRewardId",0)
		
			# firstRewardShow 首通客户端奖励展示
			self.firstRewardShow = data.get("firstRewardShow",[])
		
			# rewardId 扫荡奖励id
			self.rewardId = data.get("rewardId",0)
		
			# rewardShow 扫荡奖励展示
			self.rewardShow = data.get("rewardShow",[])
		
			# challengeList 挑战副本列表
			self.challengeList = data.get("challengeList",[])
		
			# iconImg 道馆图片
			self.iconImg = data.get("iconImg","")
		
			# lockTitle 解锁前台头
			self.lockTitle = data.get("lockTitle","")
		
			# beforeDesc 解锁前说明
			self.beforeDesc = data.get("beforeDesc","")
		
			# bossFaceId 解锁形象怪物表
			self.bossFaceId = data.get("bossFaceId",0)
		
			# unlockName 解锁人物名字
			self.unlockName = data.get("unlockName","")
		
			# afterDesc 解锁后说明
			self.afterDesc = data.get("afterDesc","")
		
			# titleName 解锁道馆名字
			self.titleName = data.get("titleName","")
		
			# eleTips 属性提示
			self.eleTips = data.get("eleTips","")
		
			# sceneId 地图场景id
			self.sceneId = data.get("sceneId",0)
		
			# sceneList 坐标
			self.sceneList = data.get("sceneList",[])
		
			# mapDesc1 地图小黑版
			self.mapDesc1 = data.get("mapDesc1","")
		
			# mapDesc2 地图小黑版
			self.mapDesc2 = data.get("mapDesc2","")
		
			# mapDesc3 地图小黑版
			self.mapDesc3 = data.get("mapDesc3","")
		
			# leavewordWin 遗言win
			self.leavewordWin = data.get("leavewordWin","")
		
			# leavewordLose 遗言lose
			self.leavewordLose = data.get("leavewordLose","")
		
			# leaderId 馆主副本id
			self.leaderId = data.get("leaderId",0)
		
			# emebleId 勋章id
			self.emebleId = data.get("emebleId",0)
		
			# emeblesort 勋章排行
			self.emeblesort = data.get("emeblesort",0)
		
			# actYskj 激活异兽空间第几层(0或者不填未不激活
			self.actYskj = data.get("actYskj",0)
		
			# YsManifesto 开启异兽空间的垃圾话
			self.YsManifesto = data.get("YsManifesto","")
		

# jiujiyishou
class ResJiujiyishou(object):
	RES_TABLE = "jiujiyishou"
	__slots__ = ("id","name","unlock","firstRewardShow","addAttr","challengeList0","challengeList1","challengeList2","challengeList3","challengeList4","challengeList5","challengeList6","iconImg","lockTitle","beforeDesc","bossFaceId","unlockName","afterDesc","titleName","sceneId","sceneList","mapDesc1","mapDesc2","mapDesc3","leaderId","skillIds",)

    def __init__(self):
		
			# id 究极异兽表
			self.id = 0
		
			# name 道馆名称
			self.name = ""
		
			# unlock 解锁道馆id
			self.unlock = 0
		
			# firstRewardShow 客户端奖励展示(脖子说客户端这里是固定的)
			self.firstRewardShow = []
		
			# addAttr 增加属性
			self.addAttr = []
		
			# challengeList0 挑战副本列表星期天
			self.challengeList0 = []
		
			# challengeList1 挑战副本列表星期一
			self.challengeList1 = []
		
			# challengeList2 挑战副本列表星期二
			self.challengeList2 = []
		
			# challengeList3 挑战副本列表星期三
			self.challengeList3 = []
		
			# challengeList4 挑战副本列表星期四
			self.challengeList4 = []
		
			# challengeList5 挑战副本列表星期五
			self.challengeList5 = []
		
			# challengeList6 挑战副本列表星期六
			self.challengeList6 = []
		
			# iconImg 道馆图片
			self.iconImg = ""
		
			# lockTitle 解锁前台头
			self.lockTitle = ""
		
			# beforeDesc 解锁前说明
			self.beforeDesc = ""
		
			# bossFaceId 解锁形象怪物表
			self.bossFaceId = 0
		
			# unlockName 解锁人物名字
			self.unlockName = ""
		
			# afterDesc 解锁后说明
			self.afterDesc = ""
		
			# titleName 解锁道馆名字
			self.titleName = ""
		
			# sceneId 地图场景id
			self.sceneId = 0
		
			# sceneList 坐标
			self.sceneList = []
		
			# mapDesc1 地图小黑版
			self.mapDesc1 = ""
		
			# mapDesc2 地图小黑版
			self.mapDesc2 = ""
		
			# mapDesc3 地图小黑版
			self.mapDesc3 = ""
		
			# leaderId 馆主副本id
			self.leaderId = 0
		
			# skillIds 道馆boss技能ID
			self.skillIds = []
		

    def load_from_json(self, data):
		
			# id 究极异兽表
			self.id = data.get("id",0)
		
			# name 道馆名称
			self.name = data.get("name","")
		
			# unlock 解锁道馆id
			self.unlock = data.get("unlock",0)
		
			# firstRewardShow 客户端奖励展示(脖子说客户端这里是固定的)
			self.firstRewardShow = data.get("firstRewardShow",[])
		
			# addAttr 增加属性
			self.addAttr = data.get("addAttr",[])
		
			# challengeList0 挑战副本列表星期天
			self.challengeList0 = data.get("challengeList0",[])
		
			# challengeList1 挑战副本列表星期一
			self.challengeList1 = data.get("challengeList1",[])
		
			# challengeList2 挑战副本列表星期二
			self.challengeList2 = data.get("challengeList2",[])
		
			# challengeList3 挑战副本列表星期三
			self.challengeList3 = data.get("challengeList3",[])
		
			# challengeList4 挑战副本列表星期四
			self.challengeList4 = data.get("challengeList4",[])
		
			# challengeList5 挑战副本列表星期五
			self.challengeList5 = data.get("challengeList5",[])
		
			# challengeList6 挑战副本列表星期六
			self.challengeList6 = data.get("challengeList6",[])
		
			# iconImg 道馆图片
			self.iconImg = data.get("iconImg","")
		
			# lockTitle 解锁前台头
			self.lockTitle = data.get("lockTitle","")
		
			# beforeDesc 解锁前说明
			self.beforeDesc = data.get("beforeDesc","")
		
			# bossFaceId 解锁形象怪物表
			self.bossFaceId = data.get("bossFaceId",0)
		
			# unlockName 解锁人物名字
			self.unlockName = data.get("unlockName","")
		
			# afterDesc 解锁后说明
			self.afterDesc = data.get("afterDesc","")
		
			# titleName 解锁道馆名字
			self.titleName = data.get("titleName","")
		
			# sceneId 地图场景id
			self.sceneId = data.get("sceneId",0)
		
			# sceneList 坐标
			self.sceneList = data.get("sceneList",[])
		
			# mapDesc1 地图小黑版
			self.mapDesc1 = data.get("mapDesc1","")
		
			# mapDesc2 地图小黑版
			self.mapDesc2 = data.get("mapDesc2","")
		
			# mapDesc3 地图小黑版
			self.mapDesc3 = data.get("mapDesc3","")
		
			# leaderId 馆主副本id
			self.leaderId = data.get("leaderId",0)
		
			# skillIds 道馆boss技能ID
			self.skillIds = data.get("skillIds",[])
		

# jiujiyishouReward
class ResJiujiyishouReward(object):
	RES_TABLE = "jiujiyishouReward"
	__slots__ = ("id","rewardShow",)

    def __init__(self):
		
			# id 究极异兽奖励星期N
			self.id = 0
		
			# rewardShow 客户端(进口奖励)
			self.rewardShow = []
		

    def load_from_json(self, data):
		
			# id 究极异兽奖励星期N
			self.id = data.get("id",0)
		
			# rewardShow 客户端(进口奖励)
			self.rewardShow = data.get("rewardShow",[])
		

# diaoyurank
class ResDiaoyurank(object):
	RES_TABLE = "diaoyurank"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id 钓鱼奖排行励表
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 钓鱼奖排行励表
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# diaoyureward
class ResDiaoyureward(object):
	RES_TABLE = "diaoyureward"
	__slots__ = ("quality","reward","reward2","score","weight","broadcast",)

    def __init__(self):
		
			# quality 钓鱼奖励表
			self.quality = 0
		
			# reward 奖励
			self.reward = []
		
			# reward2 N天后奖励
			self.reward2 = []
		
			# score 积分
			self.score = 0
		
			# weight 权重
			self.weight = 0
		
			# broadcast 广播id
			self.broadcast = 0
		

    def load_from_json(self, data):
		
			# quality 钓鱼奖励表
			self.quality = data.get("quality",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# reward2 N天后奖励
			self.reward2 = data.get("reward2",[])
		
			# score 积分
			self.score = data.get("score",0)
		
			# weight 权重
			self.weight = data.get("weight",0)
		
			# broadcast 广播id
			self.broadcast = data.get("broadcast",0)
		

# encounter
class ResEncounter(object):
	RES_TABLE = "encounter"
	__slots__ = ("id","name","des","tips","passId","maxRound","rewardId","helpRewardId","monster1","monster2","monster3","notice","eleType","increase","decrease",)

    def __init__(self):
		
			# id 遭遇战
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# des 描述
			self.des = ""
		
			# tips 提示
			self.tips = ""
		
			# passId 开放关卡ID
			self.passId = 0
		
			# maxRound 最大回合数
			self.maxRound = 0
		
			# rewardId 奖励id
			self.rewardId = 0
		
			# helpRewardId 协助奖励
			self.helpRewardId = 0
		
			# monster1 怪物1波
			self.monster1 = []
		
			# monster2 怪物2波
			self.monster2 = []
		
			# monster3 怪物3波
			self.monster3 = []
		
			# notice 产生公告的物品(物品id_公告模板)
			self.notice = []
		
			# eleType 五行属性类型
			self.eleType = 0
		
			# increase 属性增益
			self.increase = 0
		
			# decrease 属性减益
			self.decrease = 0
		

    def load_from_json(self, data):
		
			# id 遭遇战
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# des 描述
			self.des = data.get("des","")
		
			# tips 提示
			self.tips = data.get("tips","")
		
			# passId 开放关卡ID
			self.passId = data.get("passId",0)
		
			# maxRound 最大回合数
			self.maxRound = data.get("maxRound",0)
		
			# rewardId 奖励id
			self.rewardId = data.get("rewardId",0)
		
			# helpRewardId 协助奖励
			self.helpRewardId = data.get("helpRewardId",0)
		
			# monster1 怪物1波
			self.monster1 = data.get("monster1",[])
		
			# monster2 怪物2波
			self.monster2 = data.get("monster2",[])
		
			# monster3 怪物3波
			self.monster3 = data.get("monster3",[])
		
			# notice 产生公告的物品(物品id_公告模板)
			self.notice = data.get("notice",[])
		
			# eleType 五行属性类型
			self.eleType = data.get("eleType",0)
		
			# increase 属性增益
			self.increase = data.get("increase",0)
		
			# decrease 属性减益
			self.decrease = data.get("decrease",0)
		

# qhds
class ResQhds(object):
	RES_TABLE = "qhds"
	__slots__ = ("id","level","attr",)

    def __init__(self):
		
			# id 强化大师表
			self.id = 0
		
			# level 等级
			self.level = 0
		
			# attr 加成属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 强化大师表
			self.id = data.get("id",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# attr 加成属性
			self.attr = data.get("attr",[])
		

# qianghua
class ResQianghua(object):
	RES_TABLE = "qianghua"
	__slots__ = ("id","pos","lv","cost","attr",)

    def __init__(self):
		
			# id 强化表
			self.id = 0
		
			# pos 部位
			self.pos = 0
		
			# lv 等级
			self.lv = 0
		
			# cost 消耗道具
			self.cost = []
		
			# attr 当前等级属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 强化表
			self.id = data.get("id",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# lv 等级
			self.lv = data.get("lv",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# attr 当前等级属性
			self.attr = data.get("attr",[])
		

# jlds
class ResJlds(object):
	RES_TABLE = "jlds"
	__slots__ = ("id","level","attr",)

    def __init__(self):
		
			# id 精炼大师表
			self.id = 0
		
			# level 等级
			self.level = 0
		
			# attr 加成属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 精炼大师表
			self.id = data.get("id",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# attr 加成属性
			self.attr = data.get("attr",[])
		

# gem
class ResGem(object):
	RES_TABLE = "gem"
	__slots__ = ("id","pos","lv","cost","attr",)

    def __init__(self):
		
			# id 宝石表
			self.id = 0
		
			# pos 部位
			self.pos = 0
		
			# lv 等级
			self.lv = 0
		
			# cost 消耗道具
			self.cost = []
		
			# attr 当前等级属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 宝石表
			self.id = data.get("id",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# lv 等级
			self.lv = data.get("lv",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# attr 当前等级属性
			self.attr = data.get("attr",[])
		

# gemds
class ResGemds(object):
	RES_TABLE = "gemds"
	__slots__ = ("id","level","attr",)

    def __init__(self):
		
			# id 宝石大师表
			self.id = 0
		
			# level 等级
			self.level = 0
		
			# attr 加成属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 宝石大师表
			self.id = data.get("id",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# attr 加成属性
			self.attr = data.get("attr",[])
		

# dlds
class ResDlds(object):
	RES_TABLE = "dlds"
	__slots__ = ("id","level","attr",)

    def __init__(self):
		
			# id 锻炼大师表
			self.id = 0
		
			# level 等级
			self.level = 0
		
			# attr 加成属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 锻炼大师表
			self.id = data.get("id",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# attr 加成属性
			self.attr = data.get("attr",[])
		

# jinglian
class ResJinglian(object):
	RES_TABLE = "jinglian"
	__slots__ = ("id","pos","lv","cost","attr",)

    def __init__(self):
		
			# id 精炼表
			self.id = 0
		
			# pos 部位
			self.pos = 0
		
			# lv 等级
			self.lv = 0
		
			# cost 消耗道具
			self.cost = []
		
			# attr 当前等级属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 精炼表
			self.id = data.get("id",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# lv 等级
			self.lv = data.get("lv",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# attr 当前等级属性
			self.attr = data.get("attr",[])
		

# duanlian
class ResDuanlian(object):
	RES_TABLE = "duanlian"
	__slots__ = ("id","pos","lv","cost","attr",)

    def __init__(self):
		
			# id 锻炼表
			self.id = 0
		
			# pos 部位
			self.pos = 0
		
			# lv 等级
			self.lv = 0
		
			# cost 消耗道具
			self.cost = []
		
			# attr 当前等级属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 锻炼表
			self.id = data.get("id",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# lv 等级
			self.lv = data.get("lv",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# attr 当前等级属性
			self.attr = data.get("attr",[])
		

# clbf
class ResClbf(object):
	RES_TABLE = "clbf"
	__slots__ = ("id","barrierId","openLv","sweepLv","sweepCost","freeCount","baseSweepCount","name",)

    def __init__(self):
		
			# id 材料副本表
			self.id = 0
		
			# barrierId 副本id
			self.barrierId = []
		
			# openLv 开启等级
			self.openLv = 0
		
			# sweepLv 扫荡等级
			self.sweepLv = 0
		
			# sweepCost 扫荡消耗
			self.sweepCost = []
		
			# freeCount 免费次数
			self.freeCount = 0
		
			# baseSweepCount 基础扫荡次数
			self.baseSweepCount = 0
		
			# name 副本名字
			self.name = ""
		

    def load_from_json(self, data):
		
			# id 材料副本表
			self.id = data.get("id",0)
		
			# barrierId 副本id
			self.barrierId = data.get("barrierId",[])
		
			# openLv 开启等级
			self.openLv = data.get("openLv",0)
		
			# sweepLv 扫荡等级
			self.sweepLv = data.get("sweepLv",0)
		
			# sweepCost 扫荡消耗
			self.sweepCost = data.get("sweepCost",[])
		
			# freeCount 免费次数
			self.freeCount = data.get("freeCount",0)
		
			# baseSweepCount 基础扫荡次数
			self.baseSweepCount = data.get("baseSweepCount",0)
		
			# name 副本名字
			self.name = data.get("name","")
		

# lwbzStarReward
class ResLwbzStarReward(object):
	RES_TABLE = "lwbzStarReward"
	__slots__ = ("id","six","twelve","eighteen",)

    def __init__(self):
		
			# id 龙王宝藏星数奖励表
			self.id = 0
		
			# six 6星奖励
			self.six = []
		
			# twelve 12星奖励
			self.twelve = []
		
			# eighteen 18星奖励
			self.eighteen = []
		

    def load_from_json(self, data):
		
			# id 龙王宝藏星数奖励表
			self.id = data.get("id",0)
		
			# six 6星奖励
			self.six = data.get("six",[])
		
			# twelve 12星奖励
			self.twelve = data.get("twelve",[])
		
			# eighteen 18星奖励
			self.eighteen = data.get("eighteen",[])
		

# xlysBuff
class ResXlysBuff(object):
	RES_TABLE = "xlysBuff"
	__slots__ = ("key","per","cost",)

    def __init__(self):
		
			# key 小雷音寺Buff表勿动
			self.key = ""
		
			# per 增加万分比
			self.per = 0
		
			# cost 第n次购买消耗(最要配置每日能购买多少个cost就要有多少个)
			self.cost = []
		

    def load_from_json(self, data):
		
			# key 小雷音寺Buff表勿动
			self.key = data.get("key","")
		
			# per 增加万分比
			self.per = data.get("per",0)
		
			# cost 第n次购买消耗(最要配置每日能购买多少个cost就要有多少个)
			self.cost = data.get("cost",[])
		

# lwbz
class ResLwbz(object):
	RES_TABLE = "lwbz"
	__slots__ = ("id","type","needTip","baotuNo","baotuId","baotuIdClient","barrierId","star",)

    def __init__(self):
		
			# id 龙王宝藏表
			self.id = 0
		
			# type 难度
			self.type = 0
		
			# needTip 是否需要下一个难度提醒
			self.needTip = 0
		
			# baotuNo 藏宝图序号
			self.baotuNo = 0
		
			# baotuId 藏宝图id
			self.baotuId = 0
		
			# baotuIdClient 藏宝图前端id
			self.baotuIdClient = 0
		
			# barrierId 副本id
			self.barrierId = 0
		
			# star 星数
			self.star = 0
		

    def load_from_json(self, data):
		
			# id 龙王宝藏表
			self.id = data.get("id",0)
		
			# type 难度
			self.type = data.get("type",0)
		
			# needTip 是否需要下一个难度提醒
			self.needTip = data.get("needTip",0)
		
			# baotuNo 藏宝图序号
			self.baotuNo = data.get("baotuNo",0)
		
			# baotuId 藏宝图id
			self.baotuId = data.get("baotuId",0)
		
			# baotuIdClient 藏宝图前端id
			self.baotuIdClient = data.get("baotuIdClient",0)
		
			# barrierId 副本id
			self.barrierId = data.get("barrierId",0)
		
			# star 星数
			self.star = data.get("star",0)
		

# xlys
class ResXlys(object):
	RES_TABLE = "xlys"
	__slots__ = ("id","type","level","levelClient","barrierId","mstId","wuxing",)

    def __init__(self):
		
			# id 小雷音寺表
			self.id = 0
		
			# type 难度
			self.type = 0
		
			# level 关卡
			self.level = 0
		
			# levelClient 关卡
			self.levelClient = 0
		
			# barrierId 副本id
			self.barrierId = 0
		
			# mstId 怪物id
			self.mstId = 0
		
			# wuxing 五行
			self.wuxing = []
		

    def load_from_json(self, data):
		
			# id 小雷音寺表
			self.id = data.get("id",0)
		
			# type 难度
			self.type = data.get("type",0)
		
			# level 关卡
			self.level = data.get("level",0)
		
			# levelClient 关卡
			self.levelClient = data.get("levelClient",0)
		
			# barrierId 副本id
			self.barrierId = data.get("barrierId",0)
		
			# mstId 怪物id
			self.mstId = data.get("mstId",0)
		
			# wuxing 五行
			self.wuxing = data.get("wuxing",[])
		

# ttsl
class ResTtsl(object):
	RES_TABLE = "ttsl"
	__slots__ = ("id","type","lvClient","firstReward","mstId","barrierId","tipItemId",)

    def __init__(self):
		
			# id 天庭试炼表
			self.id = 0
		
			# type 难度
			self.type = 0
		
			# lvClient 前端关卡
			self.lvClient = 0
		
			# firstReward 首通奖励
			self.firstReward = []
		
			# mstId 怪物id
			self.mstId = 0
		
			# barrierId 副本id
			self.barrierId = 0
		
			# tipItemId 提示道具id
			self.tipItemId = 0
		

    def load_from_json(self, data):
		
			# id 天庭试炼表
			self.id = data.get("id",0)
		
			# type 难度
			self.type = data.get("type",0)
		
			# lvClient 前端关卡
			self.lvClient = data.get("lvClient",0)
		
			# firstReward 首通奖励
			self.firstReward = data.get("firstReward",[])
		
			# mstId 怪物id
			self.mstId = data.get("mstId",0)
		
			# barrierId 副本id
			self.barrierId = data.get("barrierId",0)
		
			# tipItemId 提示道具id
			self.tipItemId = data.get("tipItemId",0)
		

# fabaoNormalMake
class ResFabaoNormalMake(object):
	RES_TABLE = "fabaoNormalMake"
	__slots__ = ("id","min","max","odds","quality","back",)

    def __init__(self):
		
			# id 法宝普通锻造表
			self.id = 0
		
			# min 最小次数
			self.min = 0
		
			# max 最大次数
			self.max = 0
		
			# odds 获得概率
			self.odds = []
		
			# quality 获得X品质回退
			self.quality = []
		
			# back 回退到多少次数
			self.back = 0
		

    def load_from_json(self, data):
		
			# id 法宝普通锻造表
			self.id = data.get("id",0)
		
			# min 最小次数
			self.min = data.get("min",0)
		
			# max 最大次数
			self.max = data.get("max",0)
		
			# odds 获得概率
			self.odds = data.get("odds",[])
		
			# quality 获得X品质回退
			self.quality = data.get("quality",[])
		
			# back 回退到多少次数
			self.back = data.get("back",0)
		

# fabaoPerfectMake
class ResFabaoPerfectMake(object):
	RES_TABLE = "fabaoPerfectMake"
	__slots__ = ("id","min","max","odds","quality","back",)

    def __init__(self):
		
			# id 法宝完美锻造表
			self.id = 0
		
			# min 最小次数
			self.min = 0
		
			# max 最大次数
			self.max = 0
		
			# odds 获得概率
			self.odds = []
		
			# quality 获得X品质回退
			self.quality = []
		
			# back 回退到多少次数
			self.back = 0
		

    def load_from_json(self, data):
		
			# id 法宝完美锻造表
			self.id = data.get("id",0)
		
			# min 最小次数
			self.min = data.get("min",0)
		
			# max 最大次数
			self.max = data.get("max",0)
		
			# odds 获得概率
			self.odds = data.get("odds",[])
		
			# quality 获得X品质回退
			self.quality = data.get("quality",[])
		
			# back 回退到多少次数
			self.back = data.get("back",0)
		

# fabaoConstantMake
class ResFabaoConstantMake(object):
	RES_TABLE = "fabaoConstantMake"
	__slots__ = ("id","num","odds","quality","back",)

    def __init__(self):
		
			# id 法宝固定锻造表
			self.id = 0
		
			# num 次数
			self.num = 0
		
			# odds 获得概率
			self.odds = []
		
			# quality 获得X品质回退
			self.quality = []
		
			# back 回退到多少次数
			self.back = 0
		

    def load_from_json(self, data):
		
			# id 法宝固定锻造表
			self.id = data.get("id",0)
		
			# num 次数
			self.num = data.get("num",0)
		
			# odds 获得概率
			self.odds = data.get("odds",[])
		
			# quality 获得X品质回退
			self.quality = data.get("quality",[])
		
			# back 回退到多少次数
			self.back = data.get("back",0)
		

# fabaoUpgrade
class ResFabaoUpgrade(object):
	RES_TABLE = "fabaoUpgrade"
	__slots__ = ("id","pos","lv","cost","addrAdd","skillLv",)

    def __init__(self):
		
			# id 法宝升级表
			self.id = 0
		
			# pos 部位
			self.pos = 0
		
			# lv 等级
			self.lv = 0
		
			# cost 消耗道具
			self.cost = []
		
			# addrAdd 基础属性加成比例（百分比）
			self.addrAdd = 0
		
			# skillLv 技能等级
			self.skillLv = 0
		

    def load_from_json(self, data):
		
			# id 法宝升级表
			self.id = data.get("id",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# lv 等级
			self.lv = data.get("lv",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# addrAdd 基础属性加成比例（百分比）
			self.addrAdd = data.get("addrAdd",0)
		
			# skillLv 技能等级
			self.skillLv = data.get("skillLv",0)
		

# fazhen
class ResFazhen(object):
	RES_TABLE = "fazhen"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","actSkill","jjreward","offX","offY","scale",)

    def __init__(self):
		
			# id 法阵表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# actSkill 激活技能
			self.actSkill = 0
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		

    def load_from_json(self, data):
		
			# id 法阵表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# actSkill 激活技能
			self.actSkill = data.get("actSkill",0)
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		

# fazhenskill
class ResFazhenskill(object):
	RES_TABLE = "fazhenskill"
	__slots__ = ("id","skillId","lv","name","cost","attr","icon",)

    def __init__(self):
		
			# id 法阵技能表
			self.id = 0
		
			# skillId 技能id
			self.skillId = 0
		
			# lv 技能等级
			self.lv = 0
		
			# name 名称
			self.name = ""
		
			# cost 升级消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		
			# icon 图标
			self.icon = ""
		

    def load_from_json(self, data):
		
			# id 法阵技能表
			self.id = data.get("id",0)
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		
			# lv 技能等级
			self.lv = data.get("lv",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# cost 升级消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# icon 图标
			self.icon = data.get("icon","")
		

# redpacket
class ResRedpacket(object):
	RES_TABLE = "redpacket"
	__slots__ = ("time","type","num","able","times",)

    def __init__(self):
		
			# time 系统红包
			self.time = ""
		
			# type 道具类型
			self.type = 0
		
			# num 道具数量
			self.num = 0
		
			# able 可领取人数
			self.able = 0
		
			# times 发放红包个数
			self.times = 0
		

    def load_from_json(self, data):
		
			# time 系统红包
			self.time = data.get("time","")
		
			# type 道具类型
			self.type = data.get("type",0)
		
			# num 道具数量
			self.num = data.get("num",0)
		
			# able 可领取人数
			self.able = data.get("able",0)
		
			# times 发放红包个数
			self.times = data.get("times",0)
		

# worldLvReward
class ResWorldLvReward(object):
	RES_TABLE = "worldLvReward"
	__slots__ = ("id","pos","min","max",)

    def __init__(self):
		
			# id 序号
			self.id = 0
		
			# pos 经验万分比
			self.pos = 0
		
			# min 等级区间最小
			self.min = 0
		
			# max 等级区间最大
			self.max = 0
		

    def load_from_json(self, data):
		
			# id 序号
			self.id = data.get("id",0)
		
			# pos 经验万分比
			self.pos = data.get("pos",0)
		
			# min 等级区间最小
			self.min = data.get("min",0)
		
			# max 等级区间最大
			self.max = data.get("max",0)
		

# signDaily
class ResSignDaily(object):
	RES_TABLE = "signDaily"
	__slots__ = ("day","reward",)

    def __init__(self):
		
			# day 登陆天数
			self.day = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# day 登陆天数
			self.day = data.get("day",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# fuliRewardLogin
class ResFuliRewardLogin(object):
	RES_TABLE = "fuliRewardLogin"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id 循环
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 循环
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# fuliRewardVip
class ResFuliRewardVip(object):
	RES_TABLE = "fuliRewardVip"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id 循环
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 循环
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# fuliRewardCharge
class ResFuliRewardCharge(object):
	RES_TABLE = "fuliRewardCharge"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id 循环
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 循环
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# qiandaojiangli
class ResQiandaojiangli(object):
	RES_TABLE = "qiandaojiangli"
	__slots__ = ("id","reward","vipLv","mul","rewardLeiji",)

    def __init__(self):
		
			# id 签到天数
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# vipLv 额外奖励vip需求
			self.vipLv = 0
		
			# mul vip额外奖励倍数
			self.mul = 0
		
			# rewardLeiji 累计奖励
			self.rewardLeiji = []
		

    def load_from_json(self, data):
		
			# id 签到天数
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# vipLv 额外奖励vip需求
			self.vipLv = data.get("vipLv",0)
		
			# mul vip额外奖励倍数
			self.mul = data.get("mul",0)
		
			# rewardLeiji 累计奖励
			self.rewardLeiji = data.get("rewardLeiji",[])
		

# loginReward
class ResLoginReward(object):
	RES_TABLE = "loginReward"
	__slots__ = ("day","reward","isBuy",)

    def __init__(self):
		
			# day 登陆天数
			self.day = 0
		
			# reward 奖励
			self.reward = []
		
			# isBuy 直购项
			self.isBuy = 0
		

    def load_from_json(self, data):
		
			# day 登陆天数
			self.day = data.get("day",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# isBuy 直购项
			self.isBuy = data.get("isBuy",0)
		

# roleLvReward
class ResRoleLvReward(object):
	RES_TABLE = "roleLvReward"
	__slots__ = ("lv","reward","isBuyId",)

    def __init__(self):
		
			# lv 角色等级
			self.lv = 0
		
			# reward 奖励
			self.reward = []
		
			# isBuyId 直购项
			self.isBuyId = []
		

    def load_from_json(self, data):
		
			# lv 角色等级
			self.lv = data.get("lv",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# isBuyId 直购项
			self.isBuyId = data.get("isBuyId",[])
		

# lingyuangou
class ResLingyuangou(object):
	RES_TABLE = "lingyuangou"
	__slots__ = ("id","reward","cost","opt1","opt2","opt3",)

    def __init__(self):
		
			# id 0元购
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# cost 消耗
			self.cost = []
		
			# opt1 选项1
			self.opt1 = []
		
			# opt2 选项2
			self.opt2 = []
		
			# opt3 选项3
			self.opt3 = []
		

    def load_from_json(self, data):
		
			# id 0元购
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cost 消耗
			self.cost = data.get("cost",[])
		
			# opt1 选项1
			self.opt1 = data.get("opt1",[])
		
			# opt2 选项2
			self.opt2 = data.get("opt2",[])
		
			# opt3 选项3
			self.opt3 = data.get("opt3",[])
		

# everyMonthGift
class ResEveryMonthGift(object):
	RES_TABLE = "everyMonthGift"
	__slots__ = ("id","cycle","page","empty","next","limit","oldCost","cost","reward",)

    def __init__(self):
		
			# id 每月礼包活动
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# page 分页
			self.page = 0
		
			# empty 是否空挡
			self.empty = 0
		
			# next 下一档期
			self.next = 0
		
			# limit 限购次数
			self.limit = 0
		
			# oldCost 原价
			self.oldCost = []
		
			# cost 花费
			self.cost = []
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 每月礼包活动
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# page 分页
			self.page = data.get("page",0)
		
			# empty 是否空挡
			self.empty = data.get("empty",0)
		
			# next 下一档期
			self.next = data.get("next",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# oldCost 原价
			self.oldCost = data.get("oldCost",[])
		
			# cost 花费
			self.cost = data.get("cost",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# everyWeekGift
class ResEveryWeekGift(object):
	RES_TABLE = "everyWeekGift"
	__slots__ = ("id","cycle","page","empty","next","limit","oldCost","cost","reward",)

    def __init__(self):
		
			# id 每周礼包活动
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# page 分页
			self.page = 0
		
			# empty 是否空挡
			self.empty = 0
		
			# next 下一档期
			self.next = 0
		
			# limit 限购次数
			self.limit = 0
		
			# oldCost 原价
			self.oldCost = []
		
			# cost 花费
			self.cost = []
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 每周礼包活动
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# page 分页
			self.page = data.get("page",0)
		
			# empty 是否空挡
			self.empty = data.get("empty",0)
		
			# next 下一档期
			self.next = data.get("next",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# oldCost 原价
			self.oldCost = data.get("oldCost",[])
		
			# cost 花费
			self.cost = data.get("cost",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# xingyunqian
class ResXingyunqian(object):
	RES_TABLE = "xingyunqian"
	__slots__ = ("day","pow",)

    def __init__(self):
		
			# day 幸运签
			self.day = ""
		
			# pow 权重_类型_奖励表id(1小吉2中吉3大吉）
			self.pow = []
		

    def load_from_json(self, data):
		
			# day 幸运签
			self.day = data.get("day","")
		
			# pow 权重_类型_奖励表id(1小吉2中吉3大吉）
			self.pow = data.get("pow",[])
		

# barrier
class ResBarrier(object):
	RES_TABLE = "barrier"
	__slots__ = ("id","lv","vip","num","maxRound","firstReward","rewardId","rewardIdLuck","helpRewardId","monster1","monster2","monster3","notice",)

    def __init__(self):
		
			# id 副本表
			self.id = 0
		
			# lv 进入等级
			self.lv = 0
		
			# vip vip等级限制
			self.vip = 0
		
			# num 每日进入次数
			self.num = 0
		
			# maxRound 最大回合数
			self.maxRound = 0
		
			# firstReward 首通奖励
			self.firstReward = []
		
			# rewardId 奖励id
			self.rewardId = 0
		
			# rewardIdLuck 奖励id幸运状态
			self.rewardIdLuck = 0
		
			# helpRewardId 协助奖励
			self.helpRewardId = 0
		
			# monster1 怪物1波
			self.monster1 = []
		
			# monster2 怪物2波
			self.monster2 = []
		
			# monster3 怪物3波
			self.monster3 = []
		
			# notice 产生公告的物品(物品id_公告模板)
			self.notice = []
		

    def load_from_json(self, data):
		
			# id 副本表
			self.id = data.get("id",0)
		
			# lv 进入等级
			self.lv = data.get("lv",0)
		
			# vip vip等级限制
			self.vip = data.get("vip",0)
		
			# num 每日进入次数
			self.num = data.get("num",0)
		
			# maxRound 最大回合数
			self.maxRound = data.get("maxRound",0)
		
			# firstReward 首通奖励
			self.firstReward = data.get("firstReward",[])
		
			# rewardId 奖励id
			self.rewardId = data.get("rewardId",0)
		
			# rewardIdLuck 奖励id幸运状态
			self.rewardIdLuck = data.get("rewardIdLuck",0)
		
			# helpRewardId 协助奖励
			self.helpRewardId = data.get("helpRewardId",0)
		
			# monster1 怪物1波
			self.monster1 = data.get("monster1",[])
		
			# monster2 怪物2波
			self.monster2 = data.get("monster2",[])
		
			# monster3 怪物3波
			self.monster3 = data.get("monster3",[])
		
			# notice 产生公告的物品(物品id_公告模板)
			self.notice = data.get("notice",[])
		

# openTask
class ResOpenTask(object):
	RES_TABLE = "openTask"
	__slots__ = ("id","taskList","reward","openReward",)

    def __init__(self):
		
			# id 功能开启任务表
			self.id = 0
		
			# taskList 体验任务列表
			self.taskList = []
		
			# reward 奖励
			self.reward = []
		
			# openReward 功能开启手动奖励
			self.openReward = []
		

    def load_from_json(self, data):
		
			# id 功能开启任务表
			self.id = data.get("id",0)
		
			# taskList 体验任务列表
			self.taskList = data.get("taskList",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# openReward 功能开启手动奖励
			self.openReward = data.get("openReward",[])
		

# open
class ResOpen(object):
	RES_TABLE = "open"
	__slots__ = ("id","fa","scale","offX","offY","level","guideId","type","vip","svip","openServiceDay","guildLv","mapLv","taskID","actId","openTaskId","name","tyIcon","tyBg","tyDesc","panel","PanelShow","tabIndex","showStyle","reward","needTipPanel","tipTitle","tipDesc","tipImg","tipIconImg","tipBtn",)

    def __init__(self):
		
			# id 功能开启表
			self.id = 0
		
			# fa 功能预告战力(不用了)
			self.fa = 0
		
			# scale 功能预告形象缩放
			self.scale = 0
		
			# offX 功能预告形象x
			self.offX = 0
		
			# offY 功能预告形象y
			self.offY = 0
		
			# level 开放等级
			self.level = 0
		
			# guideId 功能开启触发引导id
			self.guideId = 0
		
			# type 条件类型
			self.type = 0
		
			# vip vip开启
			self.vip = 0
		
			# svip 至尊卡要求
			self.svip = 0
		
			# openServiceDay 开服天数
			self.openServiceDay = 0
		
			# guildLv 帮会等级
			self.guildLv = 0
		
			# mapLv 关卡
			self.mapLv = 0
		
			# taskID 要过了任务的ID
			self.taskID = 0
		
			# actId 活动id
			self.actId = 0
		
			# openTaskId 开放功能体验任务id
			self.openTaskId = 0
		
			# name 名字
			self.name = ""
		
			# tyIcon 图标
			self.tyIcon = ""
		
			# tyBg 系统体验背景
			self.tyBg = ""
		
			# tyDesc 描述
			self.tyDesc = ""
		
			# panel 面板ID
			self.panel = ""
		
			# PanelShow PanelShow函数名
			self.PanelShow = ""
		
			# tabIndex tab索引
			self.tabIndex = 0
		
			# showStyle 主界面显示样式
			self.showStyle = 0
		
			# reward 奖励
			self.reward = []
		
			# needTipPanel 是否需要弹出开启界面
			self.needTipPanel = 0
		
			# tipTitle 开启界面标题
			self.tipTitle = ""
		
			# tipDesc 开启界面描述
			self.tipDesc = ""
		
			# tipImg 开启界面图片
			self.tipImg = ""
		
			# tipIconImg 飞的图标
			self.tipIconImg = ""
		
			# tipBtn 开启界面飞到的按钮
			self.tipBtn = ""
		

    def load_from_json(self, data):
		
			# id 功能开启表
			self.id = data.get("id",0)
		
			# fa 功能预告战力(不用了)
			self.fa = data.get("fa",0)
		
			# scale 功能预告形象缩放
			self.scale = data.get("scale",0)
		
			# offX 功能预告形象x
			self.offX = data.get("offX",0)
		
			# offY 功能预告形象y
			self.offY = data.get("offY",0)
		
			# level 开放等级
			self.level = data.get("level",0)
		
			# guideId 功能开启触发引导id
			self.guideId = data.get("guideId",0)
		
			# type 条件类型
			self.type = data.get("type",0)
		
			# vip vip开启
			self.vip = data.get("vip",0)
		
			# svip 至尊卡要求
			self.svip = data.get("svip",0)
		
			# openServiceDay 开服天数
			self.openServiceDay = data.get("openServiceDay",0)
		
			# guildLv 帮会等级
			self.guildLv = data.get("guildLv",0)
		
			# mapLv 关卡
			self.mapLv = data.get("mapLv",0)
		
			# taskID 要过了任务的ID
			self.taskID = data.get("taskID",0)
		
			# actId 活动id
			self.actId = data.get("actId",0)
		
			# openTaskId 开放功能体验任务id
			self.openTaskId = data.get("openTaskId",0)
		
			# name 名字
			self.name = data.get("name","")
		
			# tyIcon 图标
			self.tyIcon = data.get("tyIcon","")
		
			# tyBg 系统体验背景
			self.tyBg = data.get("tyBg","")
		
			# tyDesc 描述
			self.tyDesc = data.get("tyDesc","")
		
			# panel 面板ID
			self.panel = data.get("panel","")
		
			# PanelShow PanelShow函数名
			self.PanelShow = data.get("PanelShow","")
		
			# tabIndex tab索引
			self.tabIndex = data.get("tabIndex",0)
		
			# showStyle 主界面显示样式
			self.showStyle = data.get("showStyle",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# needTipPanel 是否需要弹出开启界面
			self.needTipPanel = data.get("needTipPanel",0)
		
			# tipTitle 开启界面标题
			self.tipTitle = data.get("tipTitle","")
		
			# tipDesc 开启界面描述
			self.tipDesc = data.get("tipDesc","")
		
			# tipImg 开启界面图片
			self.tipImg = data.get("tipImg","")
		
			# tipIconImg 飞的图标
			self.tipIconImg = data.get("tipIconImg","")
		
			# tipBtn 开启界面飞到的按钮
			self.tipBtn = data.get("tipBtn","")
		

# gongchengPersonrRank
class ResGongchengPersonrRank(object):
	RES_TABLE = "gongchengPersonrRank"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id 跨服boss排行
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 跨服boss排行
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# gongcheng
class ResGongcheng(object):
	RES_TABLE = "gongcheng"
	__slots__ = ("id","near","ATK_SUCC","DEF_FAIL","ATK_FAIL","DEF_SUCC","holdReward","defLevel","x","y","level","helpId","name","fbIds","npcAndms","occupyCD","atkCD","OpenLv","guildCitySocre","isDeclarewar","BuildImg","lines","showReward","info","gbinfo",)

    def __init__(self):
		
			# id 攻城城市id
			self.id = 0
		
			# near 相邻数组
			self.near = []
		
			# ATK_SUCC 杀1人奖励攻城成功
			self.ATK_SUCC = []
		
			# DEF_FAIL 杀1人奖励防守失败
			self.DEF_FAIL = []
		
			# ATK_FAIL 杀1人奖励攻城失败
			self.ATK_FAIL = []
		
			# DEF_SUCC 杀1人奖励防守成功
			self.DEF_SUCC = []
		
			# holdReward 22点占城奖励
			self.holdReward = []
		
			# defLevel 防御等级
			self.defLevel = 0
		
			# x 中心位置X
			self.x = 0
		
			# y 中心位置Y
			self.y = 0
		
			# level 城市界别
			self.level = 0
		
			# helpId 帮助说明id
			self.helpId = 0
		
			# name 名字
			self.name = ""
		
			# fbIds NPC副本id
			self.fbIds = []
		
			# npcAndms Npc形象
			self.npcAndms = []
		
			# occupyCD 占领保护时间cd(秒)
			self.occupyCD = 0
		
			# atkCD 公鸡保护时间cd(秒)
			self.atkCD = 0
		
			# OpenLv 开放等级(公会等级)
			self.OpenLv = 0
		
			# guildCitySocre 公会占城积分
			self.guildCitySocre = 0
		
			# isDeclarewar 是否要宣战
			self.isDeclarewar = 0
		
			# BuildImg 城市图片
			self.BuildImg = ""
		
			# lines 绿线
			self.lines = []
		
			# showReward 特产奖励
			self.showReward = []
		
			# info 城市介绍
			self.info = ""
		
			# gbinfo 占城广播
			self.gbinfo = ""
		

    def load_from_json(self, data):
		
			# id 攻城城市id
			self.id = data.get("id",0)
		
			# near 相邻数组
			self.near = data.get("near",[])
		
			# ATK_SUCC 杀1人奖励攻城成功
			self.ATK_SUCC = data.get("ATK_SUCC",[])
		
			# DEF_FAIL 杀1人奖励防守失败
			self.DEF_FAIL = data.get("DEF_FAIL",[])
		
			# ATK_FAIL 杀1人奖励攻城失败
			self.ATK_FAIL = data.get("ATK_FAIL",[])
		
			# DEF_SUCC 杀1人奖励防守成功
			self.DEF_SUCC = data.get("DEF_SUCC",[])
		
			# holdReward 22点占城奖励
			self.holdReward = data.get("holdReward",[])
		
			# defLevel 防御等级
			self.defLevel = data.get("defLevel",0)
		
			# x 中心位置X
			self.x = data.get("x",0)
		
			# y 中心位置Y
			self.y = data.get("y",0)
		
			# level 城市界别
			self.level = data.get("level",0)
		
			# helpId 帮助说明id
			self.helpId = data.get("helpId",0)
		
			# name 名字
			self.name = data.get("name","")
		
			# fbIds NPC副本id
			self.fbIds = data.get("fbIds",[])
		
			# npcAndms Npc形象
			self.npcAndms = data.get("npcAndms",[])
		
			# occupyCD 占领保护时间cd(秒)
			self.occupyCD = data.get("occupyCD",0)
		
			# atkCD 公鸡保护时间cd(秒)
			self.atkCD = data.get("atkCD",0)
		
			# OpenLv 开放等级(公会等级)
			self.OpenLv = data.get("OpenLv",0)
		
			# guildCitySocre 公会占城积分
			self.guildCitySocre = data.get("guildCitySocre",0)
		
			# isDeclarewar 是否要宣战
			self.isDeclarewar = data.get("isDeclarewar",0)
		
			# BuildImg 城市图片
			self.BuildImg = data.get("BuildImg","")
		
			# lines 绿线
			self.lines = data.get("lines",[])
		
			# showReward 特产奖励
			self.showReward = data.get("showReward",[])
		
			# info 城市介绍
			self.info = data.get("info","")
		
			# gbinfo 占城广播
			self.gbinfo = data.get("gbinfo","")
		

# thanksgivingDayTask
class ResThanksgivingDayTask(object):
	RES_TABLE = "thanksgivingDayTask"
	__slots__ = ("id","pageOpen","taskOpen","taskEnd","taskList",)

    def __init__(self):
		
			# id 感恩节任务页签
			self.id = 0
		
			# pageOpen 页签开启时间
			self.pageOpen = ""
		
			# taskOpen 任务开始时间
			self.taskOpen = ""
		
			# taskEnd 任务结束时间
			self.taskEnd = ""
		
			# taskList 任务列表
			self.taskList = []
		

    def load_from_json(self, data):
		
			# id 感恩节任务页签
			self.id = data.get("id",0)
		
			# pageOpen 页签开启时间
			self.pageOpen = data.get("pageOpen","")
		
			# taskOpen 任务开始时间
			self.taskOpen = data.get("taskOpen","")
		
			# taskEnd 任务结束时间
			self.taskEnd = data.get("taskEnd","")
		
			# taskList 任务列表
			self.taskList = data.get("taskList",[])
		

# thanksgivingDayLoginReward
class ResThanksgivingDayLoginReward(object):
	RES_TABLE = "thanksgivingDayLoginReward"
	__slots__ = ("day","reward",)

    def __init__(self):
		
			# day 感恩节登陆天数
			self.day = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# day 感恩节登陆天数
			self.day = data.get("day",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# thanksgivingDayLimitReward
class ResThanksgivingDayLimitReward(object):
	RES_TABLE = "thanksgivingDayLimitReward"
	__slots__ = ("id","titleIcon","giftIcon","reward","limit","costOld","cost","chargeOld","chargeId",)

    def __init__(self):
		
			# id 感恩节限购礼包
			self.id = 0
		
			# titleIcon 名称图标
			self.titleIcon = ""
		
			# giftIcon 礼包图标
			self.giftIcon = ""
		
			# reward 奖励
			self.reward = []
		
			# limit 限购次数
			self.limit = 0
		
			# costOld 原价1
			self.costOld = 0
		
			# cost 花费
			self.cost = []
		
			# chargeOld 原价2
			self.chargeOld = 0
		
			# chargeId 直购关联充值id
			self.chargeId = []
		

    def load_from_json(self, data):
		
			# id 感恩节限购礼包
			self.id = data.get("id",0)
		
			# titleIcon 名称图标
			self.titleIcon = data.get("titleIcon","")
		
			# giftIcon 礼包图标
			self.giftIcon = data.get("giftIcon","")
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# costOld 原价1
			self.costOld = data.get("costOld",0)
		
			# cost 花费
			self.cost = data.get("cost",[])
		
			# chargeOld 原价2
			self.chargeOld = data.get("chargeOld",0)
		
			# chargeId 直购关联充值id
			self.chargeId = data.get("chargeId",[])
		

# thanksgivingDayShop
class ResThanksgivingDayShop(object):
	RES_TABLE = "thanksgivingDayShop"
	__slots__ = ("id","limit","cost","reward",)

    def __init__(self):
		
			# id 感恩节商店
			self.id = 0
		
			# limit 限购次数
			self.limit = 0
		
			# cost 花费
			self.cost = []
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 感恩节商店
			self.id = data.get("id",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# cost 花费
			self.cost = data.get("cost",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# gongchengGangRank
class ResGongchengGangRank(object):
	RES_TABLE = "gongchengGangRank"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id 跨服boss排行
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 跨服boss排行
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# monster
class ResMonster(object):
	RES_TABLE = "monster"
	__slots__ = ("id","name","type","quality","level","attr","eleType","eleVal","skillId","hasPassiveSkill","passiveSkills","dialog","dialogTime","scale",)

    def __init__(self):
		
			# id 怪物表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# type 类型
			self.type = 0
		
			# quality 品质
			self.quality = 0
		
			# level 等级
			self.level = 0
		
			# attr 属性
			self.attr = []
		
			# eleType 五行属性类型
			self.eleType = 0
		
			# eleVal 五行属性值
			self.eleVal = 0
		
			# skillId 技能
			self.skillId = 0
		
			# hasPassiveSkill 是否拥有被动技能
			self.hasPassiveSkill = 0
		
			# passiveSkills 额外被动技能列表
			self.passiveSkills = []
		
			# dialog 战斗独白
			self.dialog = ""
		
			# dialogTime 战斗独白时间秒
			self.dialogTime = 0
		
			# scale 缩放
			self.scale = 0
		

    def load_from_json(self, data):
		
			# id 怪物表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# type 类型
			self.type = data.get("type",0)
		
			# quality 品质
			self.quality = data.get("quality",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# eleType 五行属性类型
			self.eleType = data.get("eleType",0)
		
			# eleVal 五行属性值
			self.eleVal = data.get("eleVal",0)
		
			# skillId 技能
			self.skillId = data.get("skillId",0)
		
			# hasPassiveSkill 是否拥有被动技能
			self.hasPassiveSkill = data.get("hasPassiveSkill",0)
		
			# passiveSkills 额外被动技能列表
			self.passiveSkills = data.get("passiveSkills",[])
		
			# dialog 战斗独白
			self.dialog = data.get("dialog","")
		
			# dialogTime 战斗独白时间秒
			self.dialogTime = data.get("dialogTime",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		

# gongchengActive
class ResGongchengActive(object):
	RES_TABLE = "gongchengActive"
	__slots__ = ("id","openDay","lastDay","lastDayRank","reward1","reward2",)

    def __init__(self):
		
			# id 攻城期号表
			self.id = 0
		
			# openDay 开服第X天开启
			self.openDay = 0
		
			# lastDay 持续天数
			self.lastDay = 0
		
			# lastDayRank 持续天数（排行榜）
			self.lastDayRank = 0
		
			# reward1 第一名奖励
			self.reward1 = []
		
			# reward2 其他名奖励
			self.reward2 = []
		

    def load_from_json(self, data):
		
			# id 攻城期号表
			self.id = data.get("id",0)
		
			# openDay 开服第X天开启
			self.openDay = data.get("openDay",0)
		
			# lastDay 持续天数
			self.lastDay = data.get("lastDay",0)
		
			# lastDayRank 持续天数（排行榜）
			self.lastDayRank = data.get("lastDayRank",0)
		
			# reward1 第一名奖励
			self.reward1 = data.get("reward1",[])
		
			# reward2 其他名奖励
			self.reward2 = data.get("reward2",[])
		

# gongchengLimitReward
class ResGongchengLimitReward(object):
	RES_TABLE = "gongchengLimitReward"
	__slots__ = ("id","cycle","titleIcon","giftIcon","reward","limit","costOld","cost","chargeOld","chargeId",)

    def __init__(self):
		
			# id 攻城限購禮包
			self.id = 0
		
			# cycle 周期
			self.cycle = 0
		
			# titleIcon 名稱圖標
			self.titleIcon = ""
		
			# giftIcon 禮包圖標
			self.giftIcon = ""
		
			# reward 獎勵
			self.reward = []
		
			# limit 限購次數
			self.limit = 0
		
			# costOld 原價1
			self.costOld = 0
		
			# cost 花費
			self.cost = []
		
			# chargeOld 原價2
			self.chargeOld = 0
		
			# chargeId 直購關聯充值id
			self.chargeId = []
		

    def load_from_json(self, data):
		
			# id 攻城限購禮包
			self.id = data.get("id",0)
		
			# cycle 周期
			self.cycle = data.get("cycle",0)
		
			# titleIcon 名稱圖標
			self.titleIcon = data.get("titleIcon","")
		
			# giftIcon 禮包圖標
			self.giftIcon = data.get("giftIcon","")
		
			# reward 獎勵
			self.reward = data.get("reward",[])
		
			# limit 限購次數
			self.limit = data.get("limit",0)
		
			# costOld 原價1
			self.costOld = data.get("costOld",0)
		
			# cost 花費
			self.cost = data.get("cost",[])
		
			# chargeOld 原價2
			self.chargeOld = data.get("chargeOld",0)
		
			# chargeId 直購關聯充值id
			self.chargeId = data.get("chargeId",[])
		

# gongchengTask
class ResGongchengTask(object):
	RES_TABLE = "gongchengTask"
	__slots__ = ("id","cycle","pageOpen","taskOpen","taskEnd","taskList",)

    def __init__(self):
		
			# id 攻城任务页签
			self.id = 0
		
			# cycle 周期
			self.cycle = 0
		
			# pageOpen 页签开启时间(开服第x天)
			self.pageOpen = 0
		
			# taskOpen 任务开始时间(开服第x天)
			self.taskOpen = 0
		
			# taskEnd 任务结束时间(开服第x天)
			self.taskEnd = 0
		
			# taskList 任务列表
			self.taskList = []
		

    def load_from_json(self, data):
		
			# id 攻城任务页签
			self.id = data.get("id",0)
		
			# cycle 周期
			self.cycle = data.get("cycle",0)
		
			# pageOpen 页签开启时间(开服第x天)
			self.pageOpen = data.get("pageOpen",0)
		
			# taskOpen 任务开始时间(开服第x天)
			self.taskOpen = data.get("taskOpen",0)
		
			# taskEnd 任务结束时间(开服第x天)
			self.taskEnd = data.get("taskEnd",0)
		
			# taskList 任务列表
			self.taskList = data.get("taskList",[])
		

# gongchengLoginReward
class ResGongchengLoginReward(object):
	RES_TABLE = "gongchengLoginReward"
	__slots__ = ("id","cycle","day","reward",)

    def __init__(self):
		
			# id key
			self.id = 0
		
			# cycle 周期
			self.cycle = 0
		
			# day 攻城登陆天数
			self.day = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id key
			self.id = data.get("id",0)
		
			# cycle 周期
			self.cycle = data.get("cycle",0)
		
			# day 攻城登陆天数
			self.day = data.get("day",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# gongchengShop
class ResGongchengShop(object):
	RES_TABLE = "gongchengShop"
	__slots__ = ("id","limit","cost","reward","cycle",)

    def __init__(self):
		
			# id 攻城商店
			self.id = 0
		
			# limit 限购次数
			self.limit = 0
		
			# cost 花费
			self.cost = []
		
			# reward 奖励
			self.reward = []
		
			# cycle 周期
			self.cycle = 0
		

    def load_from_json(self, data):
		
			# id 攻城商店
			self.id = data.get("id",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# cost 花费
			self.cost = data.get("cost",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cycle 周期
			self.cycle = data.get("cycle",0)
		

# hualidasaiType
class ResHualidasaiType(object):
	RES_TABLE = "hualidasaiType"
	__slots__ = ("id","per","limit","AttrName","AttrNameMail","AttrNameByPet",)

    def __init__(self):
		
			# id 华丽大赛-任务级别
			self.id = 0
		
			# per 权重
			self.per = 0
		
			# limit 上限
			self.limit = 0
		
			# AttrName 属性名字
			self.AttrName = ""
		
			# AttrNameMail 邮件属性名字
			self.AttrNameMail = ""
		
			# AttrNameByPet 属性名字(报名宠物显示用)
			self.AttrNameByPet = ""
		

    def load_from_json(self, data):
		
			# id 华丽大赛-任务级别
			self.id = data.get("id",0)
		
			# per 权重
			self.per = data.get("per",0)
		
			# limit 上限
			self.limit = data.get("limit",0)
		
			# AttrName 属性名字
			self.AttrName = data.get("AttrName","")
		
			# AttrNameMail 邮件属性名字
			self.AttrNameMail = data.get("AttrNameMail","")
		
			# AttrNameByPet 属性名字(报名宠物显示用)
			self.AttrNameByPet = data.get("AttrNameByPet","")
		

# hualidasaiReward
class ResHualidasaiReward(object):
	RES_TABLE = "hualidasaiReward"
	__slots__ = ("id","reward1","reward2","reward3",)

    def __init__(self):
		
			# id 排行奖励
			self.id = 0
		
			# reward1 奖励-低
			self.reward1 = []
		
			# reward2 奖励-中
			self.reward2 = []
		
			# reward3 奖励-搞
			self.reward3 = []
		

    def load_from_json(self, data):
		
			# id 排行奖励
			self.id = data.get("id",0)
		
			# reward1 奖励-低
			self.reward1 = data.get("reward1",[])
		
			# reward2 奖励-中
			self.reward2 = data.get("reward2",[])
		
			# reward3 奖励-搞
			self.reward3 = data.get("reward3",[])
		

# hualidasaiLevel
class ResHualidasaiLevel(object):
	RES_TABLE = "hualidasaiLevel"
	__slots__ = ("id","per","limit","size","cost","sname",)

    def __init__(self):
		
			# id 华丽大赛-任务级别(id请勿乱改)
			self.id = 0
		
			# per 权重
			self.per = 0
		
			# limit 上限
			self.limit = 0
		
			# size 容量
			self.size = 0
		
			# cost 消耗
			self.cost = []
		
			# sname 品质名字邮件
			self.sname = ""
		

    def load_from_json(self, data):
		
			# id 华丽大赛-任务级别(id请勿乱改)
			self.id = data.get("id",0)
		
			# per 权重
			self.per = data.get("per",0)
		
			# limit 上限
			self.limit = data.get("limit",0)
		
			# size 容量
			self.size = data.get("size",0)
		
			# cost 消耗
			self.cost = data.get("cost",[])
		
			# sname 品质名字邮件
			self.sname = data.get("sname","")
		

# hetiMake
class ResHetiMake(object):
	RES_TABLE = "hetiMake"
	__slots__ = ("id","level","ver","match",)

    def __init__(self):
		
			# id 合体宠物规则
			self.id = 0
		
			# level 难度
			self.level = 0
		
			# ver 版本
			self.ver = 0
		
			# match 匹配规则
			self.match = []
		

    def load_from_json(self, data):
		
			# id 合体宠物规则
			self.id = data.get("id",0)
		
			# level 难度
			self.level = data.get("level",0)
		
			# ver 版本
			self.ver = data.get("ver",0)
		
			# match 匹配规则
			self.match = data.get("match",[])
		

# hetiReward
class ResHetiReward(object):
	RES_TABLE = "hetiReward"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id 合体奖励表
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 合体奖励表
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# leichongHefu
class ResLeichongHefu(object):
	RES_TABLE = "leichongHefu"
	__slots__ = ("id","cycle","page","days","empty","next","reward","rmb",)

    def __init__(self):
		
			# id id
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# page 分页
			self.page = 0
		
			# days 活动天数
			self.days = 0
		
			# empty 是否空挡
			self.empty = 0
		
			# next 下一档期
			self.next = 0
		
			# reward 奖励
			self.reward = []
		
			# rmb 人民币需求（分）
			self.rmb = 0
		

    def load_from_json(self, data):
		
			# id id
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# page 分页
			self.page = data.get("page",0)
		
			# days 活动天数
			self.days = data.get("days",0)
		
			# empty 是否空挡
			self.empty = data.get("empty",0)
		
			# next 下一档期
			self.next = data.get("next",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# rmb 人民币需求（分）
			self.rmb = data.get("rmb",0)
		

# loginRewardHefu
class ResLoginRewardHefu(object):
	RES_TABLE = "loginRewardHefu"
	__slots__ = ("day","reward","isBuy",)

    def __init__(self):
		
			# day 登陆天数
			self.day = 0
		
			# reward 奖励
			self.reward = []
		
			# isBuy 直购项
			self.isBuy = 0
		

    def load_from_json(self, data):
		
			# day 登陆天数
			self.day = data.get("day",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# isBuy 直购项
			self.isBuy = data.get("isBuy",0)
		

# chargeRankHefu
class ResChargeRankHefu(object):
	RES_TABLE = "chargeRankHefu"
	__slots__ = ("id","minRank","maxRank","value","reward",)

    def __init__(self):
		
			# id 充值排行
			self.id = 0
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# value 领奖条件值
			self.value = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 充值排行
			self.id = data.get("id",0)
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# value 领奖条件值
			self.value = data.get("value",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# dwsRewardHefu
class ResDwsRewardHefu(object):
	RES_TABLE = "dwsRewardHefu"
	__slots__ = ("id","type","reward","minRank","maxRank","info",)

    def __init__(self):
		
			# id id
			self.id = 0
		
			# type 类型(1青铜2白银3黄金4砖石
			self.type = 0
		
			# reward 奖励
			self.reward = []
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# info 描述
			self.info = ""
		

    def load_from_json(self, data):
		
			# id id
			self.id = data.get("id",0)
		
			# type 类型(1青铜2白银3黄金4砖石
			self.type = data.get("type",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# info 描述
			self.info = data.get("info","")
		

# jjcRankHefu
class ResJjcRankHefu(object):
	RES_TABLE = "jjcRankHefu"
	__slots__ = ("id","minRank","maxRank","reward",)

    def __init__(self):
		
			# id id
			self.id = 0
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id id
			self.id = data.get("id",0)
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# catchPetShopHefu
class ResCatchPetShopHefu(object):
	RES_TABLE = "catchPetShopHefu"
	__slots__ = ("id","titleIcon","giftIcon","reward","limit","limitType","costOld","cost","chargeOld","chargeId",)

    def __init__(self):
		
			# id 限購禮包
			self.id = 0
		
			# titleIcon 名稱圖標
			self.titleIcon = ""
		
			# giftIcon 禮包圖標
			self.giftIcon = ""
		
			# reward 獎勵
			self.reward = []
		
			# limit 限購次數
			self.limit = 0
		
			# limitType 限購类型1为活动期内限购
			self.limitType = 0
		
			# costOld 原價1
			self.costOld = 0
		
			# cost 花費(有花费就不走充值)
			self.cost = []
		
			# chargeOld 原價2
			self.chargeOld = 0
		
			# chargeId 直購關聯充值id(有花费就不走充值)
			self.chargeId = []
		

    def load_from_json(self, data):
		
			# id 限購禮包
			self.id = data.get("id",0)
		
			# titleIcon 名稱圖標
			self.titleIcon = data.get("titleIcon","")
		
			# giftIcon 禮包圖標
			self.giftIcon = data.get("giftIcon","")
		
			# reward 獎勵
			self.reward = data.get("reward",[])
		
			# limit 限購次數
			self.limit = data.get("limit",0)
		
			# limitType 限購类型1为活动期内限购
			self.limitType = data.get("limitType",0)
		
			# costOld 原價1
			self.costOld = data.get("costOld",0)
		
			# cost 花費(有花费就不走充值)
			self.cost = data.get("cost",[])
		
			# chargeOld 原價2
			self.chargeOld = data.get("chargeOld",0)
		
			# chargeId 直購關聯充值id(有花费就不走充值)
			self.chargeId = data.get("chargeId",[])
		

# catchPetRankRewardHefu
class ResCatchPetRankRewardHefu(object):
	RES_TABLE = "catchPetRankRewardHefu"
	__slots__ = ("id","minRank","maxRank","value","reward",)

    def __init__(self):
		
			# id 抓宠排名
			self.id = 0
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# value 领奖条件值
			self.value = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 抓宠排名
			self.id = data.get("id",0)
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# value 领奖条件值
			self.value = data.get("value",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# actRank
class ResActRank(object):
	RES_TABLE = "actRank"
	__slots__ = ("id","actId","type","minRank","maxRank","reward","titleImg","hasGoTo",)

    def __init__(self):
		
			# id xx排行
			self.id = 0
		
			# actId 关联活动id
			self.actId = 0
		
			# type 活动类型
			self.type = 0
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# reward 奖励
			self.reward = []
		
			# titleImg 标语图片
			self.titleImg = ""
		
			# hasGoTo 是否有前往
			self.hasGoTo = 0
		

    def load_from_json(self, data):
		
			# id xx排行
			self.id = data.get("id",0)
		
			# actId 关联活动id
			self.actId = data.get("actId",0)
		
			# type 活动类型
			self.type = data.get("type",0)
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# titleImg 标语图片
			self.titleImg = data.get("titleImg","")
		
			# hasGoTo 是否有前往
			self.hasGoTo = data.get("hasGoTo",0)
		

# mubiaojiangli
class ResMubiaojiangli(object):
	RES_TABLE = "mubiaojiangli"
	__slots__ = ("id","day","type","targer","seq","reward",)

    def __init__(self):
		
			# id 目标奖励
			self.id = 0
		
			# day 天数
			self.day = 0
		
			# type 需求模块
			self.type = 0
		
			# targer 目标
			self.targer = 0
		
			# seq 顺序
			self.seq = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 目标奖励
			self.id = data.get("id",0)
		
			# day 天数
			self.day = data.get("day",0)
		
			# type 需求模块
			self.type = data.get("type",0)
		
			# targer 目标
			self.targer = data.get("targer",0)
		
			# seq 顺序
			self.seq = data.get("seq",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# actNewYearRank
class ResActNewYearRank(object):
	RES_TABLE = "actNewYearRank"
	__slots__ = ("id","rankType","rankName","minRank","maxRank","reward",)

    def __init__(self):
		
			# id 元旦排行
			self.id = 0
		
			# rankType 排行榜类型
			self.rankType = 0
		
			# rankName 排行榜名称(用于邮件)
			self.rankName = ""
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 元旦排行
			self.id = data.get("id",0)
		
			# rankType 排行榜类型
			self.rankType = data.get("rankType",0)
		
			# rankName 排行榜名称(用于邮件)
			self.rankName = data.get("rankName","")
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# costRank
class ResCostRank(object):
	RES_TABLE = "costRank"
	__slots__ = ("id","minRank","maxRank","value","reward",)

    def __init__(self):
		
			# id 消费排行
			self.id = 0
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# value 领奖条件值
			self.value = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 消费排行
			self.id = data.get("id",0)
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# value 领奖条件值
			self.value = data.get("value",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# actNewYearCrossRank
class ResActNewYearCrossRank(object):
	RES_TABLE = "actNewYearCrossRank"
	__slots__ = ("id","rankType","rankName","minRank","maxRank","reward",)

    def __init__(self):
		
			# id 元旦跨服排行
			self.id = 0
		
			# rankType 排行榜类型
			self.rankType = 0
		
			# rankName 排行榜名称(用于邮件)
			self.rankName = ""
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 元旦跨服排行
			self.id = data.get("id",0)
		
			# rankType 排行榜类型
			self.rankType = data.get("rankType",0)
		
			# rankName 排行榜名称(用于邮件)
			self.rankName = data.get("rankName","")
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# actKfkh
class ResActKfkh(object):
	RES_TABLE = "actKfkh"
	__slots__ = ("id","actId","type","minRank","maxRank","value","reward","shopIds","info","links",)

    def __init__(self):
		
			# id 开服狂欢
			self.id = 0
		
			# actId 关联活动id
			self.actId = 0
		
			# type 类型
			self.type = 0
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# value 领奖条件值
			self.value = 0
		
			# reward 奖励
			self.reward = []
		
			# shopIds 限购礼包id列表
			self.shopIds = []
		
			# info 说明文本
			self.info = ""
		
			# links 快速提升途径id
			self.links = []
		

    def load_from_json(self, data):
		
			# id 开服狂欢
			self.id = data.get("id",0)
		
			# actId 关联活动id
			self.actId = data.get("actId",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# value 领奖条件值
			self.value = data.get("value",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# shopIds 限购礼包id列表
			self.shopIds = data.get("shopIds",[])
		
			# info 说明文本
			self.info = data.get("info","")
		
			# links 快速提升途径id
			self.links = data.get("links",[])
		

# actMonster
class ResActMonster(object):
	RES_TABLE = "actMonster"
	__slots__ = ("id","actNo","needFa","actId","type","lv","taskList","icon","showId","fbId","mstId","noticeId","noticeParam","title","tipDescTask","tipDescNormal","tipDesc","lostTip",)

    def __init__(self):
		
			# id xx大侠
			self.id = 0
		
			# actNo 期号
			self.actNo = 0
		
			# needFa 战力需求
			self.needFa = 0
		
			# actId 关联活动id
			self.actId = 0
		
			# type 活动类型
			self.type = 0
		
			# lv 关卡
			self.lv = 0
		
			# taskList 前置任务列表
			self.taskList = []
		
			# icon 关卡图标
			self.icon = ""
		
			# showId 前端展示道具
			self.showId = 0
		
			# fbId 副本id
			self.fbId = 0
		
			# mstId 怪物id
			self.mstId = 0
		
			# noticeId 公告id
			self.noticeId = 0
		
			# noticeParam 公告参数
			self.noticeParam = []
		
			# title 标题
			self.title = ""
		
			# tipDescTask 关卡说明未完成任务时显示
			self.tipDescTask = ""
		
			# tipDescNormal 关卡说明普通
			self.tipDescNormal = ""
		
			# tipDesc 关卡说明失败
			self.tipDesc = ""
		
			# lostTip 失败提示
			self.lostTip = ""
		

    def load_from_json(self, data):
		
			# id xx大侠
			self.id = data.get("id",0)
		
			# actNo 期号
			self.actNo = data.get("actNo",0)
		
			# needFa 战力需求
			self.needFa = data.get("needFa",0)
		
			# actId 关联活动id
			self.actId = data.get("actId",0)
		
			# type 活动类型
			self.type = data.get("type",0)
		
			# lv 关卡
			self.lv = data.get("lv",0)
		
			# taskList 前置任务列表
			self.taskList = data.get("taskList",[])
		
			# icon 关卡图标
			self.icon = data.get("icon","")
		
			# showId 前端展示道具
			self.showId = data.get("showId",0)
		
			# fbId 副本id
			self.fbId = data.get("fbId",0)
		
			# mstId 怪物id
			self.mstId = data.get("mstId",0)
		
			# noticeId 公告id
			self.noticeId = data.get("noticeId",0)
		
			# noticeParam 公告参数
			self.noticeParam = data.get("noticeParam",[])
		
			# title 标题
			self.title = data.get("title","")
		
			# tipDescTask 关卡说明未完成任务时显示
			self.tipDescTask = data.get("tipDescTask","")
		
			# tipDescNormal 关卡说明普通
			self.tipDescNormal = data.get("tipDescNormal","")
		
			# tipDesc 关卡说明失败
			self.tipDesc = data.get("tipDesc","")
		
			# lostTip 失败提示
			self.lostTip = data.get("lostTip","")
		

# actCrossRank
class ResActCrossRank(object):
	RES_TABLE = "actCrossRank"
	__slots__ = ("id","sortId","delayTime","actTime",)

    def __init__(self):
		
			# id 跨服排行奖励
			self.id = 0
		
			# sortId 排序
			self.sortId = 0
		
			# delayTime 活动开启延迟天数
			self.delayTime = 0
		
			# actTime 持续天数
			self.actTime = 0
		

    def load_from_json(self, data):
		
			# id 跨服排行奖励
			self.id = data.get("id",0)
		
			# sortId 排序
			self.sortId = data.get("sortId",0)
		
			# delayTime 活动开启延迟天数
			self.delayTime = data.get("delayTime",0)
		
			# actTime 持续天数
			self.actTime = data.get("actTime",0)
		

# actMonsterRank
class ResActMonsterRank(object):
	RES_TABLE = "actMonsterRank"
	__slots__ = ("id","daxiaId","rank","reward",)

    def __init__(self):
		
			# id xx大侠排行
			self.id = 0
		
			# daxiaId 关卡id
			self.daxiaId = 0
		
			# rank 排名
			self.rank = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id xx大侠排行
			self.id = data.get("id",0)
		
			# daxiaId 关卡id
			self.daxiaId = data.get("daxiaId",0)
		
			# rank 排名
			self.rank = data.get("rank",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# activity
class ResActivity(object):
	RES_TABLE = "activity"
	__slots__ = ("id","name","type","group","sort","openDayRange","mergeDayRange","everyday","everyweek","dateRange","level","icon","icon2","prepare","aheadTime","timeInfoStr","CycleNo","param",)

    def __init__(self):
		
			# id 活动表
			self.id = 0
		
			# name 活动名称
			self.name = ""
		
			# type 类型
			self.type = 0
		
			# group 分组
			self.group = 0
		
			# sort 排序
			self.sort = 0
		
			# openDayRange 开服天数时间段（大优先级）
			self.openDayRange = []
		
			# mergeDayRange 合服天数时间段（大优先级）
			self.mergeDayRange = []
		
			# everyday 每日活动（小优先级）
			self.everyday = []
		
			# everyweek 每周活动（小优先级）
			self.everyweek = []
		
			# dateRange 固定日期（小优先级）
			self.dateRange = []
		
			# level 等级需求
			self.level = 0
		
			# icon 按钮图标
			self.icon = ""
		
			# icon2 按钮图标2
			self.icon2 = ""
		
			# prepare 活动准备时间
			self.prepare = 0
		
			# aheadTime 提前x秒事件
			self.aheadTime = 0
		
			# timeInfoStr 时间说明文本
			self.timeInfoStr = ""
		
			# CycleNo 活动期号
			self.CycleNo = 0
		
			# param 传参
			self.param = ""
		

    def load_from_json(self, data):
		
			# id 活动表
			self.id = data.get("id",0)
		
			# name 活动名称
			self.name = data.get("name","")
		
			# type 类型
			self.type = data.get("type",0)
		
			# group 分组
			self.group = data.get("group",0)
		
			# sort 排序
			self.sort = data.get("sort",0)
		
			# openDayRange 开服天数时间段（大优先级）
			self.openDayRange = data.get("openDayRange",[])
		
			# mergeDayRange 合服天数时间段（大优先级）
			self.mergeDayRange = data.get("mergeDayRange",[])
		
			# everyday 每日活动（小优先级）
			self.everyday = data.get("everyday",[])
		
			# everyweek 每周活动（小优先级）
			self.everyweek = data.get("everyweek",[])
		
			# dateRange 固定日期（小优先级）
			self.dateRange = data.get("dateRange",[])
		
			# level 等级需求
			self.level = data.get("level",0)
		
			# icon 按钮图标
			self.icon = data.get("icon","")
		
			# icon2 按钮图标2
			self.icon2 = data.get("icon2","")
		
			# prepare 活动准备时间
			self.prepare = data.get("prepare",0)
		
			# aheadTime 提前x秒事件
			self.aheadTime = data.get("aheadTime",0)
		
			# timeInfoStr 时间说明文本
			self.timeInfoStr = data.get("timeInfoStr","")
		
			# CycleNo 活动期号
			self.CycleNo = data.get("CycleNo",0)
		
			# param 传参
			self.param = data.get("param","")
		

# chargeRank
class ResChargeRank(object):
	RES_TABLE = "chargeRank"
	__slots__ = ("id","minRank","maxRank","value","reward",)

    def __init__(self):
		
			# id 充值排行
			self.id = 0
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# value 领奖条件值
			self.value = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 充值排行
			self.id = data.get("id",0)
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# value 领奖条件值
			self.value = data.get("value",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# actCrossRankReward
class ResActCrossRankReward(object):
	RES_TABLE = "actCrossRankReward"
	__slots__ = ("id","type","minRank","maxRank","value","reward","shopIds","info","suggest","links",)

    def __init__(self):
		
			# id 跨服排行奖励
			self.id = 0
		
			# type 类型
			self.type = 0
		
			# minRank 最小排名
			self.minRank = 0
		
			# maxRank 最大排名
			self.maxRank = 0
		
			# value 领奖条件值
			self.value = 0
		
			# reward 奖励
			self.reward = []
		
			# shopIds 限购礼包id列表
			self.shopIds = []
		
			# info 说明文本
			self.info = ""
		
			# suggest tips建议
			self.suggest = ""
		
			# links 快速提升途径id
			self.links = []
		

    def load_from_json(self, data):
		
			# id 跨服排行奖励
			self.id = data.get("id",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# minRank 最小排名
			self.minRank = data.get("minRank",0)
		
			# maxRank 最大排名
			self.maxRank = data.get("maxRank",0)
		
			# value 领奖条件值
			self.value = data.get("value",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# shopIds 限购礼包id列表
			self.shopIds = data.get("shopIds",[])
		
			# info 说明文本
			self.info = data.get("info","")
		
			# suggest tips建议
			self.suggest = data.get("suggest","")
		
			# links 快速提升途径id
			self.links = data.get("links",[])
		

# qianggouGift1
class ResQianggouGift1(object):
	RES_TABLE = "qianggouGift1"
	__slots__ = ("id","type","name","qutily","limit","oldCost","cost","chargeId","reward","desc",)

    def __init__(self):
		
			# id 抢购礼包1
			self.id = 0
		
			# type 类型
			self.type = 0
		
			# name 名称
			self.name = ""
		
			# qutily 品质
			self.qutily = 0
		
			# limit 限购次数
			self.limit = 0
		
			# oldCost 原价显示
			self.oldCost = ""
		
			# cost 花费
			self.cost = []
		
			# chargeId 直购关联充值id
			self.chargeId = []
		
			# reward 奖励
			self.reward = []
		
			# desc 描述
			self.desc = ""
		

    def load_from_json(self, data):
		
			# id 抢购礼包1
			self.id = data.get("id",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# qutily 品质
			self.qutily = data.get("qutily",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# oldCost 原价显示
			self.oldCost = data.get("oldCost","")
		
			# cost 花费
			self.cost = data.get("cost",[])
		
			# chargeId 直购关联充值id
			self.chargeId = data.get("chargeId",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# desc 描述
			self.desc = data.get("desc","")
		

# qmjj
class ResQmjj(object):
	RES_TABLE = "qmjj"
	__slots__ = ("id","day","type","targer","seq","reward","num",)

    def __init__(self):
		
			# id 目标奖励
			self.id = 0
		
			# day 天数
			self.day = 0
		
			# type 需求模块
			self.type = 0
		
			# targer 目标
			self.targer = 0
		
			# seq 顺序
			self.seq = 0
		
			# reward 奖励
			self.reward = []
		
			# num 要求达到人数
			self.num = 0
		

    def load_from_json(self, data):
		
			# id 目标奖励
			self.id = data.get("id",0)
		
			# day 天数
			self.day = data.get("day",0)
		
			# type 需求模块
			self.type = data.get("type",0)
		
			# targer 目标
			self.targer = data.get("targer",0)
		
			# seq 顺序
			self.seq = data.get("seq",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# num 要求达到人数
			self.num = data.get("num",0)
		

# tuangou
class ResTuangou(object):
	RES_TABLE = "tuangou"
	__slots__ = ("id","seq","reward","num","rmb",)

    def __init__(self):
		
			# id 目标奖励
			self.id = 0
		
			# seq 顺序
			self.seq = 0
		
			# reward 奖励
			self.reward = []
		
			# num 要求达到人数
			self.num = 0
		
			# rmb 充值条件rmb分
			self.rmb = 0
		

    def load_from_json(self, data):
		
			# id 目标奖励
			self.id = data.get("id",0)
		
			# seq 顺序
			self.seq = data.get("seq",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# num 要求达到人数
			self.num = data.get("num",0)
		
			# rmb 充值条件rmb分
			self.rmb = data.get("rmb",0)
		

# qianggouGift2
class ResQianggouGift2(object):
	RES_TABLE = "qianggouGift2"
	__slots__ = ("id","type","name","qutily","limit","oldCost","cost","chargeId","reward","desc",)

    def __init__(self):
		
			# id 抢购礼包2
			self.id = 0
		
			# type 类型
			self.type = 0
		
			# name 名称
			self.name = ""
		
			# qutily 品质
			self.qutily = 0
		
			# limit 限购次数
			self.limit = 0
		
			# oldCost 原价显示
			self.oldCost = ""
		
			# cost 花费
			self.cost = []
		
			# chargeId 直购关联充值id
			self.chargeId = []
		
			# reward 奖励
			self.reward = []
		
			# desc 描述
			self.desc = ""
		

    def load_from_json(self, data):
		
			# id 抢购礼包2
			self.id = data.get("id",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# qutily 品质
			self.qutily = data.get("qutily",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# oldCost 原价显示
			self.oldCost = data.get("oldCost","")
		
			# cost 花费
			self.cost = data.get("cost",[])
		
			# chargeId 直购关联充值id
			self.chargeId = data.get("chargeId",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# desc 描述
			self.desc = data.get("desc","")
		

# qmcj
class ResQmcj(object):
	RES_TABLE = "qmcj"
	__slots__ = ("id","lv","reward",)

    def __init__(self):
		
			# id 全民冲级
			self.id = 0
		
			# lv 等级需求
			self.lv = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 全民冲级
			self.id = data.get("id",0)
		
			# lv 等级需求
			self.lv = data.get("lv",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# actShop
class ResActShop(object):
	RES_TABLE = "actShop"
	__slots__ = ("id","actId","type","shopType",)

    def __init__(self):
		
			# id xx商店
			self.id = 0
		
			# actId 关联活动id
			self.actId = 0
		
			# type 活动类型
			self.type = 0
		
			# shopType 商店标签
			self.shopType = 0
		

    def load_from_json(self, data):
		
			# id xx商店
			self.id = data.get("id",0)
		
			# actId 关联活动id
			self.actId = data.get("actId",0)
		
			# type 活动类型
			self.type = data.get("type",0)
		
			# shopType 商店标签
			self.shopType = data.get("shopType",0)
		

# actJinJie
class ResActJinJie(object):
	RES_TABLE = "actJinJie"
	__slots__ = ("id","actId","type","lv","reward","titleImg",)

    def __init__(self):
		
			# id xx进阶
			self.id = 0
		
			# actId 关联活动id
			self.actId = 0
		
			# type 类型
			self.type = 0
		
			# lv 系统等阶
			self.lv = 0
		
			# reward 奖励
			self.reward = []
		
			# titleImg 标语图片
			self.titleImg = ""
		

    def load_from_json(self, data):
		
			# id xx进阶
			self.id = data.get("id",0)
		
			# actId 关联活动id
			self.actId = data.get("actId",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# lv 系统等阶
			self.lv = data.get("lv",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# titleImg 标语图片
			self.titleImg = data.get("titleImg","")
		

# actChargeStarPool
class ResActChargeStarPool(object):
	RES_TABLE = "actChargeStarPool"
	__slots__ = ("id","sortID","reward","good","rate","limit1","limit2","limit3",)

    def __init__(self):
		
			# id 星盘奖池表
			self.id = 0
		
			# sortID 排序
			self.sortID = 0
		
			# reward 奖励
			self.reward = []
		
			# good 是否极品
			self.good = 0
		
			# rate 权重
			self.rate = 0
		
			# limit1 消费N个占星石后，加入奖池
			self.limit1 = 0
		
			# limit2 拥有后是否可再次抽取(特指宠物相关联的道具）
			self.limit2 = 0
		
			# limit3 在本期内能抽到几次
			self.limit3 = 0
		

    def load_from_json(self, data):
		
			# id 星盘奖池表
			self.id = data.get("id",0)
		
			# sortID 排序
			self.sortID = data.get("sortID",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# good 是否极品
			self.good = data.get("good",0)
		
			# rate 权重
			self.rate = data.get("rate",0)
		
			# limit1 消费N个占星石后，加入奖池
			self.limit1 = data.get("limit1",0)
		
			# limit2 拥有后是否可再次抽取(特指宠物相关联的道具）
			self.limit2 = data.get("limit2",0)
		
			# limit3 在本期内能抽到几次
			self.limit3 = data.get("limit3",0)
		

# actChargeStar
class ResActChargeStar(object):
	RES_TABLE = "actChargeStar"
	__slots__ = ("id","num","rewardStar","desc","chargeId",)

    def __init__(self):
		
			# id 星盘表
			self.id = 0
		
			# num 可领取次数
			self.num = 0
		
			# rewardStar 奖励星钻数量
			self.rewardStar = 0
		
			# desc 描述
			self.desc = ""
		
			# chargeId 直购关联充值id
			self.chargeId = []
		

    def load_from_json(self, data):
		
			# id 星盘表
			self.id = data.get("id",0)
		
			# num 可领取次数
			self.num = data.get("num",0)
		
			# rewardStar 奖励星钻数量
			self.rewardStar = data.get("rewardStar",0)
		
			# desc 描述
			self.desc = data.get("desc","")
		
			# chargeId 直购关联充值id
			self.chargeId = data.get("chargeId",[])
		

# activityMain
class ResActivityMain(object):
	RES_TABLE = "activityMain"
	__slots__ = ("key","time","timeInfo","timeInfo2",)

    def __init__(self):
		
			# key 活动大厅表
			self.key = ""
		
			# time 时间
			self.time = []
		
			# timeInfo 界面时间说明1
			self.timeInfo = ""
		
			# timeInfo2 界面时间说明2
			self.timeInfo2 = ""
		

    def load_from_json(self, data):
		
			# key 活动大厅表
			self.key = data.get("key","")
		
			# time 时间
			self.time = data.get("time",[])
		
			# timeInfo 界面时间说明1
			self.timeInfo = data.get("timeInfo","")
		
			# timeInfo2 界面时间说明2
			self.timeInfo2 = data.get("timeInfo2","")
		

# huanian
class ResHuanian(object):
	RES_TABLE = "huanian"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","jjreward","offX","offY","scale","effectTip",)

    def __init__(self):
		
			# id 花撵表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# effectTip 特效升级提示
			self.effectTip = ""
		

    def load_from_json(self, data):
		
			# id 花撵表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# effectTip 特效升级提示
			self.effectTip = data.get("effectTip","")
		

# actTrailer
class ResActTrailer(object):
	RES_TABLE = "actTrailer"
	__slots__ = ("id","actId","img","x","y","openId","timeStr",)

    def __init__(self):
		
			# id 活动预告
			self.id = 0
		
			# actId 活动id
			self.actId = 0
		
			# img 图片资源名
			self.img = ""
		
			# x 坐标x
			self.x = 0
		
			# y 坐标y
			self.y = 0
		
			# openId 点击跳转功能id
			self.openId = 0
		
			# timeStr 预告时间文本
			self.timeStr = ""
		

    def load_from_json(self, data):
		
			# id 活动预告
			self.id = data.get("id",0)
		
			# actId 活动id
			self.actId = data.get("actId",0)
		
			# img 图片资源名
			self.img = data.get("img","")
		
			# x 坐标x
			self.x = data.get("x",0)
		
			# y 坐标y
			self.y = data.get("y",0)
		
			# openId 点击跳转功能id
			self.openId = data.get("openId",0)
		
			# timeStr 预告时间文本
			self.timeStr = data.get("timeStr","")
		

# storyAction
class ResStoryAction(object):
	RES_TABLE = "storyAction"
	__slots__ = ("id","group","sortValue","type","x","y","dir","openId","talkId","sceneId","time","nextStep","cameraParam","flashParam","maskParam",)

    def __init__(self):
		
			# id 剧情
			self.id = 0
		
			# group 剧情组
			self.group = 0
		
			# sortValue 序号
			self.sortValue = 0
		
			# type 类型
			self.type = 0
		
			# x 移动到x
			self.x = 0
		
			# y 移动到y
			self.y = 0
		
			# dir 方向
			self.dir = 0
		
			# openId 功能id
			self.openId = 0
		
			# talkId 对话组id
			self.talkId = 0
		
			# sceneId 场景id
			self.sceneId = 0
		
			# time 时间毫秒
			self.time = 0
		
			# nextStep 跳过步骤
			self.nextStep = 0
		
			# cameraParam 镜头拉伸参数
			self.cameraParam = []
		
			# flashParam 闪白开始参数
			self.flashParam = []
		
			# maskParam 遮罩参数
			self.maskParam = []
		

    def load_from_json(self, data):
		
			# id 剧情
			self.id = data.get("id",0)
		
			# group 剧情组
			self.group = data.get("group",0)
		
			# sortValue 序号
			self.sortValue = data.get("sortValue",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# x 移动到x
			self.x = data.get("x",0)
		
			# y 移动到y
			self.y = data.get("y",0)
		
			# dir 方向
			self.dir = data.get("dir",0)
		
			# openId 功能id
			self.openId = data.get("openId",0)
		
			# talkId 对话组id
			self.talkId = data.get("talkId",0)
		
			# sceneId 场景id
			self.sceneId = data.get("sceneId",0)
		
			# time 时间毫秒
			self.time = data.get("time",0)
		
			# nextStep 跳过步骤
			self.nextStep = data.get("nextStep",0)
		
			# cameraParam 镜头拉伸参数
			self.cameraParam = data.get("cameraParam",[])
		
			# flashParam 闪白开始参数
			self.flashParam = data.get("flashParam",[])
		
			# maskParam 遮罩参数
			self.maskParam = data.get("maskParam",[])
		

# storyTalk
class ResStoryTalk(object):
	RES_TABLE = "storyTalk"
	__slots__ = ("id","group","sortValue","text","left","icon","arrowx","arrowy","textx","texty","textw","texth","autoTime","speed","w","h","x","y",)

    def __init__(self):
		
			# id 对话配置
			self.id = 0
		
			# group 对话组
			self.group = 0
		
			# sortValue 对话顺序
			self.sortValue = 0
		
			# text 对话内容
			self.text = ""
		
			# left 头像是否左边
			self.left = 0
		
			# icon 头像
			self.icon = ""
		
			# arrowx 箭头x
			self.arrowx = 0
		
			# arrowy 箭头y
			self.arrowy = 0
		
			# textx 文本x
			self.textx = 0
		
			# texty 文本y
			self.texty = 0
		
			# textw 文本宽
			self.textw = 0
		
			# texth 文本高
			self.texth = 0
		
			# autoTime x秒后自动下一对话
			self.autoTime = 0
		
			# speed 每秒x个字速度
			self.speed = 0
		
			# w 宽
			self.w = 0
		
			# h 高
			self.h = 0
		
			# x x
			self.x = 0
		
			# y y
			self.y = 0
		

    def load_from_json(self, data):
		
			# id 对话配置
			self.id = data.get("id",0)
		
			# group 对话组
			self.group = data.get("group",0)
		
			# sortValue 对话顺序
			self.sortValue = data.get("sortValue",0)
		
			# text 对话内容
			self.text = data.get("text","")
		
			# left 头像是否左边
			self.left = data.get("left",0)
		
			# icon 头像
			self.icon = data.get("icon","")
		
			# arrowx 箭头x
			self.arrowx = data.get("arrowx",0)
		
			# arrowy 箭头y
			self.arrowy = data.get("arrowy",0)
		
			# textx 文本x
			self.textx = data.get("textx",0)
		
			# texty 文本y
			self.texty = data.get("texty",0)
		
			# textw 文本宽
			self.textw = data.get("textw",0)
		
			# texth 文本高
			self.texth = data.get("texth",0)
		
			# autoTime x秒后自动下一对话
			self.autoTime = data.get("autoTime",0)
		
			# speed 每秒x个字速度
			self.speed = data.get("speed",0)
		
			# w 宽
			self.w = data.get("w",0)
		
			# h 高
			self.h = data.get("h",0)
		
			# x x
			self.x = data.get("x",0)
		
			# y y
			self.y = data.get("y",0)
		

# reward
class ResReward(object):
	RES_TABLE = "reward"
	__slots__ = ("id","poolType","specPool1","specNum1","specPool2","specNum2","specPool3","specNum3","specPool4","specNum4","specPool5","specNum5","activityId","actPoolType","actSpecPool1","actSpecNum1","actSpecPool2","actSpecNum2","actSpecPool3","actSpecNum3","actSpecPool4","actSpecNum4","actSpecPool5","actSpecNum5",)

    def __init__(self):
		
			# id 奖励表
			self.id = 0
		
			# poolType 奖池类型
			self.poolType = []
		
			# specPool1 特殊奖励池1
			self.specPool1 = []
		
			# specNum1 特殊奖励数量1
			self.specNum1 = []
		
			# specPool2 特殊奖励池2
			self.specPool2 = []
		
			# specNum2 特殊奖励数量2
			self.specNum2 = []
		
			# specPool3 特殊奖励池3
			self.specPool3 = []
		
			# specNum3 特殊奖励数量3
			self.specNum3 = []
		
			# specPool4 特殊奖励池4
			self.specPool4 = []
		
			# specNum4 特殊奖励数量4
			self.specNum4 = []
		
			# specPool5 特殊奖励池5
			self.specPool5 = []
		
			# specNum5 特殊奖励数量5
			self.specNum5 = []
		
			# activityId 关联活动ID
			self.activityId = 0
		
			# actPoolType 活动奖池类型
			self.actPoolType = []
		
			# actSpecPool1 活动奖励池1
			self.actSpecPool1 = []
		
			# actSpecNum1 活动奖励数量1
			self.actSpecNum1 = []
		
			# actSpecPool2 活动奖励池2
			self.actSpecPool2 = []
		
			# actSpecNum2 活动奖励数量2
			self.actSpecNum2 = []
		
			# actSpecPool3 活动奖励池3
			self.actSpecPool3 = []
		
			# actSpecNum3 活动奖励数量3
			self.actSpecNum3 = []
		
			# actSpecPool4 活动奖励池4
			self.actSpecPool4 = []
		
			# actSpecNum4 活动奖励数量4
			self.actSpecNum4 = []
		
			# actSpecPool5 活动奖励池5
			self.actSpecPool5 = []
		
			# actSpecNum5 活动奖励数量5
			self.actSpecNum5 = []
		

    def load_from_json(self, data):
		
			# id 奖励表
			self.id = data.get("id",0)
		
			# poolType 奖池类型
			self.poolType = data.get("poolType",[])
		
			# specPool1 特殊奖励池1
			self.specPool1 = data.get("specPool1",[])
		
			# specNum1 特殊奖励数量1
			self.specNum1 = data.get("specNum1",[])
		
			# specPool2 特殊奖励池2
			self.specPool2 = data.get("specPool2",[])
		
			# specNum2 特殊奖励数量2
			self.specNum2 = data.get("specNum2",[])
		
			# specPool3 特殊奖励池3
			self.specPool3 = data.get("specPool3",[])
		
			# specNum3 特殊奖励数量3
			self.specNum3 = data.get("specNum3",[])
		
			# specPool4 特殊奖励池4
			self.specPool4 = data.get("specPool4",[])
		
			# specNum4 特殊奖励数量4
			self.specNum4 = data.get("specNum4",[])
		
			# specPool5 特殊奖励池5
			self.specPool5 = data.get("specPool5",[])
		
			# specNum5 特殊奖励数量5
			self.specNum5 = data.get("specNum5",[])
		
			# activityId 关联活动ID
			self.activityId = data.get("activityId",0)
		
			# actPoolType 活动奖池类型
			self.actPoolType = data.get("actPoolType",[])
		
			# actSpecPool1 活动奖励池1
			self.actSpecPool1 = data.get("actSpecPool1",[])
		
			# actSpecNum1 活动奖励数量1
			self.actSpecNum1 = data.get("actSpecNum1",[])
		
			# actSpecPool2 活动奖励池2
			self.actSpecPool2 = data.get("actSpecPool2",[])
		
			# actSpecNum2 活动奖励数量2
			self.actSpecNum2 = data.get("actSpecNum2",[])
		
			# actSpecPool3 活动奖励池3
			self.actSpecPool3 = data.get("actSpecPool3",[])
		
			# actSpecNum3 活动奖励数量3
			self.actSpecNum3 = data.get("actSpecNum3",[])
		
			# actSpecPool4 活动奖励池4
			self.actSpecPool4 = data.get("actSpecPool4",[])
		
			# actSpecNum4 活动奖励数量4
			self.actSpecNum4 = data.get("actSpecNum4",[])
		
			# actSpecPool5 活动奖励池5
			self.actSpecPool5 = data.get("actSpecPool5",[])
		
			# actSpecNum5 活动奖励数量5
			self.actSpecNum5 = data.get("actSpecNum5",[])
		

# roleSkill
class ResRoleSkill(object):
	RES_TABLE = "roleSkill"
	__slots__ = ("pos","lv","skillId",)

    def __init__(self):
		
			# pos 角色技能表
			self.pos = 0
		
			# lv 开放等级
			self.lv = 0
		
			# skillId 初始技能id
			self.skillId = 0
		

    def load_from_json(self, data):
		
			# pos 角色技能表
			self.pos = data.get("pos",0)
		
			# lv 开放等级
			self.lv = data.get("lv",0)
		
			# skillId 初始技能id
			self.skillId = data.get("skillId",0)
		

# buff
class ResBuff(object):
	RES_TABLE = "buff"
	__slots__ = ("id","ficon","fname","fdesc","delay",)

    def __init__(self):
		
			# id BUFF表
			self.id = 0
		
			# ficon 战斗-buff图标
			self.ficon = ""
		
			# fname 战斗-tips名字
			self.fname = ""
		
			# fdesc 战斗-tips描述
			self.fdesc = ""
		
			# delay 延时消除
			self.delay = 0
		

    def load_from_json(self, data):
		
			# id BUFF表
			self.id = data.get("id",0)
		
			# ficon 战斗-buff图标
			self.ficon = data.get("ficon","")
		
			# fname 战斗-tips名字
			self.fname = data.get("fname","")
		
			# fdesc 战斗-tips描述
			self.fdesc = data.get("fdesc","")
		
			# delay 延时消除
			self.delay = data.get("delay",0)
		

# arena
class ResArena(object):
	RES_TABLE = "arena"
	__slots__ = ("id","firstReward","rankReward","barrierId","monster","fa","min","max","seckill",)

    def __init__(self):
		
			# id 竞技场表
			self.id = 0
		
			# firstReward 首次奖励
			self.firstReward = []
		
			# rankReward 排名奖励
			self.rankReward = []
		
			# barrierId 副本id
			self.barrierId = 0
		
			# monster 电脑显示模型id
			self.monster = 0
		
			# fa 战力
			self.fa = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# seckill 秒杀
			self.seckill = 0
		

    def load_from_json(self, data):
		
			# id 竞技场表
			self.id = data.get("id",0)
		
			# firstReward 首次奖励
			self.firstReward = data.get("firstReward",[])
		
			# rankReward 排名奖励
			self.rankReward = data.get("rankReward",[])
		
			# barrierId 副本id
			self.barrierId = data.get("barrierId",0)
		
			# monster 电脑显示模型id
			self.monster = data.get("monster",0)
		
			# fa 战力
			self.fa = data.get("fa",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# seckill 秒杀
			self.seckill = data.get("seckill",0)
		

# jingmai
class ResJingmai(object):
	RES_TABLE = "jingmai"
	__slots__ = ("key","cost","attr","totalAttr",)

    def __init__(self):
		
			# key 经脉表
			self.key = 0
		
			# cost 消耗材料
			self.cost = []
		
			# attr 当前增加属性
			self.attr = []
		
			# totalAttr 总增加属性
			self.totalAttr = []
		

    def load_from_json(self, data):
		
			# key 经脉表
			self.key = data.get("key",0)
		
			# cost 消耗材料
			self.cost = data.get("cost",[])
		
			# attr 当前增加属性
			self.attr = data.get("attr",[])
		
			# totalAttr 总增加属性
			self.totalAttr = data.get("totalAttr",[])
		

# marry
class ResMarry(object):
	RES_TABLE = "marry"
	__slots__ = ("id","cost","firstReward","reward","bg","posx1","posy1","posx2","posy2",)

    def __init__(self):
		
			# id 结婚档次表
			self.id = 0
		
			# cost 消耗
			self.cost = []
		
			# firstReward 首次奖励
			self.firstReward = []
		
			# reward 奖励
			self.reward = []
		
			# bg 基地背景图
			self.bg = ""
		
			# posx1 我的角色坐标x
			self.posx1 = 0
		
			# posy1 我的角色坐标y
			self.posy1 = 0
		
			# posx2 伴侣的角色坐标x
			self.posx2 = 0
		
			# posy2 伴侣的角色坐标y
			self.posy2 = 0
		

    def load_from_json(self, data):
		
			# id 结婚档次表
			self.id = data.get("id",0)
		
			# cost 消耗
			self.cost = data.get("cost",[])
		
			# firstReward 首次奖励
			self.firstReward = data.get("firstReward",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# bg 基地背景图
			self.bg = data.get("bg","")
		
			# posx1 我的角色坐标x
			self.posx1 = data.get("posx1",0)
		
			# posy1 我的角色坐标y
			self.posy1 = data.get("posy1",0)
		
			# posx2 伴侣的角色坐标x
			self.posx2 = data.get("posx2",0)
		
			# posy2 伴侣的角色坐标y
			self.posy2 = data.get("posy2",0)
		

# marryPetLv
class ResMarryPetLv(object):
	RES_TABLE = "marryPetLv"
	__slots__ = ("id","exp","cost","baseAttr","onceAttr","passiveSkillId",)

    def __init__(self):
		
			# id 结伴宠物等级表
			self.id = 0
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# passiveSkillId 新增被动技能
			self.passiveSkillId = 0
		

    def load_from_json(self, data):
		
			# id 结伴宠物等级表
			self.id = data.get("id",0)
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# passiveSkillId 新增被动技能
			self.passiveSkillId = data.get("passiveSkillId",0)
		

# marryGift
class ResMarryGift(object):
	RES_TABLE = "marryGift"
	__slots__ = ("id","cost","reward",)

    def __init__(self):
		
			# id 礼金表
			self.id = 0
		
			# cost 消耗
			self.cost = []
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 礼金表
			self.id = data.get("id",0)
		
			# cost 消耗
			self.cost = data.get("cost",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# house
class ResHouse(object):
	RES_TABLE = "house"
	__slots__ = ("id","exp","cost","addExp","common","high","luxury",)

    def __init__(self):
		
			# id 房子表
			self.id = 0
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 每次点击升级消耗
			self.cost = []
		
			# addExp 每次点击升级获得经验
			self.addExp = 0
		
			# common 普通
			self.common = []
		
			# high 高级
			self.high = []
		
			# luxury 豪华
			self.luxury = []
		

    def load_from_json(self, data):
		
			# id 房子表
			self.id = data.get("id",0)
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 每次点击升级消耗
			self.cost = data.get("cost",[])
		
			# addExp 每次点击升级获得经验
			self.addExp = data.get("addExp",0)
		
			# common 普通
			self.common = data.get("common",[])
		
			# high 高级
			self.high = data.get("high",[])
		
			# luxury 豪华
			self.luxury = data.get("luxury",[])
		

# marryPower
class ResMarryPower(object):
	RES_TABLE = "marryPower"
	__slots__ = ("id","actName","cost","type","add","cd","enlimit","uselimit","btnImg","chatId","ptName","actImg","trueLove",)

    def __init__(self):
		
			# id 亲密度
			self.id = 0
		
			# actName 行动名字
			self.actName = ""
		
			# cost 消耗
			self.cost = []
		
			# type 类型
			self.type = 0
		
			# add 增加亲密度
			self.add = 0
		
			# cd 能量恢复时间0不恢复
			self.cd = 0
		
			# enlimit 能量上限0没有能量需求
			self.enlimit = 0
		
			# uselimit 每天使用限制0不限制
			self.uselimit = 0
		
			# btnImg 按钮图片
			self.btnImg = ""
		
			# chatId 广播
			self.chatId = 0
		
			# ptName 栗子
			self.ptName = ""
		
			# actImg 动画图片
			self.actImg = ""
		
			# trueLove 放入真爱邮箱
			self.trueLove = 0
		

    def load_from_json(self, data):
		
			# id 亲密度
			self.id = data.get("id",0)
		
			# actName 行动名字
			self.actName = data.get("actName","")
		
			# cost 消耗
			self.cost = data.get("cost",[])
		
			# type 类型
			self.type = data.get("type",0)
		
			# add 增加亲密度
			self.add = data.get("add",0)
		
			# cd 能量恢复时间0不恢复
			self.cd = data.get("cd",0)
		
			# enlimit 能量上限0没有能量需求
			self.enlimit = data.get("enlimit",0)
		
			# uselimit 每天使用限制0不限制
			self.uselimit = data.get("uselimit",0)
		
			# btnImg 按钮图片
			self.btnImg = data.get("btnImg","")
		
			# chatId 广播
			self.chatId = data.get("chatId",0)
		
			# ptName 栗子
			self.ptName = data.get("ptName","")
		
			# actImg 动画图片
			self.actImg = data.get("actImg","")
		
			# trueLove 放入真爱邮箱
			self.trueLove = data.get("trueLove",0)
		

# marryLv
class ResMarryLv(object):
	RES_TABLE = "marryLv"
	__slots__ = ("id","power","needExp","reward","openId","bg",)

    def __init__(self):
		
			# id 等级
			self.id = 0
		
			# power 等级需求
			self.power = 0
		
			# needExp 下级需求
			self.needExp = 0
		
			# reward 奖励
			self.reward = []
		
			# openId 转跳
			self.openId = 0
		
			# bg 背景图
			self.bg = ""
		

    def load_from_json(self, data):
		
			# id 等级
			self.id = data.get("id",0)
		
			# power 等级需求
			self.power = data.get("power",0)
		
			# needExp 下级需求
			self.needExp = data.get("needExp",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# openId 转跳
			self.openId = data.get("openId",0)
		
			# bg 背景图
			self.bg = data.get("bg","")
		

# marryPetStar
class ResMarryPetStar(object):
	RES_TABLE = "marryPetStar"
	__slots__ = ("id","name","star","quality","curLine","totalCircle","isUpMod","baseVal","val","cost","attr","mainSkillId","atkRate","hpRate","defRate","speedRate","atkRateMax","hpRateMax","defRateMax","speedRateMax",)

    def __init__(self):
		
			# id 结伴宠物星级表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# star 当前星级
			self.star = 0
		
			# quality 品质
			self.quality = 0
		
			# curLine 当前第几个圈第几条边
			self.curLine = []
		
			# totalCircle 有几个圈
			self.totalCircle = 0
		
			# isUpMod 进化标识
			self.isUpMod = 0
		
			# baseVal 种族值显示黑字
			self.baseVal = []
		
			# val 种族值增加红字
			self.val = []
		
			# cost 消耗道具
			self.cost = []
		
			# attr 当前属性
			self.attr = []
		
			# mainSkillId 主技能id
			self.mainSkillId = 0
		
			# atkRate 攻击继承千分比（当前阶数基础）
			self.atkRate = 0
		
			# hpRate 血量继承千分比（当前阶数基础）
			self.hpRate = 0
		
			# defRate 防御继承千分比（当前阶数基础）
			self.defRate = 0
		
			# speedRate 速度继承千分比（当前阶数基础）
			self.speedRate = 0
		
			# atkRateMax 攻击继承千分比（额外养成上限）
			self.atkRateMax = 0
		
			# hpRateMax 血量继承千分比（额外养成上限）
			self.hpRateMax = 0
		
			# defRateMax 防御继承千分比（额外养成上限）
			self.defRateMax = 0
		
			# speedRateMax 速度继承千分比（额外养成上限）
			self.speedRateMax = 0
		

    def load_from_json(self, data):
		
			# id 结伴宠物星级表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# star 当前星级
			self.star = data.get("star",0)
		
			# quality 品质
			self.quality = data.get("quality",0)
		
			# curLine 当前第几个圈第几条边
			self.curLine = data.get("curLine",[])
		
			# totalCircle 有几个圈
			self.totalCircle = data.get("totalCircle",0)
		
			# isUpMod 进化标识
			self.isUpMod = data.get("isUpMod",0)
		
			# baseVal 种族值显示黑字
			self.baseVal = data.get("baseVal",[])
		
			# val 种族值增加红字
			self.val = data.get("val",[])
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# attr 当前属性
			self.attr = data.get("attr",[])
		
			# mainSkillId 主技能id
			self.mainSkillId = data.get("mainSkillId",0)
		
			# atkRate 攻击继承千分比（当前阶数基础）
			self.atkRate = data.get("atkRate",0)
		
			# hpRate 血量继承千分比（当前阶数基础）
			self.hpRate = data.get("hpRate",0)
		
			# defRate 防御继承千分比（当前阶数基础）
			self.defRate = data.get("defRate",0)
		
			# speedRate 速度继承千分比（当前阶数基础）
			self.speedRate = data.get("speedRate",0)
		
			# atkRateMax 攻击继承千分比（额外养成上限）
			self.atkRateMax = data.get("atkRateMax",0)
		
			# hpRateMax 血量继承千分比（额外养成上限）
			self.hpRateMax = data.get("hpRateMax",0)
		
			# defRateMax 防御继承千分比（额外养成上限）
			self.defRateMax = data.get("defRateMax",0)
		
			# speedRateMax 速度继承千分比（额外养成上限）
			self.speedRateMax = data.get("speedRateMax",0)
		

# marryPetCultivate
class ResMarryPetCultivate(object):
	RES_TABLE = "marryPetCultivate"
	__slots__ = ("id","type","rate","addCount","addVal",)

    def __init__(self):
		
			# id 结伴宠物培养表
			self.id = 0
		
			# type 类型
			self.type = 0
		
			# rate 权重
			self.rate = 0
		
			# addCount 增加条数
			self.addCount = []
		
			# addVal 增加值
			self.addVal = []
		

    def load_from_json(self, data):
		
			# id 结伴宠物培养表
			self.id = data.get("id",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# rate 权重
			self.rate = data.get("rate",0)
		
			# addCount 增加条数
			self.addCount = data.get("addCount",[])
		
			# addVal 增加值
			self.addVal = data.get("addVal",[])
		

# skill
class ResSkill(object):
	RES_TABLE = "skill"
	__slots__ = ("id","skillId","level","type","prev","next","name","quality","subType","atttype","odds","effType","powerfulList","powerful","upLvCond","upCost","actPoint","myEffType","enEffType","effectId","args","force","buffIcon","xdpName","xdpDesc","xdpSort",)

    def __init__(self):
		
			# id 技能表
			self.id = 0
		
			# skillId 技能Id
			self.skillId = 0
		
			# level 等级
			self.level = 0
		
			# type 类型
			self.type = 0
		
			# prev 上一级
			self.prev = 0
		
			# next 下一级
			self.next = 0
		
			# name 名称
			self.name = ""
		
			# quality 品质
			self.quality = 0
		
			# subType 子类型
			self.subType = 0
		
			# atttype 攻击类型
			self.atttype = 0
		
			# odds 触发概率
			self.odds = 0
		
			# effType 效果类型
			self.effType = 0
		
			# powerfulList 增强技能宠物id
			self.powerfulList = []
		
			# powerful 是否增强技能
			self.powerful = 0
		
			# upLvCond 升级等级限制
			self.upLvCond = 0
		
			# upCost 升级消耗
			self.upCost = []
		
			# actPoint 行动时机点
			self.actPoint = 0
		
			# myEffType 我方作用类型
			self.myEffType = 0
		
			# enEffType 敌方作用类型
			self.enEffType = 0
		
			# effectId 效果id
			self.effectId = 0
		
			# args 参数
			self.args = []
		
			# force 资质技能用的：是否强制生效不顶替
			self.force = 0
		
			# buffIcon 携带品buff图标
			self.buffIcon = ""
		
			# xdpName 携带品的名字
			self.xdpName = ""
		
			# xdpDesc 携带品技能描述
			self.xdpDesc = ""
		
			# xdpSort 携带品技能排序
			self.xdpSort = 0
		

    def load_from_json(self, data):
		
			# id 技能表
			self.id = data.get("id",0)
		
			# skillId 技能Id
			self.skillId = data.get("skillId",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# prev 上一级
			self.prev = data.get("prev",0)
		
			# next 下一级
			self.next = data.get("next",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# quality 品质
			self.quality = data.get("quality",0)
		
			# subType 子类型
			self.subType = data.get("subType",0)
		
			# atttype 攻击类型
			self.atttype = data.get("atttype",0)
		
			# odds 触发概率
			self.odds = data.get("odds",0)
		
			# effType 效果类型
			self.effType = data.get("effType",0)
		
			# powerfulList 增强技能宠物id
			self.powerfulList = data.get("powerfulList",[])
		
			# powerful 是否增强技能
			self.powerful = data.get("powerful",0)
		
			# upLvCond 升级等级限制
			self.upLvCond = data.get("upLvCond",0)
		
			# upCost 升级消耗
			self.upCost = data.get("upCost",[])
		
			# actPoint 行动时机点
			self.actPoint = data.get("actPoint",0)
		
			# myEffType 我方作用类型
			self.myEffType = data.get("myEffType",0)
		
			# enEffType 敌方作用类型
			self.enEffType = data.get("enEffType",0)
		
			# effectId 效果id
			self.effectId = data.get("effectId",0)
		
			# args 参数
			self.args = data.get("args",[])
		
			# force 资质技能用的：是否强制生效不顶替
			self.force = data.get("force",0)
		
			# buffIcon 携带品buff图标
			self.buffIcon = data.get("buffIcon","")
		
			# xdpName 携带品的名字
			self.xdpName = data.get("xdpName","")
		
			# xdpDesc 携带品技能描述
			self.xdpDesc = data.get("xdpDesc","")
		
			# xdpSort 携带品技能排序
			self.xdpSort = data.get("xdpSort",0)
		

# shenmishangdian3Time
class ResShenmishangdian3Time(object):
	RES_TABLE = "shenmishangdian3Time"
	__slots__ = ("id","cycle","startend",)

    def __init__(self):
		
			# id 神秘商店
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# startend 活动时间
			self.startend = []
		

    def load_from_json(self, data):
		
			# id 神秘商店
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# startend 活动时间
			self.startend = data.get("startend",[])
		

# meirijuhui
class ResMeirijuhui(object):
	RES_TABLE = "meirijuhui"
	__slots__ = ("id","leichong","reward","btnName","SkinId","info",)

    def __init__(self):
		
			# id 每日钜惠
			self.id = 0
		
			# leichong 累充需求分单位
			self.leichong = 0
		
			# reward 奖励
			self.reward = []
		
			# btnName 按钮文字
			self.btnName = ""
		
			# SkinId 皮肤id0普通1元旦
			self.SkinId = 0
		
			# info 界面说明
			self.info = ""
		

    def load_from_json(self, data):
		
			# id 每日钜惠
			self.id = data.get("id",0)
		
			# leichong 累充需求分单位
			self.leichong = data.get("leichong",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# btnName 按钮文字
			self.btnName = data.get("btnName","")
		
			# SkinId 皮肤id0普通1元旦
			self.SkinId = data.get("SkinId",0)
		
			# info 界面说明
			self.info = data.get("info","")
		

# huanlezadan
class ResHuanlezadan(object):
	RES_TABLE = "huanlezadan"
	__slots__ = ("id","cycle","days","empty","next","rewardPool","goldReward",)

    def __init__(self):
		
			# id 神秘商店
			self.id = 0
		
			# cycle 档期（必须与id一致
			self.cycle = 0
		
			# days 活动天数
			self.days = 0
		
			# empty 是否空挡
			self.empty = 0
		
			# next 下一档期
			self.next = 0
		
			# rewardPool 奖池普通蛋
			self.rewardPool = 0
		
			# goldReward 金蛋奖励
			self.goldReward = []
		

    def load_from_json(self, data):
		
			# id 神秘商店
			self.id = data.get("id",0)
		
			# cycle 档期（必须与id一致
			self.cycle = data.get("cycle",0)
		
			# days 活动天数
			self.days = data.get("days",0)
		
			# empty 是否空挡
			self.empty = data.get("empty",0)
		
			# next 下一档期
			self.next = data.get("next",0)
		
			# rewardPool 奖池普通蛋
			self.rewardPool = data.get("rewardPool",0)
		
			# goldReward 金蛋奖励
			self.goldReward = data.get("goldReward",[])
		

# huanlezadanCost
class ResHuanlezadanCost(object):
	RES_TABLE = "huanlezadanCost"
	__slots__ = ("id","Cost","num","totle",)

    def __init__(self):
		
			# id 欢乐砸蛋消耗
			self.id = 0
		
			# Cost 消耗钻石(当前档次需消耗)
			self.Cost = 0
		
			# num 奖励砸蛋次数
			self.num = 0
		
			# totle 累计总数(当前总数+当前消耗)=当前档次
			self.totle = 0
		

    def load_from_json(self, data):
		
			# id 欢乐砸蛋消耗
			self.id = data.get("id",0)
		
			# Cost 消耗钻石(当前档次需消耗)
			self.Cost = data.get("Cost",0)
		
			# num 奖励砸蛋次数
			self.num = data.get("num",0)
		
			# totle 累计总数(当前总数+当前消耗)=当前档次
			self.totle = data.get("totle",0)
		

# huanlezadan1
class ResHuanlezadan1(object):
	RES_TABLE = "huanlezadan1"
	__slots__ = ("id","cycle","Open","End","rewardPool","goldReward","xiaoejingxi","TacoFace",)

    def __init__(self):
		
			# id 神秘商店
			self.id = 0
		
			# cycle 档期（必须与id一致
			self.cycle = 0
		
			# Open 开启时间包含
			self.Open = ""
		
			# End 结束时间不包含
			self.End = ""
		
			# rewardPool 奖池普通蛋
			self.rewardPool = 0
		
			# goldReward 金蛋奖励
			self.goldReward = []
		
			# xiaoejingxi 小额惊喜
			self.xiaoejingxi = []
		
			# TacoFace 每日打脸次数
			self.TacoFace = 0
		

    def load_from_json(self, data):
		
			# id 神秘商店
			self.id = data.get("id",0)
		
			# cycle 档期（必须与id一致
			self.cycle = data.get("cycle",0)
		
			# Open 开启时间包含
			self.Open = data.get("Open","")
		
			# End 结束时间不包含
			self.End = data.get("End","")
		
			# rewardPool 奖池普通蛋
			self.rewardPool = data.get("rewardPool",0)
		
			# goldReward 金蛋奖励
			self.goldReward = data.get("goldReward",[])
		
			# xiaoejingxi 小额惊喜
			self.xiaoejingxi = data.get("xiaoejingxi",[])
		
			# TacoFace 每日打脸次数
			self.TacoFace = data.get("TacoFace",0)
		

# huanlezadanCost1
class ResHuanlezadanCost1(object):
	RES_TABLE = "huanlezadanCost1"
	__slots__ = ("id","Cost","num","totle",)

    def __init__(self):
		
			# id 欢乐砸蛋消耗
			self.id = 0
		
			# Cost 消耗钻石(当前档次需消耗)
			self.Cost = 0
		
			# num 奖励砸蛋次数
			self.num = 0
		
			# totle 累计总数(当前总数+当前消耗)=当前档次
			self.totle = 0
		

    def load_from_json(self, data):
		
			# id 欢乐砸蛋消耗
			self.id = data.get("id",0)
		
			# Cost 消耗钻石(当前档次需消耗)
			self.Cost = data.get("Cost",0)
		
			# num 奖励砸蛋次数
			self.num = data.get("num",0)
		
			# totle 累计总数(当前总数+当前消耗)=当前档次
			self.totle = data.get("totle",0)
		

# shenmishangdian1
class ResShenmishangdian1(object):
	RES_TABLE = "shenmishangdian1"
	__slots__ = ("id","cycle","next","days","empty","reward","cost","discount","limit","reset","sort",)

    def __init__(self):
		
			# id 神秘商店
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# next 下一档期
			self.next = 0
		
			# days 活动天数
			self.days = 0
		
			# empty 是否空挡
			self.empty = 0
		
			# reward 奖励
			self.reward = []
		
			# cost 原价
			self.cost = []
		
			# discount 折后价
			self.discount = []
		
			# limit 限购
			self.limit = 0
		
			# reset 是否重置
			self.reset = 0
		
			# sort 排序
			self.sort = 0
		

    def load_from_json(self, data):
		
			# id 神秘商店
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# next 下一档期
			self.next = data.get("next",0)
		
			# days 活动天数
			self.days = data.get("days",0)
		
			# empty 是否空挡
			self.empty = data.get("empty",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cost 原价
			self.cost = data.get("cost",[])
		
			# discount 折后价
			self.discount = data.get("discount",[])
		
			# limit 限购
			self.limit = data.get("limit",0)
		
			# reset 是否重置
			self.reset = data.get("reset",0)
		
			# sort 排序
			self.sort = data.get("sort",0)
		

# jierifanli
class ResJierifanli(object):
	RES_TABLE = "jierifanli"
	__slots__ = ("id","cycle","days","empty","next","reward","cost",)

    def __init__(self):
		
			# id 节日返利
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# days 活动天数
			self.days = 0
		
			# empty 是否空挡
			self.empty = 0
		
			# next 下一档期
			self.next = 0
		
			# reward 奖励
			self.reward = []
		
			# cost 消耗多少钻石
			self.cost = 0
		

    def load_from_json(self, data):
		
			# id 节日返利
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# days 活动天数
			self.days = data.get("days",0)
		
			# empty 是否空挡
			self.empty = data.get("empty",0)
		
			# next 下一档期
			self.next = data.get("next",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cost 消耗多少钻石
			self.cost = data.get("cost",0)
		

# shenmishangdian2
class ResShenmishangdian2(object):
	RES_TABLE = "shenmishangdian2"
	__slots__ = ("id","cycle","days","empty","next","reward","cost","discount","limit","reset",)

    def __init__(self):
		
			# id 神秘商店
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# days 活动天数
			self.days = 0
		
			# empty 是否空挡
			self.empty = 0
		
			# next 下一档期
			self.next = 0
		
			# reward 奖励
			self.reward = []
		
			# cost 原价
			self.cost = []
		
			# discount 折后价
			self.discount = []
		
			# limit 限购
			self.limit = 0
		
			# reset 是否重置
			self.reset = 0
		

    def load_from_json(self, data):
		
			# id 神秘商店
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# days 活动天数
			self.days = data.get("days",0)
		
			# empty 是否空挡
			self.empty = data.get("empty",0)
		
			# next 下一档期
			self.next = data.get("next",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cost 原价
			self.cost = data.get("cost",[])
		
			# discount 折后价
			self.discount = data.get("discount",[])
		
			# limit 限购
			self.limit = data.get("limit",0)
		
			# reset 是否重置
			self.reset = data.get("reset",0)
		

# shenmishangdian3
class ResShenmishangdian3(object):
	RES_TABLE = "shenmishangdian3"
	__slots__ = ("id","cycle","days","empty","next","reward","cost","discount","limit","reset",)

    def __init__(self):
		
			# id 神秘商店
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# days 活动天数
			self.days = 0
		
			# empty 是否空挡
			self.empty = 0
		
			# next 下一档期
			self.next = 0
		
			# reward 奖励
			self.reward = []
		
			# cost 原价
			self.cost = []
		
			# discount 折后价
			self.discount = []
		
			# limit 限购
			self.limit = 0
		
			# reset 是否重置
			self.reset = 0
		

    def load_from_json(self, data):
		
			# id 神秘商店
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# days 活动天数
			self.days = data.get("days",0)
		
			# empty 是否空挡
			self.empty = data.get("empty",0)
		
			# next 下一档期
			self.next = data.get("next",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cost 原价
			self.cost = data.get("cost",[])
		
			# discount 折后价
			self.discount = data.get("discount",[])
		
			# limit 限购
			self.limit = data.get("limit",0)
		
			# reset 是否重置
			self.reset = data.get("reset",0)
		

# roleinit
class ResRoleinit(object):
	RES_TABLE = "roleinit"
	__slots__ = ("key","i","s","arraystring2","arrayint2",)

    def __init__(self):
		
			# key 角色初始化表
			self.key = ""
		
			# i 正整数
			self.i = 0
		
			# s 字符串
			self.s = ""
		
			# arraystring2 二维数组（字符串）
			self.arraystring2 = []
		
			# arrayint2 二维数组（整形）
			self.arrayint2 = []
		

    def load_from_json(self, data):
		
			# key 角色初始化表
			self.key = data.get("key","")
		
			# i 正整数
			self.i = data.get("i",0)
		
			# s 字符串
			self.s = data.get("s","")
		
			# arraystring2 二维数组（字符串）
			self.arraystring2 = data.get("arraystring2",[])
		
			# arrayint2 二维数组（整形）
			self.arrayint2 = data.get("arrayint2",[])
		

# level
class ResLevel(object):
	RES_TABLE = "level"
	__slots__ = ("level","exp","attr","shituRecvAttr","shituSendAttr","shituTask","shituWanmei",)

    def __init__(self):
		
			# level 角色等级表
			self.level = 0
		
			# exp 经验
			self.exp = 0
		
			# attr 属性
			self.attr = []
		
			# shituRecvAttr 师徒-徒弟收(多少经验值)
			self.shituRecvAttr = []
		
			# shituSendAttr 师徒-师傅传(多少经验值)
			self.shituSendAttr = []
		
			# shituTask 师徒-任务奖励
			self.shituTask = []
		
			# shituWanmei 师徒-徒弟完美出师奖励(多少经验值)
			self.shituWanmei = []
		

    def load_from_json(self, data):
		
			# level 角色等级表
			self.level = data.get("level",0)
		
			# exp 经验
			self.exp = data.get("exp",0)
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# shituRecvAttr 师徒-徒弟收(多少经验值)
			self.shituRecvAttr = data.get("shituRecvAttr",[])
		
			# shituSendAttr 师徒-师傅传(多少经验值)
			self.shituSendAttr = data.get("shituSendAttr",[])
		
			# shituTask 师徒-任务奖励
			self.shituTask = data.get("shituTask",[])
		
			# shituWanmei 师徒-徒弟完美出师奖励(多少经验值)
			self.shituWanmei = data.get("shituWanmei",[])
		

# newKfkhActive
class ResNewKfkhActive(object):
	RES_TABLE = "newKfkhActive"
	__slots__ = ("id","openDay","lastDay",)

    def __init__(self):
		
			# id 新开服狂欢期号表
			self.id = 0
		
			# openDay 开服第X天开启
			self.openDay = 0
		
			# lastDay 持续天数
			self.lastDay = 0
		

    def load_from_json(self, data):
		
			# id 新开服狂欢期号表
			self.id = data.get("id",0)
		
			# openDay 开服第X天开启
			self.openDay = data.get("openDay",0)
		
			# lastDay 持续天数
			self.lastDay = data.get("lastDay",0)
		

# newKfkhLimitReward
class ResNewKfkhLimitReward(object):
	RES_TABLE = "newKfkhLimitReward"
	__slots__ = ("id","cycle","titleIcon","giftIcon","reward","limit","costOld","cost","chargeOld","chargeId",)

    def __init__(self):
		
			# id 限購禮包
			self.id = 0
		
			# cycle 周期
			self.cycle = 0
		
			# titleIcon 名稱圖標
			self.titleIcon = ""
		
			# giftIcon 禮包圖標
			self.giftIcon = ""
		
			# reward 獎勵
			self.reward = []
		
			# limit 限購次數
			self.limit = 0
		
			# costOld 原價1
			self.costOld = 0
		
			# cost 花費
			self.cost = []
		
			# chargeOld 原價2
			self.chargeOld = 0
		
			# chargeId 直購關聯充值id
			self.chargeId = []
		

    def load_from_json(self, data):
		
			# id 限購禮包
			self.id = data.get("id",0)
		
			# cycle 周期
			self.cycle = data.get("cycle",0)
		
			# titleIcon 名稱圖標
			self.titleIcon = data.get("titleIcon","")
		
			# giftIcon 禮包圖標
			self.giftIcon = data.get("giftIcon","")
		
			# reward 獎勵
			self.reward = data.get("reward",[])
		
			# limit 限購次數
			self.limit = data.get("limit",0)
		
			# costOld 原價1
			self.costOld = data.get("costOld",0)
		
			# cost 花費
			self.cost = data.get("cost",[])
		
			# chargeOld 原價2
			self.chargeOld = data.get("chargeOld",0)
		
			# chargeId 直購關聯充值id
			self.chargeId = data.get("chargeId",[])
		

# newKfkhShop
class ResNewKfkhShop(object):
	RES_TABLE = "newKfkhShop"
	__slots__ = ("id","limit","cost","reward","cycle",)

    def __init__(self):
		
			# id 新开服狂欢商店
			self.id = 0
		
			# limit 限购次数
			self.limit = 0
		
			# cost 花费
			self.cost = []
		
			# reward 奖励
			self.reward = []
		
			# cycle 周期
			self.cycle = 0
		

    def load_from_json(self, data):
		
			# id 新开服狂欢商店
			self.id = data.get("id",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# cost 花费
			self.cost = data.get("cost",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cycle 周期
			self.cycle = data.get("cycle",0)
		

# newKfkhLoginReward
class ResNewKfkhLoginReward(object):
	RES_TABLE = "newKfkhLoginReward"
	__slots__ = ("id","cycle","day","reward",)

    def __init__(self):
		
			# id key
			self.id = 0
		
			# cycle 周期
			self.cycle = 0
		
			# day 新开服狂欢登陆天数
			self.day = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id key
			self.id = data.get("id",0)
		
			# cycle 周期
			self.cycle = data.get("cycle",0)
		
			# day 新开服狂欢登陆天数
			self.day = data.get("day",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# newKfkhTask
class ResNewKfkhTask(object):
	RES_TABLE = "newKfkhTask"
	__slots__ = ("id","cycle","pageOpen","taskOpen","taskEnd","taskList",)

    def __init__(self):
		
			# id 任务页签
			self.id = 0
		
			# cycle 周期
			self.cycle = 0
		
			# pageOpen 页签开启时间(开服第x天)
			self.pageOpen = 0
		
			# taskOpen 任务开始时间(开服第x天)
			self.taskOpen = 0
		
			# taskEnd 任务结束时间(开服第x天)
			self.taskEnd = 0
		
			# taskList 任务列表
			self.taskList = []
		

    def load_from_json(self, data):
		
			# id 任务页签
			self.id = data.get("id",0)
		
			# cycle 周期
			self.cycle = data.get("cycle",0)
		
			# pageOpen 页签开启时间(开服第x天)
			self.pageOpen = data.get("pageOpen",0)
		
			# taskOpen 任务开始时间(开服第x天)
			self.taskOpen = data.get("taskOpen",0)
		
			# taskEnd 任务结束时间(开服第x天)
			self.taskEnd = data.get("taskEnd",0)
		
			# taskList 任务列表
			self.taskList = data.get("taskList",[])
		

# lingqi
class ResLingqi(object):
	RES_TABLE = "lingqi"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","jjreward","offX","offY","scale","effectTip",)

    def __init__(self):
		
			# id 灵气表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# effectTip 特效升级提示
			self.effectTip = ""
		

    def load_from_json(self, data):
		
			# id 灵气表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# effectTip 特效升级提示
			self.effectTip = data.get("effectTip","")
		

# kuafuMap
class ResKuafuMap(object):
	RES_TABLE = "kuafuMap"
	__slots__ = ("id","serverNo","serverNoClient",)

    def __init__(self):
		
			# id 映射数字编号
			self.id = 0
		
			# serverNo 真实服务器编号
			self.serverNo = ""
		
			# serverNoClient 服id前端用
			self.serverNoClient = ""
		

    def load_from_json(self, data):
		
			# id 映射数字编号
			self.id = data.get("id",0)
		
			# serverNo 真实服务器编号
			self.serverNo = data.get("serverNo","")
		
			# serverNoClient 服id前端用
			self.serverNoClient = data.get("serverNoClient","")
		

# kuafuGroup
class ResKuafuGroup(object):
	RES_TABLE = "kuafuGroup"
	__slots__ = ("id","sid","type","num",)

    def __init__(self):
		
			# id id
			self.id = 0
		
			# sid 映射数字编号
			self.sid = []
		
			# type 模块id
			self.type = 0
		
			# num 内分组数量
			self.num = 0
		

    def load_from_json(self, data):
		
			# id id
			self.id = data.get("id",0)
		
			# sid 映射数字编号
			self.sid = data.get("sid",[])
		
			# type 模块id
			self.type = data.get("type",0)
		
			# num 内分组数量
			self.num = data.get("num",0)
		

# serverMergeMap
class ResServerMergeMap(object):
	RES_TABLE = "serverMergeMap"
	__slots__ = ("serverNo","curMain",)

    def __init__(self):
		
			# serverNo 真实服务器编号
			self.serverNo = ""
		
			# curMain 当前从属主服
			self.curMain = ""
		

    def load_from_json(self, data):
		
			# serverNo 真实服务器编号
			self.serverNo = data.get("serverNo","")
		
			# curMain 当前从属主服
			self.curMain = data.get("curMain","")
		

# kuafuServerNo
class ResKuafuServerNo(object):
	RES_TABLE = "kuafuServerNo"
	__slots__ = ("serverNo","serverNoClient","type",)

    def __init__(self):
		
			# serverNo 真实服务器编号
			self.serverNo = ""
		
			# serverNoClient 服id前端用
			self.serverNoClient = ""
		
			# type 渠道分组
			self.type = 0
		

    def load_from_json(self, data):
		
			# serverNo 真实服务器编号
			self.serverNo = data.get("serverNo","")
		
			# serverNoClient 服id前端用
			self.serverNoClient = data.get("serverNoClient","")
		
			# type 渠道分组
			self.type = data.get("type",0)
		

# xianshituisonglibao
class ResXianshituisonglibao(object):
	RES_TABLE = "xianshituisonglibao"
	__slots__ = ("id","search","reward","targeid","attr","limit","andor","targetSW","switch","push","reset","cond","cost","ownValue","charge","connectId","sort","pos","listpos","checkpass",)

    def __init__(self):
		
			# id 限时推送礼包
			self.id = 0
		
			# search 搜索顺序
			self.search = 0
		
			# reward 奖励
			self.reward = []
		
			# targeid 对应礼包ID
			self.targeid = 0
		
			# attr 奖励属性
			self.attr = []
		
			# limit 限购
			self.limit = 0
		
			# andor 计数与或条件
			self.andor = 0
		
			# targetSW 购买统计类型
			self.targetSW = 0
		
			# switch 计数前置要求
			self.switch = []
		
			# push 计数出发推送
			self.push = 0
		
			# reset 计数是否重置
			self.reset = 0
		
			# cond 条件
			self.cond = 0
		
			# cost 消耗
			self.cost = []
		
			# ownValue 价值
			self.ownValue = 0
		
			# charge 消耗-充值id
			self.charge = []
		
			# connectId 关联礼包Id
			self.connectId = []
		
			# sort 礼包排序(只针对界面类型1组数<3到时候直接关闭界面)
			self.sort = []
		
			# pos 礼包大图标偏移(界面类型5专用)
			self.pos = []
		
			# listpos 礼包奖励图标的偏移(界面类型5专用)
			self.listpos = []
		
			# checkpass 检查满足不推送
			self.checkpass = 0
		

    def load_from_json(self, data):
		
			# id 限时推送礼包
			self.id = data.get("id",0)
		
			# search 搜索顺序
			self.search = data.get("search",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# targeid 对应礼包ID
			self.targeid = data.get("targeid",0)
		
			# attr 奖励属性
			self.attr = data.get("attr",[])
		
			# limit 限购
			self.limit = data.get("limit",0)
		
			# andor 计数与或条件
			self.andor = data.get("andor",0)
		
			# targetSW 购买统计类型
			self.targetSW = data.get("targetSW",0)
		
			# switch 计数前置要求
			self.switch = data.get("switch",[])
		
			# push 计数出发推送
			self.push = data.get("push",0)
		
			# reset 计数是否重置
			self.reset = data.get("reset",0)
		
			# cond 条件
			self.cond = data.get("cond",0)
		
			# cost 消耗
			self.cost = data.get("cost",[])
		
			# ownValue 价值
			self.ownValue = data.get("ownValue",0)
		
			# charge 消耗-充值id
			self.charge = data.get("charge",[])
		
			# connectId 关联礼包Id
			self.connectId = data.get("connectId",[])
		
			# sort 礼包排序(只针对界面类型1组数<3到时候直接关闭界面)
			self.sort = data.get("sort",[])
		
			# pos 礼包大图标偏移(界面类型5专用)
			self.pos = data.get("pos",[])
		
			# listpos 礼包奖励图标的偏移(界面类型5专用)
			self.listpos = data.get("listpos",[])
		
			# checkpass 检查满足不推送
			self.checkpass = data.get("checkpass",0)
		

# weekGift
class ResWeekGift(object):
	RES_TABLE = "weekGift"
	__slots__ = ("id","cycNo","level","cost","reward",)

    def __init__(self):
		
			# id 每周礼包表
			self.id = 0
		
			# cycNo 周期
			self.cycNo = 0
		
			# level 档位
			self.level = 0
		
			# cost 消耗材料
			self.cost = []
		
			# reward 奖励物品
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 每周礼包表
			self.id = data.get("id",0)
		
			# cycNo 周期
			self.cycNo = data.get("cycNo",0)
		
			# level 档位
			self.level = data.get("level",0)
		
			# cost 消耗材料
			self.cost = data.get("cost",[])
		
			# reward 奖励物品
			self.reward = data.get("reward",[])
		

# dayGift
class ResDayGift(object):
	RES_TABLE = "dayGift"
	__slots__ = ("id","cycNo","level","cost","reward",)

    def __init__(self):
		
			# id 每日礼包表
			self.id = 0
		
			# cycNo 周期
			self.cycNo = 0
		
			# level 档位
			self.level = 0
		
			# cost 消耗材料
			self.cost = []
		
			# reward 奖励物品
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 每日礼包表
			self.id = data.get("id",0)
		
			# cycNo 周期
			self.cycNo = data.get("cycNo",0)
		
			# level 档位
			self.level = data.get("level",0)
		
			# cost 消耗材料
			self.cost = data.get("cost",[])
		
			# reward 奖励物品
			self.reward = data.get("reward",[])
		

# chat
class ResChat(object):
	RES_TABLE = "chat"
	__slots__ = ("id","type","content","MagicLampId",)

    def __init__(self):
		
			# id 聊天模板表
			self.id = 0
		
			# type 类型
			self.type = 0
		
			# content 内容内容不填聊天框则没有消息内容不填聊天框则没有消息内容不填聊天框则没有消息内容不填聊天框则没有消息
			self.content = ""
		
			# MagicLampId 走马灯ID
			self.MagicLampId = 0
		

    def load_from_json(self, data):
		
			# id 聊天模板表
			self.id = data.get("id",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# content 内容内容不填聊天框则没有消息内容不填聊天框则没有消息内容不填聊天框则没有消息内容不填聊天框则没有消息
			self.content = data.get("content","")
		
			# MagicLampId 走马灯ID
			self.MagicLampId = data.get("MagicLampId",0)
		

# MagicLamp
class ResMagicLamp(object):
	RES_TABLE = "MagicLamp"
	__slots__ = ("id","content","num","particle",)

    def __init__(self):
		
			# id 聊天模板表
			self.id = 0
		
			# content 内容
			self.content = ""
		
			# num 次数
			self.num = 0
		
			# particle 栗子
			self.particle = ""
		

    def load_from_json(self, data):
		
			# id 聊天模板表
			self.id = data.get("id",0)
		
			# content 内容
			self.content = data.get("content","")
		
			# num 次数
			self.num = data.get("num",0)
		
			# particle 栗子
			self.particle = data.get("particle","")
		

# meiqimiaosha
class ResMeiqimiaosha(object):
	RES_TABLE = "meiqimiaosha"
	__slots__ = ("id","actid","skinId","skinName","type","reward","limit","virtual","cost","chargeId",)

    def __init__(self):
		
			# id 每日秒杀(新年大换装
			self.id = 0
		
			# actid 关联活动id
			self.actid = 0
		
			# skinId 皮肤配置表Id
			self.skinId = 0
		
			# skinName 皮肤名字
			self.skinName = ""
		
			# type 模块类型
			self.type = 0
		
			# reward 獎勵
			self.reward = []
		
			# limit 限購次數0不限制
			self.limit = 0
		
			# virtual 虚拟花費（最后选择
			self.virtual = 0
		
			# cost 花費（其次选择
			self.cost = []
		
			# chargeId 直購關聯充值id(优先选择)
			self.chargeId = []
		

    def load_from_json(self, data):
		
			# id 每日秒杀(新年大换装
			self.id = data.get("id",0)
		
			# actid 关联活动id
			self.actid = data.get("actid",0)
		
			# skinId 皮肤配置表Id
			self.skinId = data.get("skinId",0)
		
			# skinName 皮肤名字
			self.skinName = data.get("skinName","")
		
			# type 模块类型
			self.type = data.get("type",0)
		
			# reward 獎勵
			self.reward = data.get("reward",[])
		
			# limit 限購次數0不限制
			self.limit = data.get("limit",0)
		
			# virtual 虚拟花費（最后选择
			self.virtual = data.get("virtual",0)
		
			# cost 花費（其次选择
			self.cost = data.get("cost",[])
		
			# chargeId 直購關聯充值id(优先选择)
			self.chargeId = data.get("chargeId",[])
		

# minggePool
class ResMinggePool(object):
	RES_TABLE = "minggePool"
	__slots__ = ("id","cost","ybNeed","byNeed","owner","LightUpRate","type","pool",)

    def __init__(self):
		
			# id 命格池子表
			self.id = 0
		
			# cost 领取花费
			self.cost = []
		
			# ybNeed 元宝保底
			self.ybNeed = 0
		
			# byNeed 绑元保底
			self.byNeed = 0
		
			# owner 池子归属
			self.owner = 0
		
			# LightUpRate 归属点亮
			self.LightUpRate = []
		
			# type 池子类型
			self.type = 0
		
			# pool 池子
			self.pool = []
		

    def load_from_json(self, data):
		
			# id 命格池子表
			self.id = data.get("id",0)
		
			# cost 领取花费
			self.cost = data.get("cost",[])
		
			# ybNeed 元宝保底
			self.ybNeed = data.get("ybNeed",0)
		
			# byNeed 绑元保底
			self.byNeed = data.get("byNeed",0)
		
			# owner 池子归属
			self.owner = data.get("owner",0)
		
			# LightUpRate 归属点亮
			self.LightUpRate = data.get("LightUpRate",[])
		
			# type 池子类型
			self.type = data.get("type",0)
		
			# pool 池子
			self.pool = data.get("pool",[])
		

# minggeOwner
class ResMinggeOwner(object):
	RES_TABLE = "minggeOwner"
	__slots__ = ("id","icon","cost","canBuy",)

    def __init__(self):
		
			# id 命格池子归属
			self.id = 0
		
			# icon 图标
			self.icon = ""
		
			# cost 点亮消耗
			self.cost = []
		
			# canBuy 可直接点亮
			self.canBuy = 0
		

    def load_from_json(self, data):
		
			# id 命格池子归属
			self.id = data.get("id",0)
		
			# icon 图标
			self.icon = data.get("icon","")
		
			# cost 点亮消耗
			self.cost = data.get("cost",[])
		
			# canBuy 可直接点亮
			self.canBuy = data.get("canBuy",0)
		

# minggeOpen
class ResMinggeOpen(object):
	RES_TABLE = "minggeOpen"
	__slots__ = ("id","level",)

    def __init__(self):
		
			# id 命格位置解锁
			self.id = 0
		
			# level 结伴宠物需求等级
			self.level = 0
		

    def load_from_json(self, data):
		
			# id 命格位置解锁
			self.id = data.get("id",0)
		
			# level 结伴宠物需求等级
			self.level = data.get("level",0)
		

# mingge
class ResMingge(object):
	RES_TABLE = "mingge"
	__slots__ = ("id","name","icon","type","quality","level","needExp","addExp","attr","isShow","page","desc",)

    def __init__(self):
		
			# id 命格表
			self.id = 0
		
			# name 名字
			self.name = ""
		
			# icon 图标
			self.icon = ""
		
			# type 命格类型
			self.type = 0
		
			# quality 命格品质
			self.quality = 0
		
			# level 命格等级
			self.level = 0
		
			# needExp 升级经验
			self.needExp = 0
		
			# addExp 吃掉获得经验
			self.addExp = 0
		
			# attr 属性
			self.attr = []
		
			# isShow 是否展示物品
			self.isShow = 0
		
			# page 分页
			self.page = 0
		
			# desc 描述
			self.desc = ""
		

    def load_from_json(self, data):
		
			# id 命格表
			self.id = data.get("id",0)
		
			# name 名字
			self.name = data.get("name","")
		
			# icon 图标
			self.icon = data.get("icon","")
		
			# type 命格类型
			self.type = data.get("type",0)
		
			# quality 命格品质
			self.quality = data.get("quality",0)
		
			# level 命格等级
			self.level = data.get("level",0)
		
			# needExp 升级经验
			self.needExp = data.get("needExp",0)
		
			# addExp 吃掉获得经验
			self.addExp = data.get("addExp",0)
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# isShow 是否展示物品
			self.isShow = data.get("isShow",0)
		
			# page 分页
			self.page = data.get("page",0)
		
			# desc 描述
			self.desc = data.get("desc","")
		

# meirimiaosha
class ResMeirimiaosha(object):
	RES_TABLE = "meirimiaosha"
	__slots__ = ("id","day","type","reward","limit","cost","chargeId",)

    def __init__(self):
		
			# id 每日秒杀
			self.id = 0
		
			# day 日期
			self.day = ""
		
			# type 系统类型(见注释
			self.type = 0
		
			# reward 獎勵
			self.reward = []
		
			# limit 限購次數0不限制
			self.limit = 0
		
			# cost 花費（其次选择
			self.cost = []
		
			# chargeId 直購關聯充值id(优先选择)
			self.chargeId = []
		

    def load_from_json(self, data):
		
			# id 每日秒杀
			self.id = data.get("id",0)
		
			# day 日期
			self.day = data.get("day","")
		
			# type 系统类型(见注释
			self.type = data.get("type",0)
		
			# reward 獎勵
			self.reward = data.get("reward",[])
		
			# limit 限購次數0不限制
			self.limit = data.get("limit",0)
		
			# cost 花費（其次选择
			self.cost = data.get("cost",[])
		
			# chargeId 直購關聯充值id(优先选择)
			self.chargeId = data.get("chargeId",[])
		

# mazeMap
class ResMazeMap(object):
	RES_TABLE = "mazeMap"
	__slots__ = ("id","mazeId","floor","type","y","x","left","right","up","down","eventList","basetype","boxReward","bossReward","monsterIcon",)

    def __init__(self):
		
			# id 迷宫地图表
			self.id = 0
		
			# mazeId 迷宫期号
			self.mazeId = 0
		
			# floor 层数
			self.floor = 0
		
			# type 格子类型
			self.type = 0
		
			# y y格子坐标
			self.y = 0
		
			# x x格子坐标
			self.x = 0
		
			# left 左联通
			self.left = 0
		
			# right 右联通
			self.right = 0
		
			# up 上联通
			self.up = 0
		
			# down 下联通
			self.down = 0
		
			# eventList 事件链
			self.eventList = []
		
			# basetype 底图类型
			self.basetype = 0
		
			# boxReward 宝箱奖励
			self.boxReward = []
		
			# bossReward 隐藏boss奖励
			self.bossReward = []
		
			# monsterIcon boss形象
			self.monsterIcon = ""
		

    def load_from_json(self, data):
		
			# id 迷宫地图表
			self.id = data.get("id",0)
		
			# mazeId 迷宫期号
			self.mazeId = data.get("mazeId",0)
		
			# floor 层数
			self.floor = data.get("floor",0)
		
			# type 格子类型
			self.type = data.get("type",0)
		
			# y y格子坐标
			self.y = data.get("y",0)
		
			# x x格子坐标
			self.x = data.get("x",0)
		
			# left 左联通
			self.left = data.get("left",0)
		
			# right 右联通
			self.right = data.get("right",0)
		
			# up 上联通
			self.up = data.get("up",0)
		
			# down 下联通
			self.down = data.get("down",0)
		
			# eventList 事件链
			self.eventList = data.get("eventList",[])
		
			# basetype 底图类型
			self.basetype = data.get("basetype",0)
		
			# boxReward 宝箱奖励
			self.boxReward = data.get("boxReward",[])
		
			# bossReward 隐藏boss奖励
			self.bossReward = data.get("bossReward",[])
		
			# monsterIcon boss形象
			self.monsterIcon = data.get("monsterIcon","")
		

# maze
class ResMaze(object):
	RES_TABLE = "maze"
	__slots__ = ("id","openDay","lastDay","taskList","count",)

    def __init__(self):
		
			# id 迷宫期号表
			self.id = 0
		
			# openDay 开服第X天开启
			self.openDay = 0
		
			# lastDay 持续天数
			self.lastDay = 0
		
			# taskList 活动开启就计数的任务
			self.taskList = []
		
			# count 共计层数
			self.count = 0
		

    def load_from_json(self, data):
		
			# id 迷宫期号表
			self.id = data.get("id",0)
		
			# openDay 开服第X天开启
			self.openDay = data.get("openDay",0)
		
			# lastDay 持续天数
			self.lastDay = data.get("lastDay",0)
		
			# taskList 活动开启就计数的任务
			self.taskList = data.get("taskList",[])
		
			# count 共计层数
			self.count = data.get("count",0)
		

# mazeShop
class ResMazeShop(object):
	RES_TABLE = "mazeShop"
	__slots__ = ("id","lastTime","reward1","cost1","chargeId1","reward2","cost2","chargeId2","reward3","cost3","chargeId3",)

    def __init__(self):
		
			# id 迷宫商店表
			self.id = 0
		
			# lastTime 持续时间(秒)
			self.lastTime = 0
		
			# reward1 商品1
			self.reward1 = []
		
			# cost1 商品1花费
			self.cost1 = []
		
			# chargeId1 商品1关联充值id
			self.chargeId1 = []
		
			# reward2 商品2
			self.reward2 = []
		
			# cost2 商品2花费
			self.cost2 = []
		
			# chargeId2 商品2关联充值id
			self.chargeId2 = []
		
			# reward3 商品3
			self.reward3 = []
		
			# cost3 商品3花费
			self.cost3 = []
		
			# chargeId3 商品3关联充值id
			self.chargeId3 = []
		

    def load_from_json(self, data):
		
			# id 迷宫商店表
			self.id = data.get("id",0)
		
			# lastTime 持续时间(秒)
			self.lastTime = data.get("lastTime",0)
		
			# reward1 商品1
			self.reward1 = data.get("reward1",[])
		
			# cost1 商品1花费
			self.cost1 = data.get("cost1",[])
		
			# chargeId1 商品1关联充值id
			self.chargeId1 = data.get("chargeId1",[])
		
			# reward2 商品2
			self.reward2 = data.get("reward2",[])
		
			# cost2 商品2花费
			self.cost2 = data.get("cost2",[])
		
			# chargeId2 商品2关联充值id
			self.chargeId2 = data.get("chargeId2",[])
		
			# reward3 商品3
			self.reward3 = data.get("reward3",[])
		
			# cost3 商品3花费
			self.cost3 = data.get("cost3",[])
		
			# chargeId3 商品3关联充值id
			self.chargeId3 = data.get("chargeId3",[])
		

# mazeEvent
class ResMazeEvent(object):
	RES_TABLE = "mazeEvent"
	__slots__ = ("id","type","mazeShopId","monsterIcon","barrId","taskId","findReward","icon","nameIcon","desc",)

    def __init__(self):
		
			# id 迷宫事件表
			self.id = 0
		
			# type 事件类型
			self.type = 0
		
			# mazeShopId 迷宫商店id
			self.mazeShopId = 0
		
			# monsterIcon 怪物形象
			self.monsterIcon = ""
		
			# barrId 副本id
			self.barrId = 0
		
			# taskId 任务id
			self.taskId = 0
		
			# findReward 发现奖励
			self.findReward = []
		
			# icon 獎勵圖標
			self.icon = ""
		
			# nameIcon 獎勵名稱圖標
			self.nameIcon = ""
		
			# desc 奖励描述
			self.desc = ""
		

    def load_from_json(self, data):
		
			# id 迷宫事件表
			self.id = data.get("id",0)
		
			# type 事件类型
			self.type = data.get("type",0)
		
			# mazeShopId 迷宫商店id
			self.mazeShopId = data.get("mazeShopId",0)
		
			# monsterIcon 怪物形象
			self.monsterIcon = data.get("monsterIcon","")
		
			# barrId 副本id
			self.barrId = data.get("barrId",0)
		
			# taskId 任务id
			self.taskId = data.get("taskId",0)
		
			# findReward 发现奖励
			self.findReward = data.get("findReward",[])
		
			# icon 獎勵圖標
			self.icon = data.get("icon","")
		
			# nameIcon 獎勵名稱圖標
			self.nameIcon = data.get("nameIcon","")
		
			# desc 奖励描述
			self.desc = data.get("desc","")
		

# pvploot
class ResPvploot(object):
	RES_TABLE = "pvploot"
	__slots__ = ("id","name","reward","pos",)

    def __init__(self):
		
			# id 抢夺连胜表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# reward 奖励道具
			self.reward = []
		
			# pos 获取奖励位置
			self.pos = 0
		

    def load_from_json(self, data):
		
			# id 抢夺连胜表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# reward 奖励道具
			self.reward = data.get("reward",[])
		
			# pos 获取奖励位置
			self.pos = data.get("pos",0)
		

# pvprank
class ResPvprank(object):
	RES_TABLE = "pvprank"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id pvp奖排行励表
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id pvp奖排行励表
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# pvpmatch
class ResPvpmatch(object):
	RES_TABLE = "pvpmatch"
	__slots__ = ("id","startVal","endVal","downVal","downNum","upVal","upNum","valLimit",)

    def __init__(self):
		
			# id pvp匹配表
			self.id = 0
		
			# startVal 战力段起始值
			self.startVal = 0
		
			# endVal 战力段起始值
			self.endVal = 0
		
			# downVal 下限浮动(万分比)
			self.downVal = 0
		
			# downNum 下限人数
			self.downNum = 0
		
			# upVal 上限浮动(万分比)
			self.upVal = 0
		
			# upNum 上限人数
			self.upNum = 0
		
			# valLimit 浮动最大限制(万分比)
			self.valLimit = 0
		

    def load_from_json(self, data):
		
			# id pvp匹配表
			self.id = data.get("id",0)
		
			# startVal 战力段起始值
			self.startVal = data.get("startVal",0)
		
			# endVal 战力段起始值
			self.endVal = data.get("endVal",0)
		
			# downVal 下限浮动(万分比)
			self.downVal = data.get("downVal",0)
		
			# downNum 下限人数
			self.downNum = data.get("downNum",0)
		
			# upVal 上限浮动(万分比)
			self.upVal = data.get("upVal",0)
		
			# upNum 上限人数
			self.upNum = data.get("upNum",0)
		
			# valLimit 浮动最大限制(万分比)
			self.valLimit = data.get("valLimit",0)
		

# maincityTopBtn
class ResMaincityTopBtn(object):
	RES_TABLE = "maincityTopBtn"
	__slots__ = ("id","sort","name",)

    def __init__(self):
		
			# id 需要顺下去排不可插、乱
			self.id = 0
		
			# sort 排序数值大的走前面
			self.sort = 0
		
			# name 按钮名字(策划勿动
			self.name = ""
		

    def load_from_json(self, data):
		
			# id 需要顺下去排不可插、乱
			self.id = data.get("id",0)
		
			# sort 排序数值大的走前面
			self.sort = data.get("sort",0)
		
			# name 按钮名字(策划勿动
			self.name = data.get("name","")
		

# common
class ResCommon(object):
	RES_TABLE = "common"
	__slots__ = ("key","i","s","arraystring2","arrayint1","arrayint2",)

    def __init__(self):
		
			# key 全局数据表
			self.key = ""
		
			# i 正整数
			self.i = 0
		
			# s 字符串
			self.s = ""
		
			# arraystring2 二维数组（字符串）
			self.arraystring2 = []
		
			# arrayint1 一维数组（整形）
			self.arrayint1 = []
		
			# arrayint2 二维数组（整形）
			self.arrayint2 = []
		

    def load_from_json(self, data):
		
			# key 全局数据表
			self.key = data.get("key","")
		
			# i 正整数
			self.i = data.get("i",0)
		
			# s 字符串
			self.s = data.get("s","")
		
			# arraystring2 二维数组（字符串）
			self.arraystring2 = data.get("arraystring2",[])
		
			# arrayint1 一维数组（整形）
			self.arrayint1 = data.get("arrayint1",[])
		
			# arrayint2 二维数组（整形）
			self.arrayint2 = data.get("arrayint2",[])
		

# renwudajihuan
class ResRenwudajihuan(object):
	RES_TABLE = "renwudajihuan"
	__slots__ = ("day","big","boxReward","reward","reward1","reward2","reward3","reward4","reward5","task1","task2","task3","task4","task5",)

    def __init__(self):
		
			# day 日期
			self.day = ""
		
			# big 大奖励表id
			self.big = 0
		
			# boxReward 奖励客户端显示宝箱奖励
			self.boxReward = []
		
			# reward 小奖励表id
			self.reward = []
		
			# reward1 奖励客户端显示任务栏奖励
			self.reward1 = []
		
			# reward2 奖励客户端显示任务栏奖励
			self.reward2 = []
		
			# reward3 奖励客户端显示任务栏奖励
			self.reward3 = []
		
			# reward4 奖励客户端显示任务栏奖励
			self.reward4 = []
		
			# reward5 奖励客户端显示任务栏奖励
			self.reward5 = []
		
			# task1 任务1
			self.task1 = []
		
			# task2 任务2
			self.task2 = []
		
			# task3 任务3
			self.task3 = []
		
			# task4 任务4
			self.task4 = []
		
			# task5 任务5
			self.task5 = []
		

    def load_from_json(self, data):
		
			# day 日期
			self.day = data.get("day","")
		
			# big 大奖励表id
			self.big = data.get("big",0)
		
			# boxReward 奖励客户端显示宝箱奖励
			self.boxReward = data.get("boxReward",[])
		
			# reward 小奖励表id
			self.reward = data.get("reward",[])
		
			# reward1 奖励客户端显示任务栏奖励
			self.reward1 = data.get("reward1",[])
		
			# reward2 奖励客户端显示任务栏奖励
			self.reward2 = data.get("reward2",[])
		
			# reward3 奖励客户端显示任务栏奖励
			self.reward3 = data.get("reward3",[])
		
			# reward4 奖励客户端显示任务栏奖励
			self.reward4 = data.get("reward4",[])
		
			# reward5 奖励客户端显示任务栏奖励
			self.reward5 = data.get("reward5",[])
		
			# task1 任务1
			self.task1 = data.get("task1",[])
		
			# task2 任务2
			self.task2 = data.get("task2",[])
		
			# task3 任务3
			self.task3 = data.get("task3",[])
		
			# task4 任务4
			self.task4 = data.get("task4",[])
		
			# task5 任务5
			self.task5 = data.get("task5",[])
		

# task
class ResTask(object):
	RES_TABLE = "task"
	__slots__ = ("id","group","conditon","nextId","type","guideId","num","arg1","arg2","rewardInt","finishReward","bussid",)

    def __init__(self):
		
			# id 任务表
			self.id = 0
		
			# group 任务组id
			self.group = 0
		
			# conditon 领取条件
			self.conditon = []
		
			# nextId 下一个任务id
			self.nextId = 0
		
			# type 类型
			self.type = 0
		
			# guideId 引导id
			self.guideId = 0
		
			# num 任务进度
			self.num = 0
		
			# arg1 参数1
			self.arg1 = ""
		
			# arg2 参数2
			self.arg2 = ""
		
			# rewardInt 进度奖励(正整数）
			self.rewardInt = 0
		
			# finishReward 整体完成奖励
			self.finishReward = []
		
			# bussid 业务参数
			self.bussid = 0
		

    def load_from_json(self, data):
		
			# id 任务表
			self.id = data.get("id",0)
		
			# group 任务组id
			self.group = data.get("group",0)
		
			# conditon 领取条件
			self.conditon = data.get("conditon",[])
		
			# nextId 下一个任务id
			self.nextId = data.get("nextId",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# guideId 引导id
			self.guideId = data.get("guideId",0)
		
			# num 任务进度
			self.num = data.get("num",0)
		
			# arg1 参数1
			self.arg1 = data.get("arg1","")
		
			# arg2 参数2
			self.arg2 = data.get("arg2","")
		
			# rewardInt 进度奖励(正整数）
			self.rewardInt = data.get("rewardInt",0)
		
			# finishReward 整体完成奖励
			self.finishReward = data.get("finishReward",[])
		
			# bussid 业务参数
			self.bussid = data.get("bussid",0)
		

# xianqi
class ResXianqi(object):
	RES_TABLE = "xianqi"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","jjreward","offX","offY","scale","effectTip",)

    def __init__(self):
		
			# id 仙器表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# effectTip 特效升级提示
			self.effectTip = ""
		

    def load_from_json(self, data):
		
			# id 仙器表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# effectTip 特效升级提示
			self.effectTip = data.get("effectTip","")
		

# zkfm
class ResZkfm(object):
	RES_TABLE = "zkfm"
	__slots__ = ("id","minLv","maxLv","reward","zhudaoxunli",)

    def __init__(self):
		
			# id 钟馗伏魔表
			self.id = 0
		
			# minLv 最小等级
			self.minLv = 0
		
			# maxLv 最大等级
			self.maxLv = 0
		
			# reward 奖励
			self.reward = []
		
			# zhudaoxunli 诸岛巡礼加点
			self.zhudaoxunli = 0
		

    def load_from_json(self, data):
		
			# id 钟馗伏魔表
			self.id = data.get("id",0)
		
			# minLv 最小等级
			self.minLv = data.get("minLv",0)
		
			# maxLv 最大等级
			self.maxLv = data.get("maxLv",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# zhudaoxunli 诸岛巡礼加点
			self.zhudaoxunli = data.get("zhudaoxunli",0)
		

# rchyWeekReward
class ResRchyWeekReward(object):
	RES_TABLE = "rchyWeekReward"
	__slots__ = ("id","reward","target",)

    def __init__(self):
		
			# id 日常活跃周奖励表
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# target 条件
			self.target = 0
		

    def load_from_json(self, data):
		
			# id 日常活跃周奖励表
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# target 条件
			self.target = data.get("target",0)
		

# zkfmboss
class ResZkfmboss(object):
	RES_TABLE = "zkfmboss"
	__slots__ = ("id","minLv","maxLv","pos","mstId","mstIdScene","barrId",)

    def __init__(self):
		
			# id 钟馗伏魔boss表
			self.id = 0
		
			# minLv 最小等级
			self.minLv = 0
		
			# maxLv 最大等级
			self.maxLv = 0
		
			# pos 位置
			self.pos = 0
		
			# mstId boss怪物id-ui界面用
			self.mstId = 0
		
			# mstIdScene boss怪物id-场景用
			self.mstIdScene = 0
		
			# barrId 副本id
			self.barrId = 0
		

    def load_from_json(self, data):
		
			# id 钟馗伏魔boss表
			self.id = data.get("id",0)
		
			# minLv 最小等级
			self.minLv = data.get("minLv",0)
		
			# maxLv 最大等级
			self.maxLv = data.get("maxLv",0)
		
			# pos 位置
			self.pos = data.get("pos",0)
		
			# mstId boss怪物id-ui界面用
			self.mstId = data.get("mstId",0)
		
			# mstIdScene boss怪物id-场景用
			self.mstIdScene = data.get("mstIdScene",0)
		
			# barrId 副本id
			self.barrId = data.get("barrId",0)
		

# zdll
class ResZdll(object):
	RES_TABLE = "zdll"
	__slots__ = ("id","minLv","maxLv","reward","zhudaoxunli",)

    def __init__(self):
		
			# id 组队历练表
			self.id = 0
		
			# minLv 最小等级
			self.minLv = 0
		
			# maxLv 最大等级
			self.maxLv = 0
		
			# reward 奖励
			self.reward = []
		
			# zhudaoxunli 诸岛巡礼加点
			self.zhudaoxunli = 0
		

    def load_from_json(self, data):
		
			# id 组队历练表
			self.id = data.get("id",0)
		
			# minLv 最小等级
			self.minLv = data.get("minLv",0)
		
			# maxLv 最大等级
			self.maxLv = data.get("maxLv",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# zhudaoxunli 诸岛巡礼加点
			self.zhudaoxunli = data.get("zhudaoxunli",0)
		

# mr300
class ResMr300(object):
	RES_TABLE = "mr300"
	__slots__ = ("id","kill","minLv","maxLv","reward","zhudaoxunli",)

    def __init__(self):
		
			# id 每日300表
			self.id = 0
		
			# kill 需求次数
			self.kill = 0
		
			# minLv 最小等级
			self.minLv = 0
		
			# maxLv 最大等级
			self.maxLv = 0
		
			# reward 奖励
			self.reward = []
		
			# zhudaoxunli 诸岛巡礼加点
			self.zhudaoxunli = 0
		

    def load_from_json(self, data):
		
			# id 每日300表
			self.id = data.get("id",0)
		
			# kill 需求次数
			self.kill = data.get("kill",0)
		
			# minLv 最小等级
			self.minLv = data.get("minLv",0)
		
			# maxLv 最大等级
			self.maxLv = data.get("maxLv",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# zhudaoxunli 诸岛巡礼加点
			self.zhudaoxunli = data.get("zhudaoxunli",0)
		

# rchyDayReward
class ResRchyDayReward(object):
	RES_TABLE = "rchyDayReward"
	__slots__ = ("id","reward","target","zhudaoxunli",)

    def __init__(self):
		
			# id 日常活跃日奖励表
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# target 条件
			self.target = 0
		
			# zhudaoxunli 诸岛巡礼加点
			self.zhudaoxunli = 0
		

    def load_from_json(self, data):
		
			# id 日常活跃日奖励表
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# target 条件
			self.target = data.get("target",0)
		
			# zhudaoxunli 诸岛巡礼加点
			self.zhudaoxunli = data.get("zhudaoxunli",0)
		

# xyll
class ResXyll(object):
	RES_TABLE = "xyll"
	__slots__ = ("id","exp","attr","reward",)

    def __init__(self):
		
			# id 西游历练表
			self.id = 0
		
			# exp 升级经验
			self.exp = 0
		
			# attr 增加属性
			self.attr = []
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 西游历练表
			self.id = data.get("id",0)
		
			# exp 升级经验
			self.exp = data.get("exp",0)
		
			# attr 增加属性
			self.attr = data.get("attr",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# shoulinggongming
class ResShoulinggongming(object):
	RES_TABLE = "shoulinggongming"
	__slots__ = ("id","oriType","idx","weight","attr","iconImg","name","desc",)

    def __init__(self):
		
			# id 共鸣权重
			self.id = 0
		
			# oriType 定位类型
			self.oriType = 0
		
			# idx 格子012
			self.idx = 0
		
			# weight 权重
			self.weight = 0
		
			# attr 属性
			self.attr = []
		
			# iconImg 图标
			self.iconImg = ""
		
			# name 名字
			self.name = ""
		
			# desc 描述
			self.desc = ""
		

    def load_from_json(self, data):
		
			# id 共鸣权重
			self.id = data.get("id",0)
		
			# oriType 定位类型
			self.oriType = data.get("oriType",0)
		
			# idx 格子012
			self.idx = data.get("idx",0)
		
			# weight 权重
			self.weight = data.get("weight",0)
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# iconImg 图标
			self.iconImg = data.get("iconImg","")
		
			# name 名字
			self.name = data.get("name","")
		
			# desc 描述
			self.desc = data.get("desc","")
		

# shouhun
class ResShouhun(object):
	RES_TABLE = "shouhun"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","actSkill","jjreward","offX","offY","scale",)

    def __init__(self):
		
			# id 兽魂表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# actSkill 激活技能
			self.actSkill = 0
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		

    def load_from_json(self, data):
		
			# id 兽魂表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# actSkill 激活技能
			self.actSkill = data.get("actSkill",0)
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		

# shouhunskill
class ResShouhunskill(object):
	RES_TABLE = "shouhunskill"
	__slots__ = ("id","skillId","lv","name","cost","attr","icon",)

    def __init__(self):
		
			# id 兽魂技能表
			self.id = 0
		
			# skillId 技能id
			self.skillId = 0
		
			# lv 技能等级
			self.lv = 0
		
			# name 名称
			self.name = ""
		
			# cost 升级消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		
			# icon 图标
			self.icon = ""
		

    def load_from_json(self, data):
		
			# id 兽魂技能表
			self.id = data.get("id",0)
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		
			# lv 技能等级
			self.lv = data.get("lv",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# cost 升级消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# icon 图标
			self.icon = data.get("icon","")
		

# discountShopData
class ResDiscountShopData(object):
	RES_TABLE = "discountShopData"
	__slots__ = ("id","limit","reward","cost","discount","rate",)

    def __init__(self):
		
			# id 限时折扣商店物品
			self.id = 0
		
			# limit 限购次数
			self.limit = 0
		
			# reward 奖励
			self.reward = []
		
			# cost 原价
			self.cost = []
		
			# discount 折后价
			self.discount = []
		
			# rate 权重
			self.rate = 0
		

    def load_from_json(self, data):
		
			# id 限时折扣商店物品
			self.id = data.get("id",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cost 原价
			self.cost = data.get("cost",[])
		
			# discount 折后价
			self.discount = data.get("discount",[])
		
			# rate 权重
			self.rate = data.get("rate",0)
		

# yishouShop
class ResYishouShop(object):
	RES_TABLE = "yishouShop"
	__slots__ = ("id","cycNo","reward","cost","discount","discount2","cost2","limit","reset","rate",)

    def __init__(self):
		
			# id 刷新商店
			self.id = 0
		
			# cycNo 期号
			self.cycNo = 0
		
			# reward 奖励
			self.reward = []
		
			# cost 原价
			self.cost = []
		
			# discount 折后价
			self.discount = []
		
			# discount2 折上折
			self.discount2 = []
		
			# cost2 代币
			self.cost2 = []
		
			# limit 周期内出现次数
			self.limit = 0
		
			# reset 重置方式
			self.reset = 0
		
			# rate 权重
			self.rate = 0
		

    def load_from_json(self, data):
		
			# id 刷新商店
			self.id = data.get("id",0)
		
			# cycNo 期号
			self.cycNo = data.get("cycNo",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cost 原价
			self.cost = data.get("cost",[])
		
			# discount 折后价
			self.discount = data.get("discount",[])
		
			# discount2 折上折
			self.discount2 = data.get("discount2",[])
		
			# cost2 代币
			self.cost2 = data.get("cost2",[])
		
			# limit 周期内出现次数
			self.limit = data.get("limit",0)
		
			# reset 重置方式
			self.reset = data.get("reset",0)
		
			# rate 权重
			self.rate = data.get("rate",0)
		

# refreshShop
class ResRefreshShop(object):
	RES_TABLE = "refreshShop"
	__slots__ = ("id","cycNo","reward","cost","discount","limit","reset","rate",)

    def __init__(self):
		
			# id 刷新商店
			self.id = 0
		
			# cycNo 期号
			self.cycNo = 0
		
			# reward 奖励
			self.reward = []
		
			# cost 原价
			self.cost = []
		
			# discount 折后价
			self.discount = []
		
			# limit 周期内出现次数
			self.limit = 0
		
			# reset 重置方式
			self.reset = 0
		
			# rate 权重
			self.rate = 0
		

    def load_from_json(self, data):
		
			# id 刷新商店
			self.id = data.get("id",0)
		
			# cycNo 期号
			self.cycNo = data.get("cycNo",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cost 原价
			self.cost = data.get("cost",[])
		
			# discount 折后价
			self.discount = data.get("discount",[])
		
			# limit 周期内出现次数
			self.limit = data.get("limit",0)
		
			# reset 重置方式
			self.reset = data.get("reset",0)
		
			# rate 权重
			self.rate = data.get("rate",0)
		

# discountShop
class ResDiscountShop(object):
	RES_TABLE = "discountShop"
	__slots__ = ("id","startTime","endTime","itemList",)

    def __init__(self):
		
			# id 限时折扣商店
			self.id = 0
		
			# startTime 开启日期
			self.startTime = ""
		
			# endTime 结束日期
			self.endTime = ""
		
			# itemList 物品列表
			self.itemList = []
		

    def load_from_json(self, data):
		
			# id 限时折扣商店
			self.id = data.get("id",0)
		
			# startTime 开启日期
			self.startTime = data.get("startTime","")
		
			# endTime 结束日期
			self.endTime = data.get("endTime","")
		
			# itemList 物品列表
			self.itemList = data.get("itemList",[])
		

# petShop
class ResPetShop(object):
	RES_TABLE = "petShop"
	__slots__ = ("id","cycNo","reward","cost","discount","limit","reset","rate",)

    def __init__(self):
		
			# id 刷新商店
			self.id = 0
		
			# cycNo 期号
			self.cycNo = 0
		
			# reward 奖励
			self.reward = []
		
			# cost 原价
			self.cost = []
		
			# discount 折后价
			self.discount = []
		
			# limit 周期内出现次数
			self.limit = 0
		
			# reset 重置方式
			self.reset = 0
		
			# rate 权重
			self.rate = 0
		

    def load_from_json(self, data):
		
			# id 刷新商店
			self.id = data.get("id",0)
		
			# cycNo 期号
			self.cycNo = data.get("cycNo",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cost 原价
			self.cost = data.get("cost",[])
		
			# discount 折后价
			self.discount = data.get("discount",[])
		
			# limit 周期内出现次数
			self.limit = data.get("limit",0)
		
			# reset 重置方式
			self.reset = data.get("reset",0)
		
			# rate 权重
			self.rate = data.get("rate",0)
		

# superRebateShop
class ResSuperRebateShop(object):
	RES_TABLE = "superRebateShop"
	__slots__ = ("id","limit","reward","cost",)

    def __init__(self):
		
			# id 超级返利
			self.id = 0
		
			# limit 限购次数
			self.limit = 0
		
			# reward 奖励
			self.reward = []
		
			# cost 消耗
			self.cost = 0
		

    def load_from_json(self, data):
		
			# id 超级返利
			self.id = data.get("id",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# cost 消耗
			self.cost = data.get("cost",0)
		

# shopQuick
class ResShopQuick(object):
	RES_TABLE = "shopQuick"
	__slots__ = ("id","shopId","link",)

    def __init__(self):
		
			# id 快速购买表
			self.id = 0
		
			# shopId 关联的商店表Id
			self.shopId = 0
		
			# link 途径id列表
			self.link = []
		

    def load_from_json(self, data):
		
			# id 快速购买表
			self.id = data.get("id",0)
		
			# shopId 关联的商店表Id
			self.shopId = data.get("shopId",0)
		
			# link 途径id列表
			self.link = data.get("link",[])
		

# ChristmasLimitReward
class ResChristmasLimitReward(object):
	RES_TABLE = "ChristmasLimitReward"
	__slots__ = ("id","titleIcon","giftIcon","reward","limit","costOld","cost","chargeOld","chargeId",)

    def __init__(self):
		
			# id 限購禮包
			self.id = 0
		
			# titleIcon 名稱圖標
			self.titleIcon = ""
		
			# giftIcon 禮包圖標
			self.giftIcon = ""
		
			# reward 獎勵
			self.reward = []
		
			# limit 限購次數
			self.limit = 0
		
			# costOld 原價1
			self.costOld = 0
		
			# cost 花費(有花费就不走充值)
			self.cost = []
		
			# chargeOld 原價2
			self.chargeOld = 0
		
			# chargeId 直購關聯充值id(有花费就不走充值)
			self.chargeId = []
		

    def load_from_json(self, data):
		
			# id 限購禮包
			self.id = data.get("id",0)
		
			# titleIcon 名稱圖標
			self.titleIcon = data.get("titleIcon","")
		
			# giftIcon 禮包圖標
			self.giftIcon = data.get("giftIcon","")
		
			# reward 獎勵
			self.reward = data.get("reward",[])
		
			# limit 限購次數
			self.limit = data.get("limit",0)
		
			# costOld 原價1
			self.costOld = data.get("costOld",0)
		
			# cost 花費(有花费就不走充值)
			self.cost = data.get("cost",[])
		
			# chargeOld 原價2
			self.chargeOld = data.get("chargeOld",0)
		
			# chargeId 直購關聯充值id(有花费就不走充值)
			self.chargeId = data.get("chargeId",[])
		

# ChristmasActive
class ResChristmasActive(object):
	RES_TABLE = "ChristmasActive"
	__slots__ = ("id","Open","End","TacoFace","reward","skinId",)

    def __init__(self):
		
			# id 新开服狂欢期号表
			self.id = 0
		
			# Open 开启时间
			self.Open = ""
		
			# End 结束时间
			self.End = ""
		
			# TacoFace 每日打脸次数
			self.TacoFace = 0
		
			# reward 獎勵
			self.reward = []
		
			# skinId 皮肤Id0或不填是圣诞1除夕
			self.skinId = 0
		

    def load_from_json(self, data):
		
			# id 新开服狂欢期号表
			self.id = data.get("id",0)
		
			# Open 开启时间
			self.Open = data.get("Open","")
		
			# End 结束时间
			self.End = data.get("End","")
		
			# TacoFace 每日打脸次数
			self.TacoFace = data.get("TacoFace",0)
		
			# reward 獎勵
			self.reward = data.get("reward",[])
		
			# skinId 皮肤Id0或不填是圣诞1除夕
			self.skinId = data.get("skinId",0)
		

# ChristmasDrawCost
class ResChristmasDrawCost(object):
	RES_TABLE = "ChristmasDrawCost"
	__slots__ = ("id","needCost","reward","mailreward","weight1","weight2","weight3","weight4","weight5","weight6","weight7","weight8","weight9",)

    def __init__(self):
		
			# id 奖励格子
			self.id = 0
		
			# needCost 消耗跟格子无关
			self.needCost = []
		
			# reward 奖励对应格子奖励
			self.reward = []
		
			# mailreward 圣诞老人的祝福几天
			self.mailreward = 0
		
			# weight1 权重1
			self.weight1 = 0
		
			# weight2 权重2
			self.weight2 = 0
		
			# weight3 权重3
			self.weight3 = 0
		
			# weight4 权重4
			self.weight4 = 0
		
			# weight5 权重5
			self.weight5 = 0
		
			# weight6 权重6
			self.weight6 = 0
		
			# weight7 权重7
			self.weight7 = 0
		
			# weight8 权重8
			self.weight8 = 0
		
			# weight9 权重9
			self.weight9 = 0
		

    def load_from_json(self, data):
		
			# id 奖励格子
			self.id = data.get("id",0)
		
			# needCost 消耗跟格子无关
			self.needCost = data.get("needCost",[])
		
			# reward 奖励对应格子奖励
			self.reward = data.get("reward",[])
		
			# mailreward 圣诞老人的祝福几天
			self.mailreward = data.get("mailreward",0)
		
			# weight1 权重1
			self.weight1 = data.get("weight1",0)
		
			# weight2 权重2
			self.weight2 = data.get("weight2",0)
		
			# weight3 权重3
			self.weight3 = data.get("weight3",0)
		
			# weight4 权重4
			self.weight4 = data.get("weight4",0)
		
			# weight5 权重5
			self.weight5 = data.get("weight5",0)
		
			# weight6 权重6
			self.weight6 = data.get("weight6",0)
		
			# weight7 权重7
			self.weight7 = data.get("weight7",0)
		
			# weight8 权重8
			self.weight8 = data.get("weight8",0)
		
			# weight9 权重9
			self.weight9 = data.get("weight9",0)
		

# shop
class ResShop(object):
	RES_TABLE = "shop"
	__slots__ = ("id","type","viewCond","mustShow","buyCond","limitNum","refCycle","odds","itemId","num","costId","discount","discount2","vipDiscount","costOld","costValue","showXXShop","hidereward",)

    def __init__(self):
		
			# id 商店表
			self.id = 0
		
			# type 标签类型
			self.type = 0
		
			# viewCond 显示条件
			self.viewCond = 0
		
			# mustShow 折扣商店一直显示
			self.mustShow = 0
		
			# buyCond 购买条件
			self.buyCond = []
		
			# limitNum 限购数量
			self.limitNum = []
		
			# refCycle 刷新周期
			self.refCycle = 0
		
			# odds 刷新概率
			self.odds = 0
		
			# itemId 物品ID
			self.itemId = 0
		
			# num 数量
			self.num = 0
		
			# costId 消耗物品id
			self.costId = 0
		
			# discount 折扣
			self.discount = 0
		
			# discount2 折扣2
			self.discount2 = 0
		
			# vipDiscount 是否vip打折
			self.vipDiscount = 0
		
			# costOld 原价
			self.costOld = 0
		
			# costValue 消耗值
			self.costValue = 0
		
			# showXXShop xx商店显示
			self.showXXShop = 0
		
			# hidereward 隐藏赠送
			self.hidereward = []
		

    def load_from_json(self, data):
		
			# id 商店表
			self.id = data.get("id",0)
		
			# type 标签类型
			self.type = data.get("type",0)
		
			# viewCond 显示条件
			self.viewCond = data.get("viewCond",0)
		
			# mustShow 折扣商店一直显示
			self.mustShow = data.get("mustShow",0)
		
			# buyCond 购买条件
			self.buyCond = data.get("buyCond",[])
		
			# limitNum 限购数量
			self.limitNum = data.get("limitNum",[])
		
			# refCycle 刷新周期
			self.refCycle = data.get("refCycle",0)
		
			# odds 刷新概率
			self.odds = data.get("odds",0)
		
			# itemId 物品ID
			self.itemId = data.get("itemId",0)
		
			# num 数量
			self.num = data.get("num",0)
		
			# costId 消耗物品id
			self.costId = data.get("costId",0)
		
			# discount 折扣
			self.discount = data.get("discount",0)
		
			# discount2 折扣2
			self.discount2 = data.get("discount2",0)
		
			# vipDiscount 是否vip打折
			self.vipDiscount = data.get("vipDiscount",0)
		
			# costOld 原价
			self.costOld = data.get("costOld",0)
		
			# costValue 消耗值
			self.costValue = data.get("costValue",0)
		
			# showXXShop xx商店显示
			self.showXXShop = data.get("showXXShop",0)
		
			# hidereward 隐藏赠送
			self.hidereward = data.get("hidereward",[])
		

# attrbute
class ResAttrbute(object):
	RES_TABLE = "attrbute"
	__slots__ = ("key","name","name2","name4","name3","color","sortValue","ratio","isPercent","isPercent2","dpoint","rate","inheritance",)

    def __init__(self):
		
			# key 属性定义key
			self.key = ""
		
			# name 属性名字
			self.name = ""
		
			# name2 属性名字4个字
			self.name2 = ""
		
			# name4 属性名字宠物界面专用
			self.name4 = ""
		
			# name3 用于战斗buff提示
			self.name3 = ""
		
			# color 属性颜色
			self.color = ""
		
			# sortValue 属性排列
			self.sortValue = 0
		
			# ratio 战斗力系数
			self.ratio = 0
		
			# isPercent 是否万分比显示
			self.isPercent = 0
		
			# isPercent2 是否百分百显示
			self.isPercent2 = 0
		
			# dpoint 前端显示保留小数点位数
			self.dpoint = 0
		
			# rate 描述转化比率
			self.rate = 0
		
			# inheritance 属性继承比例
			self.inheritance = []
		

    def load_from_json(self, data):
		
			# key 属性定义key
			self.key = data.get("key","")
		
			# name 属性名字
			self.name = data.get("name","")
		
			# name2 属性名字4个字
			self.name2 = data.get("name2","")
		
			# name4 属性名字宠物界面专用
			self.name4 = data.get("name4","")
		
			# name3 用于战斗buff提示
			self.name3 = data.get("name3","")
		
			# color 属性颜色
			self.color = data.get("color","")
		
			# sortValue 属性排列
			self.sortValue = data.get("sortValue",0)
		
			# ratio 战斗力系数
			self.ratio = data.get("ratio",0)
		
			# isPercent 是否万分比显示
			self.isPercent = data.get("isPercent",0)
		
			# isPercent2 是否百分百显示
			self.isPercent2 = data.get("isPercent2",0)
		
			# dpoint 前端显示保留小数点位数
			self.dpoint = data.get("dpoint",0)
		
			# rate 描述转化比率
			self.rate = data.get("rate",0)
		
			# inheritance 属性继承比例
			self.inheritance = data.get("inheritance",[])
		

# fashion
class ResFashion(object):
	RES_TABLE = "fashion"
	__slots__ = ("id","type","typeName","bg","attr","ui","cost","offX","offY","scale",)

    def __init__(self):
		
			# id 时装表
			self.id = 0
		
			# type 类型
			self.type = 0
		
			# typeName 类型名
			self.typeName = ""
		
			# bg 底图
			self.bg = ""
		
			# attr 属性
			self.attr = []
		
			# ui 是否界面显示
			self.ui = 0
		
			# cost 消耗道具
			self.cost = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		

    def load_from_json(self, data):
		
			# id 时装表
			self.id = data.get("id",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# typeName 类型名
			self.typeName = data.get("typeName","")
		
			# bg 底图
			self.bg = data.get("bg","")
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# ui 是否界面显示
			self.ui = data.get("ui",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		

# luckyleyuan
class ResLuckyleyuan(object):
	RES_TABLE = "luckyleyuan"
	__slots__ = ("id","name","startTime","endTime","icon","leyuanPetList","mapId",)

    def __init__(self):
		
			# id 幸运乐园表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# startTime 开启日期
			self.startTime = ""
		
			# endTime 结束日期
			self.endTime = ""
		
			# icon 图标
			self.icon = ""
		
			# leyuanPetList 可能遇到的幸运乐园宠物id
			self.leyuanPetList = []
		
			# mapId 场景id
			self.mapId = 0
		

    def load_from_json(self, data):
		
			# id 幸运乐园表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# startTime 开启日期
			self.startTime = data.get("startTime","")
		
			# endTime 结束日期
			self.endTime = data.get("endTime","")
		
			# icon 图标
			self.icon = data.get("icon","")
		
			# leyuanPetList 可能遇到的幸运乐园宠物id
			self.leyuanPetList = data.get("leyuanPetList",[])
		
			# mapId 场景id
			self.mapId = data.get("mapId",0)
		

# shahuleyuanTime
class ResShahuleyuanTime(object):
	RES_TABLE = "shahuleyuanTime"
	__slots__ = ("id","openList",)

    def __init__(self):
		
			# id 沙狐乐园时间表
			self.id = 0
		
			# openList 开放乐园id
			self.openList = []
		

    def load_from_json(self, data):
		
			# id 沙狐乐园时间表
			self.id = data.get("id",0)
		
			# openList 开放乐园id
			self.openList = data.get("openList",[])
		

# shahuleyuanShow
class ResShahuleyuanShow(object):
	RES_TABLE = "shahuleyuanShow"
	__slots__ = ("id","tweenCount","type","desc",)

    def __init__(self):
		
			# id 沙狐乐园显示表
			self.id = 0
		
			# tweenCount 精灵球摇动次数
			self.tweenCount = 0
		
			# type 传参类型
			self.type = []
		
			# desc 提示标语
			self.desc = []
		

    def load_from_json(self, data):
		
			# id 沙狐乐园显示表
			self.id = data.get("id",0)
		
			# tweenCount 精灵球摇动次数
			self.tweenCount = data.get("tweenCount",0)
		
			# type 传参类型
			self.type = data.get("type",[])
		
			# desc 提示标语
			self.desc = data.get("desc",[])
		

# shahuleyuanGift
class ResShahuleyuanGift(object):
	RES_TABLE = "shahuleyuanGift"
	__slots__ = ("id","name","limitType","limit","chargeId","reward","value","img",)

    def __init__(self):
		
			# id 沙狐乐园礼包表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# limitType 限购类型
			self.limitType = 0
		
			# limit 限购次数
			self.limit = 0
		
			# chargeId 关联充值id
			self.chargeId = []
		
			# reward 奖励
			self.reward = []
		
			# value 价值
			self.value = 0
		
			# img 底图
			self.img = ""
		

    def load_from_json(self, data):
		
			# id 沙狐乐园礼包表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# limitType 限购类型
			self.limitType = data.get("limitType",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# chargeId 关联充值id
			self.chargeId = data.get("chargeId",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# value 价值
			self.value = data.get("value",0)
		
			# img 底图
			self.img = data.get("img","")
		

# shahuleyuanStep
class ResShahuleyuanStep(object):
	RES_TABLE = "shahuleyuanStep"
	__slots__ = ("id","step","petPool",)

    def __init__(self):
		
			# id 沙狐乐园步数表
			self.id = 0
		
			# step 步数
			self.step = 0
		
			# petPool 宠物池子
			self.petPool = []
		

    def load_from_json(self, data):
		
			# id 沙狐乐园步数表
			self.id = data.get("id",0)
		
			# step 步数
			self.step = data.get("step",0)
		
			# petPool 宠物池子
			self.petPool = data.get("petPool",[])
		

# shahuleyuanPet
class ResShahuleyuanPet(object):
	RES_TABLE = "shahuleyuanPet"
	__slots__ = ("id","petId","evolveLv","shape","meetAnim","initialPatience","maxPatience","feeding","useBall","normal","luckyNormal","advanced","luckyAdvanced","master","luckyMaster","sweet","luckySweet",)

    def __init__(self):
		
			# id 沙狐乐园宠物表
			self.id = 0
		
			# petId 宠物id
			self.petId = 0
		
			# evolveLv 宠物进化阶数
			self.evolveLv = 0
		
			# shape 所属形状
			self.shape = 0
		
			# meetAnim 遇见动画
			self.meetAnim = 0
		
			# initialPatience 初始耐心
			self.initialPatience = []
		
			# maxPatience 上限耐心
			self.maxPatience = 0
		
			# feeding 喂食
			self.feeding = []
		
			# useBall 用球
			self.useBall = []
		
			# normal 普通球奖励
			self.normal = []
		
			# luckyNormal 普通球幸运奖励
			self.luckyNormal = []
		
			# advanced 高级球奖励
			self.advanced = []
		
			# luckyAdvanced 高级球幸运奖励
			self.luckyAdvanced = []
		
			# master 大师球奖励
			self.master = []
		
			# luckyMaster 大师球幸运奖励
			self.luckyMaster = []
		
			# sweet 甜蜜球奖励
			self.sweet = []
		
			# luckySweet 甜蜜球幸运奖励
			self.luckySweet = []
		

    def load_from_json(self, data):
		
			# id 沙狐乐园宠物表
			self.id = data.get("id",0)
		
			# petId 宠物id
			self.petId = data.get("petId",0)
		
			# evolveLv 宠物进化阶数
			self.evolveLv = data.get("evolveLv",0)
		
			# shape 所属形状
			self.shape = data.get("shape",0)
		
			# meetAnim 遇见动画
			self.meetAnim = data.get("meetAnim",0)
		
			# initialPatience 初始耐心
			self.initialPatience = data.get("initialPatience",[])
		
			# maxPatience 上限耐心
			self.maxPatience = data.get("maxPatience",0)
		
			# feeding 喂食
			self.feeding = data.get("feeding",[])
		
			# useBall 用球
			self.useBall = data.get("useBall",[])
		
			# normal 普通球奖励
			self.normal = data.get("normal",[])
		
			# luckyNormal 普通球幸运奖励
			self.luckyNormal = data.get("luckyNormal",[])
		
			# advanced 高级球奖励
			self.advanced = data.get("advanced",[])
		
			# luckyAdvanced 高级球幸运奖励
			self.luckyAdvanced = data.get("luckyAdvanced",[])
		
			# master 大师球奖励
			self.master = data.get("master",[])
		
			# luckyMaster 大师球幸运奖励
			self.luckyMaster = data.get("luckyMaster",[])
		
			# sweet 甜蜜球奖励
			self.sweet = data.get("sweet",[])
		
			# luckySweet 甜蜜球幸运奖励
			self.luckySweet = data.get("luckySweet",[])
		

# shahuleyuan
class ResShahuleyuan(object):
	RES_TABLE = "shahuleyuan"
	__slots__ = ("id","name","stepNum","gifts","cost","otherCost","icon","meetList","leyuanPetList","mapId","randomGift",)

    def __init__(self):
		
			# id 沙狐乐园表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# stepNum 初始步数
			self.stepNum = 0
		
			# gifts 初始赠送
			self.gifts = []
		
			# cost 进入消耗
			self.cost = []
		
			# otherCost 非开放日进入消耗
			self.otherCost = []
		
			# icon 图标
			self.icon = ""
		
			# meetList 遇怪序列
			self.meetList = []
		
			# leyuanPetList 可能遇到的乐园宠物id
			self.leyuanPetList = []
		
			# mapId 场景id
			self.mapId = 0
		
			# randomGift 随机礼盒概率
			self.randomGift = []
		

    def load_from_json(self, data):
		
			# id 沙狐乐园表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# stepNum 初始步数
			self.stepNum = data.get("stepNum",0)
		
			# gifts 初始赠送
			self.gifts = data.get("gifts",[])
		
			# cost 进入消耗
			self.cost = data.get("cost",[])
		
			# otherCost 非开放日进入消耗
			self.otherCost = data.get("otherCost",[])
		
			# icon 图标
			self.icon = data.get("icon","")
		
			# meetList 遇怪序列
			self.meetList = data.get("meetList",[])
		
			# leyuanPetList 可能遇到的乐园宠物id
			self.leyuanPetList = data.get("leyuanPetList",[])
		
			# mapId 场景id
			self.mapId = data.get("mapId",0)
		
			# randomGift 随机礼盒概率
			self.randomGift = data.get("randomGift",[])
		

# shenbingskill
class ResShenbingskill(object):
	RES_TABLE = "shenbingskill"
	__slots__ = ("id","skillId","lv","name","cost","attr","icon",)

    def __init__(self):
		
			# id 神兵技能表
			self.id = 0
		
			# skillId 技能id
			self.skillId = 0
		
			# lv 技能等级
			self.lv = 0
		
			# name 名称
			self.name = ""
		
			# cost 升级消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		
			# icon 图标
			self.icon = ""
		

    def load_from_json(self, data):
		
			# id 神兵技能表
			self.id = data.get("id",0)
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		
			# lv 技能等级
			self.lv = data.get("lv",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# cost 升级消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# icon 图标
			self.icon = data.get("icon","")
		

# shenbingskin
class ResShenbingskin(object):
	RES_TABLE = "shenbingskin"
	__slots__ = ("id","name","type","typeName","bg","attr","cost","front","behind","up","down","offX","offY","scale",)

    def __init__(self):
		
			# id 神兵皮肤表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# type 类型
			self.type = 0
		
			# typeName 类型名
			self.typeName = ""
		
			# bg 底图
			self.bg = ""
		
			# attr 属性
			self.attr = []
		
			# cost 激活消耗道具
			self.cost = []
		
			# front 场景跟随占用0,0前面像素
			self.front = 0
		
			# behind 场景跟随占用0,0点后面像素
			self.behind = 0
		
			# up 0,0点上面
			self.up = 0
		
			# down 0,0点下面
			self.down = 0
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		

    def load_from_json(self, data):
		
			# id 神兵皮肤表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# type 类型
			self.type = data.get("type",0)
		
			# typeName 类型名
			self.typeName = data.get("typeName","")
		
			# bg 底图
			self.bg = data.get("bg","")
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# cost 激活消耗道具
			self.cost = data.get("cost",[])
		
			# front 场景跟随占用0,0前面像素
			self.front = data.get("front",0)
		
			# behind 场景跟随占用0,0点后面像素
			self.behind = data.get("behind",0)
		
			# up 0,0点上面
			self.up = data.get("up",0)
		
			# down 0,0点下面
			self.down = data.get("down",0)
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		

# shenbing
class ResShenbing(object):
	RES_TABLE = "shenbing"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","actSkill","jjreward","offX","offY","scale","effectTip",)

    def __init__(self):
		
			# id 神兵表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# actSkill 激活技能
			self.actSkill = 0
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# effectTip 特效升级提示
			self.effectTip = ""
		

    def load_from_json(self, data):
		
			# id 神兵表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# actSkill 激活技能
			self.actSkill = data.get("actSkill",0)
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# effectTip 特效升级提示
			self.effectTip = data.get("effectTip","")
		

# godEquipStep
class ResGodEquipStep(object):
	RES_TABLE = "godEquipStep"
	__slots__ = ("id","count","cost","basePer","addPer","recycle","godAttrValueCost","godAttrTypeCost",)

    def __init__(self):
		
			# id 神装阶数表
			self.id = 0
		
			# count 属性条数
			self.count = 0
		
			# cost 升阶消耗
			self.cost = []
		
			# basePer 升级基础成功率
			self.basePer = 0
		
			# addPer 失败增加成功率
			self.addPer = 0
		
			# recycle 升级失败返回材料
			self.recycle = []
		
			# godAttrValueCost 神装属性洗炼消耗
			self.godAttrValueCost = []
		
			# godAttrTypeCost 神装种类洗炼消耗
			self.godAttrTypeCost = []
		

    def load_from_json(self, data):
		
			# id 神装阶数表
			self.id = data.get("id",0)
		
			# count 属性条数
			self.count = data.get("count",0)
		
			# cost 升阶消耗
			self.cost = data.get("cost",[])
		
			# basePer 升级基础成功率
			self.basePer = data.get("basePer",0)
		
			# addPer 失败增加成功率
			self.addPer = data.get("addPer",0)
		
			# recycle 升级失败返回材料
			self.recycle = data.get("recycle",[])
		
			# godAttrValueCost 神装属性洗炼消耗
			self.godAttrValueCost = data.get("godAttrValueCost",[])
		
			# godAttrTypeCost 神装种类洗炼消耗
			self.godAttrTypeCost = data.get("godAttrTypeCost",[])
		

# godEquipAttrValueRandom
class ResGodEquipAttrValueRandom(object):
	RES_TABLE = "godEquipAttrValueRandom"
	__slots__ = ("id","weight","addValue",)

    def __init__(self):
		
			# id 神装属性洗炼权重表
			self.id = 0
		
			# weight 权重
			self.weight = 0
		
			# addValue 增加的属性
			self.addValue = []
		

    def load_from_json(self, data):
		
			# id 神装属性洗炼权重表
			self.id = data.get("id",0)
		
			# weight 权重
			self.weight = data.get("weight",0)
		
			# addValue 增加的属性
			self.addValue = data.get("addValue",[])
		

# godEquipCountGM
class ResGodEquipCountGM(object):
	RES_TABLE = "godEquipCountGM"
	__slots__ = ("id","attr",)

    def __init__(self):
		
			# id 神装件数共鸣表
			self.id = 0
		
			# attr 属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 神装件数共鸣表
			self.id = data.get("id",0)
		
			# attr 属性
			self.attr = data.get("attr",[])
		

# godEquipLvGM
class ResGodEquipLvGM(object):
	RES_TABLE = "godEquipLvGM"
	__slots__ = ("id","attr",)

    def __init__(self):
		
			# id 神装等级共鸣表
			self.id = 0
		
			# attr 属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 神装等级共鸣表
			self.id = data.get("id",0)
		
			# attr 属性
			self.attr = data.get("attr",[])
		

# leichong1
class ResLeichong1(object):
	RES_TABLE = "leichong1"
	__slots__ = ("id","cycle","page","reward","rmb",)

    def __init__(self):
		
			# id id
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# page 分页
			self.page = 0
		
			# reward 奖励
			self.reward = []
		
			# rmb 人民币需求（分）
			self.rmb = 0
		

    def load_from_json(self, data):
		
			# id id
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# page 分页
			self.page = data.get("page",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# rmb 人民币需求（分）
			self.rmb = data.get("rmb",0)
		

# shenchonglaixi
class ResShenchonglaixi(object):
	RES_TABLE = "shenchonglaixi"
	__slots__ = ("id","cycle","page","days","empty","next","reward","diamond",)

    def __init__(self):
		
			# id id
			self.id = 0
		
			# cycle 檔期
			self.cycle = 0
		
			# page 分頁
			self.page = 0
		
			# days 活動天數
			self.days = 0
		
			# empty 是否空擋
			self.empty = 0
		
			# next 下一檔期
			self.next = 0
		
			# reward 獎勵
			self.reward = []
		
			# diamond 鑽石需求
			self.diamond = 0
		

    def load_from_json(self, data):
		
			# id id
			self.id = data.get("id",0)
		
			# cycle 檔期
			self.cycle = data.get("cycle",0)
		
			# page 分頁
			self.page = data.get("page",0)
		
			# days 活動天數
			self.days = data.get("days",0)
		
			# empty 是否空擋
			self.empty = data.get("empty",0)
		
			# next 下一檔期
			self.next = data.get("next",0)
		
			# reward 獎勵
			self.reward = data.get("reward",[])
		
			# diamond 鑽石需求
			self.diamond = data.get("diamond",0)
		

# shouchong
class ResShouchong(object):
	RES_TABLE = "shouchong"
	__slots__ = ("id","reward","rmb",)

    def __init__(self):
		
			# id 充值表
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# rmb 人民币需求（分）
			self.rmb = 0
		

    def load_from_json(self, data):
		
			# id 充值表
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# rmb 人民币需求（分）
			self.rmb = data.get("rmb",0)
		

# limitLeichong
class ResLimitLeichong(object):
	RES_TABLE = "limitLeichong"
	__slots__ = ("id","reward","rmb",)

    def __init__(self):
		
			# id id
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# rmb 人民币需求（分）
			self.rmb = 0
		

    def load_from_json(self, data):
		
			# id id
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# rmb 人民币需求（分）
			self.rmb = data.get("rmb",0)
		

# leichong
class ResLeichong(object):
	RES_TABLE = "leichong"
	__slots__ = ("id","cycle","page","days","empty","next","reward","rmb",)

    def __init__(self):
		
			# id id
			self.id = 0
		
			# cycle 档期
			self.cycle = 0
		
			# page 分页
			self.page = 0
		
			# days 活动天数
			self.days = 0
		
			# empty 是否空挡
			self.empty = 0
		
			# next 下一档期
			self.next = 0
		
			# reward 奖励
			self.reward = []
		
			# rmb 人民币需求（分）
			self.rmb = 0
		

    def load_from_json(self, data):
		
			# id id
			self.id = data.get("id",0)
		
			# cycle 档期
			self.cycle = data.get("cycle",0)
		
			# page 分页
			self.page = data.get("page",0)
		
			# days 活动天数
			self.days = data.get("days",0)
		
			# empty 是否空挡
			self.empty = data.get("empty",0)
		
			# next 下一档期
			self.next = data.get("next",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# rmb 人民币需求（分）
			self.rmb = data.get("rmb",0)
		

# chengzhangjijin
class ResChengzhangjijin(object):
	RES_TABLE = "chengzhangjijin"
	__slots__ = ("id","reward","lv",)

    def __init__(self):
		
			# id 成长基金表
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# lv 人物等级需求
			self.lv = 0
		

    def load_from_json(self, data):
		
			# id 成长基金表
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# lv 人物等级需求
			self.lv = data.get("lv",0)
		

# chengzhangjijintuangou
class ResChengzhangjijintuangou(object):
	RES_TABLE = "chengzhangjijintuangou"
	__slots__ = ("id","reward","needNum",)

    def __init__(self):
		
			# id 成长基金团购表
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# needNum 需求人数
			self.needNum = 0
		

    def load_from_json(self, data):
		
			# id 成长基金团购表
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# needNum 需求人数
			self.needNum = data.get("needNum",0)
		

# touzijihua
class ResTouzijihua(object):
	RES_TABLE = "touzijihua"
	__slots__ = ("id","reward","openserver",)

    def __init__(self):
		
			# id 充值表
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# openserver 开服天数需求
			self.openserver = 0
		

    def load_from_json(self, data):
		
			# id 充值表
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# openserver 开服天数需求
			self.openserver = data.get("openserver",0)
		

# totemRan
class ResTotemRan(object):
	RES_TABLE = "totemRan"
	__slots__ = ("id","num","multi",)

    def __init__(self):
		
			# id 图腾随机暴击表
			self.id = 0
		
			# num 暴击权重
			self.num = 0
		
			# multi 暴击倍数
			self.multi = 0
		

    def load_from_json(self, data):
		
			# id 图腾随机暴击表
			self.id = data.get("id",0)
		
			# num 暴击权重
			self.num = data.get("num",0)
		
			# multi 暴击倍数
			self.multi = data.get("multi",0)
		

# totemBj
class ResTotemBj(object):
	RES_TABLE = "totemBj"
	__slots__ = ("id","num","multi",)

    def __init__(self):
		
			# id 图腾暴击表
			self.id = 0
		
			# num 暴击需要次数
			self.num = 0
		
			# multi 暴击倍数
			self.multi = 0
		

    def load_from_json(self, data):
		
			# id 图腾暴击表
			self.id = data.get("id",0)
		
			# num 暴击需要次数
			self.num = data.get("num",0)
		
			# multi 暴击倍数
			self.multi = data.get("multi",0)
		

# totems
class ResTotems(object):
	RES_TABLE = "totems"
	__slots__ = ("id","pos","level","exp","cost","tpCost","specLv","attr1","attr2",)

    def __init__(self):
		
			# id 图腾表
			self.id = 0
		
			# pos 部位
			self.pos = 0
		
			# level 等级
			self.level = 0
		
			# exp 经验
			self.exp = 0
		
			# cost 每次点击升级消耗
			self.cost = []
		
			# tpCost 突破消耗
			self.tpCost = []
		
			# specLv 特殊效果等级
			self.specLv = 0
		
			# attr1 激活突破用属性
			self.attr1 = []
		
			# attr2 小弹窗属性
			self.attr2 = []
		

    def load_from_json(self, data):
		
			# id 图腾表
			self.id = data.get("id",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# exp 经验
			self.exp = data.get("exp",0)
		
			# cost 每次点击升级消耗
			self.cost = data.get("cost",[])
		
			# tpCost 突破消耗
			self.tpCost = data.get("tpCost",[])
		
			# specLv 特殊效果等级
			self.specLv = data.get("specLv",0)
		
			# attr1 激活突破用属性
			self.attr1 = data.get("attr1",[])
		
			# attr2 小弹窗属性
			self.attr2 = data.get("attr2",[])
		

# txdyRankReward
class ResTxdyRankReward(object):
	RES_TABLE = "txdyRankReward"
	__slots__ = ("id","zoneId","min","max","reward",)

    def __init__(self):
		
			# id 天下第一循环赛奖励表
			self.id = 0
		
			# zoneId 区id
			self.zoneId = 0
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 天下第一循环赛奖励表
			self.id = data.get("id",0)
		
			# zoneId 区id
			self.zoneId = data.get("zoneId",0)
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# txdyBet
class ResTxdyBet(object):
	RES_TABLE = "txdyBet"
	__slots__ = ("id","zoneId","betType","bet","reward",)

    def __init__(self):
		
			# id 天下第一押注表
			self.id = 0
		
			# zoneId 区id
			self.zoneId = 0
		
			# betType 押注类型
			self.betType = 0
		
			# bet 押注金额
			self.bet = []
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 天下第一押注表
			self.id = data.get("id",0)
		
			# zoneId 区id
			self.zoneId = data.get("zoneId",0)
		
			# betType 押注类型
			self.betType = data.get("betType",0)
		
			# bet 押注金额
			self.bet = data.get("bet",[])
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# txdyZone
class ResTxdyZone(object):
	RES_TABLE = "txdyZone"
	__slots__ = ("id","min","max","reward8","reward4","reward2","reward1",)

    def __init__(self):
		
			# id 天下第一区表
			self.id = 0
		
			# min 最小等级
			self.min = 0
		
			# max 最大等级
			self.max = 0
		
			# reward8 8强奖励
			self.reward8 = []
		
			# reward4 4强奖励
			self.reward4 = []
		
			# reward2 前2奖励
			self.reward2 = []
		
			# reward1 第1奖励
			self.reward1 = []
		

    def load_from_json(self, data):
		
			# id 天下第一区表
			self.id = data.get("id",0)
		
			# min 最小等级
			self.min = data.get("min",0)
		
			# max 最大等级
			self.max = data.get("max",0)
		
			# reward8 8强奖励
			self.reward8 = data.get("reward8",[])
		
			# reward4 4强奖励
			self.reward4 = data.get("reward4",[])
		
			# reward2 前2奖励
			self.reward2 = data.get("reward2",[])
		
			# reward1 第1奖励
			self.reward1 = data.get("reward1",[])
		

# tianxianskin
class ResTianxianskin(object):
	RES_TABLE = "tianxianskin"
	__slots__ = ("id","name","type","typeName","bg","attr","cost","offX","offY","scale","front","behind","up","down",)

    def __init__(self):
		
			# id 天仙皮肤表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# type 类型
			self.type = 0
		
			# typeName 类型名
			self.typeName = ""
		
			# bg 底图
			self.bg = ""
		
			# attr 属性
			self.attr = []
		
			# cost 激活消耗道具
			self.cost = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# front 场景跟随占用0,0前面像素
			self.front = 0
		
			# behind 场景跟随占用0,0点后面像素
			self.behind = 0
		
			# up 0,0点上面
			self.up = 0
		
			# down 0,0点下面
			self.down = 0
		

    def load_from_json(self, data):
		
			# id 天仙皮肤表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# type 类型
			self.type = data.get("type",0)
		
			# typeName 类型名
			self.typeName = data.get("typeName","")
		
			# bg 底图
			self.bg = data.get("bg","")
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# cost 激活消耗道具
			self.cost = data.get("cost",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# front 场景跟随占用0,0前面像素
			self.front = data.get("front",0)
		
			# behind 场景跟随占用0,0点后面像素
			self.behind = data.get("behind",0)
		
			# up 0,0点上面
			self.up = data.get("up",0)
		
			# down 0,0点下面
			self.down = data.get("down",0)
		

# tianxian
class ResTianxian(object):
	RES_TABLE = "tianxian"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","actSkill","offX","offY","scale","jjreward","effectTip",)

    def __init__(self):
		
			# id 天仙表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# actSkill 激活技能
			self.actSkill = 0
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# effectTip 特效升级提示
			self.effectTip = ""
		

    def load_from_json(self, data):
		
			# id 天仙表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# actSkill 激活技能
			self.actSkill = data.get("actSkill",0)
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# effectTip 特效升级提示
			self.effectTip = data.get("effectTip","")
		

# tiannvskin
class ResTiannvskin(object):
	RES_TABLE = "tiannvskin"
	__slots__ = ("id","name","cost","attr","offX","offY","scale","bg","type","typeName",)

    def __init__(self):
		
			# id 天女皮肤表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# cost 激活消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# bg 
			self.bg = ""
		
			# type 类型
			self.type = 0
		
			# typeName 类型名
			self.typeName = ""
		

    def load_from_json(self, data):
		
			# id 天女皮肤表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# cost 激活消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# bg 
			self.bg = data.get("bg","")
		
			# type 类型
			self.type = data.get("type",0)
		
			# typeName 类型名
			self.typeName = data.get("typeName","")
		

# tiannv
class ResTiannv(object):
	RES_TABLE = "tiannv"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","jjreward","offX","offY","scale","effectTip",)

    def __init__(self):
		
			# id 天女表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# effectTip 特效升级提示
			self.effectTip = ""
		

    def load_from_json(self, data):
		
			# id 天女表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# effectTip 特效升级提示
			self.effectTip = data.get("effectTip","")
		

# tianxianskill
class ResTianxianskill(object):
	RES_TABLE = "tianxianskill"
	__slots__ = ("id","skillId","lv","name","cost","attr","icon",)

    def __init__(self):
		
			# id 天仙技能表
			self.id = 0
		
			# skillId 技能id
			self.skillId = 0
		
			# lv 技能等级
			self.lv = 0
		
			# name 名称
			self.name = ""
		
			# cost 升级消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		
			# icon 图标
			self.icon = ""
		

    def load_from_json(self, data):
		
			# id 天仙技能表
			self.id = data.get("id",0)
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		
			# lv 技能等级
			self.lv = data.get("lv",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# cost 升级消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# icon 图标
			self.icon = data.get("icon","")
		

# tiannvskill
class ResTiannvskill(object):
	RES_TABLE = "tiannvskill"
	__slots__ = ("id","actlv","skillId","icon","addSkillId",)

    def __init__(self):
		
			# id 天女技能表
			self.id = 0
		
			# actlv 激活阶数
			self.actlv = 0
		
			# skillId 技能表id
			self.skillId = 0
		
			# icon 图标
			self.icon = ""
		
			# addSkillId 加强技能id
			self.addSkillId = 0
		

    def load_from_json(self, data):
		
			# id 天女技能表
			self.id = data.get("id",0)
		
			# actlv 激活阶数
			self.actlv = data.get("actlv",0)
		
			# skillId 技能表id
			self.skillId = data.get("skillId",0)
		
			# icon 图标
			self.icon = data.get("icon","")
		
			# addSkillId 加强技能id
			self.addSkillId = data.get("addSkillId",0)
		

# myhead
class ResMyhead(object):
	RES_TABLE = "myhead"
	__slots__ = ("id","sort","type","typeName","bg","cost","attr",)

    def __init__(self):
		
			# id 时装表
			self.id = 0
		
			# sort 类型
			self.sort = 0
		
			# type 类型
			self.type = 0
		
			# typeName 类型名
			self.typeName = ""
		
			# bg 底图
			self.bg = ""
		
			# cost 消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 时装表
			self.id = data.get("id",0)
		
			# sort 类型
			self.sort = data.get("sort",0)
		
			# type 类型
			self.type = data.get("type",0)
		
			# typeName 类型名
			self.typeName = data.get("typeName","")
		
			# bg 底图
			self.bg = data.get("bg","")
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		

# condDef
class ResCondDef(object):
	RES_TABLE = "condDef"
	__slots__ = ("key","name","goname","pyname","tsname",)

    def __init__(self):
		
			# key 属性定义key
			self.key = ""
		
			# name 属性名字
			self.name = ""
		
			# goname go替换字符串
			self.goname = ""
		
			# pyname py替换字符串
			self.pyname = ""
		
			# tsname ts替换字符串
			self.tsname = ""
		

    def load_from_json(self, data):
		
			# key 属性定义key
			self.key = data.get("key","")
		
			# name 属性名字
			self.name = data.get("name","")
		
			# goname go替换字符串
			self.goname = data.get("goname","")
		
			# pyname py替换字符串
			self.pyname = data.get("pyname","")
		
			# tsname ts替换字符串
			self.tsname = data.get("tsname","")
		

# condition
class ResCondition(object):
	RES_TABLE = "condition"
	__slots__ = ("id","condition",)

    def __init__(self):
		
			# id 属性定义key
			self.id = 0
		
			# condition 条件
			self.condition = ""
		

    def load_from_json(self, data):
		
			# id 属性定义key
			self.id = data.get("id",0)
		
			# condition 条件
			self.condition = data.get("condition","")
		

# link
class ResLink(object):
	RES_TABLE = "link"
	__slots__ = ("id","name","openId","toBagId","icon","wordinfo",)

    def __init__(self):
		
			# id 途径ID
			self.id = 0
		
			# name 名字
			self.name = ""
		
			# openId 打开界面,对应功能开启表
			self.openId = 0
		
			# toBagId 打开背包跳到道具id
			self.toBagId = []
		
			# icon 途径图片图标(图标全部都在美术路径主界面)
			self.icon = ""
		
			# wordinfo 文字提示说明
			self.wordinfo = ""
		

    def load_from_json(self, data):
		
			# id 途径ID
			self.id = data.get("id",0)
		
			# name 名字
			self.name = data.get("name","")
		
			# openId 打开界面,对应功能开启表
			self.openId = data.get("openId",0)
		
			# toBagId 打开背包跳到道具id
			self.toBagId = data.get("toBagId",[])
		
			# icon 途径图片图标(图标全部都在美术路径主界面)
			self.icon = data.get("icon","")
		
			# wordinfo 文字提示说明
			self.wordinfo = data.get("wordinfo","")
		

# tongling
class ResTongling(object):
	RES_TABLE = "tongling"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","actSkill","jjreward","offX","offY","scale",)

    def __init__(self):
		
			# id 通灵表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# actSkill 激活技能
			self.actSkill = 0
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		

    def load_from_json(self, data):
		
			# id 通灵表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# actSkill 激活技能
			self.actSkill = data.get("actSkill",0)
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		

# tonglingskill
class ResTonglingskill(object):
	RES_TABLE = "tonglingskill"
	__slots__ = ("id","skillId","lv","name","cost","attr","icon",)

    def __init__(self):
		
			# id 通灵技能表
			self.id = 0
		
			# skillId 技能id
			self.skillId = 0
		
			# lv 技能等级
			self.lv = 0
		
			# name 名称
			self.name = ""
		
			# cost 升级消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		
			# icon 图标
			self.icon = ""
		

    def load_from_json(self, data):
		
			# id 通灵技能表
			self.id = data.get("id",0)
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		
			# lv 技能等级
			self.lv = data.get("lv",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# cost 升级消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# icon 图标
			self.icon = data.get("icon","")
		

# vip
class ResVip(object):
	RES_TABLE = "vip"
	__slots__ = ("id","exp","desc","lineSpacing","goldExchange","bindExchange","grBossOneKey","qmBossTz","qmBossFh","equipResolveAuto","equipResolve50","ttslOneKey","lwbzOneKey","arenaBuyTimes","clbzSweepCount","clfbSweepAll","guildTaskResetNum","fightSpeed","shopDiscount","ysAuto","addbag","mr300TaskCost","zkfmTaskCost","TaskDesc","daoguanBuyNum","daoguanSweep","pvpbuynum","pvpBuyCost","battleJumpNum","costview","cost","rewardTime","reward","dayReward","hetiBuyNum",)

    def __init__(self):
		
			# id vip表
			self.id = 0
		
			# exp vip经验
			self.exp = 0
		
			# desc 描述(没用的已废除)
			self.desc = ""
		
			# lineSpacing 描述行间距
			self.lineSpacing = 0
		
			# goldExchange 金币兑换次数
			self.goldExchange = 0
		
			# bindExchange 绑钻兑换次数
			self.bindExchange = 0
		
			# grBossOneKey 个人boss一键扫荡
			self.grBossOneKey = 0
		
			# qmBossTz 全民boss可购买挑战次数
			self.qmBossTz = 0
		
			# qmBossFh 全民boss是否可复活
			self.qmBossFh = 0
		
			# equipResolveAuto 是否可自动熔炼
			self.equipResolveAuto = 0
		
			# equipResolve50 熔炼50个
			self.equipResolve50 = 0
		
			# ttslOneKey 天庭试炼一键扫荡
			self.ttslOneKey = 0
		
			# lwbzOneKey 龙王宝藏一键挖宝
			self.lwbzOneKey = 0
		
			# arenaBuyTimes 竞技场挑战购买次数
			self.arenaBuyTimes = 0
		
			# clbzSweepCount 材料副本附加扫荡次数
			self.clbzSweepCount = 0
		
			# clfbSweepAll 材料副本一键扫荡
			self.clfbSweepAll = 0
		
			# guildTaskResetNum 帮会任务重置次数
			self.guildTaskResetNum = 0
		
			# fightSpeed 战斗倍数
			self.fightSpeed = 0
		
			# shopDiscount 商店折扣
			self.shopDiscount = 0
		
			# ysAuto 开启异兽空间自动挑战
			self.ysAuto = 0
		
			# addbag 额外增加背包格
			self.addbag = 0
		
			# mr300TaskCost 每日任务每点进度消耗
			self.mr300TaskCost = 0
		
			# zkfmTaskCost 日常对战每点进度消耗
			self.zkfmTaskCost = 0
		
			# TaskDesc 任务一键完成打折
			self.TaskDesc = 0
		
			# daoguanBuyNum 道馆购买挑战次数
			self.daoguanBuyNum = 0
		
			# daoguanSweep 道馆一键扫荡功能
			self.daoguanSweep = 0
		
			# pvpbuynum PVP购买次数
			self.pvpbuynum = 0
		
			# pvpBuyCost PVP购买次数消耗
			self.pvpBuyCost = 0
		
			# battleJumpNum 战斗跳过次数(0没有>0有-1无限)
			self.battleJumpNum = 0
		
			# costview 前端显示礼包价
			self.costview = []
		
			# cost 后端实际礼包价
			self.cost = []
		
			# rewardTime 在线时长领取(秒)
			self.rewardTime = 0
		
			# reward 奖励
			self.reward = []
		
			# dayReward vip每日奖励
			self.dayReward = []
		
			# hetiBuyNum 合体能购买的次数
			self.hetiBuyNum = 0
		

    def load_from_json(self, data):
		
			# id vip表
			self.id = data.get("id",0)
		
			# exp vip经验
			self.exp = data.get("exp",0)
		
			# desc 描述(没用的已废除)
			self.desc = data.get("desc","")
		
			# lineSpacing 描述行间距
			self.lineSpacing = data.get("lineSpacing",0)
		
			# goldExchange 金币兑换次数
			self.goldExchange = data.get("goldExchange",0)
		
			# bindExchange 绑钻兑换次数
			self.bindExchange = data.get("bindExchange",0)
		
			# grBossOneKey 个人boss一键扫荡
			self.grBossOneKey = data.get("grBossOneKey",0)
		
			# qmBossTz 全民boss可购买挑战次数
			self.qmBossTz = data.get("qmBossTz",0)
		
			# qmBossFh 全民boss是否可复活
			self.qmBossFh = data.get("qmBossFh",0)
		
			# equipResolveAuto 是否可自动熔炼
			self.equipResolveAuto = data.get("equipResolveAuto",0)
		
			# equipResolve50 熔炼50个
			self.equipResolve50 = data.get("equipResolve50",0)
		
			# ttslOneKey 天庭试炼一键扫荡
			self.ttslOneKey = data.get("ttslOneKey",0)
		
			# lwbzOneKey 龙王宝藏一键挖宝
			self.lwbzOneKey = data.get("lwbzOneKey",0)
		
			# arenaBuyTimes 竞技场挑战购买次数
			self.arenaBuyTimes = data.get("arenaBuyTimes",0)
		
			# clbzSweepCount 材料副本附加扫荡次数
			self.clbzSweepCount = data.get("clbzSweepCount",0)
		
			# clfbSweepAll 材料副本一键扫荡
			self.clfbSweepAll = data.get("clfbSweepAll",0)
		
			# guildTaskResetNum 帮会任务重置次数
			self.guildTaskResetNum = data.get("guildTaskResetNum",0)
		
			# fightSpeed 战斗倍数
			self.fightSpeed = data.get("fightSpeed",0)
		
			# shopDiscount 商店折扣
			self.shopDiscount = data.get("shopDiscount",0)
		
			# ysAuto 开启异兽空间自动挑战
			self.ysAuto = data.get("ysAuto",0)
		
			# addbag 额外增加背包格
			self.addbag = data.get("addbag",0)
		
			# mr300TaskCost 每日任务每点进度消耗
			self.mr300TaskCost = data.get("mr300TaskCost",0)
		
			# zkfmTaskCost 日常对战每点进度消耗
			self.zkfmTaskCost = data.get("zkfmTaskCost",0)
		
			# TaskDesc 任务一键完成打折
			self.TaskDesc = data.get("TaskDesc",0)
		
			# daoguanBuyNum 道馆购买挑战次数
			self.daoguanBuyNum = data.get("daoguanBuyNum",0)
		
			# daoguanSweep 道馆一键扫荡功能
			self.daoguanSweep = data.get("daoguanSweep",0)
		
			# pvpbuynum PVP购买次数
			self.pvpbuynum = data.get("pvpbuynum",0)
		
			# pvpBuyCost PVP购买次数消耗
			self.pvpBuyCost = data.get("pvpBuyCost",0)
		
			# battleJumpNum 战斗跳过次数(0没有>0有-1无限)
			self.battleJumpNum = data.get("battleJumpNum",0)
		
			# costview 前端显示礼包价
			self.costview = data.get("costview",[])
		
			# cost 后端实际礼包价
			self.cost = data.get("cost",[])
		
			# rewardTime 在线时长领取(秒)
			self.rewardTime = data.get("rewardTime",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# dayReward vip每日奖励
			self.dayReward = data.get("dayReward",[])
		
			# hetiBuyNum 合体能购买的次数
			self.hetiBuyNum = data.get("hetiBuyNum",0)
		

# wakuangreward
class ResWakuangreward(object):
	RES_TABLE = "wakuangreward"
	__slots__ = ("id","baseid","x","y","reward","robreward","score","skin","max","helpId","color","name",)

    def __init__(self):
		
			# id 挖矿奖励表
			self.id = 0
		
			# baseid 矿专属id
			self.baseid = 0
		
			# x 中心位置X
			self.x = 0
		
			# y 中心位置Y
			self.y = 0
		
			# reward 奖励宝箱
			self.reward = 0
		
			# robreward 抢矿奖励宝箱
			self.robreward = 0
		
			# score 积分
			self.score = 0
		
			# skin 皮肤
			self.skin = ""
		
			# max 矿队伍数量
			self.max = 0
		
			# helpId 帮助说明id
			self.helpId = 0
		
			# color 颜色值
			self.color = ""
		
			# name 名字
			self.name = ""
		

    def load_from_json(self, data):
		
			# id 挖矿奖励表
			self.id = data.get("id",0)
		
			# baseid 矿专属id
			self.baseid = data.get("baseid",0)
		
			# x 中心位置X
			self.x = data.get("x",0)
		
			# y 中心位置Y
			self.y = data.get("y",0)
		
			# reward 奖励宝箱
			self.reward = data.get("reward",0)
		
			# robreward 抢矿奖励宝箱
			self.robreward = data.get("robreward",0)
		
			# score 积分
			self.score = data.get("score",0)
		
			# skin 皮肤
			self.skin = data.get("skin","")
		
			# max 矿队伍数量
			self.max = data.get("max",0)
		
			# helpId 帮助说明id
			self.helpId = data.get("helpId",0)
		
			# color 颜色值
			self.color = data.get("color","")
		
			# name 名字
			self.name = data.get("name","")
		

# wakuangrankmonth
class ResWakuangrankmonth(object):
	RES_TABLE = "wakuangrankmonth"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id 挖矿月奖
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 挖矿月奖
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# wakuangbase
class ResWakuangbase(object):
	RES_TABLE = "wakuangbase"
	__slots__ = ("id","x","y","name","iconBg","color","pos",)

    def __init__(self):
		
			# id 挖矿基地（勿动
			self.id = 0
		
			# x 中心位置X
			self.x = 0
		
			# y 中心位置Y
			self.y = 0
		
			# name 基地名字
			self.name = ""
		
			# iconBg 角色头像底框
			self.iconBg = ""
		
			# color 名字颜色
			self.color = ""
		
			# pos 坐标
			self.pos = []
		

    def load_from_json(self, data):
		
			# id 挖矿基地（勿动
			self.id = data.get("id",0)
		
			# x 中心位置X
			self.x = data.get("x",0)
		
			# y 中心位置Y
			self.y = data.get("y",0)
		
			# name 基地名字
			self.name = data.get("name","")
		
			# iconBg 角色头像底框
			self.iconBg = data.get("iconBg","")
		
			# color 名字颜色
			self.color = data.get("color","")
		
			# pos 坐标
			self.pos = data.get("pos",[])
		

# wakuangrankday
class ResWakuangrankday(object):
	RES_TABLE = "wakuangrankday"
	__slots__ = ("id","reward",)

    def __init__(self):
		
			# id 挖矿日奖
			self.id = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 挖矿日奖
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# xianwei
class ResXianwei(object):
	RES_TABLE = "xianwei"
	__slots__ = ("id","name","exp","cost","baseAttr","onceAttr","actSkill","jjreward","offX","offY","scale",)

    def __init__(self):
		
			# id 仙位表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# actSkill 激活技能
			self.actSkill = 0
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		

    def load_from_json(self, data):
		
			# id 仙位表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# actSkill 激活技能
			self.actSkill = data.get("actSkill",0)
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		

# xianlv
class ResXianlv(object):
	RES_TABLE = "xianlv"
	__slots__ = ("id","name","quality","skillId","cost","offX","offY","scale",)

    def __init__(self):
		
			# id 仙侣表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# quality 品质
			self.quality = 0
		
			# skillId 技能id
			self.skillId = 0
		
			# cost 激活材料
			self.cost = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		

    def load_from_json(self, data):
		
			# id 仙侣表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# quality 品质
			self.quality = data.get("quality",0)
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		
			# cost 激活材料
			self.cost = data.get("cost",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		

# xianweiskill
class ResXianweiskill(object):
	RES_TABLE = "xianweiskill"
	__slots__ = ("id","skillId","lv","name","cost","attr","icon",)

    def __init__(self):
		
			# id 仙位技能表
			self.id = 0
		
			# skillId 技能id
			self.skillId = 0
		
			# lv 技能等级
			self.lv = 0
		
			# name 名称
			self.name = ""
		
			# cost 升级消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		
			# icon 图标
			self.icon = ""
		

    def load_from_json(self, data):
		
			# id 仙位技能表
			self.id = data.get("id",0)
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		
			# lv 技能等级
			self.lv = data.get("lv",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# cost 升级消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# icon 图标
			self.icon = data.get("icon","")
		

# xianlvqy
class ResXianlvqy(object):
	RES_TABLE = "xianlvqy"
	__slots__ = ("id","level","attr",)

    def __init__(self):
		
			# id 仙侣奇缘表
			self.id = 0
		
			# level 等级
			self.level = 0
		
			# attr 加成属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 仙侣奇缘表
			self.id = data.get("id",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# attr 加成属性
			self.attr = data.get("attr",[])
		

# xianlvlv
class ResXianlvlv(object):
	RES_TABLE = "xianlvlv"
	__slots__ = ("id","xianlvId","lv","exp","cost","baseAttr","onceAttr",)

    def __init__(self):
		
			# id 仙侣等级表
			self.id = 0
		
			# xianlvId 仙侣id
			self.xianlvId = 0
		
			# lv 等级
			self.lv = 0
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 升阶消耗
			self.cost = []
		
			# baseAttr 当前等级基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		

    def load_from_json(self, data):
		
			# id 仙侣等级表
			self.id = data.get("id",0)
		
			# xianlvId 仙侣id
			self.xianlvId = data.get("xianlvId",0)
		
			# lv 等级
			self.lv = data.get("lv",0)
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 升阶消耗
			self.cost = data.get("cost",[])
		
			# baseAttr 当前等级基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		

# xiedaiCreate
class ResXiedaiCreate(object):
	RES_TABLE = "xiedaiCreate"
	__slots__ = ("id","cost","basePer1","basePer2",)

    def __init__(self):
		
			# id 携带品打造表
			self.id = 0
		
			# cost 消耗
			self.cost = []
		
			# basePer1 基础成功率(前)
			self.basePer1 = 0
		
			# basePer2 基础成功率(后)
			self.basePer2 = 0
		

    def load_from_json(self, data):
		
			# id 携带品打造表
			self.id = data.get("id",0)
		
			# cost 消耗
			self.cost = data.get("cost",[])
		
			# basePer1 基础成功率(前)
			self.basePer1 = data.get("basePer1",0)
		
			# basePer2 基础成功率(后)
			self.basePer2 = data.get("basePer2",0)
		

# xiedaiRecycle
class ResXiedaiRecycle(object):
	RES_TABLE = "xiedaiRecycle"
	__slots__ = ("id","level","jieduan","recycle",)

    def __init__(self):
		
			# id 携带品强化回收表
			self.id = 0
		
			# level 等级
			self.level = 0
		
			# jieduan 阶段
			self.jieduan = 0
		
			# recycle 回收物品
			self.recycle = []
		

    def load_from_json(self, data):
		
			# id 携带品强化回收表
			self.id = data.get("id",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# jieduan 阶段
			self.jieduan = data.get("jieduan",0)
		
			# recycle 回收物品
			self.recycle = data.get("recycle",[])
		

# xiedai
class ResXiedai(object):
	RES_TABLE = "xiedai"
	__slots__ = ("id","pos","jieduan","name","name2","icon","quatily","effect","initSkillDesc","maxSkillDesc",)

    def __init__(self):
		
			# id 携带品表
			self.id = 0
		
			# pos 部位
			self.pos = 0
		
			# jieduan 阶段
			self.jieduan = 0
		
			# name 名字
			self.name = ""
		
			# name2 名字-有技能时
			self.name2 = ""
		
			# icon 图标
			self.icon = ""
		
			# quatily 品质
			self.quatily = 0
		
			# effect 界面特效
			self.effect = ""
		
			# initSkillDesc 初始技能预览
			self.initSkillDesc = ""
		
			# maxSkillDesc 满级强化技能预览
			self.maxSkillDesc = ""
		

    def load_from_json(self, data):
		
			# id 携带品表
			self.id = data.get("id",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# jieduan 阶段
			self.jieduan = data.get("jieduan",0)
		
			# name 名字
			self.name = data.get("name","")
		
			# name2 名字-有技能时
			self.name2 = data.get("name2","")
		
			# icon 图标
			self.icon = data.get("icon","")
		
			# quatily 品质
			self.quatily = data.get("quatily",0)
		
			# effect 界面特效
			self.effect = data.get("effect","")
		
			# initSkillDesc 初始技能预览
			self.initSkillDesc = data.get("initSkillDesc","")
		
			# maxSkillDesc 满级强化技能预览
			self.maxSkillDesc = data.get("maxSkillDesc","")
		

# xiedaiSkillPool
class ResXiedaiSkillPool(object):
	RES_TABLE = "xiedaiSkillPool"
	__slots__ = ("id","pos","jieduan","skillId","weight",)

    def __init__(self):
		
			# id 携带品技能池
			self.id = 0
		
			# pos 部位
			self.pos = 0
		
			# jieduan 阶段
			self.jieduan = 0
		
			# skillId 技能Id
			self.skillId = 0
		
			# weight 权重
			self.weight = 0
		

    def load_from_json(self, data):
		
			# id 携带品技能池
			self.id = data.get("id",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# jieduan 阶段
			self.jieduan = data.get("jieduan",0)
		
			# skillId 技能Id
			self.skillId = data.get("skillId",0)
		
			# weight 权重
			self.weight = data.get("weight",0)
		

# xiedaiUpgrade
class ResXiedaiUpgrade(object):
	RES_TABLE = "xiedaiUpgrade"
	__slots__ = ("id","level","jieduan","pos","basePer1","basePer2","cost","attr",)

    def __init__(self):
		
			# id 携带品强化表
			self.id = 0
		
			# level 等级
			self.level = 0
		
			# jieduan 阶段
			self.jieduan = 0
		
			# pos 部位
			self.pos = 0
		
			# basePer1 基础成功率(前)
			self.basePer1 = 0
		
			# basePer2 基础成功率(后)
			self.basePer2 = 0
		
			# cost 消耗
			self.cost = []
		
			# attr 属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 携带品强化表
			self.id = data.get("id",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# jieduan 阶段
			self.jieduan = data.get("jieduan",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# basePer1 基础成功率(前)
			self.basePer1 = data.get("basePer1",0)
		
			# basePer2 基础成功率(后)
			self.basePer2 = data.get("basePer2",0)
		
			# cost 消耗
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		

# daySurprise
class ResDaySurprise(object):
	RES_TABLE = "daySurprise"
	__slots__ = ("id","reward","odds","chatId",)

    def __init__(self):
		
			# id 意外奖励表
			self.id = 0
		
			# reward 奖励
			self.reward = []
		
			# odds 概率（万分比）
			self.odds = 0
		
			# chatId 世界聊天id
			self.chatId = 0
		

    def load_from_json(self, data):
		
			# id 意外奖励表
			self.id = data.get("id",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# odds 概率（万分比）
			self.odds = data.get("odds",0)
		
			# chatId 世界聊天id
			self.chatId = data.get("chatId",0)
		

# yabiaoreward
class ResYabiaoreward(object):
	RES_TABLE = "yabiaoreward"
	__slots__ = ("quality","reward","rob","weight","broadcast","fuchoubroadcast",)

    def __init__(self):
		
			# quality 押镖奖励表
			self.quality = 0
		
			# reward 奖励
			self.reward = []
		
			# rob 掠夺/复仇(道具必须一致奖励id有多少这里有多少)
			self.rob = []
		
			# weight 权重
			self.weight = 0
		
			# broadcast 广播id
			self.broadcast = 0
		
			# fuchoubroadcast 复仇广播id
			self.fuchoubroadcast = 0
		

    def load_from_json(self, data):
		
			# quality 押镖奖励表
			self.quality = data.get("quality",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# rob 掠夺/复仇(道具必须一致奖励id有多少这里有多少)
			self.rob = data.get("rob",[])
		
			# weight 权重
			self.weight = data.get("weight",0)
		
			# broadcast 广播id
			self.broadcast = data.get("broadcast",0)
		
			# fuchoubroadcast 复仇广播id
			self.fuchoubroadcast = data.get("fuchoubroadcast",0)
		

# zhoumolibao
class ResZhoumolibao(object):
	RES_TABLE = "zhoumolibao"
	__slots__ = ("id","name","addClover","limit","icon","nameImg","oldPrice","price","reward","link2chargeid",)

    def __init__(self):
		
			# id 周末礼包
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# addClover 四叶草
			self.addClover = 0
		
			# limit 限购次数
			self.limit = 0
		
			# icon 图标
			self.icon = ""
		
			# nameImg 名字图片
			self.nameImg = ""
		
			# oldPrice 原价
			self.oldPrice = ""
		
			# price 现价格
			self.price = ""
		
			# reward 客户端显示
			self.reward = []
		
			# link2chargeid 关联充值表
			self.link2chargeid = []
		

    def load_from_json(self, data):
		
			# id 周末礼包
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# addClover 四叶草
			self.addClover = data.get("addClover",0)
		
			# limit 限购次数
			self.limit = data.get("limit",0)
		
			# icon 图标
			self.icon = data.get("icon","")
		
			# nameImg 名字图片
			self.nameImg = data.get("nameImg","")
		
			# oldPrice 原价
			self.oldPrice = data.get("oldPrice","")
		
			# price 现价格
			self.price = data.get("price","")
		
			# reward 客户端显示
			self.reward = data.get("reward",[])
		
			# link2chargeid 关联充值表
			self.link2chargeid = data.get("link2chargeid",[])
		

# mail
class ResMail(object):
	RES_TABLE = "mail"
	__slots__ = ("id","title","content",)

    def __init__(self):
		
			# id 邮件模板表
			self.id = 0
		
			# title 邮件标题
			self.title = ""
		
			# content 邮件内容
			self.content = ""
		

    def load_from_json(self, data):
		
			# id 邮件模板表
			self.id = data.get("id",0)
		
			# title 邮件标题
			self.title = data.get("title","")
		
			# content 邮件内容
			self.content = data.get("content","")
		

# onlineAwd
class ResOnlineAwd(object):
	RES_TABLE = "onlineAwd"
	__slots__ = ("id","time","reward",)

    def __init__(self):
		
			# id 在线奖励表
			self.id = 0
		
			# time 时间分钟
			self.time = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 在线奖励表
			self.id = data.get("id",0)
		
			# time 时间分钟
			self.time = data.get("time",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# appointedTimeReward
class ResAppointedTimeReward(object):
	RES_TABLE = "appointedTimeReward"
	__slots__ = ("id","actId","reward","reward2",)

    def __init__(self):
		
			# id 指定时间登陆奖励表
			self.id = 0
		
			# actId 活动id
			self.actId = 0
		
			# reward 奖励
			self.reward = []
		
			# reward2 奖励
			self.reward2 = []
		

    def load_from_json(self, data):
		
			# id 指定时间登陆奖励表
			self.id = data.get("id",0)
		
			# actId 活动id
			self.actId = data.get("actId",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# reward2 奖励
			self.reward2 = data.get("reward2",[])
		

# horse
class ResHorse(object):
	RES_TABLE = "horse"
	__slots__ = ("id","name","offX","offY","scale","exp","cost","baseAttr","onceAttr","actSkill","front","behind","up","down","jjreward","effectTip",)

    def __init__(self):
		
			# id 坐骑表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# exp 升阶经验
			self.exp = 0
		
			# cost 消耗道具
			self.cost = []
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = []
		
			# onceAttr 每次点击增加属性
			self.onceAttr = []
		
			# actSkill 激活技能
			self.actSkill = 0
		
			# front 场景跟随占用0,0前面像素
			self.front = 0
		
			# behind 场景跟随占用0,0点后面像素
			self.behind = 0
		
			# up 0,0点上面
			self.up = 0
		
			# down 0,0点下面
			self.down = 0
		
			# jjreward 进阶奖励
			self.jjreward = []
		
			# effectTip 特效升级提示
			self.effectTip = ""
		

    def load_from_json(self, data):
		
			# id 坐骑表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# exp 升阶经验
			self.exp = data.get("exp",0)
		
			# cost 消耗道具
			self.cost = data.get("cost",[])
		
			# baseAttr 当前阶数基础属性
			self.baseAttr = data.get("baseAttr",[])
		
			# onceAttr 每次点击增加属性
			self.onceAttr = data.get("onceAttr",[])
		
			# actSkill 激活技能
			self.actSkill = data.get("actSkill",0)
		
			# front 场景跟随占用0,0前面像素
			self.front = data.get("front",0)
		
			# behind 场景跟随占用0,0点后面像素
			self.behind = data.get("behind",0)
		
			# up 0,0点上面
			self.up = data.get("up",0)
		
			# down 0,0点下面
			self.down = data.get("down",0)
		
			# jjreward 进阶奖励
			self.jjreward = data.get("jjreward",[])
		
			# effectTip 特效升级提示
			self.effectTip = data.get("effectTip","")
		

# horseskin
class ResHorseskin(object):
	RES_TABLE = "horseskin"
	__slots__ = ("id","name","type","typeName","bg","attr","offX","offY","scale","cost","front","behind","up","down",)

    def __init__(self):
		
			# id 坐骑皮肤表
			self.id = 0
		
			# name 名称
			self.name = ""
		
			# type 类型
			self.type = 0
		
			# typeName 类型名
			self.typeName = ""
		
			# bg 底图
			self.bg = ""
		
			# attr 属性
			self.attr = []
		
			# offX UI偏X
			self.offX = 0
		
			# offY UI偏Y
			self.offY = 0
		
			# scale 缩放
			self.scale = 0
		
			# cost 激活消耗道具
			self.cost = []
		
			# front 场景跟随占用0,0前面像素
			self.front = 0
		
			# behind 场景跟随占用0,0点后面像素
			self.behind = 0
		
			# up 0,0点上面
			self.up = 0
		
			# down 0,0点下面
			self.down = 0
		

    def load_from_json(self, data):
		
			# id 坐骑皮肤表
			self.id = data.get("id",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# type 类型
			self.type = data.get("type",0)
		
			# typeName 类型名
			self.typeName = data.get("typeName","")
		
			# bg 底图
			self.bg = data.get("bg","")
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# offX UI偏X
			self.offX = data.get("offX",0)
		
			# offY UI偏Y
			self.offY = data.get("offY",0)
		
			# scale 缩放
			self.scale = data.get("scale",0)
		
			# cost 激活消耗道具
			self.cost = data.get("cost",[])
		
			# front 场景跟随占用0,0前面像素
			self.front = data.get("front",0)
		
			# behind 场景跟随占用0,0点后面像素
			self.behind = data.get("behind",0)
		
			# up 0,0点上面
			self.up = data.get("up",0)
		
			# down 0,0点下面
			self.down = data.get("down",0)
		

# horseskill
class ResHorseskill(object):
	RES_TABLE = "horseskill"
	__slots__ = ("id","skillId","lv","name","cost","attr","icon",)

    def __init__(self):
		
			# id 坐骑技能表
			self.id = 0
		
			# skillId 技能id
			self.skillId = 0
		
			# lv 技能等级
			self.lv = 0
		
			# name 名称
			self.name = ""
		
			# cost 升级消耗道具
			self.cost = []
		
			# attr 属性
			self.attr = []
		
			# icon 图标
			self.icon = ""
		

    def load_from_json(self, data):
		
			# id 坐骑技能表
			self.id = data.get("id",0)
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		
			# lv 技能等级
			self.lv = data.get("lv",0)
		
			# name 名称
			self.name = data.get("name","")
		
			# cost 升级消耗道具
			self.cost = data.get("cost",[])
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# icon 图标
			self.icon = data.get("icon","")
		

# fightDesc
class ResFightDesc(object):
	RES_TABLE = "fightDesc"
	__slots__ = ("type","title","costJumpLv","costJumpVip","costJump","isCostFree","jumpLv","jumpVip","jump","isFree","directJumpLv","directJumpVip","directJump","isDirectFree","desc",)

    def __init__(self):
		
			# type 战斗类型
			self.type = 0
		
			# title 标题
			self.title = ""
		
			# costJumpLv 等级可跳过
			self.costJumpLv = 0
		
			# costJumpVip vip几特权可跳过
			self.costJumpVip = 0
		
			# costJump 第几回合显示跳过按钮
			self.costJump = 0
		
			# isCostFree 是否免费
			self.isCostFree = 0
		
			# jumpLv 等级可跳过
			self.jumpLv = 0
		
			# jumpVip vip几特权可跳过
			self.jumpVip = 0
		
			# jump 第几回合显示跳过按钮
			self.jump = 0
		
			# isFree 是否免费
			self.isFree = 0
		
			# directJumpLv 等级可跳过
			self.directJumpLv = 0
		
			# directJumpVip vip几特权可跳过
			self.directJumpVip = 0
		
			# directJump 第几回合显示跳过按钮
			self.directJump = 0
		
			# isDirectFree 是否免费
			self.isDirectFree = 0
		
			# desc 描述
			self.desc = ""
		

    def load_from_json(self, data):
		
			# type 战斗类型
			self.type = data.get("type",0)
		
			# title 标题
			self.title = data.get("title","")
		
			# costJumpLv 等级可跳过
			self.costJumpLv = data.get("costJumpLv",0)
		
			# costJumpVip vip几特权可跳过
			self.costJumpVip = data.get("costJumpVip",0)
		
			# costJump 第几回合显示跳过按钮
			self.costJump = data.get("costJump",0)
		
			# isCostFree 是否免费
			self.isCostFree = data.get("isCostFree",0)
		
			# jumpLv 等级可跳过
			self.jumpLv = data.get("jumpLv",0)
		
			# jumpVip vip几特权可跳过
			self.jumpVip = data.get("jumpVip",0)
		
			# jump 第几回合显示跳过按钮
			self.jump = data.get("jump",0)
		
			# isFree 是否免费
			self.isFree = data.get("isFree",0)
		
			# directJumpLv 等级可跳过
			self.directJumpLv = data.get("directJumpLv",0)
		
			# directJumpVip vip几特权可跳过
			self.directJumpVip = data.get("directJumpVip",0)
		
			# directJump 第几回合显示跳过按钮
			self.directJump = data.get("directJump",0)
		
			# isDirectFree 是否免费
			self.isDirectFree = data.get("isDirectFree",0)
		
			# desc 描述
			self.desc = data.get("desc","")
		

# teamBarr
class ResTeamBarr(object):
	RES_TABLE = "teamBarr"
	__slots__ = ("id","lv","barrId","mstId",)

    def __init__(self):
		
			# id 组队副本表
			self.id = 0
		
			# lv 开放等级
			self.lv = 0
		
			# barrId 副本id
			self.barrId = 0
		
			# mstId 怪物id(形象展示）
			self.mstId = 0
		

    def load_from_json(self, data):
		
			# id 组队副本表
			self.id = data.get("id",0)
		
			# lv 开放等级
			self.lv = data.get("lv",0)
		
			# barrId 副本id
			self.barrId = data.get("barrId",0)
		
			# mstId 怪物id(形象展示）
			self.mstId = data.get("mstId",0)
		

# petEquipAttr
class ResPetEquipAttr(object):
	RES_TABLE = "petEquipAttr"
	__slots__ = ("id","attrType","baseVal","addVal","vice","q",)

    def __init__(self):
		
			# id 宠物装备属性
			self.id = 0
		
			# attrType 属性类型
			self.attrType = ""
		
			# baseVal 初始生成值
			self.baseVal = 0
		
			# addVal 每强化1级增加值
			self.addVal = 0
		
			# vice 是否副属性
			self.vice = 0
		
			# q 对应品质
			self.q = 0
		

    def load_from_json(self, data):
		
			# id 宠物装备属性
			self.id = data.get("id",0)
		
			# attrType 属性类型
			self.attrType = data.get("attrType","")
		
			# baseVal 初始生成值
			self.baseVal = data.get("baseVal",0)
		
			# addVal 每强化1级增加值
			self.addVal = data.get("addVal",0)
		
			# vice 是否副属性
			self.vice = data.get("vice",0)
		
			# q 对应品质
			self.q = data.get("q",0)
		

# petEquipSuit
class ResPetEquipSuit(object):
	RES_TABLE = "petEquipSuit"
	__slots__ = ("id","suitType","need","attr","skillId",)

    def __init__(self):
		
			# id 宠物装备套装
			self.id = 0
		
			# suitType 套装类型
			self.suitType = 0
		
			# need 需求件数
			self.need = 0
		
			# attr 属性
			self.attr = []
		
			# skillId 技能id
			self.skillId = 0
		

    def load_from_json(self, data):
		
			# id 宠物装备套装
			self.id = data.get("id",0)
		
			# suitType 套装类型
			self.suitType = data.get("suitType",0)
		
			# need 需求件数
			self.need = data.get("need",0)
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# skillId 技能id
			self.skillId = data.get("skillId",0)
		

# petEquipUpgrade
class ResPetEquipUpgrade(object):
	RES_TABLE = "petEquipUpgrade"
	__slots__ = ("id","quality","lv","viceAdd","cost","recycl",)

    def __init__(self):
		
			# id 宠物装备强化
			self.id = 0
		
			# quality 品质
			self.quality = 0
		
			# lv 强化等级
			self.lv = 0
		
			# viceAdd 增加副属性条数
			self.viceAdd = 0
		
			# cost 消耗
			self.cost = []
		
			# recycl 分解返还
			self.recycl = []
		

    def load_from_json(self, data):
		
			# id 宠物装备强化
			self.id = data.get("id",0)
		
			# quality 品质
			self.quality = data.get("quality",0)
		
			# lv 强化等级
			self.lv = data.get("lv",0)
		
			# viceAdd 增加副属性条数
			self.viceAdd = data.get("viceAdd",0)
		
			# cost 消耗
			self.cost = data.get("cost",[])
		
			# recycl 分解返还
			self.recycl = data.get("recycl",[])
		

# equipaddlv
class ResEquipaddlv(object):
	RES_TABLE = "equipaddlv"
	__slots__ = ("id","equipLv","quality","rate",)

    def __init__(self):
		
			# id 装备附加等级表
			self.id = 0
		
			# equipLv 装备阶数
			self.equipLv = 0
		
			# quality 装备品质
			self.quality = 0
		
			# rate 权重
			self.rate = []
		

    def load_from_json(self, data):
		
			# id 装备附加等级表
			self.id = data.get("id",0)
		
			# equipLv 装备阶数
			self.equipLv = data.get("equipLv",0)
		
			# quality 装备品质
			self.quality = data.get("quality",0)
		
			# rate 权重
			self.rate = data.get("rate",[])
		

# zhudaoxunliReward
class ResZhudaoxunliReward(object):
	RES_TABLE = "zhudaoxunliReward"
	__slots__ = ("id","qihao","need","reward","rewardVip",)

    def __init__(self):
		
			# id id
			self.id = 0
		
			# qihao 期号
			self.qihao = 0
		
			# need 需求
			self.need = 0
		
			# reward 固定奖励
			self.reward = []
		
			# rewardVip 特权奖励
			self.rewardVip = []
		

    def load_from_json(self, data):
		
			# id id
			self.id = data.get("id",0)
		
			# qihao 期号
			self.qihao = data.get("qihao",0)
		
			# need 需求
			self.need = data.get("need",0)
		
			# reward 固定奖励
			self.reward = data.get("reward",[])
		
			# rewardVip 特权奖励
			self.rewardVip = data.get("rewardVip",[])
		

# tzdr
class ResTzdr(object):
	RES_TABLE = "tzdr"
	__slots__ = ("id","count","level","quality","attr",)

    def __init__(self):
		
			# id 套装达人表
			self.id = 0
		
			# count 件数
			self.count = 0
		
			# level 等级
			self.level = 0
		
			# quality 品质限制
			self.quality = 0
		
			# attr 加成属性
			self.attr = []
		

    def load_from_json(self, data):
		
			# id 套装达人表
			self.id = data.get("id",0)
		
			# count 件数
			self.count = data.get("count",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# quality 品质限制
			self.quality = data.get("quality",0)
		
			# attr 加成属性
			self.attr = data.get("attr",[])
		

# zhudaoxunliDay
class ResZhudaoxunliDay(object):
	RES_TABLE = "zhudaoxunliDay"
	__slots__ = ("id","start","buyDay","end","charge",)

    def __init__(self):
		
			# id 期号
			self.id = 0
		
			# start 开始天数包含
			self.start = 0
		
			# buyDay 开始n天后可购买等级
			self.buyDay = 0
		
			# end 结束天数包含
			self.end = 0
		
			# charge 充值表id
			self.charge = []
		

    def load_from_json(self, data):
		
			# id 期号
			self.id = data.get("id",0)
		
			# start 开始天数包含
			self.start = data.get("start",0)
		
			# buyDay 开始n天后可购买等级
			self.buyDay = data.get("buyDay",0)
		
			# end 结束天数包含
			self.end = data.get("end",0)
		
			# charge 充值表id
			self.charge = data.get("charge",[])
		

# petEquip
class ResPetEquip(object):
	RES_TABLE = "petEquip"
	__slots__ = ("id","name","needLv","pos","quality","suitType","mainPool","vicePool","viceNum","type","page","chatId",)

    def __init__(self):
		
			# id 宠物装备表
			self.id = 0
		
			# name 物品名称
			self.name = ""
		
			# needLv 穿戴等级
			self.needLv = 0
		
			# pos 部位
			self.pos = 0
		
			# quality 品质
			self.quality = 0
		
			# suitType 套装类型
			self.suitType = 0
		
			# mainPool 主属性池子
			self.mainPool = []
		
			# vicePool 副属性池子
			self.vicePool = []
		
			# viceNum 初始副属性条数
			self.viceNum = []
		
			# type 类型
			self.type = 0
		
			# page 分页
			self.page = 0
		
			# chatId 广播ID
			self.chatId = 0
		

    def load_from_json(self, data):
		
			# id 宠物装备表
			self.id = data.get("id",0)
		
			# name 物品名称
			self.name = data.get("name","")
		
			# needLv 穿戴等级
			self.needLv = data.get("needLv",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# quality 品质
			self.quality = data.get("quality",0)
		
			# suitType 套装类型
			self.suitType = data.get("suitType",0)
		
			# mainPool 主属性池子
			self.mainPool = data.get("mainPool",[])
		
			# vicePool 副属性池子
			self.vicePool = data.get("vicePool",[])
		
			# viceNum 初始副属性条数
			self.viceNum = data.get("viceNum",[])
		
			# type 类型
			self.type = data.get("type",0)
		
			# page 分页
			self.page = data.get("page",0)
		
			# chatId 广播ID
			self.chatId = data.get("chatId",0)
		

# equip
class ResEquip(object):
	RES_TABLE = "equip"
	__slots__ = ("id","name","type","pos","level","quality","skills","page","attr","godAttr","godNextId","godUpgradeCost","recycl1","recycl2","recycl3","chatId",)

    def __init__(self):
		
			# id 装备表
			self.id = 0
		
			# name 物品名称
			self.name = ""
		
			# type 类型
			self.type = 0
		
			# pos 部位
			self.pos = 0
		
			# level 等级
			self.level = 0
		
			# quality 品质
			self.quality = 0
		
			# skills 技能列表
			self.skills = []
		
			# page 分页
			self.page = 0
		
			# attr 属性
			self.attr = []
		
			# godAttr 神装极品属性
			self.godAttr = []
		
			# godNextId 神装下级装备id
			self.godNextId = 0
		
			# godUpgradeCost 神装升级消耗
			self.godUpgradeCost = []
		
			# recycl1 装备熔炼
			self.recycl1 = []
		
			# recycl2 法宝分解
			self.recycl2 = []
		
			# recycl3 神装分解
			self.recycl3 = []
		
			# chatId 广播ID
			self.chatId = 0
		

    def load_from_json(self, data):
		
			# id 装备表
			self.id = data.get("id",0)
		
			# name 物品名称
			self.name = data.get("name","")
		
			# type 类型
			self.type = data.get("type",0)
		
			# pos 部位
			self.pos = data.get("pos",0)
		
			# level 等级
			self.level = data.get("level",0)
		
			# quality 品质
			self.quality = data.get("quality",0)
		
			# skills 技能列表
			self.skills = data.get("skills",[])
		
			# page 分页
			self.page = data.get("page",0)
		
			# attr 属性
			self.attr = data.get("attr",[])
		
			# godAttr 神装极品属性
			self.godAttr = data.get("godAttr",[])
		
			# godNextId 神装下级装备id
			self.godNextId = data.get("godNextId",0)
		
			# godUpgradeCost 神装升级消耗
			self.godUpgradeCost = data.get("godUpgradeCost",[])
		
			# recycl1 装备熔炼
			self.recycl1 = data.get("recycl1",[])
		
			# recycl2 法宝分解
			self.recycl2 = data.get("recycl2",[])
		
			# recycl3 神装分解
			self.recycl3 = data.get("recycl3",[])
		
			# chatId 广播ID
			self.chatId = data.get("chatId",0)
		

# niudan
class ResNiudan(object):
	RES_TABLE = "niudan"
	__slots__ = ("id","byWeight","byFreeForbid","ybWeight","ybFreeForbid","ybActForbid","reward","jp","yb","limit","chatId",)

    def __init__(self):
		
			# id 扭蛋表
			self.id = 0
		
			# byWeight 绑元权重
			self.byWeight = 0
		
			# byFreeForbid 绑元免费限制
			self.byFreeForbid = 0
		
			# ybWeight 元宝权重
			self.ybWeight = 0
		
			# ybFreeForbid 元宝免费限制
			self.ybFreeForbid = 0
		
			# ybActForbid 元宝宠物激活限制
			self.ybActForbid = 0
		
			# reward 奖励
			self.reward = []
		
			# jp 是否极品
			self.jp = 0
		
			# yb 元宝限制
			self.yb = 0
		
			# limit 抽中上限
			self.limit = 0
		
			# chatId 聊天模板id
			self.chatId = 0
		

    def load_from_json(self, data):
		
			# id 扭蛋表
			self.id = data.get("id",0)
		
			# byWeight 绑元权重
			self.byWeight = data.get("byWeight",0)
		
			# byFreeForbid 绑元免费限制
			self.byFreeForbid = data.get("byFreeForbid",0)
		
			# ybWeight 元宝权重
			self.ybWeight = data.get("ybWeight",0)
		
			# ybFreeForbid 元宝免费限制
			self.ybFreeForbid = data.get("ybFreeForbid",0)
		
			# ybActForbid 元宝宠物激活限制
			self.ybActForbid = data.get("ybActForbid",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# jp 是否极品
			self.jp = data.get("jp",0)
		
			# yb 元宝限制
			self.yb = data.get("yb",0)
		
			# limit 抽中上限
			self.limit = data.get("limit",0)
		
			# chatId 聊天模板id
			self.chatId = data.get("chatId",0)
		

# godpetPool
class ResGodpetPool(object):
	RES_TABLE = "godpetPool"
	__slots__ = ("id","weight","reward","record","chatId",)

    def __init__(self):
		
			# id 神宠转盘奖池表
			self.id = 0
		
			# weight 权重
			self.weight = 0
		
			# reward 奖励
			self.reward = []
		
			# record 是否记录
			self.record = 0
		
			# chatId 聊天模板id
			self.chatId = 0
		

    def load_from_json(self, data):
		
			# id 神宠转盘奖池表
			self.id = data.get("id",0)
		
			# weight 权重
			self.weight = data.get("weight",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# record 是否记录
			self.record = data.get("record",0)
		
			# chatId 聊天模板id
			self.chatId = data.get("chatId",0)
		

# xingyunPool
class ResXingyunPool(object):
	RES_TABLE = "xingyunPool"
	__slots__ = ("id","byWeight","ybWeight","reward","viewSort","jp","yb","limit","record","chatId",)

    def __init__(self):
		
			# id 幸运转盘表
			self.id = 0
		
			# byWeight 绑元权重
			self.byWeight = 0
		
			# ybWeight 元宝权重
			self.ybWeight = 0
		
			# reward 奖励
			self.reward = []
		
			# viewSort 显示排序
			self.viewSort = 0
		
			# jp 是否极品
			self.jp = 0
		
			# yb 元宝限制
			self.yb = 0
		
			# limit 上限
			self.limit = 0
		
			# record 是否记录
			self.record = 0
		
			# chatId 聊天模板id
			self.chatId = 0
		

    def load_from_json(self, data):
		
			# id 幸运转盘表
			self.id = data.get("id",0)
		
			# byWeight 绑元权重
			self.byWeight = data.get("byWeight",0)
		
			# ybWeight 元宝权重
			self.ybWeight = data.get("ybWeight",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# viewSort 显示排序
			self.viewSort = data.get("viewSort",0)
		
			# jp 是否极品
			self.jp = data.get("jp",0)
		
			# yb 元宝限制
			self.yb = data.get("yb",0)
		
			# limit 上限
			self.limit = data.get("limit",0)
		
			# record 是否记录
			self.record = data.get("record",0)
		
			# chatId 聊天模板id
			self.chatId = data.get("chatId",0)
		

# xunbao
class ResXunbao(object):
	RES_TABLE = "xunbao"
	__slots__ = ("id","byWeight","ybWeight","reward","viewSort","jp","yb","limit","record","chatId",)

    def __init__(self):
		
			# id 寻宝表
			self.id = 0
		
			# byWeight 绑元权重
			self.byWeight = 0
		
			# ybWeight 元宝权重
			self.ybWeight = 0
		
			# reward 奖励
			self.reward = []
		
			# viewSort 显示排序
			self.viewSort = 0
		
			# jp 是否极品
			self.jp = 0
		
			# yb 元宝限制
			self.yb = 0
		
			# limit 抽中上限
			self.limit = 0
		
			# record 是否记录
			self.record = 0
		
			# chatId 聊天模板id
			self.chatId = 0
		

    def load_from_json(self, data):
		
			# id 寻宝表
			self.id = data.get("id",0)
		
			# byWeight 绑元权重
			self.byWeight = data.get("byWeight",0)
		
			# ybWeight 元宝权重
			self.ybWeight = data.get("ybWeight",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# viewSort 显示排序
			self.viewSort = data.get("viewSort",0)
		
			# jp 是否极品
			self.jp = data.get("jp",0)
		
			# yb 元宝限制
			self.yb = data.get("yb",0)
		
			# limit 抽中上限
			self.limit = data.get("limit",0)
		
			# record 是否记录
			self.record = data.get("record",0)
		
			# chatId 聊天模板id
			self.chatId = data.get("chatId",0)
		

# xingyun
class ResXingyun(object):
	RES_TABLE = "xingyun"
	__slots__ = ("id","poolType","rewardPool",)

    def __init__(self):
		
			# id 幸运转盘周期表
			self.id = 0
		
			# poolType 转盘类型
			self.poolType = 0
		
			# rewardPool 奖池
			self.rewardPool = []
		

    def load_from_json(self, data):
		
			# id 幸运转盘周期表
			self.id = data.get("id",0)
		
			# poolType 转盘类型
			self.poolType = data.get("poolType",0)
		
			# rewardPool 奖池
			self.rewardPool = data.get("rewardPool",[])
		

# cycleNiudanRank
class ResCycleNiudanRank(object):
	RES_TABLE = "cycleNiudanRank"
	__slots__ = ("id","cycleId","rankReward","min","max",)

    def __init__(self):
		
			# id 限时扭蛋排名表
			self.id = 0
		
			# cycleId 周期
			self.cycleId = 0
		
			# rankReward 排名奖励
			self.rankReward = []
		
			# min 最小排名
			self.min = 0
		
			# max 最大排名
			self.max = 0
		

    def load_from_json(self, data):
		
			# id 限时扭蛋排名表
			self.id = data.get("id",0)
		
			# cycleId 周期
			self.cycleId = data.get("cycleId",0)
		
			# rankReward 排名奖励
			self.rankReward = data.get("rankReward",[])
		
			# min 最小排名
			self.min = data.get("min",0)
		
			# max 最大排名
			self.max = data.get("max",0)
		

# cycleNiudan
class ResCycleNiudan(object):
	RES_TABLE = "cycleNiudan"
	__slots__ = ("id","rewardPool","taskList","TacoFace",)

    def __init__(self):
		
			# id 限时扭蛋周期表
			self.id = 0
		
			# rewardPool 奖池
			self.rewardPool = []
		
			# taskList 任务列表
			self.taskList = []
		
			# TacoFace 每次登陆大脸图(每天多少次)
			self.TacoFace = 0
		

    def load_from_json(self, data):
		
			# id 限时扭蛋周期表
			self.id = data.get("id",0)
		
			# rewardPool 奖池
			self.rewardPool = data.get("rewardPool",[])
		
			# taskList 任务列表
			self.taskList = data.get("taskList",[])
		
			# TacoFace 每次登陆大脸图(每天多少次)
			self.TacoFace = data.get("TacoFace",0)
		

# cycleNiudanPool
class ResCycleNiudanPool(object):
	RES_TABLE = "cycleNiudanPool"
	__slots__ = ("id","weight","freeForbid","reward","yb","limit","chatId",)

    def __init__(self):
		
			# id 扭蛋表
			self.id = 0
		
			# weight 权重
			self.weight = 0
		
			# freeForbid 免费限制
			self.freeForbid = 0
		
			# reward 奖励
			self.reward = []
		
			# yb 元宝限制
			self.yb = 0
		
			# limit 抽中上限
			self.limit = 0
		
			# chatId 聊天模板id
			self.chatId = 0
		

    def load_from_json(self, data):
		
			# id 扭蛋表
			self.id = data.get("id",0)
		
			# weight 权重
			self.weight = data.get("weight",0)
		
			# freeForbid 免费限制
			self.freeForbid = data.get("freeForbid",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		
			# yb 元宝限制
			self.yb = data.get("yb",0)
		
			# limit 抽中上限
			self.limit = data.get("limit",0)
		
			# chatId 聊天模板id
			self.chatId = data.get("chatId",0)
		

# cycleNiudanBx
class ResCycleNiudanBx(object):
	RES_TABLE = "cycleNiudanBx"
	__slots__ = ("id","times","cycleId","reward",)

    def __init__(self):
		
			# id 限时扭蛋宝箱表
			self.id = 0
		
			# times 次数
			self.times = 0
		
			# cycleId 周期
			self.cycleId = 0
		
			# reward 奖励
			self.reward = []
		

    def load_from_json(self, data):
		
			# id 限时扭蛋宝箱表
			self.id = data.get("id",0)
		
			# times 次数
			self.times = data.get("times",0)
		
			# cycleId 周期
			self.cycleId = data.get("cycleId",0)
		
			# reward 奖励
			self.reward = data.get("reward",[])
		

# niudanRewardCheak
class ResNiudanRewardCheak(object):
	RES_TABLE = "niudanRewardCheak"
	__slots__ = ("id",)

    def __init__(self):
		
			# id 奖励行
			self.id = 0
		

    def load_from_json(self, data):
		
			# id 奖励行
			self.id = data.get("id",0)
		

# godpet
class ResGodpet(object):
	RES_TABLE = "godpet"
	__slots__ = ("id","next_id","rewardPool",)

    def __init__(self):
		
			# id 神宠转盘周期表
			self.id = 0
		
			# next_id 下期id
			self.next_id = 0
		
			# rewardPool 奖池
			self.rewardPool = []
		

    def load_from_json(self, data):
		
			# id 神宠转盘周期表
			self.id = data.get("id",0)
		
			# next_id 下期id
			self.next_id = data.get("next_id",0)
		
			# rewardPool 奖池
			self.rewardPool = data.get("rewardPool",[])
		

# diamondMining
class ResDiamondMining(object):
	RES_TABLE = "diamondMining"
	__slots__ = ("id","pos","reward","limit","odds","costneed","titleImg","bgImg","notice",)

    def __init__(self):
		
			# id 组队副本表
			self.id = 0
		
			# pos 使用奖池百分比
			self.pos = 0
		
			# reward 固定奖励
			self.reward = []
		
			# limit 得奖限制
			self.limit = 0
		
			# odds 权重
			self.odds = 0
		
			# costneed 暗箱需求
			self.costneed = 0
		
			# titleImg 奖励等级图片
			self.titleImg = ""
		
			# bgImg 奖励等级背景图片
			self.bgImg = ""
		
			# notice 公告Id
			self.notice = 0
		

    def load_from_json(self, data):
		
			# id 组队副本表
			self.id = data.get("id",0)
		
			# pos 使用奖池百分比
			self.pos = data.get("pos",0)
		
			# reward 固定奖励
			self.reward = data.get("reward",[])
		
			# limit 得奖限制
			self.limit = data.get("limit",0)
		
			# odds 权重
			self.odds = data.get("odds",0)
		
			# costneed 暗箱需求
			self.costneed = data.get("costneed",0)
		
			# titleImg 奖励等级图片
			self.titleImg = data.get("titleImg","")
		
			# bgImg 奖励等级背景图片
			self.bgImg = data.get("bgImg","")
		
			# notice 公告Id
			self.notice = data.get("notice",0)
		