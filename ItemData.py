import random
import csv
import shutil
import os 


class ItemData:
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
                if self.name not in ItemData.class_names:
                    ItemData.class_data.append(self)
                    ItemData.class_names.append(self.name)
                else:
                    self.update_value(self.name, float(self.value))
            return

        if args:
            for name in args:
                name = name.lower().title()
                if name not in ItemData.class_names:
                    ItemData(name=name, value=0)
        ItemData.save_csv()

    def __add__(self, value: float):
        if isinstance(self.value, (int, float)):
            self.value += value
            self.save_csv()
        return self 
        
    def __sub__(self, value: float):
        if isinstance(self.value, (int, float)):
            self.value -= value
            self.save_csv()
        return self

    def update_value(self, name, value):
        for item in self.class_data:
            if item.name == name:
                item.value += value

        for k, v in self.__dict__.items():
            if k not in ['name', 'value'] and isinstance(v, (int, float)):
                if k.lower().title() not in ItemData.class_names:
                    ItemData(name=k, value=float(v))
        self.save_csv()


    @classmethod
    def load_csv(cls, file = "data.csv"):
        with open(file, 'r', newline="") as csv_data:
            reader = csv.DictReader(csv_data)
            for item in reader:
                ItemData(
                    name=item.get('name', ''),
                    value=float(item.get('value', 0))
                )

    @classmethod
    def save_csv(cls, file='data.csv'):
        if os.path.exists(file):
            backup_file = file + '.bak'
            shutil.copy(file, backup_file)
            print(f"Backup created: {backup_file}")

        fieldnames = ['name', 'value']

        for item in cls.class_data:
            for key in item.__dict__.keys():
                if key not in fieldnames:
                    fieldnames.append(key)

        with open(file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for item in cls.class_data:
                writer.writerow(item.__dict__)  

    @classmethod
    def take_input(cls):
        print("Enter Data (name, value):")            
        data = input().split(",")
        name, value = data[0], data[1]
        ItemData(name=name, value=float(value))

    @classmethod
    def set_random_value(cls, name):
        for item in cls.class_data:
            if item.name == name.title():
                item.value = float(random.randint(1, 1000))

    def __repr__(self):
        name = getattr(self, 'name', '')
        value = getattr(self, 'value', 0)
        other_fields = [k for k in self.__dict__ if k not in ['name', 'value']]
        base = f'Name: {name} - Value: {value}'
        if other_fields:
            return f'{base} - Others: {len(other_fields)}'
        return base



def main():
            # Load from CSV
    ItemData.load_csv()

    # Positional values (creates 0-value records)
    ItemData("groceries", "entertainment", "savings")

    # Keyword input
    ItemData(name='Books', value=100)
    ItemData(name='Stephen', value=840, other="Help", extra="Yes")
    ItemData(name='Stephen', value=100)

    print("testinggg")

if __name__ == '__main__':
    main()

