import math
#system by Jaylen Ho Luc and Neal Lowry

#here are the heper functions, all these functions do is calculate and/or set prices to global variables. 
#component modules are being planned to work indivually and seperating so global variable collison is a non-issue
#calculates square footage

#calculates linear footage

#sets global variable steelamount to param
class estimator:
    def __init__(self):
        while True:
            print('Welcome to the glazing automated calculations system!!!')
            print('-'*50)
            squarefoot = input('Enter a total Square Footage: ')
            if not squarefoot.isnumeric(): print('Please enter a number')
            else:
                self.find_SQf(squarefoot)
                self.squarefoot_orginal = squarefoot
                break 
    @staticmethod
    def isnum(self,param): #predicate
        if not param.isnumeric(): return False
        else: return True

    def find_SQf(self,param):
        self.squarefoot = math.ceil(int(param) / 500) * 500

        self.shops = 2 * int(self.squarefoot)

        self.fasteners = int(self.squarefoot) * .4

        self.misc = int(self.squarefoot) * 2

        self.silicone = int(self.squarefoot) * .4

        self.licensebond = 250

        #not required 
        self.steelamount = 0
        self.breakmetal = 0
        self.others = 0
        self.liftprice = 0
        self.others=0
    
    def linFoot(self,param): self.linearfootageprice = (int(param) * 2) * 4


    def steel(self,param): self.steelamount = int(param)
    #sets global variable breakmetal to param
    def breakm(self,param): self.breakmetal = int(param)
    #sets global variable others to param
    def otherd(self,param,name): 
        self.others = dict()
        self.others[name] =  int(param)
    #sets global variable liftp to param
    def liftp(self,param): self.liftprice = int(param)

    def end(self):
        print('Dollar figures:')
        print(f'-Shops: {self.shops}')
        print(f'-linear footage: {self.linearfootageprice}')
        print(f'-Fasteners: {self.fasteners}')
        print(f'-Steel: {self.steelamount}') #not req
        print(f'-Misc total: {self.misc}')
        print(f'-Liscense/Bond: {self.licensebond}')
        print(f'-Brake Metal {self.breakmetal}') #not req
        print(f'-Silicone: {self.silicone}' )
        print(f'-Liftprice: {self.liftprice}') #not req

        print()
        print('-'*50)
    
    def calculation(self):
        total = int(self.shops) + int(self.fasteners) + int(self.linearfootageprice) + int(self.steelamount) + int(self.misc) + int(self.licensebond)\
            + int(self.breakmetal) + int(self.silicone) + int(self.liftprice)
        for v in self.others.values(): total += v
        print(f'TOTAL AMOUNT FOR "OTHERS": {total}')

#main event loop
def main():
    print('COMMANDS (you must input all required fields. You can ): ')
    print()
    print('')
    print()
    print()









def u():
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
            #all these variables can be calculated with squarefoot variable
            squarefoot = math.ceil(int(squarefoot) / 500) * 500
            shops = 2 * squarefoot
            fasteners = squarefoot * .4
            misc = squarefoot * 2
            silicone = squarefoot * .4
            licensebond = 250
            #all these while loops prompt user for input and if the input is not numeric then it will continue asking 
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
            #the second "others" or other2p is optional and may or may not be added
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



    

