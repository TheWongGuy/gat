#!/bin/bash
function gat(){
    cd ~/.gat
    source .venv/bin/activate
    python gat.py "$@"
    if [ $? = 2 ] ; then
        project_dir=$(cat ~/.gat/gattemporary)
        cd "$project_dir"
    fi
}