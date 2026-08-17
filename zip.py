names = ["muaaz", "Kareem","Laika", "Irfan"]
scores = [20, 21, 15, 47]
for i in range(len(names)):
    print(names[i], scores[i])

# There is a more simple way to do that upper program here it is :
print("/////////////////////////////////")
# /////

names = ["muaaz", "Kareem","Laika", "Irfan"]
scores = [20, 21, 15, 47]
for names, scores in zip(names, scores):
    print(names, scores)

