import re;

def processData(data, separator):
    regexEmoji = re.compile("["u"\U0001F440""]+", flags=re.UNICODE)
    findEmoji = regexEmoji.finditer(data)
    foundKeys = 1

    for match in findEmoji:
        key: str = (data[match.start()+2:match.start()+19])
        key2: str = (data[match.start()+22:match.start()+39])

        if(separator == "puntos"):
            if key.find("."):
                print("Clave " + str(foundKeys) + ": " + key.replace(".", ""))
                foundKeys += 1
            if key2.find(".") and key2.find(" ") == -1:
                print("Clave " + str(foundKeys) + ": " + key2.replace(".", ""))
                foundKeys += 1
        elif(separator == "guiones"):
            if key.find("-"):
                print("Clave " + str(foundKeys) + ": " + key.replace("-", ""))
                foundKeys += 1
            if key2.find(separator) and key2.find(" ") == -1:
                print("Clave " + str(foundKeys) + ": " + key2.replace("-", ""))
                foundKeys += 1

def main():
    #Read from keyboard
    #data = input("Introduce la newsletter de esta semana:")

    #Read from file
    file = open("newsletter.txt", "r")
    data = file.read()

    separator = re.search('(?<=Hay que quitar los )(\w+)', data).group(1)    
    print("Esta semana los códigos de invitación se separan mediante " + separator)
    print("Procesando newsletter...")
    processData(data, separator)
    print("Introduce el código aquí: https://forocoches.com/codigo/")

    file.close()

if __name__ == "__main__":
    main()