# VALU3S web_server (plone&buildout)

Plone is use as the web server in VALU3S. This reposiory contains the deployment configuration and operations based on buildout.

The content on this repo is based on  **Buildout for the Mastering Plone Training** project

http://training.plone.org

The only difference is that the VALU3S framework extension is also added in this repo buildout config.

## Installation

This installation is based pn Pyhton Virtual Enviroments. If you want to use install Plone in virtual machine use vagrant. Follow Mastering plone Tarining [Step 5](https://training.plone.org/5/plone_training_config/instructions_plone5.html). You can also install/deploy  Plone as a  Docker container ([Plone Docker Install](https://docs.plone.org/manage/docker/docs/index.html)).


```bash
$ python3 -m venv .
$ source bin activate 
(web_server)$ pip install -r requirements.txt
(web_server)$ bin/buildout
(web_server)$ bin/instance start
```
And now navigate to **localhost:8080/** and create a Web site. Once the web site has been created install add the VALU3S Framework Plone extension just Throug The web from the **Admin** menu. Click  **Site Setup**  menu and select **Add-ons** section.And finally install the extension. Now you can add locally V&V data about methods, tools, organizations and Use cases. The default credentials of the installation are *admin/admin*. 

To stop the server just 
```bash
(web_server)$ bin/instance stop
```


