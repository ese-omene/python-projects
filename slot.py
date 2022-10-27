import random

#contants
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

#get the deposit from the user
def deposit():
    while True:
        amount = input("What would you like to deposit? $") #ask how much they would like to deposit
        if amount.isdigit(): #check if they entered a number
            amount = int(amount) #convert the amount from a string to an integter
            if amount > 0:
                break  #if the amount is a number and is greater than 0 you can exit the loop
            else:
                print("amount needs to be greater than 0") #get the user to enter a valid number
        else:
            print("please enter a number") # get the user to enter a number
    return amount #return the amount the user is depositting

#get the number of lines the user would like to bet on
def get_line_bet():
    while True:
        lines = input(f"Enter the number of lines you woul like to bet on ( 1 - {str(MAX_LINES)} )?") #ask how many lines, within the allowable range, they would like to bet on
        if lines.isdigit():  #make sure they enter a numer
            lines = int(lines)  #convert the amount froma string to an integer
            if 1 <= lines <= MAX_LINES:
                break #if the number is in the range, you can exit the loop
            else:
                print("Enter a valid number of line") #user needs to enter a number in the range
        else:
            print("Please enter a number") #user needs to enter a number
    return lines

#get the amount the user would like to bet
def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $") #ask how much they would like to bet on each line
        if bet.isdigit(): #make sure they entered a number
            bet = int(bet) #convert the string to an integer
            if MIN_BET <= bet <= MAX_BET: #make sure the bet is within the rang
                break #if number is in range, break out of the loop
            else:
                print(f"please entere a number between {MIN_BET} and {MAX_BET}")
        else:
            print(f"please enter a number")
    return bet

#symbols for the slot machine
symbol_count = {
    "A" : 2,
    "B" : 3,
    "C" : 4,
    "D" : 4
}
symbol_value = {
     "A" : 8,
     "B" : 3,
     "C" : 2,
     "D" : 2
}

#spin the machine and create the columns
def spin_machine(rows, cols, symbols):
    all_symbols = [] #create a list of all possible symbols
    for symbol, symbol_count in symbols.items(): # key and value for all the symbols in the list of symbols 
        for _ in range(symbol_count): #use anonymous variable to iterate through as many times as dictated by the value ("A" : 2 means two times)
            all_symbols.append(symbol) #add the symbol to the list
    columns = [] #create a list for the columns
    for _ in range(cols): # use anonmymous variable, and loop through and create as many columns as needed
        column = [] #the list for the values in a single column
        current_symbols = all_symbols[:] #create a copy of the list of symbols so you can manipulate this one for the game
        for _ in range(rows): #use anonymous variable, loop through and create as many rows as needed
            value = random.choice(current_symbols) #get a random symbol
            current_symbols.remove(value) #remove that symbol from the list so it can't be used again
            column.append(value) #add the value to the column
        columns.append(column) #add the column to the matrix
    return columns

#print out the results of spinning the machine
def print_spin(columns):
    print("**SLOTS**")
    for row in range(len(columns[0])): #for each row in the column starting at the first position
        for i, column in enumerate(columns): #key value pair for the values in the columns
            if i != len(columns) - 1: #if it's not the last item 
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print() #print a new line
    print("*********")

#calculate winnings for each spin
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #looking at all the lines
        symbol = columns[0][line] #looking at the symbol in the  first columm in the given line 
        for column in columns: #looking at each column on it's own
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

#need to determine if the user has enough to play the game
def play(balance):
    lines = get_line_bet() #find out how many lines the user bet on 
    while True:
        bet = get_bet() #find out how much they bet on each line
        total_bet = bet * lines #calculated how much the bet will cost
        if total_bet > balance: #find out if the user is betting more than they have
            print(f"You do not have enough to bet that amount, your current balance is {balance}")
        else:
            break #break out of the loop if they can proceed with the play
    print(f"You are betting ${bet} on {lines} lines.  Total bet is equal to ${total_bet}")

    spin = spin_machine(ROWS,COLS,symbol_count)
    print_spin(spin)
    winnings, winning_lines = check_winnings(spin, lines, bet, symbol_value)
    if winnings != 0 : #determin if you won anything
        print(f"you won ${winnings}")
        print(f"You won on lines ", *winning_lines)
    else:
        print("you did not win on any line")
    return winnings - total_bet



def main():
    amount = deposit()
    while True:
        print(f"your current balance is ${amount}")
        answer = input("press enter if you wan to play (q to quit)")
        if answer == "q":
            break
        amount += play(amount)
    print(f"You left with ${amount}")
   

main()

