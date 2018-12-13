$(document).ready(function(){

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  //coba cari tahu, mengapa kita perlu mengambil csrftoken dari cookie
  var csrftoken = getCookie('csrftoken');
  //token yang ada di variable csrftoken kalian masukan dipassing ke dalam fungsi xhr.setRequestHeader("X-CSRFToken", csrftoken);
  //coba cari tahu, kenapa kita perlu mensetup csrf token terlebih dahulu sebelum melakukan request post ke views django

  //yang disarankan dari dokumentasi django nya
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

	$("#showFormFlag").children().hide();
  
	$("#ask-form").click(function(){
		$("#ask-form").slideUp();
		$("#form-testimoni").slideDown();
			// $("#id_nama").html("");
	});
	$("#ask-form-unlogged").click(function(){
		$("#ask-form-unlogged").slideUp();
		$("#not-loggedIn-alert").slideDown();
			// $("#id_nama").html("");
	});

  $("#testimoni_submit").click( function() {
    var komentar = $("#id_komentar").val();
    $.ajax({
      method: "POST",
      url: "/about/tambah_komentar",
      data: {
        "komentar": komentar,
      },
      success: function(data) {
        console.log("success");
        location.reload()
      }
    })
    event.preventDefault();
  })
});