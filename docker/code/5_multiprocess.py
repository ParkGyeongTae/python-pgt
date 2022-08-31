from multiprocessing import Process
import time

class schedule:
    
    # def __init__(self):
    #     self.var_1 = None
    #     self.var_2 = None
    #     self.var_3 = None

    def set_func_1(self, var_1):
        self.var_1 = var_1

    def set_func_2(self, var_2):
        self.var_2 = var_2

    def set_func_3(self, var_3):
        self.var_3 = var_3

    def func_1(self):
        start_time = time.time()

        time.sleep(1)
        print(self.var_1)
        time.sleep(1)

        end_time = time.time()
        print('func_1: ', end_time - start_time)

    def func_2(self):
        start_time = time.time()

        time.sleep(1)
        print(self.var_2)
        time.sleep(1)

        end_time = time.time()
        print('func_2: ', end_time - start_time)

    def func_3(self):
        start_time = time.time()

        time.sleep(2)
        print(self.var_3)

        end_time = time.time()
        print('func_3: ', end_time - start_time)

if __name__ == '__main__':

    my_test = schedule()

    my_test.set_func_1('a')
    my_test.set_func_2('b')
    my_test.set_func_3('c')

    start_time = time.time()
    my_test.func_1()
    my_test.func_2()
    my_test.func_3()
    end_time = time.time()
    print('total :', end_time - start_time)
    exit()

    p1 = Process(target = my_test.func_1)
    p2 = Process(target = my_test.func_2)
    p3 = Process(target = my_test.func_3)

    start_time = time.time()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end_time = time.time()
    print('total :', end_time - start_time)
    exit()