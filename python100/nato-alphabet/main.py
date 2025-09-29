import pandas as pd

# SOLUTION: Fixed Windows file path issue using raw string
# The 'r' prefix tells Python to treat backslashes as literal characters

try:
    # Method 1: Raw string (r"") - Recommended for Windows paths
    nato_df = pd.read_csv(r"D:\pythonlearning\python100\nato-alphabet\nato_phonetic_alphabet.csv")
    nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
    
    def generate_nato():
        user_input = input("Enter a word: ").upper()
        try:
            output_list = [nato_dict[letter] for letter in user_input]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
            generate_nato()
        else:   
            print(output_list)
    
    generate_nato()
    
except ImportError:
    print("❌ Error: pandas is not installed.")
    print("Install it with: pip install pandas")
except FileNotFoundError:
    print("❌ Error: CSV file not found.")
    print("Make sure nato_phonetic_alphabet.csv exists in the current directory.")
except Exception as e:
    print(f"❌ Error: {e}")

