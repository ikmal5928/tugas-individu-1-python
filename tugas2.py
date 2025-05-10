from datetime import datetime

def hitung_umur():
    nama = input("Masukkan nama Anda: ")
    try:
        tahun_lahir_str = input("Masukkan tahun lahir Anda : ")
        tahun_lahir = int(tahun_lahir_str)
        tahun_sekarang = datetime.now().year
        umur = tahun_sekarang - tahun_lahir

        if umur < 0:
            print("Tahun lahir yang Anda masukkan tidak valid.")
        else:
            print(f"Halo {nama}, umur Anda saat ini adalah {umur} tahun.")
    except ValueError:
        print("Input tahun lahir tidak valid. Pastikan Anda memasukkan angka tahun.")

if __name__ == "__main__":
    hitung_umur()