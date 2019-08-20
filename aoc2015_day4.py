from hashlib import md5
from itertools import count


found_five = False

with open("aoc2015_day4.txt", "r") as input_file:
    cipher = input_file.read().strip()

for i in count(1):
    md5_hash = md5("{s}{n}".format(s=cipher, n=i).encode()).hexdigest()
    if md5_hash.startswith("0"*6):
        print("Smallest for six zeros:", i)
        break
    elif not found_five and md5_hash.startswith("0"*5):
        print("Smallest for five zeros:", i)
        found_five = True