# Description of Program: Outputs census data for each texas county from a csv file

import os.path
def dictionary():
    populationData = open("populationdata.csv", "r")
    censusTotal=0
    estimatedTotal=0
    countyNames=list()
    population = {}
    line=populationData.readline()
    numberOfNames=0
    while line:
        if ("#" in line):
            next
        else:
            splitLine=line.split(",")
            name=splitLine[0]
            numberOfNames+=1
            if (numberOfNames%10==0):
                countyNames.append(name + "\n")
            else:
                countyNames.append(name)
            censusTotal+=int(splitLine[1])
            estimatedTotal+=int(splitLine[2])
            population[name.lower()] = int(splitLine[1]), int(splitLine[2])
        line=populationData.readline()
    population["texas"]=int(censusTotal), int(estimatedTotal)
    return population, countyNames
    populationData.close()
        
def main():
    if not os.path.isfile("populationdata.csv"):
        print ("File does not exist")
        return
    commandInput=""
    data=dictionary()
    dic=data[0]
    countyNames=data[1]
    print("Welcome to the Texas Population Dashboard.")
    print("This provides census data from the 2010 census and")
    print("estimated population data in Texas as of 1/1/2020.")
    print("")
    print("Creating dictionary from file: populationdata.csv")
    print("")
    print("Enter any of the following commands:")
    print("Help - list available commands;")
    print("Quit - exit this dashboard;")
    print("Counties - list all Texas counties")
    print("Census <countyName>/Texas - population in 2010 census by specified county or statewide;")
    print("Estimated <countyName>/Texas - estimated population in 2020 by specified county or statewide;")
    print("Growth <countyName>/Texas - percent change from 2010 to 2020, by county or statewide.")
    
    while (commandInput!="quit"):
        print()
        command=input("Please enter a command: ")
        commandInput=command.lower()
        commWords = commandInput.split()
        comm = commWords[0].strip()
        args = commWords[1:]
        arg = " ".join(args).strip()
        if (commandInput=="quit"):
            print("Thank you for using the Texas Population Database Dashboard.  Goodbye!")
        elif (commandInput=="help"):
            print("Enter any of the following commands:")
            print("Help - list available commands;")
            print("Quit - exit this dashboard;")
            print("Counties - list all Texas counties")
            print("Census <countyName>/Texas - population in 2010 census by specified county or statewide;")
            print("Estimated <countyName>/Texas - estimated population in 2020 by specified county or statewide;")
            print("Growth <countyName>/Texas - percent change from 2010 to 2020, by county or statewide.")
        elif (commandInput=="counties"):
            print(", ".join(countyNames))
        elif (comm=="census" and arg not in dic):
            print("County", arg.title(), "is not recognized.")
        elif (comm=="estimated" and arg not in dic):
            print("County", arg.title(), "is not recognized.")
        elif (comm=="growth" and arg not in dic):
            print("County", arg.title(), "is not recognized.")
        elif (comm=="census"):
            print(arg.title(), "county had", dic[arg][0], "citizens in the 2010 Census.")
        elif (comm=="estimated"):
            print("Estimated population (January, 2020): ", dic[arg][1])
        elif (comm=="growth"):
            print("Population percent change (2010 to 2020): ", format(((dic[arg][1]-dic[arg][0])/dic[arg][0])*100, ".2f"), "%", sep="") 
        else:
            print("Command is not recognized.  Try again!")
        
            
              
main()
