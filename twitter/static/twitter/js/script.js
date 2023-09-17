// --------------------------remove html tags from users input----------------------------
// Get the textarea by its ID
var que_textarea = document.getElementById("question");

// Add an event listener for the input event on the textarea
que_textarea.addEventListener("input", function() {
    // Use a regular expression to check for HTML tags in the user's input
    this.value = this.value.trimStart();

    var pattern = /<[^>]+>/;
    if (pattern.test(this.value)) {
        // If HTML tags are found, remove them from the user's input
        this.value = this.value.replace('<', "").replace(">", "");
    }
});