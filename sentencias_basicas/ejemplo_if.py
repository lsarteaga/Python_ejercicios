#paper, sissors, rock
class Game():
    def __init__(self):
        self.players = []
        self.options = ['Paper', 'Rock', 'Scissors']
        self.choice = []

    def verify(self, winner):
        value_p1 = self.choice[0]
        value_p2 = self.choice[1]
        if value_p1 == value_p2:
            print('\nEqual result!! lets go another round...')
            winner = 0
        else:
            if value_p1 == 1 and value_p2 == 2:
                print('Congratulations {} you are the winner!!'.format(self.players[0].name))
            else:
                if value_p1 == 1 and value_p2 == 3:
                    print('Congratulations {} you are the winner!!'.format(self.players[1].name))
                else:
                    if value_p1 == 2 and value_p2 == 1:
                        print('Congratulations {} you are the winner!!'.format(self.players[1].name))
                    else:
                        if value_p1 == 2 and value_p2 == 3:
                            print('Congratulations {} you are the winner!!'.format(self.players[0].name))
                        else:
                            if value_p1 == 3 and value_p2 == 1:
                                print('Congratulations {} you are the winner!!'.format(self.players[0].name))
                            else:
                                print('Congratulations {} you are the winner!!'.format(self.players[1].name))
                winner = 1
        return winner


    def menu(self):
        print('Welcome to game of: rock, paper, scissors\n')
        #append player to game list
        for i in range(2):
            name = input('Player {} insert your name: '.format(i+1))
            self.players.append(Player(i+1, name))
        #the turns init
        winner = 0
        while winner != 1:
            for i in range(2):
                print('\n* {} select a choice: '.format(self.players[i].name))
                print('1) {}'.format(self.options[0]))
                print('2) {}'.format(self.options[1]))
                print('3) {}'.format(self.options[2]))
                option = int(input('Enter your option: '))
                self.choice.append(option)
            winner = self.verify(winner)
            self.choice.clear()

class Player():
    def __init__(self, id, name):
        self.id = id
        self.name = name

#main

if __name__ == '__main__':
    game = Game()
    game.menu()
