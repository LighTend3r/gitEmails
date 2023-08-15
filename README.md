# gitEmails

GitEmails and a tool to retrieve all emails from a github account

## Installation

```
git clone https://github.com/LighTend3r/gitEmails.git
```

Install all requirements
```
pip install -r requirements.txt
```

## Usage

The user can be found in url of github account
```
python3 main.py emails --user <user>
or
python main.py emails --url https://github.com/<user>
```

### View remaining credits 

```
python3 main.py credits
```

### Use token

Currently, if you don't use a github token, you can only make 60 requests per hour.
To retrieve a github token, go to your google account settings, then to "Developer Settings", then to "Personal access token" das generate a clasic token

![image](https://github.com/LighTend3r/gitEmails/assets/87587438/241f18e0-5f57-4d54-90b9-3fd4b1616bd1)


```
python3 main.py emails --user <user> -t <token>

python3 main.py credits -t <token>
```

### Output in json

```
python3 main.py emails --user <user> -t <token> -j <path>
or
python3 main.py credits -t <token> -j <path>
```



