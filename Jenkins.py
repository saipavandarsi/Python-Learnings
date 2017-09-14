import jenkins

#finding jenkins version

server = jenkins.Jenkins('https://cloudmatrix-jenkins.swg-devops.com:8443/login?from=%2F', username='shrmadis@in.ibm.com', password='Shru#1239')
user = server.get_whoami()
version = server.get_version()
print '\n\n user object is %s' % user
print 'Hello %s \n from Jenkins Version %s\n' %(user['fullName'], version)