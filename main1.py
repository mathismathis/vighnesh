import pickle
import time
import json
from os.path import exists

from pandas.core.interchange import column
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


df=pd.read_csv('input.csv')

username=df['username'].dropna().tolist()
columns = df['username'].dropna().tolist()
password = df['password'].dropna().tolist()
keyword = df['keyword'].dropna().tolist()
additional_keyword = df['additional_keyword'].dropna().tolist()
location_for_gender_diversity = df['location_for_gender_diversity'].dropna().tolist()
location_for_experience = df['location_for_experience'].dropna().tolist()
experience_range_col1 = df['experience_range_col1'].dropna().tolist()
experience_range_col2 = df['experience_range_col2'].dropna().tolist()
# ready_to_relocate=df['ready_to_relocate'].dropna().tolist()
tic_location=df['relocate'].dropna().tolist()
anywhere_india_experience_range_col1=df['anywhere_india_experience_range_col1'].dropna().tolist()
anywhere_india_experience_range_col2=df['anywhere_india_experience_range_col2'].dropna().tolist()

anywhere_india_data=[]
anywhere_india_data_genders=[]
gender_diversity_data=[]
experience_split_data=[]
location_count_data=[]
tic_data=[]

driver = webdriver.Chrome()
def check_cookies():
    if os.path.exists("cookies.pkl"):
        return True
    return False

def login():
    driver.get("https://www.naukri.com/")

    time.sleep(3)

    driver.maximize_window()

    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".ni-gnb-icn").click()

    time.sleep(5)



    time.sleep(5)
    try:
        driver.find_element(By.CSS_SELECTOR, ".nI-gNb-foremp > .nI-gNb-menuItems__anchorDropdown > div").click()

        driver.find_element(By.CSS_SELECTOR, ".undefined .nI-gNb-menuItems:nth-child(3) div").click()

    except:
        pass
    # 6 | type | id=loginEmail | Naukri59@flexability.in


    time.sleep(10)

    driver.find_element(By.XPATH, "//ul[@id='toggleForm']/li[2]").click()

    time.sleep(5)



    driver.find_element(By.ID, "loginEmail").send_keys(username[0])


    driver.find_element(By.ID, "password").send_keys(password[0])





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


    time.sleep(10)
    try:
        driver.find_element(By.XPATH, "//ul[@id='toggleForm']/li[2]").click()
    except:
        pass


    try:

        time.sleep(5)

        driver.find_element(By.ID, "loginEmail").send_keys(username[0])
        driver.find_element(By.ID, "password").send_keys(password[0])


        time.sleep(5)

        driver.find_element(By.ID, "loginBtn").click()

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


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#login end


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

time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".search-in-dropdown-wrap:nth-child(3) .dropArrowDD").click()


time.sleep(1)

driver.find_element(By.XPATH,"//li[contains(.,'Resume title and keyskills')]").click()
time.sleep(1)
driver.find_element(By.NAME, "boolKeywords").send_keys(keyword[0])

time.sleep(1)
driver.find_element(By.NAME, "v3-adv").click()


driver.find_element(By.NAME, "minExp").click()
driver.find_element(By.NAME,'minExp').send_keys(anywhere_india_experience_range_col1[0])

driver.find_element(By.NAME, "maxExp").click()
driver.find_element(By.NAME,"maxExp").send_keys(anywhere_india_experience_range_col2[0])

time.sleep(1)
driver.execute_script("window.scrollTo(0,300)")

time.sleep(1)

driver.find_element(By.ID, "prefLocCheckbox").click()
driver.find_element(By.NAME, "locations").click()
time.sleep(1)



anywere_india = driver.find_element(By.CSS_SELECTOR, ".selectableGroup:nth-child(2) .ico")

anywere_india.click()







time.sleep(3)


driver.find_element(By.CSS_SELECTOR, ".active-in-wrap .dropArrowDD").click()
time.sleep(1)



driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) > span > span").click()


time.sleep(1)
driver.find_element(By.ID, "adv-search-btn").click()

time.sleep(10)

data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

anywhere_india_data.append(data)

#_______________________________________________________________________________________________________________________________________________________________________
#narmal search



time.sleep(1)




extra_keyword=additional_keyword

length_of_the_extra_keyword=len(extra_keyword)

