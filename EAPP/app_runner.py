from . import create_app  
import os

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


#run interminal;
#(venv) bhupathisaicharan@CBHUPATHI EAPP % cd ~/Documents/BD\ CODES/ECM_BD
#(venv) bhupathisaicharan@CBHUPATHI ECM_BD % source EAPP/venv/bin/activate
#(venv) bhupathisaicharan@CBHUPATHI ECM_BD % python -m EAPP.app_runner
#* Serving Flask app 'EAPP'
#* Debug mode: on
#WARNING: This is a development server. Do not use it in a production deployment.
# Use a production WSGI server instead.
# * Running on http://127.0.0.1:5000
#Press CTRL+C to quit
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 102-088-865