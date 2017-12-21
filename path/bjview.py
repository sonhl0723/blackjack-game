import os

class View:
    """defines class for Input and Output View"""

    @staticmethod
    def login(name):
        """gets player's name and returns it (string)"""
        # name = input("Enter your name : (4 letters max) ") 
        # while len(name) > 4:
        #     name = input("Enter your name : (4 letters max) ")
        members = View.load_members()
        if name in members.keys():
            tries = members[name][0]
            wins = members[name][1]
            print("Your played", tries, "games and won", wins, "of them")
            winrate = 100 * wins / tries if tries > 0 else 0
            print("Your all-time winning rate is", "{0:.1f}".format(winrate), "%")
            chips = members[name][2]
            print("You have", chips, "chips.")
            return name, tries, wins, chips
        else:
            members[name] = (0,0,0)
            return name, 0, 0, 0

    @staticmethod
    def ox(message):
        """returns True if player inputs 'o' or 'O', 
                   False if player inputs 'x' or 'X'"""
        response = input(message).lower()
        while not (response == 'o' or response == 'x'):
            response = input(message).lower()
        return response == 'o'

    @staticmethod
    def load_members():
        if os.path.exists("members.txt"):
            file = open("members.txt", "r")
            members = {}
            for line in file:
                member = line.strip('\n').split(',')
                members[member[0]] = (int(member[1]), float(member[2]), int(member[3]))
            file.close()
            return members
        else:
            file = open("members.txt", "a+")
            members = {}
            for line in file:
                member = line.strip('\n').split(',')
                members[member[0]] = (int(member[1]), float(member[2]), int(member[3]))
            file.close()
            return members

    @staticmethod
    def store_members(members):
        file = open("members.txt", "w")
        names = members.keys()
        for name in names:
            tries, wins, chips = members[name]
            line = name + ',' + str(tries) + ',' + \
                   str(wins) + ',' + str(chips) + '\n'
            file.write(line)
        file.close()

    @staticmethod
    def show_top5():
        members = View.load_members()
        print('-----')
        sorted_members = sorted(members.items(),\
                                key=lambda x: x[1][2],\
                                reverse=True)
        print("All-time Top 5")
        rank = 1
        for member in sorted_members[:5]:
            chips = member[1][2]
            if chips <= 0:
                break
            print(rank, '.', member[0], ':', chips)
            rank += 1

    # @staticmethod
    # def get_number(message,low,high):
    #     response = input(message)
    #     while not (response.isdigit() and low <= int(response) <= high):
    #         response = input(message)
    #     return int(response)


