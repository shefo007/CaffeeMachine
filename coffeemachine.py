class CoffeeMachine:

#sssss
    def __init__(self):

        self.supplies = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}
        self.action()

    def stock_sup(self, water_min=0, milk_min=0, beans_min=0, cups_min=0, money_add=0):
        self.supplies['water'] -= water_min
        self.supplies['milk'] -= milk_min
        self.supplies['beans'] -= beans_min
        self.supplies['cups'] -= cups_min
        self.supplies['money'] += money_add

    def buy(self, opt_buy):
        if opt_buy == '1':
            if self.supplies['water'] >= 250 and self.supplies['beans'] >= 16 and self.supplies['cups'] >= 1:
                print('I have enough resources, making you a coffee!')
                self.stock_sup(water_min=250, milk_min=0, beans_min=16, cups_min=1, money_add=4)

            else:
                if self.supplies['water'] < 250:
                    print("Sorry, not enough water!")
                elif self.supplies['beans'] < 16:
                    print('Sorry, not enough coffee beans!')
                elif self.supplies['cups'] < 1:
                    print('Sorry, not enough cups!')

        elif opt_buy == '2':
            if self.supplies['water'] >= 350 and self.supplies['milk'] >= 75 and self.supplies['beans'] >= 20 and \
                    self.supplies[
                        'cups'] >= 1:
                print('I have enough resources, making you a coffee!')
                self.stock_sup(water_min=350, milk_min=75, beans_min=20, cups_min=1, money_add=7)
            else:
                if self.supplies['water'] < 350:
                    print("Sorry, not enough water!")
                elif self.supplies['beans'] < 20:
                    print('Sorry, not enough coffee beans!')
                elif self.supplies['milk'] < 75:
                    print("Sorry, not enough milk!")
                elif self.supplies['cups'] < 1:
                    print('Sorry, not enough cups!')

        elif opt_buy == '3':
            if self.supplies['water'] >= 200 and self.supplies['milk'] >= 100 and self.supplies['beans'] >= 12 and \
                    self.supplies[
                        'cups'] >= 1:
                print('I have enough resources, making you a coffee!')
                self.stock_sup(water_min=200, milk_min=100, beans_min=12, cups_min=1, money_add=6)
            else:
                if self.supplies['water'] < 200:
                    print("Sorry, not enough water!")
                elif self.supplies['beans'] < 12:
                    print('Sorry, not enough coffee beans!')
                elif self.supplies['milk'] < 100:
                    print("Sorry, not enough milk!")
                elif self.supplies['cups'] < 1:
                    print('Sorry, not enough cups!')
        elif opt_buy == 'back':
            print()
            self.action()

    def remaining(self):
        print(f"""The coffee machine has:
{self.supplies['water']} of water
{self.supplies['milk']} of milk
{self.supplies['beans']} of coffee beans
{self.supplies['cups']} of disposable cups
${self.supplies['money']} of money""")

    def fill(self):
        self.supplies['water'] += int(input("Write how many ml of water do you want to add: \n"))
        self.supplies['milk'] += int(input("Write how many ml of milk do you want to add: \n"))
        self.supplies['beans'] += int(input("Write how many grams of coffee beans do you want to add: \n"))
        self.supplies['cups'] += int(input('Write how many disposable cups of coffee do you want to add: \n'))

    def action(self):
        while True:
            option = input("Write action (buy, fill, take, remaining, exit): \n")
            if option == "exit":
                exit()
            elif option == 'remaining':
                print()
                self.remaining()
                print()
            elif option == 'take':
                print()
                print(f"I gave you ${self.supplies['money']}")
                self.supplies['money'] = 0
                print()
            elif option == "fill":
                print()
                self.fill()
                print()
            elif option == 'buy':
                print()
                opt_coffee = input(
                    "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
                self.buy(opt_coffee)
                print()


CoffeeMachine()
