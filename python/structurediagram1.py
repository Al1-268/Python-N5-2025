
sd = []
totaldur = 0
duration = int(input("Enter the duration of the training session in minutes: "))

while totaldur < duration:
    duration = int(input("Enter the duration of the song in minutes: "))
    sd.append(duration)
    totaldur = sum(sd)
print(str(totaldur) + " minutes")
