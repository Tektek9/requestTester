import requests
print("|===\\ TES")
print("|   |")
print("|---/")
print("|   \\")
print("URL Respon Tester")
print("Created By KuliOnline11")
a = input(str("Silahkan masukan url: "))
response = requests.get(a)

if response.status_code == 200 :
    print("\n OK Konek BOSKUH \n")
else:
    print("\n BEJATT KONEKSINE \n ")    