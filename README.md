# OnlineJudge

**requirement**

1. Ubuntu16.04 (em….other system we didn't test)
2. postgres10
3. python3
In you shell

```shell
git clone https://github.com/imustacm/OnlineJudge.git
cd OnlineJudge
pip install -r requirements.txt
cp config.py.template config.py
# notice: change your config especially databaseuri
python manage.py shell
```
In python shell
```python
db.create_all()
exit()
```
In you shell

```shell
python run.py
# or
python manager.py runserver
```

If you not change host and port config. Server will run in localhost:5000

Enter http://localhost:5000/api/ping in your browser.

You can 'run python manager.py test' in your shell to test project.