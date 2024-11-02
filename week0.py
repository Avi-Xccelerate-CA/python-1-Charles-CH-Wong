# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful


#def dose(needs):
#     #YOUR SOLUTION STARTS HERE

#Trial1
# #1 Input sth and change from str to a list of int value
# #    needs = input("Needs of the patient:(HP,Attack,Defense,Special Attack,Special Defense, Speed)").split(",")
# #    int_needs = []
# #    for i in needs:
# #        int_needs.append(int(needs[i]))
# #2 If sum of the int value list >500, return "No medicine given"
#     if sum(int_needs) > 500:
#         return "No medicine given"
# #3 If any value in the value list >250, return "No medicine given"   
#     if max(int_needs) > 250:
#         return "No medicine given"
# #4 Create a list which contains 6 tuple, then -1 when the value % 10 != 0
#     tuple_list = [(0,0)] * 6
#     for i in range(6):
#         while int_needs[i] % 10 != 0:
#             tuple_list[i][1] += 1
#             int_needs[i] -= 1
#         tuple_list[0] = int_needs [i]
#     return tuple_list

#Trial2
# #1 If sum of the int value list >500, return "No medicine given"     
#     if sum(needs) > 500:
#         return "No medicine given"

# #2 If any value in the value list >250, return "No medicine given"   
#     if max(needs) > 250:
#         return "No medicine given"
# #3 Create a list which contains 6 tuple, then -1 when the value % 10 != 0
#     tuple_list = [(0,0)] * 6
#     for i in range(6):
#         while needs[i] % 10 != 0:
#             tuple_list[i][1] += 1             
#             needs[i] -= 1
#         tuple_list[0] = needs [i]
#     return tuple_list

#Trial3
#1 If sum of the int value list >500, return "No medicine given"  
#     if sum(needs) >= 500:
#         return "No medicine given"

# #2 If any value in the value list >250, return "No medicine given"   
#     if max(needs) >= 250:
#         return "No medicine given"
    
# #3 Create a list 
#     output_list = [[0,0]]*6
#     print(output_list)
    
#     for i in range((len(needs))):
#         while needs[i] % 10 != 0:
#             output_list[i][1] += 1             
#             needs[i] -= 1
#         output_list[0][0] = needs [i]
#     return (output_list)


# dose([40,35,23,68,45,29])

#Trial4
def dose(needs):
#1 If sum of the int value list >500, return "No medicine given" 
    if sum(needs) >= 500:
        return "No medicine given"

#2 If any value in the value list >250, return "No medicine given" 
  
    if max(needs) >= 250:
        return "No medicine given"
    
#3.1 Create a empty list to store the final output
#3.2  

    output_list = []
    vitamins = 0
    injections = 0
    #attribute = 0
    for attribute in needs:
        vitamins = attribute // 10
        if attribute %10 != 0:
            vitamins += 1
            injections = vitamins * 10 - attribute
            output_list.append((vitamins, injections))
    
    return output_list
    #YOUR SOLUTION ENDS HERE

