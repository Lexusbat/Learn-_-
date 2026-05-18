from website import create_app 

app = create_app()

if __name__ == '__main__':  #Only if we run this file, not import this file 
    app.run(debug=True)  #Will excecute this line

#To run a flask application,startup a webserver, any changes to python code -
#Will automatically rerun the webserver (line 6)