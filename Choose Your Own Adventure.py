print("Welcome to this simple choose your adventure game!")

name = input('Please Enter your name: ').capitalize().strip()
print('Welcome', name, 'to this adventure')
score = 0

print("................................................................")
answer = input("You are walking down a path. You encounter a fork in the road.\nWhich way do you go? left or right: ").lower().strip()

if answer == 'left':
    print(".....................................................................")
    answer = input("You come to a lake. You can swim across or try to build a bridge?\nWhat do you do? Swim (swim) or Build a bridge(bridge): ").lower()
    
    if answer == 'swim':
        print(".................................................................................")
        print('You tried to swim and got eaten by a giant squid. You lose')
        print("Your score:", score)

    elif answer == 'bridge':
        print(".................................................................................")
        answer = input("You attempt to build a bridge. You can use wood (wood) or stones (stones). What do you use?: ").lower().strip()
        if answer == 'wood':
            print(".................................................................................")
            print('The bridge collapses halfway across. You fall into the lake and are eaten by a giant squid. You lose.')
            print("Your score:", score)
        elif answer == 'stones':
            score += 1
            print(".................................................................................")
            print('The stone bridge holds. You cross safely.')
            answer = input("You see a mysterious cave ahead. Do you enter? (yes/no): ").lower().strip()
            if answer == 'yes':
                print(".................................................................................")
                print('You enter the cave and find a sleeping dragon guarding treasure. Do you sneak past it or try to steal some treasure? (sneak/steal): ').lower()
                if answer == 'sneak':
                    score += 1
                    print(".................................................................................")
                    print('You sneak past the dragon and find an exit. You escape safely with your life!')
                    print("Your score:", score)
                elif answer == 'steal':
                    print(".................................................................................")
                    print('The dragon wakes up and incinerates you. You lose.')
                    print("Your score:", score)
                else:
                    print(".................................................................................")
                    print('Not a valid option. You lose.')
                    print("Your score:", score)
            elif answer == 'no':
                print(".................................................................................")
                print('You avoid the cave, but soon get lost in the woods. You lose.')
                print("Your score:", score)
        else:
            print(".................................................................................")
            print('Not a valid option. You lose.')
            print("Your score:", score)

    else:
        print(".................................................................................")
        print('Not a valid option. You lose')
        print("Your score:", score)

elif answer == "right":
    score += 1
    print(".................................................................................")
    answer = input('You come to a little cabin, it looks shabby and scary. Do you go in? Yes or no?: ').lower().strip()
    if answer == 'yes':
        print(".................................................................................")
        print('You go in and promptly get eaten by a monster grandma. You lose')
        print("Your score:", score)

    elif answer == 'no':
        score += 1
        print(".................................................................................")
        answer = input('You walk around the house and see a path leading into a forest. Do you go in? (yes/no): ').lower().strip()
        if answer == 'no':
            print(".................................................................................")
            print('You turn around and promptly get eaten by monster grandma. You lose.')
            print("Your score:", score)

        elif answer == 'yes':
            score += 1
            print(".................................................................................")
            answer = input('You walk down the path and see a sword sticking from the ground. Do you pick it up? (yes/no): ').lower().strip()
            if answer == 'no':
                print(".................................................................................")
                print("You don't pick up the sword and encounter a giant wolf. You lose")
                print("Your score:", score)
            elif answer == 'yes':
                score += 1
                print(".................................................................................")
                answer = input("You pick up the sword. As you walk further, you find a treasure chest. Do you open it? (yes/no): ").lower().strip()
                if answer == 'yes':
                    score += 1
                    print(".................................................................................")
                    print("You open the chest and find a magic shield. You feel stronger.")
                    print("Your score:", score)
                elif answer == 'no':
                    print(".................................................................................")
                    print("You ignore the chest and continue on your way.")
                    print("Your score:", score)

                print(".................................................................................")
                answer = input("You encounter a giant wolf. Do you fight it (fight) or run away (run)?: ").lower().strip()
                if answer == 'fight':
                    print(".................................................................................")
                    print("You slay the wolf with your magic sword and shield. You continue deeper into the forest.")
                    score += 1
                    print("Your score:", score)

                    print(".................................................................................")
                    answer = input("You find a fork in the path. Do you go left or right? (left/right): ").lower()
                    if answer == 'left':
                        print(".................................................................................")
                        print("You encounter a group of bandits. They rob you and leave you in the forest. You lose.")
                        print("Your score:", score)
                    elif answer == 'right':
                        score += 1
                        print(".................................................................................")
                        print("You find a village. The villagers welcome you and offer you shelter.")
                        answer = input("Do you stay with the villagers or continue your adventure? (stay/continue): ").lower()
                        if answer == 'stay':
                            print(".................................................................................")
                            print("You live a peaceful life in the village. You win!")
                            print("Your score:", score)
                        elif answer == 'continue':
                            print(".................................................................................")
                            answer = input("You leave the village and find a haunted mansion. Do you enter? (yes/no): ").lower()
                            if answer == 'yes':
                                print(".................................................................................")
                                print("You enter the mansion and find a ghostly figure. It offers you a choice: power or wisdom. Which do you choose? (power/wisdom): ").lower()
                                if answer == 'power':
                                    print(".................................................................................")
                                    print("The ghost grants you immense strength. You become a legendary warrior. You win!")
                                    score += 1
                                    print("Your score:", score)
                                elif answer == 'wisdom':
                                    print(".................................................................................")
                                    print("The ghost grants you great wisdom. You become a wise leader. You win!")
                                    score += 1
                                    print("Your score:", score)
                                else:
                                    print(".................................................................................")
                                    print("Not a valid option. You lose.")
                                    print("Your score:", score)
                            elif answer == 'no':
                                print(".................................................................................")
                                print("You avoid the mansion and continue your journey. You eventually find a hidden treasure. You win!")
                                score += 1
                                print("Your score:", score)
                            else:
                                print(".................................................................................")
                                print("Not a valid option. You lose.")
                                print("Your score:", score)
                        else:
                            print(".................................................................................")
                            print("Not a valid option. You lose.")
                            print("Your score:", score)
                    else:
                        print(".................................................................................")
                        print("Not a valid option. You lose.")
                        print("Your score:", score)
                elif answer == 'run':
                    print(".................................................................................")
                    print("You try to run but the wolf catches you. You lose.")
                    print("Your score:", score)
                else:
                    print(".................................................................................")
                    print('Not a valid option. You lose.')
                    print("Your score:", score)
            else:
                print('Invalid option. You Lose')
                print("Your score:", score)
        else:
            print('Not a valid option. You lose.')
            print("Your score:", score)
    else:
        print('Not a valid option. You lose.')
        print("Your score:", score)

else:
    print('Not a valid option. You lose.')
    print("Your score:", score)

print('Thank you for playing', name)
