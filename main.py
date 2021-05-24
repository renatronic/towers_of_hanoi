from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Creating the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
stacks += [left_stack, middle_stack, right_stack]

# Setting up the Game
num_disks = int(input('\nHow many disks you want to play with?\n'))

while num_disks < 3:
    num_disks = int(input('Enter a number greater than or equal to 3\n'))

for disk in range(num_disks, 0, -1): # iterates backwards through the range of the num_disks
    left_stack.push(disk)

num_optimal_moves = (2 ** num_disks) - 1 # calculates the number of optimal moves

print('\nThe fastest you can solve this game is in {0} moves'.format(num_optimal_moves))

# Getting User Input
def get_input():
  
    choices = [stack.get_name()[0] for stack in stacks] # a list of the first letters of the names of the stacks.

    while True:
        for i in range(len(stacks)): # iterates through the stacks
            name = stacks[i].get_name()
            letter = choices[i]
            print('Enter {0} for {1}'.format(letter, name))

        user_input = input('').upper()

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]: # WHY IS THIS LINE EXPENDABLE???
                    return stacks[i]

# Playing the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n…Current Stacks…")

    for stack in stacks:
        stack.print_items()

    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack.get_size() == 0:
            print("\n\nInvalid move! Try again…")
      
        elif (to_stack.get_size() == 0) or (from_stack.peek() < to_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        
        else:
            print("\n\nInvalid move! Try again…")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))