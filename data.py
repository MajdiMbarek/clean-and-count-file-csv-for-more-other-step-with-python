import csv

titles =  {}


with open("Favorite TV Shows - Form Responses 1.csv") as file:
    reader = csv.DictReader(file)
    for i in reader:
        title = i["title"].strip().upper()
        # if title in titles:
        #     titles[title] += 1
        # else:
        #     titles[title] = 1
    # or :
        if title not in titles:
            titles[title] = 0
        titles[title] += 1

for row in sorted(titles, key= lambda m : titles[m] , reverse=True):
    print(f"{row} : {titles[row]}")