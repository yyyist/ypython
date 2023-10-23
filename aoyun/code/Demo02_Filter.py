import pandas as pd
df=pd.DataFrame()
with open("C:\\Users\\No_alopecia\\IdeaProjects\\aoyun\data\\对照表.txt",encoding="utf-8") as f:
    lines=f.read().replace('"',"")
    line_list=lines.split(",\n  ")

for i in  line_list:
    k=i.split(": ")[0]
    v=i.split(": ")[1]
    # 数据结构化
    data=[[k,v]]
    df=df.append(data)

df.columns=["englishName","countryName"]
data=pd.read_csv("C:\\Users\\No_alopecia\\IdeaProjects\\aoyun\data\\countrySum.txt",
                 header=None,
                 names=["countryName","rank","goldMedalNum","silverMedalNum","bronzeMedalNum","totalMedalNum"])
data=pd.merge(data,df,on="countryName")
data.to_csv("C:\\Users\\No_alopecia\\IdeaProjects\\aoyun\\data\\data.txt",
            index=None,
            header=None)