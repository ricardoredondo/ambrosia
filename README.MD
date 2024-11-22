# Ambrosia

Lets Chat with oir diet Shit
Assume all code here is not production ready. This system is a POC desingned as a learning project.  


## Services:

### Loader App
This service is a deamon listening to changes in a folder with data
Learning service. How to create a Vector DB

### Source Loader
This folder holds the DATA to be stored as vectos. 

### Storage Data
This folder holds the vector database once the source information is parsed.    


## Building Commands



### Installation
``` 
# Like the Gemfile.lock
pip freeze > requirements.txt  

# These versions are used in the Jupiter tool 
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

`
### Build A given service

```
# Build all the services in the docker-compose file
$ docker-compose build                    
```
```
# Build only one service by the service name ( Must be listed in the docker file)
$ docker-compose build <service name>     
```

## Running Commands


```
docker-compose run --service-ports <service name> bash 
```


To run the project, execute the following commands:
