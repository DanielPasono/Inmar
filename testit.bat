echo off
echo ######################
echo    Required output
echo ######################
echo on
python piecemv.py -p wQ -s a1
python piecemv.py -p wQ -s h8
python piecemv.py -p wQ -s c4
python piecemv.py -p bQ -s f5 

python piecemv.py -p wR -s a1
python piecemv.py -p bR -s h8
python piecemv.py -p wR -s c4
python piecemv.py -p wR -s f5 

python piecemv.py -p wN -s a1
python piecemv.py -p wN -s h8
python piecemv.py -p bN -s c4
python piecemv.py -p wN -s f5 

echo off
echo ######################
echo    Optional output
echo ######################
echo on

python piecemv.py -h

python piecemv.py -p wB -s a1
python piecemv.py -p bB -s f5 

python piecemv.py -p bK -s a1
python piecemv.py -p wK -s f5 

python piecemv.py -p wP -s b2 
python piecemv.py -p wP -s a3
python piecemv.py -p wP -s c8 

python piecemv.py -p bP -s d7 
python piecemv.py -p bP -s c6
python piecemv.py -p bP -s g1 

