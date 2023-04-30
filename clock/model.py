def fun():
    inp_hour = int(input("enter a hour "))
    inp_min = int(input("enter a min "))
    if inp_hour == 12:
        s = inp_min*6 - 0*30
        print(s," degrees")
    else:
        s = inp_min*6 - (inp_hour)*30
        print(s," degrees")


import pickle
pickle.dump(fun,open("model.pkl","wb"))
# type(df),