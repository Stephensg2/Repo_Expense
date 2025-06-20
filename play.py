import random 
import csv 

class ExpenseData: 
    class_data = []
    class_names = []

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if isinstance(value,int):
                    value = float(value)
                if not hasattr(self, key):
                    setattr(self, str(key), value)
            if getattr(self, 'name', None) not in ExpenseData.class_names:
                self.name = self.name.lower().title() if isinstance(self.name,str) else self.name
                ExpenseData.class_data.append(self)
                ExpenseData.class_names.append(self.name)
                return
            else:
                self.__add__(name = self.name, value = float(self.value))
            return 

        if args and not kwargs:
            [ExpenseData(name = x, value = 0) for x in args if x not in ExpenseData.class_names]           
        return

    @classmethod
    def load_csv(cls):
        results = []
        with open("data.csv", 'r', newline="") as csv_data:
            reader = csv.DictReader(csv_data)
            items = list(reader)
        
        for item in items:
            ExpenseData(
                name = item.get('name', ''),
                value = float(item.get('value'))
            )

    @classmethod
    def take_input(cls):
        print("Enter Data")
        data = input().lower().title().split()
        results = ExpenseData(*data)

    @classmethod
    def set_random_value(cls, name):
        for item in cls.class_data:
            if item.name.title() == name:
                item.value = float(random.randint(1,1000))
                setattr(item, name, item.value)
            
    def __repr__(self):
        name = getattr(self, 'name', '')
        value = getattr(self, 'value', 0)
        other = getattr(self, 'other', '')
        base = f'Name: {name} - value: {value}'
        if other:
            return f'{base} - Kwards: {int(len(self.__dict__)/2)} Others' 
        return f'Name: {self.name} - Value {self.value}'
    
    def __add__(self, name: str, value: float):    
        for item in self.class_data:
            if item.name == name:
                if isinstance(item.value, float):item.value += value
    
        test = [x for x in self.__dict__ if x not in ['name', 'value']]
        if test: 
            for x,y in self.__dict__.items():
                if x not in ["name", "value"] and y not in ["name", "value"]: 
                    if x not in ExpenseData.class_names:
                        ExpenseData(name = x, value = y)
        return 


    def __sub__(self, name: str, value: float):
        self.value -= num
        return self

    def find_attributes(self):
        pass


class Testing1(ExpenseData):
    test1_data = []
    def __init__(self, *args, **kwargs):
        super().__init__(   
            *args,**kwargs
        )
        self.Other = kwargs.get('Other', "No Value Set")
        # for items in kwargs:
        #     if items.
        #     self.items = items
        if self.name not in Testing1.test1_data:
            Testing1.test1_data.append(self)
        else: 
            pass


ExpenseData.load_csv()
ExpenseData("random fun", "Gift", "movies", "dinners", "Apples", "Dinners")
ExpenseData( name='Bar', value=333)
test_class = Testing1
test_class(name = 'Stephen', value = 840, other = "Help", crap = "Holy")
test_class(name = 'Stephen', value = 100, tomorrow = "Yes")

test_class.take_input()
print("Done")
test_class.take_input()

test_class.set_random_value("Movies")


print("done")

