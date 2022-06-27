function confirmDelete(codigo){
    Swal.fire({
        title: 'Estas seguro??',
        text: "No se pude deshacer la accion!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!'
      }).then((result) => {
        if (result.value) {
          Swal.fire(
            'Eliminado!',
            'Producto eliminado.',
            'success'
          ).then(function(){
            window.location.href = "/eliminar/" + codigo + "/";
          })
        }
      })
}

function confirmDelete2(codigo_carrito){
  Swal.fire({
      title: 'Estas seguro??',
      text: "No se pude deshacer la accion!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, Eliminar!'
    }).then((result) => {
      if (result.value) {
        Swal.fire(
          'Eliminado!',
          'Producto eliminado.',
          'success'
        ).then(function(){
          window.location.href = "/eliminar2/" + codigo_carrito + "/";
        })
      }
    })
}