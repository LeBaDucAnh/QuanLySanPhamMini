<script>
  import {BASE_URL} from '../config';
  import {Link, navigate} from "svelte-navigator";
  export let id;
  let order = {};
  let url = BASE_URL + '/api/get-order-by-id/' + id;
  let token = localStorage.getItem('token');
  let options = {
    headers: {Authorization: "Bearer " + token}
  };
  fetch(url, options).then(resp => resp.json()).then(result => {
    order = result;
    console.log(order);
  });

  function confirmOrder() {
    if(confirm('Xác nhận hàng đã được giao?')){
      let url = BASE_URL + '/api/confirm-order/' + id;
      fetch(url,{...options, method: 'POST'}).then(_ => navigate('/'));
    }
  }

  function cancelOrder() {
    if(confirm('Hủy đơn hàng này?')){
      let url = BASE_URL + '/api/cancel-order/' + id;
      fetch(url,{...options, method: 'POST'}).then(_ => navigate('/'));
    }
  }

</script>
<div class="container mt-3">
  <h4>Thông tin đơn hàng</h4>
  <hr />
  <table class="table table-form">
    <tbody>
      <tr>
        <th colspan="2">
          <h5>Thông tin khách hàng</h5>
        </th>
      </tr>
      <tr>
        <th style="width:30%">Họ và tên:</th>
        <td>{order.customer_name}</td>
      </tr>
      <tr>
        <th>Số điện thoại:</th>
        <td>{order.customer_phone}</td>
      </tr>
      <tr>
        <th>Địa chỉ:</th>
        <td>{order.customer_address}</td>
      </tr>
      <tr>
        <th colspan="2">
          <h5>Thông tin sản phẩm</h5>
        </th>
      </tr>
      <tr>
        <th>Tên sản phẩm:</th>
        <td>{order.product_name}</td>
      </tr>
      <tr>
        <th>Đơn giá:</th>
        <td>{order.price_unit} ₫</td>
      </tr>
      <tr>
        <th>Số lượng:</th>
        <td>
          {order.qty}
        </td>
      </tr>
      <tr>
        <th>
          <h5>Trạng thái đơn hàng:</h5>
        </th>
        <td>
          {order.status == 0 ? 'Đang chờ giao hàng': ''}
          {order.status == 1 ? 'Đã nhận hàng': ''}
          {order.status == 2 ? 'Đã hủy': ''}
        </td>
      </tr>
    </tbody>
  </table>
  <div>
    <Link class="btn btn-secondary" to="/">Quay lại</Link>
    {#if order.status == 0}
      <button on:click={confirmOrder} class="btn btn-primary">Xác nhận đã giao</button>
      <button on:click={cancelOrder} class="btn btn-danger">Huỷ đơn hàng</button>
    {/if}
  </div>
</div>