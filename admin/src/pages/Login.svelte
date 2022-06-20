<script>
  import {BASE_URL} from '../config';

  let username = '';
  let password = '';
  let error = '';

  async function logIn(e) {
    e.preventDefault();
    let data = {username, password};
    let options = {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {'Content-Type': 'application/json'}
    };
    let url = BASE_URL + '/api/token';
    alert(url);
    alert(JSON.stringify(data));
    let resp = await fetch(url, options);
    if(resp.status != 200) {
      error = 'Tên đăng nhập hay mật khẩu không đúng';
    }else {
      let result = await resp.json();
      localStorage.setItem('token', result.access);
      location.href = '/'; // reload
    }
  }
</script>

<div class="bg-login">
  <div class="login-form">
    <h3>Đăng nhập</h3>

    <form on:submit={logIn} method="POST" style="margin-top: 30px;">
      <div class="mt-3">
        <label for="username" class="mb-1">Tên tài khoản</label>
        <input name="username" type="text" class="form-control" 
          on:change={e => username = e.target.value}
        />
      </div>
      <div class="mt-4">
        <label for="password" class="mb-1">Mật khẩu</label>
        <input name="password" type="password" class="form-control" 
        on:change={e => password = e.target.value}
        />
      </div>
      <div class="mt-3">
        <span id="error" style="color:red">{error??''}</span>
      </div>
      <div style="margin-top: 35px;">
        <button type="submit" class="btn btn-primary" style="width: 100%;">Đăng nhập</button>
      </div>
    </form>
    <p class="text-center mt-4"><a href="#/">Đăng ký tài khoản</a></p>
  </div>
</div>

<style>
  .bg-login {
    position: relative;
    width: 100%;
    min-height: auto;
    background-position: right 0px top 0px;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    background-size: cover;
    -o-background-size: cover;
  }

  .login-form {
    border: 1px solid #DDD;
    max-width: 400px;
    padding: 20px;
    margin-top: 100px;
    margin-left: auto;
    margin-right: auto;
  }
</style>