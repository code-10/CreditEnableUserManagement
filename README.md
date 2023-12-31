# CreditEnableUserManagement

A User Management System supporting CRUD operations for users, complete with an integrated logging system within middleware that connects to a NoSQL MongoDB. Additionally, it features a Celery task to send email notifications upon successful user account creation. This system uses MySQL as the database for data storage and leverages FastAPI as the web server.

Prerequisites
1. Python

Steps to run the application
1. Create a Virtual Environment\
   `virtualenv venv`
3. Install all the requirements\
  `pip install -r requirements.txt`
4. Run the Fastapi Application\
   `uvicorn app.main:app --reload`
5. Run Celery, Celery Beat and Flower\
  `celery -A app.celery_config worker --loglevel=debug`\
  `celery -A app.celery_config beat`\
  `celery -A app.celery_config flower`\

Details about MySQL DB\
I have used free MySQL remote db, please find the information below\
[Link to FreeDB](#https://freedb.tech/dashboard/)\
`email: nereji6806@usoplay.com`\
`password: nereji6806@usoplay.com`

Details about GMX Mail\
[Link to GMX](#https://www.gmx.com/)\
`email: nereji6806@gmx.us`\
`password: nereji6806@usoplay.com`\

Helpful Commands to get information about Celery\
[http://localhost:5555](#http://localhost:5555)\
1. `celery -A app.celery_config inspect registered`\
2. `celery -A app.celery_config inspect reserved`\
3. `celery -A app.celery_config inspect scheduled`

Head to [http://localhost:8000/docs](#https://localhost:8000/docs) for Swagger Link\
![Screenshot 2023-12-31 211643](https://github.com/code-10/CreditEnableUserManagement/assets/23309323/093ad724-0e94-40cb-888f-0a0590a52c79)

Database Snapshot\
![Screenshot 2023-12-31 211930](https://github.com/code-10/CreditEnableUserManagement/assets/23309323/97ce9211-4dba-432f-8a07-be3b40cca266)

MongoDB Logging\
![Screenshot 2023-12-31 215939](https://github.com/code-10/CreditEnableUserManagement/assets/23309323/462f8609-7acb-4232-ad4e-a50bb86e9446)

Celery Task\
![Screenshot 2023-12-31 151425](https://github.com/code-10/CreditEnableUserManagement/assets/23309323/00d6ade9-b437-414c-b53d-58f0b11b7a52)
![Screenshot 2023-12-31 151508](https://github.com/code-10/CreditEnableUserManagement/assets/23309323/0779c9c4-77f6-48c0-a313-d887e8cac1ad)
![Screenshot 2023-12-31 151531](https://github.com/code-10/CreditEnableUserManagement/assets/23309323/d34fa078-ac2a-40d5-9c0b-3e9818141140)
![Screenshot 2023-12-31 151425](https://github.com/code-10/CreditEnableUserManagement/assets/23309323/684bd6ee-7181-444a-8262-252882eb16db)
![Screenshot 2023-12-31 151315](https://github.com/code-10/CreditEnableUserManagement/assets/23309323/068bc57d-f960-41de-b2b7-903895456efa)


