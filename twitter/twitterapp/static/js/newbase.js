$(document).ready(function(){
    $.ajax('/newajax/',{
        'type' : 'POST',
        'async' : true,
        'datatype' : 'json',
        'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
        },
        'success' : function(data){
            document.getElementById('basediv').innerHTML += data
        }
    })
})