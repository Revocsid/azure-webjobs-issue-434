# azure-webjobs-issue-434
Repro issue 434 azure webjobs package

# Step 1 : 
Create an azure storage account, get credentials and create a queue

# Step 2 : 
Set credentials in the test.py script 

# Step 3 : 
Create a queue trigger Node azure function in order to handle messages from this queue

# Step 4 : 
Run test.py, you will see that you can get message from the queue with Python script but not in the JS azure function
