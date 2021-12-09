## Mitchell Navon
## Cs 120
## 11/22/2021
## @Mnavon@clarku.edu
import random
import json
import sys

class npc:
    
    def __init__(self, allignment, lvl, name):
        self.allignmentnumber=allignment
        self.lvl=lvl
        self.name=name
        if allignment>=5:
            self.allignmenttype='Good'
        elif 5>allignment>0:
            self.allignmenttype='Neutral Good'
        elif allignment==0:
            self.allignmenttype='Neutral'
        elif 0>allignment>-5:
            self.allignmenttype='Neural Evil'
        elif allignment<-5:
            self.allignmenttype='Evil'
    def __repr__(self):
        s=''
        s+=self.name+'\n'
        s+='Allignment: '+self.allignmenttype+'\n'
        s+='Level '+str(self.lvl)+'\n'
        return s
    
class mikeorike(npc):
    def __init__(self, allignment, lvl, name):
        super().__init__(allignment, lvl, name)
        
class goblin(npc):
    def __init__(self, allignment, lvl, relation):
        name='Goblin Emmisary'
        self.playerrelation=relation
        super().__init__(allignment, lvl, name)
    def player_interact_update(self,var):
        ##work on after outershell
        if self.playerrelation==0 and var==1:
            print('You have unlocked the goblin emmisary in town')
            self.playerrelation+=var
        elif self.playerrelation>0 and var==1:
            self.playerrelation+=var
        elif self.playerrelation>=0 and var==0:
            print('The goblin emmisary has noticed your actions! The goblins that you have befreinded will no longer like you!')
            self.playerrelation=0
    def __repr__(self):
        s=''
        s+='Relation='+str(self.playerrelation)+'\n'
        s+=self.name+'\n'
        s+='Allignment: '+self.allignmenttype+'\n'
        s+='Level '+str(self.lvl)+'\n'
        return s

class dragon(npc):
    def __init__(self, allignment, lvl, relation):
        name='Dragon'
        self.playerrelation=relation
        super().__init__(allignment, lvl, name)
    def player_interact_update(self,var):
        ##work on after outershell
        if self.playerrelation==0 and var==1:
            print('You have unlocked the dragon emmisary in town')
            self.playerrelation+=var
        elif self.playerrelation>0 and var==1:
            self.playerrelation+=var
        elif self.playerrelation>=0 and var==0:
            print('The dragon emmisary has noticed your actions! The dragons that you have befreinded will no longer like you!')
            self.playerrelation=0
        
class pc:
    def __init__(self, name, allignment, lvl, exp):
        self.name=name
        self.allignment=allignment
        self.lvl=lvl
        self.exp=exp
        self.itemequip=0
        self.baseitem='None'
        self.baseitemst=0
        self.power=0
        self.allignmenttype=''
        self.allignmentstrupdate()
    def __repr__(self):
        s=''
        s+=self.name+'\n'
        s+='Allignment: '+str(self.allignment)+' '+self.allignmenttype+'\n'
        s+='Level: '+str(self.lvl)+'\n'
        s+='Power:'+str(self.power)
        return s
    def allignmentstrupdate(self):
        if self.allignment>=5:
            self.allignmenttype='Good'
        elif 5>self.allignment>0:
            self.allignmenttype='Neutral Good'
        elif self.allignment==0:
            self.allignmenttype='Neutral'
        elif 0>self.allignment>-5:
            self.allignmenttype='Neural Evil'
        elif self.allignment<-5:
            self.allignmenttype='Evil'
    
    def Good_bad_allignment(self, variable):
        if variable!=0:
            self.allignment+=variable
        elif variable==0:
            self.allignment=0
        self.allignmentstrupdate()
        if self.allignment>=100:
            print('Mike wants to speak with you in town')
        elif self.allignment<=-100:
            print('Ike wants to speak with you in town')

    def next_level(self, newexperience):
        lvlupexperience=self.lvl*2
        self.exp+=newexperience
        while self.exp>=lvlupexperience:
            self.lvl+=1
            self.power+=10000
            print('Lvl up')
            self.exp-=lvlupexperience
        
    def equip_baseitem(self, bi):
        if bi==1:
            self.baseitem='Sword of Truth'
            self.baseitemst=2.5
            self.power=self.baseitemst
        elif bi==2:
            self.baseitem='Spear of Deceit'
            self.baseitemst=3
            self.power=self.baseitemst
    
    def equip_item(self, itemstat):
        if self.baseitem=='Sword of Truth':
            self.power+=(itemstat*1.5)
        elif self.baseitem=='Spear of Deceit':
            self.power+=(itemstat*1.8)
            
        
