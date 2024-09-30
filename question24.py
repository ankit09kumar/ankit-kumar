def print_list(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list , idx + 1)
    
cars = ["bmw" , "audi" , "lamborghini" , "bugatti" , "mercedes" , "mahindra"]
print_list(cars)