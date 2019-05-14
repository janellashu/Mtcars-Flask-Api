# Mtcars-Flask-Api
STAT 418, HW#3

**1. In command line, change directory to the docker folder and run: docker-compose up** <br/>
   &nbsp;&nbsp;&nbsp;&nbsp;If there is an error like "ModuleNotFoundError: No module named 'statsmodels'", try: docker images ls <br/>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If there is a docker_flask image, run: docker rmi docker_flask -f <br/>

After you see, something like this: <br/>
&nbsp;&nbsp;&nbsp;&nbsp;Starting docker_flask_1 ... done <br/>
&nbsp;&nbsp;&nbsp;&nbsp;Attaching to docker_flask_1 <br/>
&nbsp;&nbsp;&nbsp;&nbsp;flask_1  |  * Serving Flask app "server" (lazy loading) <br/>
&nbsp;&nbsp;&nbsp;&nbsp;flask_1  |  * Environment: production <br/>
&nbsp;&nbsp;&nbsp;&nbsp;flask_1  |    WARNING: Do not use the development server in a production environment. <br/>
&nbsp;&nbsp;&nbsp;&nbsp;flask_1  |    Use a production WSGI server instead. <br/>
&nbsp;&nbsp;&nbsp;&nbsp;flask_1  |  * Debug mode: on <br/>
&nbsp;&nbsp;&nbsp;&nbsp;flask_1  |  * Running on ht<span>tp://</span>0.0.0.0:####/ (Press CTRL+C to quit) <br/>
&nbsp;&nbsp;&nbsp;&nbsp;flask_1  |  * Restarting with stat <br/>
&nbsp;&nbsp;&nbsp;&nbsp;flask_1  |  * Debugger is active! <br/>
&nbsp;&nbsp;&nbsp;&nbsp;flask_1  |  * Debugger PIN: ###-###-### <br/>


**2. Open a new terminal (be in the same directory) and run the following curl command: curl ht<span>tp://</span>localhost:5000/** <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You should get the response: "server is up - nice job! " <br/>

**3. To get a prediction of mpg using predictors**: weight in thousands of pounds (wt); 1/4 mile time (qsec); transmission (am) where 0 = automatic and 1 = manual <br/>

**curl -H "Content-Type: application/json" -X POST -d '{"wt":"3.73", "qsec":"17.6", "am":"0"}' "ht<span>tp://</span>localhost:5000/predict_mpg"** <br/>

&nbsp;&nbsp;&nbsp;&nbsp;You can change any of the 3 values to see the prediction change. <br/>

**4. To stop your server running the API, type ctrl-C in first terminal** <br/>

*OPTIONAL: Check to see if you have any docker containers running using docker container ls and stop them through "docker container kill &lt;container-name >"* <br/>
