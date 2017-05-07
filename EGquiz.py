def calculate_final_score(q1,q2,q3,q4):
#adds scores from all questions. 

    final_score = total_score + q1 + q2 + q3 + q4

    return final_score


total_score = 0

begin = raw_input("""Welcome to the elder god quiz! Type begin to play!  """)

if begin == "begin".lower():
    pass
else:
    print "maybe later!"


ans1 = raw_input(""""Pick a cuddly kitten!
        a) Steve!
        b)Sammie
        c) Tiger!
        d)Minerva!
          """)
if ans1 == "a".lower():
    q1 = 25
elif ans1 == "b".lower():
    q1 = 50
elif ans1 == "c".lower():
    q1 = 75
elif ans1 == "d".lower():
    q1 = 100
else:
    print "Please pick a,b,c or d"


ans2 = raw_input(""""Pick a British comfort food!
        a) Curry!
        b)Fry-up
        c)Yorkshire Pudding!
        d)Fish & Chips!
          """)
if ans2 == "a".lower():
    q2 = 75
elif ans2 == "b".lower():
    q2 = 25
elif ans2 == "c".lower():
    q2 = 100
elif ans2 == "d".lower():
    q2 = 50
else:
    print "Please pick a,b,c or d"

ans3 = raw_input(""""Pick a famous Ryan!
        a) Ryan Reynolds!
        b)Ryan Goesling!
        c)Ryan Seacrest!
        d)Ryan Lochte!
          """)
if ans3 == "a".lower():
    q3 = 100
elif ans3 == "b".lower():
    q3 = 50
elif ans3 == "c".lower():
    q3 = 75
elif ans3 == "d".lower():
    q3 = 25
else:
    print "Please pick a,b,c or d"

ans4 = raw_input(""""Pick a unicorn food!
        a)Unicorn toast!
        b)Unicorn frappuccino!
        c)Unicorn pasta!
        d)Unicorn bagel!
          """)
if ans4 == "a".lower():
    q4 = 100
elif ans4 == "b".lower():
    q4 = 50
elif ans4 == "c".lower():
    q4 = 75
elif ans4 == "d".lower():
    q4 = 25
else:
    print "Please pick a,b,c or d"

final_score = calculate_final_score(q1,q2,q3,q4)

if final_score <= 100:
    print "Congratulations, you are Cthulu!"
elif final_score <= 200:
    print "Congratulations, you are Nyogtha, The Thing That Should Not Be!"
elif final_score <= 300:
    print "Congratulations, you are Tsathoggua!"
else:
    print "Congratulations, you are The Worm That Gnaws in the Night!"
