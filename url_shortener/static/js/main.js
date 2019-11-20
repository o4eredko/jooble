"use strict";

const XHR_STATE_READY = 4;
const HTTP_201_CREATED = 201;

let form = document.querySelector('.url-form');

if (form) {
	form.onsubmit = e => {
		e.preventDefault();

		document.querySelectorAll('.url-form label .alert').forEach(alert => {
			if (!alert.classList.contains('d-none')) {
				alert.classList.add('d-none')
			}
		});
		let xhr = new XMLHttpRequest();
		let data = new FormData(form);
		let form_success = document.querySelector('.alert-success');

		xhr.open('POST', `${window.origin}/api/links/`);
		xhr.send(data);
		xhr.onreadystatechange = () => {
			if (xhr.readyState !== XHR_STATE_READY)
				return;
			let response = JSON.parse(xhr.responseText);
			if (xhr.status === HTTP_201_CREATED) {
				form_success.classList.remove('d-none');
				form_success.innerHTML =
					"<span>Great, your url was created.</span>: " +
					`<a href='${response.short_url}'>${response.short_url}</a>`;
			} else {
				let keys = Object.keys(response);
				for (let i in keys) {
					let key = keys[i];
					let input = form[key];
					if (input) {
						let error = input.nextElementSibling;
						error.classList.remove('d-none');
						error.innerText = response[key];
					}
				}
			}
		}
	};
}