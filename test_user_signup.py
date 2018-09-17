
import sys
import getopt
import re
import time
from itertools import chain
from user_signup import UserSignup

test_signup = UserSignup()

# initial stats should be set to zero with a default of pass: False
test_signup.dump_stats()

if True:
    test_signup.check_input(uname='',expected_to_pass=False)
    test_signup.check_input(uname='xyz')
    #test_signup.check_input(uname='ab',expected_to_pass=True)
    test_signup.check_input(uname='ab',expected_to_pass=False)

    #test_signup.dump_stats()

if True:
    for ord_val in range(0,55296):
    #for ord_val in range(0,2):
        try:
            test_signup.check_input(uname=chr(ord_val),expected_to_pass=False)
        except UnicodeEncodeError as error:
            print("{} - {}".format(ord_val,error))
            #sys.exit()
 
    for ord_val in range(0,55296):
    #for ord_val in range(0,2):
        try:
            test_signup.check_input(uname=chr(ord_val) + chr(ord_val),expected_to_pass=False)
        except UnicodeEncodeError as error:
            print("{} - {}".format(ord_val,error))
            #sys.exit()

    #for ord_val in range(0,55296):
    for ord_val in range(0,2):
        try:
            test_signup.check_input(uname="ab" + chr(ord_val))
        except UnicodeEncodeError as error:
            print("{} - {}".format(ord_val,error))
            #sys.exit()
    for ord_val in range(0,55296):
    #for ord_val in range(0,2):
        try:
            test_signup.check_input(uname='a' + chr(ord_val) + 'b')
        except UnicodeEncodeError as error:
            print("{} - {}".format(ord_val,error))
            #sys.exit()

###

if True:
    #test_signup.check_input(firstname='',expected_to_pass=True)
    test_signup.check_input(firstname='',expected_to_pass=False)

if True:
    #[32,39,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
    #for ord_val in chain([32,39],range(65,91),range(97,123)):
    for ord_val in [ord(c) for c in " 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"]:
        try:
            test_signup.check_input(firstname='abc ' + chr(ord_val) + ' xyz')
        except:
            print("unexpected error when creating valid name string with ordinal character value: " + str(ord))

if True:
    # UTF-8 is a variable width character encoding capable of encoding all 1,112,064[1] valid code points in Unicode using one to four 8-bit bytes
    # 55296 - 'utf-8' codec can't encode character '\ud800' in position 45: surrogates not allowed
    # for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,1112065)):

    for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,55296)):
    #for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,1000)):
        try:
            test_signup.check_input(firstname='abc ' + chr(ord_val) + ' xyz',expected_to_pass=False)
        except UnicodeEncodeError as error:
            print("{} - {}".format(ord_val,error))
            #sys.exit()

###

if True:
    #test_signup.check_input(lastname='',expected_to_pass=True)
    test_signup.check_input(lastname='',expected_to_pass=False)

if True:
    #[32,39,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
    #for ord_val in chain([32,39],range(65,91),range(97,123)):
    for ord_val in [ord(c) for c in " 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"]:
        try:
            test_signup.check_input(lastname='abc ' + chr(ord_val) + ' xyz')
        except:
            print("unexpected error when creating valid name string with ordinal character value: " + str(ord))

if True:
    # UTF-8 is a variable width character encoding capable of encoding all 1,112,064[1] valid code points in Unicode using one to four 8-bit bytes
    # 55296 - 'utf-8' codec can't encode character '\ud800' in position 45: surrogates not allowed
    # for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,1112065)):

    for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,55296)):
    #for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,1000)):
        try:
            test_signup.check_input(lastname='abc ' + chr(ord_val) + ' xyz',expected_to_pass=False)
        except UnicodeEncodeError as error:
            print("{} - {}".format(ord_val,error))
            #sys.exit()

###

