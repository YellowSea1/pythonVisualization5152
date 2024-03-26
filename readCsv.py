import csv
import pandas as pd
import numpy as np


def readMonthProfitCsv():
    with open('月销售利润统计.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        monthProfit_date = []
        monthProfit_order = []
        monthProfit_sell = []
        monthProfit_profit = []
        for row in reader:
            monthProfit_date.append(row[0])
            monthProfit_order.append(row[3])
            monthProfit_sell.append(row[4])
            monthProfit_profit.append(row[5])
    return monthProfit_date, monthProfit_order, monthProfit_sell, monthProfit_profit


def readTotalProductCategoryCsv():
    with open('总产品类别统计.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        totalProductCategory_category = []
        totalProductCategory_sell = []
        totalProductCategory_avgProfit = []
        for row in reader:
            totalProductCategory_category.append(row[0])
            totalProductCategory_sell.append(row[1])
            totalProductCategory_avgProfit.append(row[2])
    return totalProductCategory_category, totalProductCategory_sell, totalProductCategory_avgProfit


def readYearProductCategoryCsv():
    with open('年产品类别统计.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        yearProductCategory_year = []
        yearProductCategory_category = []
        yearProductCategory_sell = []
        yearProductCategory_avgProfit = []
        for row in reader:
            yearProductCategory_year.append(row[0])
            yearProductCategory_category.append(row[1])
            yearProductCategory_sell.append(row[2])
            yearProductCategory_avgProfit.append(row[3])
    return yearProductCategory_year, yearProductCategory_category, yearProductCategory_sell, yearProductCategory_avgProfit


def readTotalTransportCsv():
    with open('总运输方式统计.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        totalTransport_mode = []
        totalTransport_order = []
        totalTransport_avgProfit = []
        for row in reader:
            totalTransport_mode.append(row[0])
            totalTransport_order.append(row[1])
            totalTransport_avgProfit.append(row[2])
    return totalTransport_mode, totalTransport_order, totalTransport_avgProfit


def readYearTransportCsv():
    with open('年运输方式统计.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        yearTransport_mode = []
        yearTransport_order = []
        yearTransport_avgProfit = []
        for row in reader:
            yearTransport_mode.append(row[0])
            yearTransport_order.append(row[1])
            yearTransport_avgProfit.append(row[2])
    return yearTransport_mode, yearTransport_order, yearTransport_avgProfit


def readStateDistCsv():
    with open('china_start_end.csv',encoding='GBK') as csvfile:
        reader = csv.reader(csvfile)
        stateDist_state = []
        stateDist_order = []
        stateDist_sell = []
        for row in reader:
            stateDist_state.append(row[0])
            stateDist_order.append(row[1])
            stateDist_sell.append(row[2])
    return stateDist_state, stateDist_order, stateDist_sell


def readUS():
    with open('美国疫情数据.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        us_month=[]
        us_confirm=[]
        us_death=[]
        us_recovered=[]
        for row in reader:
            us_month.append(row[0])
            us_confirm.append(row[1])
            us_death.append(row[2])
            us_recovered.append(row[3])
    return us_month,us_confirm,us_death,us_recovered

def readStateDistCsvUS():
    with open('us_start_end.csv',encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        stateDist_state = []
        stateDist_order = []
        stateDist_sell = []
        for row in reader:
            stateDist_state.append(row[0])
            stateDist_order.append(row[1])
            stateDist_sell.append(row[2])
    return stateDist_state, stateDist_order, stateDist_sell


def readCompareCountNumber():
    df_num=pd.read_csv('中美疫情数据对比.csv', header=0)
    df_num=np.array(df_num)
    ChinaConfirmNumber=[]
    USConfirmNumber=[]
    Date=[]
    ChinaGrowth=[1]
    AmericanGrowth=[1]
    for row in df_num:
        Date.append(row[0])
        ChinaConfirmNumber.append(row[1])
        USConfirmNumber.append(row[2])
    i=0
    while(i<6):
        #print('while loop')
        #print(round(int(ChinaConfirmNumber[i+1])/int(ChinaConfirmNumber[i]),3))
        ChinaGrowth.append(round(int(ChinaConfirmNumber[i+1])/int(ChinaConfirmNumber[i]),3))
        AmericanGrowth.append(round(int(USConfirmNumber[i+1])/int(USConfirmNumber[i]),3))
        i=i+1
    return Date,ChinaConfirmNumber,USConfirmNumber,ChinaGrowth,AmericanGrowth

def readCH():
    with open('中国疫情数据.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        ch_month=[]
        ch_confirm=[]
        ch_death=[]
        ch_recovered=[]
        for row in reader:
            ch_month.append(row[0])
            ch_confirm.append(row[1])
            ch_death.append(row[2])
            ch_recovered.append(row[3])
    return ch_month,ch_confirm,ch_death,ch_recovered
# def readCusPurchase():
#     with open('州分布统计.csv', encoding='utf-8-sig') as csvfile:
#         reader = csv.reader(csvfile)
#         stateDist_state = []
#         stateDist_order = []
#         stateDist_sell = []
#         for row in reader:
#             stateDist_state.append(row[0])
#             stateDist_order.append(row[2])
#             stateDist_sell.append(row[3])
#     return stateDist_state, stateDist_order, stateDist_sell