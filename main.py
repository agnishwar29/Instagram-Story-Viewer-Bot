from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)

username = 'playing_underrated_games'
password = '19Arka99'


class StoryViewer:
    # initializing the username and the password field and the url for instagram login page
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__url = "https://www.instagram.com/"

    # calling functions from here
    def start(self):
        # Function to log in
        self.__login()

        # Function to visit profile, needs a list of usernames but currently not implemented
        self.__visit_profile([])

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

    def __visit_profile(self, profiles):

        sleep = 3

        time.sleep(sleep)
        # go to search bar
        search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]'
                                                   '/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys("arcturuschild")
        time.sleep(sleep)

        # click on first account
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/'
                            'div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div').click()

        time.sleep(sleep)
        # click on followers
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/'
                                      'section/main/div/header/section/ul/li[2]/a/div').click()

        time.sleep(sleep)

        def view_story(*, profile_xpath):
            driver.find_element(By.XPATH,profile_xpath).click()
            try:
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/div/div/span/img').click()
                print("Clicked")
            except:
                print("No story")
                print("Going back")
                driver.execute_script("window.history.go(-1)")
                action = webdriver.ActionChains(driver)
                action.move_by_offset(10, 20).perform()

        p_xpath = ['/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/span/a/span/div',
                   '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div/span/a/span/div',
                   '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div/span/a/span/div']

        for i in p_xpath:
            view_story(profile_xpath=i)


viewer = StoryViewer(username, password)
viewer.start()
