document.getElementById('copy-btn').addEventListener('click', function() {

    const emailText = document.getElementById('my-email').innerText;

    navigator.clipboard.writeText(emailText).then(() => {
    
        const toast = document.getElementById('copy-toast');
        toast.classList.add('show');
        
        setTimeout(() => {
            toast.classList.remove('show');
        }, 2000);
    }).catch(err => {
        console.error('Error al copiar el correo: ', err);
    });
});