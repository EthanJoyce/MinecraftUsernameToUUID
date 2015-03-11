""" Username to UUID
 Converts a Minecraft username to it's UUID equivalent.

Parses http://www.lb-stuff.com/Minecraft-Name-History output to retrieve the UUID
 of an old name that's no longer in use.
"""
import http.client

from bs4 import BeautifulSoup


class UsernameToUUID:
    def __init__(self, username):
        self.username = username

    def get_uuid(self):
        """
          Get the UUID of the player.
        """
        httpConn = http.client.HTTPConnection("www.lb-stuff.com");
        httpConn.request("GET", "/Minecraft-Name-History?user=" + self.username);
        response = httpConn.getresponse().read()
        soup = BeautifulSoup(response)

        return soup.body.findAll('p')[1].findAll('code')[1].text
