# Stack-OverFlow-Clone

- Get this project locally into your machine by running git clone.
- `git clone https://github.com/ravinderreddy-p/stack-overflow-clone.git`

## Front-End:
- Go to Frontend path: `/stack-overflow-clone/frontend/stack-overflow-clone`
- run `ng build` & then `ng serve`
- Navigate to `http://localhost:4200/`
- You need to provide existed user to login to the app. If user not exist, you need to register by postman by calling API end point: '/api/addUser' by passing `username`. [Ensure Backend app is running]


## Back-end:
- Navigate to `/stack-overflow-clone/stack-overflow-clone/backend`
- Create venv `python3 -m venv venv`
- Activate venv `source venv/bin/activate`
- pip install requirements.txt
- export FLASK_APP=src/api.py
- export FLASK_ENV=development 
- Apply Flask DB migrations `flask db upgrade`
- flask run
- Backend app runs on: http://127.0.0.1:5000/

- Note that before running backend app, ensure to create DB.

## Database:
- Update `database_path = 'postgresql://pravinderreddy@localhost:5432/sof-clone'` to your local DB path. 

