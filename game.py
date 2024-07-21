# import tkinter
import random
import json

#地图
map=["起点","上海","命运","北京","所得税","郑州火车站","成都","机会","桂林","深圳","监狱","大连","电力公司","沈阳","哈尔滨","天津火车站","长春","命运","吉林","西藏","停车场","杭州","机会","云南","贵州","长沙火车站","湖北","四川","自来水公司","新疆","进牢","澳门","甘肃","命运","陕西","广州火车站","机会","抚州","财产税","苏州"]
#索引   0     1      2     3      4         5        6      7     8      9    10    11     12      13     14       15       16     17    18     19     20     21    22     23    24      25      26     27    28         29     30    31    32    33     34       35       36     37     38    39
owner=[""   ,""    ,""   ,""    ,""       ,""      ,""    ,""   ,""    ,""  ,""   ,""    ,""     ,""    ,""      ,""      ,""    ,""   ,""    ,""    ,""    ,""   ,""    ,""   ,""     ,""     ,""    ,""   ,""        ,""    ,""   ,""   ,""   ,""    ,""      ,""      ,"",     ""    ,""   ,"" ]
#色子
def dice():
    dice = int(random.randint(1,6))
    return dice
#购买价
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
        return 4000
#升级价
def get_buildcost(local_name):
    if local_name == "上海":
        return 2000
    if local_name == "北京":
        return 2000
    if local_name == "成都":
        return 1500
    if local_name == "桂林":
        return 1500
    if local_name == "深圳":
        return 1500
    if local_name == "大连":
        return 1500
    if local_name == "沈阳":
        return 1500
    if local_name == "哈尔滨":
        return 500
    if local_name == "长春":
        return 1000
    if local_name == "吉林":
        return 1000
    if local_name == "西藏":
        return 1000
    if local_name == "杭州":
        return 1000
    if local_name == "云南":
        return 1000
    if local_name == "贵州":
        return 1500
    if local_name == "湖北":
        return 500
    if local_name == "四川":
        return 500
    if local_name == "新疆":
        return 2000
    if local_name == "澳门":
        return 1500
    if local_name == "甘肃":
        return 1500
    if local_name == "陕西":
        return 1500
    if local_name == "抚州":
        return 2000
    if local_name == "苏州":
        return 3000
    if local_name == "郑州火车站":
        return 500
    if local_name == "电力公司":
        return 500
    if local_name == "天津火车站":
        return 500
    if local_name == "长沙火车站":
        return 500
    if local_name == "自来水公司":
        return 1500
    if local_name == "广州火车站":
        return 500
#过路费
#增长函数
def f(Lv,x):
    i = Lv[3:len(Lv)]
    i = int(i)
    i += 1
    a = 1 / (1 + 2 ** (-((i - 10) - 20 * int((i - 10) / 20) + 5))) + int((i - 10) / 10)
    a = int(100*a)
    a = int(x*100*a)
    return a
