class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.in1 = None
        self.main_menu()

    def main_menu(self):
        self.in1 = input("Write action (buy, fill, take, remaining, exit): ")
        if self.in1 == "buy":
            self.buy()
        elif self.in1 == "fill":
            self.fill()
        elif self.in1 == "take":
            self.take()
        elif self.in1 == "remaining":
            self.remaining()
        elif self.in1 == "exit":
            return

    def buy(self):
        self.in1 = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if self.in1 == "1":
            self.espresso()
        elif self.in1 == "2":
            self.latte()
        elif self.in1 == "3":
            self.cappuccino()
        elif self.in1 == "back":
            self.main_menu()
        else:
            return

    def espresso(self):
        if self.water < 250:
            print("Sorry, not enough water!")
        elif self.milk < 0:
            print("Sorry, not enough milk!")
        elif self.beans < 16:
            print("Sorry, not enough beans!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.milk -= 0
            self.beans -= 16
            self.cups -= 1
            self.money += 4
        self.main_menu()

    def latte(self):
        if self.water < 350:
            print("Sorry, not enough water!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        elif self.beans < 20:
            print("Sorry, not enough beans!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
        self.main_menu()

    def cappuccino(self):
        if self.water < 200:
            print("Sorry, not enough water!")
        if self.milk < 100:
            print("Sorry, not enough milk!")
        if self.beans < 12:
            print("Sorry, not enough beans!")
        if self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
        self.main_menu()

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.beans += int(input("Write how many grams of coffee do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))
        self.main_menu()

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0
        self.main_menu()

    def remaining(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print(str(self.money) + " of money")
        self.main_menu()


CoffeeMachine()
