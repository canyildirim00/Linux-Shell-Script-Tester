linux_dict = {"pwd": "pwd shows the path of current working directory",
              "cd directory_name": "cd enables you to go to given directory. Using cd without directory, sends you to home folder",
              "cd ..": "cd .. sends you to upper directory of current directory",
              "ls": "ls shows the contents in the current directory",
              "cat x.txt": "cat command shows the contents of x file",
              "cp x y": "cp copies x to y location",
              "mv x y": "mv moves x to y location",
              "mkdir": "mkdir creates a new directory.",
              "rmdir": "rmdir deletes directory if it is empty",
              "rm -rf": "rm -rf deletes any contents",
              "touch x.extension": "touch allows you to create a new file with given extension",
              "locate x": "locate command locates the target file",
              "find x y": "find command finds for x in y",
              "grep x y": "grep command searches x in y",
              "sudo": "sudo means superuser do. It enables you to act like root or admin",
              "tar x.tar": "tar enables you to extract tar folders ",
              "chmod": "chmod used to change the read, write, and execute permissions of files and directories",
              "kill x": "By using kill command, you can terminate programs.",
              "ping x": "ping command lets you to check your connectivity status to a server",
              "history": "history command shows command history. In order to clear history, type history -c",
              "echo x > y": "echo command writes x into y. In order to keep on writing without losing previous data, >> is used",
              "zip x": "zip compresses files into a zip archive",
              "unzip x.zip": "unzip extracts the zipped files from a zip archive."
              }

linux_list = []
for i in linux_dict:
    all = [i,linux_dict[i]]
    linux_list.append(all)

def quest():
    for i in linux_list:
        print(i)


print(""" 
    .--.
   |o_o |
   |:_/ |
  //   \ \ 
 (|     | )
/'\_   _/`\ 
\___)=(___/ 
""")

test = input("Do you want to see questions? Y/n ").lower()
if test =="y":
    quiz_on = True
    while quiz_on:
        score = 0
        pwd = input("How can you see the current working directory? ")
        if pwd == "pwd":
            print("Correct")
            score += 1
        else:
            print(linux_list[0])

        ls = input("How can you show contents in current directory? ")
        if ls == "ls":
            print("Correct")
            score += 1

        else:
            print(linux_list[3])
        echo = input("How can i write 'xyz' into the test.txt? ")
        if echo == "echo xyz > test.txt":
            print("Correct")
            score += 1
        else:
            print(linux_list[-3])
        cat = input("How can i see what is written in test.txt? ")
        if cat == "cat test.txt":
            print("Correct")
            score += 1
        else:
            print(linux_list[4])
        echo2 = input("I want to write 'abcd' without losing previous data in test.txt. What should i do? ")
        if echo2 == "echo abcd >> test.txt":
            print("Correct")
            score += 1
        else:
            print(linux_list[-3])
        rm = input("I want to delete test.txt. Which command should i use? ")
        if rm == "rm test.txt":
            print("Correct")
            score += 1
        else:
            print("rm can delete it. You can also use -rf parameters too.")
        unzip = input("I have this xyz.zip file. I want to extract it in shell. How can i extract it ? ")
        if unzip == "unzip xyz.zip":
            print("Correct")
            score += 1
        else:
            print(linux_list[-1])
        history = input("If you want to see your command history? ")
        if history == "history":
            print("Correct")
            score += 1
            history_c = input("If you want to clear your history? ")
            if history_c == "history -c":
                print("Correct")
                score += 1
            else:
                print(linux_list[-4])
        else:
            print([linux_list[-4]])
        touch = input("I want to create a txt folder with name x. What can i do? ")
        if touch == "touch x.txt":
            print("Correct")
            score += 1
        else:
            print("Correct answer is touch x.txt")
        mkdir = input("How can you create a new directory named new? ")
        if mkdir == "mkdir new":
            print("Correct")
            score += 1
        else:
            print(linux_list[7])
        rmdir = input("How can you delete an empty directory named old? ")
        if rmdir == "rmdir old":
            print("Correct")
            score += 1
        else:
            print([linux_list[8]])
        grep = input("I want to find specific detail 'abc' in test.txt. How can i find it? ")
        if grep == "grep abc test.txt":
            print("Correct")
            score += 1
        else:
            print(linux_list[-10])
        cd = input("I am at Desktop now. I want to go x directory. How can i go? ")
        if cd == "cd x":
            print("Correct")
            score += 1
            cd2 = input("How can i come back to Desktop? ")
            if cd2 == "cd ..":
                print("Correct")
                score += 1
            else:
                print(linux_list[2])
        else:
            print(linux_list[1])
        cp = input("I want to copy x to /Desktop. How can i? ")
        if cp == "cp x /Desktop":
            print("Correct. But in your case, full path should be given")
            score += 1
        else:
            print(linux_list[5])
        sudo = input("You are not root but you want to act like root. Which command you add before your command? ")
        if sudo == "sudo":
            print("Correct")
            score += 1
        else:
            print(linux_list[-9])
        ping = input("I want to check my connection status of x.com. What should i do?  ")
        if ping == "ping x.com":
            print("Correct")
            score += 1
        else:
            print(linux_list[-5])

        print(f"Your score is {score}/18. Congrats.")
        if score == 17:
            print("FULL SCORE. Congrats")
        again = input("Do you want to test your information again? Y/n ").lower()
        if again == "y":
            quiz_on
        else:
            request1 = input("Do you want to see the wordlist? Y/n ").lower()
            if request1 == "y":
                quest()
                break
            else:
                print("Goodbye.")



else:
    commands = input("Do you want to see command list? Y/n ").lower()
    if commands =="y":
        quest()
    else:
        request = input("Do you want to see the wordlist? Y/n ").lower()
        if request == "y":
            quest()
        else:
            print("Goodbye.")





