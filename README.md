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
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [ # new
    'rest_framework.authentication.SessionAuthentication', # for browsable api
    'rest_framework.authentication.TokenAuthentication'
],
}

# Project-Level permissions: Update the DEFAULT_PERMISSION_CLASSES with any of these in settings.py
• AllowAny - any user, authenticated or not, has full access

• IsAuthenticated - only authenticated (logged in), registered users have access

• IsAdminUser - only admins/superusers have access

• IsAuthenticatedOrReadOnly - unauthorized users can view any page, but only
authenticated users have write, edit, or delete privileges
```

```javascript
DRF Permissions can be allowed at 
• project-level
• view-level, or
• at any individual model level.

```

### Custom Permissions:

```python
- Internally, Django REST Framework relies on a BasePermission class from which all
other permission classes inherit

- Here is the actual source code which
is available on Github:

class BasePermission(object):
    """
    A base class from which all permission classes should inherit.
    """
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
    """
        return True


    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

```
### Four(4) different types of Authentication
```python
## 1. Basic Authentication Flow:
1. Client makes an HTTP request

2. Server responds with an HTTP response containing a 401 (Unauthorized) status
code and WWW-Authenticate HTTP header with details on how to authorize

3. Client sends credentials back via the Authorization HTTP header

4. Server checks credentials and responds with either 200 OK or 403 Forbidden status
code

*Note that the authorization credentials sent are the unencrypted base64 encoded version of <username>:<password> . So in my case, this is admin:password123 which with
base64 encoding is d3N2OnBhc3N3b3JkMTIz .*

### Why Basic Authentication is not advisable:
- The primary advantage of this approach is its simplicity. But there are several major
downsides. First, on every single request the server must look up and verify the
username and password, which is inefficient. It would be better to do the look up
once and then pass a token of some kind that says, this user is approved. Second,
user credentials are being passed in clear text—not encrypted at all—over the internet.
This is incredibly insecure. Any internet traffic that is not encrypted can easily be
captured and reused. Thus `basic authentication should only be used via` **HTTPS**, the
secure version of HTTP .


## 2. Session Authentication
1. A user enters their log in credentials (typically username/password)
2. The server verifies the credentials are correct and generates a session object that
is then stored in the database
3. The server sends the client a session ID—not the session object itself—which is
stored as a cookie on the browser
4. On all future requests the session ID is included as an HTTP header and, if verified
by the database, the request proceeds
5. Once a user logs out of an application, the session ID is destroyed by both the
client and server
6. If the user later logs in again, a new session ID is generated and stored as a cookie
on the client


## 3. Token Authentication

Token-based authentication is stateless: once a client sends the initial user creden-
tials to the server, a unique token is generated and then stored by the client as either
a cookie or in local storage. This token is then passed in the header of each incoming
HTTP request and the server uses it to verify that a user is authenticated. The server
itself does not keep a record of the user, just whether a token is valid or not.

### NOTE:
Cookies vs localStorage

Cookies are used for reading server-side information. They are smaller (4KB) in
size and automatically sent with each HTTP request. LocalStorage is designed for
client-side information. It is much larger (5120KB) and its contents are not sent by
default with each HTTP request. Tokens stored in both cookies and localStorage are
vulnerable to XSS attacks. The current best practice is to store tokens in a cookie with
the httpOnly and Secure cookie flags.

### Outstanding win for Token Authentication
There are multiple benefits to this approach. Since tokens are stored on the client,
scaling the servers to maintain up-to-date session objects is no longer an issue. And
tokens can be shared amongst multiple front-ends: the same token can represent a
user on the website and the same user on a mobile app. The same session ID can not
be shared amongst different front-ends, a major limitation.

### Downside of Tokens
A potential downside is that tokens can grow quite large. A token contains all user
information, not just an id as with a session id/session object set up. Since the token
is sent on every request, managing its size can become a performance issue.

- 

```
- Tokens are only generated after there is an API call for a user to
log in.

- Install: pip install `django-rest-auth`: For login, logout, password reset for clients.
- add `rest_auth` to Installed apps
- paths:
    1. `<domain.com>/api/v1/rest-auth/login`
    2. `<domain.com>/api/v1/rest-auth/logout`
    3. `<domain.com>/api/v1/rest-auth/password/reset`

- Install: pip install `django-allauth`: To couple with `rest_auth` for registration

```
In our front-end framework, we would need to capture and store this token(generated during registration) on the
client either in localStorage or as a cookie. Then configure our application so that all
future requests include the token in the header as a way to authenticate the user.
```

### Viewsets and Routers

```python
- A viewset is a way to combine the logic for multiple related views into a single class

- In other words, one viewset can replace multiple views.

- ModelViewSet which provides both a
list view and a detail view for us. And we no longer have to repeat the same queryset
and serializer_class for each view.

```