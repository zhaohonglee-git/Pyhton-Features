# E = mc²
c = 300_000_000


def energy(mass: float) -> float:
    return mass * (c**2)


m = 1.0
print(energy(m))
print("******")

energy_lambda = lambda mass: mass * (c**2)
print(energy_lambda(m))


sum = lambda number1, number2: number1 + number2

print(sum(3, 5))
print("&&&&")


directors = [
    {"name": "Kubrick", "age": 41},
    {"name": "Jiajia", "age": 24},
    {"name": "Shuang", "age": 43},
    {"name": "Zhaohong", "age": 18},
]

print(sorted(directors, key=lambda directors: directors["name"]))
print(max(directors, key=lambda directors: directors["age"]))
