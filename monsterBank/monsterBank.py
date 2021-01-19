from random import randint
import math
import sys

#monster functions
monsterList = ["kobold", "goblin"]
monsterListStr = "Available monsters:\n" + "\n".join(monsterList)

def kobold():
    monName = "kobold"
    arCls = 14
    hitPoints = 14
    stren = 7
    dex = 15
    con = 12
    intel = 8
    wis = 8
    cha = 8
    attacks = ["dagger","javelin"]
    prof = 2
    #print("kobold has executed") #check if kobold has executed
    return monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof

#attack functions
def dagger(monName, rollType):
    prof = getProf(monName)
    dex = getDex(monName)
    dexMod = getMod(dex)
    arCls = arClsTarget()
    #print("dagger has executed") #check if dagger has executed
    attackRoll = makeAttackRoll(rollType)
        #attackRoll = 20 #critical roll test value
    if attackRoll == 20:
        damage = randint(1,4)+randint(1,4)+dexMod
        criticalAttack(damage)
    else:
        attackRoll = attackRoll + prof + dexMod
        if  attackRoll >= arCls:
            damage = randint(1,4)+dexMod
            attackHit(attackRoll, damage)
        else:
            attackMiss(attackRoll)

def javelin(monName, rollType):
    arClsTarget()
    print("javelin has executed")

#general functions
def monster():
    callMonster = ""
    while callMonster != True:
        monName = input("What monster do you want to use? ").lower()
        if monName in monsterList:
            callMonster = True
        else:
            print("Sorry, that monster does not exist. Valid monsters include:\n" + "\n".join(monsterList))
    return monName

def getMod(skill):
    modifier = math.floor((skill-10)/2)
    return modifier

def attack(monName):
    attacks = getAttacks(monName)
    print(", ".join(attacks))
    callAttackCheck = ""
    while callAttackCheck != True:
        callAttack = input("Which attack would you like to use?\n").lower()
        if callAttack in attacks: 
            callAttackCheck = True
        else:
            print("Sorry, this is not a valid attack for this monster.")
    rollType = input("Do you have advantage or disadvantage on this attack?\na = advantage\nd = disadvantage\nn = neither\n").lower()
    callAttackExecute = callAttack + "(monName, rollType)"
    eval(callAttackExecute)

def makeAttackRoll(rollType):
    if rollType == "n":
        attackRoll = randint(1,20)
    elif rollType == "a":
        print("\nThis attack was made with advantage.")
        attackRoll = advantage()
    elif rollType == "d":
        print("\nThis attack was made with disadvantage.")
        attackRoll = disadvantage()
    return attackRoll

def criticalAttack(damage):
    print(f"\nYou scored a critical hit! Your attack deals {damage} damage.")

def attackHit(attackRoll, damage):
    print(f"\nYour dagger attack hits with an attack roll of {attackRoll} and deals {damage} damage.")

def attackMiss(attackRoll):
    print(f"\nYour dagger attack misses with an attack roll of {attackRoll}.")

def advantage():
    attackRoll1 = randint(1,20)
    attackRoll2 = randint(1,20)
    print(f"Your first attack roll is {attackRoll1} and your second attack roll is {attackRoll2}.")
    if attackRoll1 >= attackRoll2:
        return attackRoll1
    else:
        return attackRoll2

def disadvantage():
    attackRoll1 = randint(1,20)
    attackRoll2 = randint(1,20)
    print(f"\nYour first attack roll is {attackRoll1} and your second attack roll is {attackRoll2}.")
    if attackRoll1 <= attackRoll2:
        return attackRoll1
    else:
        return attackRoll2

def defend(monName):
    arCls = getArCls(monName)
    attack = int(input("What was the opponent's attack roll? "))
    if attack >= arCls:
        print("The attack hits.")
    else:
        print("The attack does not hit.")

def arClsTarget():
    arClsTarget = int(input("What is the target's AC? "))
    return arClsTarget

def getArCls(monName):
    monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof = eval(monName + "()")
    return arCls

def getHitPoints(monName):
    monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof = eval(monName + "()")
    return hitPoints

def getstren(monName):
    monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof = eval(monName + "()")
    return stren

def getDex(monName):
    monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof = eval(monName + "()")
    return dex

def getCon(monName):
    monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof = eval(monName + "()")
    return con

def getIntel(monName):
    monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof = eval(monName + "()")
    return intel

def getWis(monName):
    monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof = eval(monName + "()")
    return wis

def getCha(monName):
    monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof = eval(monName + "()")
    return cha

def getAttacks(monName):
    monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof = eval(monName + "()")
    return attacks

def getProf(monName):
    monName, arCls, hitPoints, stren, dex, con, intel, wis, cha, attacks, prof = eval(monName + "()")
    return prof

print(monsterListStr) #print list of available monsters

monName = monster() #get monster's stats
actionType = input("Is this monster attacking or defending?\na = attacking\nd = defending\n").lower()
try:
    if actionType == "a":
        attack(monName)
    if actionType == "d":
        defend(monName)
except:
    raise
    #print("Sorry, that is not a valid answer.")
