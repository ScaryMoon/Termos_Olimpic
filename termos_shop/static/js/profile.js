function updateProfile() {

    const csrfToken =
        document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/api/me/', {
        method: 'PATCH',

        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },

        body: JSON.stringify({
            phone: '111111111'
        })
    })
    .then(response => {

        if (response.status === 401) {
            alert('Необходимо войти');
            return;
        }

        if (response.status === 403) {
            alert('Недостаточно прав');
            return;
        }

        return response.json();
    })
    .then(data => {
        console.log(data);
        alert('Профиль обновлён');
    });
}