class goods:
    def __init__(self,num,name,price,tot,res):
        #商品序号、商品名、单价、总数量和剩余数量。
        self.__num = num
        self.__name = name
        self.__price = price
        self.__tot = tot
        self.__res = res
    
    #输出商品信息
    def dispaly(self):
        print("该商品序号为",self.__num)
        print("该商品名称为",self.__name)
        print("该商品单价为",self.__price)
        print("该商品总数量为",self.__tot)
        print("该商品剩余数量为",self.__res)
    
    #输出已售出商品价值
    def income(self):
        print(self.price * (self.__tot - self.__res))
    
    def setdata(self,num,name,price,tot,res):
        self.__num = num
        self.__name = name
        self.__price = price
        self.__tot = tot
        self.__res = res