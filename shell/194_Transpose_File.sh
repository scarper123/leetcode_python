#!/usr/bin/env bash

#   Given a text file file.txt, transpose its content.
#
#   You may assume that each row has the same number of columns and each field is separated by the ' ' character.
#
#   For example, if file.txt has the following content:
#
#   name age
#   alice 21
#   ryan 30
#   Output the following:
#
#   name alice ryan
#   age 21 30

# awk
awk '{
    for (i = 1; i <= NF; i++) {
        if (NR == 1){
            s[i]=$i;
        }else{
            s[i] = s[i] " " $i;
        }
    }

}
END {
    for (i = 1; s[i] != ""; i++) {
        print s[i];
    }
}
' 194.txt

# python
#python -c """res = []
#with open('194.txt') as f:
#    for line in f:
#        res.append(line.split())
#
#for tmp in zip(*res):
#    print(' '.join(tmp))
#"""