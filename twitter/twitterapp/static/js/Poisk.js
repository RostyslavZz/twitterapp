$(function(){
    $('#123').on('input',function(e){
console.log(1)
        $.ajax('/Poisk/',{
            'type': 'POST',
                'async': true,
                'dataType': 'json',
                'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'pole' : $('#123').val()
                    },
                'success' : function(data){
                    document.getElementById('poisk').innerHTML = data
                }
        })
    })
}
)