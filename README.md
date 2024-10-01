# Mini Project 1 Daspro
Nama : Fikri Abiyyu Rahman NIM : 2409116063

Flowchart :
![Untitled Diagram drawio (1)](https://github.com/user-attachments/assets/b48dcaa1-1c69-4c9c-991a-cd5f94a80bb0)

Output Terminal :
![Screenshot 2024-09-30 015801](https://github.com/user-attachments/assets/60233f9b-128c-43ea-b310-a581266d086d)

Penjelesan Kode :
1. import getpass
   #ini fungsinya biar kita bisa input password tanpa kelihatan di layar, jadi lebih aman.
   
2. print("Silahkan masukkan username dan password baru")
   print("--------------------------------------------")

   username_1 = input('silahkan username baru anda : ')
   password_1 = input('silahkan password baru anda : ')
   print('\n-----------DATA TELAH DIKONFIRMASI-------')
   #ini untuk membuat username dan password baru.

3. while kesempatan > 0: 
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
    #ini untuk mengkonfirmasi ulang username dan password, jika user salah memasukkan username dan password lebih dari 3x, maka user akan program         akan berhenti
   #dibagian ini ada perulangan yang akan terus jalan selama "kesempatan" masih lebih dari 0. dalam perulangan ini kita disuruh input username dan        password kembali. Kalau username dan password yang kita input sama dengan yang pertama, berarti login berhasil dan kita keluar dari perulangan.
