import random

rock='''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''
scisor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

dontmatter = input("wanna ple rock paper scissor? Y or N :").upper()
items= [rock,paper,scisor]
if dontmatter == "Y" :
        print("Oke then Lets strat")
        you=int(input("pick a item rock is = 0 paper = 1 scissor =2: "))
        print(items[you] + "\n")
        pc = random.randint(0,2)
        print("Pc chose: ")
        print(items[pc])
        if you >= 3 or you < 0: 
            print("You typed an invalid number, you lose!") 
        elif you == 0 and pc == 2:
            print("You win!")
        elif pc == 0 and you == 2:
            print("You lose")
        elif pc > you:
            print("You lose")
        elif you > pc:
            print("You win!")
        elif pc == you:
            print("It's a draw")

    
elif dontmatter=="N" :
        print("                       :::!~!!!!!:.\n"
              "                  .xUHWH!! !!?M88WHX:.\n"
              "                .X*#M@$!!  !X!M$$$$$$WWx:.\n"
              "               :!!!!!!?H! :!$!$$$$$$$$$$8X:\n"
              "              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:\n"
              "             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!\n"
              "             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!\n"
              "               !:~~~ .:!M\"T#$$$$WX??#MRRMMM!\n"
              "               ~?WuxiW*`   `\"#$$$$8!!!!??!!!\n"
              "             :X- M$$$$       `\"T#$T~!8$WUXU~\n"
              "            :%`  ~#$$$m:        ~!~ ?$$$$$$\n"
              "          :!`.-   ~T$$$$8xx.  .xWW- ~\"\"##*\"\n"
              ".....   -~~:<` !    ~?T#$$@@W@*?$$      /`\n"
              "W$@@M!!! .!~~ !!     .:XUW$W!~ `\"~:    :\n"
              "#\"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`\n"
              ":::~:!!`:X~ .: ?H.!u \"$$$B$$$!W:U!T$$M~\n"
              ".~~   :X@!.-~   ?@WTWo(\"*$$$W$TH$! `\n"
              "Wi.~!X$?!-~    : ?$$$B$Wu(\"**$RM!\n"
              "$R@i.~~ !     :   ~$$$$$B$$en:``\n"
              "?MXT@Wx.~    :     ~\"##*$$$$M~\n"
              "YOU DON'T HAVE A CHOICE" + "\n")
        
        you=int(input("pick a item rock is = 0 paper = 1 scissor =2: "))
        print(items[you] + "\n")
        pc = random.randint(0,2)
        print("Pc chose: ")
        print(items[pc])
        if you >= 3 or you < 0: 
            print("You typed an invalid number, you lose!") 
        elif you == 0 and pc == 2:
            print("You win!")
        elif pc == 0 and you == 2:
            print("You lose")
        elif pc > you:
            print("You lose")
        elif you > pc:
            print("You win!")
        elif pc == you:
            print("It's a draw")
        
else :
    print("  .... NO! ...                  ... MNO! ...\n"
      "   ..... MNO!! ...................... MNNOO! ...\n"
      " ..... MMNO! ......................... MNNOO!! .\n"
      "..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .\n"
      " ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....\n"
      "    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...\n"
      "   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....\n"
      "   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...\n"
      "    ....... MMMMM..    OPPMMP    .,OMI! ....\n"
      "     ...... MMMM::   o.,OPMP,.o   ::I!! ...\n"
      "         .... NNM:::.,,OOPM!P,.::::!! ....\n"
      "          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....\n"
      "         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....\n"
      "           .. MMMMMNNOOMMNNIIIPPPOO!! ......\n"
      "          ...... MMMONNMMNNNIIIOO!..........\n"
      "       ....... MN MOMMMNNNIIIIIO! OO ..........\n"
      "    ......... MNO! IiiiiiiiiiiiI OOOO ...........\n"
      "  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........\n"
      "   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........\n"
      "   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........\n"
      "      ...... OO! ................. ON! .......\n"
      "         ................................\n"
     " you did not answer RIGHT""\n"
      "YOU DIE HERE""\n")
        


