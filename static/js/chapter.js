function copyCode(button) {
    // Find the code element
    var codeBlock = button.nextElementSibling.querySelector('code');
    // Create a range object
    var range = document.createRange();
    range.selectNode(codeBlock);
    // Select the text
    window.getSelection().removeAllRanges(); // Clear current selection
    window.getSelection().addRange(range); // Select the text
    // Copy the text to clipboard
    try {
        document.execCommand('copy');
        alert('Code copied to clipboard!');
    } catch (err) {
        console.log('Failed to copy code', err);
    }
    window.getSelection().removeAllRanges(); // Deselect text
}

// JavaScript for searching chapters
document.getElementById('chapterSearch').addEventListener('keyup', function() {
    var filter = this.value.toLowerCase();
    var chapters = document.getElementById('chapterList').getElementsByTagName('li');
    for (var i = 0; i < chapters.length; i++) {
        var a = chapters[i].getElementsByTagName('a')[0];
        var textValue = a.textContent || a.innerText;
        if (textValue.toLowerCase().indexOf(filter) > -1) {
            chapters[i].style.display = "";
        } else {
            chapters[i].style.display = "none";
        }
    }
});