from tasks import longtime_add
from time import sleep

if __name__ == '__main__':
    time_input=int(input("Enter number less than or equal to or greater than 12 : "))
    result = longtime_add.delay(time_input)
    # task not finished, return False
    print ('Task finished? ', result.ready())
    print ('Task result: ', result.result)
    # sleep 10 seconds 
    sleep(10)
    # now the task should be finished and return True
    print ('Task finished? ', result.ready())
    print ('Task result: ', result.result)