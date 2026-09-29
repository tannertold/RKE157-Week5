#Kirjuta programm, mis käib läbi iga tähe sõnas ja prindib selle välja.

text = "hello"
""" for i in text:
    print(i) """

#Prindi sõna tagurpidi (viimasest tähemärgist esimese juurde, iga täht sõnast kuvatakse eraldi reale tagurpidi järjekorras).

length = len(text)
print(length)

for letter in range(len(text) -1, -1, -1):
    print(text[letter])


