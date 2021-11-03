teori = float(input("input nilai teori: "))
praktek = float(input("input nilai praktek: "))

if teori >= 70 and praktek >= 70:
    print ("Selamat, anda lulus!")
elif teori >= 70 and praktek <= 70:
    print ("Anda harus mengulang ujian praktek.")
elif teori <= 70 and praktek >= 70:
    print ("Anda harus mengulang ujian teori.") 
else:
    print("Anda harus mengulang ujian teori dan praktek.")