import hashlib, argparse, sys

# parser = argparse.ArgumentParser(description = "MD5 cracker")
# parser.add_argument("-md5", dest="hash", help="md5 hash", required=True)
# parser.add_argument("-w", dest="wordlist", help="wordlist", required=True)
# parsed_args = parser.parse_args()

# def md5_main():
#     cracked = ""
#     with open(parsed_args.wordlist) as file:
#         for line in file: 
#             line = line.strip()
#             if hashlib.md5(bytes(line, encoding="utf-8")).hexdigest() == parsed_args.hash:
#                 cracked = line
#                 print("Hash Cracked. Value is %s"%line)
#             if cracked == "":
#                 print("Failed to crack hash")

def md5_main():
    cracked = ""
    hash = input("Enter MD5 Hash: ")
    wordlist = input("Enter Wordlist: ")
    with open(wordlist) as file:
        for line in file: 
            line = line.strip()
            if hashlib.md5(bytes(line, encoding="utf-8")).hexdigest() == hash:
                cracked = line
                print("Hash Cracked. Value is %s"%line)
                break
            if cracked == "":
                print("Failed to crack hash")

if __name__ == "__main__":
    md5_main()