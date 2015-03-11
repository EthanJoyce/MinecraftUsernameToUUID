from username_to_uuid import UsernameToUUID
import sys


print("Please enter a username: ")
username = sys.stdin.readline().rstrip()

converter = UsernameToUUID(username)
uuid = converter.get_uuid()

if (uuid is not ""):
    print("That player's UUID is: " + uuid)
else:
    print("That player was not found.")
