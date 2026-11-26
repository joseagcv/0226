class Character:

    def __init__(self, hitpoints: int, num_lives: int, damage_per_attack: int, id: str):
        self.__id = id
        self.__hitpoints = hitpoints
        self.__num_lives = num_lives
        self.__damage_per_attack = damage_per_attack

    def __add_hitpoints(self, hitpoints_to_add: int):
        self.__hitpoints += hitpoints_to_add

    def __add_lifes(self, num_lifes_to_add: int):
        self.__num_lives += num_lifes_to_add

    def __add_damage_per_attack(self, damage_to_add: int):
        self.__damage_per_attack += damage_to_add

    def evolve(self):
        self.__add_hitpoints(100)
        self.__add_lifes(1)
        self.__add_damage_per_attack(5)

    def show_hitpoints(self):
        print(f'Hitpoints: {self.__hitpoints}')
        if self.__hitpoints > 500:
            print('A LOT of hitpoints!!')

    def show_number_of_lives(self):
        print(f'Number of lives: {self.__num_lives}')
        if self.__num_lives > 1:
            print('Wow!! More than one life!')

    def show_damage_per_attack(self):
        print(f'Damage per attack: {self.__damage_per_attack}')
        if self.__damage_per_attack > 50:
            print('Strong player!')

    def show_data(self):
        self.show_hitpoints()
        self.show_number_of_lives()
        self.show_damage_per_attack()
    
    def to_dict(self):
        return {
            "id": self.__id,
            "hitpoints": self.__hitpoints,
            "num_lives": self.__num_lives,
            "damage_per_attack": self.__damage_per_attack
        }
