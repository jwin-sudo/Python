wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50


while True:
    print('1)   Wizard')
    print('2)   Elf')
    print('3)   Human')
    print('4    Add another character')
    print('5    Exit')

    character = input('Choose your character: ')

    if(character == '1' or character == 'Wizard' or character.lower().capitalize() == 'Wizard'):
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break

    if(character == '2' or character == 'Elf' or character.lower().capitalize() == 'Elf'):
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break

    if(character == '3' or character == 'Human' or character.lower().capitalize() == 'Human'):
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break

    if(character == '4'):
        character = input('Input character name: ')
        my_hp = int(input('Input character hitpoint: '))
        my_damage = int(input('Input character damage: '))
        break

    if(character == '5'):
        print('Goodbye!')
        exit(0)

    else:
        print('Unknown character')

print("You have choosen the character: " + str(character) + "\n" +
      "Health: " + str(my_hp) + "\n" + "Damage: " + str(my_damage))


while True:
    dragon_hp = dragon_hp - my_damage
    print("The " + character + " damage the Dragon")
    print("The Dragon's hitpoints are now " + str(dragon_hp))
    if(dragon_hp <= 0):
        print('The Dragon has lost the battle')
        break

    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at the " + character)
    print("The " + character + "'s hitpints are now " + str(my_hp))
    if(my_hp <= 0):
        print(character + " has lost the battle")
        break
