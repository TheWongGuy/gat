#!/bin/bash
function gat(){
    CURDIR=$(pwd)
    TEMPFILE=$(echo ~/.gat/gattemporary)
    cd ~/.gat
    source .venv/bin/activate
    python gat.py "$@"
    deactivate
    if [ -f $TEMPFILE ] ; then
        project_dir=$(cat ~/.gat/gattemporary)
        cd "$project_dir"
    else
        cd "$CURDIR"
    fi
}