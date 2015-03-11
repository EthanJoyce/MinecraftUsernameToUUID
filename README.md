# Minecraft Username to UUID
Convert old Minecraft usernames to their UUID.
Written for Python3.

## Usage
1. Add the username_to_uuid.py file to your Python path.
2. Use the library like this:
```
from username_to_uuid import UsernameToUUID

converter = UsernameToUUID("MrLolEthan")
uuid = converter.get_uuid()

... # Do stuff
```
The contents of `uuid` will now be:
`854dd5e0fe044568a787053417ea6335`

