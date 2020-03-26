function new_admin() {
  form_div = document.getElementById('form_add_ema_user')
  form_div.style.visibility='visible'
  role = document.getElementById('new_ema_role')
  role.setAttribute(value,"admin")
  chc = document.getElementById('new_ema_chc')
  chc.style.visibility='hidden'
  phc = document.getElementById('new_ema_phc')
  phc.style.visibility='hidden'
}
