
// Jquery functions for page interactivity //

$(document).ready(function(){
    $(".sidenav").sidenav();
    $(".dropdown-trigger").dropdown();
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $("select").formSelect();
    $(".datepicker").datepicker();
    $("input#input_text, textarea#textarea2").characterCounter();
  });


// Email JS function for contact form //

  function sendMail(contactForm) {
    emailjs
        .send("outlook", "Milestone_3", {
            from_name: contactForm.name.value,
            role: contactForm.role.value,
            from_email: contactForm.from_email.value,
            help_request: contactForm.help_request.value
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
}

  

  