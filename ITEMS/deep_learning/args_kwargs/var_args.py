#!/usr/bin/python3

def test_var_args(f_arg, *argv):
    print("First normal arg:", f_arg)
    for arg in argv:
        print("Another arg through *argv: ", arg)

test_var_args('Ryano', 'Python', 'eggs', 'test')

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" %(key, value))

greet_me(name="Ryan")

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)
args = ("two", 3, 5)
test_args_kwargs(*args)

kwargs = { "arg3": 3, "arg2": "two", "arg1": 5 }
test_args_kwargs(**kwargs)
