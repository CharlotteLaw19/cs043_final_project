class HtmlUtils:

    def __init__(self):
        super()

    def getLoginPage(self):
        return '''
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Login or Register</title>
</head>
<br>

<style>
div{
width: 500px;
height: 115px;
text-align: center;
margin-left:auto;
margin-right:auto;
font-size: 400%;
}

form{
width: 500px;
height: 215px;
text-align: center;
margin-left:auto;
margin-right:auto;
font-size: 150%;
}

</style>


<div class="highlight3" style="background: linear-gradient(to bottom, lightblue 0%, white 80%)">Play Tic Tac Toe!</div>

<form class="form1" action="/login" style="background: linear-gradient(to bottom, #F493D1 0%, white 100%)">
    <h1>Login Below!</h1>
    User:  <input type="text" name="username"><br>
    Pass:  <input type="password" name="password"><br>
    <input type="submit" value="Log in">
</form><br>


<form class="form2" action="/register" style="background: linear-gradient(to bottom, #D293F4 0%, white 100%)">
    <h1>Register Below!</h1>
    User:  <input type="text" name="username"><br>
    Pass:  <input type="password" name="password"><br>
    <input type="submit" value="Register">
</form></html>
'''

    def getNotFoundPage(self):
        return 'Status 404: Resource not found'

    def getNotLoginPage(self):
        return 'Not logged in <a href="/">Login</a>'

    def getAccountPage(self, username, won, lost, join_game_id):
        join_game_link = ""
        if join_game_id != 0:
            join_game_link = "<a href='/game?gameId={}'>Join an existing game</a>".format(join_game_id)

        logout = "<a href='/logout'>Log Out</a>"

        create_game = "<a href='/create?username={}'>Create a new game</a>".format(username)
        page = self.getAccountPageStr()

        page = page.format(username, join_game_link, create_game, logout)
        #page = page.format(username, won, lost, join_game_link, create_game, logout)
        page = page.replace('...', '}', 3)
        page = page.replace('..', '{', 3)
        return page

    def getGamePage(self, gameId, user, u1, u2, win1, win2, nextTurn, gameBoard):

        pos = gameBoard.getPositions()
        links = [''] * 10
        for i in range(1, 10):
            if pos[i] == 'X':
                links[i] = 'X'
            elif pos[i] == 'O':
                links[i] = 'O'
            else:
                if user == u1 and nextTurn == 'O' or user == u2 and nextTurn == 'X':
                    links[i] = '_'
                elif gameBoard.isBoardFull() == True or win1 == True or win2 == True:
                    links[i] = '_'
                else:
                    links[i] = "<a href='/game?gameId={}&move={}'>?</a>".format(gameId, i)
        # if  there  is a winner,  end  the game  and display message




        page = self.getGamePageStrHead()

        account = "<a href='/account'>Go back to account screen.</a>"
        page = page.format(gameId, links[7] , links[8], links[9], links[4], links[5], links[6], links[1], links[2], links[3], u1, u2, account)

        waitStr = self.getGamePageStrWait()
        winStr = self.getGamePageStrWin()
        loseStr = self.getGamePageStrLose()
        tieStr = self.getGamePageStrTie()

        if user == u1 and nextTurn == 'O' or user == u2 and nextTurn == 'X':
            page = page + waitStr

        if win1 == True and win2 == False:
            winStr = winStr.format(u1)
            loseStr = loseStr.format(u2)
            page = page + winStr + loseStr

        elif win1 == False and win2 == True:
            winStr = winStr.format(u2)
            loseStr = loseStr.format(u1)
            page = page + winStr + loseStr

        elif gameBoard.isBoardFull() == True and win1 == False and win2 == False:
            page = page + tieStr

        page = page + self.getGamePageStrTail()

        page = page.replace('...', '}')
        page = page.replace('..', '{')

        return page

    def getGamePageStrHead(self):
        return '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="refresh" content="2">
    <title>Playing Tic Tac Toe!</title>
</head>


<br>
<style>
div..
width: 500px;
height: 115px;
text-align: center;
margin-left:auto;
margin-right:auto;
font-size: 400%;
...

table, td, th ..
  border: 1px solid black;
...

table ..
  border-collapse: collapse;
  height: 130px;
  width: 13%;
  margin-left:auto;
  margin-right:auto;
  font-size: 230%;
...


td ..
  text-align: center;
...

h2 ..
  margin-left:auto;
  margin-right:auto;
  text-align: center;
...

body..

text-align:center;
color: black;
background-color: white;
align:center;
...

</style>

<body>

<div style="background: linear-gradient(to bottom, lightblue 0%, white 80%">Tic Tac Toe Game</div>
<div style="background: linear-gradient(to bottom, yellow 0%, white 80%">Game ID: {}</div>

<table>
  <tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
  </tr>
  <tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
  </tr>
  <tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
  </tr>
</table>
<br>



<h2 class="user1">User 1: {}</h2>
<h2 class="user2">User 2: {}</h2>

<h2>{}</h2>


'''

    def getGamePageStrWait(self):
        return '<h2 style="background: linear-gradient(to bottom, lavendar 0%, white 70%">Waiting for opponent\'s move</h2>'

    def getGamePageStrWin(self):
        return '<div style="background: linear-gradient(to bottom, lightgreen 0%, white 70%">{} wins!</div>'

    def getGamePageStrLose(self):
        return '<div style="background: linear-gradient(to bottom, tomato 0%, white 70%">{} loses!</div>'

    def getGamePageStrTie(self):
        return '<div style="background: linear-gradient(to bottom, orange 0%, white 70%">The game is a tie!</div>'



    def getGamePageStrTail(self):
        return '</body></html>'

    def getAccountPageStr(self):
        return '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="refresh" content="2">
    <title>Player's Account</title>
</head>

<style>
div..
width: 500px;
height: 115px;
text-align: center;
margin-left:auto;
margin-right:auto;
font-size: 400%;
...

h1..
width:150px;
height: 55px;
margin-left:auto;
margin-right:auto;
font-size: 200%;
...

body..
text-align:center;
color: black;
background-color: white;
align:center;
...

</style>

<br>

<div class="highlight2" style="background: linear-gradient(to bottom, lightblue 0%, white 80%)">Tic Tac Toe Lobby</div><br><br>

<h1 class="highlight1" style="background: linear-gradient(to bottom, yellow 0%, white 80%)">User Info</h1>

<body>
<h2>Account: {}</h2><br>

<h1 class="highlight1" style="background: linear-gradient(to bottom, yellow 0%, white 80%)">Play Now!</h1>

<h2>{}</h2>
<h2>{}</h2>
<br>
<h1 class="highlight1" style="background: linear-gradient(to bottom, tomato 0%, white 80%)">{}</h1>

</body>

</html>'''