def questgiver(name, q):
    if 'Mike' in name.__repr__():
        i=random.randrange(0,5)
        x=0
        if i==0:
            print('Befreind a goblin\nReward: 20 exp\nAccept=1 Decline=2')
            while True:
                x=input('')
                x=int(x)
                if x==1 or x==2:
                    break
                else:
                    print('invalid input')
            if x==1:
                print('Accepted Quest')
                q.add_quest(i)
                return
            else:
                print("Declined Quset")
                return
        if i==1:
            print('Collect a flower\nReward: 5 exp\nAccept=1 Decline=2')
            while True:
                x=input('')
                x=int(x)
                if x==1 or x==2:
                    break
                else:
                    print('invalid input')
            if x==1:
                print('Accepted Quest')
                q.add_quest(i)
                return
            else:
                print("Declined Quset")
                return
        if i==2:
            print('Slay a Demon\nReward: 50 exp\nAccept=1 Decline=2')
            while True:
                x=input('')
                x=int(x)
                if x==1 or x==2:
                    break
                else:
                    print('invalid input')
            if x==1:
                print('Accepted Quest')
                q.add_quest(i)
                return
            else:
                print("Declined Quset")
                return
        if i==3:
            print('Gather firewood\nReward: 10 exp\nAccept=1 Decline=2')
            while True:
                x=input('')
                x=int(x)
                if x==1 or x==2:
                    break
                else:
                    print('invalid input')
            if x==1:
                print('Accepted Quest')
                q.add_quest(i)
                return
            else:
                print("Declined Quset")
                return
        if i==4:
            print('Befreind a dragon\nReward:100 exp\nAccept=1 Decline=2')
            while True:
                x=input('')
                x=int(x)
                if x==1 or x==2:
                    break
                else:
                    print('invalid input')
            if x==1:
                print('Accepted Quest')
                q.add_quest(i)
                return
            else:
                print("Declined Quset")
                return
    elif 'Ike' in name.__repr__():
        print('Slay a Goblin\n Reward: Powerful Equipment\nAccept=1 Decline=2')
        while True:
            x=input('')
            x=int(x)
            if x==1 or x==2:
                break
            else:
                print('invalid input')
        if x==1:
            print('Accepted Quest')
            q.add_quest(5)
            return
        else:
            print("Declined Quset")
            return
        
class questlist:
    def __init__(self):
        self.list=[]
    def add_quest(self, quest):
        if quest==0:
            self.list+=['Befreind a Goblin']
        elif quest==1:
            self.list+=['Collect a Flower']
        elif quest==2:
            self.list+=['Slay a Demon']
        elif quest==3:
            self.list+=['Gather Firewood']
        elif quest==4:
            self.list+=['Befreind a Dragon']
        elif quest==5:
            self.list+=['Slay a Goblin']
        elif quest==6:
            self.list+=['Defeat Ike']
        elif quest==7:
            self.list+=['Defeat Mike']
    def __repr__(self):
        if len(self.list)==0:
            return 'You have no quests at this time'
        else:
            s=''
            for i in range(len(self.list)):
                s+=self.list[i]+'\n'
            return s
    def remove_quest(self, i):
        del self.list[i]
        return
    def load_from_save(self,li):
        li=li.replace("[",'')
        li=li.replace("'",'')
        li=li.replace("]",'')
        if li=='':
            pass
        else:
            li2=list(li.split(','))
            self.list+=li2

def is_quest_comp(a,qlist,p):
    if a==0:
        for i in range(len(qlist.list)):
            if 'Befreind a Goblin' in qlist.list[i]:
                qlist.remove_quest(i)
                print('You completed a quest! Gained 20 exp')
                p.next_level(20)
                break
            else:
                pass
    elif a==1:
        for i in range(len(qlist.list)):
            if 'Collect a Flower' in qlist.list[i]:
                qlist.remove_quest(i)
                print('You completed a quest! Gained 5 exp')
                p.next_level(5)
                break
            else:
                pass
    elif a==2:
        for i in range(len(qlist.list)):
            if 'Slay a Demon' in qlist.list[i]:
                qlist.remove_quest(i)
                print('You completed a quest! Gained 50 exp')
                p.next_level(50)
                break
            else:
                pass
    elif a==3:
        for i in range(len(qlist.list)):
            if 'Gather Firewood' in qlist.list[i]:
                qlist.remove_quest(i)
                print('You completed a quest! Gained 10 exp')
                p.next_level(10)
                break
            else:
                pass
    elif a==4:
        for i in range(len(qlist.list)):
            if 'Befreind a Dragon' in qlist.list[i]:
                qlist.remove_quest(i)
                print('You completed a quest! Gained 100 exp')
                p.next_level(100)
                break
            else:
                pass
    elif a==5:
        for i in range(len(qlist.list)):
            if 'Slay a Goblin' in qlist.list[i]:
                qlist.remove_quest(i)
                print('You completed a quest! Gained Precious Sword Power(6)')
                p.equip_item(6)
                break
            else:
                pass
    elif a==6:
        for i in range(len(qlist.list)):
            if 'Defeat Ike' in qlist.list[i]:
                qlist.remove_quest(i)
                print('You have completed the Final Quest!')
                break
            else:
                pass
    elif a==7:
        for i in range(len(qlist.list)):
            if 'Defeat Mike' in qlist.list[i]:
                qlist.remove_quest(i)
                print('You have completed the Final Quest')
                break
            else:
                pass
            
def save_function(p,l,g,d,sw,sp,mend,iend,qlist):
    z=0
    with open('gamesave.json') as file:
        data=json.load(file)
        li=[p.name,p.lvl,p.exp,p.power,p.allignment,p.baseitem,l,g.playerrelation,d.playerrelation,sw,sp,mend,iend,str(qlist.list)]
        for v in range(len(data)):
            v1=str(v)
            if p.name in data[v1]:
                data[v]=li
                z+=1
        if z==0:
            v+=1
            v1=str(v)
            data[v1]=li
    with open('gamesave.json','w') as file:
        json.dump(data,file)
