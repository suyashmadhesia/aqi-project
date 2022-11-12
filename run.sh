SCR="$(pwd)/env/bin/activate"
if [ -e "$SCR" ]
then
    source $(pwd)/env/bin/activate
else
    $(pwd)/env/Scripts/activate
fi 
RED='\033[0;31m'
if test "$#" -eq 0
then 
  printf "${RED}err: Provide a environment name\n${RED}"
  exit 1
fi
if [ "$1" = "local" ];
then
    echo "Running locally..."
    uvicorn main:app --reload
    exit 0
elif [ "$1" = "server" ]
then
    echo "Running on server..."
    uvicorn main:app
    exit 0
else
    printf "${RED}err: Invalid environment name...${RED}\n"
    exit 1
fi