function utilizouHoraExtra(id){
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-he/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        sucess: function(result){
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });

}

function naoutilizouHoraExtra(id){
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/naoutilizou-he/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        sucess: function(result){
            $("#horas_atualizadas").text(result.horas);
        }
    });

}
