locators_: list = [":1v", ":1w"]
senders_: list = []
try:
    import Tkinter
except ImportError:
    import tkinter


def check_mail(wbd_):
    from all_imports import WebDriverWait, By, EC, garbg_coll_, time
    import report_box
    from report_box import dia_box_
    # Verifies presence of ui elements, selects Primary tab
    try:
        WebDriverWait(wbd_, 500, poll_frequency=5).until(EC.presence_of_element_located((By.ID, locators_[0])))  # =>
        # Promotions tab. Clicking to ensure the test runs as expected.
        WebDriverWait(wbd_, 500, poll_frequency=5).until(EC.presence_of_element_located((By.ID, locators_[1])))
        wbd_.find_element(By.ID, ':1v').click() # Clicks Promotions tab.
        if_selected_el = wbd_.find_element(By.ID, locators_[0])
        if not if_selected_el.is_selected():# Clicks Primary tab in case it isn't already clicked.
            primary_tab = wbd_.find_element(By.ID, locators_[1])
            WebDriverWait(wbd_, 500, poll_frequency=5)
            primary_tab.click() # Clicks Primary tab.
        # Verify presence of the mail entries.
        WebDriverWait(wbd_, 500, poll_frequency=5).until(EC.presence_of_element_located((By.CLASS_NAME, "afn")))
        total_mails: list = wbd_.find_elements(By.CLASS_NAME, "afn")
        # Lists the senders.
        sender_nm: list = wbd_.find_elements(By.XPATH, "//span[contains(@translate,'no')]")
        WebDriverWait(wbd_, 500, poll_frequency=5)
        # If a msg headers contain a text, copies the headers to the list.
        for elem in sender_nm:
            if not elem.text == '':
                senders_.append(elem.text)
        # Subjects reader:
        # WebDriverWait(wbd_, 500, poll_frequency=5).until(EC.presence_of_element_located((By.CLASS_NAME, "bog")))
        subjects: list = wbd_.find_elements(By.CLASS_NAME, "bog")
        subjects_text: list = []
        for sbj in subjects:
            if not sbj.text == '':
                subjects_text.append(sbj.text)
            else:
                print("Subject is empty")

        print("::::::::::::::::::::::::::: Subjects list :::::::::::::::::::::::::::")
        for idx2_, log_ in enumerate(subjects_text):
            print(str(idx2_) + " > " + str(log_) )
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

        # Forms a report.
        report_: str = f'You have mails from {str(senders_.__len__())} senders: { ", ".join(senders_)} \nin total of' \
                       f' {str(total_mails.__len__())} messages.'
        print(report_)
        time.sleep(2)
        report_box.msg_root_ = tkinter.Tk()
        report_box.msg_wn_ = tkinter.Toplevel(report_box.msg_root_)
        dia_box_(report_)
    except Exception as exp:
        print(exp)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
                'Mail selection failed.\n'
                'The test is discontinued.\n\n'
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        wbd_.close()
        wbd_.quit()

    garbg_coll_.enable()
    time.sleep(10)
    wbd_.close()
    wbd_.quit()
