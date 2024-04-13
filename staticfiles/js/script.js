function atraso(callback) {
  setTimeout(callback, 300000);
}

function atualizando() {
  window.location.reload()
}

atraso(atualizando);