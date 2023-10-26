# SEOT_3
# Rapport for GitHub Actions Oppsett med Python, pytest og Conda

Prosedyre

For å oppnå dette, ble følgende trinn fulgt:

- **Opprettelse av Repository**: Opprettet et nytt repository på GitHub for å hoste koden og testene fra oppgave 2.
- **Innlegging av Kode**: La til Python-koden og testene (skrevet med `pytest`) til det nye repositoryet.
- **Oppsett av GitHub Actions**:
    - Laget en ny `.github/workflows/python-package-conda.yml` fil i repoen.
    - Denne filen definerer en workflow som setter opp Python via Conda, installerer nødvendige avhengigheter (inkludert `pytest`), og kjører testene.
- **Testkjøring**: Etter å ha satt opp workflowen, ble en testcommit og push utført for å verifisere at GitHub Actions kjørte testene som forventet ved hjelp av Conda.

## 3. Resultater

Etter å ha pushet endringene til GitHub, ble "Actions"-fanen i repoet sjekket.

- Testene ble automatisk kjørt ved hver push ved hjelp av Conda.
- GitHub Actions-loggen viste at testene kjørte som forventet og passerte uten feil.

## Bilder:
![[Pasted image 20231026191938.png]]
![[Pasted image 20231026191947.png]]
![[Pasted image 20231026192004.png]]
