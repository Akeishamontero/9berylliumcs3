class Patient: #Create Parent Class
    def __init__(self, name, bill_amount): #Initalize the class with name and bill amount
        self.name = name #Initialize patient name
        self.bill_amount = bill_amount #Initialize bill amount

#METHODS 

    def get_name(self): #Get the name of the patient
        return self.name #Return the name of the patient

    def set_name(self, name): #Set the name of the patient
        self.name = name #Set the name of the patient

    def get_bill_amount(self): #Get the bill amount of the patient
        return self.bill_amount #Return the bill amount of the patient

    def set_bill_amount(self, bill_amount: float): #Set the bill amount of the patient
        self.bill_amount = bill_amount #Set the bill amount of the patient

    def display_info(self): #Display the information of the patient
        print(f"Patient Name: {self.name}, Bill Amount: ${self.bill_amount:.2f}")

    def calculate_bill(self): #Calculate the bill amount of the patient
        return self.bill_amount #Return the bill amount of the patient 

    def display_patient_type(self): #Display the information of the patient
        print("Patient Type: Regular Patient") #Display the patient type as regular patient

#Create Child Class 1

class Senior_Patient(Patient): #Create Child Class 1
    
    def calculate_bill(self): #Override the calculate_bill method
        discount = 0.8 #Set the discount to 20% for senior patients
        discounted_amount = self.bill_amount * discount #Calculate the discounted amount
        return discounted_amount #Return the discounted amount
    
    def display_patient_type(self): #Override the display_patient_type method
        print("Patient Type: Senior Citizen") #Display the patient type as senior citizen

class PhilHealth_Patient(Patient): #Create Child Class 2
    
    def calculate_bill(self): #Override the calculate_bill method
        discount = 0.85 #Set the discount to 15% for PhilHealth patients
        discounted_amount = self.bill_amount * discount #Calculate the discounted amount
        return discounted_amount #Return the discounted amount
    
    def display_patient_type(self): #Override the display_patient_type method
        print("Patient Type: PhilHealth Patient") #Display the patient type as PhilHealth patient

#OBJECTS
p1 = Patient("Juan Dela Cruz", 15000.00)
p2 = Senior_Patient("Maria Santos", 15000.00)
p3 = PhilHealth_Patient("Pedro Reyes", 15000.00)

#PRINTING THE INFORMATION OF THE PATIENTS

print("Hospital Billing System") # Prints the title "Hospital Billing System"
print("-----------------------")
print("Patient Name:", p1.get_name()) # Prints "Patient Name: Juan Dela Cruz"
p1.display_patient_type() # Prints "Patient Type: Regular Patient"
print("Original Bill:", f"₱{p1.get_bill_amount():,.2f}") # Prints "Original Bill: ₱15000.00"
print("Final Bill:", f"₱{p1.calculate_bill():,.2f}") # Prints "Final Bill: ₱15000.00"

print()

print("Patient Name:", p2.get_name()) # Prints "Patient Name: Maria Santos"
p2.display_patient_type() # Prints "Patient Type: Senior Citizen"
print("Original Bill:", f"₱{p2.get_bill_amount():,.2f}") # Prints "Original Bill: ₱15000.00"
print("Final Bill:", f"₱{p2.calculate_bill():,.2f}")

print()

print("Patient Name:", p3.get_name()) # Prints "Patient Name: Pedro Reyes"
p3.display_patient_type() # Prints "Patient Type: PhilHealth Patient"
print("Original Bill:", f"₱{p3.get_bill_amount():,.2f}") # Prints "Original Bill: ₱15000.00"
print("Final Bill:", f"₱{p3.calculate_bill():,.2f}") # Prints "Final Bill: ₱12750.00"
