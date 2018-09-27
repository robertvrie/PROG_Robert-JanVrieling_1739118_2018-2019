print("------1. If Statement------")
score = 18 #float(input("Wat was de score van je multiplechoice toets? "))
if score <= 15:
    print("Sorry, je hebt het niet gehaald.")
else:
    print("Gefeliciteerd, je hebt het gehaald.")


print("\n------2. If met 2 boolean operators------")
leeftijd = 18 #int(input("Hoe oud ben je? "))
paspoort = "ja" #input("Heb je een nederlands paspoort? ")
if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen.")
else:
    print("Je mag niet stemmen.")


print("\n------3. If/Else------")
leeftijd = 18 #int(input("Hoe oud ben je? "))
paspoort = "ja" #input("Heb je een nederlands paspoort? ")
if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen.")
else:
    print("Je mag niet stemmen.")

print("\n------4. For, if en strings------")
dagen = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]
teller = -1
for x in dagen:
    teller += 1
    if teller <= 6:
        print(dagen[teller][0:2])


print("\n------5. For, if en numbers------")
dagen = [1,2,3,4,5,6,7,8,9,10]
teller = -1
for x in dagen:
    teller += 1
    if teller <= 9:
        bereken = dagen[teller] % 2
        if bereken == 0:
            print(dagen[teller])


print("\n------6. For, if en vowels------")
s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = "aeiouy"

for char in s:
    if char in klinkers:
        print(char)