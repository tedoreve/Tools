import re
import bs4
import requests
import numpy as np
import pandas as pd
import time

# request主页信息并用beautifulsoup处理
mainpageRes = requests.get('https://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&jl=北京&p=1')
mainpageRes.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(mainpageRes.text, "lxml")
# 获取自标签对应网址，并用正则表达式获取标签对应的代号
tagHtml = noStarchSoup.select('#search_jobtype_tag a[class=""]')[1:]
tags = [i.get('href') for i in tagHtml]
tagRegex = re.compile(r'sj=\d\d')
tagCodes = [tagRegex.search(i).group() for i in tags]

columns = ['工作名称', '公司名称', '公司规模', '公司性质', '月薪', '工作经验', '招聘人数', '最低学历', '工作性质',
           '五险一金', '带薪休假', '员工旅游', '周末双休', '弹性工作', '餐补', '交通补助', '年底双薪', '股票期权']
index = range(50000)
table = pd.DataFrame(index=index, columns=columns)
count = 0
# 分别获取子标签首页页面信息
mainAddress = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&ispts=1&isfilter=1&bj=160000' 
for k in range(len(tagCodes)):
    tagRes = requests.get(mainAddress + '&p1' + '&' + tagCodes[k])
    tagRes.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(tagRes.text, "lxml")
    # 获取总工作数和首页信息行书数，计算最大页数，因智联限制最大页数为90，故页数大于90的按90算
    jobNum = int(noStarchSoup.select(
        'body > div.main > div.search_newlist_main > div.seach_yx > span.search_yx_tj > em')[0].getText())
    jobs = noStarchSoup.select(
        '#newlist_list_content_table > table.newlist a[style="font-weight: bold"]')
    pages = int(np.ceil(jobNum/len(jobs)))
    if pages >= 90:
        pages = 90
    # 分别获取每页每行的工作的详情页面地址
    for i in range(pages):
        tagRes = requests.get(mainAddress + '&p{0}'.format(i+1) + '&' + tagCodes[k])
        tagRes.raise_for_status()
        noStarchSoup = bs4.BeautifulSoup(tagRes.text, "lxml")
        jobs = noStarchSoup.select(
            '#newlist_list_content_table > table.newlist a[style="font-weight: bold"]')
        # 分析页面信息，获取题目中工作的各方面信息并转化为需要的格式
        for j in range(len(jobs)):
            url = jobs[j].get('href')
            jobRes = requests.get(url)
            jobRes.raise_for_status()
            jobSoup = bs4.BeautifulSoup(jobRes.text, "lxml")
            salary = jobSoup.select('body > div.terminalpage.clearfix > div.terminalpage-left > ul > li strong')[0].getText()
            money = re.findall("\d+",salary)
            if len(money) == 1:
                salary = int(money)
            elif len(money) == 2:
                salary = (int(money[0]) + int(money[1]))/2
            else:
                continue
            jobName = jobSoup.select('body div.top-fixed-box div.fixed-inner-box > div.inner-left.fl h1')[0].getText()
            comName = jobSoup.select('body div.top-fixed-box div.fixed-inner-box > div.inner-left.fl h2')[0].getText()
            comProp = jobSoup.select(
                'body > div.terminalpage.clearfix > div.terminalpage-right > div.company-box > ul > li strong')[1].getText()
            comScale = jobSoup.select(
                'body > div.terminalpage.clearfix > div.terminalpage-right > div.company-box > ul > li strong')[0].getText()
            infolist1 = jobSoup.select('body > div.terminalpage.clearfix > div.terminalpage-left > ul > li strong')
            jobType = infolist1[3].getText()
            jobExp = infolist1[4].getText()
            education = infolist1[5].getText()
            workerNum = int(re.findall("\d+",infolist1[6].getText())[0])
            welfare = jobSoup.select('body div.top-fixed-box div.fixed-inner-box > div.inner-left.fl div')[0].getText()
            w1 = '五险一金' in welfare
            w2 = '带薪休假' in welfare
            w3 = '员工旅游' in welfare
            w4 = '周末双休' in welfare
            w5 = '弹性工作' in welfare
            w6 = '餐补' in welfare
            w7 = '交通补助' in welfare
            w8 = '年底双薪' in welfare
            w9 = '股票期权' in welfare
            datalist = [jobName, comName, comScale, comProp, salary, jobExp, workerNum, education, jobType, 
                        w1, w2, w3, w4, w5, w6, w7, w8, w9]
            table.loc[count] = datalist
            count = count + 1
            print(count)
table.to_csv('zlzp.csv')
