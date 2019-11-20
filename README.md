# Jooble Test Task
It is a service, that allows you to make your url shorter and more readable.
Every url will be tracking how many times it was used

### Installation
Prerequisites:
* python 3.6
* pip3
* virtualenv 15.1

If you don't have it installed on your computer, here is the instruction to install these packages in **Ubuntu 18.04.03 LTS**.
```
sudo apt-get install python3.6
sudo apt-get install python3-pip
pip3 install virtualenv
```
Then you need to install project requirements.
```
cd <project directory>
sh install.sh
```
That's all. Now you need to run the server
```
python3 manage.py runserver <port>
You can leave <port> blank, if you want it to be default (8000)
```
### Testing
To ensure that everything is working well, you can run command
```
python3 manage.py test
```
Or you can write your own tests inside **url_shortener/tests.py** file

### Delete expired url's
User can choose the lifetime for his url. To delete expired url's from database, you can run the following command:
```
python3 manage.py delete_expired_links
```

### Api Endpoints
```
<domain>/api/links/
GET:
    show all links that already exist in database
    return: json with all links
POST:
    insert link into database
    fields: original_url, url that will be encoded
            lifetime, int from 1 to 360, default is 90, number of days while redirect will be working
    return: json with fields (url, short_url, original_url, visits, created, lifetime)

<domain>/api/links/<id>/
GET:
    show the information about one specific link
    return: json with fields (url, short_url, original_url, visits, created, lifetime)
```
