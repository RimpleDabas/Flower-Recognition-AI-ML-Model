/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imageResult')
                .attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

$(function () {
    $('#upload').on('change', function () {
        readURL(input);
    });
});

/*  ==========================================
    SHOW UPLOADED IMAGE NAME
* ========================================== */
var input = document.getElementById('upload');
var tryagain = document.getElementById('btn-tryagain');
var infoArea = document.getElementById('upload-label');

function showFileName(event) {
    var input = event.srcElement;
    var fileName = input.files[0].name;
    infoArea.textContent = 'File name: ' + fileName;
  }

if(tryagain) {
    $('#btn-tryagain').hide();
}

if(input) {
    input.addEventListener('change', showFileName);
}

$(function () {
    $('#btn-correct').on('click', function () {
        $('#img-thinking')
                .attr('src', "static/images/happy.png");
        $('#btn-correct').hide();
        $('#btn-incorrect').hide();
        $("#btn-tryagain").prop("value", "Yay!!! Want to try one more?");
        $('#btn-tryagain').show();
    });
});

$(function () {
    $('#btn-incorrect').on('click', function () {
        $('#img-thinking')
                .attr('src', "static/images/sad.png");
        $('#btn-correct').hide();
        $('#btn-incorrect').hide();
        $("#btn-tryagain").prop("value", "Sorry, I'm not trained enough yet.Let's Try another one!");
        $('#btn-tryagain').show();
    });
});

$(function () {
    $('#btn-tryagain').on('click', function () {
        $(location).attr('href', "/");
    });
});
