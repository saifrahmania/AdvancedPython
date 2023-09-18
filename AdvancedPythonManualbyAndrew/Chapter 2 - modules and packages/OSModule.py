import os 
# // give me some examples about OSModule
# // You will have to talk about the following:
# // 1. os.name
# // 2. os.getcwd()
# // 3. os.listdir()
# // 4. os.mkdir()
# // 5. os.makedirs()
# // 6. os.remove()
# // 7. os.rmdir()
# // 8. os.removedirs()
# // 9. os.rename()
# // 10. os.stat()
# // 11. os.path.join()
# // 12. os.path.split()
# // 13. os.path.exists()
# // 14. os.path.isdir()
# // 15. os.path.isfile()
# // 16. os.path.splitext()
# // 17. os.path.getsize()
# // 18. os.path.getmtime()
# // 19. os.path.abspath()
# // 20. os.path.dirname()
# // 21. os.path.basename()
# // 22. os.path.commonprefix()
# // 23. os.path.expanduser()
# // 24. os.path.expandvars()
# // 25. os.path.normpath()
# // 26. os.path.relpath()
# // 27. os.path.curdir
# // 28. os.path.pardir
# // 29. os.path.walk()
# // 30. os.path.supports_unicode_filenames
# // 31. os.path.samefile()
# // 32. os.path.sameopenfile()
# // 33. os.path.samestat()
# // 34. os.path.ismount()
# // 35. os.path.splitdrive()
# // 36. os.path.getatime()
# // 37. os.path.getctime()
# // 38. os.path.islink()
# // 39. os.path.isabs()
# // 40. os.path.lexists()
# // 41. os.path.realpath()
# // 42. os.path.expandvars()
# // 43. os.path.expanduser()
# // 44. os.path.normcase()
# // 45. os.path.normpath()
# // 46. os.path.relpath()
# // 47. os.path.supports_unicode_filenames
# // 48. os.path.walk()
os.chdir('C:\\Users\\Admin\\Documents\\GitHub\\AdvancedPython\\Chapter 2 - modules and packages')
os.getcwd() # get current working directory
os.mkdir('DeleteModule') # create a folder
os.rmdir('DeleteModule') # delete a folder
os.listdir() # list all files and folders in current directory
os.remove('DeleteModule.py') # delete a file
os.rename('DeleteModule.py', 'DeleteModule.py') # rename a file
os.path.exists('DeleteModule.py') # check if a file exists
os.path.isdir('DeleteModule.py') # check if a file is a directory
os.path.isfile('DeleteModule.py') # check if a file is a file
os.path.splitext('DeleteModule.py') # split a file name into name and extension
os.path.getsize('DeleteModule.py') # get the size of a file
os.path.getmtime('DeleteModule.py') # get the last modified time of a file
os.path.getatime('DeleteModule.py') # get the last accessed time of a file
os.path.relpath('DeleteModule.py') # get the relative path of a file
os.path.realpath('DeleteModule.py') # get the real path of a file
os.path.abspath('DeleteModule.py') # get the absolute path of a file
os.path.dirname('DeleteModule.py') # get the directory name of a file
os.path.basename('DeleteModule.py') # get the base name of a file
os.path.commonprefix('DeleteModule.py') # get the common prefix of a file
os.path.expanduser('DeleteModule.py') # expand the user of a file
os.path.expandvars('DeleteModule.py') # expand the variables of a file
os.path.walk('DeleteModule.py') # walk through a file
os.path.samestat('DeleteModule.py') # check if two files have the same stat
os.path.normcase('DeleteModule.py') # normalize the case of a file
os.path.normpath('DeleteModule.py') # normalize the path of a file