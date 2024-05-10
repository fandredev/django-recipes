function myScope() {
    // your code here
    const forms = document.querySelectorAll('.form-delete');

    for(const form of forms) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            const confirmation = confirm('Tem certeza que deseja deletar?');

            if(confirmation) {
                form.submit()
            }
        });
    }
}

myScope();