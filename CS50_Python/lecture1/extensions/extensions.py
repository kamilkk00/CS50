name = input("File name: ").lower().strip()
newname = name[-4:]
sadname = name[-5:]

if newname == ".gif":
    print ("image/gif")
elif newname == ".jpg":
    print ("image/jpeg")
elif sadname == ".jpeg":
    print ("image/jpeg")
elif newname == ".png":
    print ("image/png")
elif newname == ".pdf":
    print ("application/pdf")
elif newname == ".txt":
    print ("text/plain")
elif newname == ".zip":
    print ("application/zip")
else:
    print("application/octet-stream")
