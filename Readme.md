# Integrate Django with React
## Why use Django with React integration
Django is one of the most complete web development frameworks available, with which manages everything from database to the HTML sent to the client. 

On other hands, React is such a powerfull tool to create frontend web applications, in particular if planning to crate a single-page application.

So merging the functionality of Django with the frontend versatility of React come in handy.

In order to do that is necessary to use Django to manage the backend of the application creating an API which send data to a React application that will render the web page. This will completely separate the backend and the frontend, with the ability of develop both in their respective enviroments independently.

# Django
## Setup
In addition to the normal installation, Django needs two dependencies to create a Rest Api:
- the toolkit ==Django REST Framework==
- ==django-cors-headers== to handle server headers required for Cross-Origin Resource Sharing
These two dependencies will help comunicating with React app in case, in general these are useful with applications which try to access the API.

Both these dependencies must be added as an installed app into django settings.py as "corsheaders" and "rest_framework" and a middleware, for use a filter to apply CORS logic to application's requests, must be added as "corsheaders.middleware.CorsMiddleware"

## Creating the API
After having created an app inside the django project, it is time to create the behavior of the API.

The first step is to create a model which will instruct the database, then create a migrations and migrate it.

In order to work, Django make use of views. A view, in Django, is an initial entrypoint of a request made through a specific endpoint served by an URL. This can be mapped by using Django REST Framework by connecting the function itself to the endpoint. 

REST Framework uses also a serializer to allow complex data to be converted into native python datatypes. 

Creating a new file "serializers.py" can be useful and there the serializers can be imported (`from rest_framework import serializers`). Next step is create a class using the serializer with a `class Meta` that made use of the desidered models and its fields.  

```
class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test 
        fields = ('field', 'field', 'field')
```

Now the serializer must be imported into views.py where, assuming that urls are already been created, is possible to handle requests.
```
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Student
from .serializers import *
```

The let the serializer works it needs to get the data from the models or from the requests depending if the view receive a get request from the client that asks for the data
```
data = Test.objects.all()
serializer = TestSerializer(data, context={'request': request}, many=true)
return Response(serializer.data)
```
or if the client is trying to post some new information into the database.
```
serializer = TestSerializer(data=request.data)
if serializer.is_valid():
    serializer.save()
    return Response(status=status.HTTP_201_CREATED)
return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Now is possible to test the API by simply requesting the urls from the browser, where Django will render an human-friendly HTML output for easy browsing into the API.

## React
After creating a new react app, alongside the Django's one, is possible to create the style of the page. How the page is styled is not importat as it is completly arbitrary. But, React needs a way to interact with the API, and to do that it can use ==Axios==.

==Axios== is a promise-based HTTP client and can be installed as dependencies using `npm install axios`.

Another useful thing is create a ==constants== folder in which store a file with constants. In this case just add the base URL to the API, to avoid writing it into the React code, by simply creating an ==index.js== file and adding the constant `export const API_URL = "http://localhost:8000/api/test"`[^1]

[^1]: Note that this is only a placeholder to connect the React app to an api running in local for developing.

Now axios can imported into the needed React components and, after importing also the constant of the API url, use his shorthand methods to make an HTPP request
```
import axios from "axios";

import {API_URL} from "../constants";
...
    axios.post('/login', {
        firstName: 'Finn',
        lastName: 'Williams'
    })
    .then((response) => {
        console.log(response);
    }, (error) => {
        console.log(error);
    });
...
```
