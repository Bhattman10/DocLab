import os
import pwd
import users


__USER_DIR = "users"
username = "testuser"
password = "testpass"

user_dir = os.path.join(os.path.split(__file__)[0], __USER_DIR, username)
print(user_dir)

with users.create(username, password, user_dir) as user:
    os.mkdir("testdir")