if  length_of_the_extra_keyword!=0:

    keyword=driver.find_element(By.CSS_SELECTOR,".collapser-wrapper:nth-child(2) .collapser-header .ico")
    keyword.click()

    key=driver.find_element(By.CSS_SELECTOR,".active .suggestor-input")
    key.click()


    key.send_keys(extra_keyword[0])

    button=driver.find_element(By.CSS_SELECTOR,".naukri-btn-primary")
    button.click()


    time.sleep(10)

    data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

    anywhere_india_data.append(data)

else:
    pass


# ------------------------------------------------------------------------------------------------------------------------
#location


d = []

if length_of_the_extra_keyword!=0:
    time.sleep(3)

    driver.execute_script("window.scrollTo(0,110)")

    locations = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(4) .ico")
    locations.click()

    time.sleep(1)



    driver.find_element(By.CSS_SELECTOR, ".more-location").click()

    time.sleep(10)

    page = driver.execute_script('return document.body.innerHTML')
    page_soup = BeautifulSoup(''.join(page), 'html.parser')

    cases = page_soup.find_all('ul', {'class': 'filter-location-list'})



    for case in cases:
        o = case.find_all('li')
        for i in o:
            a = i.find('span', {'class': 'chk-label'})
            a = a.text
            b = i.find('span', {'class': 'cnt'})
            b = b.text
            d.append([a, b])



    # more-location link-button

    driver.find_element(By.CSS_SELECTOR, ".card-close > svg").click()

    time.sleep(1)

    locations = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(3) .ico")
    locations.click()

    driver.execute_script("window.scrollTo(0, 0)")

    time.sleep(1)

else:


    driver.execute_script("window.scrollTo(0,0)")
    driver.execute_script("window.scrollTo(0,400)")

    time.sleep(10)

    locations = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(3) .ico")
    locations.click()

    time.sleep(1)

#driver.execute_script("window.scrollTo(0,110)"

    driver.find_element(By.CSS_SELECTOR, ".more-location").click()


    time.sleep(10)

    page = driver.execute_script('return document.body.innerHTML')
    page_soup = BeautifulSoup(''.join(page), 'html.parser')

    cases = page_soup.find_all('ul', {'class': 'filter-location-list'})





    for case in cases:
        o=case.find_all('li')
        for i in o:
            a=i.find('span',{'class':'chk-label'})
            a=a.text
            b=i.find('span',{'class':'cnt'})
            b=b.text
            d.append([a,b])




    # more-location link-button


    driver.find_element(By.CSS_SELECTOR, ".card-close > svg").click()

    time.sleep(1)

    locations = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(3) .ico")
    locations.click()



    time.sleep(3)



df1 = pd.DataFrame(d, columns=['attributes','value'])



#______________________________________________________________________________________________________
#functional-area

da=[]

if length_of_the_extra_keyword!=0:
    time.sleep(3)

    driver.execute_script("window.scrollTo(0,100)")


    industry = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(9) .ico")
    industry.click()

    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, ".more-functional-area").click()
    time.sleep(1)

    time.sleep(10)

    page = driver.execute_script('return document.body.innerHTML')
    page_soup = BeautifulSoup(''.join(page), 'html.parser')


    alss = page_soup.find_all('div', {'class': 'farea-list'})

    time.sleep(1)




    for case in alss:
        o=case.find_all('li')
        for i in o:
            div = i.find('div', {'class': 'inside'})
            title = div['title']


            b=i.find('span',{'class':'cnt'})
            b=b.text
            da.append([title,b])



    driver.find_element(By.CSS_SELECTOR, ".naukri-icon-times:nth-child(1)").click()

    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".expanded:nth-child(3)").click()

    time.sleep(1)


else:
    time.sleep(4)

    industry = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(8) .ico")
    industry.click()

    time.sleep(4)

    driver.find_element(By.CSS_SELECTOR, ".more-functional-area").click()
    time.sleep(1)

    time.sleep(10)

    page = driver.execute_script('return document.body.innerHTML')
    page_soup = BeautifulSoup(''.join(page), 'html.parser')

    alss = page_soup.find_all('div', {'class': 'farea-list'})

    time.sleep(1)



    for case in alss:
        o = case.find_all('li')
        for i in o:
            div = i.find('div', {'class': 'inside'})
            title = div['title']

            b = i.find('span', {'class': 'cnt'})
            b = b.text
            da.append([title, b])



    driver.find_element(By.CSS_SELECTOR, ".naukri-icon-times:nth-child(1)").click()

    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".expanded:nth-child(3)").click()

    time.sleep(1)


