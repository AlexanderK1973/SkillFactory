from pat_house import Cat

    animals = [
        {
            'Имя': "Барон",
            'Пол': 'Мальчик',
            'Возраст': 2,
        },
        {
            'Имя': "Сэм",
            'Пол': 'Мальчик',
            'Возраст': 2,
    },
]

for cat in animals:
    cat_spec = Cat(name=cat.get("Имя"),
                   gender=cat.get("Пол"),
                   age=cat.get("Возраст"))
    print(f'Имя котика - {cat_spec.name},'
          f' его пол - {cat_spec.gender},'
          f' и возраст - {cat_spec.age} года.'
          f'\n_______________________')
