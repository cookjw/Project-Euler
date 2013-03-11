def spellout(number):
    num = str(number)
    if len(num) == 1:
        if num == "1":
            return "one"
        if num == "2":
            return "two"
        if num == "3":
            return "three"
        if num == "4":
            return "four"
        if num == "5":
            return "five"
        if num == "6":
            return "six"
        if num == "7":
            return "seven"
        if num == "8":
            return "eight"
        if num == "9":
            return "nine"
    if len(num) == 2:
        tens = num[0]
        ones = num[1]
        if tens == "1":
            if ones == "0":
                return "ten"
            if ones == "1":
                return "eleven"
            if ones == "2":
                return "twelve"
            if ones == "3":
                return "thirteen"
            if ones == "4":
                return "fourteen"
            if ones == "5":
                return "fifteen"
            if ones == "8":
                return "eighteen"
            else:
                return spellout(int(ones)) + "teen"
        if tens == "2":
            if ones == "0":
                return "twenty"
            else:
                return "twenty"+spellout(int(ones))
        if tens == "3":
            if ones == "0":
                return "thirty"
            else:
                return "thirty" + spellout(int(ones))
        if tens == "4":
            if ones == "0": 
                return "forty"
            else:
                return "forty" + spellout(int(ones))
        if tens == "5":
            if ones == "0":
                return "fifty"
            else:
                return "fifty" + spellout(int(ones))
        if tens == "8":
            if ones == "0":
                return "eighty"
            else:
                return "eighty" + spellout(int(ones))
        else:
            if ones == "0":
                return spellout(int(tens))+ "ty"
            else:
                return spellout(int(tens)*10) + spellout(int(ones))
    if len(num) == 3:
        if num[1] == "0" and num[2] == "0":
            return spellout(int(num[0])) + "hundred"
        elif num[1] == "0":
            return spellout(int(num[0])) + "hundred" + "and" + spellout(int(num[2]))
        else:
            return spellout(int(num[0])) + "hundred" + "and" + spellout(num[1:])
    if num == "1000":
        return "one" + "thousand"
        

print sum([len(spellout(n)) for n in range(1,1001)])

            
        
         
                            
            
            
            
                