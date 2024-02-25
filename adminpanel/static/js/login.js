$(document).ready(function() {
    $('#submitButton').click(function(event) {
        event.preventDefault(); // Prevent the default form submission behavior
        sendVerificationCode();
    });
    
    function sendVerificationCode() {
        var email = $('#email').val();
        var password = $('#password').val();
        showVerificationCodeInput();
        changeFormColor('#A4C3B2'); // Change the color of the form when clicked
    }

    function showVerificationCodeInput() {
        var form = $('.form');
        var loginForm = $('#loginForm');
        loginForm.attr('action','/send_verification')
        form.html(`
            <h1>Verification Code</h1>
            <div class="verification-form">
                <input type="text" placeholder="Verification Code" id="verificationCode" required>
                <button type="submit" id="verifyButton">Verify</button>
            </div>
        `);
      
        // Attach click event handler to the verify button
        // This line should be moved out of this function
        // $('#verifyButton').click(verifyCode);
    }

    // Move the event handler attachment here
    // This ensures that the #verifyButton exists in the DOM before attaching the event handler
    $(document).on('click', '#verifyButton', verifyCode);

    function verifyCode() {
        var verificationCode = $('#verificationCode').val();
        
        // Verify the code
        
        // Redirect to admin dashboard if successful
        // window.location.href = 'done.html';
    }

    function changeFormColor(color) {
        var form = $('.form');
        form.css('background-color', color);
    }
});