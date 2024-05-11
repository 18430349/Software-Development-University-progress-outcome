# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1840439
# Date:21/11/2022

#creating counters for histogram
counter_p=0
counter_pmt=0
counter_e=0
counter_dnpmr=0
total_inputs=0
#for list and dictionaries 
progress_list=[]
trailer_list=[]
retriever_list=[]
exclude_list=[]
total_list={}
#creating a textfile named dharshi  
myfile=open('dharshi.txt', 'w')
myfile.close()#to show changes made

while True:#overall loop for histogram,list,dictionaries and textfile
        
        while True:# while loop for integer validation
                credit_pass=input("Please enter your credit at pass: ")
                try:
                        credit_pass=int(credit_pass)
                        if credit_pass not in range(0,121,20):#condition for out of range validation
                            print("Out of range")
                            continue#loops unitl correct value entered
                        else:
                            break#ending condition
                        break#ending while loop
                except ValueError:
                        print("Integer required")
                        continue#loops until integer entered
                
        while True:#repeated the above process for defer credits validations
                credit_defer=input("Please enter your credit at defer:")
                try:
                        credit_defer=int(credit_defer)
                        if credit_defer not in range(0,121,20):
                            print("Out of range")
                            continue
                        else:
                            break
                        break
                except ValueError:
                        print("Integer required")
                        continue
                
        while True:#repeated the above process for fail credits validations
                credit_fail=input("Please enter your credit at fail:")
                try:
                        credit_fail=int(credit_fail)
                        if credit_fail not in range(0,121,20):
                            print("Out of range")
                            continue
                        else:
                            break
                        break
                except ValueError:
                        print("Integer required")
                        continue
       
        
        credit_total= int(credit_pass + credit_defer + credit_fail)#variable for total credits
        if credit_total==120:#condition for incorrect total outcome
                total_inputs=total_inputs+ 1#counter for total inputs for histogram
                uniqueid=input("Please enter your student ID:")
                if credit_pass == 120:# first condition for progression outcome 
                        print("Progress")
                        counter_p=counter_p+ 1
                        progress_list.append([credit_pass,credit_defer,credit_fail]) 
                        total_list[uniqueid] = 'Progress-'+ str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)#dictionary in the format key=values(source:Reference no 2)
                        myfile=open('dharshi.txt', 'a')#opening textfile for writing and appending to the end of file, (source from lecture notes)
                        myfile.write('Progress-'+ str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)+"\n")#displays in list 
                        myfile.close()#closing textfile
                elif credit_pass ==100:#second condition for progression outcome
                        print("Progress (module trailer)")
                        counter_pmt=counter_pmt+ 1 
                        trailer_list.append([credit_pass,credit_defer,credit_fail])
                        total_list[uniqueid] = 'Progress(module trailer)-'+str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)
                        myfile=open('dharshi.txt', 'a') 
                        myfile.write('Progress(module trailer)-'+ str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)+"\n")
                        myfile.close()
                elif credit_fail >=80:#third condition for progression outcome
                        print("Exclude")
                        counter_e=counter_e+ 1
                        exclude_list.append([credit_pass,credit_defer,credit_fail])
                        total_list[uniqueid] = 'Module retriever-'+str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)
                        myfile=open('dharshi.txt', 'a') 
                        myfile.write('Module retriever-'+ str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)+"\n")
                        myfile.close()
                else:
                        print("Module retriever")
                        counter_dnpmr=counter_dnpmr+ 1
                        retriever_list.append([credit_pass,credit_defer,credit_fail])
                        total_list[uniqueid] = 'Exclude-'+ str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)
                        myfile=open('dharshi.txt', 'a') 
                        myfile.write('Exclude-'+ str(credit_pass)+','+str(credit_defer)+','+str(credit_fail)+"\n")
                        myfile.close()
        else:
                print("Total incorrect")
        
        #setting user prompt for multiple outcomes          
        user_choice=input("\nWould you like to enter another set of data?\nEnter 'y' to continue or 'q' to quit and view results: " )
        while user_choice != 'y' and user_choice!= 'q':#loop for invalid input
                print("Invalid input")
                user_choice=input("\nWould you like to enter another set of data?\nEnter 'y' to continue or 'q' to quit and view results: " )
        if user_choice == 'y':#condition for continuing loop
                continue 
        elif user_choice == 'q':#condition to quit and view data in histogram, list, textfile and dictionaries
                print("\n",50*"-","\nHistogram")
                print(counter_p,"Progress  :", '*'*counter_p)
                print(counter_pmt,"Trailer   :",'*'*counter_pmt)
                print(counter_dnpmr,"Retriever :", '*'*counter_dnpmr)
                print(counter_e,"Exclude   :",'*'*counter_e)
                print("\nOutcomes in total is:",total_inputs)
     
                #(source for using 'map' function and join into nested list) https://stackoverflow.com/questions/30521975/print-a-nested-list-line-by-line-python
                print(50*"-","\nList")
                for i in progress_list:
                        print("Progress -" + ",".join(map(str, i)))#this map function will get all the item in the nested list and convert int to string 
                for i in trailer_list:
                        print("Progress(module trailer) -" + ",".join(map(str, i)))
                for i in retriever_list:
                        print("Module retriever -" + ",".join(map(str, i)))
                for i in exclude_list:
                        print("Exclude -" + ",".join(map(str, i)))

                #(source: Lecture notes 'Using python to write/read text files(pdf,page 6) in Blackboard)
                print(50*"-","\nTextfile")        
                myfile= open('dharshi.txt', 'r')#open textfile
                for line in myfile:#read the whole line from the whole file
                        print(line, end='')#returns each line in a new line
                myfile.close()#closing textfile

                #(source for using for loop method for dictionary)https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/
                print(50*"-","\nDictionary")
                for key, value in total_list.items():#copy the keys and values in pairs from the dictionary 
                    print(key, ' : ', value)#print the items in order

                print(50*"-","\nThank you\n")


                break#ending the main while loop



##        References
##        1)"Print a nested list line by line-Python",Available from:(https://stackoverflow.com/questions/30521975/print-a-nested-list-line-by-line-python, Accessed on:15/11/2022
##        2)Varun, "Python:Print items of a dictionary line by line(4 Ways)", Available from:https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/,Accessed on:18/11/2022
##        3)Lecture notes for Software Development 1 from Blackboard under learning resources.
##
##



