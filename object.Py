class BankAccount:
    def __init__(self,acou,passw,inibal,W_Amount,d_amount,w_answ,d_ans,j_answr,di_answer,d_psw,d_password,de_p):
        self.acc  = acou
        self.passw = passw
        self.inibal = inibal
        self.W_Amount = W_Amount
        self.amount = d_amount
        self.w_answ = w_answ
        self.d_ans = d_ans
        self.j_answr = j_answr
        self.di_answer = di_answer
        self.d_psw = d_psw
        self.d_password = d_password
        self.de_p = de_p

    def input_att(self):
        self.acc = input("Faka inombolo ye akhawunti")
        self.passw = input("Faka inombolo echanekileyo yokuvula")
        self.inibal = float(input("Faka imali yokuqala kwi akhawunti yakho"))

    def Deposit(self):
        d_ans = input("Uyafuna na ukufaka imali kwi akhawunti yakho?")
        if d_ans == "ewe" or d_ans == "Ewe" or d_ans == "EWE":
            j_answr = input("Yiyo na le akhawunti ufuna ukuyithumelela le: " + self.acc)
            if j_answr == "ewe" or j_answr == "Ewe" or j_answr == "EWE":
                self.d_amount = float(input(" Bhala lemali ufuna ukuyifaka kwi akhawunti yakho"))
                password = input("Faka inombolo echanekileyo yokuvula")
                while (password != self.passw):
                    password = input("Akuyiyo inombolo yokuvula echanekileyo le,phinda ufake echanekileyo")
                print("Yinombolo echanekileyo le")
                print("Ingenile imali ekuyi R ", self.d_amount, " kwi akhawunti engu ", self.acc)
                current = self.inibal + self.d_amount
                return current
            else:
                acc_n = input("Faka inombolo ye akhawunti yakho elungileyo")
                self.d_amount = float(input(" Bhala lemali ufuna ukuyifaka kwi akhawunti yakho"))
                password = input("Faka inombolo echanekileyo yokuvula")
                while (password != self.passw):
                    password = input("Akuyiyo inombolo yokuvula echanekileyo le,phinda ufake echanekileyo")
                print("Yinombolo echanekileyo le")
                print("Ingenile imali ekuyi R ", self.d_amount, " kwi akhawunti engu ", self.acc)
                current = self.inibal + self.d_amount
                return current
        else:
            current = self.inibal
            return current


    def Withdraw(self,c):
        self.w_answ = input("Uyafuna ukukhupha imali?")
        if self.w_answ == "ewe" or self.w_answ == "Ewe" or self.w_answ == "EWE":
            self.W_Amount = float(input(" Faka imali ofuna ukuyikhupha"))
            w_password = input("Faka inombolo echanekileyo yokuvula")
            while (w_password != self.passw):
                password = input("Akuyiyo inombolo yokuvula echanekileyo le,phinda ufake echanekileyo")
            print("Yinombolo echanekileyo le")
            print("Ukhuphe imali engange R ", self.W_Amount, "kwi akhawunti yakho")
            C_bal = c - self.W_Amount
            return C_bal
        else:
            C_bal = c
            return C_bal

    def Display(self,c):
        self.di_answer = input("Uyafuna na ukubona imali eshiyekileyo kwi akhawunti yakho")
        if self.di_answer == "ewe" or self.di_answer == "Ewe" or self.di_answer == "EWE":
            d_psw = input("Faka inombolo yokuvula echanekileyo")
            while d_psw != self.passw:
                password = input("Akuyiyo inombolo yokuvula echanekileyo le,phinda ufake echanekileyo")
            print("Yinombolo echanekileyo le")
            print(" Imali eshiyekileyo kwi akhawunti yakho yebhanki yi : R", c)

        print("Siyabulela ngokuba usebenzise lebhanki yethu")

class Main:
    if __name__ == '__main__':
        obj = BankAccount("1212","111",1000,100,100,"ewe","ewe","ewe","ewe","111","111","111")
        obj.Display(1000)
        obj2 = BankAccount("","",0,0,0,"","","","","","","")
        obj2.input_att()
        c_bal = obj2.Deposit()
        cure_bal = obj2.Withdraw(c_bal)
        obj2.Display(cure_bal)