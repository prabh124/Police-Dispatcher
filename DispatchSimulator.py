#Command used to read the text file and print the line of the job
def printJob(x):
    commandFile = open('emergencies.txt', 'r') 
    job = commandFile.readlines()
    return job[x]
def numOfLines():
    with open('emergencies.txt') as r:
        lines = 0
        for line in r:
            lines += 1
    return lines


#function used to check for the first word of each command and return a specific value
def commandCheck(x, line):
    line = line.split()

    if 'received' in line[0]:
        return 1
    elif 'respond' in line[0]:
        return 2
    elif 'show' in line[0]:
        return 3
    elif 'modify' in line[0]:
        return 4
    elif 'remove' in line[0]:
        return 5
    elif 'details' in line[0]:
        return 6
    elif 'statistics' in line[0]:
        return 7
    #if none are there then break out of the loop
    else:
        return 8

#helper function to read the priority of the current job from the text file
def priorityCheck(List, jobCounter):
    counter = 0
    ptr = List   
    while counter != jobCounter:
        ptr = ptr["next"]
        counter += 1
    test = ptr["data"][2]
    test = int(test)
    return test

#helper function to read the job number from the text file
def jobNumber(List, jobCounter):
    counter = 0
    ptr = List   
    while counter != jobCounter:
        ptr = ptr["next"]
        counter += 1
    test = ptr["data"][1]
    test = int(test)
    return test

#helper function to read the job type of the current job from the text file
def jobType(List, jobCounter):
    counter = 0
    ptr = List   
    while counter != jobCounter:
        ptr = ptr["next"]
        counter += 1
    test = ptr["data"][3]
    return test

#Function used to calculate the average priority, this is done by summing up all the priorities and dividing it by the jobCounter created below which counts how many jobs are in the current list
def averagePriority(List, jobCounter):
    sum = 0
    ptr = List   
    for i in range(jobCounter):
        test = 0
        test = ptr["data"][2]
        test = int(test)
        sum += test
        ptr = ptr["next"]
    average = sum // jobCounter
    return average

#simple function used to print the list of jobs/queue
def printTheList(theList):
    ptr = theList
    while ptr != None:
        print(ptr["data"], end = " ")
        ptr = ptr["next"]
#helper function in order to create the list
def addToHead(List, value):
    node = {}
    node["data"] = value
    node["next"] = List
    return node

#function used to create the initial linkedlist
def createList(theList):
    Lists = None
    for i in theList:
        Lists = addToHead(Lists, i)
    return Lists

#function used to add to the linked list (received from the online forum from OnQ)
def addToList(theList, value):
    ptr = theList
    while ptr["next"] != None:
        ptr = ptr["next"]
    newnode = {}
    newnode["data"] = value
    newnode["next"] = None
    ptr["next"] = newnode
    return newnode

#helper function to find the job number for the other commands
def getJobNum(line):
    line = line.split()
    return line[1]

#function used to remove a certain job from queue, received from the online forum from OnQ
def remove(jobList, job):
    head = jobList
    if head['data'][1] == job:   
        head = head['next']
        jobList = head
    else:
        ptr = head
        while ptr['data'][1] != job:  
            nodeBefore = ptr
            ptr = ptr['next']
        nodeBefore['next'] = ptr['next']
    print("Job " + job, " has been removed from the queue")
    return jobList

#function for details of a job, simply gets the value and outputs the job
def details(jobList, job):
    head = jobList
    if head['data'][1] == job:   
        print("The details of job " + job, " are: " + head['data'][2], "priority, with the type as: " + head['data'][3])
    else:
        ptr = head
        while ptr['data'][1] != job:  
            ptr = ptr['next']
        print("The details of job " + job, " are: " + ptr['data'][2], "priority, with the type as: " + ptr['data'][3])
    return jobList

#responding to the head of the queue, and then deleting it
def respond(jobList):
    ptr = jobList
    if jobList != None:
        print("Responding to job " + ptr['data'][1], "!") 
        jobList = jobList['next']
    else:
        print("No current emergencies! Time for a coffee break!")
    return jobList

#modifying a certain job and changing the priority level
def modify(jobList, job):
    head = jobList
    job = job.split()
   
    if head['data'][1] == job[1]:   
        ptr['data'][2] = job[2]
    else:
        ptr = head
        while ptr['data'][1] != job[1]:  
            ptr = ptr['next']
        ptr['data'][2] = job[2]
  
    return jobList

