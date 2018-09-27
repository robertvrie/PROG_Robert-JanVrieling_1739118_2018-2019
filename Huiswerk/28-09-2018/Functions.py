print("\n------ 1. Functie met 3 parameters ------")
def optellen(getal1,getal2,getal3):
    antwoord = getal1 + getal2 + getal3
    return antwoord

getal1invoer = 1 #int(input("Geef het eerste getal: "))
getal2invoer = 1 #int(input("Geef het tweede getal: "))
getal3invoer = 1 #int(input("Geef het derde getal: "))

print(optellen(getal1invoer,getal2invoer,getal3invoer))


print("\n------ 2. Functie met list-parameter ------")
def som(getallenLijst):
    return sum(getallenLijst)

nummerLijst = [1,2,3,4,5,6,7,8,9,10,11,12]
print(som(nummerLijst))


print("\n------ 3. Functie met if ------")
def lang_genoeg(lengte):
    if lengte < 120:
        return "Sorry, je bent te klein!"
    else:
        return "Je bent lang genoeg voor de attractie!"

lengte = 120 #int(input("Hoe lang ben je in centimeters?"))
print(lang_genoeg(lengte))


print("\n------ 4. Functie met if ------")
def new_password(oldpassword,newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        return "Je wachtwoord is succesvol gewijzigd"
    else:
        return "Dat wachtwoord komt overeen met je oude wachtwoord of is niet lang genoeg."

oldpassword = "abcdef" #str(input("Wat is je oude wachtwoord?"))
newpassword = "asdfgh" #str(input("Wat is je nieuwe wachtwoord?"))
print(new_password(oldpassword,newpassword))


print("\n------ 5. Functie met list-parameter en for-loop  ------")
def kwadraten_som(grondgetallen):
    for idx,item in enumerate(grondgetallen):
        if (idx+1) <= 10:
            if grondgetallen[idx] < 0:
                continue
            else:
                grondgetallenLijst.append(grondgetallen[idx] ** 2)
    return sum(grondgetallenLijst)

grondgetallenLijst = []
cijfers = [4,5,3,-81]
print("De som van de getallen is:",kwadraten_som(cijfers))

print("\n------ 6. Functie met (im)mutable parameter ------")
def wijzig(letterlijst):
    for i in range(0,4,1):
        if i > 0:
            letterlijst.pop()
            if letterlijst == []:
                print("De lege lijst:",letterlijst)
    letterlijst.extend(("d","e","f"))

lijst = ["a","b","c"]
lengte = len(lijst)
print("Lijst voor de wijziging:",lijst)
wijzig(lijst)
print("Lijst na de wijziging:",lijst)

#vraag 1: Dan leeg je de lijst niet, je vervangt dan gelijk wat er al stond
#vraag 2: De functie werkt niet met een string, omdat hij probeert in de parameter letterLijst de laatste waarde zoekt van een lijst, maar die bestaat niet, want het is een string
#vraag 3: Mutabiliteit zorgt ervoor dat de lijst kan worden leeggemaakt en nieuwe objects weer toegevoegd kunnen worden