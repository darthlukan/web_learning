// No JQuery
var xhr;

var ajaxDelete = function () {
    try {
        xhr = new XMLHttpRequest();
    } catch (error) {
        try {
            xhr = new ActiveXObject('Microsoft.XMLHTTP');
        } catch (error) {
            xhr = null;
        }
    }

    if (xhr != null) {
    
        xhr.open('POST', 'url', true);
    
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) {
                if (xhr.status == 200 || xhr.status == 304) {
                    // do stuff
                } else {
                    // do other stuff
                }
            }
        };
        
        xhr.send();
        return false;
    } else {
        return false;
    }
}

// With JQuery
// Basic:

var dataArrayOrObject = array({
    'key': 'val',
    'key1': 'val1'
    });

$.ajax({
        type: 'POST', // POST, GET, PUT, DELETE
        url: 'example.com',
        data: dataArrayOrObject,
    });

// With JQuery
// POST:

$.post({
    url: 'example.com',
    data: dataArrayOrObject,
    callback: function () {
        //do stuff on success
        // WILL SILENTLY FAIL ON ERROR!
    }
});

// With JQuery
// GET:

$.get('remote_path',
      {'param': 'param_value'},
      function (returned_data) {
        //do stuff
      }
    );