def main():
    print("*"*40)
    print("\n:: COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print('\nPress 1. Insert a new Course\n')
    print('Press 2. Show all courses\n')
    print('Press 3. Delete a course (NEED ID OF COURSE)\n')
    print("#"*40)
    print("\n")

    choice = input("\n Enter a choice: ")

    if choice == "1":
        name = input("\n Enter course name: ")
        description = input("\n Enter course description: ")
        price = input("\n Enter course price: ")
        private = input("\n Is this course private (0/1): ")

        if db.insert_data([name, description, price, private]):
            print("Course was inserted successfully")
        else:
            print("OOPS SOMEthing is wrong")


    elif choice == "2":
        print("\n:: Course List ::")

        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no : " + str(index + 1))
            print("Course ID : " + str(item[0]))
            print("Course Name : " + str(item[1]))
            print("Course description : " + str(item[2]))
            print("Course Price : " + str(item[3]))
            private = 'Yes' if item[4] else 'NO'
            print("Is Private : " + private)
            print("\n")

    elif choice == "3":
        record_id = input("Enter the course ID: ")

        if db.delete_data(record_id):
            print("Course was deleted with a success")
        else:
            print("OOPS SOMETHING WENT WRONG")

    else:
        print("\n BAD CHOICE")      



if __name__ == '__main__':
    main()