to create the virtual env 
python -m venv ./venv
to get in the virtual env 
.\venv\Scripts\activate
to get out the virtual env 
deactivate

installing pakeges in the vierual env 
py -m pip install -r requirements.txt
py -m pip install {PAKAGE NAME}

runnig the code in the virtual env 
cd app
python -m uvicorn main:app --reload

go to swagger api 
http://127.0.0.1:8000/docs