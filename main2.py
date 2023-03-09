import pickle
import time
import json
from os.path import exists

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as soup

from selenium import webdriver
import time
import pandas as pd


driver = webdriver.Chrome()
def check_cookies():
    if os.path.exists("cookies.pkl"):
        return True
    return False

def login():


    driver.get("https://www.naukri.com/")

    time.sleep(3)
    # 2 | setWindowSize | 1296x688 |
    driver.maximize_window()

    time.sleep(1)
    # 3 | click | css=.nI-gNb-menuItems__anchorDropdown--active > div |
    driver.find_element(By.CSS_SELECTOR, ".ni-gnb-icn").click()

    time.sleep(5)
    # 4 | click | css=.nI-gNb-foremp > .nI-gNb-menuItems__anchorDropdown > div |

    # # 5 | click | css=.undefined .nI-gNb-menuItems:nth-child(3) div |

    time.sleep(5)
    try:
        driver.find_element(By.CSS_SELECTOR, ".nI-gNb-foremp > .nI-gNb-menuItems__anchorDropdown > div").click()

        driver.find_element(By.CSS_SELECTOR, ".undefined .nI-gNb-menuItems:nth-child(3) div").click()

    except:
        pass
    # 6 | type | id=loginEmail | Naukri59@flexability.in



    print("Login")
    time.sleep(10)

    driver.find_element(By.XPATH, "//ul[@id='toggleForm']/li[2]").click()

    print("NOtLogin")

    time.sleep(5)


    l="Naukri60@flexability.in"
    l1="Naukri59@flexability.in"
    l2 = "Naukri21@flexability.in"

    driver.find_element(By.ID, "loginEmail").send_keys(l2)
    # 7 | type | id=password | Jan@2023

    a="Insights123$"
    a1="Jan@2023"
    a2="Jan@2022"

    driver.find_element(By.ID, "password").send_keys(a2)
    # 8 | click | id=loginEmail |




    time.sleep(5)
    # 9 | click | id=loginBtn |
    driver.find_element(By.ID, "loginBtn").click()
    # 10 | mouseOver | css=.gnb_resdex .gnb_mTxt |
    time.sleep(15)

    try:
        driver.find_element(By.CSS_SELECTOR, ".icon - close").click()
    except:
        pass





    try:

        driver.find_element(By.ID, "otpCode").click()

        time.sleep(10)


        while driver.current_url!="https://recruit.naukri.com/":

            try:
                driver.find_element(By.ID, "verifyOtpBtn").click()

                time.sleep(20)
            except:
                pass
    except:
        pass


    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))



if check_cookies():
    driver.get("https://www.naukri.com/")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get("https://www.naukri.com/")

    print('--------------------------------')

    driver.maximize_window()

    time.sleep(1)
    # 3 | click | css=.nI-gNb-menuItems__anchorDropdown--active > div |
    driver.find_element(By.CSS_SELECTOR, ".ni-gnb-icn").click()

    time.sleep(5)
    # 4 | click | css=.nI-gNb-foremp > .nI-gNb-menuItems__anchorDropdown > div |

    # # 5 | click | css=.undefined .nI-gNb-menuItems:nth-child(3) div |

    time.sleep(5)
    try:
        driver.find_element(By.CSS_SELECTOR, ".nI-gNb-foremp > .nI-gNb-menuItems__anchorDropdown > div").click()

        driver.find_element(By.CSS_SELECTOR, ".undefined .nI-gNb-menuItems:nth-child(3) div").click()

    except:
        pass
    # 6 | type | id=loginEmail | Naukri59@flexability.in

    print("Login")
    time.sleep(10)
    try:
        driver.find_element(By.XPATH, "//ul[@id='toggleForm']/li[2]").click()
    except:
        pass

    print("NOtLogin")
    try:

        time.sleep(5)

        l = "Naukri60@flexability.in"
        l1 = "Naukri59@flexability.in"
        l2= "Naukri21@flexability.in"
        driver.find_element(By.ID, "loginEmail").send_keys(l2)
        # 7 | type | id=password | Jan@2023

        a = "Insights123$"
        a1 = "Jan@2023"
        a2 = "Jan@2022"

        driver.find_element(By.ID, "password").send_keys(a2)
        # 8 | click | id=loginEmail |

        time.sleep(5)
        # 9 | click | id=loginBtn |
        driver.find_element(By.ID, "loginBtn").click()
        # 10 | mouseOver | css=.gnb_resdex .gnb_mTxt |
        time.sleep(5)

    except:
        pass

    try:

        driver.find_element(By.CSS_SELECTOR, ".icon - close").click()
    except:
        print("pass")

    try:

        driver.find_element(By.ID, "otpCode").click()

        time.sleep(10)

        while driver.current_url != "https://recruit.naukri.com/":

            try:
                driver.find_element(By.ID, "verifyOtpBtn").click()

                time.sleep(10)
            except:
                pass
    except:
        pass

    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))




