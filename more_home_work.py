class Building:
    total = 0

    def __init__(self):
        Building.total = self.total + 1


count = 1
builds = Building()
while count < 40:
    new_builds = Building()
    print(Building.total)
    count += 1
