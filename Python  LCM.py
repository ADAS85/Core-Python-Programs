try:
  nOne = int(input("Enter number 1 : "))
  try:
    nTwo = int(input("Enter number 2 : "))
    if nOne > nTwo:
      lcm = nOne
    else:
      lcm = nTwo
    while True:
      if lcm % nOne == 0 and lcm % nTwo == 0:
        break
      else:
        lcm = lcm + 1
    print("\nLCM (" + str(nOne) + ", " + str(nTwo) + ") = ", lcm)
  except ValueError:
    print("\nInvalid Input!")
except ValueError:
  print("\nInvalid Input!")
