# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:24:35 2015

@author: tedoreve
"""
import pandas  as pd
import tushare as ts
import numpy as np

s=open('C:/Users/tedoreve/Documents/Python_Scripts/data/stocks.txt','r')
p=s.read()
#==============================================================================
# 交易数据'line', 'bar', 'barh', 'kde', 'density', 'area', scatter', 'hexbin'
#==============================================================================
#df=ts.get_hist_data('600848')             #一次性获取全部日k线数据

#for i in range(1081,1120):
#    df=ts.get_h_data(str(p[i*7:i*7+6]),start='2009-11-12',end='2015-11-12')   #获取周k线数据
#    df[['open','close']].plot(kind='line',title=str(p[i*7:i*7+6]))
#df=ts.get_hist_data('600848',ktype='M')   #获取月k线数据
#df=ts.get_hist_data('600848',ktype='5')   #获取5分钟k线数据
#ts.get_hist_data('600848',ktype='15')     #获取15分钟k线数据
#ts.get_hist_data('600848',ktype='30')     #获取30分钟k线数据
#df=ts.get_hist_data('000425',ktype='60')  #获取60分钟k线数据
#df=ts.get_hist_data('sh')                 #获取上证指数k线数据，其它参数与个股一致，下同
#df=ts.get_hist_data('sz')                 #获取深圳成指k线数据
#df=ts.get_hist_data('hs300')                 #获取沪深300指数k线数据
#ts.get_hist_data('sz50')                  #获取上证50指数k线数据
#df=ts.get_hist_data('zxb')                   #获取中小板指数k线数据
#ts.get_hist_data('cyb')                   #获取创业板指数k线数据
    
#df = ts.get_stock_basics()
#date = df.ix['600848']['timeToMarket'] #上市日期YYYYMMDD
#
df=ts.get_h_data('002292',start='2000-11-12',end='2015-11-12')                #前复权
df[['open','close']].plot(kind='line')
#ts.get_h_data('002337',autype='hfq')   #后复权
#ts.get_h_data('002337',autype=None)    #不复权
#ts.get_h_data('002337',start='2015-01-01',end='2015-03-16') #两个日期之间的前复权数据
#
#df=ts.get_h_data('000425', index=True)    #深圳综合指数
#df=ts.get_today_all()                     #实时行情

#
#df = ts.get_tick_data('600848',date='2014-01-09')
#df.head(10)                            #历史分笔
#df = ts.get_today_ticks('601333')
#df.head(10)                            #当日历史分笔
#df = ts.get_realtime_quotes('000581') #Single stock symbol
#df[['code','name','price','bid','ask','volume','amount','time']] #实时分笔
#
#df = ts.get_index()                    #大盘行情
#==============================================================================
# 投资参考数据
#==============================================================================
#df = ts.profit_data(top=60)
#df.sort('shares',ascending=False)      #分配预案
#ts.forecast_data(2014,2)               #业绩预告
#
#ts.xsg_data()                          #限售股解禁
#ts.fund_holdings(2014, 4)              #基金持股
#ts.new_stocks()                        #新股数据
#
#ts.sh_margins(start='2015-01-01', end='2015-04-19')                        #融资融券（沪市）
#ts.sh_margin_details(start='2015-01-01', end='2015-04-19', symbol='601989')#融资融券（沪市细节）
#ts.sz_margins(start='2015-01-01', end='2015-04-19')                        #融资融券（深市）
#ts.sz_margin_details('2015-04-20')
#深市融资融券明细一次只能获取一天的明细数据，如果不输入参数，则为最近一个交易日的明细数据
#==============================================================================
# 股票分类数据
#==============================================================================
#ts.get_industry_classified()           #行业分类
#ts.get_concept_classified()            #概念分类
#ts.get_area_classified()               #地域分类
#ts.get_sme_classified()                #中小版分类
#ts.get_gem_classified()                #创业版分类
#ts.get_st_classified()                 #风险警示版分类
#ts.get_hs300s()                        #沪深300成分及权重
#ts.get_sz50s()                         #上证50成分股
#ts.get_zz500s()                        #中证500成分股
#ts.get_terminated()                    #终止上市股票列表
#ts.get_suspended()                     #暂停上市股票列表
#==============================================================================
# 基本面数据
#==============================================================================
#ts.get_stock_basics()                  #股票列表
#ts.get_report_data(2014,3)             #业绩报告（主表）
#ts.get_profit_data(2014,3)             #盈利能力
#ts.get_operation_data(2014,3)          #营运能力
#ts.get_growth_data(2014,3)             #成长能力
#ts.get_debtpaying_data(2014,3)         #偿债能力
#ts.get_cashflow_data(2014,3)           #现金流量
#==============================================================================
#宏观经济数据 
#==============================================================================
#ts.get_deposit_rate()                  #存款利率
#ts.get_loan_rate()                     #贷款利率
#ts.get_rrr()                           #存款准备金率
#ts.get_money_supply()                  #货币供应量
#ts.get_money_supply_bal()              #货币供应量（年底余额）
#ts.get_gdp_year()                      #国内生产总值（年度）
#ts.get_gdp_quarter()                   #国内生产总值（季度）
#ts.get_gdp_for()                       #三大需求对GDP贡献
#ts.get_gdp_pull()                      #三大产业对GDP拉动
#ts.get_gdp_contrib()                   #三大产业贡献率
#ts.get_cpi()                           #居民消费价格指数
#ts.get_ppi()                           #工业品出厂价格指数
#==============================================================================
# 新闻事件数据
#==============================================================================
#ts.get_latest_news()                   #默认获取最近80条新闻数据，只提供新闻类型、链接和标题
#ts.get_latest_news(top=5,show_content=True) #显示最新5条新闻，并打印出新闻内容
#ts.get_notices()                       #信息地雷
#ts.guba_sina()                         #新浪股吧
#==============================================================================
# 龙虎榜数据
#==============================================================================
#ts.top_list('2015-06-12')              #每日龙虎榜列表
#ts.cap_tops()                          #个股上榜统计
#ts.broker_tops()                       #营业部上榜统计
#ts.inst_tops()                         #机构席位追踪
#ts.inst_detail()                       #机构成交明细
#==============================================================================
# 银行间同业拆放利率
#==============================================================================
#----------------------------------------------------Shibor拆放利率
#df = ts.shibor_data()                  #取当前年份的数据
##df = ts.shibor_data(2014)             #取2014年的数据
#df.sort('date', ascending=False).head(10)
#-----------------------------------------------------银行报价数据
#df = ts.shibor_quote_data()            #取当前年份的数据
##df = ts.shibor_quote_data(2014)       #取2014年的数据
#df.sort('date', ascending=False).head(10)
# ----------------------------------------------------Shibor均值数据
#df = ts.shibor_ma_data()               #取当前年份的数据
##df = ts.shibor_ma_data(2014)          #取2014年的数据
#df.sort('date', ascending=False).head(10)
#-----------------------------------------------------贷款基础利率（LPR）
#df = ts.lpr_data()                     #取当前年份的数据
##df = ts.lpr_data(2014)                #取2014年的数据
#df.sort('date', ascending=False).head(10)
#-----------------------------------------------------LPR均值数据
#df = ts.lpr_ma_data()                  #取当前年份的数据
##df = ts.lpr_ma_data(2014)             #取2014年的数据
#df.sort('date', ascending=False).head(10)
#==============================================================================
# 数据存储
#==============================================================================
#------------------------------------------------------CSV
#df = ts.get_hist_data('000875')
#                                       #直接保存
#df.to_csv('c:/day/000875.csv')
#                                       #选择保存
#df.to_csv('c:/day/000875.csv',columns=['open','high','low','close'])
#------------------------------------------------------EXCEL
#df = ts.get_hist_data('000875')
#                                       #直接保存
#df.to_excel('c:/day/000875.xlsx')
#                                       #设定数据位置（从第3行，第6列开始插入数据）
#df.to_excel('c:/day/000875.xlsx', startrow=2,startcol=5)
#------------------------------------------------------MySQL数据库
#from sqlalchemy import create_engine
#df = ts.get_tick_data('600848', date='2014-12-22')
#engine = create_engine('mysql://user:passwd@127.0.0.1/db_name?charset=utf8')
#                                       #存入数据库
#df.to_sql('tick_data',engine)
#                                       #追加数据到现有表
##df.to_sql('tick_data',engine,if_exists='append')
#==============================================================================
# 联通数据token：3600597193ee883ec10124c460bdef9d008dbb8037f4aef389a4130f598825f8
#==============================================================================
##---------------------------------------------------------调用方法
#ts.set_token('3600597193ee883ec10124c460bdef9d008dbb8037f4aef389a4130f598825f8')#设置token
#ts.get_token()#查看token
#mkt = ts.Market() 
#df = mkt.TickRTSnapshot(securityID=‘000001.XSHE’)#获取某类数据
##---------------------------------------------------------证券概况
##获取一段时间内的日期是否为交易日，isOpen=1是交易日，isOpen=0为休市
#mt = ts.Master()
#df = mt.TradeCal(exchangeCD='XSHG', beginDate='20150928', endDate='20151010', field='calendarDate,isOpen,prevTradeDate')
##---------------------------------------------------------行情数据
##获取历史某一日股票行情数据，包括了停牌股票（停牌的报价都是0）
#st = ts.Market()
#df = st.MktEqud(tradeDate='20150917', field='ticker,secShortName,preClosePrice,openPrice,highestPrice,lowestPrice,closePrice,turnoverVol,turnoverRate')
#df['ticker'] = df['ticker'].map(lambda x: str(x).zfill(6))
##----------------------------------------------------------基本面数据
#bd = ts.Fundamental()
#df = bd.FdmtBS(ticker='600848', field='ticker,TCA,fixedAssets,inventories,intanAssets')
##----------------------------------------------------------股票信息
##获取沪深A股正常股票信息，listStatusCD上市状态，可选状态有L——上市，S——暂停，DE——已退市，UN——未上市
#eq = ts.Equity()
#df = eq.Equ(equTypeCD='A', listStatusCD='L', field='ticker,secShortName,totalShares,nonrestFloatShares')
#df['ticker'] = df['ticker'].map(lambda x: str(x).zfill(6))
##----------------------------------------------------------港股信息
##获取港股信息
#hk = ts.HKequity()
#df = hk.HKEqu(listStatusCD='L', field='secShortName,listDate,tradingUnit,partyID')
#df = df.sort('listDate', ascending=False)
##----------------------------------------------------------基金信息
##获取基金的净值调整信息，包括基金分红和基金拆分两种调整情况
#fd = ts.Fund()
#df = fd.FundDiv(ticker='184688', adjustedType='D',beginDate='20000101', field='secShortName,effectDate,publishDate,dividendAfTax,dividendBfTax')
##----------------------------------------------------------期货信息
#fd = ts.Future()
#df = fd.Futu(exchangeCD='CCFX', field='secShortName,contractObject,minChgPriceNum,lastTradeDate,deliMethod')
##----------------------------------------------------------期权信息
##获取期权合约编码，交易代码，交易市场，标的等相关信息
#fd = ts.Options()
#df = fd.Opt(contractStatus='L,DE', field='optID,secShortName,varShortName,listDate')
##----------------------------------------------------------期权隐含波动率
##原始隐含波动率
#iv = ts.IV()
#df = iv.DerIv(beginDate='20150810', endDate='20150810', SecID='510050.XSHG')
##-----------------------------------------------------------债券信息
##固定利率债券、浮动利率债券每个计息周期的票面利率，包括分段计息的具体利率。
#fd = ts.Bond()
#df = fd.BondCoupon(ticker='000001', field='secShortName,perValueDate,refRatePer,coupon')
##-----------------------------------------------------------指数信息
##获取国内外指数的成分构成情况，包括指数成份股名称、成份股代码、入选日期、剔除日期等。
#fd = ts.Idx()
#df = fd.IdxCons(ticker='000001', field='secShortName,consTickerSymbol,consShortName,isNew,intoDate')
##------------------------------------------------------------宏观行业
##包含中国居民消费价格指数(CPI)数据，如大类CPI同比、环比、36大中城市CPI。历史数据从1993年开始，按月更新。
#fd = ts.Macro()
#df = fd.ChinaDataCPI(indicID='M030000003', field='indicName,periodDate,dataValue,dataSource')
#df = df.sort('periodDate', ascending=False)
##------------------------------------------------------------特色大数据
##包含所有主题基本信息。输入主题代码或名称、主题来源，可以获取主题相关信息，包括主题ID、主题名称、主题描述、主题来源、当天是否活跃、主题插入时间、主题更新时间等。(注：1、主题基期自2011/4/16始；2、数据按日更新主题活跃状态。)
#fd = ts.Subject()
#df = fd.ThemesContent(field='themeName,themeBaseDate,isActive,insertTime')
#df = df.sort('insertTime', ascending=False)
#==============================================================================
# 数据来源：http://pythonhosted.org/tushare/
# 编写：古而树里
# 开发：Anaconda
#==============================================================================


























































