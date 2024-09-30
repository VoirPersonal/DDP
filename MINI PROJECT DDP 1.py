# Memasukkan username dan password baru

import getpass
kesempatan = 3

print("Silahkan masukkan username dan password baru")
print("--------------------------------------------")

username_1 = input('silahkan username baru anda : ')
password_1 = input('silahkan password baru anda : ')
print('\n-----------DATA TELAH DIKONFIRMASI-------')

# Melakukan konfirmasi username dan password
# Diberikan 3x kesempatan jika gagal, jika lebih akses ditolak

while kesempatan > 0: 
    username_2 = input('\nmasukkan username anda : ')
    password_2 = getpass.getpass('masukkan kata sandi : ')
    if username_2==username_1 and password_2==password_1:
        print('----------------------------------------------')
        print(f'Login terkonfirmasi, selamat datang {username_1}..')
        print('----------------------------------------------')
        break
    elif kesempatan >= 2:
        print('----------------------------------------------')
        print('Username dan password tidak sesuai, silahkan coba lagi..')
        print('----------------------------------------------')
        kesempatan -= 1
    else:
        kesempatan -=1

# Memasukkan lama jam kerja dan tarif kerja per jam
# Jika lebih > 165 akan mendapatkan bonus 10%, jika < 160 tidak akan mendapatkan bonus

if kesempatan >= 1:
    while True:
        Lama_Jam_Kerja = int(input("Masukkan lama jam kerja : "))
        if Lama_Jam_Kerja == 0:
            break
        Tarif_Kerja_Per_Jam = int(input("Masukkan tarif kerja per-jam : "))
        if Tarif_Kerja_Per_Jam == 0:
            break
        Gaji = Lama_Jam_Kerja * Tarif_Kerja_Per_Jam
        if Lama_Jam_Kerja > 160 :
            print((Lama_Jam_Kerja - 160) * (Tarif_Kerja_Per_Jam * 10/100) + Gaji)
        elif Lama_Jam_Kerja <= 160 :
            print(Gaji)
        pengulangan = (input("Apakah anda ingin menghitung ulang (Y/N) : "))
        if pengulangan == "N":
            print("Terimakasih silahkan kembali lagi")
            break
        
else:
    print("Kesempatan habis. Akses anda ditolak.")
