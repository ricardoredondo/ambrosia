# Ambrosia

Lets Chat with our nutrition data. Kind of a Diet specialist on an REST API.


**IMPORTANT**: Assume all code here is not production ready. This system is a POC desingned as a learning project:

### Learning / Practice Areas
- Python 
- Flask
- LangChain
- OpenAI
- Docker as a practice 


## Services
System is designed in smaller services. 


### Loader App
This service is a deamon developed in Python. It listens to changes in a particular folder. It reads only PDF files and loads its contents to a Vector DB. 

Once all files are loaded, it saves the Vector DB under the 'storage_data' folder and creates a new 'current' package. 

If there already is a 'current' package, the old one gets renamed (include a timestamp)

---
### Jenkins App
This is a Python Rest API. Build using Flask and different other libraries. 

This API lets you discuss the content stored in the vector DB. 
Current implemented endpoints:

> Status of the service. This endpoint helps make sure the service is up and running. 
``
curl --location 'jenkins.localtest.me/status'
``


> Ask endpoint allow us to get information about the data. Required parameter 'q' passes the query to the system

``
curl --location 'jenkins.localtest.me/api/ask' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'q=What is the main subject of the content?'
``

---
### Secretary
This is the REACT APP that allow the user to interact with the data thru the API 



---
### Source Loader Folder
- source_loader

This folder holds the DATA to be stored as vectors. We should include only PDF files as service will only read PDF. 

---
### Storage Data Folder
- storage_data

This folder holds the vector database once the source information is processed. Vector DB is stored in a 'current' package. Preexistent versions are stored as backups.   

---

## How to build / Run Docker images

Loader App
* docker-compose build loader_app
* docker-compose run --service-ports loader_app bash 
* docker-compose up loader_app

API App
* docker-compose build jenkins
* docker-compose run --service-ports jenkins bash 
* docker-compose up jenkins 

FrontEnd App
* docker-compose run --service-ports secretary bash 
* docker-compose up secretary


Both services have a `run` command that needs to executed afert loggin into the shell. Docker Compose up will run the service from the start



### Libraries / Packages

``` 
# How to get the packages stored in a lock file
pip freeze > requirements.txt  

# These versions are used in the Jupiter tool. Used them here to keep consistency
pip install chromadb==0.3.26
pip install pulsar-client==3.5.0
pip install openai==0.27.0
pip install pypdf==3.7.1
pip install langchain==0.0.213
pip install beautifulsoup4==4.12.3
pip install tiktoken==0.4.0


# This block shows the versions installed
import sys
import pkg_resources

list = ["chromadb", "pulsar-client", "openai", "langchain", "pypdf", "beautifulsoup4", "tiktoken"]

for ele in list:
    version = pkg_resources.get_distribution(ele).version
    print(f"{ele} version: {version}")
print("Python version:", sys.version)



# pip install -U langchain-community
```




## TODO


### Loader APP:

* Check for preious Current version and decide if it is worth generating a new version
* 

