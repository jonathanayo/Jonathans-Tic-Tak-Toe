from helper import draw_board, check_turn, check_for_win
import os

spots = {1:"1",2:"2",3:"3",
         4:"4",5:"5",6:"6",
         7:"7",8:"8",9:"9"}

draw_board(spots)

playing = True
complete =  False
turn = 0
prev_turn = -1
while playing:
  # reset screen so board is only displayed once
  os.system('cls' if os.name == 'nt' else 'clear')
  draw_board(spots)
  if prev_turn == turn:
    print("Invalid spot selected, please pick another.")
  prev_turn = turn
  
  print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press q to quit")

  #get player input
  choice = input()
  if choice == 'q':
    playing = False
    #make sure number entered is on board (1-9)
  elif str.isdigit(choice) and int(choice) in spots:
    #check if spot has already been marked
    if not spots[int(choice)] in {"X", "O"}:
      #if number 1-9 and spots not marked mark the spot and switch turns
      turn += 1
      spots[int(choice)] = check_turn(turn)

  # check if a player has won/game ended
  if check_for_win(spots): 
    playing, complete = False, True
  if turn > 8:
    playing = False

#draw the board one last time outside of the loop to print the final results of the game
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
#declare a winner or a tie
if complete:
  if check_turn(turn) == 'X' :
    print (" Player 1 Wins!")
  else:
    print(" Player 2 Wins! ")
else:
  print("No Winner")
  
    