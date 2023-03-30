class Fibonacci(object):
    def __init__(self, max_len):
        self.max_len = max_len
        self.a = 0
        self.b = 1
        self.current_num = 0
        self.fibonacci_list = list()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.max_len:
            self.current_num += 1
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            return ret
        else:
            self.current_num = 0
            self.a = 0
            self.b = 1
            raise StopIteration
        
def fibonacci(num):
    # a, b = 1, 1
    # if n<=2:
    #     return 1
    # else:
    #     n -= 2
    #     while n>0:
    #         a, b = b, a+b
    #         yield b
    a, b = 0, 1
    i = 0
    while i < num: 
        yield a
        a, b = b, a+b
        i += 1
    
def yield_example():
    num = 500
    a = 0
    type = 0
    while a<num:
        print(f"type={type}")
        if(type==1):
            a = 114514
        else:
            a = a*2 + 1
        type = yield a

if __name__ == "__main__":
    # for num in fibonacci(3):
    #     print(num)

    # for i in Fibonacci(10):
    #     print(i)

    # G = (x for x in range(10))
    # print(G)# <generator object <genexpr> at 0x000001FE9AA5E5C8>
    # print(tuple(G))

    # for i in yield_example(50):
    #     print(i)
    a = yield_example()
    print(next(a))
    print(a.send(1))
    # # print(a.send(1))
