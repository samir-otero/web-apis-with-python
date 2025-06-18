from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    """
    TODO: Render the home page provided under templates/index.html in the repository
    """
    return render_template( "index.html" )

@app.get("/search")
def search():
    """
    TODO:
    1. Capture the word that is being searched
    2. Seach for the word on Google and display results
    """
    args = request.args.get( "q" )
    # if the button clicked is "Search", redirect to Google search results
    if request.args.get("btn") == "Search":
        return redirect(f"https://google.com/search?q={args}")
    # if the button clicked is "I'm Feeling Lucky", redirect to the first result
    elif request.args.get("btn") == "I'm Feeling Lucky":
        return redirect(f"https://google.com/search?q={args}&btnI=1")

if __name__ == "__main__":
    app.run()