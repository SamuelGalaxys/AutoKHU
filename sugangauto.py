from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
from bs4 import BeautifulSoup

from random import *
 
i = randint(5, 30)  # 1부터 100 사이의 임의의 정수
 
f = random()   # 0부터 1 사이의 임의의 float
 
f = uniform(1.0, 36.5)   # 1부터 36.5 사이의 임의의 float
 
i = randrange(1, 101, 2) # 1부터 100 사이의 임의의 짝수
 
i = randrange(10)  # 0부터 9 사이의 임의의 정수

from random import randint

random_wait_min = 10
random_wait_max = 25

random_next_min = 5
random_next_max = 20










from selenium.webdriver.common.by import By

ID = '123123' #Google ID
PW = '213123' #Google PW

#화면 띄우기
browser = webdriver.Chrome('/Users/samuelgalaxys/desktop/chromedriver')
browser.get("https://sugang.khu.ac.kr/")




# iframe id값을 이용해 프레임 전환
element = browser.find_element_by_id("Main") #iframe 태그 엘리먼트 찾기
browser.switch_to.frame(element)

element1 = browser.find_element_by_xpath('/html/frameset/frame') #iframe 태그 엘리먼트 찾기
browser.switch_to.frame(element1)

time.sleep(1)

 
search = browser.find_element_by_xpath('/html/body/div[3]/div[1]/form/div/div/div/input[1]')
# search = browser.find_element_by_TEXT('학번 (Student ID)')

search.send_keys('2022103XXX')

search2 = browser.find_element_by_xpath('/html/body/div[3]/div[1]/form/div/div/div/input[2]')
# search = browser.find_element_by_TEXT('비밀번호 (Password)')
search2.send_keys('0000000.')





#로그인 버튼
browser.find_element(By.XPATH,"/html/body/div[3]/div[1]/form/div/div/div/button[1]" ).click()



try:
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        
        # 취소하기(닫기)
        alert.dismiss()
        
        # 확인하기
        alert.accept()
except:
        print("no alert")

 

time.sleep(2)

 





 

# iframe id값을 이용해 프레임 전환
elementz = browser.find_element_by_xpath('/html/body/iframe[1]') #iframe 태그 엘리먼트 찾기
browser.switch_to.frame(elementz)

elementz1 = browser.find_element_by_xpath('/html/frameset/frame') #iframe 태그 엘리먼트 찾기
browser.switch_to.frame(elementz1)

time.sleep(1)
 

browser.find_element(By.XPATH,"/html/body/div[4]/div[3]/ul/li[5]" ).click()
















time.sleep(300)













time.sleep(100)
browser.find_element(By.XPATH,value='//*[text()="경희대학교 e-campus"]' ).click()






time.sleep(2)







browser.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[2]/div[2]/a" ).click()



#/html/body/div/div/div/div[2]/div[3]/div[1] (최근 목록)


#로딩하는 시간 기다리기
time.sleep(1)

#Login ID 속성값 찾고 입력하기
login_id = browser.find_element(By.XPATH,"/html/body/div[2]/form/div/div[1]/span/input" ).click()
login_id = browser.find_element(By.XPATH,"/html/body/div[2]/form/div/div[1]/span/input" )

login_id.send_keys(ID)
#login_id.send_keys(Keys.RETURN)


#browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button" ).click()
 



#Login PW 속성값 찾기 입력하기
login_pw = browser.find_element(By.XPATH,"/html/body/div[2]/form/div/div[2]/span/input" )
login_pw.send_keys(PW)
#login_pw.send_keys(Keys.RETURN)  # 엔터키 누르기

browser.find_element(By.XPATH,"/html/body/div[2]/form/div/div[3]/a").click()

time.sleep(1)


# 정보 저장 팝업 닫기
# popup = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
# popup.send_keys(Keys.ENTER)

 
# 내 강ㅢㅣㄹ 바가  // ERROR
browser.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[2]/div[2]/div[1]/a" ).click()


# 강의목록 버튼
browser.find_element(By.XPATH,"/html/body/div[2]/header[2]/div[1]/ul/li[3]/button" ).click()


# 강의 대상 ex. 빅데이터프로그래밍
browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div[5]/div/div[5]/div/div[1]" ).click()
time.sleep(1)


 # 강의콘텐츠

browser.find_element(By.XPATH,value='//*[text()="강의콘텐츠"]' ).click()





time.sleep(2)

 
browser.switch_to.frame(browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/iframe"))

browser.execute_script("window.scrollTo(0,0)")  # Scroll to TOP

#browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/iframe").send_keys(Keys.PAGE_UP)

time.sleep(2)

 
browser.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div/div/a[1]/div" ).click()





browser.find_element(By.XPATH,value='//*[text()="1주차"]' ).click()

  
#CKCK2 = browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[2]/div[2]" )


#if CKCK2 == False:
    #browser.find_element(By.XPATH,value='//*[text()="1주차"]' ).click()



    #browser.find_element(By.XPATH,value='//*[text()="2주차"]' ).click()






 













browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[2]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[3]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[4]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[5]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[6]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[7]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[8]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[9]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[10]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[11]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[12]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[13]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[14]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[15]/div[1]/div/div[1]/i" ).click()
browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[16]/div[1]/div/div[1]/i" ).click()
 




time.sleep(100)

 

 









