# polls-api
An end-to-end development process of Django Rest Framework (DRF)

# Adding CORS

```python
• pip install django-cors-headers

• add corsheaders to the INSTALLED_APPS

• add CorsMiddleware above CommonMiddleWare in MIDDLEWARE

• create a CORS_ORIGIN_WHITELIST

```

```javascript
• There are two popular ways to make HTTP requests: 
with the built-in Fetch API or
with axios, which comes with several additional features. 

• We will use axios in this
example.

• $ npm install axios

*******************************************************
• First, we’ll use axios for our GET request. We can make
a dedicated `getTodos` function for this purpose.

* Second, we want to make sure that this API call is issued at the correct time during
the React lifecycle. HTTP requests should be made using `componentDidMount` so we
will call getTodos there.
```

```python
# new
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',    # default port for React app
    'http://localhost:8000',    # port for hosting the api
)

# third-party
    'rest_framework',
    'corsheaders',

# Cors middleware
    'corsheaders.middleware.CorsMiddleware',

# Explicitly allowing permissions for everyone
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.AllowAny',
    ]
}
```