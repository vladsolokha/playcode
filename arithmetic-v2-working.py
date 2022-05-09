def arithmetic_arranger(problems, *calculate):
  # Count no. of problems.
  numofproblems = len(problems)
  
  # Check if there are more than 5 problems.
  if numofproblems > 5:
    print("Error: Too Many Problems")
  
  # Make empty list to store problems to print later.
  listofproblems = []
  
  # Loop through problems list with iterable problem. 
  for problem in problems:
    # Split into list of elements.
    #print(problem)
    splitproblem = problem.split(" ") #need to check for errors
    #print(splitproblem)
    listofproblems.append(splitproblem)
    
  
    # Map elements to vars. 
    firstnum = splitproblem[0]
    secondnum = splitproblem[2]
    op = splitproblem[1]
    
    # Check if numbers are digits.
    if not firstnum.isdigit() and not secondnum.isdigit():
      print("Error: Numbers must only contain digits")
    
    # Check if op (operator) is + or -.
    if op != '+' and op != '-':
      print("Error: Operator must be '+' or '-'")
    
    # Check if numbers are more than 4 digits
    if len(firstnum) > 4 or len(secondnum) > 4:
      print("Error: Numbers cannot be more than four digits")

    # Evaluate if input option is true.
    if calculate == True:
      sumofprob = eval(problem)
      splitproblem.append(str(sumofprob))
    
  # I have array of problems.
  # Access each element and format to print.

  #print(listofproblems)
  for element in listofproblems:
    firstnum = element[0]
    secondnum = element[2]
    totalproblength = len(max(firstnum, secondnum))+2
    firstline =(" "*(totalproblength-len(firstnum))+firstnum)    
    print(firstline, end="    ")

  print()
  for element in listofproblems:  
    firstnum = element[0]
    op = element[1]
    secondnum = element[2]
    totalproblength = len(max(firstnum, secondnum))
    secondline =(op + " " + " "*(totalproblength-len(secondnum))+secondnum)
    print(secondline, end="    ")
    
  print()
  for element in listofproblems:  
    firstnum = element[0]
    secondnum = element[2]
    totalproblength = len(max(firstnum, secondnum))+2
    thirdline = ('-'*totalproblength)
    print(thirdline, end="    ")

#  for listofproblems in zip(listofproblems
#    print(listofproblems)

  #return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2"], True)