# OnlineJudge

[![Build Status](https://travis-ci.org/imustacm/OnlineJudge.svg?branch=master)](https://travis-ci.org/imustacm/OnlineJudge)

An OnlineJudge base on python.

## Getting Started

[Click to download the latest OnlineJudge](https://github.com/imustacm/OnlineJudge/archive/master.zip) or clone from Github

```
git clone --recursive https://github.com/imustacm/OnlineJudge.git
```

### Prerequisites

1. Ubuntu 16.04 LTS or MacOS
2. Postgresql >= 9.6
3. redis-server4.0.8
4. redis-sentinel4.0.8
5. Python3.6

> Notice: Python and Redis we not verify other versions.

**Ubuntu16.04**

> sudo reqiure

```shell
sudo apt install postgresql
sudo apt install redis-server
sudo apt install redis-sentinel
```
About Sentinel  
You can run Redis in sentinel mode with the –sentinel arg, or by its command named: redis-sentinel. This will vary from your distribution and version of Redis, so check its help page to know how you can run it.  
In any case, you will need to run a sentinel node, as OnlineJudge uses it to load-balance the queries, and also to autoconfigure the master and slaves automagically.


**MacOS**

> Use Homebrew, [Install Homebrew](https://brew.sh/) first.

```shell
brew install redis
brew install postgres
brew install python
```
> Notice: Install python not python3 [Read more](https://discourse.brew.sh/t/brew-install-python3-fails/1756)

### Installing

#### Install in Ubuntu

**Configuring Python**  
Installing [virtualenv](http://pypi.python.org/pypi/virtualenv) in the Ubuntu:  
> lines starting with # are comments

```
sudo apt-get install python-virtualenv
```
After installing the software you will be able to create independent virtual environments for the `OnlineJudge` installation as well as for the template projects.  
If you decide to use a virtualenv then, follow these steps :

```shell
# get the source code if you didn't got it.
git clone --recursive https://github.com/imustacm/OnlineJudge.git
# Access the source code folder
cd OnlineJudge
virtualenv env
# Activate the virtual environment
source env/bin/activate
# Upgrade pip to latest version
pip install -U pip
# Install the required libraries
pip install -r requirements.txt
```
Otherwise, you should be able to install the libraries in your system like this:

```
# get the source if you didn't get it.
git clone --recursive https://github.com/imustacm/OnlineJudge.git
# Access the source code folder
cd OnlineJudge
# Upgrade pip to latest version
pip install -U pip
# Install the required libraries
pip install -r requirements.txt
```
Create a settings file (include all we need config files) and enter your SQLAlchemy DB URI (you can also override default settings as needed):

```shell
cp config.py.template config.py
cp sentinel.conf.template sentinel.conf
# now edit ...
vim config.py
vim sentinel.conf
```
**Configuring Redis and Redis-sentinel**  
To run OnlineJudge, you will need first to configure a Sentinel node. Create a config file named sentinel.conf with something like `sentinel.conf.template`

```shell
# make sure redis-server is start
redis-server sentinel.conf --sentinel
```

**Configuring Database**  

```shell
sudo su postgres
# Login postgres user
createuser -d -P onlinejudge
```
> You should use the same username that you have used in the config.py file.

Use password `onlinejudge` when prompted.  
After running the last command, you may also have to answer to these questions:  

* Shall the new role be a super user? Answer n (press the n key).
* Shall the new role be allowed to create databases? Answer y (press the y key).
* Shall the new role be allowed to create more new roles? Answer n (press the n key).

And now, you can create the database:

```shell
createdb onlinejudge -O onlinejudge
```
Finally, exit the postgresql user:

```shell
exit
```
Then, populate the database with its tables:

```shell
python manager.py upgrade
```
Run the web server:

```shell
python manager.py runserver
# or
python run.py
```
Open in your web browser the following URL: http://localhost:5000/api/ping	  
And if you see the:
 
```json
{
  "data": [
    "It's OK, you get me", 
    {}
  ], 
  "status": 200
}
```
Then, your installation has been completed

## Running the tests

This is still a work in progress


## Deployment

This is still a work in progress

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used

This is still a work in progress

## Contributing

This is still a work in progress

## Authors

* **Zhaoyaqiong** - *Initial work* - [Zhaoyaqiong](https://github.com/zhaoyaqiong)

See also the list of [contributors](https://github.com/imustacm/OnlineJudge/graphs/contributors) who participated in this project.

## License

Thinking

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* [Pybossa](https://pybossa.com/) I copy the docs and I like Pybossa Project.

