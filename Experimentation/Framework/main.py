import doclab
import os
import random
import secrets
import string
import time
import users


python_library = (
    """
import math

def distance(u: tuple[float, float], v: tuple[float, float]) -> float:
    dx = v[0] - u[0]
    dy = v[1] - u[1]
    return math.sqrt(dx * dx + dy * dy)

"""
)

python_program = (
    """
import mathlib

u = (1.0, 2.0)
v = (5.0, 5.0)
dist = mathlib.distance(u, v)
print(f"The distance between {u} and {v} is {dist}.")

"""
)

cpp_program = (
    """
#include <iostream>
#include <fstream>
#include <sstream>

int main()
{
    std::ifstream infile("text_file.txt");
    std::stringstream ss;
    ss << infile.rdbuf();

    std::cout << ss.str();
                
    return 0;
}
"""
)

__USER_DIR = "users"
__SOURCE_DIR = "source"
__PASSWORD_LEN = 16


username = "testuser"
user_dir = os.path.join(os.path.split(__file__)[0], __USER_DIR, username)
with users.create(username, "testpass", user_dir) as user:
    with doclab.Environment(__SOURCE_DIR) as env:
        env.update_file("text_file.txt", "Hello this is a file\n")
        env.update_file("mathlib.py", python_library)
        env.update_file("hello.py", python_program)
        env.update_file("main.cpp", cpp_program)

        build, output = env.execute("test.exe", "main.cpp", [])
        print(output.message)
        build, output = env.execute("test.py", "hello.py", ["mathlib.py"])
        print(output.message)

# usernames = ["abc123", "varuns1", "jnaki"]

# for username in usernames:
#     print(f"User: {username}")
#     password = "".join(random.choices(string.ascii_uppercase + string.digits, k=__PASSWORD_LEN))
#     user_dir = os.path.join(os.path.split(__file__)[0], __USER_DIR, username)
#     with users.create(username, password, user_dir) as user:
#         with doclab.Environment(__SOURCE_DIR) as env:
#             env.update_file("text_file.txt", "Hello this is a file\n")
#             env.update_file("mathlib.py", python_library)
#             env.update_file("hello.py", python_program)
#             env.update_file("main.cpp", cpp_program)

#             build, output = env.execute("test.exe", "main.cpp", [])
#             print(output.message)
#             build, output = env.execute("test.py", "hello.py", ["mathlib.py"])
#             print(output.message)

# print("Waiting...")
# time.sleep(10)

# for username in usernames:
#     users.destroy(username)
