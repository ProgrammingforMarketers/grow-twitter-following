''''
In this code we'll have a bunch of examples you can use at your own discretion. 

Simply remove the three ' marks above and below the code you want in order to run it, while
leaving the text within a new set of three ' marks.

Once that's done, go to your Terminal, navigate to where this code and the twitter_follow_bot
code is (they have to be in the same folder), and just type in "python sample_twitter_codes.py" (without quotes)

WARNING: Following too many people, favoriting too many things, CAN and WILL get you banned.

Be smart. And have fun :). 

Justin and Nat
'''

'''
#1 Here you can automatically follow people who tweet about a certain phrase. Just replace the phrase
with something relevant to you! Also you can set the count to whatever makes you most comfortable.

from twitter_follow_bot import auto_follow
auto_follow("phrase", count=100)
'''

'''
#2 In this code, change "jwmares" to the twitter handle whose followers you want to follow, 
and set the count to how many people should be followed. Default is 100.

from twitter_follow_bot import auto_follow_followers_for_user
auto_follow_followers_for_user("jwmares", count=10)
'''

'''
#3 This code will let you favoite things that are relevant to you. Just replace "phrase" with the phrase
you want to favorite for, and set the count to how many things you want to favorite.

from twitter_follow_bot import auto_fav
auto_fav("phrase", count=100)
'''

'''
#4 This code will automatically un-follow everyone who hasn't followed you back.

from twitter_follow_bot import auto_unfollow_nonfollowers
auto_unfollow_nonfollowers()
'''