# import tkinter
import random
import json
import time

#地图
map=["起点","上海","命运","北京","所得税","郑州火车站","成都","机会","桂林","深圳","监狱","大连","电力公司","沈阳","哈尔滨","天津火车站","长春","命运","吉林","西藏","停车场","杭州","机会","云南","贵州","长沙火车站","湖北","四川","自来水公司","新疆","进牢","澳门","甘肃","命运","陕西","广州火车站","机会","抚州","财产税","苏州"]
#索引   0     1     2      3      4         5        6      7     8      9     10    11     12       13     14        15       16     17    18     19     20     21    22     23    24      25         26     27    28         29     30    31     32    33     34       35       36     37     38     39
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
def get_buildcost(localname):
    if localname == "上海":
        return 2000
    if localname == "北京":
        return 2000
    if localname == "成都":
        return 1500
    if localname == "桂林":
        return 1500
    if localname == "深圳":
        return 1500
    if localname == "大连":
        return 1500
    if localname == "沈阳":
        return 1500
    if localname == "哈尔滨":
        return 500
    if localname == "长春":
        return 1000
    if localname == "吉林":
        return 1000
    if localname == "西藏":
        return 1000
    if localname == "杭州":
        return 1000
    if localname == "云南":
        return 1000
    if localname == "贵州":
        return 1500
    if localname == "湖北":
        return 500
    if localname == "四川":
        return 500
    if localname == "新疆":
        return 2000
    if localname == "澳门":
        return 1500
    if localname == "甘肃":
        return 1500
    if localname == "陕西":
        return 1500
    if localname == "抚州":
        return 2000
    if localname == "苏州":
        return 3000
    if localname == "郑州火车站":
        return 500
    if localname == "电力公司":
        return 500
    if localname == "天津火车站":
        return 500
    if localname == "长沙火车站":
        return 500
    if localname == "自来水公司":
        return 1500
    if localname == "广州火车站":
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
#多层感知机
wh1 = [0,0,0,0,0]
wh2 = [0,0,0,0,0]
wh3 = [0,0,0,0,0]
wh4 = [0,0,0,0,0]
wh5 = [0,0,0,0,0]

wh1 = [0,0]
wh2 = [0,0]
wh3 = [0,0]
wh4 = [0,0]
wh5 = [0,0]
# wlocal = [0, -15, 0, -19, 0, -17, 8, 0, 14, -18, 0, 11, 17, 26, 47, -16, -17, 0, 20, -20, 0, -16, 0, -13, 23, 20, -13, 26, -12, 0, 0, -10, -5, 0, 2, 20, 0, 5, 0, 0]
wlocal=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# wlocal = [0, 127, 0, 137, 0, -66, -65, 0, 107, -65, 0, 219, -66, -64, 236, 168, 227, 0, -63, 209, 0, 149, 0, 139, 169, 159, 208, 259, -61, 199, 0, 120, 99, 0, 99, 149, 0, 50, 0, 70]
wmoney=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def o(x,w):
    if w*x+w >= 0:
        return 1
    else:
        return 0
def MLP(local,money):
    try:
        if o(local,wlocal[local])+o(local,wmoney[local]) == 0 or money < get_buycost(map[local]): #\
        #or map[local]=="命运"or"机会"or"监狱"or""
            return False
    except:
        return False
    if o(local,wlocal[local])+o(local,wmoney[local]) == 1:
        if dice() == 1:
            return True
        else:
            return False
    if o(local,wlocal[local])+o(local,wmoney[local]) == 2:
        return True


