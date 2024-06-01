# mydist={
#     "fast":"in a quick manner",
#     "sujan":"a student",
#      "phoenix":"lincon affilated college",
#      "marks":[2,0,89],
#      "anotherdist":{"sujan":"a cricket player"}
# }

# print(mydist.keys())
# print(tuple(mydist.keys()))
# print(mydist.values())
# print(tuple(mydist.values()))
# print(mydist.items()) #prints (key,values) for all contents
# print(mydist)
# updateDict={
#     "rohit sharma":"hitman",
#     "paras khadka":"legend",
#     "sujan sapkota": "student"

# }
# mydist.update(updateDict) #updates the dictionary by adding keys,values from updateDict
# # print(mydist)



# # difference between .get and [] is .get method won't throw error if value is not present in dictionary but for mydist[] value must be present in dictionary to not throw error
# print(mydist.get("sujan2")) #returns none because sujan2 is not present in mydist
# print(mydist["sujan2"]) #returns error as sujan2 is not present in mydist





sujan={
    "name":"sujan sapkota",
    "class":"bit",
    "religion":"hindu",
    "fav sport":"cricket"
}

sampanna={
    "name":"sampanna",
    "fav sport":"football",
    "study":"phoenix"
}

sujan.update(sampanna)
print(sujan)


# print(list(sujan.values()))
# sujan_updated={
#     "name":"sujan sapkota jr",
#     "class":"semester 5",
#     "age":"21"
# }

# sujan.update(sujan_updated)
# print(list(sujan.values()))

# list=['sujan','sapkota']
# list[0]="sampanna"
# print(list)