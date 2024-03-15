# -*-coding:utf-8-*-
import pandas as pd
import numpy as np


def readYearProductCategoryCsv():
    df_2018 = pd.read_csv("年产品类别统计.csv", nrows=3)
    category_2018 = []
    sell_2018 = []
    avgProfit_2018 = []
    df_2018 = np.array(df_2018)
    for row in df_2018:
        category_2018.append(row[1])
        sell_2018.append(row[2])
        avgProfit_2018.append(row[3])

    df_2019 = pd.read_csv("年产品类别统计.csv", skiprows=3, nrows=3)
    category_2019 = []
    sell_2019 = []
    avgProfit_2019 = []
    df_2019 = np.array(df_2019)
    for row in df_2019:
        category_2019.append(row[1])
        sell_2019.append(row[2])
        avgProfit_2019.append(row[3])

    df_2020 = pd.read_csv("年产品类别统计.csv", skiprows=6, nrows=3)
    category_2020 = []
    sell_2020 = []
    avgProfit_2020 = []
    df_2020 = np.array(df_2020)
    for row in df_2020:
        category_2020.append(row[1])
        sell_2020.append(row[2])
        avgProfit_2020.append(row[3])

    df_2021 = pd.read_csv("年产品类别统计.csv", skiprows=9, nrows=3)
    category_2021 = []
    sell_2021 = []
    avgProfit_2021 = []
    df_2021 = np.array(df_2021)
    for row in df_2021:
        category_2021.append(row[1])
        sell_2021.append(row[2])
        avgProfit_2021.append(row[3])

    return category_2018, sell_2018, avgProfit_2018, category_2019, sell_2019, avgProfit_2019, category_2020, sell_2020, avgProfit_2020, category_2021, sell_2021, avgProfit_2021


def readYearTransportCsv():
    df_2018 = pd.read_csv("年运输方式统计.csv", nrows=3)
    mode_2018 = []
    order_2018 = []
    avgProfit_2018 = []
    df_2018 = np.array(df_2018)
    for row in df_2018:
        mode_2018.append(row[1])
        order_2018.append(row[2])
        avgProfit_2018.append(row[3])

    df_2019 = pd.read_csv("年运输方式统计.csv", skiprows=3, nrows=3)
    mode_2019 = []
    order_2019 = []
    avgProfit_2019 = []
    df_2019 = np.array(df_2019)
    for row in df_2019:
        mode_2019.append(row[1])
        order_2019.append(row[2])
        avgProfit_2019.append(row[3])

    df_2020 = pd.read_csv("年运输方式统计.csv", skiprows=6, nrows=3)
    mode_2020 = []
    order_2020 = []
    avgProfit_2020 = []
    df_2020 = np.array(df_2020)
    for row in df_2020:
        mode_2020.append(row[1])
        order_2020.append(row[2])
        avgProfit_2020.append(row[3])

    df_2021 = pd.read_csv("年运输方式统计.csv", skiprows=9, nrows=3)
    mode_2021 = []
    order_2021 = []
    avgProfit_2021 = []
    df_2021 = np.array(df_2021)
    for row in df_2021:
        mode_2021.append(row[1])
        order_2021.append(row[2])
        avgProfit_2021.append(row[3])

    return mode_2018, order_2018, avgProfit_2018, \
           mode_2019, order_2019, avgProfit_2019, \
           mode_2020, order_2020, avgProfit_2020, \
           mode_2021, order_2021, avgProfit_2021
