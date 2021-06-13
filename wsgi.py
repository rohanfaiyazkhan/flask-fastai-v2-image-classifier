"""Web Server Gateway Interface"""

##################
# FOR PRODUCTION
####################
from flaskr.app import app

if __name__ == "__main__":
    ####################
    # FOR DEVELOPMENT
    ####################
    app.run(debug=True)