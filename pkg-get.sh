$(pwd)/scripts/env.sh
source env/bin/activate
if test "$#" -eq 0
then 
  echo $'Provide at least one Python package name\n' 
else 
  for package in "$@"
  do
    pip install $package
    pkg=$(pip freeze | grep -i $package)
    if grep -Fq $pkg requirements.txt
    then
      echo "skipping entry in requirements.txt"
    else
        pip freeze | grep -i $package >> requirements.txt
    fi
  done
fi