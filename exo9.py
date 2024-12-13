# Magical World City Population Calculator

def calculate_city_population():
    cities = {}

    while True:
        # Ask the user for the city name
        city_name = input("Enter the name of a city (or type 'stop' to finish): ").strip()

        # Stop the input phase if the user types 'stop'
        if city_name.lower() == "stop":
            break

        # Calculate the population based on the length of the city name
        population = len(city_name) * 1_000_000
        cities[city_name] = population

    # Sort the cities by population from largest to smallest
    sorted_cities = list(cities.items())
    sorted_cities.sort(key=lambda x: x[1], reverse=True)

    # Print the cities and their populations in order
    print("\nCity populations (largest to smallest):")
    for city, population in sorted_cities:
        print(f"{city}: {population:,} citizens")

# Run the program
calculate_city_population()
