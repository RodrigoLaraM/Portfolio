cd Portfolio
git fetch && git reset origin/main --hard
virtualenv env
source env/bin/activate
pip install -r requirements.txt
systemctl restart myportfolio
cd
clear