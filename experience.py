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


time.sleep(3)


driver.find_element(By.XPATH,"//li[contains(.,'Resume title and keyskills')]").click()
time.sleep(1)
driver.find_element(By.NAME, "boolKeywords").send_keys(keyword[0])

time.sleep(1)
driver.find_element(By.NAME, "v3-adv").click()

driver.execute_script("window.scrollTo(0,400)")


driver.find_element(By.NAME, "minCtc").click()
driver.find_element(By.NAME,'minCtc').send_keys(3)
driver.find_element(By.NAME, "v3-adv").click()

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

time.sleep(3)




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


else:
    pass









driver.find_element(By.LINK_TEXT, "Modify").click()





a=experience_range_col1
b=experience_range_col2


location = []
Ex_range = []
salery = []


country=location_for_experience

x=0

if  length_of_the_extra_keyword==0:
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


                    time.sleep(3)

                    try:

                        driver.find_element(By.CSS_SELECTOR, ".show-page-wrap:nth-child(2) .dropArrowDD").click()
                        time.sleep(2)
                        driver.find_element(By.XPATH, "//li[@value='a3']").click()

                        time.sleep(1)


                        page = driver.execute_script('return document.body.innerHTML')
                        page_soup = BeautifulSoup(''.join(page), 'html.parser')




                        cases = page_soup.find_all('div', {'class': 'candidate-overview'})


                    except:

                        location.append(country[i])

                        Ex_range.append([l, m])

                        salery.append('No_profile_found')




                    for candidate_overview in cases:
                        try:
                            salary_div = candidate_overview.find_all('div', {'class': 'meta-data'})[1]
                            title = salary_div.find('span')['title']

                            location.append(country[i])
                            Ex_range.append([l, m])
                            salery.append(title)
                        except:
                            print("None")

                    driver.find_element(By.CSS_SELECTOR, ".clear-all").click()
                    time.sleep(5)

                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                print(country[i]+"Profile not found ")


        else:

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


                    time.sleep(3)

                    try:


                        driver.find_element(By.CSS_SELECTOR, ".show-page-wrap:nth-child(2) .dropArrowDD").click()
                        time.sleep(2)
                        driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > span > span").click()

                        time.sleep(3)

                        page = driver.execute_script('return document.body.innerHTML')
                        page_soup = BeautifulSoup(''.join(page), 'html.parser')



                        cases = page_soup.find_all('div', {'class': 'candidate-overview'})


                    except:

                        location.append(country[i])
                        Ex_range.append([l, m])
                        salery.append('No_profile_found')


                    for candidate_overview in cases:
                        try:

                            salary_div = candidate_overview.find_all('div', {'class': 'meta-data'})[1]
                            title = salary_div.find('span')['title']



                            location.append(country[i])
                            Ex_range.append([l, m])
                            salery.append(title)
                        except:
                            print("None")
                    driver.find_element(By.CSS_SELECTOR, ".clear-all").click()
                    time.sleep(5)

                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                print(country[i]+"Profile not found ")

else:



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

                    try:

                        driver.find_element(By.CSS_SELECTOR, ".show-page-wrap:nth-child(2) .dropArrowDD").click()
                        time.sleep(2)
                        driver.find_element(By.XPATH, "//li[@value='a3']").click()

                        time.sleep(1)

                        page = driver.execute_script('return document.body.innerHTML')
                        page_soup = BeautifulSoup(''.join(page), 'html.parser')



                        cases = page_soup.find_all('div', {'class': 'candidate-overview'})


                    except:

                        location.append(country[i])
                        Ex_range.append([l, m])
                        salery.append('No_profile_found')

                    for candidate_overview in cases:
                        try:
                            salary_div = candidate_overview.find_all('div', {'class': 'meta-data'})[1]
                            title = salary_div.find('span')['title']

                            location.append(country[i])
                            Ex_range.append([l, m])
                            salery.append(title)
                        except:
                            print("None")

                    driver.find_element(By.CSS_SELECTOR, ".focusable:nth-child(2) > .tag-ico").click()
                    time.sleep(5)

                    time.sleep(3)


                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                location_count_data.append("0 profiles found for " + country[i])


        else:

            time.sleep(3)

            driver.execute_script("window.scrollTo(0,0)")
            driver.execute_script("window.scrollTo(0,200)")

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

                    time.sleep(3)

                    try:

                        driver.find_element(By.CSS_SELECTOR, ".show-page-wrap:nth-child(2) .dropArrowDD").click()
                        time.sleep(2)
                        driver.find_element(By.XPATH, "//li[@value='a3']").click()

                        time.sleep(1)

                        page = driver.execute_script('return document.body.innerHTML')
                        page_soup = BeautifulSoup(''.join(page), 'html.parser')



                        cases = page_soup.find_all('div', {'class': 'candidate-overview'})

                    except:
                        location.append(country[i])
                        Ex_range.append([l, m])
                        salery.append('No_profile_found')




                    for candidate_overview in cases:
                        try:
                            salary_div = candidate_overview.find_all('div', {'class': 'meta-data'})[1]
                            title = salary_div.find('span')['title']

                            location.append(country[i])
                            Ex_range.append([l, m])
                            salery.append(title)
                        except:
                            print("None")

                    experience_split_data.append(data)
                    driver.find_element(By.CSS_SELECTOR, ".focusable:nth-child(2) > .tag-ico").click()
                    time.sleep(5)

                driver.find_element(By.LINK_TEXT, "Modify").click()

            except:
                location_count_data.append("0 profiles found for " + country[i])


print(location,Ex_range,salery)

df = pd.DataFrame({'location': location, 'Ex_range': Ex_range, 'salary': salery})

df.to_csv('Salery.csv')



























#_______________________________________________________________________________________________________________________________________________________________________
#narmal search


