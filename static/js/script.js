$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.dropdown-trigger').dropdown();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.datepicker').datepicker()
    $('input#input_text, textarea#textarea2').characterCounter();
  });


  function sendMail(contactForm) {
    emailjs
        .send("outlook", "milestone2", {
            from_name: contactForm.name.value,
            from_email: contactForm.emailaddress.value,
            package_type: contactForm.packagetype.value,
            package_request: contactForm.packagerequest.value,
        })
        .then(
            function (response) {
                alert("SUCCESS! We will get back to you ASAP", response);
            },
            function (error) {
                alert("FAILED! Sorry try sending again", error);
            }

        );
        document.form.reset();
        return false; 
};



  

  