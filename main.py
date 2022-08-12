from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)


class StoryViewer:
    # initializing the username and the password field and the url for instagram login page
    def __init__(self, *, username, password, n_profiles):
        self.__username = username
        self.__password = password
        self.__url = "https://www.instagram.com/"
        self.__profiles = int(n_profiles)

    # calling functions from here
    def start(self):
        # Function to log in
        try:
            self.__login()
            self.__visit_profile([])
        except:
            return

    # Log in function
    def __login(self):
        # Setting a sleep timer for 3 seconds
        sleep = 3

        # Getting instagram login page
        driver.get("https://www.instagram.com/")

        # waiting for page to load
        time.sleep(sleep)

        # username input
        user_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_input.send_keys(self.__username)

        # password input
        password_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(self.__password)

        # login button
        time.sleep(sleep)
        try:
            driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()

            # handle popups
            time.sleep(sleep)
            # Save login info
            driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()

            time.sleep(sleep)

            # turn on notification pop-up
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/'
                                          'div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()

            print("Successfully Logged in")



        except:
            print("Error Occurred")
            return

    def __visit_profile(self, profiles):

        sleep = 3

        time.sleep(sleep)
        # go to search bar
        search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]'
                                                   '/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys("arcturuschild")
        time.sleep(sleep)

        # click on first account on searchbar
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/'
                            'div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div').click()

        time.sleep(sleep)

        # click on followers
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/'
                                      'section/main/div/header/section/ul/li[2]/a/div').click()
        time.sleep(sleep)
        # account xpath of n number of accounts
        p_xpaths = [
            f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[{i}]/div[2]/div[1]/div/div/span/a/span/div'
            for i in range(1, self.__profiles + 1)]

        viewed = 0

        for i in p_xpaths:

            try:
                # click on next profile
                driver.find_element(By.XPATH, i).click()

                time.sleep(2)

                # Click on story
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/div/div/span/img').click()

                # Story like logic should be here
                time.sleep(3)

                # get back to profile
                driver.execute_script("window.history.go(-1)")

                time.sleep(1)

                # get back to followers list
                driver.execute_script("window.history.go(-1)")

                time.sleep(2)

                viewed += 1
                print("Seen a profile ", viewed)
                continue

            except:
                # click on followers button
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/'
                                              'section/main/div/header/section/ul/li[2]/a/div').click()
                time.sleep(1)
                # click on next profile
                driver.find_element(By.XPATH, i).click()

                time.sleep(2)

                # click on story
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/div/div/span/img').click()

                # Story like logic should be here
                time.sleep(3)

                # go back to profile
                driver.execute_script("window.history.go(-1)")

                time.sleep(1)

                # go back to followers list
                driver.execute_script("window.history.go(-1)")

                time.sleep(2)
                viewed += 1
                print("Seen a profile ", viewed)
                continue


username = 'playing_underrated_games'
password = '19Arka99'

# username = 'test_911_test'
# password = 'Agni@Arka911'


viewer = StoryViewer(username=username, password=password, n_profiles=5)
viewer.start()
