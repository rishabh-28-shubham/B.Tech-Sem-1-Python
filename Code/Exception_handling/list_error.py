l1 = [10,20,30,40,50]
d1 = {"a":0,"b":1,"c":9,"d":10}
def list_ele_print(d1,key):
    try:
        print(d1[key])
    except KeyError:
        print(f"Given Key doesn't exist")
        # print(f"Given Range of Index : {key} is out of Range")

list_ele_print(d1,8)