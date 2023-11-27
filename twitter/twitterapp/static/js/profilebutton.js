$(function(){
    $('#follow').click(function(){
        var button = $(this)
        $.ajax(button.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'follow': 'follow'
            },
            'success': function(data){
                if(data['key'] == 'unfollowed'){
                    document.getElementById('follow').innerHTML = 'follow'
                }
                else{document.getElementById('follow').innerHTML = 'unfollow'}
            }
        })
    })
})
$(function(){
    $('#like').click(function(){
        var button = $(this)
        $.ajax(button.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'like': 'like'
            },
            'success': function(data){
                document.getElementById('kollike').innerHTML = data['kol']
                if(data['like'] == 0){
                    document.getElementById('like').innerHTML = 'like'
                }
                else{document.getElementById('like').innerHTML = 'dislike'}
            }
        })
    })
})