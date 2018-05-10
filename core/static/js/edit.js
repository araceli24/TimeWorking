$('#edit').click(function () {

    $('td').each(function () {
        var content = $(this).html();
        $(this).html('<textarea>' + content + '</textarea>');
    });
});

$('#save').click(function () {

    $('textarea').each(function () {
        var content = $(this).val();
        $(this).html(content);
        $(this).contents().unwrap();
      //  var newDescription = $(this).parent().children('.newDescription').val()
   
    // $.ajax({
    //     type: "PATCH",
    //     url: '/api/projects/'+content+'/',
    //     data: { description : newDescription },
    //     success: function (response){
    //   //      text(newDescription)
    //     }
    // });
    });

});