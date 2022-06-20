<script>
  import { Router, Route, Link } from "svelte-navigator";
  import Login from "./pages/Login.svelte";
  import OrderList from "./pages/OrderList.svelte";
  import OrderDetail from "./pages/OrderDetail.svelte";

  let token =  localStorage.getItem('token');

  function logOut() {
    localStorage.removeItem('token');
    location.href = '/';
  }
</script>

{#if token}
  <Router>
    <header>
      <nav class="navbar navbar-expand-lg navbar-dark bg-primary p-0">
        <div class="navbar-nav collapse navbar-collapse">
          <a class="nav-item nav-link active" href="/">Quản lý đơn hàng</a>
          <a class="nav-item nav-link" href="#/">Quản lý sản phẩm</a>
        </div>
      
        <ul class="navbar-nav ml-auto">
          <li class="nav-item no-arrow">
            <a class="nav-link dropdown-toggle p-0" data-bs-toggle="dropdown" href="void(0)">
              <img alt="" class="rounded-circle" style="width:60px"
                src="https://raw.githubusercontent.com/pytutorial/html_samples/master/css_bootstrap/user.svg" />
            </a>
            <div class="dropdown-menu dropdown-menu-end">
              <a class="dropdown-item" href="#/">
                Thông tin tài khoản
              </a>
              <div class="dropdown-divider"></div>
              <a on:click={logOut} class="dropdown-item" href="#/">
                Đăng xuất
              </a>
            </div>
          </li>
        </ul>
      </nav>
    </header>
    <main>
      <Route path="/" component={OrderList} />
      <Route path="/order-detail/:id" component={OrderDetail} />
    </main>
  </Router>
{:else}
  <Login/>
{/if}

