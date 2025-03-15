# pip install python-dotenv
import dotenv

import os

v = os.getenv("JAVA_HOME")
print(v)

#
dotenv.load_dotenv(override=True, encoding="utf-8")

v1 = os.getenv("HTTP_PROXY")
print(v1)

v2 = os.getenv("JAVA_HOME")
print(v2)