def get_tolls(local_name,Lv):
    if local_name == "上海":
        return f(Lv,2)
    if local_name == "北京":
        return f(Lv,2)
    if local_name == "成都":
        return f(Lv,1.5)
    if local_name == "桂林":
        return f(Lv,1.5)
    if local_name == "深圳":
        return f(Lv,1.75)
    if local_name == "大连":
        return f(Lv,1.5)
    if local_name == "沈阳":
        return f(Lv,1.7)
    if local_name == "哈尔滨":
        return f(Lv,0.5)
    if local_name == "长春":
        return f(Lv,0.5)
    if local_name == "吉林":
        return f(Lv,0.5)
    if local_name == "西藏":
        return f(Lv,0.6)
    if local_name == "杭州":
        return f(Lv,0.7)
    if local_name == "云南":
        return f(Lv,0.6)
    if local_name == "贵州":
        return f(Lv,0.75)
    if local_name == "湖北":
        return f(Lv,0.5)
    if local_name == "四川":
        return f(Lv,0.4)
    if local_name == "新疆":
        return f(Lv,2)
    if local_name == "澳门":
        return f(Lv,1.7)
    if local_name == "甘肃":
        return f(Lv,1.7)
    if local_name == "陕西":
        return f(Lv,1.8)
    if local_name == "抚州":
        return f(Lv,2)
    if local_name == "苏州":
        return f(Lv,3)
    if local_name == "长沙火车站":
        d = dice()
        return d * f(Lv, 0.3)
    if local_name == "天津火车站":
        d = dice()
        return d * f(Lv, 0.3)
    if local_name == "电力公司":
        d = dice()
        return d*f(Lv,0.2)
    if local_name == "广州火车站":
        d = dice()
        return d * f(Lv, 0.3)
    if local_name == "郑州火车站":
        d = dice()
        return d * f(Lv, 0.3)
    if local_name == "自来水公司":
        d = dice()
        return d * f(Lv, 0.3)
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
                self.haven_place.append((self.local_name,"Lv.0"))
                owner.pop(self.local)
                owner.insert(self.local,self.name)
                print(f"你购买了{self.local_name}")
            else:
                print("无法购买，钱不足")
    def input(self):
        # 人
        if self.type == "human":
            # 为了enter下一人
            i = True
            have = False
            getLv = 0
            while i == True:
                #防止重复买
                #get 有无&等级
                for (place,Lv) in self.haven_place:
                    if place == self.local_name:
                        have = True
                        Lv = getLv
                if have == True:
                    print(f"你有{self.money}元")
                    print(f"{self.local_name}(升级{get_buildcost(self.local_name)}元)")
                    ip = input("按b升级，按s查询已有，无操作下一步")
                    #升级
                    if ip == "b" and type(get_buildcost(self.local_name)) != None:
                        self.cost(get_buildcost(self.local_name))
                        for (place, Lv) in self.haven_place:
                            if place == self.local_name:
                                  self.haven_place.remove((place,f"Lv.{getLv}"))
                                  getLv += 1
                                  self.haven_place.append((place,f"Lv.{getLv}"))
                    # 查看已买
                    if ip == "s":
                        print(self.haven_place)
                    # 下一人
                    if ip == "":
                        i = False
                if have == False:
                    print(f"你有{self.money}元")
                    print(f"{self.local_name}(购买-{get_buycost(self.local_name)}元)")
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
                    if ip == "d":
                        self.money = -1
        if self.type == "robot":
            i = True
            have = False
            getLv = 0
            while i == True:
                #防止重复买
                #get 有无&等级
                for (place,Lv) in self.haven_place:
                    if place == self.local_name:
                        have = True
                        Lv = getLv
                if have == True:
                    print(f"你有{self.money}元")
                    print(f"{self.local_name}(升级{get_buildcost(self.local_name)}元)")
                    ip = print("按b升级，按s查询已有，无操作下一步")
                    if self.money >= get_buildcost(self.local_name):
                        ip = "b"
                        print("b")
                    #升级
                    if ip == "b" and type(get_buildcost(self.local_name)) != None:
                        self.cost(get_buildcost(self.local_name))
                        for (place, Lv) in self.haven_place:
                            if place == self.local_name:
                                  self.haven_place.remove((place,f"Lv.{getLv}"))
                                  getLv += 1
                                  self.haven_place.append((place,f"Lv.{getLv}"))
                    # 查看已买
                        print(self.haven_place)
                    # 下一人
                    if ip == "":
                        i = False
                if have == False:
                    print(f"你有{self.money}元")
                    print(f"{self.local_name}(购买-{get_buycost(self.local_name)}元)")
                    ip = input("按b购买脚下，按s查询已有，无操作下一步")
                    if self.money >= get_buycost(self.local_name):
                        ip = "b"
                        print("b")
                    #买
                    if ip == "b":
                        self.buy()
                    #查看已买
                    if ip == "s":
                        print(self.haven_place)
                    #下一人
                    if ip == "":
                        i = False


    def is_it_mine(self):
        for (place, Lv) in self.haven_place:
            if place == self.local_name:
                return True
    def tolls(self):
        if self.name == "player1":
            lv = "Lv.20"
            for (local_name, Lv) in player2.haven_place:
                if local_name == player1.local_name:
                    lv = Lv
            player1.money -= get_tolls(player1.local_name,lv)
            print(f"你花费了{get_tolls(player1.local_name,lv)}元")
        if self.name == "player2":
            lv = "lv.100"
            for (local_name, Lv) in player1.haven_place:
                if local_name == player2.local_name:
                    lv = Lv
            print(lv)
            player2.money -= get_tolls(player2.local_name,lv)
            print(f"你花费了{get_tolls(player2.local_name,lv)}元")
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
        print(f"{self.name}走了{dicenum}步至{self.local_name}")
    def cost(self,money):
        if self.money >= money:
            self.money -= money
            print(f"你花费了{money}元")
        else:
            print("钱不足")
    def get(self,money):
        self.money += money
        print(f"你得到了{money}元")
    def move(self):
        if self.local_name == "所得税":
            self.money -= 2000
            print(f"你失去了2000元")
        if self.local_name == "财产税":
            self.money -= 1000
            print(f"你失去了2000元")
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
            if owner[self.local] != "" and f"{self.name}":
                self.tolls()
            else:
                self.input()
        print("")#分割块

    def getLv(self,place):
        for (local_name, Lv) in self.haven_place:
            if local_name == place:
                return Lv

player1 = Player("player1","human")
type = input("1p|2p?")
if type == "1p":
    type = "robot"
if type == "2p":
    type = "player"
player2 = Player("player2",type)
#主循环
while True:
    player1.move()
    if player1.money < 0:
        print("player2 win!")
        break
    player2.move()
    if player2.money < 0:
        print("player1 win!")
        break
