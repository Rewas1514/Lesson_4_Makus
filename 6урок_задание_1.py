with open('nginx_logs.txt') as c:
    data = []
    for line in c:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"',''),splitted[6]))

print(data)
