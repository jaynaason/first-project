# Emotional levels
sad = 0
happiness = 0
anger = 0

while True:
    print '\n\nWelcome to this game'
    intro = raw_input('Would you like to play? ')
    if intro == "yes":
        print 'Cool lets get started!'
        break
    elif intro == "no":
        print 'Thats cool next time!'
        break
    else:
        print 'Please try again'
        continue

print '\nThis game is too see your emotional state'
lonely = raw_input('Do you feel lonely now? ')
if lonely == 'yes':
    sad += 1
elif lonely == 'no':
    pass



