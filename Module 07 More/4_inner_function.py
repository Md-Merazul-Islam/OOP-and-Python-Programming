def inner_fun_check():
    print("This is first fun")
    def inner_fun():
        print("this is inner funtion")
        return 100
    return inner_fun

print(inner_fun_check()())


def do_something(work):
    print("work something")
    work()
    
    
def work():
    print("This is work function ")    
    
do_something(work)