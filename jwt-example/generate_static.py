import os

base_dir = r"d:\BT10\jwt-example\src\main\resources"

# create directories
os.makedirs(os.path.join(base_dir, "templates"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "static", "js"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "static", "images"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "static", "css"), exist_ok=True)

with open(os.path.join(base_dir, "templates", "login.html"), "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="utf-8">
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65"
          crossorigin="anonymous">
</head>
<body>
<div class="container" style="min-height: 500px">
    <form action="" method="post">
        <label>Email</label>
        <input type="email" name="email" id="email" required="required">
        <label>Password</label>
        <input type="password" name="password" id="password" required="required" autocomplete="on">
        <button id="Login" type="button">Login</button>
    </form>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.min.js"></script>
<script src="/js/mainjs.js"></script>
</body>
</html>
""")

with open(os.path.join(base_dir, "templates", "profile.html"), "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Spring Boot REST API with AJAX</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<body>
<div class="container" style="min-height: 500px">
    <div class="starter-template">
        <h1>Spring Boot REST API with AJAX Example</h1>
        <img id="images" src="" alt="" width="100">
        <div id="profile"></div>
        <button id="logout">Logout</button>
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.min.js"></script>
<script src="/js/mainjs.js"></script>
</body>
</html>
""")

with open(os.path.join(base_dir, "static", "js", "mainjs.js"), "w", encoding="utf-8") as f:
    f.write("""$(document).ready(function() {
    // Hiển thị thông tin người dùng đăng nhập thành công
    $.ajax({
        type: 'GET',
        url: '/users/me',
        dataType: 'json',
        contentType: "application/json; charset=utf-8",
        beforeSend: function(xhr) {
            if (localStorage.token) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + localStorage.token);
            }
        },
        success: function(data) {
            var json = JSON.stringify(data, null, 4);
            // $('#profile').html(json);
            $('#profile').html(data.fullName);
            $('#images').html(document.getElementById("images").src = data.images);
            // console.log("SUCCESS : ", data);
            // alert('Hello ' + data.email + '! You have successfully accessed to /api/profile.');
        },
        error: function() {
            // var json = e.responseText;
            // $('#feedback').html(json);
            // console.log("ERROR : ", e);
            alert("Sorry, you are not logged in.");
        }
    });

    // Hàm login
    $('#Login').click(function() {
        var email = document.getElementById('email').value;
        var password = document.getElementById('password').value;
        var basicInfo = JSON.stringify({
            email: email,
            password: password
        });
        $.ajax({
            type: "POST",
            url: "/auth/login",
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            data: basicInfo,
            success: function(data) {
                localStorage.token = data.token;
                // alert('Got a token from the server! Token: ' + data.token);
                window.location.href = "/user/profile";
            },
            error: function() {
                alert("Login Failed");
            }
        });
    });
    
    // Hàm đăng xuất
    $('#logout').click(function() {
        localStorage.clear();
        window.location.href = "/login";
    });
});
""")
