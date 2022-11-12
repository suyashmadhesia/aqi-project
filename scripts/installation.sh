$(pwd)/scripts/env.sh
SCR="$(pwd)/env/bin/activate"
if [ -e "$SCR" ]
then
    source $(pwd)/env/bin/activate
else
    source $(pwd)/env/Scripts/activate
fi 
RED='\033[0;31m'
if [ -e requirements.txt ]
then
    echo "installing packages from requirements.txt"
    pip install -r requirements.txt
else
    printf "${RED}requirements.txt does not exist${RED}\n"
    exit 1
fi