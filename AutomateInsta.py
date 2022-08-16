from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = r"C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)


class StoryViewer:

    """
        The StoryViewer class takes 4 positional arguments : username, password, target_profile,
        number of profiles.
        username : username of the account to use for viewing stories
        password: password of the account to user
        target_profile : The profile to get follower list from
        n_profiles : The number of profiles to visit and view stories (This doesn't count number of stories)
    """


    # initializing the username and the password field and the url for instagram login page
    def __init__(self, *, username, password, target_profile, n_profiles):
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
        """
            Going to the login page of Instagram. Entering the username and the password taken from user input.
            Created a try block to handle any exception there. If there's any issue closing the driver.
            otherwise handling the "save info" pop-up and "turn on notification" pop-up.
            If logged in successfully getting to the next process.
        """

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
            driver.close()
            return

    # Going to target profile
    def __target(self, profile_id):

        """
        Taking the target profile from __visit_profile function call. Going to the search bar and sending the
        profile id. Clicking on the first result. Going to the follower list of that profile.
        """

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

        # Going to target profile's followers list
        self.__target(profile)

        # account xpath of n number of accounts
        p_xpaths = [
            f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[' \
            f'1]/div/div[{i}]/div[2]/div[1]/div/div/span/a/span/div '
            for i in range(1, self.__profiles + 1)]

        viewed = 0

        """ 
        ---------------------------------------------------------------------------------------------------------------
            Creating a list of profile xpath and a variable to store number of profiles visited.
            Looping over all the paths and trying to click each profile.
            If entered in a profile:
                1 > Clicking on the story [there's a story].
                2 > Another try block to handle story viewing
                    setting a variable to store maximum number of stories to view. A while loop to iterate over and 
                    view. If it's a first story then clicking on first button else clicking on next.
                    If couldn't click next button breaking while loop and continuing to other options.
                3 > After viewing stories going back one step [already in story profile home page] and continuing.

            If there's an issue to enter the profile or viewing the story:
                1 > Going back and continuing   
        ---------------------------------------------------------------------------------------------------------------
        """

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
                    # Story viewing logic || currently visiting up to 5 stories
                    story = 15
                    while story != 0:
                        try:
                            if story == 15:
                                # Clicking the like button
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[3]/div/div/div[2]/span/button').click()
                                time.sleep(1)

                                # first next button in the story
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/button/div').click()

                                story -= 1
                            else:
                                # Clicking the like button
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/div[3]/div/div/div[2]/span/button').click()
                                time.sleep(1)
                                # second next button in the story
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div[1]/div/section/div/button[2]/div').click()

                                story -= 1
                        except:
                            break

                    if story != 15:
                        time.sleep(2)
                        # going back to follower list || Adding two times, there's a glitch in instagram
                        driver.execute_script("window.history.go(-1)")
                        driver.execute_script("window.history.go(-1)")
                        viewed += 1
                        print("Seen Story ")
                        continue
                    else:
                        viewed += 1
                        print("No Story")
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
                print("Couldn't enter")
                driver.execute_script("window.history.go(-1)")
                viewed += 1
                continue

        print(f"{viewed} Profiles Viewed")
        driver.close()

