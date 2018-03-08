import os

test=os.getenv("JAVA_HOME", None)
print('.'.join(["aaa",test]))