if True:
    test_signup.check_input(password='',expected_to_pass=False)
    test_signup.check_input(password='123456',expected_to_pass=False)
    test_signup.check_input(password='1234567890123456789012',expected_to_pass=False)
    #test_signup.check_input(password='',expected_to_pass=True)
    #test_signup.check_input(password='123456',expected_to_pass=True)
    #test_signup.check_input(password='1234567890123456789012',expected_to_pass=True)

if True:
    test_signup.check_input(password='1234567',expected_to_pass=False)
    test_signup.check_input(password='123456a',expected_to_pass=False)
    test_signup.check_input(password='123456B',expected_to_pass=False)
    test_signup.check_input(password='abcdef0',expected_to_pass=False)
    test_signup.check_input(password='abcdef0*',expected_to_pass=False)

if True:
    for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,55296)):
        try:
            test_signup.check_input(password='aBcD01' + chr(ord_val))
        except UnicodeEncodeError as error:
            print("{} - {}".format(ord_val,error))
            #sys.exit()
    for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,55296)):
        try:
            test_signup.check_input(password=' aBcD0' + chr(ord_val))
        except UnicodeEncodeError as error:
            print("{} - {}".format(ord_val,error))
            #sys.exit()
    for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,55296)):
        try:
            test_signup.check_input(password='aBcD0' + chr(ord_val) + ' ')
        except UnicodeEncodeError as error:
            print("{} - {}".format(ord_val,error))
            #sys.exit()
    for ord_val in chain(range(0,32),range(33,39),range(40,65),range(123,55296)):
        try:
            test_signup.check_input(password='aBc' + chr(ord_val) + 'Cd0')
        except UnicodeEncodeError as error:
            print("{} - {}".format(ord_val,error))
            #sys.exit()

