function new_admin() {
  form_div = document.getElementById('form_add_ema_user')
  form_div.style.visibility='visible'
  role = document.getElementById('new_ema_role')
  role.setAttribute("value","admin")
  chc = document.getElementById('new_ema_chc')
  chc.style.display='none'
  phc = document.getElementById('new_ema_phc')
  phc.style.display='none'
}
function new_chc() {
  form_div = document.getElementById('form_add_ema_user')
  form_div.style.visibility='visible'
  role = document.getElementById('new_ema_role')
  role.setAttribute("value","chc")
  chc = document.getElementById('new_ema_chc')
  chc.style.display='none'
  phc = document.getElementById('new_ema_phc')
  phc.style.display='none'
}
function new_phc() {
  form_div = document.getElementById('form_add_ema_user')
  form_div.style.visibility='visible'
  role = document.getElementById('new_ema_role')
  role.setAttribute("value","phc")
  chc = document.getElementById('new_ema_chc')
  chc.style.display='inline'
  phc = document.getElementById('new_ema_phc')
  phc.style.display='none'
}
function new_mo() {
  form_div = document.getElementById('form_add_ema_user')
  form_div.style.visibility='visible'
  role = document.getElementById('new_ema_role')
  role.setAttribute("value","mo")
  chc = document.getElementById('new_ema_chc')
  chc.style.display='inline'
  phc = document.getElementById('new_ema_phc')
  phc.style.display='inline'
}
