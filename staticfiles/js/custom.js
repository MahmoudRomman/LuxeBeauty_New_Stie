// owl carousel 

$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 6
        }
    }
})



// Script to prevent the user to back to the website content after he logged out...
history.pushState(null, null, location.href);
window.onpopstate = function () {
    history.go(1);
};








// document.addEventListener("DOMContentLoaded", function() {
//     // Check if the user is authenticated using Django's template variable
//     if (request.user.is_authenticated){
//         var isAuthenticated = "true";
//     } else {
//         var isAuthenticated = "false";
//     }

//     // Redirect to the home page if the user is already authenticated
//     if (isAuthenticated) {
//         // Replace the current history entry with the home page
//         history.replaceState(null, null, '/home');
//     }
// });