df2=pd.DataFrame(da,columns=['attributes','value'])

#______________----------------------------------------------------------------
#department_


daa=[]

if length_of_the_extra_keyword!=0:

    department = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(10) .ico")
    department.click()

    time.sleep(4)

    driver.find_element(By.CSS_SELECTOR, ".more-industry").click()
    time.sleep(1)

    time.sleep(10)




    page = driver.execute_script('return document.body.innerHTML')
    page_soup = BeautifulSoup(''.join(page), 'html.parser')

    cases = page_soup.find_all('ul', {'class': 'filter-industry-list'})






    for case in cases:
        o=case.find_all('li')

        for i in o:
            a=i.find_all('span',{'class':'chk-label'})
            a=a[1].text
            b=i.find('span',{'class':'cnt'})
            b=b.text
            daa.append([a,b])



    driver.find_element(By.CSS_SELECTOR, ".naukri-icon-times:nth-child(1)").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".expanded:nth-child(3)").click()



else:
    department = driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(9) .ico")
    department.click()

    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".more-industry").click()
    time.sleep(1)

    time.sleep(10)

    page = driver.execute_script('return document.body.innerHTML')
    page_soup = BeautifulSoup(''.join(page), 'html.parser')

    cases = page_soup.find_all('ul', {'class': 'filter-industry-list'})



    for case in cases:
        o = case.find_all('li')

        for i in o:
            a = i.find_all('span', {'class': 'chk-label'})
            a = a[1].text
            b = i.find('span', {'class': 'cnt'})
            b = b.text
            daa.append([a, b])



    driver.find_element(By.CSS_SELECTOR, ".naukri-icon-times:nth-child(1)").click()

    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".expanded:nth-child(3)").click()


df3=pd.DataFrame(daa,columns=['attributes','value'])

df1['Source'] = 'Location'
df2['Source'] = 'Department'
df3['Source'] = 'industry'

concat_df = pd.concat([df1, df2,df3], ignore_index=True)

concat_df.to_csv('concat_df.csv', index=False,mode='w')



a=experience_range_col1
b=experience_range_col2




time.sleep(1)



driver.find_element(By.LINK_TEXT, "Modify").click()



#_____________________________________gender_diversity_anywere_india____________________________________________________________
x=2



for i in range(3):

    time.sleep(3)
    driver.execute_script("window.scrollTo(0,800)")

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



    anywhere_india_data_genders.append(data)

    driver.find_element(By.LINK_TEXT, "Modify").click()







#........................................ check ............................................................



tic_count=0

tic = tic_location

vals = "Delhi / NCR"
length = 50
for i in range(len(tic)):

    time.sleep(3)

    driver.execute_script("window.scrollTo(0,0)")
    driver.execute_script("window.scrollTo(0,200)")

    if tic[i] == "delhi" or tic[i] == "mumbai":

        if tic[i] == "mumbai":
            vals = "Mumbai (All Areas)"
            length = 55
        else:
            vals = "Delhi / NCR"
            length = 50

        time.sleep(1)

        if tic_count==0:
            driver.find_element(By.ID, "prefLocCheckbox").click()
            tic_count=tic_count+1

        time.sleep(1)

        driver.find_element(By.NAME, "locations").click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".last > .tag-ico").click()

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

            location_count_data.append(data)

        except:

            location_count_data.append("0 profiles found for " + tic[i])


        try:

            driver.find_element(By.LINK_TEXT, "Modify").click()

        except:
            pass



    else:

        time.sleep(10)





        driver.execute_script("window.scrollTo(0,0)")
        driver.execute_script("window.scrollTo(0,200)")

        time.sleep(1)

        if tic_count == 0:
            driver.find_element(By.ID, "prefLocCheckbox").click()
            tic_count=tic_count+1



        time.sleep(3)

        driver.find_element(By.NAME, "locations").click()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR, ".last > .tag-ico").click()

        time.sleep(1)



        loc = driver.find_element(By.NAME, "locations")
        loc.click()
        loc.send_keys(tic[i])

        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".tuple-wrap:nth-child(1) > .opt").click()
        time.sleep(1)





        time.sleep(1)

        time.sleep(1)
        driver.find_element(By.ID, "adv-search-btn").click()

        time.sleep(10)

        try:

            data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

            tic_data.append(data)

        except:

            tic_data("0 profiles found for "+tic[i])

        driver.find_element(By.LINK_TEXT, "Modify").click()

