import math
#system by Jaylen Ho Luc
def find_SQf(param):
    squarefoot = math.ceil(int(param) / 500) * 500
    global shops
    shops = 2 * int(squarefoot)
    global fasteners
    fasteners = int(squarefoot) * .4
    global misc
    misc = int(squarefoot) * 2
    global silicone
    silicone = int(squarefoot) * .4
    global licensebond
    licensebond = 250
def linFoot(param):
    global linearfootageprice
    linearfootageprice = (int(param) * 2) * 4
def steel(param):
    global steelamount
    steelamount = int(param)
def breakm(param):
    global breakmetal
    breakmetal = int(param)
def otherd(param):
    global others
    others = int(param)
def liftp(param):
    global liftprice
    liftprice = int(param)
def other22(param):
    global others2p
    others2p = int(param)
while True:
    while True:
        print()
        print('Welcome to the glazing automated calculations system!!!')
        print('-'*50)
        while True:
            print()
            squarefoot = input('Enter a total Square Footage: ')
            if not squarefoot.isnumeric(): print('Please enter a number')
            else: break 
        squarefoot = math.ceil(int(squarefoot) / 500) * 500
        shops = 2 * squarefoot
        fasteners = squarefoot * .4
        misc = squarefoot * 2
        silicone = squarefoot * .4
        licensebond = 250
        while True:
            linearfoot = input('Enter linear footage: ')
            if not linearfoot.isnumeric(): print('Please enter a number') 
            else: break
        linearfootageprice = (int(linearfoot) * 2) * 4
        while True:
            steelamount = input('What is the steel amount: ')
            if not steelamount.isnumeric(): print('Please enter a number') 
            else: break
        while True:
            breakmetal = input('What is the break metal price: ')
            if not breakmetal.isnumeric(): print('Please enter a number')
            else: break
        while True:
            others = input('What is the other price?: ')
            othername =  input('What is the "other" name?: ')
            if not others.isnumeric() : print('Please enter a number') 
            if not type(othername) == str: print('Please enter a name for "other"')
            else: break
        while True:
            others2 = 'other'
            others2p = 0
            inp0 = input('Do you want to input another "other" pricing. Enter "yes" or "no": ')
            if type(inp0) == str and inp0 in ('Yes', 'yes'): 
                others2 = input('What is the name of the second "other"?: ')
                while type(others2) != str :
                    others2 = input('What is the name of the second "other"?: ')
                    
                others2p = input('What is the price for the second "other"?: ')
                while not others2.isnumeric():
                    print('please enter a number for the second "other" pricing')
                    print()
                    others2p = input('What is the price for the second "other"?: ')
                break
            else: break

        while True:
            liftprice = input('What is the lift price?: ')
            if not liftprice.isnumeric(): print('Please enter a number')
            else: break
        while True:
            inp3 = input('Is there any value that you input incorrectly? If so, enter "yes", If not enter "no": ')
            if inp3 not in ('Yes', 'yes', 'YES'): break
            elif inp3 in ('Yes', 'yes', 'YES'):
                print('*'*25)
                print('Here are the value names:')
                print()
                print('-squarefoot')
                print('-linearfoot')
                print('-steelamount')
                print('-breakmetal')
                print('-others')
                print('-liftprice')
                print('2nd_other')
                print('*'*25)
                while True:
                    inp4 = input('Enter the data name whos value you mistyped exactly the way it is above:')
                    errorans = ['squarefoot','linearfoot','steelamount','breakmetal','others','liftprice']
                    if inp4 not in errorans: print('Invalid data type. Please enter one of the datum above')
                    else:
                        errorans = [i for i in errorans if inp4 == str(i)]
                        while True:
                            global inp5
                            inp5 = input('What is the new corrected value?: ')
                            if not inp5.isnumeric(): print('Please enter a number') 
                            else: break
                        errordict = {'squarefoot': find_SQf,'linearfoot': linFoot,'steelamount': steel,'breakmetal': breakm,\
                            'others': otherd,'liftprice' : liftp, '2nd_other': other22}
                        for k,v in errordict.items():
                            if str(errorans[0]) == k: v(inp5)
                        inp7 = input('Did you input anything else wrong? Enter "yes" if so, if not enter "no": ')
                        if inp7 in ('Yes', 'yes', 'YES'): continue
                        break
        #barring any scoping issues this should work, look for scoping issues
        print('Dollar figures:')
        print(f'-Shops: {shops}')
        print(f'-linear footage: {linearfootageprice}')
        print(f'-Fasteners: {fasteners}')
        print(f'-Steel: {steelamount}')
        print(f'-Misc total: {misc}')
        print(f'-Liscense/Bond: {licensebond}')
        print(f'-Brake MetalL {breakmetal}')
        print(f'-Silicone: {silicone}' )
        print(f'-{othername}: {others}')
        print(f'-Liftprice: {liftprice}')
        print(f'-{others2}: {others2p} ')
        print()
        print('-'*50)
        total = int(shops) + int(fasteners) + int(linearfootageprice) + int(steelamount) + int(misc) + int(licensebond)\
             + int(breakmetal) + int(silicone) + int(others) + int(liftprice) + int(others2p)
        print(f'TOTAL AMOUNT FOR "OTHERS": {total}')



    

