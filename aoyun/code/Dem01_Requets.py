import requests

import pandas as pd
url="https://app-sc.miguvideo.com/vms-livedata/olympic-medal/total-table/15/110000004609"
data=requests.get(url).json()
# 数据处理 获取想要的数据 国家countryName 排名rank 金牌goldMedalNum 银牌silverMedalNum 铜牌bronzeMedalNum 总数totalMedalNum
data=data["body"]["allMedalData"]
df=pd.DataFrame()
for country in data:
    countryName=country['countryName']
    rank=country['rank']
    goldMedalNum=country['goldMedalNum']
    silverMedalNum=country['silverMedalNum']
    bronzeMedalNum=country['bronzeMedalNum']
    totalMedalNum=country['totalMedalNum']
    # 结构化数据
    country_data=[[countryName,rank,goldMedalNum,silverMedalNum,bronzeMedalNum,totalMedalNum]]
    df=df.append(country_data)
df.columns=["countryName","rank","goldMedalNum","silverMedalNum","bronzeMedalNum","totalMedalNum"]
df.to_csv("C:\\Users\\No_alopecia\\IdeaProjects\\aoyun\data\\countrySum.txt",
          header=None,
          index=None)