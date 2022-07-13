#! python 3

#A function that prints a table in an ordered manner

#data
tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

#function
def printTable(tables):
        len_max = []

            # Appends the number of the highest string to the len_max list
            # using the max function: max(list, key = len)
            

        for word in range(len(tables)):
            len_max.append(len(max(tables[word], key = len)))
            
        for items in range(len(tables[0])):
            for i in range(len(tables)):
                print(tables[i][items].rjust(len_max[i]), end=' ')
            print()

printTable(tableData)