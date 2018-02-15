The application loads the Scene and Shapes using django templates using aframe
The Models are defines in xrframework/models
The url to call is localhost:<portnumber>/aframe/<id>   where is is the scene id to load
The Scene are associated with one or more Shapes and the attributes of the Shape are stores as a
JSON String.
Please load copy the sqllite db or create your own using migrations. Copy the files under the app xrframework
And add Scene and Shapes to the admin console and invoke the url as above passing in the Scene ID 
