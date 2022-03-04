# -*- coding: UTF-8 -*-

enter_features: list = [
    ["//input[@type='email']", "//input[@type='password']"], # Inputs
    ["VfPpkd-LgbsSe", "VfPpkd-LgbsSe"], # Buttons
    ["rubiserg.aidock.e2e.test@gmail.com", "rubisergAutomation222"] # Creds
    ]

def login_mail(wbd_):
    from all_imports import WebDriverWait, TimeoutException, time, By,EC, \
                            ElementNotInteractableException, NoSuchElementException
    from check_mail import check_mail

    # Verifies presence of ui elements, enters email, clicks
    try:
        for ix_ in range(0, enter_features.__len__() - 1):
            if ix_ > 0:
                time.sleep(10) # A timeout necessary to start search for the elements on
                                 # the second login page.
            WebDriverWait(wbd_, 100, poll_frequency=5).until(EC.presence_of_element_located((By.XPATH, enter_features[0][ix_])))
            WebDriverWait(wbd_, 100, poll_frequency=5).until(EC.element_to_be_clickable((By.CLASS_NAME, enter_features[1][ix_])))
            wbd_.find_element(By.XPATH, enter_features[0][ix_]).send_keys(enter_features[2][ix_])
            the_button = wbd_.find_element(By.CLASS_NAME, enter_features[1][ix_])
            WebDriverWait(wbd_, 100, poll_frequency=5)
            the_button.click()
        # time.sleep(3)
        WebDriverWait(wbd_, 100, poll_frequency=5)
        check_mail(wbd_)
    except (ElementNotInteractableException, NoSuchElementException, TimeoutException):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                'Login failed.\n'
                'The test is discontinued.\n\n'
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        wbd_.close()
        wbd_.quit()
