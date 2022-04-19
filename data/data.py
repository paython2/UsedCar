import random

# 单品
edit_data = [
    {
        "auctionName": "商品编号-{}".format(random.randint(1, 100)),
        "auctionSimple": "ck01",
        "supplierId": 1,
        "viewTargetCustomerTypes": 1,
        "bidTargetCustomerTypes": 1,
        "auctionType": 2,
        "batchNum": '',
        "supplierName": "首汽租赁",
        "auctionPic": "https://sqzl-img.oss-cn-beijing.aliyuncs.com/pc/test/secondHand/auction/f8c99a4fea0d4be9.png",
        "auctionPicsDetail": "https://sqzl-img.oss-cn-beijing.aliyuncs.com/pc/test/secondHand/auction/41f5ef32a1f24d3f.png",
        "minimumAddPrice": 1000,
        "hiddenRetainPrice": 1,
        "descr": 123,
        "delaySupport": 0,
        "delayPeriod": '',
        "ensurePriceSingle": 1000,
    },
]

# 包!
edit_data1 = [
    {
        "auctionName": "商品编号-{}".format(random.randint(200, 300)),
        "auctionSimple": "ck01",
        "supplierId": 1,
        "viewTargetCustomerTypes": 1,
        "bidTargetCustomerTypes": 1,
        "auctionType": 1,
        "batchNum": '',
        "supplierName": "首汽租赁",
        "auctionPic": "https://sqzl-img.oss-cn-beijing.aliyuncs.com/pc/test/secondHand/auction/f8c99a4fea0d4be9.png",
        "auctionPicsDetail": "https://sqzl-img.oss-cn-beijing.aliyuncs.com/pc/test/secondHand/auction/41f5ef32a1f24d3f.png",
        "minimumAddPrice": 1000,
        "hiddenRetainPrice": 1,
        "descr": 123,
        "delaySupport": 1,
        "delayPeriod": 24,
        "ensurePriceSingle": 1000,
    },
]

import datetime

# 当前时间
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# 多加3分钟
upperTime = (datetime.datetime.now() + datetime.timedelta(minutes=3)).strftime("%Y-%m-%d %H:%M:%S")
# 多加5分钟
auctionTime = (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
# 多加7分钟
endTime = (datetime.datetime.now() + datetime.timedelta(minutes=7)).strftime("%Y-%m-%d %H:%M:%S")

edit_data2 = [{
    "upperTime": f"{upperTime}",
    "auctionTime": f"{auctionTime}",
    "endTime": f"{endTime}",
    "auctionSubmit": 1,
    "auctionBatchName": "批次-{}".format(random.randint(1, 100)),
    "needEstimate": 0,
    "noEstimateReason": "123123",
    "payBatchName": "批次-{}".format(random.randint(1, 100)),
    "msgSendType": 1
}]

# print(edit_data2)
