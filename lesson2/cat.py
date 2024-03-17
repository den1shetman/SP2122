class cat:
    def __init__(self, name:str, age:float = 0.0,):
        self.Name:str = name
        self.Age:float = age

        def __str__(self):
            return (f"Name {self.Name}\n"
           f"Age: {self.Age}\n")