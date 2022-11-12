$(pwd)/scripts/env.sh
source $(pwd)/env/bin/activate || $(pwd)/env/Scripts/activate
RED='\033[0;31m'
if test "$#" -eq 0
then 
  printf "${RED}err: Provide at least one Python package name\n${RED}"
  exit 1
else 
  for package in "$@"
  do
    pip install $package
    pkg=$(pip freeze | grep -i $package)
    if grep -Fq $pkg requirements.txt
    then
      echo "skipping entry in requirements.txt"
    else
      echo "adding entry in requirements.txt"
      pip freeze | grep -i $package >> requirements.txt
    fi
  done
fi