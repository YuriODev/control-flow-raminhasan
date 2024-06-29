# Your solution to Exercise 18

name = input("Do you remember their name? ")

if name == "yes":
  is_ex = input()

  if is_ex == "yes":
    is_drunk = input()

    if is_drunk == "yes":
      rekindle = input()

      if rekindle == "yes":
        print("Say hi.")

      elif rekindle == "no":
        print("Don't say hi.")

    elif is_drunk == "no":
      convertible = input()

      if convertible == "yes":
        print("Say hi.")

      elif convertible == "no":
        print("Don't say hi.")

  elif is_ex == "no":
    friend_ex = input()

    if friend_ex == "yes":
      print("Don't say hi.")

    elif friend_ex == "no":
      enemy = input()

      if enemy == "yes":
        convertible = input()

        if convertible == "yes":
          print("Say hi.")

        elif convertible == "no":
          print("Don't say hi.")

      elif enemy == "no":
        robbing_bank = input()

        if robbing_bank == "yes":
          print("Don't say hi.")

        elif robbing_bank == "no":
          bathrobe = input()

          if bathrobe == "yes":
            print("Don't say hi.")

          elif bathrobe == "no":
            print("Say hi.")

elif name == "no":
  flee = input()

  if flee == "yes":
    print("Run for it.")

  elif flee == "no":
    phone_call = input()

    if phone_call == "yes":
      print("Hello, doctor. What are my test results?")

    elif phone_call == "no":
      sunglasses = input()

      if sunglasses == "yes":
        print("Keep walking.")

      elif sunglasses == "no":
        print('Address the person using an amusing nickname such as "Sarge", "Slugger", or "Master Blaster".')
  