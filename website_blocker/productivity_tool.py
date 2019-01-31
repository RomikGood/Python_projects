import time
from datetime import datetime as dt   

host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = '127.0.0.1'
sites_that_kill_me = ['www.facebook.com', 'www.twitter.com', 'www.twiter.com']

print(dt.now())

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
    # if dt.now():
        print('working hours')

        with open(host_path, 'r+') as file:
            content = file.read()
            for site in sites_that_kill_me:
                if site in content:
                    pass
                else:
                    file.write(redirect + ' ' + site +  '\n')

    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites_that_kill_me):
                    file.write(line)
            
            file.truncate()
        print('time to play!!!')
    time.sleep(600)



