# LINK TO PROBLEM: https://www.hackerrank.com/challenges/python-lists/problem

# Problem Summary:
#   Consider a list (list = []). You can perform the following commands:
#     insert i e: Insert integer i at position e.
#     print: Print the list.
#     remove e: Delete the first occurrence of integer e.
#     append e: Insert integer e at the end of the list.
#     sort: Sort the list.
#     pop: Pop the last element from the list.
#     reverse: Reverse the list.

# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

def run_commands(command, answer_list):
  # Split the command into its components
  command_list = command.split()
  current_command = command_list[0]

  # Handling Commands: print, sort, pop, reverse
  if len(command_list) == 1:
    if current_command == "print":
      print(answer_list)
    else:
      eval(f"answer_list.{current_command}()")

  # Handling commands with one index/element provided
  elif len(command_list) == 2:
      index = command_list[1]
      eval(f"answer_list.{current_command}({index})")

  # Handling commands with two indexes/elements provided
  elif len(command_list) == 3:
      index = command_list[1]
      element = command_list[2]
      eval(f"answer_list.{current_command}({index}, {element})")
    
def main():
  N = int(input())
  answer_list = []
  for command_number in range(N):
    command = input()
    run_commands(command, answer_list)

if __name__ == "__main__":
  main()
  

  
