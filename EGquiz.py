total_score = 0

begin = raw_input("""Welcome to the elder god quiz! Type begin to play!  """)

if begin == "begin".lower():
    pass
else:
    print "maybe later!"

kittens = {"prompt": """Pick a cuddly kitten!
        a) Steve!
        b)Sammie
        c) Tiger!
        d)Minerva!""", "a": 25, "b":50, "c": 75, "d": 100 }


ukfood = {"prompt":""""Pick a British comfort food!
        a) Curry!
        b)Fry-up
        c)Yorkshire Pudding!
        d)Fish & Chips!
          """, "a": 75, "b": 25, "c": 100, 'd': 50}

ryans = {"prompt": """"Pick a famous Ryan!
        a) Ryan Reynolds!
        b)Ryan Goesling!
        c)Ryan Seacrest!
        d)Ryan Lochte!
          """, "a": 100, "b": 50, "c": 75, "d": 25}

unicorn = {"prompt":""""Pick a unicorn food!
        a)Unicorn toast!
        b)Unicorn frappuccino!
        c)Unicorn pasta!
        d)Unicorn bagel!
          """, "a": 50, "b": 75, "c": 100, "d": 25}


questions = [kittens, ukfood, ryans, unicorn]
for question in questions:
    answer = raw_input(question["prompt"])
    if answer in question:
        total_score = question[answer] + total_score
    else:
        print "Please pick a,b,c or d"

if answer <= 100:
    print "Congratulations, you are Cthulu!"
elif answer <= 200:
    print "Congratulations, you are Nyogtha, The Thing That Should Not Be!"
elif answer <= 300:
    print "Congratulations, you are Tsathoggua!"
else:
    print "Congratulations, you are The Worm That Gnaws in the Night!"
