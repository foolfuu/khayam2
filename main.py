from tkinter import *
from tkinter import messagebox
from random import choice,randint
from math import sqrt
p12 = []
# pit = [{a : b},{b : c},{c : d}]
pit = [{},{},{}]
nae = ""
class algorithm:
    # براي ساده تر شدن استفاده از کتابخانه از تابع هاي زير استفاده مي کنيم
    def error_y_or_n(x,y): messagebox.askquestion(x,y)
    def error_ok(x,y):messagebox.showinfo(x,y)
    def rand():
        ran = list()
        for i in "abcdefghijmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ023456789!@#$%&*?":ran.append(i)
        text_r = ""
        for i in range(randint(8,12)): text_r += choice(ran)
        return text_r
    #$#
    def Searched(Search,li):
        pse = []
        sa = Search
        if len(sa) == 0:
            for i in range(li.size()):
                li.delete(0)
            for i in p12:
                li.insert(END,i)
        else:
            for i in p12:
                if sa in i:
                    pse.append(i)
            for i in range(li.size()):
                li.delete(0)
            if len(pse) == 0:
                pse.append('نتیجه ای یافت نشد')
            for i in pse:
                li.insert(END,i)
    def DELETE(li, ha, hp, hm, hc):
        itemnumber = li.curselection()
        if len(itemnumber)>0:
            itemname=li.get(itemnumber)
            if itemname != "No product found":
                choice= messagebox.askquestion('Delete', '?آیا از کار خود اطمینان دارید')
                if choice == 'yes':
                    if itemname in p12:
                        a = pit[0][itemname]
                        b = pit[1][a]
                        del pit[0][itemname]
                        del pit[1][a]
                        del pit[2][b]
                        ha.config(text = '')
                        hp.config(text = '')
                        hm.config(text = '')
                        hc.config(text = '')
                        a = p12.index(itemname)
                        p12.pop(a)
                        for i in range(li.size()):
                            li.delete(0)
                        for i in p12:
                            li.insert(END,i)
                        # print(pit)