#..............................................check.......................................................



time.sleep(10)





driver.execute_script("window.scrollTo(0,0)")
driver.execute_script("window.scrollTo(0,200)")


driver.find_element(By.ID, "prefLocCheckbox").click()


time.sleep(3)




time.sleep(10)







tic = location_for_experience

vals = "Delhi / NCR"
length = 50
for i in range(len(tic)):

    time.sleep(3)

    driver.execute_script("window.scrollTo(0,0)")
    driver.execute_script("window.scrollTo(0,200)")

    if tic[i] == "delhi" or tic[i] == "mumbai":

        if tic[i] == "mumbai":
            vals = "Mumbai (All Areas)"
            length = 55
        else:
            vals = "Delhi / NCR"
            length = 50

        time.sleep(1)


        time.sleep(1)

        driver.find_element(By.NAME, "locations").click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".last > .tag-ico").click()

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

            tic_data.append(data)

        except:

            tic_data.append("0 profiles found for " + tic[i])


        try:

            driver.find_element(By.LINK_TEXT, "Modify").click()

        except:
            pass



    else:

        time.sleep(10)





        driver.execute_script("window.scrollTo(0,0)")
        driver.execute_script("window.scrollTo(0,200)")

        time.sleep(1)



        time.sleep(3)

        driver.find_element(By.NAME, "locations").click()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR, ".last > .tag-ico").click()

        time.sleep(1)



        loc = driver.find_element(By.NAME, "locations")
        loc.click()
        loc.send_keys(tic[i])

        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".tuple-wrap:nth-child(1) > .opt").click()
        time.sleep(1)





        time.sleep(1)

        time.sleep(1)
        driver.find_element(By.ID, "adv-search-btn").click()

        time.sleep(10)

        try:

            data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

            tic_data.append(data)

        except:

            tic_data("0 profiles found for "+tic[i])

        driver.find_element(By.LINK_TEXT, "Modify").click()


































































































if length_of_the_extra_keyword == 0:
    x = 2

    vals = "Delhi / NCR"
    length = 50

    country=location_for_gender_diversity

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

            for j in range(3):

                time.sleep(3)
                driver.execute_script("window.scrollTo(0,0)")
                driver.execute_script("window.scrollTo(0,730)")

                time.sleep(1)

                if x == 2:
                    driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()

                elif j == 2:
                    driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child(1) > .txt").click()
                    time.sleep(3)
                    driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()
                    time.sleep(1)

                if j == 2:
                    break

                time.sleep(1)

                driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child({x}) > .txt").click()
                x = x + 1
                time.sleep(1)
                driver.find_element(By.ID, "adv-search-btn").click()

                time.sleep(10)

                try:

                    data=driver.find_element(By.CSS_SELECTOR, ".top-band-header").text
                    gender_diversity_data.append(data)
                except:
                    gender_diversity_data.append("0 profiles found for "+country[i])



                try:
                    driver.find_element(By.LINK_TEXT, "Modify").click()

                except:
                    pass

            x = 2

        else:

            driver.execute_script("window.scrollTo(0,0)")
            driver.execute_script("window.scrollTo(0,300)")

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

            for j in range(3):

                time.sleep(3)
                driver.execute_script("window.scrollTo(0,0)")
                driver.execute_script("window.scrollTo(0,730)")

                time.sleep(1)

                if x == 2:
                    driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()

                elif j == 2:
                    driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child(1) > .txt").click()
                    time.sleep(3)
                    driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()
                    time.sleep(1)

                if j == 2:
                    break

                time.sleep(1)

                driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child({x}) > .txt").click()
                x = x + 1
                time.sleep(1)
                driver.find_element(By.ID, "adv-search-btn").click()

                time.sleep(10)


                try:

                    data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text
                    gender_diversity_data.append(data)

                except:
                    gender_diversity_data.append("0 profiles found for ",country[i])




                try:
                    driver.find_element(By.LINK_TEXT, "Modify").click()

                except:
                    pass

            x = 2


    # ______________________________________________________________________________________________________________

    # experience

    driver.find_element(By.NAME, "minExp").click()
    time.sleep(3)
    driver.find_element(By.NAME, 'minExp').send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
    time.sleep(3)
    driver.find_element(By.NAME, "maxExp").click()
    time.sleep(3)
    driver.find_element(By.NAME, "maxExp").send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
    time.sleep(3)

    driver.find_element(By.NAME, "v3-adv").click()

    country = location_for_experience

    vals = "Delhi / NCR"
    length = 50
    for i in range(len(country)):

        driver.execute_script("window.scrollTo(0,0)")
        driver.execute_script("window.scrollTo(0,300)")

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
            driver.find_element(By.ID, "adv-search-btn").click()

            time.sleep(10)

            try:

                data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text



                time.sleep(10)

                for l, m in zip(a, b):
                    driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(4) .ico").click()
                    time.sleep(10)

                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(l)
                    time.sleep(5)

                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(m)
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR, ".naukri-btn-primary").click()
                    time.sleep(1)
                    data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

                    time.sleep(3)

                    experience_split_data.append(data)

                    driver.find_element(By.CSS_SELECTOR, ".clear-all").click()
                    time.sleep(5)

                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                location_count_data.append("0 Profiles found for "+ country[i])


        else:


            time.sleep(10)




            driver.execute_script("window.scrollTo(0,0)")
            driver.execute_script("window.scrollTo(0,300)")

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

            time.sleep(1)
            driver.find_element(By.ID, "adv-search-btn").click()

            time.sleep(10)

            try:

                data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text



                time.sleep(10)

                for l, m in zip(a, b):
                    driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(4) .ico").click()
                    time.sleep(10)

                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(l)
                    time.sleep(5)

                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(m)
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR, ".naukri-btn-primary").click()
                    time.sleep(1)
                    data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

                    time.sleep(3)

                    experience_split_data.append(data)
                    driver.find_element(By.CSS_SELECTOR, ".clear-all").click()
                    time.sleep(5)

                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                location_count_data.append("0 Profiles found for " + country[i])

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




