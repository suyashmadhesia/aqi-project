source $(pwd)/env/bin/activate
if test "$#" -eq 0
then 
  echo $'Provide at branch name\n' 
  exit 1
fi
if [ "$1" = "local" ];
then
    echo "Running locally"
    uvicorn main:app --reload
    exit 0
elif [ "$1" = "server" ]
then
    echo "Running on server"
    uvicorn main:app
    exit 0
else
    echo "Invalid argument"
    exit 1
fi