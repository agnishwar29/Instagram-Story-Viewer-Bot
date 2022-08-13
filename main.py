from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)


class StoryViewer:
    # initializing the username and the password field and the url for instagram login page
    def __init__(self, *, username, password,target_profile, n_profiles):
        self.__username = username
        self.__password = password
        self.__url = "https://www.instagram.com/"
        self.__profiles = int(n_profiles)
        self.__target_profile = target_profile

    # calling functions from here
    def start(self):
        # Function to log in
        try:
            self.__login()
            self.__visit_profile(self.__target_profile)
        except:
            return

    # Log in function
    def __login(self):
        # Setting a sleep timer for 3 seconds
        sleep = 3

        # Getting instagram login page
        driver.get("https://www.instagram.com/")

        # waiting for page to load
        time.sleep(2)

        # username input
        user_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_input.send_keys(self.__username)

        # password input
        password_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(self.__password)

        # login button
        time.sleep(2)
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
    # Going to target profile
    def __target(self, profile_id):

        sleep = 3

        time.sleep(sleep)
        # go to search bar
        search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]'
                                                   '/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(profile_id)
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

    def __visit_profile(self, profile):

        self.__target(profile)

        # account xpath of n number of accounts
        p_xpaths = [
            f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[' \
            f'1]/div/div[{i}]/div[2]/div[1]/div/div/span/a/span/div '
            for i in range(1, self.__profiles + 1)]

        viewed = 0

        for i in p_xpaths:
            time.sleep(1)
            try:
                # click on next profile
                driver.find_element(By.XPATH, i).click()

                time.sleep(2)

                # Click on story
                driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div['
                                    '1]/section/main/div/header/div/div/span/img').click()
                time.sleep(3)
                # Story like logic should be here
                try:
                    # Closing story currently
                    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[3]/button').click()
                    time.sleep(1)

                    # Going back two times // there might be a glitch in Instagram
                    driver.execute_script("window.history.go(-1)")
                    driver.execute_script("window.history.go(-1)")
                    viewed +=1
                    print("Seen Story ")
                    continue
                except:
                    # if there's no story going back
                    print("No Story")
                    driver.execute_script("window.history.go(-1)")
                    time.sleep(1)
                    viewed += 1
                    continue
            except:
                # if any error to open story or profile simply going back
                print("No Story")
                driver.execute_script("window.history.go(-1)")
                viewed += 1
                continue

        print(f"{viewed} Profiles Viewed")
        driver.close()

# username = 'playing_underrated_games'
# password = '19Arka99'

username = 'test_911_test'
password = 'Agni@Arka911'


viewer = StoryViewer(username=username, password=password,target_profile="agnishwar.art", n_profiles=5)
viewer.start()
