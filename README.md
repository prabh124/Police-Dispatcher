# Police-Dispatcher
A police dispatcher using Linked Lists to simulate a priority queue. Commands are taken from a text file, as well as the job descriptions/ratings which are explained later on.

The commands are as follows:

Command 1: Receiving an Emergency

An example of a new job is:

received 205 14 crime

The keyword received indicates that the line is a new job that is being submitted for emergency response.  Next is the (integer) priority rating for the call. Priority levels are assigned in the range of 1 to 30. You could imagine that a relatively minor emergency (such as a fender bender with no injuries) would be assigned a priority of approximately 1 while a natural disaster emergency (such as a fire or a tornado) would be assigned a priority of approximately 30. 

After processing this line, the program should print "Adding job XXX to the queue. YYY is the priority of the call. Job XXX is of type (traffic, crime or medical).

Command 2: Respond

The respond command indicates that the next job should be taken off the queue. In response, the program should print "Responding to job XXX" where XXX is the job id. If there is nothing in the queue to respond to, you should print "No current emergencies – time for a coffee break!".

Command 3: Active Calls

When you see a line that reads show, the program should print the number of jobs currently in the queue along with the average priority of all of the calls.  This simulates the "LED" on the monitor in the dispatch office.

Command 4: Modify Priority

In some cases, people who placed a call for emergency response may call back to modify the priority of a previously added call. Write a function that will modify the priority of a call, given the call ID: modify id newPriority. You will need to ensure that this call is moved to the correct location in the queue to ensure that the sorting of the queue by priority rating is maintained. 

Command 5: Remove

Removes the job from the queue. 

Once a police officer has completed a job, they will issue a command: remove 104. This command means to remove job 104 from the current queue.

Command 6: Details

Prints out the details for a specific call.

The command details 104 would print out all of the details associated with call id 104.

Command 7: Statistics

Prints out the number of calls associated with each job type (medical, traffic or crime).
