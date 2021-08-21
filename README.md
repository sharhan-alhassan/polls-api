# polls-api
An end-to-end development process of Django Rest Framework (DRF)
For the Full Blog API, checkout to `chapter03-blog-api`
- `chapter03-blog-api` is a stand-alone project not merged with main


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