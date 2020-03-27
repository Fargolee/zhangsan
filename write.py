import time
now = time.strftime("%y-%m-%d %H:%M:%S")
# 20-03-27 22:02:35

text = input('今天的心情:')
# with open('日记.txt', 'a', encoding='utf8') as f:
with open('F:\日记.txt', 'a', encoding='utf8') as f:
    f.write(now+'\n')
    f.write(text + '\n')
    f.write('----------\n')
