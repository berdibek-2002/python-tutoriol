class Contestant:
    def __init__(self, name):
        self.name = name
        self.scores = {}
        self.total_score = 0

    def add_points(self, competition, points):
        self.scores[competition] = points
        self.total_score += points

    def display_info(self):
        print(f"{self.name} - Umumiy ball: {self.total_score}")
        for competition, points in self.scores.items():
            print(f"  {competition}: {points} ball")

class Team(Contestant):
    def __init__(self, name):
        super().__init__(name)

class IndividualParticipant(Contestant):
    def __init__(self, name):
        super().__init__(name)

class Competition:
    def __init__(self, name):
        self.name = name

def get_contestant_by_name(contestants, name):
    for contestant in contestants:
        if contestant.name == name:
            return contestant
    return None

def display_all_contestants(contestants):
    for contestant in contestants:
        contestant.display_info()

def add_contestant(contestants, name, contestant_type):
    contestants.append(contestant_type(name))

def add_competition(competitions, competition_name):
    competitions.append(Competition(competition_name))

def conduct_competition(contestants, competitions):
    for contestant in contestants:
        print(f"\n{contestant.name} uchun musobaqalar:")
        for competition in competitions:
            points = int(input(f"{contestant.name} uchun ballarni {competition.name} da kiriting: "))
            contestant.add_points(competition.name, points)

def declare_winner(contestants):
    winner = max(contestants, key=lambda x: x.total_score)
    print(f"\n{winner.name} jami {winner.total_score} ball toʻplagan holda gʻolib bo'ldi!")

print('************************* Xush kelibsiz! ************************* \n'
      '****** Ushbu dastur musobaqalarda jamoalar va individual ishtirokchilar uchun ballarni hisoblab chiqadi ******')

max_teams = 4
max_participants = 20
stop = "stop"
contestants_list = []
competitions_list = []

# Adding teams
while len(contestants_list) < max_teams:
    add_team_name = input("Jamoa nomini kiriting (yoki tugatish uchun 'stop') -> ")

    if add_team_name == stop:
        print("Jamoa qo'shish tugallandi.")
        break

    add_contestant(contestants_list, add_team_name, Team)

# Adding individual participants
while len(contestants_list) < max_participants:
    add_participant_name = input("Ididual ishtirokchining ismini kiriting (yoki tugatish uchun 'stop') -> ")

    if add_participant_name == stop:
        print("Ishtirokchilarni qo'shish tugallandi.")
        break

    add_contestant(contestants_list, add_participant_name, IndividualParticipant)

# Displaying teams and participants
display_all_contestants(contestants_list)

# Adding competitions
while True:
    competition_name = input("Musobaqa nomini kiriting (yoki tugatish uchun 'stop') -> ")

    if competition_name == stop:
        print("Musobaqalarni qo'shish tugallandi.")
        break

    add_competition(competitions_list, competition_name)

# Conducting competitions and adding points
conduct_competition(contestants_list, competitions_list)

# Displaying final scores
print("\nYakuniy ballar:")
display_all_contestants(contestants_list)

# Declare the winner
declare_winner(contestants_list)
