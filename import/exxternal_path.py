import sys

for p in sys.path:
    print(p)

print("-"*20)
sys.path.append("/home/yuwei/桌面/test")
import a
for p in sys.path:
    print(p)
print(a.name)
