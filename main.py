from website import create_app
# learnt from https://www.youtube.com/watch?v=dam0GPOAvVI&t=4263s
app = create_app()

# the below code says only if we run main file, the code inside will execute
if __name__ == '__main__':
    # debug = true means it will rerun the server everytime a change is made
    app.run(debug=True)