from time import sleep
for c in range(10, 0-1,-1):
    print('\033[1;33m', c, '\033[m')
    sleep(1)

print('\033[7;33mFIM\033[m')