import pandas as pd
from pyecharts.charts import Map
from pyecharts.charts import Pie
from pyecharts.charts import Bar
from pyecharts import options as opts
data=pd.read_csv("C:\\Users\\No_alopecia\\IdeaProjects\\aoyun\\data\\data.txt",
            header=None,
            names=["countryName","rank","goldMedalNum","silverMedalNum","bronzeMedalNum","totalMedalNum","englishName"])

#把获取的数据 处理成map可以识别的格式
def create_Map():
    data_list=[[k,v] for k,v in zip(data["englishName"],data["totalMedalNum"])]
    m=(
        Map()
        .add("",data_list,"world",is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="2021年奥运会获奖总数"),
                         visualmap_opts=opts.VisualMapOpts(min_=1,max_=120))
    )
    # m.render("C:\\Users\\admin\\ideaprojects\\SpiderTest\\SpiderTest\\data\\countrymap.html")
    return m

def create_Bar():
    b=(
        Bar()
        .add_xaxis(data["countryName"].head(20).tolist())
        .add_yaxis("金牌",data["goldMedalNum"].head(20).tolist(),stack="stack1")
        .add_yaxis("银牌",data["silverMedalNum"].head(20).tolist(),stack="stack1")
        .add_yaxis("铜牌",data["bronzeMedalNum"].head(20).tolist(),stack="stack1")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True,font_size=12,position="inside"))
        .set_global_opts(title_opts=opts.TitleOpts(title="2021奥运会获奖数"),
                         xaxis_opts=opts.AxisOpts(type_="category",
                                                  axislabel_opts=opts.LabelOpts(rotate=45)))
    )
    # b.render("C:\\Users\\admin\\ideaprojects\\SpiderTest\\SpiderTest\\data\\countrybar.html")
    return b

# 画饼图
def create_Pie():
    data1=data.head(20)
    data_list=[[k,v] for k,v in zip(data1["countryName"],data1["totalMedalNum"])]
    # data_list.head(20)
    p=(
        Pie()
        .add("",data_list,radius=[160,200])
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    # p.render("C:\\Users\\admin\\ideaprojects\\SpiderTest\\SpiderTest\\data\\countrypie.html")
    return p

# 使用Page需要在conda环境中 下载
# pip install --upgrade jinja2
from pyecharts.charts  import Page

page=Page(layout=Page.DraggablePageLayout,page_title="2021奥运会奖牌数据")
page.add(
    create_Map(),
    create_Pie(),
    create_Bar()
)
page.render("C:\\Users\\No_alopecia\\IdeaProjects\\aoyun\\html\\page.html")
