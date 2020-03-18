class participants:

    def __init__(self):
        self.name = ''
        self.participant = ''
        self.interests = []
        self.availableTime = 0
    
    def addStacks(self):
        if len(self.interests) > 5:
            print("You can't add anymore interests")
        else:
            while True:
                x = input('Add your interests: ')
                self.interests.append(x)
                if input('Add more? (y/n) ') != 'y':
                    break

    def setMentorOrLearner(self):
        x = input('Are you a mentor or a learner? ')
        if x.lower() == 'mentor':
            self.participant = 'mentor'
        elif x.lower() == 'learner':
            self.participant = 'learner'
        else:
            print('Please enter a valid choice')
    
    def personName(self):
        self.name = input('Enter your name: ')

    def setAvailableTime(self):
        if self.participant == 'mentor':
            self.availableTime = int(input('Enter the available time: '))
    
    def getMentor(self,people, interests, availableTime):
        l = []
        commonInterests = []
        for person in people:
            commonInterests = [value for value in person.interests if value in self.interests]
            if person.availableTime > 0 and len(commonInterests) != 0:
                l.append(person.name)
        print(l)
people = []

for i in range(100):
    people.append(participants())


for person in people:
    person.setMentorOrLearner()
    person.personName()
    person.addStacks()
    person.setAvailableTime()
    if person.participant == 'learner':
        person.getMentor(people, person.interests, person.availableTime)