if True:
    for ord_val in [ord(c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]:
        try:
            test_signup.check_input(password='0123a*' + chr(ord_val))
        except:
            print("unexpected exception when checking legal password")
            #sys.exit()
    for ord_val in [ord(c) for c in "abcdefghijklmnopqrstuvwxyz"]:
        try:
            test_signup.check_input(password='0123A*' + chr(ord_val))
        except:
            print("unexpected exception when checking legal password")
            #sys.exit()
    for ord_val in [ord(c) for c in "0123456789"]:
        try:
            test_signup.check_input(password='aAbBc*' + chr(ord_val))
        except:
            print("unexpected exception when checking legal password")
            #sys.exit()
    for ord_val in [ord(c) for c in "0123456789"]:
        try:
            test_signup.check_input(password=' AbB*' + chr(ord_val) + ' ')
        except:
            print("unexpected exception when checking legal password")
            #sys.exit()

###

if True:
    test_signup.check_input(phonenumber='',expected_to_pass=False)
    test_signup.check_input(phonenumber='12345678901',expected_to_pass=False)
    test_signup.check_input(phonenumber='1234567890123',expected_to_pass=False)

if True:
    test_signup.check_input(phonenumber='123-abc-4567',expected_to_pass=False)
    test_signup.check_input(phonenumber=' 12-abc-4567',expected_to_pass=False)
    test_signup.check_input(phonenumber='123-abc- 567',expected_to_pass=False)
    test_signup.check_input(phonenumber='123-abc-456 ',expected_to_pass=False)
    test_signup.check_input(phonenumber='123-7 9-4567',expected_to_pass=False)

if True:
    test_signup.check_input(phonenumber='123-456-7890')

###

if True:
    test_signup.check_input(email='',expected_to_pass=False)
    test_signup.check_input(email='123456789x123456789x123456789x123456789x123456789x123456789x1234@xyz.com',expected_to_pass=False)
    test_signup.check_input(email='123456789x123456789x123456789x123456789x123456789x123456789x12345@xyz.com',expected_to_pass=False)
    test_signup.check_input(email='123456789x123456789x123456789x123456789x123456789x123456789x1234@123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789\
x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x1.com',expected_to_pass=False)
    test_signup.check_input(email='123456789x123456789x123456789x123456789x123456789x123456789x1234@123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789\
x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x123456789x12.com',expected_to_pass=False)
    test_signup.check_input(email='xyz',expected_to_pass=False)
    test_signup.check_input(email='xyz@@abc.com',expected_to_pass=False)
    test_signup.check_input(email='xyz@def@abc.com',expected_to_pass=False)

if True:
    test_signup.check_input(email='abc..def@xyz.com',expected_to_pass=False)
    test_signup.check_input(email='abc.def@xyz..com',expected_to_pass=False) #
    test_signup.check_input(email='abc.def.@xyz.com',expected_to_pass=False)
    test_signup.check_input(email='abc.def@.xyz.com',expected_to_pass=False)
    test_signup.check_input(email='abc.def@xyz.com.',expected_to_pass=False)

if True:
    test_signup.check_input(email='(comment)abc@xyz.com')
    test_signup.check_input(email='abc(comment)@xyz.com')
    test_signup.check_input(email='abc(comment)def@xyz.com',expected_to_pass=False)
    test_signup.check_input(email='abc"(comment)"def@xyz.com')
    test_signup.check_input(email='abc@(comment)xyz.com')
    test_signup.check_input(email='abc@xyz.com(comment)')
    test_signup.check_input(email='abc@xyz(comment).com',expected_to_pass=False)

if True:
    test_signup.check_input(email='abc@(comment)xyz.com')
    test_signup.check_input(email='abc@xyz(comment).com',expected_to_pass=False)
    test_signup.check_input(email='abc@xyz.com(comment)')
    test_signup.check_input(email='abc@x*z.com',expected_to_pass=False)
    test_signup.check_input(email='abc@tuv-xyz.com')
    test_signup.check_input(email='abc@tuv_xyz.com',expected_to_pass=False)
    test_signup.check_input(email='abc@xyz.com-',expected_to_pass=False)
    test_signup.check_input(email='abc@-xyz.com',expected_to_pass=False)
    test_signup.check_input(email='abc@1-2-3-x-y-z.com')
    test_signup.check_input(email='a1b2c3@xyz890..com',expected_to_pass=False)
    test_signup.check_input(email='a1b2c3@xyz.890.com')
    test_signup.check_input(email='a1b2c3@xyz890. .com',expected_to_pass=False)

if True:
    test_signup.check_input(email='abc.def(@xyz.com',expected_to_pass=False)
    test_signup.check_input(email='"abc.def"@xyz.com')
    test_signup.check_input(email='"abc".def"@xyz.com',expected_to_pass=False)
    test_signup.check_input(email='"abc\\".def"@xyz.com')
    test_signup.check_input(email='"abc\\.def"@xyz.com')
    test_signup.check_input(email='"abc .def"@xyz.com',expected_to_pass=False)
    test_signup.check_input(email='"abc\\ .def"@xyz.com')
    test_signup.check_input(email='mno"abc.def"tuv@xyz.com',expected_to_pass=False)

if True:
    test_signup.check_input(email="!#$%&'*+-/=?^_`{|}~@xyz.com")
    for special_char in "!#$%&'*+-/=?^_`{|}~":
        test_signup.check_input(email=str(special_char) + '@xyz.com')
    for special_char in "!#$%&'*+-/=?^_`{|}~":
        test_signup.check_input(email='abc.def' + str(special_char) + '@xyz.com')
    for special_char in "!#$%&'*+-/=?^_`{|}~":
        test_signup.check_input(email='abc' + str(special_char) + 'def@xyz.com')
    for special_char in "!#$%&'*+-/=?^_`{|}~":
        test_signup.check_input(email=str(special_char) + 'abc.def@xyz.com')

if True:
    test_signup.check_input(email='"abc[def"@ghi.com')
    test_signup.check_input(email='no!"abc.def"tuv@xyz.com')
    test_signup.check_input(email='no"abc.def"!tuv@xyz.com')

###

test_signup.dump_stats()