class page:
    def CALCULATE():
        root = Tk()
        class add_number:
            def n0():
                x = sun.get()
                if len(x) != 0: sun.insert(END,"0")
            def n1(): sun.insert(END,"1")
            def n2(): sun.insert(END,"2")
            def n3(): sun.insert(END,"3")
            def n4(): sun.insert(END,"4")
            def n5(): sun.insert(END,"5")
            def n6(): sun.insert(END,"6")
            def n7(): sun.insert(END,"7")
            def n8(): sun.insert(END,"8")
            def n9(): sun.insert(END,"9")
        class erfun:
            def CE(vb):
                x = vb.get()
                for i in range(len(x)):
                    vb.delete(0)
                
            def jam(vb):
                x = vb.get()
                if "+" in x or "-" in x or "*" in x or "/" in x or "**" in x: pass
                elif len(x) == 0: pass
                else: vb.insert(END,"+")
            
            def men(vb):
                x = vb.get()
                if "+" in x or "-" in x or "*" in x or "/" in x or "**" in x: pass
                elif len(x) == 0: pass
                else: vb.insert(END,"-")

            def zar(vb):
                x = vb.get()
                if "+" in x or "-" in x or "*" in x or "/" in x or "**" in x: pass
                elif len(x) == 0: pass
                else: vb.insert(END,"*")
            
            def tag(vb):
                x = vb.get()
                if "+" in x or "-" in x or "*" in x or "/" in x or "**" in x: pass
                elif len(x) == 0: pass
                else: vb.insert(END,"/")

            def power(vb):
                x = vb.get()
                if "+" in x or "-" in x or "*" in x or "/" in x or "**" in x: pass
                elif len(x) == 0: pass
                else: vb.insert(END,"**")
            
            def Sqrt(vb):
                x = vb.get()
                try:
                    if "+" in x or "-" in x or "*" in x or "/" in x: pass
                    else:
                        if len(x) != 0:
                            for i in range(len(x)):
                                vb.delete(0)
                            a = sqrt(float(x))
                            a = str(a)
                            for i in a:
                                vb.insert(END,i)
                except ValueError:
                    for i in x: vb.delete(0)

            def numbersum(vb):
                x = vb.get()
                if len(x) != 0:
                    ui = 0
                    for i in x: ui += 1
                    
                    if x[ui-1] == "+" or x[ui-1] == "-" or x[ui-1] == "*" or x[ui-1] == "/": pass
                    elif "+" in x or "-" in x or "*" in x or "/" in x or "**" in x:
                        sub = vb.get()
                        
                        if "+" in sub:
                            try:
                                number1 = ''
                                number2 = ''
                                for i in sub:
                                    if i != "+": number1 += i
                                    else: break
                                # number1 ok
                                fg = list(sub)
                                for i in range(len(number1)+1): fg.pop(0)
                                for i in fg: number2 += i
                                # number2 ok
                                for i in sub: vb.delete(0)
                                hasel = float(number1) + float(number2)
                                for i in str(hasel): vb.insert(END,i)

                            except ValueError:
                                for i in sub: vb.delete(0)
                        
                        elif "-" in sub:
                            try:
                                number1 = ''
                                number2 = ''
                                for i in sub:
                                    if i != "-": number1 += i
                                    else: break
                                # number1 ok
                                fg = list(sub)
                                for i in range(len(number1)+1): fg.pop(0)
                                for i in fg: number2 += i
                                # number2 ok
                                for i in sub: vb.delete(0)
                                hasel = float(number1) - float(number2)
                                for i in str(hasel): vb.insert(END,i)
                            except ValueError: 
                                for i in sub: vb.delete(0)

                        elif "**" in sub:
                            try:
                                number1 = ''
                                number2 = ''
                                for i in sub:
                                    if i != "*": number1 += i
                                    else: break
                                # number1 ok
                                fg = list(sub)
                                for i in range(len(number1)+2): fg.pop(0)
                                for i in fg: number2 += i
                                # number2 ok
                                for i in sub: vb.delete(0)
                                hasel = float(number1) ** float(number2)
                                for i in str(hasel): vb.insert(END,i)
                            except ValueError:
                                for i in sub: vb.delete(0)

                        elif "*" in sub:
                            try:
                                number1 = ''
                                number2 = ''
                                for i in sub:
                                    if i != "*": number1 += i
                                    else: break
                                # number1 ok
                                fg = list(sub)
                                for i in range(len(number1)+1): fg.pop(0)
                                for i in fg: number2 += i
                                # number2 ok
                                for i in sub: vb.delete(0)
                                hasel = float(number1) * float(number2)
                                for i in str(hasel): vb.insert(END,i)
                            except ValueError:
                                for i in sub: vb.delete(0)

                        elif "/" in sub:
                            try:
                                number1 = ''
                                number2 = ''
                                for i in sub:
                                    if i != "/": number1 += i
                                    else: break
                                # number1 ok
                                fg = list(sub)
                                for i in range(len(number1)+1): fg.pop(0)
                                for i in fg: number2 += i
                                # number2 ok
                                for i in sub: vb.delete(0)
                                hasel = float(number1) / float(number2)
                                for i in str(hasel): vb.insert(END,i)
                            except ValueError:
                                for i in sub: vb.delete(0)
                            except ZeroDivisionError:
                                for i in sub: vb.delete(0)
                                vb.insert(0,"Error")

        def KCE(): erfun.CE(sun)
        def kojam(): erfun.jam(sun)
        def kmen(): erfun.men(sun)
        def kzar(): erfun.zar(sun)
        def kteg(): erfun.tag(sun)
        def kpow(): erfun.power(sun)
        def ksqrt(): erfun.Sqrt(sun)
        def sumer(): erfun.numbersum(sun)
        root.title("calculaator")
        root.geometry("280x350")
        root.config(bg = "black")
        root.resizable(False , False)
        # math:
        Button(root,text = "=",command = sumer).place(x = 219 , y = 291 , width = 60 , height = 60)
        Button(root,text = "+",command = kojam).place(x = 219 , y = 224 , width = 60 , height = 60)
        Button(root,text = "-",command = kmen).place(x = 219 , y = 157 , width = 60 , height = 60)
        Button(root,text = "*",command = kzar).place(x = 219 , y = 90 , width = 60 , height = 60)
        Button(root,text = "/",command = kteg).place(x = 219 , y = 23 , width = 60 , height = 60)
        Button(root,text = "pow",command = kpow).place(x = 142 , y = 23 , width = 60 , height = 60)
        Button(root,text = "sqrt",command = ksqrt).place(x = 75 , y = 23 , width = 60 , height = 60)
        Button(root,text = "CE",command = KCE).place(x = 8 , y = 23 , width = 60 , height = 60)
        # end math.
        sun = Entry(root, font = ("Times 14",19),bg = "#9BA4B5");sun.pack()
        # number:
        Button(root,text = "0",command = add_number.n0).place(x = 8 , y = 291 , width = 60 , height = 60)
        Button(root,text = "1",command = add_number.n1).place(x = 8 , y = 224 , width = 60 , height = 60)
        Button(root,text = "2",command = add_number.n2).place(x = 75 , y = 224 , width = 60 , height = 60)
        Button(root,text = "3",command = add_number.n3).place(x = 142 , y = 224 , width = 60 , height = 60)
        Button(root,text = "4",command = add_number.n4).place(x = 8 , y = 157 , width = 60 , height = 60)
        Button(root,text = "5",command = add_number.n5).place(x = 75 , y = 157 , width = 60 , height = 60)
        Button(root,text = "6",command = add_number.n6).place(x = 142 , y = 157 , width = 60 , height = 60)
        Button(root,text = "7",command = add_number.n7).place(x = 8 , y = 90 , width = 60 , height = 60)
        Button(root,text = "8",command = add_number.n8).place(x = 75 , y = 90 , width = 60 , height = 60)
        Button(root,text = "9",command = add_number.n9).place(x = 142 , y = 90 , width = 60 , height = 60)
        # end nuber.
        root.mainloop()
    def khayam():
        def adder():
            def backer():
                mo.destroy()
                page.khayam()
            kh.destroy()
            mo = Tk()
            mo.geometry("1200x740+10+10")
            mo.title("Khayam")
            mo.resizable(False,False)
            mo.config(bg = "#FF6500")
            mx = 140
            myf = 90
            for i in range(17):
                Label(mo,text = "$",bg = "#C40C0C",fg = "white").place(x = mx , y = 90 , width=25 , height=25)
                Label(mo,text = "$",bg = "#C40C0C",fg = "white").place(x = mx , y = 600 , width=25 , height=25)
                Label(mo,text = "$",bg = "#C40C0C",fg = "white").place(x = 140 , y = myf , width=25 , height=25)
                Label(mo,text = "$",bg = "#C40C0C",fg = "white").place(x = 1130 , y = myf , width=25 , height=25)
                mx += 59
                myf += 31.90

            my = 160
            for i in [":نام محصول",":از شرکت",":قیمت(تومان)",":طول عمر محصول(به ماه)"]:
                Label(mo,text = i,font = ("Times 14",40),bg = "#FF6500").place(x = 610 , y = my)
                my += 90
            item = Entry(mo,fg = "#FFC55A",bg = "#C40C0C" , font = ("Times 14",40),bd = 5);item.place(x = 230 , y = 160,width = 370)
            comp = Entry(mo,fg = "#FFC55A",bg = "#C40C0C" , font = ("Times 14",40),bd = 5);comp.place(x = 230 , y = 250,width = 370)
            cale = Entry(mo,fg = "#FFC55A",bg = "#C40C0C" , font = ("Times 14",40),bd = 5);cale.place(x = 230 , y = 340,width = 370)
            moon = Entry(mo,fg = "#FFC55A",bg = "#C40C0C" , font = ("Times 14",40),bd = 5);moon.place(x = 230 , y = 430,width = 370)
            def checked2():
                temp = True
                temp2 = True
                for i in 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"""!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"""':
                    if i in cale.get(): temp = False
                for i in 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"""!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"""':
                    if i in moon.get(): temp2 = False
                if len(item.get()) == 0 or len(comp.get()) == 0 or len(cale.get()) == 0 or len(moon.get()) == 0: algorithm.error_ok("!یک مشکل","لطفا به تمام سوالات پاسخ دهید")
                elif temp == False: algorithm.error_ok("!یک مشکل","قیمت کالا نادرست وارد شده است")
                elif temp2 == False: algorithm.error_ok("!یک مشکل","طول عمر کالا نادرست وارد شده است")
                else:
                    pit[0][item.get()] = comp.get()
                    pit[1][comp.get()] = cale.get()
                    pit[2][cale.get()] = moon.get()
                    p12.append(item.get())
                    backer()
            Button(mo,text = "اضافه کردن" , bg = "#FFAF61" , bd = 5 , font = ("Times 14",20),command = checked2).place(x = 227 , y = 520)
            Button(mo,text = "برگشت به صفحه اصلی" , bg = "#FFAF61" , bd = 5 , font = ("Times 14",20),command = backer).place(x = 390 , y = 520)
            
            mo.mainloop()
        
        
        kh = Tk()
        kh.geometry("1200x740+10+10")
        kh.title("Khayam")
        kh.resizable(False,False)
        kh.config(bg = "#DC0000")

        

        Button(kh , text = "اضافه کردن" , bg = "#FFAF61" , font = ("Times" , 20),command = adder).place(x = 15 , y = 620)
        def k_delete(): algorithm.DELETE(li,item_l,comp_l,cale_l,moon_l)
        Button(kh , text = " حذف کردن " , bg = "#FFC100" , font = ("Times" , 20),command = k_delete).place(x = 150 , y = 620)
        Button(kh , text = "ماشین حساب" , bg = "#FF8A08" , font = ("Times" , 20) , command = page.CALCULATE).place(x = 310 , y = 5)
        Button(kh , text = "افذودن به سبد خرید" , bg = "#FF6500" , font = ("Times" , 20)).place(x = 58 , y = 680)
        v = Entry(kh , font = ("Times",25) , bg = "#FF76CE" , bd = 6);v.place(x = 15 , y = 5 , width = 200)
        def k_search(): algorithm.Searched(v.get(),li)
        Button(kh , text = "سرچ" , bg = "#FFC100" , font = ("Times" , 18),bd = 5,command = k_search).place(x = 220 , y = 5)
        
        def Show(event):
            if li.size() > 0:
                itemnumber = li.curselection()
                if len(itemnumber) != 0:
                    itemname = li.get(itemnumber)
                    if itemname in p12:
                        item_l.config(text = itemname)
                        comp_l.config(text = pit[0][itemname])
                        cale_l.config(text = pit[1][pit[0][itemname]])
                        moon_l.config(text = pit[2][pit[1][pit[0][itemname]]])
        
        li = Listbox(kh,bg = "#FDDE55",bd = 5,font = ("Times",20));li.place(x = 15 , y = 60 , width = 270 , height = 560)
        for i in p12: li.insert(END,i)
        li.bind('<Double-1>', Show)
        my = 160
        for i in [":نام محصول",":از شرکت",":قیمت(تومان)",":طول عمر محصول(به ماه)"]:
            Label(kh,text = i,font = ("Times 14",30),bg = "#DC0000").place(x = 800 , y = my)
            my += 70

        
        item_l = Label(kh,text = "",bg = "#DC0000" , font = ("Times 14",30),bd = 5);item_l.place(x = 320 , y = 160)
        comp_l = Label(kh,text = "",bg = "#DC0000" , font = ("Times 14",30),bd = 5);comp_l.place(x = 320 , y = 230)
        cale_l = Label(kh,text = "",bg = "#DC0000" , font = ("Times 14",30),bd = 5);cale_l.place(x = 320 , y = 310)
        moon_l = Label(kh,text = "",bg = "#DC0000" , font = ("Times 14",30),bd = 5);moon_l.place(x = 320 , y = 380)
        kh.mainloop()
    def re_or_lo():
        # ما در این جا اول صفحه قبل را می بندیم و بعد صفحه جدید را می سازیم
        root.destroy()
        rl = Tk()
        rl.geometry("1200x740+10+10")
        rl.title("Khayam")
        rl.resizable(False,False)
        rl.config(bg = "#DC0000")

        mx = 140
        my = 90
        for i in range(17):
            Label(rl,text = "$",bg = "#FFCD32",fg = "white").place(x = mx , y = 90 , width=25 , height=25)
            Label(rl,text = "$",bg = "#FFCD32",fg = "white").place(x = mx , y = 600 , width=25 , height=25)
            Label(rl,text = "$",bg = "#FFCD32",fg = "white").place(x = 140 , y = my , width=25 , height=25)
            Label(rl,text = "$",bg = "#FFCD32",fg = "white").place(x = 1020 , y = my , width=25 , height=25)
            mx += 55
            my += 31.90
        Label(rl,text = "دوست من برای ورود گزینه زیر را فشار دهید",bg = "#DC0000",font = ("Times",30)).place(x = 310 , y = 160)
        def komaki():
            rl.destroy()
            page.register()
        # Button(rl , text = "ثبت نام",font = ("Times",20),bg = "#FFC55A",cursor = "heart",bd = 7).place(x = 350 , y = 350)
        Button(rl , text = " ورود ",font = ("Times",20),bg = "#FFC55A",cursor = "heart",bd = 7,command = komaki).place(x = 460 , y = 350)
        rl.mainloop()
    
    def register():
        re = Tk()
        re.geometry("1200x740+10+10")
        re.title("Khayam")
        re.resizable(False,False)
        re.config(bg = "#DC0000")

        Label(re,text = ".دوست من لطفا به سوالات زیر پاسخ دهید، و لطفا از حروف فارسی استفاده کنید",font = ("Times",25),bg = "#DC0000",fg = "#FFEC9E").pack()
        my = 90
        for i in [":نام",":نام خانوادگی",":شماره همراه"]:
            Label(re,text = i,bg = "#DC0000",font = ("Times",35),fg = "#FFF7FC").place(x = 850 , y = my)
            my += 70
        Label(re,text = ":تست من رباط نیستم",font = ("Times 14",40),fg = "#FFC55A",bg = "#DC0000").place(x = 820 , y = 350)
        name = Entry(re,font = ("Times",25),fg = "#912BBC",bg = "#FC4100",bd = 7);name.place(x = 450 , y = 100)
        name_b = Entry(re,font = ("Times",25),fg = "#912BBC",bg = "#FC4100",bd = 7);name_b.place(x = 450 , y = 170)
        phon = Entry(re,font = ("Times",25),fg = "#912BBC",bg = "#FC4100",bd = 7);phon.place(x = 450 , y = 240)
        text_r2 = algorithm.rand()
        # لیبل تست من رباط نیستم
        Label(re,text = text_r2 , font = ("Times",40), bg = "#DC0000").place(x = 790 , y = 500)
        robat = Entry(re,bd = 7,font = ("Times 14",40),bg = "#FF6500",fg = "#0E46A3");robat.place(x = 290 , y = 500,width = 440)
        def checked():
            temp = True
            for i in 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"""!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"""':
                if i in phon.get(): temp = False
            if len(name.get()) == 0 or len(name_b.get()) == 0 or len(phon.get()) == 0 or len(robat.get()) == 0: algorithm.error_ok("!یک مشکل" , "لطفا به تمام سوالات پاسخ دهید")
            elif temp == False: algorithm.error_ok("!یک مشکل","شماره تلفن مشکل دارد")
            elif (phon.get())[0] != "0" or (phon.get())[1] != "9": algorithm.error_ok("!یک مشکل","شماره تلفن مشکل دارد")
            elif len(phon.get()) != 11: algorithm.error_ok("!یک مشکل","ارقام شماره تلفن درست نیست")
            elif robat.get() != text_r2: algorithm.error_ok("!یک مشکل","تست من رباط نیستم نادرست است")
            else:
                re.destroy()
                page.khayam()
        Button(re,text ="ورود به صفحه اصلی", bg = "#FDDE55",font = ("Times",20),bd = 5,command = checked).place(x = 200 , y = 620)
        re.mainloop()


root = Tk()
# در اينجا صفحه ورودي را ميسازيم
root.geometry("1200x740+10+10")
root.title("Khayam")
root.resizable(False,False)
root.config(bg = "#DC0000")
mx = 10
for i in range(22):
    Label(root,text = " ",bg = "#FFCD32").place(x = mx , y = 120 , width=25 , height=25)
    mx += 55
Label(root,text = "خوش آمديد",font = ("Times",50),bg = "#DC0000").pack()
Label(root,text = "سلام دوست من",font = ("Times",60),bg = "#DC0000",fg = "yellow").place(x = 750 , y = 250)
Label(root,text = "اين برنامه براي راحتي کار شما مغازه داران عزيزه",font = ("Times",30),bg = "#DC0000",fg = "yellow").place(x = 490 , y = 350)
Label(root,text = "براي ورود دکمه را فشار دهيد",font = ("Times",45),bg = "#DC0000",fg = "white").place(x = 570 , y = 430)
Button(root,text = "  ادامه  ",font = ("Times",20),bd = 7,bg = "#FFA500",command = page.re_or_lo).place(x = 370,y = 440)
root.mainloop()
