<script>
  import {Link} from "svelte-navigator";
  import {BASE_URL} from "../config";
  let orderList=[];
  let keyword = "";
  let token = localStorage.getItem('token');

  function getOrderList() {
    let url = BASE_URL + '/api/search-order?keyword=' + keyword;
    //alert(url);
    let options = {
      headers: {Authorization: "Bearer " + token}
    }
    fetch(url, options).then(resp => resp.json()).then(result => {
      orderList = result;
      console.log(orderList);
    });
  }

  getOrderList();
</script>

<div class="container mt-3">
  <form class="row">
    <div class="col-9">
      <input class="form-control" placeholder="Tìm kiếm theo tên/sđt khách hàng/tên sản phẩm" />
    </div>
    <div class="col-3">
      <button class="btn btn-primary">Tìm kiếm</button>
    </div>
  </form>
  <table class="table mt-3">
    <thead>
      <tr>
        <th style="width:25%">Khách hàng</th>
        <th style="width:25%">Sản phẩm</th>
        <th style="width:20%">Ngày mua</th>
        <th style="width:20%">Trạng thái</th>
        <th style="width:10%"></th>
      </tr>
    </thead>
    <tbody>
      {#each orderList as order}
        <tr>
        <td>{order.customer_name} ({order.customer_phone})</td>
        <td>{order.product_name} (Số lượng: {order.qty})</td>
        <td>{order.order_date}</td>
        <td>
          {order.status == 0 ? 'Đang chờ giao hàng': ''}
          {order.status == 1 ? 'Đã nhận hàng': ''}
          {order.status == 2 ? 'Đã hủy': ''}
        </td>
        <td>
          <Link class="btn btn-sm btn-secondary" to={"/order-detail/" + order.id}>Xem</Link>
        </td>
      </tr>
      {/each}
    </tbody>
  </table>
  <nav aria-label="Page navigation example">
    <ul class="pagination">
      <li class="page-item"><a class="page-link" href="#/">&laquo;</a></li>
      <li class="page-item"><a class="page-link" href="#/">&lsaquo;</a></li>
      <li class="page-item"><a class="page-link" href="#/">&rsaquo;</a></li>
      <li class="page-item"><a class="page-link" href="#/">&raquo;</a></li>
    </ul>
    <span>Hiển thị 1-10 trên tổng số 25 đơn hàng</span>
  </nav>
</div>