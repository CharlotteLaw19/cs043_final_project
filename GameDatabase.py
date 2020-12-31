import sqlite3
import random

class GameDb:

    def __init__(self):
        connection = sqlite3.connect('games.db')
        stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name in ('users', 'games', 'join_games')"
        result = connection.execute(stmt)
        r = result.fetchall()
        if (r == []) :
            exp = 'CREATE TABLE users (username, password, win, lose, current_game, pass_game)'
            connection.execute(exp)
            exp = 'CREATE TABLE games (game_id, user_x, user_o, next_turn, positions, x_win, o_win)'
            connection.execute(exp)
            exp = 'CREATE TABLE join_games (username, game_id)'
            connection.execute(exp)
        connection.commit()
        connection.close()
        super()

    def getConn(self):
        return sqlite3.connect('games.db')

    def registerUser(self, username, password):
        connection = self.getConn()
        user = connection.execute('SELECT * FROM users WHERE username = ?', [username]).fetchall()
        if user :
            return 'Sorry, username {} is taken'.format(username)
        else :
            connection.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)', [username, password, 0, 0, 0, '0,1'])
            connection.commit()
            return 'Congratulations, username {} been successfully registered'.format(username)

    def isValidUser(self, un, pw):
        connection = self.getConn()
        user = connection.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()
        if user:
            return True
        else:
            return False

    def login(self, username, password):
        connection = self.getConn()
        return connection.execute('SELECT * FROM users WHERE username = ? AND password = ?', [username, password]).fetchall()

    def logout(self, username, win, lose):
        connection = self.getConn()
        connection.execute('UPDATE users SET win = ?, lose = ? WHERE username = ?', [win, lose, username])
        connection.commit()
        connection.close()

    def createGame(self, username):
        connection = self.getConn()
        game_id = random.randint(1000, 5000)

        # game_id,username,user_x,user_o,next_turn, positions, x_win, o_win
        connection.execute('INSERT INTO games VALUES (?, ?, ?, ?, ?, ?, ?)', [game_id, username, '', 'X', '-, , , , , , , , , ', False, False])

        # username,game_id
        connection.execute('INSERT INTO join_games VALUES (?, ?)', [username, game_id])
        connection.commit()
        connection.close()

        return game_id

    def joinGame(self, username, game_id):
        connection = self.getConn()
        connection.execute('UPDATE games SET user_o = ? WHERE game_id = ?', [username, int(game_id)])
        connection.commit()
        connection.close()
        return game_id

    def updateUser(self, username, game_id):
        connection = self.getConn()
        connection.execute('UPDATE users SET current_game = ? WHERE username = ?', [game_id, username])
        connection.commit()
        connection.close()
        return game_id

    def getGame(self, game_id):
        # game_id, user_x, user_o, next_turn, positions, x_win, o_win
        connection = self.getConn()
        game = connection.execute('SELECT * from games WHERE game_id = ?', [int(game_id)]).fetchall()
        if game.__len__() == 0:
            return []
        else:
            return game[0]

    def saveGame(self, gameId, positions, x_win, o_win, next_turn):
        posStr = ''
        for pos in positions:
            if pos == '-':
                posStr += '-,'
            elif pos == 'X':
                posStr += 'X,'
            elif pos == 'O':
                posStr += 'O,'
            else:
                posStr += ","
        posStr = posStr[0:len(posStr)-1]

        connection = self.getConn()
        connection.execute("UPDATE games SET positions = ?, x_win = ?, o_win = ?, next_turn = ? WHERE game_id = ?", [posStr, x_win, o_win, next_turn, int(gameId)])
        connection.commit()
        connection.close()

    def loadFirstJoinableGame(self, username):
        #game = self.connection.execute('SELECT * from join_games WHERE username != ?', [username]).fetchall()
        connection = self.getConn()
        game = connection.execute('SELECT * from join_games').fetchall()

        # todo better
        if game.__len__() == 0:
            return 0
        else:
            return game[0][1]

    def deleteJoinedGame(self, gameId):
        connection = self.getConn()
        connection.execute("DELETE FROM join_games WHERE game_id = ?", [int(gameId)])
        connection.commit()
        connection.close()
        return gameId




