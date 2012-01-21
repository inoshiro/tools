# vim:fileencoding=utf-8
import sys, urllib2
from scrape import connpass

def main():
    content = getContent(sys.argv[1])
    id_list = getidlist(content)

def getidlist(content):
    event = connpass.EventScraper(content)

    id_list = []
    for user in event.users:
        url = "http://connpass.com/user/" + user
        content = getContent(url)
        user = connpass.UserScraper(content)
        print("get id: " + user.twitter_id + "\n")
        id_list.append(user.twitter_id)
    return id_list

def getContent(url):
    content = urllib2.urlopen(url).read()
    return content

if __name__ == '__main__':
    main()
