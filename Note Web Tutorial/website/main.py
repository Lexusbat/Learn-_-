from website import create_app
#Enabled because when an __init__.py file is in a folder it makes it a package

app = create_app()

if __name__ == '__main__': #Only if we run this file, the next line will be executed
    app.run(debug=True)

#Flask Application and Startup webserver and if puthon code changes - will automatically rerun webserver
