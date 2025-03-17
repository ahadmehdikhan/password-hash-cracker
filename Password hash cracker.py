import hashlib

def crack_hash(hash_value, wordlist, hash_type):
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
            for password in file:
                password = password.strip()
                hashed_pass = None
                
                if hash_type == "md5":
                    hashed_pass = hashlib.md5(password.encode()).hexdigest()
                elif hash_type == "sha1":
                    hashed_pass = hashlib.sha1(password.encode()).hexdigest()
                elif hash_type == "sha256":
                    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
                else:
                    print("[!] Unsupported hash type! Use md5, sha1, or sha256.")
                    return
                
                if hashed_pass == hash_value:
                    print(f"[+] Password Found: {password}")
                    return
        print("[-] Password Not Found in Wordlist")
    except FileNotFoundError:
        print("[!] Wordlist file not found. Please provide a valid file.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    hash_value = input("Enter the hashed password: ").strip()
    hash_type = input("Enter the hash type (md5, sha1, sha256): ").strip().lower()
    wordlist = input("Enter the path to the wordlist file: ").strip()
    
    crack_hash(hash_value, wordlist, hash_type)
