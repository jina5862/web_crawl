import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime, time
from multiprocessing import Pool

def get_bestseller():
    url_1 = "http://www.bandinlunis.com/front/display/listBest.do?page="
    url_2 = "&searchType=top&recommendYear="
    url_3 = "&recommendMonth="
    url_4 = "&recommendWeek="
    url_5 = "&cateId=&sex=&age=&prodStat=&sort=sort8"
    date_= datetime.date.today()
    get_date = str(date_)
    get_year, get_month, get_day = get_date.split("-")
    get_month = get_month.split("0")[1]
    week = 0
    num=1

    for i in range(1, int(get_day)+1):
        start = date_.replace(int(get_year), int(get_month), i)
        day = start.weekday()
        if str(day) == "0":
            week+=1

    url_front = url_1
    url_back = url_2 + get_year +  url_3 + get_month + url_4 + str(week) + url_5

    f = open("베스트셀러_" + get_year+"년"+get_month+"월"+str(week)+"주차", 'w')             # 새로운 파일 작성
    f.write(get_year + " 년 " + get_month + " 월 " + str(week) + " 주차 베스트셀러\n")
    f.write("------------------------------------------------------\n")

    for i in range(1, 6):           # 웹에서 책 제목 가져오기
        if i ==1:
            url ="http://www.bandinlunis.com/front/display/listBest.do"
        else : url = url_front + str(i)+ url_back
        driver = webdriver.Chrome('/Users/귀욤디욤/Downloads/chromedriver_win32/chromedriver')
        #driver.get('http://www.bandinlunis.com/front/display/listBest.do')
        driver.implicitly_wait(3)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        titles = soup.select('#contentWrap > div.conWrap > div.con_t2 > form > div.prod_list_type.prod_best_type > ul > li > dl.prod_info > dt > a')
        details = soup.select('#contentWrap > div.conWrap > div.con_t2 > form > div.prod_list_type.prod_best_type > ul > li > dl.prod_info > dd.txt_bex')
        result = []

        for j in range(0,len(titles)):  #
            s = str(titles[j].text.strip())
            t = str(details[j].text.strip())
            f.write(str(num)+". < "+s + " >\n")
            f.write('\t'+t+'\n\n')
            result.append(titles[j].text.strip())
            num+=1

    return result


if __name__ == '__main__':
    get_bestseller()

