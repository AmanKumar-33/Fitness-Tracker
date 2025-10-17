

class Workout(object):
    """A simple class to keep the record of workouts"""
    cal_per_hr = 200

    def __init__(self,start,end,calories) -> None:
        self.start = start
        self.end = end
        self.calorie = calories
        self.icon = '@'
        self.kind = 'workout'

        pass
    def get_calorie(self):
        if calorie == None:
            return Workout.cal_per_hr*(self.end-self.start).total_secounds()//3600
        else:
            return self.calorie
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def set_start(self,start):
        self.start = start
    def set_end(self,end):
        self.end = end
    def set_calorie(self,calories):
        self.calorie = calories
# create an instance of the class 
my_workout = Workout('9/03/24 1:35pm','9/03/24 2:33pm',200)

#TEST: internal state of class 
print(Workout.__dict__.keys())
print()
print(Workout.__dict__.values())

print(my_workout.__dict__.keys())
print()
print(my_workout.__dict__.values())

"""Dot notation is used to access attributes(data and method) //my_workout.calories
it's better to use getter and setter to acess data attribute  //my_workout.get_calories
    """

class RunWorkout(Workout):
    
    def __init__(self, start, end,elev=0, calories):
        super().__init__(start, end, calories)
    










 """Inheritance hepls in code reusability, enhance the modularity and improve the clarity 
    Modularity means can pass subclass to any method that uses parent
    Information hiding """
    
    
