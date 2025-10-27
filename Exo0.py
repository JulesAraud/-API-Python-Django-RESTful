def longueur_dernier_mot(s: str) -> int:
    i = len(s) - 1

    while i >= 0 and s[i] == ' ':
        i -= 1

    longueur = 0
    while i >= 0 and s[i] != ' ':
        longueur += 1
        i -= 1
    return longueur


print(longueur_dernier_mot("Hello World"))
