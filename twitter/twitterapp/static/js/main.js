$(function(){
    $(document).click(function(event){
        var click = $(event.target)
        if (click.attr('class') == 'buttonsImages ml-4'){
             $.ajax('/', {
                'type': 'POST',
                'async': true,
                'dataType': 'json',
                'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'key': click.attr('id')
                },
                'success' : function(data){
                    if(data['like'] == 1){
                        document.getElementById(click.attr('id')).src = '/static/images/like.png'
                    }else{document.getElementById(click.attr('id')).src = '/static/images/dislike.png'}
                    document.getElementById(`likes${click.attr('id')}`).innerHTML = data['kol']
                    }
                })
            }
        })
    })
