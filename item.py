import csv


class Item:
    data_item = []

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', "N/A")
        self.type = kwargs.get('type', "Chore")
        Item.data_item.append(self)

    def __repr__(self):
        return f'Name: {self.name} | Type: {self.type}'

class Chores(Item):
    data_chores = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Capture daily tracking info (as floats)
        self.days = {day: float(kwargs.get(day, 0)) for day in [
            'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'
        ]}
        Chores.data_chores.append(self)

    @classmethod
    def load_csv(cls, path='chores.csv'):
        with open(path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                chore_kwargs = {
                    'name': row.get('chores', '').strip(),
                    'value': row.get('value', 0)
                }
                for day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
                    chore_kwargs[day] = row.get(day, 0)
                cls(**chore_kwargs)
        print("Chores loaded successfully.")


# Load data and print all chores
Chores.load_csv()
for chore in Chores.cd_chores:
    print(chore)
    print("  Days:", chore.days)
