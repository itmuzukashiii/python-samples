@echo off

set hand=KD QD AD JD 10D
echo hand: %hand% ?
echo %hand% | python poker.py
echo;

set hand=KD 8S KS 8D KH
echo hand: %hand% ?
echo %hand% | python poker.py
echo;
pause
