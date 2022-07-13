cd Portfolio
git fetch && git reset origin/main --hard
virtualenv env
tmux kill-session
source env/bin/activate
pip install -r requirements.txt
systemctl restart myportfolio
source python3-virtualenv/bin/activate
flask run --host=0.0.0.0