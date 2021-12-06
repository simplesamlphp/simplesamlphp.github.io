#! /bin/python3

import markdown
import glob
import os
import urllib.request
import json 
from bs4 import BeautifulSoup

# for which versions should we generate documentation?
# ToDo: replace with dynamic assasment based on github tags
ssp_versions=["latest","1.19", "1.18", "1.17"]
#ssp_versions=["latest"]



# Some functions

# Convert md file to html file
# - make sure links remain working
# - add header, navigation and footer to the converted file
def md2html(md_file, html_file, file_name):
    #print("Working on: " + md_file)
    
    with open(md_file, 'r') as f:
       text = f.read()

       html = markdown.markdown(text, tab_length=2)
       soup = BeautifulSoup(html, 'html.parser')
       for a in soup.findAll('a'):
         
         if not a['href'].startswith(('http://', 'https://')):
           if not a['href'].endswith(('html')):
              a['href'] = a['href']+".html"
       
           if (str(a['href']).find(":") > 0):
             a['href'] = a['href'].replace(":", "/")
       
       # TODO: At this point we could use title and description to auto generate a breadcrum or an index
       #title = soup.find('h1').string
       #if (len(title.split(":")) > 1):
       #  title = title.split(":")[1]
       
       #desc = ""
       #p = soup.find('p')
       #if not p is None:
       #   desc = " - " + str(p.string)

    with open(html_file, 'w') as f:
       f.write(header + mkContentHeader(ssp_versions) + str(soup.prettify()) + footer)	

# search a filesystem directory for subdirs and retum these in a list
def getsubdirs(dir_path):
	return(glob.glob(dir_path + '*/'))

# search a filesystem directory for markdown (md) files and parse these into html using the md2html function
def parsefiles(docsdir, outputdir):
    print("parsing files from '" + docsdir + "' into '" + outputdir + "'")

    if os.path.isdir(docsdir):

      if not os.path.isdir(outputdir):
        os.makedirs(outputdir)

      print("OutputDir? " + str(os.path.isdir(outputdir)))

      os.chdir(docsdir)

      for file in glob.glob('*.md'):
        md_file = docsdir + file
        html_file = outputdir + file[:-3] + '.html'

        md2html(md_file, html_file, file)

# get a list of all repositories in the ssp github project
def getmodulerepos():
    module_repos = []
    
    with urllib.request.urlopen("https://api.github.com/users/simplesamlphp/repos") as url:
       repos = json.loads(url.read().decode())
    
    for repo in repos:
      a_repo = {"name": [], "description": [], "html_url": []}
	
      # we assume all module will have a name that starts with 'simplesamlphp-module-' 
      if (repo['name'].find('simplesamlphp-module-') == 0):
        a_repo['name'] = str(repo['name'])
        a_repo['description'] = str(repo['description'])
        a_repo['html_url'] = str(repo['html_url'])

        module_repos.append(a_repo)       
    
    return module_repos

# clone a specific git repo to a given directory. Optionally fetch specific version
# Target directories will be autocreated
def getgitrepo(repo, repo_clone_dir, repo_root, version=None):
   os.makedirs(os.path.join(repo_clone_dir))
   os.chdir(repo_clone_dir)
   os.system('git clone --depth=1 ' + repo)
   os.chdir(repo_clone_dir + repo_root)
   
   print("Working in git repo from" + os.getcwd())
   
   if (version is not None):
      os.system('git checkout -b ' + version)
   os.system('git status')

# make the header and headerbad div contents for indjection into each documentation page
def mkContentHeader(versions):
    content = '<body>'

    content += '<!-- Red logo header -->'
    content += '<div id="header">'
    content += '	<div id="logo"><a href="https://simplesamlphp.org" style="color: #fff; text-decoration: none" target="_blank">SimpleSAMLphp</a></div>'
    content += '</div>'
    content += '<!-- Grey header bar below -->'
    content += '<div id="headerbar" style="clear: both">'
    content += mkNavigation(versions)
    #content += '<p id="breadcrumb">Home</p><div class="mtoolbar"><div class="menuitem first"><a href="/download">Download</a></div><div class="menuitem"><a href="/docs">Documentation</a></div><div class="menuitem"><a href="/security">Security</a></div><div class="menuitem"><a href="/modules">Modules</a></div><div class="menuitem"><a href="/translation">Translation</a></div><div class="menuitem"><a href="/developers">Developers</a></div><div class="menuitem"><a href="/releaseplan">Roadmap</a></div><div class="menuitem"><a href="/awards">Awards</a></div><div class="menuitem"><a href="/users">Users</a></div><div class="menuitem"><a href="/lists">Mailing lists</a></div><div class="menuitem last"><a href="/support">Support</a></div></div><br style="clear: both; height: 0px; width: 0px" />'
    content += '<br style="height: 0px; clear: both" />'
    content += '</div><!-- /#headerbar -->'
    content += '<div id="content">'
   
    return content

