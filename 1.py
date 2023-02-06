import requests
import re

# YES
# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample1.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html
link_A = input()
link_B = input()
link_C = requests.get(link_A).text.split('"')[1]
link_C_returns = requests.get(link_C).text.split('"')[1]
if link_C_returns == link_B:
    print("Yes")
else:
    print("No")
