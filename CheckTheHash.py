import hashlib
from prettytable import PrettyTable


def banner():
    print("""
██╗  ██╗██████╗ ██╗   ██╗████████╗███████╗
██║  ██║██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
███████║██████╔╝ ╚████╔╝    ██║   █████╗  
██╔══██║██╔══██╗  ╚██╔╝     ██║   ██╔══╝  
██║  ██║██████╔╝   ██║      ██║   ███████╗
╚═╝  ╚═╝╚═════╝    ╚═╝      ╚═╝   ╚══════╝ 
    Made by: @KyzaaDev                            
""")

def madeTablehash():
    print("🔐 Available hash algorithms:")
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
        upperAlgorithm = algoritma.upper()

        # operator logika untuk menentukan apakah algoritma tersebut adalah shake
        # jika iya, maka hash_example akan dihasilkan dengan panjang 16 byte. Dan akan mengembalikan nilai utuh jika hash tidak lebih dari 32 byte
        if "shake_" in algoritma:
            hash_example = nameAlgorithm.hexdigest(16)
        else:
            hash_example = nameAlgorithm.hexdigest()
        if len(hash_example) > max_length:
            hash_example = hash_example[:max_length] + "..."
        
        # memasukkan informasi ke dalam tabel yang telah dibuat
        table.add_row([f"{upperAlgorithm}", f"{digest_size}", f"{block_size}", f"{hash_example}"])
    
    return table

# bagian kode yang menyimpan function pada menu
def hashMessages(message, algorithm="sha256"):
    try: 
        if algorithm not in hashlib.algorithms_guaranteed:
            return None
        else:
            ubahHash = hashlib.new(algorithm)
            ubahHash.update(message.encode())
            
            if "shake_" in algorithm:
                panjangHash = int(input("🔢 Enter the hash length you want: "))
                hashedMessage  = ubahHash.hexdigest(panjangHash)
            else:
                hashedMessage = ubahHash.hexdigest()


            print("\n" + "="*40)
            print(f"[✔ ] Hashed Message with {algorithm.upper()}:")
            print(f"📄 {hashedMessage}")
            print("="*40)

            input("⏎ Press enter to return to the main menu....")

            return hashedMessage

    except ValueError:
        return None

def hashTypes(hashInput):
    try:
        panjangHex = bytes.fromhex(hashInput)  # Menghitung panjang byte dari string yang diinputkan
        panjangByte = len(panjangHex)  # Menghitung panjang byte dari string yang diinputkan

        print(f"🔍 Hash byte length: {panjangByte} byte\n")

        kemungkinanHash = []

        for algoritma in hashlib.algorithms_guaranteed:
            panjangHash = hashlib.new(algoritma).digest_size

            if panjangByte == panjangHash:
                kemungkinanHash.append(algoritma)
        

        print(f"💡 Possible algorithms: ")
        for possibleHashes in kemungkinanHash:
            print(f"[+] {possibleHashes}")
        return kemungkinanHash

    except ValueError:
        print("❌ Hex not valid!")
        return None

def compareHash(expectedHash, inputHash):
    if expectedHash == inputHash:
        return "✅ Hash matches."
    else:
        return "❌ Hash doesn't match."

def modeMenu():
    print("\n📂 Available mode: ")
    choose = PrettyTable()
    choose.field_names = ["Mode", "Description"]
    hashMess = choose.add_row(["1", "🔏 Hash password"])
    hashType = choose.add_row(["2", "🧠 Check hash types"])
    checkHash = choose.add_row(["3", "🔎 Check a hash"])
    hashCompare = choose.add_row(["4", "📦 Hash Comparison"])
    keluar = choose.add_row(["5", "🚪 Exit"])
    return choose

def chooseMode():
    while True:
        choose = input("\n👉 Choose a mode (1-5): ").strip()

        if choose == "1":
            print("\n⚠️ Note: Spaces are part of the hashed message!")
            message = input("✉️ Input the message to hash: ")
            algorithm = input("⚙️ input the hash algorithm (default: sha256): ") or "sha256"
            
            if hashMessages(message, algorithm.lower()):
                continue
            print("❗ Invalid algorithm. Please choose from the available algorithms.")
    
        elif choose == "2":
            inputHash = input("Let's Guess your hash: ").strip()
            typeHash = hashTypes(inputHash)

        elif choose == "4":
            expectedHash = input("Enter the original hash: ")
            inputHash = input("Enter the hash to compare: ")
            print(compareHash(expectedHash, inputHash))
        
        elif choose == "5":
            keluar = input("Are you sure want to get out? (y/n): ")
            if keluar.lower() == "y":
                print("Bye Bye!!")
                break

            elif rillkh.lower() == "n": 
                continue

            else:
                print("Input is invalid!")
                continue

        else:
            print("❗ Invalid input, please try again!!")
            continue

def main():
    banner()
    print(madeTablehash())
    print(modeMenu())
    chooseMode()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram stoped by user, BYE!")