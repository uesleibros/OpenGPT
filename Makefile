.PHONY: dependencies clean

dependencies:
  pip install -r requirements.txt
  
clean:
  rm -f *.pyc