#______________________________________________  gender____________________________________________________________________________


else:

    x=2


    vals="Delhi / NCR"
    length=50


    country = location_for_gender_diversity

    for i in range(len(country)):

        driver.execute_script("window.scrollTo(0,0)")
        driver.execute_script("window.scrollTo(0,300)")



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

            driver.find_element(By.CSS_SELECTOR, ".last > .tag-ico").click()

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

            for j in range(3):

                time.sleep(3)
                driver.execute_script("window.scrollTo(0,0)")
                driver.execute_script("window.scrollTo(0,900)")

                time.sleep(1)

                if x == 2:
                    driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()

                elif j == 2:
                    driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child(1) > .txt").click()
                    time.sleep(3)
                    driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()
                    time.sleep(1)

                if j == 2:
                    break

                time.sleep(1)

                driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child({x}) > .txt").click()
                x = x + 1
                time.sleep(1)
                driver.find_element(By.ID, "adv-search-btn").click()

                time.sleep(10)


                try:


                    data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text
                    gender_diversity_data.append(data)

                except:
                    gender_diversity_data.append("0 profiles found for "+ country[i])


                try:
                    driver.find_element(By.LINK_TEXT, "Modify").click()

                except:
                    pass

            x = 2

        else:

            driver.execute_script("window.scrollTo(0,0)")
            driver.execute_script("window.scrollTo(0,300)")

            driver.find_element(By.NAME, "locations").click()
            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, ".last > .tag-ico").click()

            time.sleep(1)

            loc = driver.find_element(By.NAME, "locations")
            loc.click()
            loc.send_keys(country[i])

            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, ".tuple-wrap:nth-child(1) > .opt").click()
            time.sleep(1)

            for j in range(3):

                time.sleep(3)
                driver.execute_script("window.scrollTo(0,0)")
                driver.execute_script("window.scrollTo(0,900)")

                time.sleep(1)


                if x==2:
                    driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()

                elif j==2:
                    driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child(1) > .txt").click()
                    time.sleep(3)
                    driver.find_element(By.CSS_SELECTOR, ".diversity-details svg").click()
                    time.sleep(1)

                if j==2:
                    break

                time.sleep(1)

                driver.find_element(By.CSS_SELECTOR, f".frow > .wrap .focusable:nth-child({x}) > .txt").click()
                x=x+1
                time.sleep(1)
                driver.find_element(By.ID, "adv-search-btn").click()

                time.sleep(10)


                try:


                    data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text
                    gender_diversity_data.append(data)

                except:

                    gender_diversity_data.append("profiles found for"+country[i])





                try:
                    driver.find_element(By.LINK_TEXT, "Modify").click()

                except:
                    pass

            x=2


