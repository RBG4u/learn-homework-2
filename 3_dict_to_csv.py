import csv

users_card = [
        {'name': 'Маша', 'age': 25, 'gender': 'female', 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'gender': 'male', 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'gender': 'male', 'job': 'Big boss'},
        {'name': 'Катя', 'age': 33, 'gender': 'female', 'job': 'Manager'},
        {'name': 'Никита', 'age': 56, 'gender': 'male', 'job': 'Digger'}
    ]

def main():
    with open ('users.csv', 'w', encoding='utf-8') as users:
        fields = ['name', 'age', 'gender', 'job']
        writer = csv.DictWriter(users, fields, delimiter=';')
        writer.writeheader()
        for user in users_card:
            writer.writerow(user)


if __name__ == "__main__":
    main()