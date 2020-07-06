print("Game Loaded. Programmed July 6 2020")

print("Welcome to the game. Type CONTINUE when it prompts you for input to continue storyline.")
user_name = input()

print("Story: You are in a prison cell. Wrongly accused of a bank robbery, you must find a way to break out.")
user_name = input()
print("MARCH 1, 2001: State Penitentiary")
user_name = input()
print("Prison Guard 1: Hello, Henry. You have a package. We already checked it, don't expect anything. Right Charles?")
user_name = input()
print("Prison Guard 2: Well, uh, of course I have! I would lose my job if I didn't, *nervous grin* hehe? Right?")
user_name = input()
print("Prison Guard 3: Alright. Let's go.")
user_name = input()
print("You open the box to see what is inside - Select what will be inside.")
print("INPUT one of these items: File, Phone, Mini Drill")
user_name = input()
if user_name == "File":
    print("You discover a file. Input where to use the file: CELL DOOR/WINDOW")
    user_name = input()
    if user_name == "CELL DOOR":
        print("You successfully cut a few bars without guards noticing. When it breaks however, two of them responds.")
        print("Input FIGHT to fight them, input RUN to flee from them.")
        user_name = input()
        if user_name == "FIGHT":
            print(
                "You fight the guards. One of them is taken down but the other shoots you to death successfully. Fail")
            user_name = input()
            
            
        if user_Name == "FLEE":
            print("You run as fast as you can. The guards chase you all the way to the main hall.")
            print('You eventually run near a wall. They are shooting you. Input LEFT to turn to the left hall. Input '
                  'RIGHT to turn to the right hall.')
            user_name = input()
            if user_name == "LEFT":
                print(
                    "You go to the left hall. As you turn, a guard was waiting for at the left hall and you are shot.")
                print("Fail.")
            if user_name == "RIGHT":
                print("You successfully turn right. But now you are cornered. Type GIVE UP to surrender or ESCAPE...")
                print("...to try and attempt to get out of the prison.")
                user_name = input()
                if user_name == "GIVE UP":
                    print("You surrender. You are now transferred to maximum security. Fail.")
                if user_name == "ESCAPE":
                    print("You learned acrobatics when you were young. You used it and managed to get out.")
                    user_name = input()
                    print("You get out of the complex. Disguise as a guard and safely leave the prison.")
                    print("You are now free, but you will have to lay low for a long, long time... SUCCESS")
                    user_name = input()

    if user_name == "WINDOW":
        print("You are caught by a guard halfway done cutting the bars. Moved to max security cell. Fail.")
        user_name = input()
if user_name == "Phone":
    print("You pull out a phone. Who are you going to call? Type GANG"
          " for your homies to break you out. Type LAWYER to plead for a re-trial.")
    user_name = input()
    if user_name == "GANG":
        print("You call a gang that you used to be part of when you were younger.")
        print("They agree to help break you out...")
        user_name = input()
        print("MARCH 10, 2001")
        user_name = input()
        print("The whole prison was destroyed as 40 gang trucks approached the complex.")
        user_name = input()
        print("The gang outnumbered the guards, but had poor weaponry.")
        user_name = input()
        print("They find you and break you out, along with 27 other inmates.")
        user_name = input()
        print("You barely escaped. The fate of the gang is unknown. You must lay low. SUCCESS.")
    if user_name == "LAWYER":
        print("After long months pass, a re-trial is scheduled..")
        print("AUGUST 2, 2001 - STATE COURT")
        print("Judge: Continue, witness.")
        user_name = input()
        print("Witness: Alright, so I found this stray moneybag driving my way to the bank...")
        print("Witness: I naturally put it into the truck, and later into the vault.")
        user_name = input()
        print("Judge: Alright. All evidence points to Henry being guilty-")
        user_name = input()
        print("Attorney: Objection! I have proof that Henry was not hiding there deliberately.")
        user_name = input()
        print("Judge: Hm, well then? Present this evidence already!")
        user_name = input()
        print("Attorney: If he alone were hiding there deliberately, the knot wouldn't be tied!")
        user_name = input()
        print("Judge, Witness and Witness' Attorney: !!!")
        user_name = input()
        print("Attorney: He wouldn't be able to tie the knot from the inside if it was deliberate!")
        print("The moneybag that was used as evidence, was indeed tied! Meaning he was put in there...")
        print("...by someone else! By this very witness!")


        user_name = input()



        print("Attorney: As you can see by this doctor's analysis, the defendant had taken quite a beating.")
        user_name = input()
        print("While he was in the bag, he was unconscious!")
        user_name = input()
        print("Witness: W-what! These are lies!")
        user_name = input()
        print("Witness' Attorney: This, this is absurd!")
        user_name = input()
        print("Attorney: The witness attempted to dispose of the body, so he left the defendant in the bag,")
        print("knowing he'd drive it back to the bank.")
        user_name = input()
        print(" When the witness and his partner passed the bag, he made his partner throw the bag with the others.")
        print("Witness' Attorney: But why would he do that?")
        user_name = input()
        print("Attorney: Why? To dispose of the body of course. It would take a long time for him to be found along...")
        print("the other bags. But unlucky for him, he woke up, and found at the vault!")
        user_name = input()
        print("Witness: No no no! This can't be happening to ME!!!!")
        print("Success. You are now legally free.")
if user_name == "Mini Drill":
    print("You pull out.. a mini drill? You try breaking the floor with it, but a guard quickly noticed. Fail.")
    user_name = input()


print("Thank you for playing! Updates will be made soon!")
user_name = input()


