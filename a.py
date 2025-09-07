library = {}

def add_book():
    title = input("Enter book title: ")  #  إدخال عنوان الكتاب
    author = input("Enter author name: ")  #  إدخال اسم المؤلف
    year = input("Enter publication year: ")  #  إدخال سنة النشر
    library[title] = {'author': author, 'year': year}  # إضافة الكتاب كمفتاح مع المؤلف وسنة النشر كقيمة
    print("Book added successfully!")

def view_books():
    if library:
        for title, details in library.items():
            print(f"Title: {title}, Author: {details['author']}, Year: {details['year']}")
    else:
        print("No books available.")

def search_book():
    title = input("Enter book title to search: ")
    if title in library:
        print(f"Found: Title: {title}, Author: {library[title]['author']}, Year: {library[title]['year']}")
    else:
        print(f"Book '{title}' not found.")

def delete_book():
    title = input("Enter book title to delete: ")
    if title in library:
        del library[title]
        print(f"Book '{title}' deleted.")
    else:
        print(f"Book '{title}' not found.")

while True:
    print("\n=== Library Management System ===")
    print("1. Add a book")
    print("2. Show all books")
    print("3. Search for a book")
    print("4. Delete a book")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == '1':
        add_book()  #   إضافة كتاب
    elif choice == '2':
        view_books()  #  عرض الكتب
    elif choice == '3':
        search_book()  # البحث عن كتاب
    elif choice == '4':
        delete_book()  #  حذف كتاب
    elif choice == '5':
        print("Exiting... Goodbye!")  #  الخروج
        break
    else:
        print("Invalid choice! Please try again.")  # إذا اختار المستخدم خيار غير صحيح
