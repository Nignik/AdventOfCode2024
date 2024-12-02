with open("kalendarz2.txt","r") as file:
    lines=file.read().splitlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split()
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
safe = 0
for liczba in lines:
    for i in range(len(liczba)):
        if liczba[0] > liczba[1]:
            if liczba[i-1] < liczba[i]:
                break
            else:
                safe +=1
                break
        if liczba[0] < liczba[1]:
            if liczba[i-1] > liczba[i]:
                break
            else:
                safe +=1
                break

print(safe)