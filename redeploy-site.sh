git fetch && git reset origin/main --hard
virtualenv env
source env/bin/activate
systemctl restart myportfolio
source python3-virtualenv/bin/activate
flask run --host=0.0.0.0