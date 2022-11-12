$(pwd)/scripts/env.sh
source $(pwd)/env/bin/activate || $(pwd)/env/Scripts/activate
if [ -e requirements.txt ]
then
    echo "installing packages from requirements.txt"
    pip install -r requirements.txt
else
    echo "requirements.txt does not exist"
    exit 1
fi