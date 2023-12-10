from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(service=service)

browser.get(
    url='https://www.google.com/search?q=TI+empregos&sca_esv=589543827&sxsrf=AM9HkKlaLNce1_cMaHXPNxyEbJ-zyhgnXA'
        ':1702206087869&ei=h5p1ZZrbNKXR1sQPt6CgqAM&uact=5&oq=TI+empregos&gs_lp'
        '=Egxnd3Mtd2l6LXNlcnAiC1RJIGVtcHJlZ29zMgUQABiABDIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHkjXDVDABFjIDHABeAGQAQCYAaoBoAH-CaoBAzAuObgBA8gBAPgBAcICChAAGEcY1gQYsAPCAg0QABiABBiKBRhDGLADwgIKECMYgAQYigUYJ8ICChAAGIAEGIoFGEPCAgoQLhiABBiKBRhDwgIHEAAYgAQYCsICBxAuGIAEGArCAgoQABiABBgUGIcC4gMEGAAgQYgGAZAGCg&sclient=gws-wiz-serp&ibp=htl;jobs&sa=X&ved=2ahUKEwjy4L_r24SDAxVOrpUCHTAXC38QudcGKAF6BAgaECo#htivrt=jobs&htidocid=bQR1n9MnRGadhA7oAAAAAA%3D%3D&fpstate=tldetail')


wait = WebDriverWait(browser, 10)
jobs_div = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'nJXhWc')))

for div in jobs_div:

    uls = div.find_element(By.TAG_NAME, 'ul')

    lis = uls.find_elements(By.TAG_NAME, 'li')

    for li in lis:
        elem = li.find_element(By.CLASS_NAME, 'BjJfJf')
        textContent = elem.get_attribute('textContent')

        print(textContent)

browser.quit()
