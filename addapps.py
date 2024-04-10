print("Input the exact name of the app this will append it to the open-apps.txt file with correct code")
appendtofile = input()
applcode = 'set question to display dialog "Choose your app." buttons {"' + appendtofile + '", "Quit", "Next page"}\nset answer to button returned of question\nif answer = "Finder" then\n	tell application answer to activate\nend if\nif answer = "Quit" then\n	tell "Open-Apps" to quit\nend if'

f = open("open-apps.txt", "a")
f.write(applcode)
f.close()
