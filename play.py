from conf import *
from login_gui import *
import conf

class Player:
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

class View:
    """defines class for Input View"""

    @staticmethod
    def get_record(name):
        """gets player's name and returns it (string)"""
        members = View.load_members()
        if name in members.keys():
            tries = members[name][0]
            wins = members[name][1]
            winrate = 100 * wins / tries if tries > 0 else 0
            chips = members[name][2]
            return (name, tries, wins, chips)
        else:
            members[name] = (0,0,0)
            return name, 0, 0, 0

    @staticmethod
    def load_members():
        """if "members.txt" exist, read "members.txt" else make members.txt and read members.txt"""
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
        """write line in members.txt"""
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
        """load members.txt and sorted members into chips"""
        members = View.load_members()
        sorted_members = sorted(members.items(),\
                                key=lambda x: x[1][2],\
                                reverse=True)
        s = []
        if len(sorted_members) < 5:
            for i in range(len(sorted_members)):
                s.append(sorted_members[i])
        else:
            for i in range(5):
                s.append(sorted_members[i])
        return s

if __name__=='__main__':
    conf.root.title("Blackjack")
    conf.root.resizable(width=False, height=False)
    LoginGui(conf.root)
    conf.root.mainloop()