class openBrowser:
    def __init__(self):
        global requests
        from all_imports import selenium
        print(
            'Your Selenium version: ' + str(selenium.__version__))  # The driver below is set for Selenium 4.1.0. Please
        # change it if you have another version on your machine. Samples here: https://pypi.org/project/webdriver-manager/
        target_url_: str = 'https://www.gmail.com/'

        # Unfortunately the browser keeps closing automatically while using ChromeDriverManager. Probably the
        # driver gets garbage-collected. So I was compelled to use a machine-located driver.
        def start_browser():
            from all_imports import os, abspath, Service, webdriver
            drv_path_: str = abspath('../driver_/chromedriver_win32').replace('/', os.path.sep)
            drv_name_: str = 'chromedriver.exe'
            service_ = Service(drv_path_ + os.path.sep + drv_name_)
            chrome_opts_ = webdriver.ChromeOptions()
            chrome_opts_.add_argument("start-maximized")
            chrome_opts_.add_argument("disable-infobars")
            chrome_opts_.add_argument("--disable-extensions")
            chrome_opts_.add_experimental_option("detach", True)  # Prevents the browser from closing automatically
            wbd_ = webdriver.Chrome(service=service_, options=chrome_opts_)
            wbd_.get(target_url_)
            wbd_.implicitly_wait(10)
            login_mail(wbd_)
            return wbd_

        try:
            from all_imports import requests, time
            from login_mail import login_mail

            http_req_ = requests.get(target_url_)
            time.sleep(1)
            if http_req_.status_code == 200:
                start_browser()
                print(
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                    'Successfully connected!\n\n'
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        except requests.ConnectionError:
            print(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                'No server connection.\n'
                'The test is discontinued.\n\n'
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')


if __name__ == '__main__':
    openBrowser()