#玩家&操作
class Player:
    def __init__(self,name,type):
        self.name = name
        self.local = 0
        self.local_name = "起点"
        self.haven_list = []
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
                self.haven_list.append((self.local_name, "Lv.0"))
                owner.pop(self.local)
                owner.insert(self.local,self.name)
                print(f"你购买了{self.local_name}")
            else:
                print("无法购买，钱不足")
    def input(self):
        time.sleep(0.5)
        # 人
        if self.type == "human":
            # 为了enter下一人
            i = True
            have = False
            getLv = 0
            while i == True:
                #防止重复买
                #get 有无&等级
                for (place,Lv) in self.haven_list:
                    if place == self.local_name:
                        have = True
                        Lv = getLv
                if have == True:
                    print(f"你有{self.money}元")
                    print(f"{self.local_name}(升级{get_buildcost(self.local_name)}元)")
                    ip = input("按b升级，按s查询已有，无操作下一步")
                    #升级
                    if ip == "b" :
                            self.cost(get_buildcost(self.local_name))
                            for (place, Lv) in self.haven_list:
                                if place == self.local_name:
                                    self.haven_list.remove((place, f"Lv.{getLv}"))
                                    getLv += 1
                                    self.haven_list.append((place, f"Lv.{getLv}"))

                    # 查看已买
                    if ip == "s":
                        print(self.haven_list)
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
                        print(self.haven_list)
                    #下一人
                    if ip == "":
                        i = False
                    if ip == "d":
                        self.money = -1
        #人机
        if self.type == "robot":
           if MLP(self.local,self.money) == True:

                   # 为了enter下一人
                   i = True
                   have = False
                   getLv = 0

                   while i == True:

                       # 防止重复买
                       # get 有无&等级
                       for (place, Lv) in self.haven_list:
                           if place == self.local_name:
                               have = True
                               Lv = getLv
                       if have == True:
                           print(f"你有{self.money}元")
                           print(f"{self.local_name}(升级{get_buildcost(self.local_name)}元)")
                           if self.money < get_buildcost(self.local_name):
                               i = False
                           ip = print("按b升级，按s查询已有，无操作下一步")
                           # 升级
                           if MLP(self.local,self.money):
                               self.cost(get_buildcost(self.local_name))
                               for (place, Lv) in self.haven_list:
                                   if place == self.local_name:
                                       self.haven_list.remove((place, f"Lv.{getLv}"))
                                       getLv += 1
                                       self.haven_list.append((place, f"Lv.{getLv}"))
                               time.sleep(0.3)
                           else:
                               i = False


                           # 查看已买

                           print(self.haven_list)
                           # 下一人

                       if have == False:
                           print(f"你有{self.money}元")
                           print(f"{self.local_name}(购买-{get_buycost(self.local_name)}元)")
                           if self.money < get_buycost(self.local_name):
                               i = False
                           ip = print("按b购买脚下，按s查询已有，无操作下一步")
                           # 买
                           if MLP(self.local,self.money):
                               self.buy()
                               time.sleep(0.3)
                           # 查看已买

                           print(self.haven_list)
                           # 下一人

                           if ip == "d":
                               self.money = -1
    def is_it_mine(self):
        for (place, Lv) in self.haven_list:
            if place == self.local_name:
                return True
    def tolls(self,Player):
        # if self.name == "player1":
        #     lv = "Lv.20"
        #     lv = player2.getLv(player1.local_name)
        #     player1.money -= get_tolls(player1.local_name,lv)
        #     print(f"你花费了{get_tolls(player1.local_name,lv)}元")
        #     ######################
        #     pop = wlocal.pop(self.local) +1
        #     wlocal.insert(self.local,pop)
        #     print(wlocal)
        # if self.name == "player2":
        #     lv = "lv.100"
        #     lv = player1.getLv(player2.local_name)
        #     pop = wlocal.pop(self.local) + 1
        #     wlocal.insert(self.local, pop)
        #     print(wlocal)
        #     print(lv)
        #     player2.money -= get_tolls(player2.local_name,lv)
        #     print(f"你花费了{get_tolls(player2.local_name,lv)}元")
        if self.name == "palyer1":
            havenlist = player2.haven_list()
            for (place,lv) in havenlist:
                if place == self.local_name:
                    LV = lv
            self.money -= get_tolls(self.local_name, LV)
            print(f"player1付了{get_tolls(self.local_name, LV)}元")
            player2.money += get_tolls(self.local_name, LV)
            print(f"player2得到了{get_tolls(self.local_name, LV)}元")
            pop = wlocal.pop(self.local) + 3#奖励参数
            wlocal.insert(self.local, pop)

            print(wlocal)
        if self.name == "player2":
            havenlist = player1.getHavenplace()
            for (place,lv) in havenlist:
                if place == self.local_name:
                    LV = lv
            self.money -= get_tolls(self.local_name, LV)
            print(f"player2付了{get_tolls(self.local_name, LV)}元")
            player1.money += get_tolls(self.local_name, LV)
            print(f"player1得到了{get_tolls(self.local_name, LV)}元")
            pop = wlocal.pop(self.local) + 3#奖励参数
            wlocal.insert(self.local, pop)

            print(wlocal)
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
        print(f"{self.name}(有{self.money}元)走了{dicenum}步至{self.local_name}({get_buycost(self.local_name)})")
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
            time.sleep(0.5)
        if self.canmove == True:
            self.run()
            if self.local_name == "所得税":
                self.money -= 2000
                print(f"你失去了2000元")
            if self.local_name == "财产税":
                self.money -= 1000
                print(f"你失去了2000元")
            # if self.name == "player1":
            if owner[self.local] != "":
                if self.name == "player1" and owner[self.local] != self.name:
                    self.tolls(player2)
                if self.name == "player2" and owner[self.local] != self.name:
                    self.tolls(player1)
            else:
                self.input()
        print("")#分割块
    # def getLv(self,Player):
    #     for (local_name, Lv) in Player.haven_place:
    #         if local_name == self.local_name:
    #             return Lv
    def getHavenplace(self):
        return self.haven_list


typ1 = "human"
type = input("1p|2p?")
if type == "1p":
    type = "robot"
if type == "2p":
    type = "human"
if type == "0p":
    type = "robot"
    typ1 = "robot"
player1 = Player("player1",typ1)
player2 = Player("player2",type)
#主循环
a=1#局数
while True:
    player1.move()
    if player1.money < 0:
        player2.money = 0
        print(f"player2({a}) win!")
        a+=1
        player1.money += 100*a
        print(f"player1 +{100*a}")
        i=0
        for own in owner :
            if  own == "player1":
                pop = wlocal.pop(i) -1
                wlocal.insert(i,pop)

            i += 1
        print(wlocal)
        time.sleep(5)
        # break
    player2.move()
    if player2.money < 0:
        player1.money = 0
        print(f"player1({a}) win!")
        a+=1
        player2.money += 100*a
        print(f"player2 +{100*a}")
        i = 0
        for own in owner:
            if own == "player2":
                pop = wlocal.pop(i) - 1
                wlocal.insert(i, pop)

            i += 1
        print(wlocal)
        time.sleep(5)
        # break
