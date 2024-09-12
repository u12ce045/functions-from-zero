my_list = ["apple","cheery","kiwi"]
my_dict = {"drink":["coffee","milk","coconut"], "food":["Burger","Pizza","Pasta"]}

for item in my_list:
    print(f"My favourite thing to eat is {item}")

for key,values in my_dict.items():
    print(f"My favourite think to drink from {key} are")
    for v in values:
        print(v)
