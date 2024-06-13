git clone https://github.com/kaiynbaev/practice_13.06.2024.git
cd practice_13.06.2024
cd app
nano .env
enter postgresql(
DB_NAME 
DB_USER 
DB_PASS 
DB_HOST 
DB_PORT 
)
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 manage.py makemigration account, tender, registration
python3 manage.py migrate
python3 manage.py runserver

