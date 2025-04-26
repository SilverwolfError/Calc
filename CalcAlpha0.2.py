import tkinter as t
import tkinter.messagebox as tm
import math
import sympy as s
import string as st
from sympy import Expr,Symbol,sympify

def asciifind(something):
    letters=set(st.ascii_letters)
    letters_include=[]
    for i in something:
        if i in letters:
            letters_include.append(i)
    return letters_include
root = t.Tk()
root.geometry('420x300')
def closed():
    root.destroy()
def dynamic_windows_width(window,labels):
    window.update()
    max_width=max(f.winfo_width() for f in labels)
    window_width=max_width+20
    window.geometry(f'{window_width}x200')
def general(operation,clues=['Please input first number','Please input second number']):
    new = t.Toplevel(root)
    entries=[]
    labels=[]
    for i in clues:
        label = t.Label(new,text=i)
        label.grid()
        labels.append(label)
        e = t.Entry(new)
        e.grid()
        entries.append(e)
    dynamic_windows_width(new,labels)
    def calc():
            prm = [j.get() for j in entries]
            if all(isinstance(k,(int,float)) for k in prm) == True:
                res = operation(*prm)
                if isinstance(res,(int,float)):
                    back = tm.showinfo("tk",'result:'+str(round(res,5)))
                    if back == 'ok':
                        closed()
                elif isinstance(res,str):
                    tm.showinfo("tk",'result:'+res)
                else:
                    tm.showerror(str(type(res)),'Something went wrong.Please Try Again.')
            elif all(isinstance(k,str) for k in prm) == True:
                if operation.__name__ in ('extandexp', 'factorexp','afe','fs','fa','l1'):
                    res = operation(*prm)
                    if isinstance(res,(int,float)):
                        back = tm.showinfo("tk",'result:'+str(round(res,5)))
                        if back == 'ok':
                            closed()
                    elif isinstance(res,str):
                        tm.showinfo("tk",'result:'+res)
                    elif isinstance(res,Expr):
                        tm.showinfo("tk",'result:'+str(res))
                    else:
                        return
    t.Button(new,text='Get Rusult',command=calc).grid()
    t.Button(new,text='Quit',command=new.destroy).grid()
def extra():
    extrawindow=t.Toplevel(root)
    extrawindow.geometry('410x300')
    def triangle_area():
        general(lambda x,y:x*y/2)
    def rectangle_perimeter():
        general(lambda x,y:(x+y)*2)
    def polygon_area():
        general(lambda x,y:x/4*y**2*(1/math.tan(math.pi/x)),['Please input number of polygon sides','Please input Polygon side length'])
def addition():
    general(lambda x,y:x+y,['Please input an adder','Please input another adder'])
def subtraction():
    general(lambda x,y:x-y,['Please input subtracted number','Please input subtractive number'])
def multiplication():
    general(lambda x,y:x*y,['Please input a multiplier','Please input another multiplier'])
def division():
    def divide(x,y):
        if y == 0:
            tm.showerror("Error!",'The Divisor is Zero,Please Try Again!')
        else:
            return x/y,x//y,x%y
    general(divide,['Please input dividend','Please input divisor'])
def power():
    general(lambda x,y:x**y,['Please input base number','Please input exponential'])
def radical():
    general(lambda x,y:x**(1/y),['Please input square a number of times','Please input ordinal number'])
def logarithm():
    general(math.log,['Please input base number','Please input a number'])
def comparisons():
    def cmprs(x,y):
        if x>y:
            return str(x)+' is bigger than '+str(y)
        if x==y:
            return str(x)+' is equal '+str(y)
        if x<y:
            return str(x)+' is smaller than '+str(y)
    general(cmprs)
def ands():
    general(lambda x,y:x&y)
def ors():
    general(lambda x,y:x|y)
def xor():
    general(lambda x,y:x^y)
def nots():
    general(lambda x:~x,['Please input a number'])
def left():
    general(lambda x,y:x<<y)
def right():
    general(lambda x,y:x>>y)
def xnor():
    general(lambda x,y:x^y^1)
#expand & factor
def extand():
    def extandexp(expression):
        if not expression:
            tm.showerror("Error!",'The Experssion is Empty!')
            return
        expletters = s.symbols(asciifind(expression))
        expanded = s.expand(expression)
        return expanded
    general(extandexp,['Please input an expression'])
def factori():
    def factorexp(expression):
        if not expression:
            tm.showerror("Error!",'The Experssion is Empty!')
            return
        expletters = s.symbols(asciifind(expression))
        factored = s.factor(expression)
        return factored
    general(factorexp,['Please input an expression'])
def add_for_expression():
    def afe(expression1,expression2):
        if not expression1 or not expression2:
            tm.showerror("Error!",'The Experssion is Empty!')
            return
        expletters1 = s.symbols(asciifind(expression1))
        expletters2 = s.symbols(asciifind(expression2))
        final = s.expand(s.parse_expr(expression1)+s.parse_expr(expression2))
        return final
    general(afe,['Please input the first experssion','Please input the second experssion'])

