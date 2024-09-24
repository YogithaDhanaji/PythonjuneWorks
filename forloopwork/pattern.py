# for row in range (1,4):
#     for col in range (1,5):
#         print(col, end=" ")

#     print()    




# for row in range (1,5):
#     for col in range (0,5):
#         print(row,end=" ")

#     print( )    


# for row in range(1,5):

#     for col in range (1,6):

#         print("@", end=" ")

#     print( )    



# for row in range (1,5):

#     for col in range (1,7):

#         print("*", end="\t")

#     print( )    







# for row in range(1,5):
#     for col in range (1,row+1):

#         print("*", end="\t")
#     print( )    


for row in range (1,5):
    for col in range(1,6-row):

        print("*",end="\t")
    print( )        


