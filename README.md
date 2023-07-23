# Backend-API-Invoker
# http://apiinvoker.pythonanywhere.com/

## This project is made made to access data through news-api.org in frontend projects. As in free plan they don't allow to fetch data when site is hosted on github pages.

## Example:-

```javascript
fetch("https://apiinvoker.pythonanywhere.com/api/", {
        method: "POST",
        body: JSON.stringify({
            'api': url
        })
    })
        .then((response) => response.json())
        .then((data) =>  console.log(data))
```

### Above link may not work in future as it is hosted for 3 months in free plan, after 3 months we need to refresh it. Try to host on your own server.


### username : ApiInvoker
### mail : zkfefcyqnvwihjrxzq@cazlg.com
### pass : 79...
