planets = {
    "jupiter": 2.360,
    "neptune": 1.140,
    "saturn": 1.081,
    "uranus": 0.815,
    "mars": 0.378,
    "mercury": 0.376,
    "venus": 0.889
}

for planet in planets:
    print(planet, end=" ")

def calculateWeight(planet: str, weight: float):
    if planet.lower() not in planets:
        print(f"{planet} not a planet")
        planet = input("Enter your planet: ")
        print(f"The equivalent on {planet}:", round((weight * planets[planet.lower()]), 2))
    else:
        print(f"The equivalent on {planet}:", round((weight * planets[planet.lower()]), 2))

while True:   
    try:
        calculateWeight(input("Enter your planet: "), float(input("Enter your weight: ")))
    except:
        print("Incorrect values!")
    else: 
        break
