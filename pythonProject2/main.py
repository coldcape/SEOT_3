# For å kjøre pytest så trenger du bare å ha prosjektet åpent i terminalen og skrive "pytest"
def isLeapYear(year):
    # Om året er delelig med 4 og ikke delelig med 100
    # Eller at året er delelig med 400, da er det et skuddår.
    # Så TRUE
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    # Ellers så falsk
    else:
        return False

# Denne blokken er for manuell testing.
# Når 'main.py' blir kjørt så kan du inpute år du ønsker å kjøre en test på for å sjekke om det er et skuddår.
if __name__ == "__main__":

    year = int(input("Tast inn året du ønsker å sjekke: "))
    if isLeapYear(year):
        print(f"{year} er et skuddår.")
    else:
        print(f"{year} er ikke et skuddår.")
