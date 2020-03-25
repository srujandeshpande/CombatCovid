fetch("https://combat-covid-v1.herokuapp.com/api/add_new_user_qma", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    first_name: "rabindranath",
    last_name: "tagore",
    dob: "1-12-2005",
    currently_under_quarantine: "False",
    date_time_quarantined: "NULL",
    date_time_unquarantined: "NULL",
    phone_number: "1001001001",
    email_address: "test@email.com",
    home_coordinates: "-40,80",
    address: "Thubarahalli",
    city: "Bengaluru",
    state: "Karnataka",
    pincode: "560066"
  })
}).then(res => {
  if (res.success) console.log("SUCCESS!");
  console.log(res);
});