else:
    login()

element = driver.find_element(By.CSS_SELECTOR, ".gnb_resdex .gnb_mTxt")
actions = ActionChains(driver)
time.sleep(1)
actions.move_to_element(element).perform()
time.sleep(1)
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)


time.sleep(1)
actions.move_to_element(element).perform()
driver.find_element(By.LINK_TEXT, "Search Resumes").click()

# 15 | click | name=boolKeywords |

x=False
while x==False:
    try:
        driver.find_element(By.CSS_SELECTOR, ".rdx-quota-btn").click()
        x=True
    except:
        x=False




time.sleep(1)




driver.find_element(By.CSS_SELECTOR, ".boolean-toggle .highlighter").click()
# 16 | type | name=boolKeywords | docter
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".search-in-dropdown-wrap:nth-child(3) .dropArrowDD").click()


time.sleep(1)

driver.find_element(By.XPATH,"//li[contains(.,'Resume title and keyskills')]").click()
time.sleep(1)
driver.find_element(By.NAME, "boolKeywords").send_keys('"python","pyspark","java"')

time.sleep(1)
driver.find_element(By.NAME, "v3-adv").click()

# driver.find_element(By.NAME, "boolKeywords").send_keys(Keys.ENTER)
# time.sleep(10)
# driver.find_element(By.LINK_TEXT, "Modify").click()
# time.sleep(4)

print("Modify location")
time.sleep(1)
driver.execute_script("window.scrollTo(0,300)")

time.sleep(1)

driver.find_element(By.ID, "prefLocCheckbox").click()
driver.find_element(By.NAME, "locations").click()
time.sleep(1)



anywere_india = driver.find_element(By.CSS_SELECTOR, ".selectableGroup:nth-child(2) .ico")

anywere_india.click()

print(anywere_india.text)

time.sleep(8)
t = time.strftime("%Y-%m-%d,%H-%M-%S")

if not os.path.exists('process'):
    os.makedirs('process')



l1 = []
job = []
loc = []

kd = "./process/" + str(t) + "-" + "-process-" + ".csv"
mydfproce = pd.DataFrame(list(zip(job, loc, l1)), columns=['jobtitle', 'location', 'count'])

mydfproce.to_csv(kd, index=False)

time.sleep(1)

any=driver.find_element(By.CSS_SELECTOR, ".selectableGroup:nth-child(1) .ico")
any.text


time.sleep(3)



time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".active-in-wrap .dropArrowDD").click()
time.sleep(1)

print("click")

driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) > span > span").click()

print("months")

time.sleep(1)
driver.find_element(By.ID, "adv-search-btn").click()

time.sleep(10)

data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

print(data)

time.sleep(1)


extra_keyword=['doctor']

if  len(extra_keyword)!=0:

    keyword=driver.find_element(By.CSS_SELECTOR,".collapser-wrapper:nth-child(2) .collapser-header .ico")
    keyword.click()

    key=driver.find_element(By.CSS_SELECTOR,".active .suggestor-input")
    key.click()


    key.send_keys(extra_keyword[0])

    button=driver.find_element(By.CSS_SELECTOR,".naukri-btn-primary")
    button.click()

else:
    pass

time.sleep(10)


driver.execute_script("window.scrollTo(0,0)")



locations = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(3) .ico")
locations.click()

time.sleep(1)

#driver.execute_script("window.scrollTo(0,110)"

driver.find_element(By.CSS_SELECTOR, ".more-location").click()


time.sleep(10)

page = driver.execute_script('return document.body.innerHTML')
page_soup = BeautifulSoup(''.join(page), 'html.parser')

cases = page_soup.find_all('ul', {'class': 'filter-location-list'})


d=[]



for case in cases:
    o=case.find_all('li')
    for i in o:
        a=i.find('span',{'class':'chk-label'})
        a=a.text
        b=i.find('span',{'class':'cnt'})
        b=b.text
        d.append([a,b])

print(d)


# more-location link-button


driver.find_element(By.CSS_SELECTOR, ".card-close > svg").click()

time.sleep(1)

locations = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(3) .ico")
locations.click()

driver.execute_script("window.scrollTo(0, 0)")

time.sleep(1)




industry = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(8) .ico")
industry.click()

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, ".more-functional-area").click()
time.sleep(1)

time.sleep(10)

page = driver.execute_script('return document.body.innerHTML')
page_soup = BeautifulSoup(''.join(page), 'html.parser')


alss = page_soup.find_all('div', {'class': 'farea-list'})

time.sleep(1)


da=[]

for case in alss:
    o=case.find_all('li')
    for i in o:
        div = i.find('div', {'class': 'inside'})
        title = div['title']


        b=i.find('span',{'class':'cnt'})
        b=b.text
        da.append([title,b])

print(da)

driver.find_element(By.CSS_SELECTOR, ".naukri-icon-times:nth-child(1)").click()

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".expanded:nth-child(3)").click()

time.sleep(1)

department = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(9) .ico")
department.click()

time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".more-industry").click()
time.sleep(1)

time.sleep(10)




page = driver.execute_script('return document.body.innerHTML')
page_soup = BeautifulSoup(''.join(page), 'html.parser')

cases = page_soup.find_all('ul', {'class': 'filter-industry-list'})


d=[]



for case in cases:
    o=case.find_all('li')

    for i in o:
        a=i.find_all('span',{'class':'chk-label'})
        a=a[1].text
        b=i.find('span',{'class':'cnt'})
        b=b.text
        d.append([a,b])

print(d)

driver.find_element(By.CSS_SELECTOR, ".naukri-icon-times:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, ".expanded:nth-child(3)").click()



a=[1,2.1]
b=[2,4]




time.sleep(1)



driver.find_element(By.LINK_TEXT, "Modify").click()
x=2

for i in range(3):

    time.sleep(3)
    driver.execute_script("window.scrollTo(0,730)")

    time.sleep(1)


    if x==2:
        driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()

    elif i==2:
        driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child(1) > .txt").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()
        time.sleep(1)

    if i==2:
        break

    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child({x}) > .txt").click()
    x=x+1
    time.sleep(1)
    driver.find_element(By.ID, "adv-search-btn").click()

    time.sleep(10)

    data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

    print(data)

    driver.find_element(By.LINK_TEXT, "Modify").click()


#_________________________________________________________________________________________________________
#divercity

x=2


vals="Delhi / NCR"
length=50


country=['delhi','mumbai','chennai','Bangalore','Pune','Hyderabad']

for i in range(len(country)):

    driver.execute_script("window.scrollTo(0,0)")
    driver.execute_script("window.scrollTo(0,200)")



    if country[i] == "delhi" or country[i] == "mumbai":

        if country[i] == "mumbai":
            vals = "Mumbai (All Areas)"
            length = 55
        else:
            vals = "Delhi / NCR"
            length = 50

        time.sleep(1)

        driver.find_element(By.NAME, "locations").click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".tag-ico").click()

        time.sleep(1)

        loc = driver.find_element(By.NAME, "locations")
        loc.click()

        element = driver.find_element(By.CSS_SELECTOR, ".list .verticalThumb")
        actions = ActionChains(driver)
        actions.move_to_element(element).drag_and_drop_by_offset(element, 0, length).perform()

        length = length + 1

        time.sleep(2)

        driver.find_element(By.XPATH, f"//span[contains(.,'{vals}')]").click()

        time.sleep(1)

        time.sleep(1)
        time.sleep(1)


        time.sleep(10)

        for i in range(3):

            time.sleep(3)
            driver.execute_script("window.scrollTo(0,0)")
            driver.execute_script("window.scrollTo(0,730)")

            time.sleep(1)

            if x == 2:
                driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()

            elif i == 2:
                driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child(1) > .txt").click()
                time.sleep(3)
                driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()
                time.sleep(1)

            if i == 2:
                break

            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child({x}) > .txt").click()
            x = x + 1
            time.sleep(1)
            driver.find_element(By.ID, "adv-search-btn").click()

            time.sleep(10)

            try:
                data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text
                print("gender_diversity",- data)

            except:
                print("data not available")

            try:
                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                pass

        x = 2

    else:

        driver.execute_script("window.scrollTo(0,0)")
        driver.execute_script("window.scrollTo(0,200)")

        driver.find_element(By.NAME, "locations").click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".tag-ico").click()

        time.sleep(1)

        loc = driver.find_element(By.NAME, "locations")
        loc.click()
        loc.send_keys(country[i])

        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".tuple-wrap:nth-child(1) > .opt").click()
        time.sleep(1)

        for i in range(3):

            time.sleep(3)
            driver.execute_script("window.scrollTo(0,0)")
            driver.execute_script("window.scrollTo(0,730)")

            time.sleep(1)


            if x==2:
                driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()

            elif i==2:
                driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child(1) > .txt").click()
                time.sleep(3)
                driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()
                time.sleep(1)

            if i==2:
                break

            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child({x}) > .txt").click()
            x=x+1
            time.sleep(1)
            driver.find_element(By.ID, "adv-search-btn").click()

            time.sleep(10)

            try:
                data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text
                print("gender_diversity",data)

            except:
                print("data not available")



            try:
                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                pass

        x=2

        for i in range(3):

            time.sleep(3)
            driver.execute_script("window.scrollTo(0,0)")
            driver.execute_script("window.scrollTo(0,730)")

            time.sleep(1)


            if x==2:
                driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()

            elif i==2:
                driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child(1) > .txt").click()
                time.sleep(3)
                driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()
                time.sleep(1)

            if i==2:
                break

            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child({x}) > .txt").click()
            x=x+1
            time.sleep(1)
            driver.find_element(By.ID, "adv-search-btn").click()

            time.sleep(10)

            try:
                data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text
                print(data)

            except:
                print("data not available")



            try:
                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                pass

        x=2


















