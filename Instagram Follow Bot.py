from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv()
import datetime
hashtag_list = ['nust', 'uet','nustian','pieas','eme','cae','nustuniversity', 'nustgram','pieas']

commentsList = ['Wow!!','Amazing','Intense','Awesome','I love NUST!!','lvl']

total_posts = 100
comment_percentage = 100

print('===>Script started!')

uname = 'xyz'
pwd = 'xyz'

print('===>Opening Browser')
webdriver = webdriver.Chrome(r'C:\Users\x\Desktop\Python\chromedriver.exe')
webdriver.implicitly_wait(15) #will wait until the element appears: for all the elements we find below in the file
sleep(1)

print('===>Opening Instagram')
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

print('===>Entering login details')
username = webdriver.find_element_by_name('username')
username.send_keys(uname) 
sleep(1)

password = webdriver.find_element_by_name('password')
password.send_keys(pwd) 
sleep(1)

button_login = webdriver.find_element_by_xpath("//div[text()='Log In']")
button_login.click()
sleep(randint(2,4))

try:
    print("===>Bypassing, saving info screen, if present")
    notnow = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    notnow.click() 
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print (message)
    pass

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    print('===>On hashtag: ', hashtag)
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(randint(2,4))
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    print("===>Clicking first post of the hashtag",hashtag)
    first_thumbnail.click()
    sleep(randint(1,2))
    try:
        for x in range(1,total_posts+1):
            print('Hashtag: ', hashtag, 'Post: ', x)

            # If we already like, then do nothing with the post, go to next post
            alreadyLike = webdriver.find_elements_by_xpath( "//section/span/button/div/span[*[local-name()='svg']/@aria-label='Like']")
            if len(alreadyLike) == 1:
                print('===>Following the user if we have follow button')
                button_follow = webdriver.find_element_by_xpath("//button[text()='Follow']")

                if button_follow.text == 'Follow' :
                    print("===following user now in few seconds")
                    sleep(randint(4,6))
                    button_follow.click()
                    followed += 1
                else: 
                    print("===>No follow button available, so skipping the following")

                # Liking the picture
                print('===>Liking the picture')
                sleep(randint(1,2))
                button_like = webdriver.find_element(By.xpath ,'/html/body/div[5]/div[2]/div/article/div/div[3]/div/div/section[1]/span[1]/button')
                button_like.click()
                likes += 1

                # Comments and tracker
                comm_prob = randint(1,10)
                print('===>Trying to comment if probability is found to be more than',comment_percentage)
                print('===>Probability found to be: ', comm_prob*10)
                if comm_prob > comment_percentage/10:
                    waitTime = randint(1,8)
                    print('===>So commenting')
                    sleep(randint(1,8))                                                    
                    webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                    sleep(randint(2,4))
                    comment_box = webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                    commentIndex = randint(0,len(commentsList)-1)
                    print('===>printing comment number {0}, which is {1}'.format(commentIndex+1, commentsList[commentIndex]))
                    comment_box.send_keys(commentsList[commentIndex])
                    sleep(1)
                    # Enter to post comment
                    comment_box.send_keys(Keys.ENTER)
                    comments += 1
                    print('===>Commented! now waiting few seconds')
                    sleep(randint(3,6))
                else:
                    print('===>Skipping commenting, since probability is low')
            else:
                print('===>Post already liked, so skipping the post')

            # Next picture
            print('===>Moving next')
            webdriver.find_element_by_link_text('Next').click()
            # sleep(randint(2,5))
        
    # Some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
        continue


print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
