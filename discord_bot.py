#!/usr/bin/env python3

import discord
import asyncio
import requests
import re
import random
import itertools
from random import randint

client = discord.Client()

numbers = [1,2,3,4,5,6,7,8,9]

def attempt_board(m=3):
    """Make one attempt to generate a filled m**2 x m**2 Sudoku board,
    returning the board if successful, or None if not.

    """
    n = m**2
    numbers = list(range(1, n + 1))
    board = [[None for _ in range(n)] for _ in range(n)]
    for i, j in itertools.product(range(n), repeat=2):
        i0, j0 = i - i % m, j - j % m # origin of mxm block
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+m]         # block
                        for row in board[i0:i])):
                board[i][j] = x
                break
        else:
            # No number is valid in this cell.
            return None
    return board

def remove_cells(board):

    for i in baord:
        for j in i:
            print(j)

def remove_cells(board):    
    for i in board:
        for j in i:            
            random = randint(0, 9)
            if random < 5:
                i[j-1] = 0
    
    return board

    

def boardToString(board):
    string_board = ""

    for i in board:
        string_board = string_board + str(i) + " \n"

    return string_board
    
#trying to implement better formatting of our sudoku board
# async def print_sudoku2(board,user):
#     print("+" + "---+"*9)
#     for i, row in enumerate(board):
#         print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
#         if i % 3 == 2:
#             print("+" + "---+"*9)
#         else:
#             print("+" + "   +"*9)

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)

def check(msg):
    if msg.content.startswith('!submit'):
        raise AttributeError
    else:
        return msg.content.startswith('')

@client.event
async def on_message(message):
    if message.content.startswith("!play"):
        user = message.author
        await client.send_message(user,"Welcome to Sudoku Bot!")
        
        board = None
        while board == None:
            board = attempt_board()        

        string_board_full = boardToString(board)               

        test_board = remove_cells(board)

        string_board_test = boardToString(test_board)
        print(string_board_full)        

        await client.send_message(user,string_board_test)

        await client.send_message(user,"\nLooking for something challenging?\nYou're in the right place!\n\nUse the following format to solve the puzzle:\nFor example: If you want to enter the number 8 in the cell formed by the 3rd row and 4th column:\n3,4=8")

        exit = False

        while exit == False:
            try:
                response = await client.wait_for_message(author=user, check=check)
            except AttributeError:
                break
            
            content = response.content
            
            try:
                searchObj = re.match(r'([0-9],[0-9])=([0-9])', content, re.M|re.I)

                cordinates = searchObj.group(1)
                value = int(searchObj.group(2))
            except AttributeError:
                await client.send_message(user,"Incorrect format try again")
                continue


            searchCord = re.match(r'([0-9]),([0-9])', content, re.M|re.I)

            x_coord = int(searchCord.group(1))
            y_coord = int(searchCord.group(2))

            test_board[x_coord-1][y_coord-1] = value

            string_board_test = boardToString(test_board)

            await client.send_message(user,string_board_test)
        
        string_board_test = boardToString(test_board)
        if string_board_full == string_board_test:
            await client.send_message(user,"You are right\nWell done!")
        else:
            await client.send_message(user,"You are wrong")
        
        await client.send_message(user,"Game Over")        

        
client.run("<CLIENT_KEY>")