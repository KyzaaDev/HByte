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
    for algorithm in hashlib.algorithms_guaranteed:

        # membuat variable yang menampung informasi tentang algoritma hash
        # seperti ukuran digest, ukuran blok, dan contoh hash berdasarkan hash yang telah ditentukan
        hash_instance = hashlib.new(algorithm)
        digest_size = hash_instance.digest_size
        block_size = hash_instance.block_size
        hash_instance.update(b"password123")
        upper_algorithm = algorithm.upper()

        # operator logika untuk menentukan apakah algoritma tersebut adalah shake
        # jika iya, maka hash_example akan dihasilkan dengan panjang 16 byte. Dan akan mengembalikan nilai utuh jika hash tidak lebih dari 32 byte
        if "shake_" in algorithm:
            hash_example = hash_instance.hexdigest(16)
        else:
            hash_example = hash_instance.hexdigest()
        if len(hash_example) > max_length:
            hash_example = hash_example[:max_length] + "..."
        
        # memasukkan informasi ke dalam tabel yang telah dibuat
        table.add_row([f"{upper_algorithm}", f"{digest_size}", f"{block_size}", f"{hash_example}"])
    
    return table

# bagian kode yang menyimpan function pada menu
def hashMessages(message, algorithm="sha256"):
    try: 
        if algorithm not in hashlib.algorithms_guaranteed:
            return None
        else:
            hash_object = hashlib.new(algorithm)
            hash_object.update(message.encode())
            
            if "shake_" in algorithm:
                hash_length = int(input("🔢 Enter the hash length you want: "))
                hashed_message  = hash_object.hexdigest(hash_length)
            else:
                hashed_message = hash_object.hexdigest()


            print("\n" + "="*40)
            print(f"[✔ ] Hashed Message with {algorithm.upper()}:")
            print(f"📄 {hashed_message}")
            print("="*40)

            input("⏎ Press enter to return to the main menu....")

            return hashed_message

    except ValueError:
        return None

def hashTypes(hash_input):
    try:
        hex_bytes = bytes.fromhex(hash_input)  # Menghitung panjang byte dari string yang diinputkan
        byte_length = len(hex_bytes)  # Menghitung panjang byte dari string yang diinputkan

        print(f"🔍 Hash byte length: {byte_length} byte\n")

        possible_hashes = []

        for algorithm in hashlib.algorithms_guaranteed:
            hash_size = hashlib.new(algorithm).digest_size

            if byte_length == hash_size:
                possible_hashes.append(algorithm)
        

        print(f"💡 Possible algorithms: ")
        for possible_hash in possible_hashes:
            print(f"[+] {possible_hash}")
        return possible_hashes

    except ValueError:
        print("❌ Hex not valid!")
        return None

def compareHash(expected_hash, input_hash):
    if expected_hash == input_hash:
        return "✅ Hash matches."
    else:
        return "❌ Hash doesn't match."

def modeMenu():
    print("\n📂 Available mode: ")
    choose_table = PrettyTable()
    choose_table.field_names = ["Mode", "Description"]
    hash_mess = choose_table.add_row(["1", "🔏 Hash password"])
    hash_type = choose_table.add_row(["2", "🧠 Check hash types"])
    check_hash = choose_table.add_row(["3", "🔎 Check a hash"])
    hash_compare = choose_table.add_row(["4", "📦 Hash Comparison"])
    keluar = choose_table.add_row(["5", "🚪 Exit"])
    return choose_table

def chooseMode():
    while True:
        user_choice = input("\n👉 Choose a mode (1-5): ").strip()

        if user_choice == "1":
            print("\n⚠️ Note: Spaces are part of the hashed message!")
            message = input("✉️ Input the message to hash: ")
            algorithm = input("⚙️ input the hash algorithm (default: sha256): ") or "sha256"
            
            if hashMessages(message, algorithm.lower()):
                continue
            print("❗ Invalid algorithm. Please choose from the available algorithms.")
    
        elif user_choice == "2":
            input_hash = input("Let's Guess your hash: ").strip()
            type_hash = hashTypes(input_hash)

        elif user_choice == "4":
            expected_hash = input("Enter the original hash: ")
            input_hash = input("Enter the hash to compare: ")
            print(compareHash(expected_hash, input_hash))
        
        elif user_choice == "5":
            exit_confirmation = input("Are you sure want to get out? (y/n): ")
            if exit_confirmation.lower() == "y":
                print("Bye Bye!!")
                break

            elif exit_confirmation.lower() == "n": 
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