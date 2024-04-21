#!/sys/bin/sh
#!/usr/bin/sys/bash

if pip show -V requests > log
then
    rm -rf log
else
    pip install requests
fi

kivyfunction(){
   if pip show -V kivy -q
then
   echo "kivy is installed"
else
   pip install kivy
fi

}

while true
do
  kivyfunction
  if pip show -V kivy;then
      break
  else
      kivyfunction
  fi
done
