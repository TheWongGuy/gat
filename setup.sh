#!/bin/bash
rm -rf ~/.gat

mkdir ~/.gat

#
cp ./gat.sh ~/.gat/gat.sh
source ~/.gat/gat.sh
#

cp ./gat.py  ~/.gat/gat.py
cp -r ./src ~/.gat/src
cp -r ./.venv ~/.gat/.venv