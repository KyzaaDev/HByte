import hashlib
from prettytable import PrettyTable


def banner():
    print("""

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██╗░░░██╗██████╗░██╗░░██╗░█████╗░░██████╗██╗░░██╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██║░░░██║██╔══██╗██║░░██║██╔══██╗██╔════╝██║░░██║
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██║░░░██║██████╔╝███████║███████║╚█████╗░███████║
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██║░░░██║██╔══██╗██╔══██║██╔══██║░╚═══██╗██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗╚██████╔╝██║░░██║██║░░██║██║░░██║██████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
                Made by: @KyzaaDev                            
""")

def madeTablehash():
    print("Available hash algorithms:")
    # membuat tabel untuk menampilkan algoritma hash
    # dan informasi terkaitnya
    table = PrettyTable()
    table.field_names = ["Algorithm", "Digest size", "Block size", "Hash example"]

    # menetapkan panjang maksimum dari contoh hash yang ditampilkan
    max_length = 32

    # menapilkan beberapa algoritma yang tersedia di semua platform
    for algoritma in hashlib.algorithms_guaranteed:

        # membuat variable yang menampung informasi tentang algoritma hash
        # seperti ukuran digest, ukuran blok, dan contoh hash berdasarkan hash yang telah ditentukan
        nameAlgorithm = hashlib.new(algoritma)
        digest_size = nameAlgorithm.digest_size
        block_size = nameAlgorithm.block_size
        nameAlgorithm.update(b"password123")

        # operator logika untuk menentukan apakah algoritma tersebut adalah shake
        # jika iya, maka hash_example akan dihasilkan dengan panjang 16 byte. Dan akan mengembalikan nilai utuh jika hash tidak lebih dari 32 byte
        if "shake_" in algoritma:
            hash_example = nameAlgorithm.hexdigest(16)
        else:
            hash_example = nameAlgorithm.hexdigest()
        if len(hash_example) > max_length:
            hash_example = hash_example[:max_length] + "..."
        
        # memasukkan informasi ke dalam tabel yang telah dibuat
        table.add_row([f"{algoritma}", f"{digest_size}", f"{block_size}", f"{hash_example}"])
    
    return table

# bagian kode yang menyimpan function pada menu
def hashMessages(pesan, algorithm="sha256"):
    try:
        ubahHash = hashlib.new(algorithm)
        ubahHash.update(pesan.encode())
        return ubahHash.hexdigest()
    except ValueError:
        return None

def hashTypes(hashInput):
    panjangHex = bytes.fromhex(hashInput)  # Menghitung panjang byte dari string yang diinputkan
    panjangByte = len(panjangHex)  # Menghitung panjang byte dari string yang diinputkan

    print(f"Byte dari string  anda adalah {panjangByte} byte\n")

    kemungkinanHash = []

    for algoritma in hashlib.algorithms_guaranteed:
        panjangHash = hashlib.new(algoritma).digest_size

        if panjangByte == panjangHash:
            kemungkinanHash.append(algoritma)
        

    print(f"Possible hashes: ")
    for possibleHashes in kemungkinanHash:
        print(f"[+] {possibleHashes}")
    return kemungkinanHash


def modeMenu():
    print("\n")
    choose = PrettyTable()
    choose.field_names = ["Mode", "Description"]
    hashMess = choose.add_row(["1", "Hash a message"])
    hashType = choose.add_row(["2", "Check hash types"])
    checkHash = choose.add_row(["3", "Check a hash"])
    keluar = choose.add_row(["4", "Exit"])
    return choose

def chooseMode():
    choose = input("\nChoose a mode (1-4): ")

    if choose == "1":
        message = input("Input the message to hash: ")
        algorithm = input("input the hash algorithm (default: sha256): ") or "sha256"

        if algorithm not in hashlib.algorithms_guaranteed:
            print("Invalid algorithm. Please choose from the available algorithms.")
            return chooseMode()

        hashedMessage = hashMessages(message, algorithm)
        return print("Your hashed message: " + hashedMessage + " <= " + algorithm)
    
    elif choose == "2":
        inputHash = input("Mari Tebak hash anda: ").strip()
        typeHash = hashTypes(inputHash)


if __name__ == "__main__":
    banner()
    print(madeTablehash())
    print(modeMenu())
    chooseMode()
# lanjut ntar malem bang, mau main game dulu