var minlen = document.getElementById('min_length')
var minlenval = document.getElementById('min-val')
var maxlen = document.getElementById('max_length')
var maxlenval = document.getElementById('max-val')

minlen.addEventListener("input", function(){
    minlenval.innerHTML = minlen.value
})

maxlen.addEventListener("input", function(){
    maxlenval.innerHTML = maxlen.value
})

// --------------------------------COPY---------------------------------------
// Get the textarea and icon by their IDs
var summary_textarea = document.getElementById("summary");
var copyIcon = document.getElementById("copyIcon");
var summary_tooltip = document.getElementById("tooltip-summary");

// Add an event listener for the click event on the icon
copyIcon.addEventListener("click", async function() {
    try {
        if (summary_textarea.value===''){
            summary_tooltip.innerHTML = 'Kya karega khali text copy karke?'
            summary_tooltip.style.visibility = "visible";
        setTimeout(function() {
        tooltip.style.visibility = "hidden";
        }, 3000);
        }
        else{
        await navigator.clipboard.writeText(summary_textarea.value);
        summary_tooltip.style.visibility = "visible";
        setTimeout(function() {
        summary_tooltip.style.visibility = "hidden";
        }, 3000);
    }
    } catch (err) {
        console.error("Failed to copy text: ", err);
    }
});

// --------------------------remove html tags from users input----------------------------
// Get the textarea by its ID
var raw_textarea = document.getElementById("text");

// Add an event listener for the input event on the textarea
raw_textarea.addEventListener("input", function() {
    // Use a regular expression to check for HTML tags in the user's input
    var pattern = /<[^>]+>/;
    if (pattern.test(this.value)) {
        // If HTML tags are found, remove them from the user's input
        this.value = this.value.replace(pattern, "");
    }
});


// ------------------------AFTER SUBMITTING THE FORM------------------------------------------

var submit_button = document.getElementById("submit")

submit_button.addEventListener("click", async function(){
    let language = document.getElementById('language')
    if (language.value =='hindi'){
        var decorated_text = 'Badi summary matlab jyada time. Thodasa wait karo. Waise bhi jyada jaldbaji achhi nahi hoti.'
    }
    else if (language.value == 'marathi'){
        var decorated_text = 'Mothi summary mhanje jast vel ghenarach. Thoda vel thamba. Tasahi ati ghai bari nahi.'
    }
    else{
        var decorated_text = "Large summaries take more time. Wait for a while. Rushing is never good."
    }
    summary_textarea.innerHTML = ''
    for (let i = 0; i < decorated_text.length; i++) {
        setTimeout(() => {
            summary_textarea.innerHTML= decorated_text.slice(0, i+1);
        }, 80 * i);
      }
})

// ----------------------CLEAR TEXT------------------------------

var clear_element = document.getElementById('clear')
var clear_tooltip = document.getElementById('tooltip-clear')

clear_element.addEventListener("click", async function(){
    try {
    if (raw_textarea.value ==  ''){
        clear_tooltip.innerHTML = 'Kitna clear karega bhai?'
        clear_tooltip.style.visibility = "visible";
        setTimeout(function() {
        clear_tooltip.style.visibility = "hidden";
        }, 3000);
    }
    raw_textarea.innerHTML = '';
    summary_textarea.innerHTML = '';
} catch(err) {
    console.log('Error occured while clearing text.')
}
})