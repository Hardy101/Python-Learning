# Imports
import time
start_time = time.time()


# Switch / Match Statement
# http_status = 500
# match http_status:
#     case 200 | 201:
#         print("Success")
#     case 400:
#         print("Bad Request")
#     case 500 | 501:
#         print("Server Error")
#     case _:
#         print("Unknown")
# Loops | FOR Loop
# favourites_1 = ["The conjuring", 'Annabelle', 'The conjuring 2']
# for idx, num in enumerate(favourites_1):
#     print(idx+1, "Looping ..", num)
# WHILE Loop
# count = 0
# while count < len(favourites):
#     print('Item #', count + 1, favourites[count])
#     count +=1
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# count = 0
# for x in list_1:
#     count += x
#     for y in list_2:
#         count += y

# print(count)

for i in range(100):
    for j in range(10000):
        print(0, end = " ")
    print("")
print(round((time.time() - start_time), 2), "time Taken")