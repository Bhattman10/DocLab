import crypt
import dataclasses
import datetime
import os
import pwd
import subprocess


@dataclasses.dataclass
class UserProperties:
    username: str
    password: str
    uid: int
    gid: int
    home_dir: str
    shell_dir: str
    expiration: datetime.datetime


class User:

    def __init__(self, properties: UserProperties):
        self.__properties = properties
        self.__prev_uid = None
        self.__prev_gid = None
        self.__prev_path = None
        
    def __enter__(self):
        # Store previous user settings
        self.__prev_uid = os.getuid()
        self.__prev_gid = os.getgid()
        self.__prev_path = os.path.abspath(".")
        # Change user and move to home directory
        os.chdir(self.__properties.home_dir)
        os.seteuid(self.__properties.uid)
        # os.setegid(self.__properties.gid)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Restore previous user
        os.seteuid(self.__prev_uid)
        os.setegid(self.__prev_gid)
        os.chdir(self.__prev_path)

    @property
    def properties(self):
        return self.__properties



def create(username: str, password: str, home_dir: str = ""):
    # Create password hash
    salt = crypt.mksalt(crypt.METHOD_SHA512)
    password_hashed = crypt.crypt(password, salt)
    # Generate user creation command
    command = ["useradd", "-m", "-p", password_hashed]
    if home_dir:
        command.extend(["-d", home_dir])
    command.append(username)
    # Create user
    subprocess.run(command, capture_output=True)
    pw = pwd.getpwnam(username)
    properties = UserProperties(
        username,
        password,
        pw.pw_uid,
        pw.pw_gid,
        pw.pw_dir,
        pw.pw_shell,
        datetime.datetime.now()
    )
    return User(properties)


def destroy(username: str):
    return subprocess.run(["userdel", "-r", username], capture_output=True)


