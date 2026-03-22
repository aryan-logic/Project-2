import numpy as np
import pandas as pd

print("--------------------------------------")
print("Welcome To The Students Marks Analyzer")
print("--------------------------------------")


def get_marks(subject):
            while True:
                try:
                    marks = int(input(f"Enter his/her {subject} marks :"))
                    if marks < 0 or marks >100 :
                        print("Marks must be not less than 0 or greater than 100")
                        continue 
                    return marks
                
                except ValueError:
                    print("Marks Should be a number")
while True:
    try: # Input 
        choice = int(input("Enter Your Choice (1-4) \n" \
        "1.Add Student\n" \
        "2.View Data\n" \
        "3.Analyze Data\n" \
        "4.Exit -> "))
    except ValueError:
        print("Your Choice Must be a number (1-4)")
        continue
        # Adding the Students to the list
    if choice == 1:
        df = pd.read_csv("Students.csv")

        # Using the functions properly 
        name = input("Enter the name of the student : ")
        maths = get_marks("maths")
        physics = get_marks("physics")
        chemistry = get_marks("chemistry")
        biology = get_marks("biology")
        english = get_marks("english")

        new_df = {    # New DataFrame
            "name":name,
            "maths":maths,
            "physics":physics,
            "chemistry":chemistry,
            "biology":biology,
            "english":english
        }

        df = pd.concat([df,pd.DataFrame([new_df])],ignore_index=True)
        df.to_csv("Students.csv" , index=False)
        print("---------------------------")
        print("Student Added Successfully ✅")
        print("---------------------------") # Added the Student
        # Exit  
    if choice == 4:
        print("--------------------")
        print("Thanks For Visiting ")
        print("--------------------")
        break

    if choice ==2:
        df = pd.read_csv("Students.csv")
        if df.empty :
            print("No student data found. Please add students first.")
        else : 
            print(df)


    if choice == 3 :
        df = pd.read_csv("Students.csv")
        if df.empty :
             print("No student data found. Please add students first.")

        else :
            df["Average"] = df[["maths", "physics", "chemistry", "biology", "english"]].mean(axis=1)

            index = df["Average"].idxmax()
            topper = df.loc[index]
            print("---------------------------")
            print(f"Topper : {topper['name']}")
            print(f"Average : {topper['Average']}")
            print("---------------------------")

            low_index = df["Average"].idxmin()
            lowest_marks= df.loc[low_index]
            print()
            print("---------------------------")
            print(f"Lowest Marks Student:{lowest_marks['name']}")
            print(f"Lowest Average -> {lowest_marks['Average']}")
            print("---------------------------")

            marks_array = df[["maths", "physics", "chemistry", "biology", "english"]].values

            class_avg = np.mean(marks_array)
            print("---------------------------")
            print(f"class Average:  {class_avg}")
            print("----------------------------")

            