
import sys
import getopt
import re
import time
import calendar
import os
from itertools import chain

t0_epoch = calendar.timegm(time.gmtime())
print("t0_epoch: " + str(t0_epoch))
os.mkdir("test_results_" + str(t0_epoch))
fh_uname       = open("test_results_" + str(t0_epoch) + "/uname_testing.txt","w")
fh_firstname   = open("test_results_" + str(t0_epoch) + "/firstname_testing.txt","w")
fh_lastname    = open("test_results_" + str(t0_epoch) + "/lastname_testing.txt","w")
fh_password    = open("test_results_" + str(t0_epoch) + "/password_testing.txt","w")
fh_phonenumber = open("test_results_" + str(t0_epoch) + "/phonenumber_testing.txt","w")
fh_email       = open("test_results_" + str(t0_epoch) + "/email_testing.txt","w")

user_signup_stats = {'uname':{'count':0,'pass':False,'starttime':t0_epoch,'endtime':t0_epoch,'test_log':fh_uname},\
                     'firstname':{'count':0,'pass':False,'starttime':t0_epoch,'endtime':t0_epoch,'test_log':fh_firstname},\
                     'lastname':{'count':0,'pass':False,'starttime':t0_epoch,'endtime':t0_epoch,'test_log':fh_lastname},\
                     'password':{'count':0,'pass':False,'starttime':t0_epoch,'endtime':t0_epoch,'test_log':fh_password},\
                     'phonenumber':{'count':0,'pass':False,'starttime':t0_epoch,'endtime':t0_epoch,'test_log':fh_phonenumber},\
                     'email':{'count':0,'pass':False,'starttime':t0_epoch,'endtime':t0_epoch,'test_log':fh_email}}

