# https://www.beecrowd.com.br/judge/pt/problems/view/1019


seconds = int(input())

hours = 0
minutes = 0

while seconds >= 60:
    minutes += 1
    seconds -= 60

    if minutes >= 60:
        hours += 1
        minutes -= 60

print(f"{hours}:{minutes}:{seconds}")