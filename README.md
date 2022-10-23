# Start-NTNU-Hackathon-2022

JOFEADAR is a simple application that let's you fast build dashboard for you specific use case. Has the ability to store wanted files which may be generated, and allows you to easily clean data from your favorite censor.

- [Presentation](https://docs.google.com/presentation/d/1jKLJZWKXbeiSMcCX9wsFdJUZh47pcVeYCSYsqyjhLrU/edit?usp=sharing)


## How to run

Run app.py and go to the provided localhost.

#### Application

- install the required python libraries
- python app.py

#### Notebooks

- In data-plots you can use notebook(s) to check individual loaded plots. Data processing notebook handles loading, cleaning, validation of data.

#### Dashboards

- Dashboard are the main component that shows the data and gives insight to the user.

#### Storage

- To build on file storage for the servce, you need an api key.
Here is a simple solution but bad one as key is exposed in the codebase. This should simply be gitignored in production.

#### Data processsing

- Pandas is the library used for data processing. 
This part includes loading in raw data, simple cleaning of data and saving to storage.

##### Error handling and data validation

- A part of the pipeline is used to check if the data is correct. Now we check for hex values to confirm file format. Trykksensor does not conform to the right format for example.

##### Machine learning and AI

- The data processing part could also include machine learning to be displayed to the user. This will be user-specific, but an example is in the end of the data processing notebook.

## Built With

* [DASH](https://dash.plotly.com/)
* [Plotly](https://plotly.com/dash/)
* [GCP](https://cloud.google.com/storage)
* [Bootstrap](https://getbootstrap.com)
* [Pandas]()
* [Numpy]()


## TEAM MEMBERS

* [Adam]()
* [Ferdinand]()
* [Joans]()
* [Arvin]()

## To Do's

- Make homepage
- Build out file storage, connect generatad file to bucket, bucket to storage.py (pages) and then have possibilty to download files direclty from cloud
- Create a slicker UI for the dashboards
- File error handling
- Incoroporate all parts off application in a more robust pipelline
- Complete .gitignore for __pycache__ files and api-key


## Articles and tutorials to help you build and understand the application 

- Dash multipage

https://community.plotly.com/t/multi-page-app-help/20410/3 


- Dash App Gallery:

https://dash-gallery.plotly.host/Portal/ 


- Dash components

https://dash.plotly.com/dash-core-components 


- Plotly Graphs

https://plotly.com/python/ 


- The Callback

Connects dash components + Plot Graphs

https://dash.plotly.com/basic-callbacks 


- Dash bootstrap components

https://dash-bootstrap-components.opensource.faculty.ai/

https://dash-bootstrap-components.opensource.faculty.ai/docs/components/dropdown_menu/ 


- Dash   

https://realpython.com/python-dash/ 


- Basic callbacks 

https://dash.plotly.com/basic-callbacks 

https://medium.datadriveninvestor.com/visualizing-some-key-financial-metrics-for-your-stocks-f987ea37035e



- Storage 

https://www.youtube.com/watch?v=pEbL_TT9cHg&ab_channel=JieJenn 

https://www.youtube.com/watch?v=bHudgNDyltI&ab_channel=Cloud%26AIAnalytics

https://www.youtube.com/watch?v=yStmKhLvay4&ab_channel=SoumilShah 

https://soumilshah1995.blogspot.com/2020/11/getting-started-with-gcp-storage-bucket.html



- Downloading dynamically generated files from a Dash/Flask app


 https://stackoverflow.com/questions/54443531/downloading-dynamically-generated-files-from-a-dash-flask-app 

- Dash download 

https://dash.plotly.com/dash-core-components/download 

## Relevant sources on data

- Water physics
https://www.fondriest.com/environmental-measurements/parameters/water-quality/water-temperature/

- North Sea
https://en.wikipedia.org/wiki/North_SeaNorth Sea

- Oil-fields
https://en.wikipedia.org/wiki/File:North_Sea_oil_and_gas_fields.svg

- ISD4000 manual
https://www.impactsubsea.co.uk/wp-content/uploads/2022/06/ISD4000-Manual-Rev-2.0.pdf