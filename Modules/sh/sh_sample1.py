# coding=utf-8

import sh

print sh.ifconfig("lo0")

print(sh.ls("/"))

# print(sh.Command("zsh"))

p=sh.sleep(3, _bg=True)
print "print directly"
p.wait()
print "3 sec later"
