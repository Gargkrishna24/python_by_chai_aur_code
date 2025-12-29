from pathlib import Path

def list_directory_contents():
    """List all files/folders in current directory"""
    path = Path('.').resolve()  # Current directory
    items = list(path.rglob('*'))  # All files recursively
    print("\n📁 Current Directory Contents:")
    for i, item in enumerate(items, 1):
        print(f"{i:2d} : {item.name:<20} {'📄' if item.is_file() else '📁'}")
    print("-" * 50)

def create_file():
    """Create new file with content"""
    try:
        list_directory_contents()
        name = input("\n📝 Enter file name (with .txt): ").strip()
        p = Path(name)
        
        if not p.exists():  # Fixed: exists() not exist()
            with open(p, "w", encoding='utf-8') as fs:
                data = input("✏️  What to write: ")
                fs.write(data)
            print(f"✅ File '{name}' CREATED successfully!")
        else:
            print(f"❌ File '{name}' already exists!")
            
    except Exception as err:
        print(f"❌ Error creating file: {err}")

def read_file():
    """Read existing file content"""
    try:
        list_directory_contents()
        name = input("\n📖 Enter file name: ").strip()
        p = Path(name)
        
        if p.exists() and p.is_file():  # Fixed: exists()
            with open(p, 'r', encoding='utf-8') as fs:
                data = fs.read()
            print(f"\n📄 Content of '{name}':")
            print("-" * 40)
            print(data)
        else:
            print(f"❌ File '{name}' does not exist or is not a file!")
            
    except Exception as err:
        print(f"❌ Error reading file: {err}")

def update_file():
    """Append content to existing file"""
    try:
        list_directory_contents()
        name = input("\n🔄 Enter file name to update: ").strip()
        p = Path(name)
        
        if p.exists() and p.is_file():
            with open(p, 'a', encoding='utf-8') as fs:  # 'a' = append
                data = input("➕ What to append: ")
                fs.write("\n" + data)  # Add newline
            print(f"✅ File '{name}' UPDATED!")
        else:
            print(f"❌ File '{name}' does not exist!")
            
    except Exception as err:
        print(f"❌ Error updating file: {err}")

def delete_file():
    """Delete existing file"""
    try:
        list_directory_contents()
        name = input("\n🗑️  Enter file name to delete: ").strip()
        p = Path(name)
        
        if p.exists() and p.is_file():
            confirm = input(f"⚠️  Delete '{name}'? (y/N): ").lower()
            if confirm == 'y':
                p.unlink()  # Delete file
                print(f"✅ File '{name}' DELETED!")
            else:
                print("❌ Deletion cancelled.")
        else:
            print(f"❌ File '{name}' does not exist!")
            
    except Exception as err:
        print(f"❌ Error deleting file: {err}")

# MAIN MENU
print("🔧 FILE MANAGER")
print("=" * 40)
print("1️⃣  Create File")
print("2️⃣  Read File") 
print("3️⃣  Update File")
print("4️⃣  Delete File")
print("5️⃣  Exit")
print("=" * 40)

while True:
    try:
        choice = int(input("\n🎯 Enter your choice (1-5): "))
        
        if choice == 1:
            create_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            update_file()
        elif choice == 4:
            delete_file()
        elif choice == 5:
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Enter 1-5")
            
    except ValueError:
        print("❌ Enter a valid number!")
    except KeyboardInterrupt:
        print("\n👋 Exiting...")
        break
