$(pwd)/scripts/env.sh
source env/bin/activate
if test "$#" -eq 0
then 
  echo $'Provide at least one Python package name\n' 
else 
  for package in "$@"
  do
    pip install $package
    '\n' >> requirements.txt
    pip freeze | grep -i $package >> requirements.txt
  done
fi