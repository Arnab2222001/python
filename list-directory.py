alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

list = []
for i in range(5):
    alien_0 = {'color': 'green', 'points': 5}
    list.append(alien_0)
print(list)
for aline in (list[:5]):
    print(aline)