# make a navigation structure based on the versions we have doucmentation for    
def mkNavigation(versions):
    
    content = '<div id="langbar" style="clar: both"><div id="navigation">Documentation is available for the following versions: '
    for version in versions:
        content += '<a href="/'+version+'/index.html">'+version+'</a> | '
    content += ' modules</div></div>'
    
    return content

# make sure some hard coded resources like css, js and some images are put in the right place for teh website
def mkResources(root_dir, web_root):
    # Copy over the website js and css resources
    #if not os.path.exists(os.path.join(site_root_dir + '/res/js/')):
    os.makedirs(os.path.join(web_root + '/res/js/'))
   
    #if not os.path.exists(os.path.join(site_root_dir + '/res/css/')):
    os.makedirs(os.path.join(site_root_dir + '/res/css/'))
    os.system('cp -R ' +  root_dir + 'resources/js/ ' + web_root + 'res/')
    os.system('cp -R ' +  root_dir + 'resources/css/ ' + web_root + 'res/')

    # starter index.html (just a redirect to 'latest')    
    os.system('cp ' +  root_dir + 'resources/index.html ' + root_dir + 'html/index.html ')



################################################
#
# MAIN
#
################################################

# Configuration of static variables
root_dir = "website_scripts/"
tempdir = "/tmp/ssp_tmp/"

repo_root_dir = "simplesamlphp/"
repo_docs_dir = "docs/"
repo_modules_dir = "modules/"

site_root_dir = "./_site/docs/"
header = "website_scripts/resources/header"
footer = "website_scripts/resources/footer"


# Housekeeping actions
# Clean up the tempdir, just to be sure
#os.system('rm -Rf ' +  site_root_dir + '/*')

# Clean up the html dir, just to be sure
#os.system('rm -Rf ' +  tempdir)

# make the header and footer available as global vars
print("reading Header")
with open(header, 'r') as f:
  header = f.read()

print("reading Footer")
with open(footer, 'r') as f:
  footer = f.read()

# Copy the starter index.html that will always redirect to "latest"
#mkResources(root_dir, site_root_dir)

# Now generate contents based documentation for core simplesamlphp repo
for ssp_version in ssp_versions:
   print("Working on: " + ssp_version)
   print("Repo Root: " + repo_root_dir)
   
   version_dir = tempdir + ssp_version + "/"
   print("Version dir: " + version_dir)

   
   getgitrepo('https://github.com/simplesamlphp/simplesamlphp.git', version_dir, repo_root_dir, ssp_version)

   versioned_site_root =  site_root_dir + ssp_version + "/"
   print("versioned_site_root: " + versioned_site_root)
   
   # Parse main docs for this version
   parsefiles(os.path.join(version_dir, repo_root_dir, repo_docs_dir), versioned_site_root)

   # get all the modules in this version
   #mods = getsubdirs(os.path.join(os.path.join(version_dir, repo_root_dir, repo_modules_dir)))

   # parse 'core' modules docs (if available)
   #for module in mods:
    #print("Working on: " + module)
    
    #module_name = os.path.basename(os.path.normpath(module))
    #module_dir = os.path.join(module, "docs/")
    #module_output_dir = os.path.join(versioned_site_root, module_name + "/" )
    #parsefiles(module_dir, module_output_dir)

# fetch and generade documentation for contributed modules as made availabe in the ssp repos
#contrib_mods = getmodulerepos()

#for module in contrib_mods:
#    print("Working on: " + module["name"])
#    contrib_mod_dir = tempdir + "contrib_modules/" + module["name"] + "/"
#    contrib_mod_web_dir = site_root_dir + "contrib_modules" + "/"
#    
#    getgitrepo(module["html_url"], contrib_mod_dir, module["name"])
#    
#   #module_name = os.path.basename(os.path.normpath(module))
#    module_dir = os.path.join(contrib_mod_dir, module["name"], "docs/")
#    print(module_dir)
#    module_output_dir = os.path.join(contrib_mod_web_dir, module["name"].split("-")[2] + "/" )
#    print(module_output_dir)
#    parsefiles(module_dir, module_output_dir)


   
# Clean up the tempdir
#os.system('rm -Rf ' +  tempdir)

