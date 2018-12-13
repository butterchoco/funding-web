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
	
	// to hide testimonials form if user is not authenticated yet
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
	
	
	// to load the testimonies
	$("#submitButton").click(function(){
    $.ajax({
      method : "POST",
      data : $('form').serialize(),
      success : function (datajson) {
		$("#form-testimoni").slideUp();
		
        $("#successAlert").slideDown();
        window.setTimeout(function() {
            $("#successAlert").slideUp();
        }, 3000);
		
		$("#ask-form").slideDown();
		$("#id_nama").html("");
		$("#testimoni").html("");
      },
    });
  });

  $.ajax({
    url : "testi_json",
    dataType : "json",
    success : function (datajson) {
      var dataSubs = datajson.testimonies;
      for (var i = 0; i < dataSubs.length; i++) {
        var info = dataSubs[i];
        var nama = info.nama;
        var testimoni = info.komentar;
        var barisTesti = '<h4 class="text-center" style="color:black">' + nama + '</h4>' +
				'<div class="flex-content text-center"> <div> <p id="testiKomen">'testimoni'</p> </div> </div></div>';
        $('#testiKonten').append(barisTesti);
      };
    },
	error: function (error) {
      var baristabel = "<p class = \"text-center\">JSON gagal di-load :(</p>";
      $('#testiKonten').append(baristabel);
    },
  });
});