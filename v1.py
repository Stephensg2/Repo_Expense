import random
import csv

class ExpenseData:
    class_data = []
    class_names = []

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                value = float(value) if isinstance(value, int) else value
                if not hasattr(self, key):
                    setattr(self, key, value)

            name = getattr(self, 'name', None)
            if name:
                self.name = name.lower().title() if isinstance(name, str) else name
                if self.name not in ExpenseData.class_names:
                    ExpenseData.class_data.append(self)
                    ExpenseData.class_names.append(self.name)
                else:
                    self.update_value(self.name, float(self.value))
            return

        if args:
            for name in args:
                name = name.lower().title()
                if name not in ExpenseData.class_names:
                    ExpenseData(name=name, value=0)

    def __add__(self, num: float):
        for v in ExpenseData.class_data:
            if v.name == self.name:
                self.value += num

    def __sub__(self, value: float):
        if isinstance(self.value, (int, float)):
            self.value -= value
        return self

    def update_value(self, name, value):
        for item in self.class_data:
            if item.name == name:
                item.value += value

        # Promote any other non-name/value attributes to new ExpenseData objects
        for k, v in self.__dict__.items():
            if k not in ['name', 'value']:
                if k not in ExpenseData.class_names:
                    ExpenseData(name=k, value=float(v) if isinstance(v, int) else v)

    def __repr__(self):
        name = getattr(self, 'name', '')
        value = getattr(self, 'value', 0)
        other_fields = [k for k in self.__dict__ if k not in ['name', 'value']]
        base = f'Name: {name} - Value: {value}'
        if other_fields:
            return f'{base} - Others: {len(other_fields)}'
        return base

    @classmethod
    def load_csv(cls, file = "data.csv"):
        with open(file, 'r', newline="") as csv_data:
            reader = csv.DictReader(csv_data)
            for item in reader:
                ExpenseData(
                    name=item.get('name', ''),
                    value=float(item.get('value', 0))
                )

    @classmethod
    def take_input(cls):
        print("Enter Data (name, value):")            
        data = input().split(",")
        name, value = data[0], data[1]
        ExpenseData(name=name, value=float(value))

    @classmethod
    def set_random_value(cls, name):
        for item in cls.class_data:
            if item.name == name.title():
                item.value = float(random.randint(1, 1000))


class Testing1(ExpenseData):
    test1_data = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.other = kwargs.get('other', "No Value Set")
        if self.name not in [obj.name for obj in Testing1.test1_data]:
            Testing1.test1_data.append(self)



# Load from CSV
ExpenseData.load_csv()

# Positional values (creates 0-value records)
ExpenseData("groceries", "entertainment", "savings")

# Keyword input
ExpenseData(name='Books', value=100)
Testing1(name='Stephen', value=840, other="Help", extra="Yes")
Testing1(name='Stephen', value=100, tomorrow="Sure")

# User input
# ExpenseData.take_input()

# Randomize value
ExpenseData.set_random_value("Groceries")

# View all entries
for entry in ExpenseData.class_data:
    print(entry)

print("Done")


