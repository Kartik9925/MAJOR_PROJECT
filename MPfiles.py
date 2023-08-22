import pandas as pd
import random
import csv
import sys
from faker import Faker
fake=Faker
sys.exit()
class Data():
    a={"Id":['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52',
        '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'],
        "NAME":["Raju singh", "Aanya Gupta", "Aditi Sharma", "Akash Patel", "Aman Singh", "Amrita Verma", "Anika Choudhury",
    "Arjun Mehta", "Avani Desai", "Chirag Joshi", "Deepika Kapoor", "Dev Shah", "Eesha Reddy", "Gaurav Yadav",
    "Ishaan Malhotra", "Jasmine Bhatia", "Kabir Agarwal", "Kavya Nair", "Lakshay Menon", "Mira Iyer",
    "Neha Khanna", "Nikhil Rana", "Palak Datta", "Pranav Chawla", "Priya Kumar", "Rahul Mathur", "Riya Shah",
    "Rohan Gupta", "Sanya Singh", "Shivam Saxena", "Shreya Sharma", "Siddharth Verma", "Sneha Patel",
    "Sohan Kumar", "Sonia Bajaj", "Tanvi Oberoi", "Utkarsh Rawat", "Vedika Singh", "Vikram Mehta", "Yash Gupta",
    "Zara Malhotra", "Amit Kapoor", "Anushka Singh", "Ayush Sharma", "Bhavya Srinivasan", "Charul Reddy",
    "Dhruv Patel", "Divya Iyer", "Eshaan Kapoor", "Farhan Khan", "Gayatri Patel", "Harsh Shah", "Ishika Sharma",
    "Jay Verma", "Juhi Gupta", "Kritika Sharma", "Manish Patel", "Meera Menon", "Naman Gupta", "Natasha Reddy",
    "Omkar Sharma", "Pooja Patel", "Rajat Agarwal", "Rashi Kapoor", "Samaira Kumar", "Samir Gupta",
    "Tanisha Patel", "Urmila Sharma", "Varun Yadav", "Vidya Iyer", "Yuvraj Singh", "Zoya Khan",
    "Aarush Sharma", "Aditi Patel", "Akshay Kumar", "Ayesha Verma", "Bhavna Gupta", "Chaitanya Rao",
    "Disha Patel", "Eva Menon", "Faisal Khan", "Gia Malhotra", "Hemant Singh", "Ira Shah", "Jai Kumar",
    "Kajal Reddy", "Lavanya Kapoor", "Mayank Agarwal", "Nehal Verma", "Ojas Patel", "Pari Sharma",
    "Rahil Khan", "Ria Choudhury", "Samar Patel", "Sanya Kapoor", "Tanya Sharma", "Uday Verma",
    "Vanya Singh", "Vihaan Yadav", "Zain Kumar"
]}
    df=pd.DataFrame(a)


    try:
     def mn(self):
        a="".join(random.choice(["9",'8','7','6','5','4','3','5'])for i in range(8))
        b=random.choice(['9','8'])
        return b+a
     
    except Exception as e:
     pass


    try:
     def age(self):
        a=random.choice(['17','15','16','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','42','41','43','45','50','51','52','53','56','57','58','59','60','61','62','63','64','65','67','68','69','70'])
        return a
    
    except Exception as e:
       pass


    try:
     def ad(self):
        a=random.choice(["Mumbai_bandra","Mumbai_Malad","Mumbai_Thane","NaviMumbai_Aeroli","Pune_Katraj","Nagpur_Hingna","Banglore_East",'Nagpur_pratapnagar',"Wardha","Delhi_Gurgaon"])
        b=random.choice(["1",'2','3','4','5','5','6','7','10','9'])
        c=a+" "+"Ward"+" "+b
        return c
    
    except Exception as e:
     df["ADD"]=[fake.addd()for i in range(100)]


    try:
     def tr(self):
        a=random.choice(['Diabetes', 'Cancer', "Alzheimer's", "Parkinson's", 'HIV/AIDS', 'Tuberculosis', 'Malaria', 'Influenza', 'Hypertension', 
    'Arthritis', 'Asthma', 'Hepatitis', 'Heart Disease', 'Stroke', 'Osteoporosis', 'Epilepsy', 'Multiple Sclerosis', 
    'Celiac Disease', 'Lyme Disease', 'Polio', 'Dengue Fever', "Crohn's Disease", 'Psoriasis', 'Glaucoma', 'Bipolar Disorder', 
    'Leukemia', 'Melanoma', 'Cholera', 'Ebola', 'Anemia', 'Gout', 'Chronic Kidney Disease', 'Osteoarthritis', 'Rheumatoid Arthritis', 
    'Bronchitis', 'Cystic Fibrosis', 'Endometriosis', 'Hemorrhoids', 'Gallstones', 'Jaundice', 'Lupus', 'Measles', 'Migraine', 
    'Obesity', 'Peptic Ulcer', 'Pneumonia', 'Rabies', 'Sarcoidosis', 'Scoliosis', 'Tetanus', 'Thyroid Disorders', 'Tinnitus', 
    'Varicose Veins', 'Vitiligo', 'Wilson Disease', 'Yellow Fever', 'Zika Virus', 'Ovarian Cancer', 'Pancreatitis', 
    'Prostate Cancer', 'Testicular Cancer', 'Leukemia'])
        return a
    
    except Exception as e:
     df["TR"]=[fake.tr()for i in range(100)]


    try:
     def doc(self):
        a=random.choice(["Aditi Patel", "Aarav Sharma", "Ananya Gupta", "Arjun Mehta", "Alisha Singh", "Bhavesh Patel", "Chitra Iyer",
    "Deepak Verma", "Eshaan Kumar", "Fatima Khan", "Gaurav Rao", "Hemant Agarwal", "Ishika Joshi", "Jai Nair",
    "Kajal Chopra", "Karthik Sharma", "Lavanya Reddy", "Manish Das", "Nisha Khanna", "Naveen Kapoor",
    "Omkar Yadav", "Priya Malik", "Pranav Bhatia", "Rahul Rastogi", "Ria Srinivasan", "Sahil Varma",
    "Sanya Choudhury", "Tanvi Desai", "Uday Oberoi", "Vijay Rao", "Vidya Menon", "Yash Patel",
    "Zara Khan", "Amit Mishra", "Aanya Sahu", "Akash Chawla", "Ayush Patel", "Bhavya Singh", "Chirag Gupta",
    "Divya Verma", "Devika Mathur", "Eesha Saxena", "Farhan Iqbal", "Gia Patel", "Harsh Shah", "Ishaan Das",
    "Juhi Sharma", "Karan Mehta", "Khushi Sengupta", "Lakshay Kumar", "Mira Choudhury", "Nandini Srinivasan",
    "Nikhil Rao", "Palak Sharma", "Parth Kapoor", "Pooja Rana", "Rohan Sharma", "Riya Kumar", "Saisha Nambiar",
    "Samir Gupta", "Siddharth Sharma", "Sneha Das", "Sohan Patel", "Sonia Choudhury", "Trisha Iyer",
    "Urmila Verma", "Vikram Yadav", "Vivaan Chawla", "Varun Kapoor", "Yuvraj Singh", "Zoya Nair",
    "Aarushi Menon", "Aditya Khanna", "Ayesha Gupta", "Akshay Iyer", "Bhavna Sharma", "Chaitanya Das",
    "Dhruv Sahu", "Eva Mehta", "Faisal Ali", "Gauri Nambiar", "Hrishita Patel"])
        return "Dr."+a
    
    except Exception as e:
     df["DOCTOR_NAME"]=[fake.dr()for i in range(100)]


    try:
     def fi(self):
        a=random.choice(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'])
        b=random.choice(['1','2','3','4','5','6'])
        c="2022"
        return a+"/"+b+"/"+c
    
    except Exception as e:
     pass
    

    try:
     def si(self):
        a=random.choice(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'])
        b=random.choice(['7','8','9','10','11','12'])
        c="2022"
        return a+"/"+b+"/"+c
    
    except Exception as e:

     df["S-INSPECTION"]=[fake.datess()for i in range(100)]
     

    try:
     def md(self):
        a=random.choice(["Insulin", "Metformin", "Adriamycin", "Taxol", 
                     "Imatinib", "Pembrolizumab", "Donepezil", "Memantine", "Levodopa", 
                     "Pramipexole", "Tenofovir", "Lamivudine", "Isoniazid", "Rifampicin", 
                     "Artemether-Lumefantrine", "Oseltamivir", "Zanamivir", "Lisinopril", 
                     "Atenolol", "Acetaminophen", "Ibuprofen", "Aspirin", "Prednisone", 
                     "Hydrochlorothiazide", "Losartan", "Metoprolol", "Omeprazole", 
                     "Pantoprazole", "Simvastatin", "Atorvastatin", "Warfarin", 
                     "Clopidogrel", "Furosemide", "Amoxicillin", "Azithromycin", "Ciprofloxacin", "Doxycycline", "Fluconazole", "Gabapentin", "Pregabalin", "Sertraline", "Fluoxetine",
                       "Paroxetine", "Escitalopram", "Atorvastatin", "Levothyroxine", "Albuterol", "Montelukast", "Sertraline", "Fluoxetine", "Paroxetine", "Escitalopram"
])
        b=random.choice(["Insulin", "Metformin", "Adriamycin", "Taxol", 
                     "Imatinib", "Pembrolizumab", "Donepezil", "Memantine", "Levodopa", 
                     "Pramipexole", "Tenofovir", "Lamivudine", "Isoniazid", "Rifampicin", 
                     "Artemether-Lumefantrine", "Oseltamivir", "Zanamivir", "Lisinopril", 
                     "Atenolol", "Acetaminophen", "Ibuprofen", "Aspirin", "Prednisone", 
                     "Hydrochlorothiazide", "Losartan", "Metoprolol", "Omeprazole", 
                     "Pantoprazole", "Simvastatin", "Atorvastatin", "Warfarin", 
                     "Clopidogrel", "Furosemide", "Amoxicillin", "Azithromycin", "Ciprofloxacin", "Doxycycline", "Fluconazole", "Gabapentin", "Pregabalin", "Sertraline", "Fluoxetine",
                       "Paroxetine", "Escitalopram", "Atorvastatin", "Levothyroxine", "Albuterol", "Montelukast", "Sertraline", "Fluoxetine", "Paroxetine", "Escitalopram"])
        
        c=random.choice(["Insulin", "Metformin", "Adriamycin", "Taxol", 
                     "Imatinib", "Pembrolizumab", "Donepezil", "Memantine", "Levodopa", 
                     "Pramipexole", "Tenofovir", "Lamivudine", "Isoniazid", "Rifampicin", 
                     "Artemether-Lumefantrine", "Oseltamivir", "Zanamivir", "Lisinopril", 
                     "Atenolol", "Acetaminophen", "Ibuprofen", "Aspirin", "Prednisone", 
                     "Hydrochlorothiazide", "Losartan", "Metoprolol", "Omeprazole", 
                     "Pantoprazole", "Simvastatin", "Atorvastatin", "Warfarin", 
                     "Clopidogrel", "Furosemide", "Amoxicillin", "Azithromycin", "Ciprofloxacin", "Doxycycline", "Fluconazole", "Gabapentin", "Pregabalin", "Sertraline", "Fluoxetine",
                       "Paroxetine", "Escitalopram", "Atorvastatin", "Levothyroxine", "Albuterol", "Montelukast", "Sertraline", "Fluoxetine", "Paroxetine", "Escitalopram"])
        return a+" "+b+" "+c
    
    except Exception as e:
     df["MEDICINES"]=[fake.medicines()for i in range(100)]
   
    
    try:
        def p(self):
            a=random.choice(["Wearing_mask",'',"","",'Engage in low-impact exercise',"","Maintain a healthy weight","","Use assistive devices if needed","","","Practice good hygiene, including washing hands regularly"])
            return a
        
    except Exception as e:
        df.fake.precaution()


a1=Data()        

m1= list(map(lambda x: a1.mn(), range(100)))
a1.df["MOBILE_NUMBER"]=m1

ag= list(map(lambda x: a1.age(), range(100)))
a1.df["AGE"]=ag

d1= list(map(lambda x: a1.ad(), range(100)))
a1.df["ADDRESS"]=d1

t= list(map(lambda x: a1.tr(), range(100)))
a1.df['TREATMENT']=t

d= list(map(lambda x: a1.doc(), range(100)))
a1.df["DOCTOR_NAME"]=d

f= list(map(lambda x: a1.fi(), range(100)))
a1.df["FIRST_INSPECTION"]=f

s=list(map(lambda x: a1.si(),range(100)))
a1.df['SECOND_INSPECTION']=s

md1= list(map(lambda x: a1.md(), range(100)))
a1.df["MEDICIENS_NAME"]=md1

pc= list(map(lambda x: a1.p(), range(100)))
a1.df["PRECAUTION"]=pc





a1.df.to_csv('Pharma_data.csv')

print(a1.df)



import pandas as pd
import csv
import sys 
sys.exit()
df=pd.DataFrame()
a={"Id":['1', '2', '3', '4', '5', '6', '7', '8', '9', 
         '10', '11', '12', '13', '14', '15', '16', '17',
           '18', '19', '20', '21', '22', '23', '24', '25', 
           '26', '27', '28', '29', '30', '31', '32', '33', 
           '34', '35', '36', '37', '38', '39', '40', '41', 
           '42', '43', '44', '45', '46', '47', '48', '49', 
           '50', '51', '52','53', '54', '55', '56', '57', 
           '58', '59', '60', '61', '62', '63', '64', '65', 
           '66', '67', '68', '69', '70', '71', '72', '73', 
           '74', '75', '76', '77', '78', '79', '80', '81', 
           '82', '83', '84', '85', '86', '87', '88', '89', 
           '90', '91', '92', '93', '94', '95', '96', '97',
           '98', '99', '100'],"DOCTOR_NAME":["Dr.Eva Mehta", "Dr.Zara Khan", "Dr.Saisha Nambiar", "Dr.Eesha Saxena",
    "Dr.Vidya Menon", "Dr.Bhavesh Patel", "Dr.Pooja Rana", "Dr.Hemant Agarwal",
    "Dr.Farhan Iqbal", "Dr.Aarav Sharma", "Dr.Nisha Khanna", "Dr.Parth Kapoor",
    "Dr.Nisha Khanna", "Dr.Pranav Bhatia", "Dr.Priya Malik", "Dr.Karthik Sharma",
    "Dr.Farhan Iqbal", "Dr.Priya Malik", "Dr.Divya Verma", "Dr.Hemant Agarwal",
    "Dr.Tanvi Desai", "Dr.Urmila Verma", "Dr.Amit Mishra", "Dr.Eva Mehta",
    "Dr.Aditi Patel", "Dr.Hrishita Patel", "Dr.Rahul Rastogi", "Dr.Sanya Choudhury",
    "Dr.Chirag Gupta", "Dr.Mira Choudhury", "Dr.Chitra Iyer", "Dr.Sahil Varma",
    "Dr.Ayush Patel", "Dr.Gia Patel", "Dr.Rohan Sharma", "Dr.Parth Kapoor",
    "Dr.Juhi Sharma", "Dr.Chitra Iyer", "Dr.Hemant Agarwal", "Dr.Nisha Khanna",
    "Dr.Chirag Gupta", "Dr.Palak Sharma", "Dr.Priya Malik", "Dr.Tanvi Desai",
    "Dr.Riya Kumar", "Dr.Priya Malik", "Dr.Riya Kumar", "Dr.Vivaan Chawla",
    "Dr.Chaitanya Das", "Dr.Yash Patel", "Dr.Eshaan Kumar", "Dr.Hrishita Patel",
    "Dr.Palak Sharma", "Dr.Uday Oberoi", "Dr.Gauri Nambiar", "Dr.Eesha Saxena",
    "Dr.Siddharth Sharma", "Dr.Rahul Rastogi", "Dr.Bhavesh Patel", "Dr.Trisha Iyer",
    "Dr.Arjun Mehta", "Dr.Manish Das", "Dr.Kajal Chopra", "Dr.Jai Nair",
    "Dr.Gauri Nambiar", "Dr.Faisal Ali", "Dr.Sonia Choudhury", "Dr.Saisha Nambiar",
    "Dr.Riya Kumar", "Dr.Bhavesh Patel", "Dr.Zoya Nair", "Dr.Urmila Verma",
    "Dr.Bhavya Singh", "Dr.Lakshay Kumar", "Dr.Gauri Nambiar", "Dr.Trisha Iyer",
    "Dr.Samir Gupta", "Dr.Dhruv Sahu", "Dr.Nandini Srinivasan", "Dr.Bhavya Singh",
    "Dr.Dhruv Sahu", "Dr.Saisha Nambiar", "Dr.Rohan Sharma", "Dr.Karan Mehta",
    "Dr.Sohan Patel", "Dr.Mira Choudhury", "Dr.Sahil Varma", "Dr.Ishika Joshi",
    "Dr.Vivaan Chawla", "Dr.Palak Sharma", "Dr.Gaurav Rao", "Dr.Parth Kapoor",
    "Dr.Ananya Gupta", "Dr.Ananya Gupta", "Dr.Chaitanya Das", "Dr.Yuvraj Singh",
    "Dr.Lakshay Kumar", "Dr.Khushi Sengupta", "Dr.Harsh Shah", "Dr.Zoya Nair"
]
    ,"TREATMENT": [
    "Gallstones", "Cholera", "Ebola", "Jaundice", "Dengue Fever",
    "Chronic Kidney Disease", "Peptic Ulcer", "Obesity", "Lupus",
    "Crohn's Disease", "Glaucoma", "Peptic Ulcer", "Chronic Kidney Disease",
    "Bronchitis", "Tuberculosis", "Epilepsy", "Chronic Kidney Disease",
    "Anemia", "Influenza", "Crohn's Disease", "Hemorrhoids", "Gout",
    "Parkinson's", "Psoriasis", "Anemia", "Vitiligo", "Jaundice", "Hemorrhoids",
    "Obesity", "Alzheimer's", "Bronchitis", "Ovarian Cancer", "Anemia",
    "Influenza", "Bronchitis", "Tetanus", "Bipolar Disorder", "Malaria",
    "Crohn's Disease", "Vitiligo", "Glaucoma", "Scoliosis", "Gout",
    "Gallstones", "Varicose Veins", "Melanoma", "Melanoma", "Yellow Fever",
    "Multiple Sclerosis", "Migraine", "Crohn's Disease", "Cholera", "HIV/AIDS",
    "Lyme Disease", "Asthma", "Parkinson's", "Arthritis", "Epilepsy", "Measles",
    "Polio", "Cystic Fibrosis", "Lupus", "Sarcoidosis", "Rabies", "Crohn's Disease",
    "Zika Virus", "Bipolar Disorder", "Obesity", "Endometriosis", "Tuberculosis",
    "Rabies", "Wilson Disease", "Obesity", "Leukemia", "Anemia", "Leukemia",
    "Crohn's Disease", "Polio", "HIV/AIDS", "Leukemia", "Rheumatoid Arthritis",
    "Pneumonia", "Stroke", "Bipolar Disorder", "Malaria", "Celiac Disease",
    "Vitiligo", "Hemorrhoids", "Leukemia", "Arthritis", "Celiac Disease",
    "Endometriosis", "Rheumatoid Arthritis", "Jaundice", "Osteoarthritis",
    "Pneumonia", "Malaria", "Yellow Fever", "Rheumatoid Arthritis",
    "Varicose Veins"],"MEDICENS":["Albuterol Levodopa Paroxetine", "Atorvastatin Imatinib Pramipexole",
    "Montelukast Fluconazole Paroxetine", "Albuterol Aspirin Oseltamivir",
    "Prednisone Oseltamivir Escitalopram", "Doxycycline Fluoxetine Donepezil",
    "Imatinib Clopidogrel Ibuprofen", "Fluoxetine Oseltamivir Taxol",
    "Azithromycin Gabapentin Escitalopram", "Adriamycin Isoniazid Atorvastatin",
    "Rifampicin Fluoxetine Pramipexole", "Insulin Tenofovir Atorvastatin",
    "Zanamivir Ibuprofen Tenofovir", "Atenolol Aspirin Rifampicin",
    "Sertraline Isoniazid Adriamycin", "Fluoxetine Donepezil Simvastatin",
    "Rifampicin Rifampicin Montelukast", "Prednisone Amoxicillin Ibuprofen",
    "Azithromycin Losartan Levothyroxine", "Insulin Pramipexole Sertraline",
    "Clopidogrel Paroxetine Omeprazole", "Azithromycin Metformin Losartan",
    "Azithromycin Metformin Fluconazole", "Adriamycin Gabapentin Donepezil",
    "Omeprazole Clopidogrel Warfarin", "Memantine Escitalopram Isoniazid",
    "Prednisone Doxycycline Ibuprofen", "Ciprofloxacin Omeprazole Doxycycline",
    "Imatinib Escitalopram Levothyroxine", "Aspirin Escitalopram Insulin",
    "Escitalopram Doxycycline Tenofovir", "Lisinopril Levothyroxine Warfarin",
    "Gabapentin Sertraline Pregabalin", "Warfarin Omeprazole Pramipexole",
    "Metformin Pembrolizumab Atorvastatin", "Levothyroxine Aspirin Atorvastatin",
    "Donepezil Montelukast Pembrolizumab", "Furosemide Doxycycline Sertraline",
    "Artemether-Lumefantrine Pramipexole Prednisone",
    "Ibuprofen Artemether-Lumefantrine Imatinib", "Warfarin Tenofovir Insulin",
    "Metformin Escitalopram Artemether-Lumefantrine",
    "Oseltamivir Pembrolizumab Pantoprazole",
    "Levodopa Tenofovir Atorvastatin", "Metoprolol Levothyroxine Tenofovir",
    "Donepezil Rifampicin Oseltamivir", "Atorvastatin Pembrolizumab Omeprazole",
    "Pantoprazole Levothyroxine Isoniazid", "Rifampicin Amoxicillin Atenolol",
    "Prednisone Atorvastatin Artemether-Lumefantrine",
    "Hydrochlorothiazide Pregabalin Pembrolizumab",
    "Aspirin Furosemide Pregabalin", "Atorvastatin Doxycycline Doxycycline",
    "Imatinib Atorvastatin Imatinib", "Pembrolizumab Metformin Ibuprofen",
    "Sertraline Lamivudine Metoprolol", "Levodopa Levothyroxine Hydrochlorothiazide",
    "Atorvastatin Azithromycin Montelukast", "Metoprolol Metformin Atorvastatin",
    "Pantoprazole Acetaminophen Isoniazid", "Montelukast Pregabalin Isoniazid",
    "Pantoprazole Ibuprofen Ciprofloxacin", "Metoprolol Donepezil Isoniazid",
    "Atorvastatin Gabapentin Fluoxetine", "Ibuprofen Lamivudine Ibuprofen",
    "Ibuprofen Lamivudine Gabapentin", "Losartan Ibuprofen Azithromycin",
    "Escitalopram Memantine Paroxetine", "Amoxicillin Fluconazole Donepezil",
    "Atenolol Adriamycin Hydrochlorothiazide", "Lisinopril Amoxicillin Pantoprazole",
    "Sertraline Metformin Furosemide", "Fluoxetine Rifampicin Simvastatin",
    "Lisinopril Memantine Pramipexole", "Sertraline Hydrochlorothiazide Isoniazid",
    "Clopidogrel Rifampicin Simvastatin", "Oseltamivir Zanamivir Metformin",
    "Zanamivir Pembrolizumab Ibuprofen", "Memantine Pantoprazole Adriamycin",
    "Amoxicillin Atorvastatin Pantoprazole", "Gabapentin Adriamycin Acetaminophen",
    "Levodopa Atorvastatin Isoniazid", "Paroxetine Atenolol Simvastatin",
    "Lisinopril Pembrolizumab Levodopa", "Pregabalin Escitalopram Escitalopram",
    "Fluoxetine Pramipexole Sertraline", "Gabapentin Paroxetine Atorvastatin",
    "Furosemide Pembrolizumab Zanamivir", "Prednisone Oseltamivir Insulin",
    "Gabapentin Aspirin Atenolol", "Atorvastatin Lamivudine Atorvastatin",
    "Donepezil Atorvastatin Montelukast", "Fluconazole Warfarin Sertraline",
    "Escitalopram Isoniazid Sertraline", "Zanamivir Paroxetine Doxycycline",
    "Isoniazid Insulin Pantoprazole", "Pregabalin Isoniazid Pregabalin",
    "Atorvastatin Albuterol Warfarin", "Donepezil Artemether-Lumefantrine Lisinopril",
    "Furosemide Ibuprofen Metoprolol"]}
df=pd.DataFrame(a)
df.to_csv("Medical_det.csv")
print(df)








