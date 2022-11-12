$(pwd)/scripts/env.sh
source $(pwd)/env/bin/activate || $(pwd)/env/Scripts/activate
RED='\033[0;31m'
if [ -e requirements.txt ]
then
    echo "installing packages from requirements.txt"
    pip install -r requirements.txt
else
    printf "${RED}requirements.txt does not exist${RED}\n"
    exit 1
fi