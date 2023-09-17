class Dog:
    def get_mood(self):
        print("Dog is an animal")
        return self.mood
    
    def set_mood(self, data):
        self.mood = data

    def animate(self):
        if self.mood == 'Happy':
            return("wagging the tail")
        elif self.mood == 'Angry':
            return("growling")
        else:
            return("berk")

snoopy = Dog()
snoopy.set_mood("Happy")
print(snoopy.get_mood())
snoopy.set_mood("Angry")
print(snoopy.get_mood())
print(snoopy.animate())


