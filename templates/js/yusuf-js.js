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

  $("#tombolsubmit").fadeTo(0, 0.2);
  $("#tombolsubmit").prop("disabled", true);

  $(".alerts").children().hide();

  //setup before functions
  var timerketik;                //timer identifier
  var waktuketik = 200;
  var $input = $(":input");

  //on keyup, start the countdown
  $input.on('keyup', function () {
    clearTimeout(timerketik);
    timerketik = setTimeout(selesaiketik, waktuketik);
  });

  //on keydown, clear the countdown
  $input.on('keydown', function () {
    clearTimeout(timerketik);
  });

  //user is "finished typing," do something
  function selesaiketik () {
    $.ajax({
      method : "POST",
      url : "/cek_email/",
      data : {email:$("#id_email").val()},
      dataType : "json",
      success : function (datajson) {
        var terdaftar = datajson.email_is_taken;
        console.log(terdaftar);
        var nama_cek = $("#id_nama").val().length > 0;
        var email_cek = $("#id_email").val().length > 0;
        var pass_cek = $("#id_password").val().length > 0;
        var valid = nama_cek && email_cek && pass_cek;
        // if (terdaftar || !valid) {
        //   if (terdaftar) {
        //     // alert('Email sudah terdaftar.')
        //     $("#emailterdaftar").slideDown();
        //   }
        //   $("#tombolsubmit").fadeTo(600, 0.2);
        //   $("#tombolsubmit").prop("disabled", true);
        // } else if (email_cek.length != 0 && valid) {
        //   $("#emailterdaftar").slideUp();
        //   $("#tombolsubmit").fadeTo(600, 1);
        //   $("#tombolsubmit").prop("disabled", false);
        // }
        if (terdaftar) {
          $("#emailterdaftar").slideDown();
        } else {
          $("#emailterdaftar").slideUp();
        }

        if (valid && !terdaftar) {
          $("#tombolsubmit").fadeTo(600, 1);
          $("#tombolsubmit").prop("disabled", false);
        } else {
          $("#tombolsubmit").fadeTo(600, 0.2);
          $("#tombolsubmit").prop("disabled", true);
        }
      },

      error: function (error) {
        console.log("Data JSON tidak berhasil diakses");
      },
    });
  };

  $("#tombolsubmit").click(function(){
    $.ajax({
      method : "POST",
      data : $('form').serialize(),
      success : function (datajson) {
        // alert("Data berhasil tersimpan!")
        $("#simpansub").slideDown();
        $("#tombolsubmit").fadeTo(0, 0.2);
        $("#tombolsubmit").prop("disabled", true);
        window.setTimeout(function() {
            $("#simpansub").slideUp();
          }, 3000);
      },
      error: function (error) {
      },
    });
  });

  $.ajax({
    url : "/sub_json/",
    dataType : "json",
    success : function (datajson) {
      var dataSubs = datajson.subscribers;
      for (var i = 0; i < dataSubs.length; i++) {
        var info = dataSubs[i];
        var nama = info.nama;
        var email = info.email;
        var email_id = email.replace(/[^\w\s!?]/g,'');
        console.log(email_id);
        var baristabel = '<tr id = "baris' + email_id + '">' +
          "<th scope=\"row\">" + nama + "</th>" +
          "<td>" + email + "</td>" +
          "<td>" +
            '<button type="button" class="btn btn-danger yusuf-isi-button2 border-0 unsub" id = "' + email + '">' +
            '<span class="yusuf-bold">UNSUBSCRIBE</span>' +
            '</button>' +
          "</td>" +
        "</tr>";
        $('#isijson').append(baristabel);
      };
    },

    error: function (error) {
      var baristabel = "<tr><td colspan=\"3\" class = \"text-center\">JSON gagal di-load :(</td></tr>";
      $('#isijson').append(baristabel);
    },
  });

  $(document).on('click', '.unsub', function(){
    var id = $(this).attr('id');
    var idbersih = id.replace(/[^\w\s!?]/g,'');
    $("#baris" + idbersih).remove();
    $.ajax({
      method : "POST",
      url : "/hapus_sub/",
      data : {email:id},
      dataType : "json",
    });
  });

  //Ganti tema
  $("#ubah_tema").click(function(){
    if ($("#style_tema").prop("disabled")) {
      $("#style_tema").prop("disabled", false);
    } else {
      $("#style_tema").prop("disabled", true);
    }
  });

  //Smooth scrolling
  $('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
  // On-page links
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '')
      &&
      location.hostname == this.hostname
    ) {
        // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000, function() {
          // Callback after animation
          // Must change focus!
          var $target = $(target);
          $target.focus();
          if ($target.is(":focus")) { // Checking if the target was focused
            return false;
          } else {
            $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
            $target.focus(); // Set focus again
          };
        });
      }
    }
  });
});
