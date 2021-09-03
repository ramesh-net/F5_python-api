# Get Virtual server and Pool memnbers information

## Installation steps:

###### For Windows users:

1. Clone the repository using Git/GitHub Desktop.  [More Info](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop)
2. Change working directory to F5_python-api/ in cmd prompt/powershell
3. Create a Python Virtual Environment
```ps
       pip install virtualenv
       virtualenv myenv
       myenv\Scripts\activate
       pip install -r requirements.txt
```

###### For Linux/MAC users:

1. Clone the repository using Git/GitHub Desktop.  [More Info](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop)
2. Change working directory to F5_python-api/ in terminal
3. Create a Python Virtual Environment and install dependencies
```shell
       pip install virtualenv
       virtualenv myenv
       source myenv\Scripts\activate
       pip install -r requirements.txt
```

**Arguments to be passed:**

**--token** - token

**--host** - hostname

###### Example
```python
python get_vs&pool_info.py --host **HOSTNAME** --token **TOKEN** 

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:12<00:00,  1.28s/it]
Completed
File Location: 
```