#______________________________________________________________________________________________________________

# experience

country=['delhi','mumbai','chennai','Bangalore','Pune','Hyderabad']

vals = "Delhi / NCR"
length=50
for i in range(len(country)):


    driver.execute_script("window.scrollTo(0,0)")
    driver.execute_script("window.scrollTo(0,200)")

    if country[i]=="delhi" or country[i]=="mumbai":

        if country[i] == "mumbai":
            vals = "Mumbai (All Areas)"
            length = 55
        else:
            vals = "Delhi / NCR"
            length = 50


        time.sleep(1)

        driver.find_element(By.NAME, "locations").click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".tag-ico").click()

        time.sleep(1)

        loc = driver.find_element(By.NAME, "locations")
        loc.click()

        element = driver.find_element(By.CSS_SELECTOR, ".list .verticalThumb")
        actions = ActionChains(driver)
        actions.move_to_element(element).drag_and_drop_by_offset(element, 0, length).perform()

        length = length + 1

        time.sleep(2)
        driver.find_element(By.XPATH, f"//span[contains(.,'{vals}')]").click()

        time.sleep(1)



        time.sleep(1)
        time.sleep(1)
        driver.find_element(By.ID, "adv-search-btn").click()

        time.sleep(10)

        try:

            data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text



            print(data)

            time.sleep(10)

            for i, j in zip(a, b):
                driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(4) .ico").click()
                time.sleep(10)

                driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(i)
                time.sleep(5)

                driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(j)
                time.sleep(5)
                driver.find_element(By.CSS_SELECTOR, ".naukri-btn-primary").click()
                time.sleep(1)
                data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

                time.sleep(3)

                print(data)
                driver.find_element(By.CSS_SELECTOR, ".clear-all").click()
                time.sleep(5)

            driver.find_element(By.LINK_TEXT, "Modify").click()

        except:
            print(" data Not availble for this location")


    else:

        print(" data Not availble for this location............................................................")

        try:

            driver.execute_script("window.scrollTo(0,0)")
            driver.execute_script("window.scrollTo(0,200)")

            driver.find_element(By.NAME, "locations").click()
            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR,".tag-ico").click()

            time.sleep(1)

            loc=driver.find_element(By.NAME, "locations")
            loc.click()
            loc.send_keys(country[i])

            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR,".tuple-wrap:nth-child(1) > .opt").click()
            time.sleep(1)

            time.sleep(1)
            driver.find_element(By.ID, "adv-search-btn").click()

            time.sleep(10)

            data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

            print(data)

            time.sleep(10)

            for i, j in zip(a, b):
                driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(4) .ico").click()
                time.sleep(10)

                driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(i)
                time.sleep(5)

                driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(j)
                time.sleep(5)
                driver.find_element(By.CSS_SELECTOR, ".naukri-btn-primary").click()
                time.sleep(1)
                data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

                time.sleep(3)

                print(data)
                driver.find_element(By.CSS_SELECTOR, ".clear-all").click()
                time.sleep(5)

            driver.find_element(By.LINK_TEXT, "Modify").click()

        except:
            print(country[i]+"Profile not found ")





















#
# page = driver.find_element(By.CSS_SELECTOR, ".show-page-wrap:nth-child(2) .page-value").text









#
# b = page.split()
# number = int(b[-1])
#
# current_page=driver.get_current_page()
#
# b=current_page.split("pageNo=1")
# d1=[]
# for i in range(1,number):
#     d = b[0] + f"pageNo={i}" + b[1]
#     d1.append(d)
#
#
# print(page)





driver.quit()