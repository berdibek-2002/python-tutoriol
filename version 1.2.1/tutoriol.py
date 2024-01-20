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
        if not isinstance(contestant, Contestant):
            raise ValueError("Tanlov ishtirokchilari roʻyxatidagi obʼyekt turi yaroqsiz.")
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


def get_valid_score_input():
    while True:
        try:
            points = int(input("Ballarni kiriting (1-9 oraligida ball bering!) -> "))
            if 1 <= points <= 9:
                return points
            else:
                print("Noto'g'ri ball! Faqat 1-9 oraligida ball bering.")
        except ValueError:
            print("Noto'g'ri qiymat! Faqat raqam kiriting.")


def conduct_team_competition(teams, competition):
    for team in teams:
        print(f"\n{team.name} uchun {competition.name} musobaqasi:")
        points = get_valid_score_input()
        team.add_points(competition.name, points)


def conduct_individual_competition(participants, competition):
    for participant in participants:
        print(f"\n{participant.name} uchun {competition.name} musobaqasi:")
        points = get_valid_score_input()
        participant.add_points(competition.name, points)


def determine_team_winner(teams):
    winner = max(teams, key=lambda x: x.total_score)
    print(f"\nJamoaviy musobaqa g'alibi: {winner.name} jami {winner.total_score} ball toʻplagan holda gʻolib bo'ldi!")


def determine_individual_winner(participants):
    winner = max(participants, key=lambda x: x.total_score)
    print(f"\nIndividual musobaqa g'alibi: {winner.name} jami {winner.total_score} ball toʻplagan holda gʻolib bo'ldi!")


print('************************* Xush kelibsiz! ************************* \n'
      '****** Ushbu dastur musobaqalarda jamoalar va individual ishtirokchilar uchun ballarni hisoblab chiqadi ******')

max_teams = 4
max_participants = 20
stop = "stop"
team_list = []
individual_list = []
team_competitions_list = []
individual_competitions_list = []

# Adding teams
while len(team_list) < max_teams:
    add_team_name = input("Jamoa nomini kiriting (yoki tugatish uchun 'stop') -> ")

    if not add_team_name:
        print("Siz jamoa nomini kiritmadingiz. Iltimos qayta urinib ko'ring!")
    elif add_team_name == stop:
        print("Jamoa qo'shish tugallandi.")
        break
    else:
        add_contestant(team_list, add_team_name, Team)

# Adding individual participants
while len(individual_list) < max_participants:
    add_participant_name = input("Individual ishtirokchining ismini kiriting (yoki tugatish uchun 'stop') -> ")

    if not add_participant_name:
        print("Siz individual ishtirokchi nomini kiritmadingiz. Iltimos qayta urinib ko'ring!")
    elif add_participant_name == stop:
        print("Individual ishtirokchilarni qo'shish tugallandi.")
        break
    else:
        add_contestant(individual_list, add_participant_name, IndividualParticipant)

# Check if either teams or individual participants joined
if not team_list and not individual_list:
    print("Hech qanday jamoa va individual ishtirokchi qo'shilmadi. Dasturni qayta boshlang!")
    exit()

# Displaying teams and participants
print("\nJamoa:")
display_all_contestants(team_list)
print("\nIndividual ishtirokchilar:")
display_all_contestants(individual_list)

# Adding team competitions
while True:
    competition_name = input("Jamoaviy musobaqasining nomini kiriting (yoki tugatish uchun 'stop') -> ")

    if not competition_name:
        print("Siz musobaqa nomini kiritmadingiz. Iltimos qayta urinib ko'ring!")
    elif competition_name == stop:
        print("Jamoa musobaqalarni qo'shish tugallandi.")
        break
    else:
        add_competition(team_competitions_list, competition_name)

# Conducting team competitions and adding points
for team_competition in team_competitions_list:
    conduct_team_competition(team_list, team_competition)

# Adding individual competitions
while True:
    competition_name = input("Individual musobaqasining nomini kiriting (yoki tugatish uchun 'stop') -> ")

    if not competition_name:
        print("Siz musobaqa nomini kiritmadingiz. Iltimos qayta urinib ko'ring!")
    elif competition_name == stop:
        print("Individual musobaqalarni qo'shish tugallandi.")
        break
    else:
        add_competition(individual_competitions_list, competition_name)

# Conducting individual competitions and adding points
for individual_competition in individual_competitions_list:
    conduct_individual_competition(individual_list, individual_competition)

# Displaying final scores
print("\nYakuniy ballar:")
display_all_contestants(team_list + individual_list)

# Determine winners
determine_team_winner(team_list)
determine_individual_winner(individual_list)
