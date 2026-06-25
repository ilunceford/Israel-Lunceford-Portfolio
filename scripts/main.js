const contactForm = document.querySelector("#contactForm");
const messageInput = document.querySelector("#message");
const characterCount = document.querySelector("#characterCount");
const formStatus = document.querySelector("#formStatus");

const fields = {
    name: document.querySelector("#name"),
    email: document.querySelector("#email"),
    reason: document.querySelector("#reason"),
    message: messageInput
};

const errors = {
    name: document.querySelector("#nameError"),
    email: document.querySelector("#emailError"),
    reason: document.querySelector("#reasonError"),
    message: document.querySelector("#messageError")
};

function updateCharacterCount() {
    if (!messageInput || !characterCount) {
        return;
    }

    const length = messageInput.value.trim().length;
    characterCount.textContent = `${length} character${length === 1 ? "" : "s"}`;
}

function setError(fieldName, message) {
    const field = fields[fieldName];
    const error = errors[fieldName];

    if (!field || !error) {
        return;
    }

    error.textContent = message;
    field.classList.toggle("input-error", Boolean(message));
}

function validateForm() {
    let isValid = true;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!fields.name.value.trim()) {
        setError("name", "Please enter your name.");
        isValid = false;
    } else {
        setError("name", "");
    }

    if (!emailPattern.test(fields.email.value.trim())) {
        setError("email", "Please enter a valid email address.");
        isValid = false;
    } else {
        setError("email", "");
    }

    if (!fields.reason.value) {
        setError("reason", "Please choose a reason.");
        isValid = false;
    } else {
        setError("reason", "");
    }

    if (fields.message.value.trim().length < 20) {
        setError("message", "Please write at least 20 characters.");
        isValid = false;
    } else {
        setError("message", "");
    }

    return isValid;
}

function createMailtoLink() {
    const subject = encodeURIComponent(`Portfolio Contact: ${fields.reason.value}`);
    const body = encodeURIComponent(
        `Name: ${fields.name.value.trim()}\n` +
        `Email: ${fields.email.value.trim()}\n` +
        `Reason: ${fields.reason.value}\n\n` +
        `${fields.message.value.trim()}`
    );

    return `mailto:?subject=${subject}&body=${body}`;
}

if (messageInput) {
    messageInput.addEventListener("input", updateCharacterCount);
    updateCharacterCount();
}

if (contactForm) {
    contactForm.addEventListener("submit", (event) => {
        event.preventDefault();

        if (!validateForm()) {
            formStatus.textContent = "Please fix the highlighted fields before creating the email draft.";
            formStatus.classList.add("status-error");
            return;
        }

        formStatus.textContent = "Opening your email app with the completed message.";
        formStatus.classList.remove("status-error");
        window.location.href = createMailtoLink();
        contactForm.reset();
        updateCharacterCount();
    });
}
