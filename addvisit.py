from bs4 import BeautifulSoup
import requests
import time
import random
import pprint


def get_response(home_url):

    response = requests.get(home_url)
    html = response.text
    bsObj = BeautifulSoup(html)

    return bsObj


def get_url_list(bsObj):

    urllist = []

    for url in bsObj.find_all("a",attrs={'target':'_blank'}):

        href = url.get('href')
        urllist.append(href)

    return urllist


def get_clean_urlist(urllist, home_url):

    clean_list = []
    remove_iterate_list=list(set(urllist))
    number_of_list=len(remove_iterate_list)

    for i in range(number_of_list):

        if home_url in remove_iterate_list[i]:
            clean_list.append(remove_iterate_list[i])

    pprint.pprint(clean_list)

    return clean_list


def add_visit(clean_list):

    for url in clean_list:

        time.sleep(random.random()*3)
        response = requests.get(url)

    num_of_url = len(clean_list)

    return num_of_url


def times(n,cleanlist):

    i = 0

    for i in range(n):

        num_of_url=add_visit(clean_list)
        i = i + 1

    print('增加访问次数',i*num_of_url)


def begin_time():

    timestart = time.localtime(time.time())
    fmt = '%Y-%m-%d %a %H:%M:%S'
    test = time.strftime(fmt, timestart)

    print('开始的时间：', test)
    return test


def stop_time():

    timestop = time.localtime(time.time())
    fmt = '%Y-%m-%d %a %H:%M:%S'
    test = time.strftime(fmt, timestop)

    print('结束的时间：', test)
    return test



if __name__ == '__main__':

    begin_time()

    home_url = "https://blog.csdn.net/weixin_42326230"
    n= 20

    bsObj = get_response(home_url)
    urlist = get_url_list(bsObj)
    clean_list = get_clean_urlist(urlist,home_url)
    times(n,clean_list)

    stop_time()