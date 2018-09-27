def standaardPrijs(afstandKM):
    if afstandKM < 0:
        prijs = 0
        return prijs
    else:
        if afstandKM >= 50:
            prijs = (1.40 * afstandKM) + 15
            return prijs
        else:
            prijs = 0.80 * afstandKM
            return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
        if leeftijd < 12 or leeftijd >= 65:
            if weekendrit == "ja":
                kosten = standaardPrijs(afstandKM) * 0.65
                return kosten
            else:
                kosten = standaardPrijs(afstandKM) * 0.70
                return kosten
        else:
            if weekendrit == "ja":
                kosten = standaardPrijs(afstandKM) * 0.60
                return kosten
            else:
                return standaardPrijs(afstandKM)


leeftijd = int(input("Hoed oud ben je? "))
weekendrit = input("Heb je een weekendrit gemaakt? ")
afstandKM = float(input("Hoeveel KM heb je gereisd? "))

print("Je kosten zijn:",ritprijs(leeftijd,weekendrit,afstandKM))