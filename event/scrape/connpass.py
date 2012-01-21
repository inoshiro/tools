# vim:fileencoding=utf-8
from BeautifulSoup import BeautifulSoup

class EventScraper(object):
    def __init__(self, source):
        self.soup = BeautifulSoup(source)
        self.users = self._getUsers()

    def _getUsers(self):
        users = self.soup.findAll('p', {'class':'user'})
        return [ u.text for u in users ]

class UserScraper(object):
    def __init__(self, source):
        self.soup = BeautifulSoup(source)
        self.facebook_id = ''
        self.twitter_id = self._getTwitterId()

    def _getTwitterId(self):
        social_link = self.soup.find('p', {'class':'social_link clearfix'}).findAll('a')
        if social_link == []:
            twitter_id = ''
        else:
            twitter_id = social_link.pop()['href'].split('/').pop()
        return twitter_id
