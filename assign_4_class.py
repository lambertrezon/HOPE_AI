class FindPercent:
    def percentage():
        for mark in marks:
            print(f"Subject {mark.index(mark) + 1}: {mark}")
        total_marks = sum(mark)
        percentage = (total_marks / (len(mark) * 100)) * 100
        print(total_marks, percentage)

class SubfieldsInAI:
    def Subfields():
        subfields = [
            "Machine learning",
            "Neuralnetworks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        print("Sub-fields in AI are:")
        for subfield in subfields:
            print(subfield)

class OddEven:
    def OddEven(num):
        if num % 2 == 0:
            print(f"The number {num} is Even.")
        else:
            print(f"The number {num} is Odd.")

class EligibilityForMarriage:
    def Eligible(gender, age):
        if gender.lower() == "male":
            if age >= 21:
                print(f"Male, age {age}: Eligible for marriage.")
            else:
                print(f"Male, age {age}: Not eligible for marriage.")
        elif gender.lower() == "female":
            if age >= 18:
                print(f"Female, age {age}: Eligible for marriage.")
            else:
                print(f"Female, age {age}: Not eligible for marriage.")
        else:
            print("Invalid gender. Please specify 'male' or 'female'.")

class Triangle:
    def area(height, breadth):
        area = (height * breadth) / 2
        print(f"The area of the triangle is {area}")

    def perimeter(side1, side2, base):
        perimeter = side1 + side2 + base
        print(f"The perimeter of the triangle is {perimeter}")