def game_run():
    print("New Game?\nEnter 1\nLoad Save?\nEnter 2")
    while True:
        q=input('')
        q=int(q)
        if q==1 or q==2:
            break
        else:
            print('invalid input')
    if q==1:
        uq1=0
        uq2=0
        sp=0
        sw=0
        mend=0
        iend=0
        qlist=questlist()
        g=goblin(0,3,0)
        d=dragon(4,60,0)
        print('Enter a name for your character')
        q=input('')
        p=pc(q,0,1,0)
        print('Welcome to the land of Fake Earth\nYou have been summoned to end a dispute between two powerful lords: Mike and Ike.')
        print('Mike and Ike have been fighting for centuries to see who was better, and decided on a bet to finish their conflict')
        print('They have decided to summon a hero and vie for their loyalty to prove who is best')
        print('And that is where you come in. You are the hero who will decide the fate of Fake Earth')
        print('...')
        print('... ...')
        print("MIKE: You have awakened valient Hero!\nIKE: Move out of the way you blubbering idiot!\nHello there I'm Ike! Please excuse my fool of a brother for bothering yo so soon. I...")
        print("MIKE: Be quiet you devilish wretch!\nHello there Hero I am most sorry for bringing you to our land of Fake Earth, but there are urgent matters at hand.\nMy ... brother and I summoned you to help us settle a dispute.\nMe and my brother will give you quests.")
        print('IKE: And the person you follow more shall be the winner.\nNow I will be giving you wonderous items for completing my quest, whereas my brother will be giving you...\nMIKE: Experience!!! It might not seem like much but I promise you it will be worth it.')
        print('IKE: Now onto more improtant matters! You can travel this land freely, and I hope you do. We are currently in the town,\nwhere you may speek to my brother and I, and around here there is the despicable Flower Feilds, the Goblin Cave, and Mt.Ice,')
        print('MIKE: We both will also offer a unique starting weapons that power up based on items that you find out in the world (you will get the item of whomever you speak to first)')
        print("MIKE: Now I belive that is enough introduction to this world. Now go Hero, and Explore!!!")
        l=0
                
    elif q==2:
        print('Select a file')
        with open('gamesave.json') as file:
            da=json.load(file)
            for i in range(len(da)):
                i1=str(i)
                pl=da[i1]
                print("Enter",i,"For",pl[0])
        v=input('')
        l=da[v]
        p=pc(l[0],l[4],l[1],l[2])
        p.power=l[3]
        p.baseitem=l[5]
        g=goblin(0,3,l[7])
        d=dragon(4,60,l[8])
        sw=l[9]
        sp=l[10]
        mend=l[11]
        iend=l[12]
        qlist=questlist()
        qlist.load_from_save(l[13])
        l=int(l[6])
    
    mike=mikeorike(10,100,'Mike')
    ike=mikeorike(-10,100,'Ike')
    run=0
    while run==0:
        if l==0:
            print('\nLocation: Town')
            if g.playerrelation==0 and d.playerrelation==0:
                print("Speak to Mike?\nEnter 1\nSpeak to Ike?\nEnter 2\nTravel?\nEnter 3\nCheck Quests?\n Enter 4\nCheck Status?\nEnter 5\nSave and Quit?\nEnter 0")
            elif g.playerrelation>0 and d.playerrelation==0:
                print("Speak to Mike?\nEnter 1\nSpeak to Ike?\nEnter 2\nTravel?\nEnter 3\nCheck Quests?\n Enter 4\nCheck Status?\nEnter 5\nSpeak to Goblin Emmisary?\nEnter 6\nSave and Quit?\nEnter 0")
            elif g.playerrelation>0 and d.playerrelation>0:
                print("Speak to Mike?\nEnter 1\nSpeak to Ike?\nEnter 2\nTravel?\nEnter 3\nCheck Quests?\n Enter 4\nCheck Status?\nEnter 5\nSpeak to Goblin Emmisary?\nEnter 6\nSpeak to Dragon Emmisary?\nEnter 7\nSave and Quit?\nEnter 0")
            elif g.playerrelation==0 and d.playerrelation>0: 
                print("Speak to Mike?\nEnter 1\nSpeak to Ike?\nEnter 2\nTravel?\nEnter 3\nCheck Quests?\n Enter 4\nCheck Status?\nEnter 5\nSpeak to Dragon Emmisary?\nEnter 7\nSave and Quit?\nEnter 0")   
            while True:
                q=input('')
                q=int(q)
                if q==1 or q==2 or q==3 or q==4 or q==5 or q==6 or q==7 or q==0:
                    break
                else:
                    print('Invalid input')
            if q==1:
                uq1=0
                if mend==1:
                    print('Mike has left town. You must defeat him at the hill in Flower Feilds')
                    pass
                elif p.baseitem=='None':
                    print(mike,'\nMIKE: Here is a starting weapon. Would you like a quest?')
                    print('Gained Wooden Sword of Truth')
                    p.equip_baseitem(1)
                    print('Enter 1 for yes\nEnter 2 for no')
                elif p.allignment>=100 and iend==0:
                    if p.baseitem=='Sword of Truth' and sw==1:
                        print(mike,'MIKE: I see that you have Excaliber. I belive that it is time that we settled my score with Ike')
                        print('Will you undergo my ultimate quest?')
                        uq1=1
                        print('Enter 1 for yes\nEnter 2 for no\n')
                    elif p.baseitem=='Sword of Truth' and sw==0:
                        print(mike,'MIKE: Come back to me when you have found Excaliber')
                        print('In the meantime, would you like a regular quest?')
                        print('Enter 1 for yes\nEnter 2 for no\n')
                    elif p.baseitem=='Spear of Deceit' and sp==1:
                        print(mike,'MIKE: I see that you have Gungir. I belive that it is time that we settled my score with Ike')
                        print('Will you undergo my ultimate quest?')
                        uq1=1
                        print('Enter 1 for yes\nEnter 2 for no\n')
                    elif p.baseitem=='Spear of Deceit' and sp==0:
                        print(mike,'MIKE: Come back to me when you have found Gungir')
                        print('In the meantime, would you like a regular quest?')
                        print('Enter 1 for yes\nEnter 2 for no\n')
                else:
                    print(mike,'\nWould you like a quest?')
                    print('Enter 1 for yes\nEnter 2 for no\n')
                while True:
                    if mend==1:
                        break
                    q=input('')
                    q=int(q)
                    if q==1 or q==2:
                        break
                    else:
                        print('Invalid input')
                if q==1 and uq1==0 and mend==0:
                    questgiver(mike,qlist)
                elif q==2 and uq1==0 and mend==0:
                    print('MIKE: See you later!')
                elif q==1 and uq1==1:
                    print('Ultimate Quest: Defeat Ike Has Been Accepted')
                    iend=1
                    qlist.add_quest(6)
                    print(ike,'IKE: I see that you have made your choice!\nMeet me at the top of Mt. Ice!')
                elif q==2 and uq1==1:
                    print('MIKE: Would you rather take a regular quest?')
                    print('Enter 1 for yes\nEnter 2 for no\n')
                    while True:
                        q=input('')
                        q=int(q)
                        if q==1 or q==2:
                            break
                        else:
                            print('Invalid input')
                    if q==1:
                        questgiver(mike,qlist)
                    elif q==2:
                        print('MIKE: See you later!')
                    
            elif q==2:
                uq2=0
                if iend==1:
                    print('Ike has left town. You must defeat him at the top of Mt. Ice')
                    pass
                elif p.baseitem=='None':
                    print(ike,'\nIKE: Here is a starting weapon. Would you like a quest?')
                    print('Gained Wooden Spear of Deceit')
                    p.equip_baseitem(2)
                    print('Enter 1 for yes\nEnter 2 for no')
                elif p.allignment<=-100 and mend==0:
                    if p.baseitem=='Sword of Truth' and sw==1:
                        print(ike,'IKE: I see that you have Excaliber. I belive that it is time that we settled my score with Mike')
                        print('Will you undergo my ultimate quest?')
                        uq2=1
                        print('Enter 1 for yes\nEnter 2 for no\n')
                    elif p.baseitem=='Sword of Truth' and sw==0:
                        print(ike,'IKE: Come back to me when you have found Excaliber')
                        print('In the meantime, would you like a regular quest?')
                        print('Enter 1 for yes\nEnter 2 for no\n')
                    elif p.baseitem=='Spear of Deceit' and sp==1:
                        print(ike,'MIKE: I see that you have Gungir. I belive that it is time that we settled my score with Mike')
                        print('Will you undergo my ultimate quest?')
                        uq2=1
                        print('Enter 1 for yes\nEnter 2 for no\n')
                    elif p.baseitem=='Spear of Deceit' and sp==0:
                        print(ike,'MIKE: Come back to me when you have found Gungir')
                        print('In the meantime, would you like a regular quest?')
                        print('Enter 1 for yes\nEnter 2 for no\n')
                elif iend==0:
                    print(ike,'\nWould you like a quest?')
                    print('Enter 1 for yes\nEnter 2 for no\n')
                while True:
                    if iend==1:
                        break
                    q=input('')
                    q=int(q)
                    if q==1 or q==2:
                        break
                    else:
                        print('Invalid input')
                if q==1 and uq2==0 and iend==0:
                    questgiver(ike,qlist)
                elif q==2 and uq2==0 and iend==0:
                    print('IKE: Come back soon!')
                elif q==1 and uq2==1:
                    print('Ultimate Quest: Defeat Mike Has Been Accepted')
                    mend=1
                    qlist.add_quest(7)
                    print(mike,'MIKE: I see that you have made your choice!\nMeet me at the hill in Flower Feilds!')
                elif q==2 and uq2==1:
                    print('IKE: Would you rather take a regular quest?')
                    print('Enter 1 for yes\nEnter 2 for no\n')
                    while True:
                        q=input('')
                        q=int(q)
                        if q==1 or q==2:
                            break
                        else:
                            print('Invalid input')
                    if q==1:
                        questgiver(ike,qlist)
                    elif q==2:
                        print('IKE: Come back soon!!')
            elif q==3:
                print('Where would you like to travel?\nEnter 1 for Flower Feilds\nEnter 2 for Goblin Cave\nEnter 3 for Mt. Ice')
                while True:
                    q=input('')
                    q=int(q)
                    if q==1 or q==2 or q==3:
                        break
                    else:
                        print('Invalid input')
                if q==1:
                    l=1
                elif q==2:
                    l=2
                elif q==3:
                    l=3
            elif q==4:
                print(qlist)
            elif q==5:
                print(p)
            elif q==6:
                if g.playerrelation==0:
                    print('This option has not been unlocked yet')
                else:
                    print(g,'GOBLIN: Hello! I hope you continue to keep good relations with us Goblins. We will help you in your greatest hour of need!')
            elif q==7:
                if d.playerrelation==0:
                    print('This option has not been unlocked yet')
                else:
                    print(d,'DRAGON: Greetings! I hope you continue to keep good relations with us Dragons. We will help you in your greatest hour of need!')
            elif q==0:
                save_function(p,l,g,d,sw,sp,mend,iend,qlist)
                run=1
                    
        elif l==1:
            print('\nLocation: Flower Feilds')
            
            print('Pick a Daisy?\n Enter 1\nWander around?\nEnter 2\nTravel?\n Enter 3\nCheck Quests?\nEnter 4\nCheck Status?\nEnter 5\nHead to Small Hill?\n Enter 6\nSave and Quit?\nEnter 0')
            while True:
                    q=input('')
                    q=int(q)
                    if q==1 or q==2 or q==3 or q==4 or q==5 or q==6 or q==0:
                        break
                    else:
                        print('Invalid input')
            if q==1:
                print('You picked a Daisy, your allignment went up by 1')
                p.Good_bad_allignment(1)
                is_quest_comp(1,qlist,p)
            elif q==2:
                x=random.randrange(0,99)
                if x>=0 and x<=63:
                    print('You came across a Slime!\n Slime:\n Defense 3')
                    print('Slay the slime?\nEnter 1\nRun?\nEnter 2')
                    while True:
                        q=input('')
                        q=int(q)
                        if q==1:
                            if p.power>3:
                                print('You slayed the Slime!\nGained 5 exp')
                                p.next_level(5)
                                break
                            elif p.power<3:
                                print('The Slime was not effected')
                        elif q==2:
                            print('You ran away\nGained 1 exp')
                            p.next_level(1)
                            break
                        else:
                            print('Invalid input')
                elif x>63 and x<=99:
                    print('You found a chest\nYou opened it and found a Rusty Sword power(4)')
                    p.equip_item(4)
            elif q==3:
                print('Where would you like to travel?\nEnter 1 for Town\nEnter 2 for Goblin Cave\nEnter 3 for Mt. Ice')
                while True:
                    q=input('')
                    q=int(q)
                    if q==1 or q==2 or q==3:
                        break
                    else:
                        print('Invalid input')
                if q==1:
                    l=0
                elif q==2:
                    l=2
                elif q==3:
                    l=3
            elif q==4:
                print(qlist)
            elif q==5:
                print(p)
            elif q==6:
                print('You stand on a hill surounded by beutiful flowers. The sky is calm here.')
                print('In the middle of the hill is a boulder')
                if sw==0 and mend==0:
                    print('In the boulder lies the legendary sword Excaliber! Pick it up?\nEnter 1 for yes\nEnter 2 for no')
                    while True:
                        q=input('')
                        q=int(q)
                        if q==1 or q==2:
                            break
                        else:
                            print('Invalid input')
                    if q==1:
                        if p.baseitem=='None':
                            print('VOICE FROM ABOVE: You Must Make Your Choice!!!')
                        if p.allignment>=100 and p.baseitem=='Sword of Truth':
                            print('VOICE FROM ABOVE: You Are Worthy!!!')
                            print('You picked Excaliber up!')
                            p.equip_item(10500)
                            sw+=1
                        elif p.allignment<100 and p.baseitem=='Sword of Truth':
                            print('VOICE FROM ABOVE: You Are Not Worthy Yet!!!')
                            print('You attempted to pick up Excaliber, but it was too heavy')
                        elif p.baseitem=='Spear of Deceit':
                            print('VOICE FROM ABOVE: You Will Never Be Worthy')
                            print('You attempted to pick up Excaliber but it singed your hand')
                    elif q==2:
                        print("It is best to leave legendary swords alone isn't it")
                elif sw==1 and mend==0:
                    pass
                elif sw==1 and mend==1:
                    print('MIKE: I see that you have my sword. I wish that it did not have to come to this ... En gaurd!')
                    mhealth=5000
                    mpower=750
                    mhost=10
                elif sw==0 and mend==1:
                    print('MIKE: I see that you have chosen the path of evil. (Mike draws Excaliber from the boulder) I wish that it did not have to come to this ... En gaurd!')
                    mhealth=10000
                    mpower=1500
                    mhost=10
                if mend==1:
                    print('You are challenged by Mike\nDefense: 1000\nPower:',mpower,'\nHealth:',mhealth,'\nHostility: 10')
                    health=p.power//2
                    attack=p.power//1.5
                    if g.playerrelation>0:
                        print('The Goblins that you have befreinded have come to help you')
                        o=g.playerrelation
                        o*=100
                        health+=o
                        attack+=o
                    if d.playerrelation>0:
                        print('The Dragons that you have befreinded have come to help you')
                        z=d.playerrelation
                        z*=1000
                        health+=z
                        attack+=z
                    while True:
                        print("Health:",health, 'Attack:',attack,"Mike's Health:",mhealth,"Mike's Hostility:",mhost)
                        print('Attack Mike?\nEnter 1\nAttempt to Passify Mike?\nEnter 2\nRun?\nEnter 3')
                        while True:
                            q=input('')
                            q=int(q)
                            if q==1 or q==2 or q==3:
                                break
                            else:
                                print('Invalid input')
                        if q==1:
                            if p.power>1000:
                                print('You attacked Mike')
                                mhealth-=attack
                                if mhealth<=0:
                                    break
                            elif p.power<1000:
                                print('Mike was not effected')
                        elif q==2:
                            print('You attempted to passify Mike')
                            mhost-=1
                            if mhost==0:
                                break
                        elif q==3:
                            print('MiKE: No Running Away!')
                        print("Mike attacked you")
                        health-=mpower
                        if health<=0:
                            break
                    if health<=0:
                        print('You whited out\nYou woke up in town')
                        l=0
                    elif mhealth<=0:
                        is_quest_comp(7,qlist,p)
                        print('MiKE: I never thought that you would slay me ...\nI thought I was good to you ...\n... ...\n... ... ...\n')
                        print('IKE: Finally, the deed is done. But alas hero ... You have completed the ultimate quest.')
                        print('Congradulations.\n...\n... ...\n... ... ...\nYou brought chaos to Fake Earth.')
                        print('The game will close. When you next open this save you will have the stats that you have completed this game with, but you will not have started the ultimate quest.')
                        print('Have peace Hero. You can change your choices.')
                        is_quest_comp(7,qlist,p)
                        mend=0
                        save_function(p,l,g,d,sw,sp,mend,iend,qlist)
                        run=1
                    elif mhost==0:
                        print("MIKE: What is the point anymore. You wont fight me.\nI guess you never wanted to do this.\nI'm sorry for summoning you, Its just... my brother is tought to deal with.\n...\n... ...\nWill you be my freind?")
                        print('Enter 1 for yes\nEnter 2 for no')
                        while True:
                            q=input('')
                            q=int(q)
                            if q==1 or q==2:
                                break
                            else:
                                print('Invalid input')
                        if q==1:
                            print('MIKE: Thank you')
                        if q==2:
                            print('MIKE: I understand')
                        print('IKE: You Idiot!\n You were supposed to kill him\nMIKE: Leave him to me, I will try to make ammends with him')
                        print('Congradulations!\nYou brought ??? to Fake Earth!')
                        print('The game will close. When you next open this save you will have the stats that you have completed this game with, but you will not have started the ultimate quest.')
                        print('Have peace Hero. You can change your choices.')
                        is_quest_comp(7,qlist,p)
                        mend=0
                        save_function(p,l,g,d,sw,sp,mend,iend,qlist)
                        run=1
            elif q==0:
                save_function(p,l,g,d,sw,sp,mend,iend,qlist)
                run=1
        elif l==2:
            print('\nLocation: Goblin Cave')
            
            print('Pick up a Gem of Neutrality\n Enter 1\nWander around?\nEnter 2\nTravel?\nEnter 3\nCheck Quests?\nEnter 4\nCheck Status?\nEnter 5\nSave and Quit?\nEnter 0')
            while True:
                q=input('')
                q=int(q)
                if q==1 or q==2 or q==3 or q==4 or q==5 or q==0:
                    break
                else:
                    print('Invalid input')
            if q==1:
                print('You picked a gem of neutrality, your allignment went back to 0')
                p.Good_bad_allignment(0)
            if q==2:
                x=random.randrange(0,99)
                if x>=0 and x<25:
                    print('You came across a Goblin!\nDefense: 10\nPower: 10\nHealth: 15\nHostility: 3')
                    ghealth=15
                    gattack=10
                    ghost=3
                    health=p.power//2
                    attack=p.power//1.5
                    while True:
                        print('Health:',health, 'Attack:',attack,'Goblin Health:',ghealth,'Goblin Hostility:',ghost)
                        print('Attack the Goblin?\nEnter 1\nGive the Goblin a treat?\nEnter 2\nRun?\nEnter 3')
                        while True:
                            q=input('')
                            q=int(q)
                            if q==1 or q==2 or q==3:
                                break
                            else:
                                print('Invalid input')
                        if q==1:
                            if p.power>10:
                                print('You attacked the Goblin')
                                ghealth-=attack
                                if ghealth<=0:
                                    break
                            elif p.power<10:
                                print('The Goblin was not effected')
                        elif q==2:
                            print('You attempted to passify the goblin')
                            ghost-=1
                            if ghost==0:
                                break
                        elif q==3:
                            print('You ran away\nGained 1 exp')
                            p.next_level(1)
                            break
                        print("The Goblin attacked you")
                        health-=gattack
                        if health<=0:
                            break
                    if health<=0:
                        print('You whited out\nYou woke up in town')
                        l=0
                    elif ghealth<=0:
                        print('You slayed the Goblin\nYou gained 10 exp\nYour allignment went down by five')
                        if g.playerrelation>0:
                            g.player_interact_update(0)
                        p.Good_bad_allignment(-5)
                        is_quest_comp(5,qlist,p)
                        p.next_level(10)
                    elif ghost==0:
                        print('You befreinded the Goblin\nYou gained 10 exp\nYour allignment went up by five')
                        g.player_interact_update(1)
                        p.Good_bad_allignment(5)
                        is_quest_comp(0,qlist,p)
                        p.next_level(10)
                elif x>=25 and x<=99:
                    print('You found a chest\nYou opened it and found a Sharp Sword power(10)')
                    p.equip_item(6)
            elif q==3:
                print('Where would you like to travel?\nEnter 1 for Town\nEnter 2 for Flower Feilds\nEnter 3 for Mt. Ice')
                while True:
                    q=input('')
                    q=int(q)
                    if q==1 or q==2 or q==3:
                        break
                    else:
                        print('Invalid input')
                if q==1:
                    l=0
                elif q==2:
                    l=1
                elif q==3:
                    l=3
            elif q==4:
                print(qlist)
            elif q==5:
                print(p)
            elif q==0:
                save_function(p,l,g,d,sw,sp,mend,iend,qlist)
                run=1
        elif l==3:
            print('\nLocation: Mt. Ice')
            
            print('Pick up a Thorned Rose\n Enter 1\nWander around?\nEnter 2\nTravel?\nEnter 3\nCheck Quests?\nEnter 4\nCheck Status?\nEnter 5\nGather Firewood?\nEnter 6\nHead to Peak?\nEnter 7\nSave and Quit?\nEnter 0')
            while True:
                q=input('')
                q=int(q)
                if q==1 or q==2 or q==3 or q==4 or q==5 or q==6 or q==7 or q==0:
                    break
                else:
                    print('Invalid input')
            if q==1:
                print('You picked a thorned rose, your allignment went down by 1')
                p.Good_bad_allignment(-1)
                is_quest_comp(1,qlist,p)
            if q==2:
                x=random.randrange(0,99)
                if x>=0 and x<50:
                    print('You came across a Demon!\nDefense: 500\nPower: 300\nHealth: 800')
                    dehealth=800
                    deattack=300
                    health=p.power//2
                    attack=p.power//1.5
                    while True:
                        print('Health:',health, 'Attack:',attack,'Demon Health:',dehealth)
                        print('Attack the Demon?\nEnter 1\nRun?\nEnter 2')
                        while True:
                            q=input('')
                            q=int(q)
                            if q==1 or q==2:
                                break
                            else:
                                print('Invalid input')
                        if q==1:
                            if p.power>500:
                                print('You attacked the Demon')
                                dehealth-=attack
                                if dehealth<=0:
                                    break
                            elif p.power<500:
                                print('The Demon was not effected')
                        elif q==2:
                            print('You ran away\nGained 10 exp')
                            p.next_level(10)
                            break
                        print("The Demon attacked you")
                        health-=deattack
                        if health<=0:
                            break
                    if health<=0:
                        print('You whited out\nYou woke up in town')
                        l=0
                    elif dehealth<=0:
                        print('You slayed the Demon\nYou gained 100 exp\nYour allignment went up by 10')
                        p.Good_bad_allignment(10)
                        is_quest_comp(2,qlist,p)
                        p.next_level(100)
                elif x>=50 and x<90:
                    print('You found a chest\nYou opened it and found a Pristine Sword power(20)')
                    p.equip_item(6)
                elif x>=90 and x<=99:
                    print('You came across a Dragon!\nDefense: 800\nPower: 500\nHealth: 1500\nHostility: 10')
                    dhealth=1500
                    dattack=500
                    dhost=10
                    health=p.power//2
                    attack=p.power//1.5
                    while True:
                        print('Health:',health,'Attack:',attack,'Dragon Health:',dhealth,'Dragon Hostility:',dhost)
                        print('Attack the Dragon?\nEnter 1\nGive the Dragon a treat?\nEnter 2\nRun?\nEnter 3')
                        while True:
                            q=input('')
                            q=int(q)
                            if q==1 or q==2 or q==3:
                                break
                            else:
                                print('Invalid input')
                        if q==1:
                            if p.power>800:
                                print('You attacked the Dragon')
                                dhealth-=attack
                                if dhealth<=0:
                                    break
                            elif p.power<800:
                                print('The Dragon was not effected')
                        elif q==2:
                            print('You attempted to passify the Dragon')
                            dhost-=1
                            if dhost==0:
                                break
                        elif q==3:
                            print('You ran away\nGained 50 exp')
                            p.next_level(50)
                            break
                        print("The Dragon attacked you")
                        health-=dattack
                        if health<=0:
                            break
                    if health<=0:
                        print('You whited out\nYou woke up in town')
                        l=0
                    elif dhealth<=0:
                        print('You slayed the Dragon\nYou gained 500 exp\nYour allignment went down by ten')
                        if d.playerrelation>0:
                            d.player_interact_update(0)
                        p.Good_bad_allignment(-10)
                        p.next_level(500)
                    elif dhost==0:
                        print('You befreinded the Dragon\nYou gained 500 exp\nYour allignment went up by ten')
                        d.player_interact_update(1)
                        p.Good_bad_allignment(10)
                        is_quest_comp(4,qlist,p)
                        p.next_level(500)
                    
            elif q==3:
                print('Where would you like to travel?\nEnter 1 for Town\nEnter 2 for Flower Feilds\nEnter 3 for Goblin Cave')
                while True:
                    q=input('')
                    q=int(q)
                    if q==1 or q==2 or q==3:
                        break
                    else:
                        print('Invalid input')
                if q==1:
                    l=0
                elif q==2:
                    l=1
                elif q==3:
                    l=2
            elif q==4:
                print(qlist)
            elif q==5:
                print(p)
            elif q==6:
                print('You Gathered Firewood')
                is_quest_comp(3,qlist,p)
            elif q==7:
                print('You reach the top of Mt. Ice after a long journey. The peak is snowy, serene and quiet. The sky is cloudy, and fresh snow falls around you')
                print('In the middle of the peak of Mt. Ice is a pillar of ice')
                if sp==0 and iend==0:
                    print('In the pillar of ice lies the legendary spear Gungnir! Pick it up?\nEnter 1 for yes\nEnter 2 for no')
                    while True:
                        q=input('')
                        q=int(q)
                        if q==1 or q==2:
                            break
                        else:
                            print('Invalid input')
                    if q==1:
                        if p.baseitem=='None':
                            print('VOICE FROM BELOW: You Must Make Your Choice!!!')
                        if p.allignment<=-100 and p.baseitem=='Spear of Deceit':
                            print('VOICE FROM Below: You Are Worthy!!!')
                            print('You picked Gungir up!')
                            p.equip_item(10500)
                            sp+=1
                        elif p.allignment>-10 and p.baseitem=='Spear of Deceit':
                            print('VOICE FROM BELOW: You Are Not Worthy Yet!!!')
                            print('You attempted to pick up Gungir, but it was too heavy')
                        elif p.baseitem=='Sword of Truth':
                            print('VOICE FROM BELOW: You Will Never Be Worthy')
                            print('You attempted to pick up Gungir but you nearly got frostbite')
                    elif q==2:
                        print("It is best to leave legendary spears alone isn't it")
                elif sp==1 and iend==0:
                    pass
                elif sp==1 and iend==1:
                    print(ike,'IKE: I see that you have my spear. I have been looking forward to this ... En gaurd!')
                    ihealth=3000
                    ipower=750
                    ihost=15
                elif sp==0 and iend==1:
                    print(ike,'IKE: I see that you have chosen the path of the weak. (Ike draws Gungir from the pillar of ice) I have been looking forward to this ... En gaurd!')
                    ihealth=5000
                    ipower=1500
                    ihost=15
                if iend==1:
                    print('You are challenged by Ike\nDefense: 1000\nPower:',ipower,'\nHealth:',ihealth,'\nHostility: 15')
                    health=p.power//2
                    attack=p.power//1.5
                    if g.playerrelation>0:
                        print('The Goblins that you have befreinded have come to help you')
                        o=g.playerrelation
                        o*=100
                        health+=o
                        attack+=o
                    if d.playerrelation>0:
                        print('The Dragons that you have befreinded have come to help you')
                        z=d.playerrelation
                        z*=1000
                        health+=z
                        attack+=z
                    while True:
                        print("Health:",health, 'Attack:',attack,"Ike's Health:",ihealth,"Ike's Hostility:",ihost)
                        print('Attack Ike?\nEnter 1\nAttempt to Passify Ike?\nEnter 2\nRun?\nEnter 3')
                        while True:
                            q=input('')
                            q=int(q)
                            if q==1 or q==2 or q==3:
                                break
                            else:
                                print('Invalid input')
                        if q==1:
                            if p.power>1000:
                                print('You attacked Ike')
                                ihealth-=attack
                                if ihealth<=0:
                                    break
                            elif p.power<1000:
                                print('Ike was not effected')
                        elif q==2:
                            print('You attempted to passify Ike')
                            ihost-=1
                            if ihost==0:
                                break
                        elif q==3:
                            print('IKE: No Running Away!')
                        print("Ike attacked you")
                        health-=ipower
                        if health<=0:
                            break
                    if health<=0:
                        print('You whited out\nYou woke up in town')
                        l=0
                    elif ihealth<=0:
                        is_quest_comp(6,qlist,p)
                        print('IKE: I never thought that you would slay me ...\nI wish that I could have changed my ways ...\n... ...\n... ... ...\n')
                        print('MIKE: I wish that it did not come to this. But alas hero ... You have completed the ultimate quest.')
                        print('Congradulations.\n...\n... ...\n... ... ...\nYou brought ??? to Fake Earth.')
                        print('The game will close. When you next open this save you will have the stats that you have completed this game with, but you will not have started the ultimate quest.')
                        print('Have peace Hero. You can change your choices.')
                        iend=0
                        is_quest_comp(6,qlist,p)
                        save_function(p,l,g,d,sw,sp,mend,iend,qlist)
                        run=1
                    elif ihost==0:
                        print('IKE: What is the point anymore. You wont fight me.\nI dont want to live like I do anymore.\nAll I ever wanted was for people to like me.\n...\n... ...\nWill you be my freind?')
                        print('Enter 1 for yes\nEnter 2 for no')
                        while True:
                            q=input('')
                            q=int(q)
                            if q==1 or q==2:
                                break
                            else:
                                print('Invalid input')
                        if q==1:
                            print('IKE: Thank you')
                        if q==2:
                            print('IKE: I understand')
                        print('MIKE: Thank you for saving my brother!\nWe will forever be greatful to you!')
                        print('Congradulations!\nYou brought peace to Fake Earth!')
                        print('The game will close. When you next open this save you will have the stats that you have completed this game with, but you will not have started the ultimate quest.')
                        print('Have peace Hero. You can change your choices.')
                        iend=0
                        is_quest_comp(6,qlist,p)
                        save_function(p,l,g,d,sw,sp,mend,iend,qlist)
                        run=1
            elif q==0:
                save_function(p,l,g,d,sw,sp,mend,iend,qlist)
                run=1
                        
game_run()