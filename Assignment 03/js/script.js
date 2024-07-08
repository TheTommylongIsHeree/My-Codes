function check_email() {
 var info = document.getElementById('the_info_itself');
 var form = document.getElementById('the_form');
 var textbox = document.getElementById('email_textbox').value;
 const regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
 var reg = new RegExp(regex);
 if (reg.test(textbox)) {
  info.style.display = "block";
  form.style.display = "none";
 }
 else {
  alert("Email không hợp lệ")
 }
}

function jobs_hideandshow() {
 var elementid = "jobs"
 var element = document.getElementById(elementid);
 var button = document.getElementById(elementid+"_button");
 if (element.style.display === "none") {
   element.style.display = "block";
   button.innerHTML = "View Less";
 } else {
   element.style.display = "none";
   button.innerHTML = "View More";
 }
}

function learning_hideandshow() {
 var elementid = "learning"
 var element = document.getElementById(elementid);
 var button = document.getElementById(elementid+"_button");
 if (element.style.display === "none") {
   element.style.display = "block";
   button.innerHTML = "View Less";
 } else {
   element.style.display = "none";
   button.innerHTML = "View More";
 }
}

function activity_hideandshow() {
 var elementid = "activity"
 var element = document.getElementById(elementid);
 var button = document.getElementById(elementid+"_button");
 if (element.style.display === "none") {
   element.style.display = "block";
   button.innerHTML = "View Less";
 } else {
   element.style.display = "none";
   button.innerHTML = "View More";
 }
}

function hobbies_hideandshow() {
 var elementid = "hobbies"
 var element = document.getElementById(elementid);
 var button = document.getElementById(elementid+"_button");
 if (element.style.display === "none") {
   element.style.display = "block";
   button.innerHTML = "View Less";
 } else {
   element.style.display = "none";
   button.innerHTML = "View More";
 }
}

function languages_hideandshow() {
 var elementid = "languages"
 var element = document.getElementById(elementid);
 var button = document.getElementById(elementid+"_button");
 if (element.style.display === "none") {
   element.style.display = "block";
   button.innerHTML = "View Less";
 } else {
   element.style.display = "none";
   button.innerHTML = "View More";
 }
}

function skills_hideandshow() {
 var elementid = "skills"
 var element = document.getElementById(elementid);
 var button = document.getElementById(elementid+"_button");
 if (element.style.display === "none") {
   element.style.display = "block";
   button.innerHTML = "View Less";
 } else {
   element.style.display = "none";
   button.innerHTML = "View More";
 }
}



