"""
mil = km / 1.609344
"""

def get_km():
    return float(input("Kilometreyi giriniz: "))

def km_to_mile(km):
    return km / 1.609344

if __name__ == "__main__":
    km = get_km()
    print("Mili:", km_to_mile(km))