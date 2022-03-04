# Gmail_E2E_sketch-test

Environment

Windows 10, Chrome, Gmail Inbox, Promotions and Primary sections


Objective of a test

Verify:

•	Login passes OK, correct credentials;

•	Interaction with Promotions and Primary tabs is possible;

•	Counting of the messages in Primary section is possible;

•	The Subject data of these messages is accessible.


Test’s implementation

On running the test from [ start_test_e2e.py ]:

•	Establish connection with https://www.gmail.com/;

•	If OK, logs into account with correct credentials;

•	As Primary tab is selected by default, clicks Promotions tab to ensure the proper UI interaction;

•	Returns to Primary section;

•	Verify presence of the mail entries;

•	Lists the senders;

•	If  Subject of a message contains text, writes it down;

•	Opens a dialog listing senders and showing total of mails;

•	Prints Subjects to console/CMD, depends of how the test was run.


QA notes

•	Unfortunately the browser keeps closing automatically while using ChromeDriverManager. Probably the driver gets garbage-collected. So I was compelled to use a machine-located driver. Please find a driver included there;

•	The driver for the test was set for Selenium 4.1.0. Please change it if you have another version on your machine. Drivers are here: https://pypi.org/project/webdriver-manager/ ;
