
testing user signup

-----

two files needed to test
  - test_user_signup.py
  - user_signup.py

how to run
> python3.6 test_user_signup.py

-----

what gets displayed to the console

stat summary before testing is broken down by each input type
  - count is 0 and will be incremented each test (uname, firstname, lastname, password, phonenumber, and email)
  - pass initially defaults to False for all input types until the 1st test for that input type
    is tested - any unexpected failure will set pass to False
  - starttime is the epoch time when the test starts - each test type should set this again before
    the 1st test occurrence
  - endtime is set after each test type
  - a test_log is kept for each test type and is written to a newly created directory "test_results_<epoch time>/<test type>_testing.txt"

t0_epoch: 1537206439

uname
  count: 0
  pass: False
  starttime: 1537206439
  endtime: 1537206439
  test_log: <_io.TextIOWrapper name='test_results_1537206439/uname_testing.txt' mode='w' encoding='UTF-8'>
firstname
  count: 0
  pass: False
  starttime: 1537206439
  endtime: 1537206439
  test_log: <_io.TextIOWrapper name='test_results_1537206439/firstname_testing.txt' mode='w' encoding='UTF-8'>
lastname
  count: 0
  pass: False
  starttime: 1537206439
  endtime: 1537206439
  test_log: <_io.TextIOWrapper name='test_results_1537206439/lastname_testing.txt' mode='w' encoding='UTF-8'>
password
  count: 0
  pass: False
  starttime: 1537206439
  endtime: 1537206439
  test_log: <_io.TextIOWrapper name='test_results_1537206439/password_testing.txt' mode='w' encoding='UTF-8'>
phonenumber
  count: 0
  pass: False
  starttime: 1537206439
  endtime: 1537206439
  test_log: <_io.TextIOWrapper name='test_results_1537206439/phonenumber_testing.txt' mode='w' encoding='UTF-8'>
email
  count: 0
  pass: False
  starttime: 1537206439
  endtime: 1537206439
  test_log: <_io.TextIOWrapper name='test_results_1537206439/email_testing.txt' mode='w' encoding='UTF-8'>

at the end of the testing there is another dump of the test summary stats

uname
  count: 165893
  pass: True
  starttime: 1537206439
  endtime: 1537206440
  test_log: <_io.TextIOWrapper name='test_results_1537206439/uname_testing.txt' mode='w' encoding='UTF-8'>
firstname
  count: 55291
  pass: True
  starttime: 1537206439
  endtime: 1537206441
  test_log: <_io.TextIOWrapper name='test_results_1537206439/firstname_testing.txt' mode='w' encoding='UTF-8'>
lastname
  count: 55291
  pass: True
  starttime: 1537206439
  endtime: 1537206443
  test_log: <_io.TextIOWrapper name='test_results_1537206439/lastname_testing.txt' mode='w' encoding='UTF-8'>
password
  count: 221024
  pass: True
  starttime: 1537206439
  endtime: 1537206449
  test_log: <_io.TextIOWrapper name='test_results_1537206439/password_testing.txt' mode='w' encoding='UTF-8'>
phonenumber
  count: 9
  pass: True
  starttime: 1537206439
  endtime: 1537206449
  test_log: <_io.TextIOWrapper name='test_results_1537206439/phonenumber_testing.txt' mode='w' encoding='UTF-8'>
email
  count: 118
  pass: True
  starttime: 1537206439
  endtime: 1537206449
  test_log: <_io.TextIOWrapper name='test_results_1537206439/email_testing.txt' mode='w' encoding='UTF-8'>

real	    0m10.109s
user	    0m9.981s
sys	    0m0.057s

-----

script: test_user_signup.py uses class UserSignup

the UserSignup object uses method "check_input" to test the various inputs

args to the "check_input" method:
  - input type: uname, first_name, lastname, password, phonenumber, and email
  - the second arg is optional and controls the "expected_to_pass" arg that is  True or False (defaults to True if not used)
    when set to True then any illegal inputs will set the "pass" value to False
    when set to False then any expected illegal inputs will pass with an expected to fail message

-----

typical usage (see script: test_user_signup.py for specific testcases separated by input type):

test_signup = UserSignup()

test_signup.check_input(uname='',expected_to_pass=False)
test_signup.check_input(uname='xyz')

test_signup.check_input(firstname='',expected_to_pass=False)

for ord_val in [ord(c) for c in " 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"]:
    test_signup.check_input(firstname='abc ' + chr(ord_val) + ' xyz')

test_signup.check_input(lastname='',expected_to_pass=False)

for ord_val in [ord(c) for c in " 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"]:
    test_signup.check_input(lastname='abc ' + chr(ord_val) + ' xyz')

test_signup.check_input(password='',expected_to_pass=False)
test_signup.check_input(password='123456',expected_to_pass=False)
test_signup.check_input(password='1234567890123456789012',expected_to_pass=False)

for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,55296)):
    test_signup.check_input(password='aBcD01' + chr(ord_val))

test_signup.check_input(phonenumber='',expected_to_pass=False)
test_signup.check_input(phonenumber='12345678901',expected_to_pass=False)
test_signup.check_input(phonenumber='123-abc-4567',expected_to_pass=False)
test_signup.check_input(phonenumber='123-456-7890')

test_signup.check_input(email='',expected_to_pass=False)
test_signup.check_input(email='xyz',expected_to_pass=False)
test_signup.check_input(email='xyz@@abc.com',expected_to_pass=False)
test_signup.check_input(email='abc..def@xyz.com',expected_to_pass=False)
test_signup.check_input(email='(comment)abc@xyz.com')
test_signup.check_input(email='abc@(comment)xyz.com')
test_signup.check_input(email='abc@x*z.com',expected_to_pass=False)
test_signup.check_input(email='"abc\\".def"@xyz.com')

for special_char in "!#$%&'*+-/=?^_`{|}~":
    test_signup.check_input(email=str(special_char) + '@xyz.com')
