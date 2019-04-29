# Importing pandas
import pandas as pd

# For menu purpose
from numpy import array, arange, any


# Make monk.csv as data
data = pd.read_csv('monk.csv')

# Rearrange class column to the last column
kolom = data.pop('class')
data['class'] = kolom

# making model as 3D list
model = []
for i in range(len(data.columns)-1):
    model.append([])
    ikr = 0
    for j in sorted(data[data.columns[i]].unique()):
        model[i].append([])
        model[i][ikr].append(len(data[data[data.columns[i]]==j][data[data[data.columns[i]]==j]['class'] == 0]))
        model[i][ikr].append(len(data[data[data.columns[i]]==j][data[data[data.columns[i]]==j]['class'] == 1]))
        ikr += 1

# Implement laplace estimator to data
for k in range(len(data.columns)-1):
    for l in range(len(model[k])):
        model[k][l] = [n+1 for n in model[k][l]]

# Transform the data to 0 - 1 range
for m in range(len(data.columns)-1):
    for n in range(len(model[m])):
        model[m][n] = [x/sum(model[m][n]) for x in model[m][n]]

# Applying Naive Bayes formula
def hitung(a,b,c,d,e,f):
        for n in range(len(data["class"].unique())):
                nilai_prob[n] = model[0][a][n]*model[1][b][n]*model[2][c][n]*model[3][d][n]*model[4][e][n]*model[5][f][n]*(len(data[data["class"]==n])/len(data))
                
                total = sum(nilai_prob.values())
                
        for i in range(len(nilai_prob)):
                nilai_prob[i]=nilai_prob[i]/total
                                
# Make yes or no classification and print the results
def penentu():
        if (nilai_prob[0] > nilai_prob[1]):
                print(nama,"| Result : No")
        else:
                print(nama,"| Result : Yes")
                                
        print(nilai_prob)


# yes or no classification
nilai_prob = {}


def inputNumber(prompt):
        while True:
                try:
                        num = float(input(prompt))
                        break
                except ValueError:
                        pass
        return num

def displayMenu(options):
        for i in range(len(options)):
                print("{:d}. {:s}".format(i+1, options[i]))
        
        choice = 0
        while not(any(choice == arange(len(options))+1)):
                choice = inputNumber("Masukkan Pilihan: ")
        
        return choice

#define menu items
menuItems = array(["Masukkan Data", "Tampilkan Prediksi", "Tampilkan Nilai Tiap Kolom", "Keluar"])

while True:
        # Display menu
        choice = displayMenu(menuItems)

        # Enter data of patient
        if choice == 1:
                global nama, head_shape, body_shape, is_smiling, holding, jacket_color, has_tie
                nama = input("Name :")
                _head_shape = input("Head Shape (1-3) :")
                _body_shape = input("Body Shape (1-3) :")
                _is_smiling = input("Is Smiling (1-2) :")
                _holding = input("Is Holding (1-3) :")
                _jacket_color = input("Jacket Color (1-4) :")
                _has_tie = input("Has Tie (1-2) :")
                # input to be applied to the data to check if he/she has monk  
                head_shape = int(_head_shape)                   # Cast the value to Int
                body_shape = int(_body_shape)
                is_smiling = int(_is_smiling)
                holding = int(_holding)
                jacket_color = int(_jacket_color)
                has_tie = int(_has_tie)
        
        # Display the result
        elif choice == 2:
                hitung(head_shape-1, body_shape-1 , is_smiling-1 , holding-1, jacket_color-1, has_tie-1)
                penentu()

        # Display values 
        elif choice == 3:
                print(nama, head_shape, body_shape, is_smiling, holding, jacket_color, has_tie)
                print(nilai_prob)
        # Quit
        elif choice == 4:
                break
