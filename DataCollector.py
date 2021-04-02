from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def completeForm(driver, eloMin, eloMax, tipus):

    driver.get('https://lichess.org/games/search')

    eloMinXPath = '//*[@id="form3-ratingMin"]'
    eloMaxXPath = '//*[@id="form3-ratingMax"]'
    tipusXPath = '//*[@id="form3-perf"]'

    if tipus == 'B':
        tipus = 1
    elif tipus == 'R':
        tipus = 6
    elif tipus == 'C':
        tipus = 3
    else:
        return -1

    s = Select(driver.find_element_by_xpath(eloMinXPath))
    s.select_by_value(str(eloMin))
    s = Select(driver.find_element_by_xpath(eloMaxXPath))
    s.select_by_value(str(eloMax))
    s = Select(driver.find_element_by_xpath(tipusXPath))
    s.select_by_value(str(tipus))
    # always rated games // 0 = casual, 1 = rated
    s = Select(driver.find_element_by_xpath('//*[@id="form3-mode"]'))
    s.select_by_value('1')

    driver.find_element_by_xpath('//*[@id="main-wrap"]/main/form/table/tbody/tr[22]/td/button').click()

    return

def getDataGame(driver, XPath, attributeName):
    return str(driver.find_element_by_xpath(XPath).get_attribute(attributeName))

def getPlayerWhiteName(driver, XPath, attributeName):
    return str(driver.find_element_by_xpath(XPath).get_attribute(attributeName))

def getPlayerBlackName(driver, XPath, attributeName):
    return str(driver.find_element_by_xpath(XPath).get_attribute(attributeName))

def getWhiteElo(driver, XPath):
    return str(driver.find_element_by_xpath(XPath).text)

def getBlackElo(driver, XPath):
    return str(driver.find_element_by_xpath(XPath).text)

def getOppening(driver, XPath):
    return str(driver.find_element_by_xpath(XPath).text)

def getWinner(driver, XPath):
    value = str(driver.find_element_by_xpath(XPath).text)
    if "blancas ganan" in value:
        return '1-0'
    elif "negras ganan" in value:
        return '0-1'
    else:
        return '1/2-1/2' 

def getFileData(driver, fileNum):

    resultsXPath = '//*[@id="results"]/div[2]'
    gameXPath = '//*[@id="results"]/div[2]/article[' + str(fileNum) + ']/div[2]'

    data = []
    data.append(getDataGame(driver, gameXPath + '/div[1]/div/time', 'title'))
    data.append(getPlayerWhiteName(driver, gameXPath + '/div[2]/div[1]/a', 'href'))
    data.append(getPlayerWhiteName(driver, gameXPath + '/div[2]/div[3]/a', 'href'))
    data.append(getWhiteElo(driver, gameXPath + '/div[2]/div[1]'))
    data.append(getBlackElo(driver, gameXPath + '/div[2]/div[3]'))
    data.append(getOppening(driver, gameXPath + '/div[4]/strong'))
    data.append(getWinner(driver,gameXPath + '/div[3]/span'))

    # neteja de dades

    data[1] = data[1].replace('https://lichess.org/@/','')  # nom white
    data[2] = data[2].replace('https://lichess.org/@/','')  # nom black

    data[3] = data[3].replace(data[1]+'\n','')
    data[4] = data[4].replace(data[2]+'\n','')
    data[3] = data[3][0:len(data[3])-3]
    data[4] = data[4][0:len(data[4])-3]
    print(data)

    return data

def getData(eloMin, eloMax, tipus, numFiles):

    data = []

    try:
        lichessMainLink = 'https://lichess.org/login?referrer=/'
        lichessFormLink = 'https://lichess.org/games/search'

        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get(lichessMainLink)

        # log in
        usernameXPath = '//*[@id="form3-username"]'
        passwrodXPath = '//*[@id="form3-password"]'
        logInButtonXPath = '//*[@id="main-wrap"]/main/form/div[1]/button'

        driver.find_element_by_xpath(usernameXPath).click()
        driver.find_element_by_xpath(usernameXPath).send_keys('vitolopaolo')
        driver.find_element_by_xpath(passwrodXPath).click()
        driver.find_element_by_xpath(passwrodXPath).send_keys('31415920865255')
        driver.find_element_by_xpath(logInButtonXPath).click()

        time.sleep(4)

        # lichess form

        completeForm(driver, eloMin, eloMax, tipus)

        # scroll down
        for i in range(0,3):
            driver.execute_script("window.scrollTo(0, 9999)")
            time.sleep(2)
            print('scroll ' + str(i))

        # get different data
        
        for i in range(0,numFiles):
            data.append(getFileData(driver, i+1))

    except:
        print("S'han recollit " + str(len(data)) + " durant la cerca amb error")
        return data
    print("S'han recollit " + str(len(data)) + " durant la cerca sense error")
    return data

def main():

    aux = getData()

    return 0

if __name__ == '__main__':
    main()