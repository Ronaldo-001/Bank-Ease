import os

def check_transaction_files():
    """ Reads the created transaction files and applies three if-else conditions. """
    transaction_files = sorted([f for f in os.listdir('.') if f.startswith("transaction_") and f.endswith(".txt")])
    
    if not transaction_files:
        print("❌ No transaction files found!")
        return
    
    for file in transaction_files:
        with open(file, "r") as f:
            content = f.read().strip()
            
        print(f"📂 Processing {file}: {content}")
        
        # Applying three if-else conditions
        if "error" in content.lower():
            print(f"🚨 Alert: {file} contains an error message!")
        elif content.isdigit():
            print(f"✅ {file} contains a numeric value: {content}")
        else:
            print(f"ℹ️ {file} contains a general text: {content}")

if __name__ == "__main__":
    check_transaction_files()