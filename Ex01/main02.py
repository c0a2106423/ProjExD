if __name__ == "__main__":
    import datetime
    st = datetime.datetime.now()
    for i in range(10000*10):
        i=i
    ed = datetime.datetime.now()
    diff = ed-st
    print(diff)
    print("end")