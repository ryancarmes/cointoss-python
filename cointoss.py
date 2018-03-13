def cointoss (number_of_tosses):
    head = 0
    tail = 0
    import random
    for x in range (0, number_of_tosses+1):
        result = random.randint(0, 1)
        if result == 0:
            head = head + 1 
            print "Attempt #" + str(x) + ": Throwing a coin...It's a head! ... Got " + str(head) + " head(s) and " + str(tail) + " tails so far"
        else:
            tail = tail + 1
            print "Attempt #" + str(x) + ": Throwing a coin...It's a tail! ... Got " + str(head) + " head(s) and " + str(tail) + " tails so far"
    print "Ending program, thank you!"

cointoss(5000)
        