from time import sleep

# Blocking 한 함수들로 구성

def sleep_3s():
    sleep(3)
    print('Wake up!')


print('Start Sleeping')
sleep_3s()
print('End of Program')