from time import sleep

def countdown(n):
    for i in range(n):
        print(n)
        n-=1
        sleep(1)

loendus = int(input("Sisestage taimeri sekundid"))

print(countdown(loendus))
    