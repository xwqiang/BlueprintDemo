from config import dev

name="aa"
pwd="aa"

s={}
keys = [key for key in dir(dev) if not key.startswith('__')]
for k in keys:
    print(k,getattr(dev,k))