#"working"

#______________________________________________________________________________________________________________

    # experience

    driver.find_element(By.NAME, "minExp").click()
    time.sleep(3)
    driver.find_element(By.NAME, 'minExp').send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
    time.sleep(3)
    driver.find_element(By.NAME, "maxExp").click()
    time.sleep(3)
    driver.find_element(By.NAME, "maxExp").send_keys(Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE)
    time.sleep(10)

    driver.find_element(By.NAME, "v3-adv").click()





    country= location_for_experience

    vals = "Delhi / NCR"
    length=50
    for i in range(len(country)):


        driver.execute_script("window.scrollTo(0,0)")
        driver.execute_script("window.scrollTo(0,300)")

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

            driver.find_element(By.CSS_SELECTOR, ".last > .tag-ico").click()

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





                time.sleep(10)

                for l, m in zip(a, b):
                    driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(5) .ico").click()
                    time.sleep(10)

                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(l)
                    time.sleep(5)

                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(m)
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR, ".naukri-btn-primary").click()
                    time.sleep(1)
                    data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

                    time.sleep(3)

                    experience_split_data.append(data)
                    driver.find_element(By.CSS_SELECTOR, ".focusable:nth-child(2) > .tag-ico").click()
                    time.sleep(5)

                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                location_count_data.append("0 profiles found for "+country[i])


        else:

            time.sleep(3)




            driver.execute_script("window.scrollTo(0,0)")
            driver.execute_script("window.scrollTo(0,200)")

            driver.find_element(By.NAME, "locations").click()
            time.sleep(1)


            driver.find_element(By.CSS_SELECTOR,".last > .tag-ico").click()

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

            try:

                data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text



                time.sleep(10)

                for l, m in zip(a, b):
                    driver.find_element(By.CSS_SELECTOR, ".collapser-wrapper:nth-child(5) .ico").click()
                    time.sleep(10)

                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(l)
                    time.sleep(5)

                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").click()
                    driver.find_element(By.XPATH, "(//input[@value=''])[2]").send_keys(m)
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR, ".naukri-btn-primary").click()
                    time.sleep(1)
                    data = driver.find_element(By.CSS_SELECTOR, ".top-band-header").text

                    time.sleep(3)

                    experience_split_data.append(data)
                    driver.find_element(By.CSS_SELECTOR, ".focusable:nth-child(2) > .tag-ico").click()
                    time.sleep(5)

                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                location_count_data.append("0 profiles found for "+country[i])




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





print(anywhere_india_data)
print(anywhere_india_data_genders)
print(gender_diversity_data)
print(experience_split_data)
print(location_count_data)
print(tic_data)


anywhere_india_data=pd.DataFrame(anywhere_india_data,columns=['attributes'])
anywhere_india_data.to_csv('anywhere_india_data.csv',index=False)

anywhere_india_data_genders =pd.DataFrame(anywhere_india_data_genders,columns=['attributes'])
anywhere_india_data_genders.to_csv('anywhere_india_data_genders.csv',index=False)

gender_diversity_data =pd.DataFrame(gender_diversity_data,columns=['attributes'])

gender_diversity_data.to_csv("gender_diversity_data.csv",index=False)

experience_split_data =pd.DataFrame(experience_split_data,columns=['attributes'])
experience_split_data.to_csv("experience_data.csv",index=False)

location_count_data =pd.DataFrame(location_count_data,columns=['attributes'])
location_count_data.to_csv("location_count.csv",index=False)

tic_data =pd.DataFrame(tic_data,columns=['attributes'])
tic_data.to_csv('tic_data.csv',index=False)


anywhere_india_data['Source'] = 'anywhere_india_data'
anywhere_india_data_genders['Source'] = 'anywhere_india_data_genders'
gender_diversity_data['Source'] = 'gender_diversity_data'
experience_split_data['Source']='experience_split_data'
location_count_data['Source']='location_count_data'
tic_data['Source']='tic_data'


concat_df_2 = pd.concat([anywhere_india_data, anywhere_india_data_genders,gender_diversity_data,experience_split_data,location_count_data,tic_data], ignore_index=True)

concat_df_2.to_csv('concat_df_2.csv', index=False,mode='w')

driver.quit()


