# from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
# from selenium.webdriver.common.by import By
# it needs some native things.
# but it is always the fuck.
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support import expected_conditions as expected
# from selenium.webdriver.support.wait import WebDriverWait
import re
from process_dom import bing_dom
import traceback
import time
import copy


def parser(a):
    return "+".join(re.findall(r'[^ ]+', a))

# if __name__ == "__main__":


def getSearched(a):
    fx = []
    f = parser(a)
    # d=d*10
    # it does not supports paging.
    # should consider javascript execution.
    # d=str(d)
    try:
        fireFoxOptions = Options()
    #    fireFoxOptions.set_headless()
    #    print(fireFoxOptions.headless)
    #    fireFoxOptions.headless=True
        fireFoxOptions.add_argument("-headless")
        # not working.
    # not headless. why the fuck?
    # nvm. we just need the dom.
    # we will have timeout.
        # what the heck?
        brower = Firefox(executable_path='geckodriver', options=fireFoxOptions)
        # shit-like.
        # brower = Firefox(executable_path='geckodriver',firefox_options=fireFoxOptions)
        # e='https://cn.bing.com/search?q='+f+'&qs=n&form=QBRE&sp=-1&pq='+f+'&sc=3-19&first='+d
        # there is nothing.
        # e="https://cn.bing.com/search?q="+f+"&first="+d+"&qs=HS&sc=8-0&form=QBRE&sp=1&FORM=PERE"
        # e="https://cn.bing.com/search?q="+f+"&qs=HS&sc=8-0&sp=2&first="+d+"&FORM=PERE"
        e = "https://cn.bing.com/search?q="+f+"&qs=HS&sc=8-0&sp=1&first=28&FORM=PERE2"
        # https://cn.bing.com/search?q=tensorflow+has+no+attribute+contrib&qs=HS&sc=8-0&sp=1&first=20&FORM=PERE
        # print(e)
        # wait = WebDriverWait(brower, timeout=10)
    #     driver.get('https://pythonbasics.org')
        brower.get(e)
        # wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
        # wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
        # print(brower.page_source)
        max_try = 20
        # really strange.
        while max_try >= 0:
            time.sleep(0.1)
            fx = copy.copy(brower.page_source)
            fx = bing_dom(fx)
            if fx != []:
                brower.quit()
                return fx
            else:
                max_try -= 1
        brower.quit()
        # print(fx)
        return fx
        # print(type(brower.page_source))
        # # dead code.
        # if fx is not None:
        #     pass
    except:
        print(traceback.format_exc())
    finally:
        try:
            brower.quit()
            return fx
        except:
            print(traceback.format_exc())
            pass
    return fx


# def getLinked(a,d):
#     g=getSearched(a,d)
#     if g is not None:
#         return bing_dom(g)
#         # error is here.
#     return


# from selenium.webdriver import Firefox
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support import expected_conditions as expected
# from selenium.webdriver.support.wait import WebDriverWait

# if __name__ == "__main__":
#     options = Options()
#     options.add_argument('-headless')
#     driver = Firefox(executable_path='geckodriver', options=options)
#     # wait = WebDriverWait(driver, timeout=10)
#     driver.get('https://pythonbasics.org')
#     # wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
#     # wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
#     print(driver.page_source)
#     # maybe it is working.
#     driver.quit()
