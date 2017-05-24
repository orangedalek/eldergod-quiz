total_score = 0

begin = raw_input("""Welcome to the elder god quiz! Type begin to play!  """)

if begin == "begin".lower():
    pass
else:
    print "maybe later!"

kittens = {"prompt": """Pick a cuddly kitten!
        a) Steve! Ginger and cuddly!
        b)Sammie! Calico and sassy!
        c) Tiger! Grey tabby and fluffy!
        d)Minerva! Tortie and wise!""", "a": 25, "b":50, "c": 75, "d": 100 }


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



decor = {"prompt": """Choose a style to decorate your room!
        a)Midcentury Modern
        B)Shabby Chic
        c)Farmhouse
        d)Brutalist
        """, "a": 25, "b": 50, "c": 25, "d": 100}

fashion = {"prompt": """Pich a terrible 00s fashion trend!
        a)Low rise jeans
        b)Glitter everything
        c)Tinted visor shades
        d)Trucker hats
        """, "a": 25, "b": 75, "c": 100, "d": 50}

pizza = {"prompt": """Pick a pizza!
        a)Hawaiian
        b)BBQ chicken
        c)Peas and mayo
        d)Buffalo wing
        """, "a": 50, "b": 100, "c":75, "d":25}

cumberbatch = {"prompt": """Pick an alternate name for Benedict Cumberbatch!
        a)Benefit Cumberbund
        b)Benicio Cauliflower
        c)Bearington Cantaloupe
        d)Benneton Catalogue
        """, "a": 100, "b": 75, "c": 50, "d": 25}


questions = [kittens, ukfood, ryans, unicorn, decor, fashion, pizza, cumberbatch]
for question in questions:
    answer = raw_input(question["prompt"])
    if answer in question:
        total_score = question[answer] + total_score
    else:
        print "Please pick a,b,c or d"

if answer <= 200:
    print """Congratulations, you are Cthulu!
    You love naps and the sea. You’re stoic and easy going most of the time, 
    but aren’t afraid to devout the soul of anyone who dares to disturb your slumber."""
elif answer <= 400:
    print """Congratulations, you are Nyogtha, The Thing That Should Not Be!
    While you used to haunt the red abyss, these days, you prefer to haunt the local Sephora, 
    where you’ve perfected the smokey eye."""
elif answer <= 600:
    print """Congratulations, you are Tsathoggua! 
    You’ve been around long enough to know what you want,
    and what you want is Pizza and alone time. Your home is your sanctuary, 
    and you hardly ever leave, even to terrorize the people of K’n-yan."""
else:
    print """Congratulations, you are The Worm That Gnaws in the Night! 
    People lose their minds in terror just from looking at you, but you’re 
    really a misunderstood party animal who loves dancing, late night burritos, 
    and the eternal chaos that awaits us all upon our deaths."""
