PWD="$(pwd)"
    DIR="${PWD}/env"
    if [ -d "$DIR" ]; then
        echo "virtual environment exists"
    else
        echo $'virtual environment does not exist \n creating virtual environment...'
        python3 -m venv env
    fi