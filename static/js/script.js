/**
 * Created by dkeyson on 19/02/2017.
 */
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
function submitForm(){
    var form = $("#myform");
    var url = form.attr("action");
    var formData = {};
    $("form").find("input[name]").each(function (index, node) {
        formData[node.name] = node.value;
        node.value="";
    });
    $.ajax({
    url: "/new-post",
    type: "POST",
    data: formData,
    cache:false
    // dataType: "json",
  
    }).done(function(data){
        console.log("test");
        var newPost = $("<div>").html(data);
        console.log(newPost);
       $("#next-posts").append(newPost);
       newPost.slideDown();
    });
}

$(document).ready(function(){
    $(".add").click(function(){
        $("form").slideDown();
        $(".button.add").hide();
        $(".next-buttons").show();
    });

    $(".save").click(submitForm);
    $(".add.top-menu").click(function(){
        console.log('clicked');
        var n = $(document).height();
         $('html, body').animate({ scrollTop: n }, 500);
         $(".add ");
    });
    // $(".post-comment").click(function(){
    //     setTimeout(function(){
    //         $(".new_comment_form input").val('');
    //     },100)
        
    // });
});

