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
                    document.getElementById('follow').innerHTML = '<b>Follow</b>'
                    document.getElementById('follow').className = "follow my-3 mx-4"
                }
                else{document.getElementById('follow').innerHTML = '<b>Unfollow</b>'
                document.getElementById('follow').className = "settings my-3 mx-4"}
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
                if(data['like'] == 1){
                        document.getElementById('like').src = '/static/images/like.png'
                    }else{document.getElementById('like').src = '/static/images/dislike.png'
                    }
            }
        })
    })
})