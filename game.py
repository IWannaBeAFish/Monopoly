# import tkinter
import random

#地图
map=["起点","上海","命运","北京","所得税","郑州火车站","成都","机会","桂林","深圳","监狱","大连","电力公司","沈阳","哈尔滨","天津火车站","长春","命运","吉林","西藏","停车场","杭州","机会","云南","贵州","长沙火车站","湖北","四川","自来水公司","新疆","进牢","澳门","甘肃","命运","陕西","广州火车站","机会","抚州","财产税","苏州"]
#索引   0     1      2     3      4         5        6      7     8      9    10    11     12      13     14       15       16     17    18     19     20     21    22     23    24      25      26     27    28         29     30    31    32    33     34       35       36     37     38    39
#色子
def dice():
    dice = int(random.randint(1,6))
    return dice
#房价
def get_buycost(local_name):
    if local_name == "上海":
        return 3000
    if local_name == "北京":
        return 3000
    if local_name == "郑州火车站":
        return 2000
    if local_name == "成都":
        return 2600
    if local_name == "桂林":
        return 2600
    if local_name == "深圳":
        return 2600
    if local_name == "大连":
        return 2500
    if local_name == "电力公司":
        return 1500
    if local_name == "沈阳":
        return 2200
    if local_name == "哈尔滨":
        return 1000
    if local_name == "天津火车站":
        return 2000
    if local_name == "长春":
        return 1400
    if local_name == "吉林":
        return 1400
    if local_name == "西藏":
        return 2000
    if local_name == "杭州":
        return 2000
    if local_name == "云南":
        return 2000
    if local_name == "贵州":
        return 2800
    if local_name == "长沙火车站":
        return 2000
    if local_name == "湖北":
        return 1200
    if local_name == "四川":
        return 1200
    if local_name == "自来水公司":
        return 1500
    if local_name == "新疆":
        return 4000
    if local_name == "澳门":
        return 2600
    if local_name == "甘肃":
        return 2600
    if local_name == "陕西":
        return 2600
    if local_name == "广州火车站":
        return 2000
    if local_name == "抚州":
        return 3500
    if local_name == "苏州":
        return 3200
#玩家&操作
class Player:
    def __init__(self,name,type):
        self.name = name
        self.local = 0
        self.local_name = "起点"
        self.haven_place = []
        self.canmove = True
        self.stoptimes = 0
        self.money = 2000
        self.type = type
    def buy(self):
        buycost = get_buycost(self.local_name)
        if buycost == None:
            print("这是非卖品")
        else:
            if self.money >= buycost:
                self.cost(buycost)
                self.haven_place.append(self.local_name)
                print(f"你购买了{self.local_name}")
            else:
                print("无法购买，钱不足")
    def input(self):
        # 人
        if self.type == "human":
            # 为了enter下一人
            i = True
            while i == True:
                #防止重复买
                have = False
                for place in self.haven_place:
                    if place == self.local_name:
                        have = True
                    if have == True:
                        ip = input("按b购买脚下，按s查询已有，无操作下一步")
                        # 查看已买
                        if ip == "s":
                            print(self.haven_place)
                        # 下一人
                        if ip == "":
                            i = False
                    #买

                    if have == False:
                        ip = input("按b购买脚下，按s查询已有，无操作下一步")
                        #买
                        if ip == "b":
                            self.buy()
                        #查看已买
                        if ip == "s":
                            print(self.haven_place)
                        #下一人
                        if ip == "":
                            i = False
    def tp(self,local):
        self.local = local
        self.local_name = map[self.local]
    def run(self):
        dicenum = dice()
        self.local += dicenum
        if self.local > 39:
            self.local -= 39
            self.get(2000)
        self.local_name = map[self.local]
        print(f"{self.name}走了{dicenum}步至{self.local_name}({get_buycost(self.local_name)}元)")
        print(f"你有{self.money}元")
    def cost(self,money):
        self.money -= money
        print(f"你花费了{money}元")
    def get(self,money):
        self.money += money
        print(f"你得到了{money}元")
    def move(self):
        if self.local_name == "进牢":
            self.tp(10)
        if self.local_name == "监狱":
            if self.stoptimes < 2:
                self.canmove = False
                self.stoptimes += 1
            if self.stoptimes >= 2:
                self.stoptimes = 0
                self.canmove = True
                print(f"{self.name}刑满释放")
        if self.canmove == False:
            print(f"{self.name}无法移动")
        if self.canmove == True:
            self.run()
            self.input()
        print("")#分割块

player1 = Player("player1","human")
player2 = Player("player2","human")
#主循环
while True:
    player1.move()
    player2.move()













