def subtraction_for_expression():
    def afe(expression1,expression2):
        if not expression1 or not expression2:
            tm.showerror("Error!",'The Experssion is Empty!')
            return
        expletters1 = s.symbols(asciifind(expression1))
        expletters2 = s.symbols(asciifind(expression2))
        final = s.expand(s.parse_expr(expression1)-s.parse_expr(expression2))
        return final
    general(afe,['Please input the first experssion','Please input the second experssion'])

def multiplication_for_expression():
    def afe(expression1,expression2):
        if not expression1 or not expression2:
            tm.showerror("Error!",'Experssion is Empty!')
            return
        expletters1 = s.symbols(asciifind(expression1))
        expletters2 = s.symbols(asciifind(expression2))
        final = s.expand(s.parse_expr(expression1)*s.parse_expr(expression2))
        return final
    general(afe,['Please input the first experssion','Please input the second experssion'])

def division_for_expression():
    def afe(expression1,expression2):
        if not expression1 or not expression2:
            tm.showerror("Error!",'Experssion is Empty!')
            return
        expletters1 = s.symbols(asciifind(expression1))
        expletters2 = s.symbols(asciifind(expression2))
        final = s.expand(s.parse_expr(expression1)/s.parse_expr(expression2))
        return final
    general(afe,['Please input the first experssion','Please input the second experssion'])
def fraction_simplification():
    def fs(fraction):
        try:
            fraletters = s.symbols(asciifind(fraction))
            final = s.cancel(fraction)
            return final
        except:
            tm.showerror("Error!",'The Fraction is wrong.Maybe You should add "*" between number and letter.Please Try Again When You Changed.')
    general(fs,['Please input a expression what is in fraction'])
def fraction_add():
    def fa(fraction1,fraction2):
        try:
            fraletters1 = s.symbols(asciifind(fraction1))
            fraletters2 = s.symbols(asciifind(fraction2))
            final = s.cancel(s.together(sympify(fraction1)+sympify(fraction2)))
            return final
        except:
            tm.showerror("Error!",'The Fraction is wrong.')
    general(fa,['Please input the first fraction','Please input the second fraction'])
def fraction_subtraction():
    def fa(fraction1,fraction2):
        try:
            fraletters1 = s.symbols(asciifind(fraction1))
            fraletters2 = s.symbols(asciifind(fraction2))
            final = s.cancel(s.together(sympify(fraction1)-sympify(fraction2)))
            return final
        except:
            tm.showerror("Error!",'The Fraction is wrong.')
    general(fa,['Please input the first fraction','Please input the second fraction'])
def le1un():
    def l1(equation):
        eqlist = equation.split('=')
        equation2 = s.Eq(sympify(eqlist[0]),sympify(eqlist[1]))
        final = s.solve(equation2)
        return final
    general(l1,['Please input a 1:1'])
t.Button(root,text='Addition',command=addition).grid(row=0,column=0)
t.Button(root,text='Subtraction',command=subtraction).grid(row=0,column=1)
t.Button(root,text='Multiplication',command=multiplication).grid(row=0,column=2)
t.Button(root,text='Division',command=division).grid(row=0,column=3)
t.Button(root,text='Power',command=power).grid(row=0,column=4)
t.Button(root,text='Radical',command=radical).grid(row=1,column=0)
t.Button(root,text='Logarithm',command=logarithm).grid(row=1,column=1)
t.Button(root,text='Comparisons',command=comparisons).grid(row=1,column=2)
t.Button(root,text='And',command=ands).grid(row=1,column=3)
t.Button(root,text='Or',command=ors).grid(row=1,column=4)
t.Button(root,text='Xor',command=xor).grid(row=2,column=0)
t.Button(root,text='Not',command=nots).grid(row=2,column=1)
t.Button(root,text='Left',command=left).grid(row=2,column=2)
t.Button(root,text='Right',command=right).grid(row=2,column=3)
t.Button(root,text="Xnor",command=xnor).grid(row=2,column=4)
t.Button(root,text='Expand',command=extand).grid(row=3,column=0)
t.Button(root,text='Factor',command=factori).grid(row=3,column=1)
t.Button(root,text='Expression\nAddition',command=add_for_expression).grid(row=3,column=2)
t.Button(root,text='Expression\nSubtraction',command=subtraction_for_expression).grid(row=3,column=3)
t.Button(root,text='Expression\nMultiplication',command=multiplication_for_expression).grid(row=3,column=4)
t.Button(root,text='Expression\nDivision',command=division_for_expression).grid(row=4,column=0)
t.Button(root,text='Fraction\nSimplification',command=fraction_simplification).grid(row=4,column=1)
t.Button(root,text='Fraction\nAdd',command=fraction_add).grid(row=4,column=2)
t.Button(root,text='Fraction\nSubtraction',command=fraction_subtraction).grid(row=4,column=3)
t.Button(root,text='Solve 1:1',command=le1un).grid(row=4,column=4)
t.Button(root,text='Extra Option',command=extra).grid(row=5,column=1)
t.Button(root,text='Quit',command=closed).grid(row=5,column=3)

root.mainloop()