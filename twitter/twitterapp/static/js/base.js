


function base(){
    $('#open').click(function(){
        document.getElementById('input').show()
        document.getElementById('color').inert=true
    })
}
function close(){
    $('#close').click(function(){
        document.getElementById('input').close()
        document.getElementById('color').inert=false
    })
}
function button(){
    $('#button').click(function(){
        var data = new FormData()
        data.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val())
        data.append('text',$('#text').val())
        data.append('image', document.getElementById('image').files[0])
        $.ajax('/postCreate/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': data,
            'processData': false,
            'contentType': false,
            'success': function(data){
                document.getElementById('input').close()
                alert('post created')
            }
        })
    })
}
$(document).ready(function(){
    base()
    close()
    button()
    $('#galereya').on('click', function(i){
        i.preventDefault()
        $('#image').trigger('click')
    })
})