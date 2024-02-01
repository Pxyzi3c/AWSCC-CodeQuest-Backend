def to_bool(answer):
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print("Answer must 'y' or 'n' only")
        exit()

def last_scenario(scenario, next_action):
    print(f"**{scenario}**")
    action = input(f"{next_action} [y/n]? ")

    if to_bool(action):
        print("YOU WON!")
    else:
        print("GAME OVER!")

def asking_shelter(scenario):
    last_scenario(scenario, "POLICE: Is the thief inside")

def not_asking_shelter(scenario):
    last_scenario(scenario, "Will you knock him down")

is_asking_shelter = input("Man asking for help [y/n]? ")

if to_bool(is_asking_shelter):
    asking_shelter("POLICE ARRIVED")
else:
    not_asking_shelter("HE ATTACKED ON YOU")
