$(function(){
    $('#comentb').click(function(){
        var button = $(this)
        $.ajax(button.data('url'), {
        'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'id_text' : $('#id_text').val()
            },
            'success': function(data){
                document.getElementById('comments').innerHTML += data
            }
            }
        )}
        )})