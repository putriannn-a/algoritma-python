print("Selamat datang di Kalkulator Sederhana!")
print("Anda dapat melakukan operasi penjumlahan, pengurangan, perkalian, dan pembagian.")

def calculator():

    while True: 
        try: 
            angka_pertama = int(input("Masukkan angka pertama: "))
            break
        except ValueError:
            print("Error: Input harus berupa angka. Coba lagi!")
            continue

    while True:
        try:
            angka_kedua = int(input("Masukkan angka kedua: "))
            break
        except ValueError:
            print("Error: Input harus berupa angka. Coba lagi!")
            continue

    operasi = input("Masukkan operasi yang diinginkan (+, -, *, /): ").lower()

    if operasi == "+":
        hasil = angka_pertama + angka_kedua
        print(f"Hasil dari {angka_pertama} + {angka_kedua} = {hasil}")
    elif operasi == "-":
        hasil = angka_pertama - angka_kedua
        print(f"Hasil dari {angka_pertama} - {angka_kedua} = {hasil}")
    elif operasi == "*":
        hasil = angka_pertama * angka_kedua
        print(f"Hasil dari {angka_pertama} * {angka_kedua} = {hasil}")
    elif operasi == "/":
        if angka_kedua != 0:
            hasil = angka_pertama / angka_kedua
            print(f"Hasil dari {angka_pertama} / {angka_kedua} = {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        print("Operasi tidak valid. Silakan pilih antara tambah, kurang, kali, atau bagi.")
        
while True:
    calculator()
    while True:
        lanjut = input("\nHitung lagi? (y/n): ").strip().lower()
        if lanjut == 'y':
            calculator()
        elif lanjut == 'n':
            print("Terima kasih telah menggunakan kalkulator!")
            exit()
        else:
            print("Input tidak valid. Silakan masukkan 'y' untuk ya atau 'n' untuk tidak.")
        