class UserSignup:
    """
    user sign up class
    """

    def __init__(self,**kwargs):
        self.func_options = {'uname': self.check_uname,
                             'firstname': self.check_firstname,
                             'lastname': self.check_lastname,
                             'password': self.check_password,
                             'phonenumber': self.check_phonenumber,
                             'email' : self.check_email
                            }

    def start(self):
        print("started")

    def dump_stats(self):
        print()
        for val in user_signup_stats:
            print(str(val))
            for stat in user_signup_stats[val]:
                print("  " + str(stat) + ": " + str(user_signup_stats[val][stat]))

    def check_uname(self,uname='',expected_to_pass=True):
        if len(uname) > 2 or expected_to_pass == False:
            if user_signup_stats['uname']['count'] == 0:
                user_signup_stats['uname']['pass'] = True
            if expected_to_pass == True:
                user_signup_stats['uname']['test_log'].write("pass - the length of the user name exceeds two characters: " + str(uname) + os.linesep)
            else:
                user_signup_stats['uname']['test_log'].write("pass - the length of the user name was expected to fail: " + str(uname) + os.linesep)
        else:
            user_signup_stats['uname']['test_log'].write("fail - the length of the user name is less than three characters: " + str(uname) + os.linesep)
            user_signup_stats['uname']['pass'] = False

    def check_firstname(self,firstname='',expected_to_pass=True):
        if len(firstname):
            legal_name_ordinal_values = [ord(c) for c in " 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"]
            #[32,39,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
            not_legal_name_characters = [c for c in firstname if ord(c) not in legal_name_ordinal_values]
            if len(not_legal_name_characters):
                if expected_to_pass == True:
                    user_signup_stats['firstname']['test_log'].write("fail - illegal first name characters - only use characters: a-zA-Z<space> or an apostrophe" + str(firstname) + os.linesep)
                    user_signup_stats['firstname']['pass'] = False
                else:
                    user_signup_stats['firstname']['test_log'].write("pass - illegal first name characters failed as expected - any characters not in: a-zA-Z<space> or an apostrophe should fail" + str(firstname) + os.linesep)
                    if user_signup_stats['firstname']['count'] == 0:
                        user_signup_stats['firstname']['pass'] = True
            else:
                user_signup_stats['firstname']['test_log'].write("pass - legal first name characters" + str(firstname) + os.linesep)
                if user_signup_stats['firstname']['count'] == 0:
                    user_signup_stats['firstname']['pass'] = True
        else:
            if expected_to_pass == True:
                user_signup_stats['firstname']['test_log'].write("fail - first name must be at least one character: " + str(firstname) + os.linesep)                
                user_signup_stats['firstname']['pass'] = False
            else:
                user_signup_stats['firstname']['test_log'].write("pass - first name was less than one character and failed as expected" + os.linesep)
                if user_signup_stats['firstname']['count'] == 0:
                    user_signup_stats['firstname']['pass'] = True

    def check_lastname(self,lastname='',expected_to_pass=True):
        if len(lastname):
            legal_name_ordinal_values = [ord(c) for c in " 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"]
            #[32,39,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
            not_legal_name_characters = [c for c in lastname if ord(c) not in legal_name_ordinal_values]
            if len(not_legal_name_characters):
                if expected_to_pass == True:
                    user_signup_stats['lastname']['test_log'].write("fail - illegal last name characters - only use characters: a-zA-Z<space> or an apostrophe" + str(lastname) + os.linesep)
                    user_signup_stats['lastname']['pass'] = False
                else:
                    user_signup_stats['lastname']['test_log'].write("pass - illegal last name characters failed as expected - any characters not in: a-zA-Z<space> or an apostrophe should fail" + \
                                                                    str(lastname) + os.linesep)
                    if user_signup_stats['lastname']['count'] == 0:
                        user_signup_stats['lastname']['pass'] = True
            else:
                user_signup_stats['lastname']['test_log'].write("pass - legal last name characters" + str(lastname) + os.linesep)
                if user_signup_stats['lastname']['count'] == 0:
                    user_signup_stats['lastname']['pass'] = True
        else:
            if expected_to_pass == True:
                user_signup_stats['lastname']['test_log'].write("fail - last name must be at least one character: " + str(lastname) + os.linesep)
                user_signup_stats['lastname']['pass'] = False
            else:
                user_signup_stats['lastname']['test_log'].write("pass - last name was less than one character and failed as expected" + os.linesep)
                if user_signup_stats['lastname']['count'] == 0:
                    user_signup_stats['lastname']['pass'] = True

    def check_password(self,password='',expected_to_pass=True):
        if len(password) > 6 and len(password) < 20:
            uppercase_list = [ord(c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
            lowercase_list = [ord(c) for c in "abcdefghijklmnopqrstuvwxyz"]
            number_list    = [ord(c) for c in "0123456789"]
            legal_list     = chain(uppercase_list,lowercase_list,number_list)
            uppercase      = [c for c in password if ord(c) in uppercase_list]
            lowercase      = [c for c in password if ord(c) in lowercase_list]
            number         = [c for c in password if ord(c) in number_list]
            special        = [c for c in password if ord(c) not in legal_list]
            if len(uppercase) and len(lowercase) and len(number) and len(special):
                if user_signup_stats['password']['count'] == 0:
                    user_signup_stats['password']['pass'] = True
                    user_signup_stats['password']['test_log'].write("pass - password created successfully: " + str(password) + os.linesep)
            else:
                if expected_to_pass == True:
                    user_signup_stats['password']['pass'] = False
                    user_signup_stats['password']['test_log'].write("fail - password must contain at least 1 uppercase letter, at least 1 lowercase letter, at least 1 number, and at least one special character: " + str(password) + os.linesep)
                else:
                    if user_signup_stats['password']['count'] == 0:
                       user_signup_stats['password']['pass'] = True
                       user_signup_stats['password']['test_log'].write("pass - password failed as expected: " + str(password) + os.linesep)
        else:
            if expected_to_pass == True:
                user_signup_stats['password']['pass'] = False
                user_signup_stats['password']['test_log'].write("fail - password has to be greater than six characters and less than tewnty characters: " + str(password) + os.linesep)
            else:
                if user_signup_stats['password']['count'] == 0:
                    user_signup_stats['password']['pass'] = True
                    user_signup_stats['password']['test_log'].write("pass - password length failed as expected: " + str(password) + os.linesep)

    def check_phonenumber(self,phonenumber='',expected_to_pass=True):
        if len(phonenumber) == 12:
            legal_phone_number = re.search("^\d\d\d-\d\d\d-\d\d\d\d$",phonenumber)
            if legal_phone_number:
                if user_signup_stats['phonenumber']['count'] == 0:
                    user_signup_stats['phonenumber']['pass'] = True
                user_signup_stats['phonenumber']['test_log'].write("pass - phonenumber is valid: " + str(phonenumber) + os.linesep)
            else:
                if expected_to_pass == True:
                    user_signup_stats['phonenumber']['pass'] = False
                    user_signup_stats['phonenumber']['test_log'].write("fail - phonenumber is not valid should equal 12 characters: xxx-xxx-xxxx: " + str(phonenumber) + os.linesep)
                else:
                    if user_signup_stats['phonenumber']['count'] == 0:
                        user_signup_stats['phonenumber']['pass'] = True
                    user_signup_stats['phonenumber']['test_log'].write("pass - invalid phonenumber failed as expected: " + str(phonenumber) + os.linesep)
        else:
            if expected_to_pass == True:
                user_signup_stats['phonenumber']['pass'] = False
                user_signup_stats['phonenumber']['test_log'].write("fail - phonenumber should equal 12 characters: xxx-xxx-xxxx " + str(phonenumber) + os.linesep)
            else:
                if user_signup_stats['phonenumber']['count'] == 0:
                    user_signup_stats['phonenumber']['pass'] = True
                user_signup_stats['phonenumber']['test_log'].write("pass - phonenumber length was not twelve as expected: " + str(phonenumber) + os.linesep)

    def check_email(self,email='',expected_to_pass=True):
        if len(email):
            email_part = re.split('@',email)
            if len(email_part) == 2:
                localpart = email_part[0]
                domain    = email_part[1]
                if len(localpart) > 64:
                    if expected_to_pass == True:
                        user_signup_stats['email']['pass'] = False
                        user_signup_stats['email']['test_log'].write("fail - length of email local part exceeds 64 characters - actual (" + str(len(localpart)) + ") :" + str(email) + os.linesep)
                    else:
                        if user_signup_stats['email']['count'] == 0:
                            user_signup_stats['email']['pass'] = True
                        user_signup_stats['email']['test_log'].write("pass - length of email local part exceeds 64 characters and failed as expected - actual (" + str(len(localpart)) + ") :" + str(email) + os.linesep)
                elif len(domain) > 255:
                    if expected_to_pass == True:
                        user_signup_stats['email']['pass'] = False
                        user_signup_stats['email']['test_log'].write("fail - length of email domain exceeds 255 characters - actual (" + str(len(domain)) + ") :" + str(email) + os.linesep)
                    else:
                        if user_signup_stats['email']['count'] == 0:
                            user_signup_stats['email']['pass'] = True
                        user_signup_stats['email']['test_log'].write("pass - length of email domain exceeds 255 characters and failed as expected - actual (" + str(len(domain)) + ") :" + str(email) + os.linesep)
                else:
                    if re.search('^\(.*\)',localpart) is not None:
                        localpart = re.sub('^\(.*\)','',localpart)
                    if re.search('\(.*\)$',localpart) is not None:
                        localpart = re.sub('\(.*\)$','',localpart)
                    if re.search('^\(.*\)',domain) is not None:
                        domain = re.sub('^\(.*\)','',domain)
                    if re.search('\(.*\)$',domain) is not None:
                        domain = re.sub('\(.*\)$','',domain)

                    legal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789."
                    legal_chars = [ord(c) for c in legal]
                    special_chars = [ord(c) for c in "!#$%&'*+-/=?^_`{|}~"]
                    restricted_chars = [ord(c) for c in ' "(),:;<>@[\]']
                    not_legal_email_chars = [c for c in localpart if ord(c) not in chain(legal_chars,special_chars)]
                    #print("not_legal_email_chars: " + str(not_legal_email_chars) + " - localpart " + str(localpart) + " - email " + str(email))

                    if len(not_legal_email_chars):
                        if not_legal_email_chars.count('"') > 1:
                            between_quotes = re.search('^(.*?)"(.*)"(.*)$',localpart)
                            #print("0 ->" + between_quotes.group(0))
                            #print("1 ->" + between_quotes.group(1))
                            #print("2 ->" + between_quotes.group(2))
                            #print("3 ->" + between_quotes.group(3))

                            not_legal_outside_of_quotes = [c for c in between_quotes.group(1)+between_quotes.group(3) if ord(c) not in chain(legal_chars,special_chars)]
                            #print("not_legal_outside_of_quotes: " + str(not_legal_outside_of_quotes) + " - localpart " + str(localpart) + " - email " + str(email))
                            if len(not_legal_outside_of_quotes):
                                if expected_to_pass == True:
                                    user_signup_stats['email']['pass'] = False
                                    user_signup_stats['email']['test_log'].write("fail - invalid characters " + str(not_legal_outside_of_quotes) + " before/after quotes in email local part: " + str(email) + os.linesep)
                                else:
                                    if user_signup_stats['email']['count'] == 0:
                                        user_signup_stats['email']['pass'] = True
                                    user_signup_stats['email']['test_log'].write("pass - invalid characters " + str(not_legal_outside_of_quotes) + " before/after quotes in email local part failed as expected: " + str(email) + os.linesep)
                            else:
                                between_quotes_chars = between_quotes.group(2)
                                #print("between quotes: " + str(between_quotes_chars))
                                not_legal_between_quotes = [c for c in between_quotes_chars if ord(c) not in chain(legal_chars,special_chars,restricted_chars)]
                                #print("not_legal_email_chars between quotes " + str(not_legal_between_quotes))
                                if len(not_legal_between_quotes):
                                    if expected_to_pass == True:
                                        user_signup_stats['email']['pass'] = False
                                        user_signup_stats['email']['test_log'].write("fail - invalid characters between quotes in email local part: " + str(not_legal_between_quotes) + " - email " + str(email) + os.linesep)
                                    else:
                                        if user_signup_stats['email']['count'] == 0:
                                            user_signup_stats['email']['pass'] = True
                                        user_signup_stats['email']['test_log'].write("pass - invalid characters between quotes in email local part failed as expected: " + str(not_legal_between_quotes) + " - email " + str(email) + os.linesep)
                                else:
                                    between_quotes_chars = between_quotes.group(2)
                                    not_legal_between_quotes = [c for c in between_quotes_chars if ord(c) not in chain(legal_chars,special_chars,restricted_chars)]
                                    if len(not_legal_between_quotes):
                                        if expected_to_pass == True:
                                            user_signup_stats['email']['pass'] = False
                                            user_signup_stats['email']['test_log'].write("fail - invalid characters between double quotes in email local part " + str(localpart) + " - invalid characters: " + str(not_legal_between_quotes) + " - email " + str(email) + os.linesep)
                                        else:
                                            if user_signup_stats['email']['count'] == 0:
                                                user_signup_stats['email']['pass'] = True
                                            user_signup_stats['email']['test_log'].write("pass - invalid characters between double quotes in email local part and failed as expected " + str(localpart) + " - invalid characters: " + str(not_legal_between_quotes) + " - email " + str(email) + os.linesep)
                                    else:
                                        if re.search('"',between_quotes_chars) is not None and re.search('\\\\"',between_quotes_chars) is None:
                                            if expected_to_pass == True:
                                                user_signup_stats['email']['pass'] = False
                                                user_signup_stats['email']['test_log'].write("fail - double quote within a pair of double quotes must be escaped with a backslash in email local part: " + str(email) + os.linesep)
                                            else:
                                                if user_signup_stats['email']['count'] == 0:
                                                    user_signup_stats['email']['pass'] = True
                                                user_signup_stats['email']['test_log'].write("pass - double quote within a pair of double quotes must be escaped with a backslash in email local part and failed as expected: " + str(email) + os.linesep)
                                        if re.search(' ',between_quotes_chars) is not None and re.search('\\\\ ',between_quotes_chars) is None:
                                            if expected_to_pass == True:
                                                user_signup_stats['email']['pass'] = False
                                                user_signup_stats['email']['test_log'].write("fail - a space within a pair of double quotes must be escaped with a backslash in email local part: " + str(email) + os.linesep)
                                            else:
                                                if user_signup_stats['email']['count'] == 0:
                                                    user_signup_stats['email']['pass'] = True
                                                user_signup_stats['email']['test_log'].write("pass - a space within a pair of double quotes must be escaped with a backslash in email local part and failed as expected: " + str(email) + os.linesep)
                        else:
                            if expected_to_pass == True:
                                user_signup_stats['email']['pass'] = False
                                user_signup_stats['email']['test_log'].write("fail - invalid characters in email local part - " + str(not_legal_email_chars) + " - " + str(email) + os.linesep)
                            else:
                                if user_signup_stats['email']['count'] == 0:
                                    user_signup_stats['email']['pass'] = True
                                user_signup_stats['email']['test_log'].write("pass - invalid characters in email local part and failed as expected - " + str(not_legal_email_chars) + " - " + str(email) + os.linesep)
                    else:
                        match1 = re.search('^\.',localpart)
                        match2 = re.search('\.$',localpart)
                        match3 = re.search('\.\.',localpart)
                        if match1 is not None or match2 is not None or match3 is not None:
                            if expected_to_pass == True:
                                user_signup_stats['email']['pass'] = False
                                user_signup_stats['email']['test_log'].write("fail - illegal characters in the email local part - no leading '.', no trailing '.', and no double '..' outside of double quotes: " + str(email) + os.linesep)
                            else:
                                if user_signup_stats['email']['count'] == 0:
                                    user_signup_stats['email']['pass'] = True
                                user_signup_stats['email']['test_log'].write("pass - illegal characters in the email local part - no leading '.', no trailing '.', and no double '..' outside of double quotes and failed as expected: " + str(email) + os.linesep)
                        else:
                            if user_signup_stats['email']['count'] == 0:
                                user_signup_stats['email']['pass'] = True
                            user_signup_stats['email']['test_log'].write("pass - email local part does not contain any illegal dot '.' characters: " + str(email) + os.linesep)

                        match1 = re.search('^\.',domain)
                        match2 = re.search('\.$',domain)
                        match3 = re.search('\.\.',domain)
                        if match1 is not None or match2 is not None or match3 is not None:
                            if expected_to_pass == True:
                                user_signup_stats['email']['pass'] = False
                                user_signup_stats['email']['test_log'].write("fail - illegal characters in the email domain - no leading '.', no trailing '.', and no double '..' outside of double quotes: " + str(email) + os.linesep)
                            else:
                                if user_signup_stats['email']['count'] == 0:
                                    user_signup_stats['email']['pass'] = True
                                user_signup_stats['email']['test_log'].write("pass - illegal characters in the email domain - no leading '.', no trailing '.', and no double '..' outside of double quotes and failed as expected: " + str(email) + os.linesep)
                        else:
                            if user_signup_stats['email']['count'] == 0:
                                user_signup_stats['email']['pass'] = True
                            user_signup_stats['email']['test_log'].write("pass - email domain does not contain any illegal dot '.' characters: " + str(email) + os.linesep)

                    # verify email domain section                                                                                                                                                                                 
                    legal_chars = [ord(c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-."]
                    not_legal_email_domain_chars = [c for c in domain if ord(c) not in legal_chars]
                    #print("not_legal_email_domain_chars: " + str(not_legal_email_domain_chars) + " - domain " + str(domain) + " - email " + str(email))
                    if len(not_legal_email_domain_chars):
                        if expected_to_pass == True:
                            user_signup_stats['email']['pass'] = False
                            user_signup_stats['email']['test_log'].write("fail - illegal characters in the email domain " + str(not_legal_email_domain_chars) + ": " + str(email) + os.linesep)
                        else:
                            if user_signup_stats['email']['count'] == 0:
                                user_signup_stats['email']['pass'] = True
                            user_signup_stats['email']['test_log'].write("pass - illegal characters in the email domain and failed as expected " + str(not_legal_email_domain_chars) + ": " + str(email) + os.linesep)
                    elif re.search('^-|-$',domain) is not None:
                        if expected_to_pass== True:
                            user_signup_stats['email']['pass'] = False
                            user_signup_stats['email']['test_log'].write("fail - the '-' character cannot be the 1st or last character in the email domain: " + str(email) + os.linesep)
                        else:
                            if user_signup_stats['email']['count'] == 0:
                                user_signup_stats['email']['pass'] = True
                            user_signup_stats['email']['test_log'].write("pass - the '-' character cannot be the 1st or last character in the email domain and failed as expected: " + str(email) + os.linesep)
                    elif re.search('\.\.',domain) is not None:
                        if expected_to_pass== True:
                            user_signup_stats['email']['pass'] = False
                            user_signup_stats['email']['test_log'].write("fail - double '.' character is illegal in the email domain: " + str(email) + os.linesep)
                        else:
                            if user_signup_stats['email']['count'] == 0:
                                user_signup_stats['email']['pass'] = True
                            ser_signup_stats['email']['test_log'].write("pass - double '.' character is illegal in the email domain and failed as expected: " + str(email) + os.linesep)
                    else:
                        if user_signup_stats['email']['count'] == 0:
                            user_signup_stats['email']['pass'] = True
                        user_signup_stats['email']['test_log'].write("pass - email domain does not contain any illegal characters: " + str(email) + os.linesep)
            else:
                if expected_to_pass== True:
                    user_signup_stats['email']['pass'] = False
                    user_signup_stats['email']['test_log'].write("fail - email must contain one '@': " + str(email) + os.linesep)
                else:
                    if user_signup_stats['email']['count'] == 0:
                        user_signup_stats['email']['pass'] = True
                    user_signup_stats['email']['test_log'].write("pass - email missing one '@' and failed as expected: " + str(email) + os.linesep)
        else:
            if expected_to_pass == True:
                user_signup_stats['email']['pass'] = False
                user_signup_stats['email']['test_log'].write("fail - email is empty - it should be at least 3 characters: " + str(email) + os.linesep)
            else:
                if user_signup_stats['email']['count'] == 0:
                    user_signup_stats['email']['pass'] = True
                user_signup_stats['email']['test_log'].write("pass - empty email failed as expected: " + str(email) + os.linesep)

    def check_input(self,expected_to_pass=True,**kwargs):
        tnow_epoch = calendar.timegm(time.gmtime())
        for text_box in kwargs:
            try:
                #print("text_box: " + str(text_box) + " -> " + str(kwargs[text_box]))
                self.func_options[str(text_box)](kwargs[text_box],expected_to_pass)
                user_signup_stats[text_box]['endtime'] = tnow_epoch
                user_signup_stats[text_box]['count'] += 1
                #print(str(text_box) + " count " + user_signup_stats[text_box]['count'])
            except:
                print("unknown text_box value (" + str(text_box) + ") - kwargs " + str(kwargs[text_box]))
                #sys.exit()
