import uuid
from collections import defaultdict

'''
Problem Statement:
Build a expense management application wherein users can add an expense and assign
shares to their friends eg.
3 users, Ram, Shyam and Gyan went for a movie and ram paid 300 for tickets. He should be
able to add this expense and assign a amount of 100 to Shyam and gyan each.
Key functionalities to be implemented:
1. Add an expense and add other friend’s amount.
2. Get details of the amount owed by each friend.
3. Get details of the amount the user owes to friends 
'''

''' Solution: '''


class User:
    def __init__(self):
        self.friends = defaultdict(list)
    
    def add_friend(self, friend1, friend2):
        self.friends[friend1].append(friend2)
        self.friends[friend2].append(friend1)

    def get_friends(self, friend):
        return self.friends[friend]
    

class ExpenseManager:
    def __init__(self):
        self.payer = defaultdict(list)
        self.receiver = defaultdict(list)
    
    def add_expense(self, payer, amount, friend):
        self.payer[payer].append([amount, friend])
        self.receiver[friend].append([amount, payer])
    
    def get_amount_owed_by_friend(self, payer):
        result = defaultdict(list)
        for amount, friend in self.payer[payer]:
            result[payer].append([friend, amount])
        return result

    def get_aggregate_owned_by_friend(self, payer):
        result= 0
        for amount, friend in self.payer[payer]:
            result += amount
        for amount, friend in self.receiver[payer]:
            result -= amount
        return result

    def get_amount_owed_to_friend(self, friend):
        result = defaultdict(list)
        for amount, payer in self.receiver[friend]:
            # print("Amount owed to", payer, ":", amount)
            result[friend].append([payer, amount])
        return result
    
    def update_expense(self, payer, amount, friend):
        for idx in range(len(self.payer[payer])):
            if self.payer[payer][idx][1] == friend:
                self.payer[payer][idx][0] = amount


manager = ExpenseManager()

# Adding expenses
ram = "ram"
shyam = "shyam"
gyan = "gyan"

# user = User()
# user.add_friend(ram, shyam)
# user.add_friend(ram, gyan)


manager.add_expense(ram, 100, shyam)
manager.add_expense(ram, 120, shyam)
manager.add_expense(ram, 100, gyan)

print(manager.get_amount_owed_by_friend(ram))

# print(manager.get_amount_owed_by_friend(ram))
print(manager.get_amount_owed_to_friend(shyam))
print(manager.get_aggregate_owned_by_friend(ram))

# ram -> shyam = 100
# gyan -> ram = 120
# ram = -20

