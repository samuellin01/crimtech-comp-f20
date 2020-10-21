// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
    "In a dark place we find ourselves, and a little more knowledge lights our way.",
    "Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
    "Always two there are, no more, no less. A master and an apprentice.",
    "In the end, cowards are those who follow the dark side."
];
let force_quotes = ["Luminous beings are we, not this crude matter.",
    "A Jedi uses the Force for knowledge and defense, never for attack.",
    "Clear your mind must be, if you are to find the villains behind this plot.",
    "The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
    "My ally is the Force, and a powerful ally it is."
];
let std_quotes = ["Patience you must have, my young padawan.",
    "When nine hundred years old you reach, look as good you will not.",
    "No! Try not! Do or do not, there is no try.",
    "Judge me by my size, do you?",
    "Difficult to see. Always in motion is the future."
];

function respond() {
    // Array of Yoda Pics
    var yodaPics = new Array("img/cute-dark.jpg", "img/cute-force.jpg", "img/cute-std.jpg", "img/regular-dark.jpg", "img/regular-force.jpg", "img/regular-std.jpg");
    // Textbox Input
    var textInput = document.getElementById("input").value;

    // Takes in textbox input and changes picture, caption accordingly.
    if (textInput.includes("cute") || textInput.includes("baby")) {
        if (textInput.includes("dark")) {
            document.getElementById("pic").setAttribute("src", yodaPics[0]);
            document.getElementById("caption").innerHTML = "Yes, h".concat("m".repeat(randomInteger(3, 10))).concat(".");
        } else if (textInput.includes("force")) {
            document.getElementById("pic").setAttribute("src", yodaPics[1]);
            document.getElementById("caption").innerHTML = "Yes, h".concat("m".repeat(randomInteger(3, 10))).concat(".");
        } else {
            document.getElementById("pic").setAttribute("src", yodaPics[2]);
            document.getElementById("caption").innerHTML = "Yes, h".concat("m".repeat(randomInteger(3, 10))).concat(".");
        }
    } else {
        if (textInput.includes("force") && textInput.includes("dark")) {
            document.getElementById("pic").setAttribute("src", yodaPics[3]);
            document.getElementById("caption").innerHTML = dark_quotes[randomInteger(0, dark_quotes.length - 1)];
        } else if (textInput.includes("force") || textInput.includes("dark")) {
            document.getElementById("pic").setAttribute("src", yodaPics[4]);
            document.getElementById("caption").innerHTML = force_quotes[randomInteger(0, force_quotes.length - 1)];
        } else {
            document.getElementById("pic").setAttribute("src", yodaPics[5]);
            document.getElementById("caption").innerHTML = std_quotes[randomInteger(0, std_quotes.length - 1)];
        }
    }

    // Console log shenanigans
    console.log(document.getElementById("input").value)
    console.log("Hello World!");

    // Clears the textbox when button pressed
    document.getElementById("input").value = "";
}

// Returns an integer random number between min (included) and max (included)
function randomInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}