def checkIfSorted(jobList, jobCounter):
    ptr = jobList
    ptrCounter = 0
    while ptr['next'] != None:
        if ptr['data'][0] < ptr['next']['data'][0]:
            ptrCounter += 1
        ptr = ptr['next']
    if ptrCounter is 0:
        return True
    else:
        return False




#sorting the linked list in descencding order
def sort(jobList, jobCounter):
    head = jobList
    ptr = head
    sortedList = False
    while sortedList is False:
        for i in range(jobCounter):
            node = {}
            if int(head['data'][2]) < int(ptr['data'][2]):
                node['data'] = ptr['data'] 
                ptr['data'] = head['data']
                head['data'] = node['data']
                head = head['next']
                ptr = ptr['next']
                jobList = head
        sortedList = checkIfSorted(jobList, jobCounter) #create a new function which will return Ture or False based on if the list is sorted or not
    return jobList


    
#global counter variables
jobCounter = 0
num = 0
medicalCounter = 0
trafficCounter = 0
crimeCounter = 0


#loop used to iterate through, it is broken when there are no more lines left to read
while num < numOfLines():
    
    #using the first 2 functions to get line
    line = printJob(num)
    print(line)
    command = commandCheck(num, line)

    #THE LIST IS PRINTED IN EVERY CALL, THIS IS USED TO MAKE IT EASIER TO VIEW

    #if the command is one then we are receiving a job
    if command is 1:

        #if this is the first iteration then create the list instead of adding to it
        if num is 0:
            line = line.split()
            List = createList([line])
            print("Adding job: " + str(jobNumber(List, jobCounter)), "to the queue. " + str(priorityCheck(List, jobCounter)), "is the priority of this job. Job " + str(jobNumber(List, jobCounter)), "is of type " + jobType(List, jobCounter))
            
            #counting how many of each type of job is used up for command 7
            typeOfJob = jobType(List, jobCounter)
            if "traffic"  in typeOfJob:
                trafficCounter += 1
            elif "medical"  in typeOfJob:
                medicalCounter += 1
            elif "crime"  in typeOfJob:
                crimeCounter += 1           
            List = sort(List, jobCounter)
            printTheList(List)
            jobCounter += 1
        #anything after the first iteration will be added onto the linked list
        else:
            line = line.split()
            addToList(List, line)
            print("Adding job: " + str(jobNumber(List, jobCounter)), "to the queue. " + str(priorityCheck(List, jobCounter)), "is the priority of this job. Job " + str(jobNumber(List, jobCounter)), "is of type " + jobType(List, jobCounter))
            typeOfJob = jobType(List, jobCounter)
            if "traffic"  in typeOfJob:
                trafficCounter += 1
            elif "medical"  in typeOfJob:
                medicalCounter += 1
            elif "crime"  in typeOfJob:
                crimeCounter += 1
            List = sort(List, jobCounter)
            printTheList(List)
            jobCounter += 1
            
    #if the command is 2 then we are responding to a job and removing the first node
    elif command is 2:
        List = respond(List)
        List = sort(List, jobCounter)
        printTheList(List)
        #decrement jobCounter as we are taking away a job
        jobCounter -= 1

    #if the command is 3 then we are displaying the number of calls on queue and the average priority of those calls
    elif command is 3:

        print("Total waiting calls in queue: " + str(jobCounter))
        print("Average waiting priority is: " + str(averagePriority(List, jobCounter)))

    #if the command is 4 then we are modifying the selected jobs priority
    elif command is 4:

        line = printJob(num)
        print(line)
        modify(List, line)
        List = sort(List, jobCounter)
        printTheList(List)

    #if the command is 5 then we are removing a certain job from the queue
    elif command is 5:

        line = printJob(num)
        line = getJobNum(line)
        print(line)
        remove(List, line)
        List = sort(List, jobCounter)
        printTheList(List)
        jobCounter -= 1

    #if the command is 6 then we are displaying details about a certain job that is in the file
    elif command is 6:

        line = printJob(num)
        line = getJobNum(line)
        details(List, line)
        List = sort(List, jobCounter)
        printTheList(List)

    #else the command is 7 then we display statistics for how many of each type of job there is
    else:
        print("\nStatistics:\n")
        print("There are: " + str(medicalCounter), "medical calls!")
        print("There are: " + str(crimeCounter), "crime calls!")
        print("There are: " + str(trafficCounter), "traffic calls!")
    
    #adding one to num every loop
    num = num + 1
    
#when the max number of lines have been reached, close the program
print("Done! Goodbye!")



