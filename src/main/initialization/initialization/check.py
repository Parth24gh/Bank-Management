def check():
    try:
        with open("files//firsttime.txt","r") as a:
            if a.read().strip()=="True":
                return True
            else:
                return False
    except (OSError, IOError) as e:
        with open("files//firsttime.txt","w") as a:
            a.write("True")
            return True