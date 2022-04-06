import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class LTAutomate(unittest.TestCase):
    """
    LambdaTest selenium automation sample example
    Configuration
    ----------
    username: Username can be found at automation dashboard
    accessToken:  AccessToken can be genarated from automation dashboard or profile section

    Result
    -------
    Execute Test on lambdatest Distributed Grid perform selenium automation based 
    """

    
    def setUp(self):
        """
        Setup remote driver
        Params
        ----------
        platfrom : Supported platfrom - (Windows 10, Windows 8.1, Windows 8, Windows 7,  macOS High Sierra, macOS Sierra, OS X El Capitan, OS X Yosemite, OS X Mavericks)
        browserName : Supported platfrom - (chrome, firefox, Internet Explorer, MicrosoftEdge)
        version :  Supported list of version can be found at https://www.lambdatest.com/capabilities-generator/

        Result
        -------
        """
        # username: Username can be found at automation dashboard
        username=os.getenv('LT_USERNAME') 
                
        # accessToken:  AccessToken can be genarated from automation dashboard or profile section
        accessToken=os.getenv('LT_ACCESS_KEY') 
        # gridUrl: gridUrl can be found at automation dashboard
        gridUrl = os.getenv('LT_GRID_URL')
        
        desired_cap = {
            'platform' : "win10", 
            'browserName' : "chrome",
            'version' :  "latest-4",
            # Resolution of machine
            "name": "LambdaTest python google search test ",
            "build": "LambdaTest python google search build",
            "network": True,
            "video": True,
            "visual": True,
            "console": True,
        }

        #url = "http://"+username+":"+accessToken+"@"+gridUrl
        url = gridUrl
        
        print("Initiating remote driver on platfrom: "+desired_cap["platform"]+" browser: "+desired_cap["browserName"]+" version: "+desired_cap["version"] + ", url : "+url)
        self.driver = webdriver.Remote(
            desired_capabilities=desired_cap,
            command_executor= url
        )

    
    def test_search_in_google(self):
        """
        Setup remote driver
        Params
        ----------
        Execute test:  navigate google.com search LambdaTest
        Result
        -------
        print title
        """
        driver = self.driver
        print("Driver initiated sucessfully.  Navigate url")

        val = 7 # in seconds
        driver.implicitly_wait(val)
        driver.get("https://www.google.com/ncr")

        element = driver.find_element_by_link_text("Courses")
        print("Searching lambdatest on google.com ")

        print("Printing title of current page :"+driver.title)
        driver.execute_script("lambda-status=passed")
        print("Requesting to mark test : pass")

    
    def tearDown(self):
        """
        Quit selenium driver
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
