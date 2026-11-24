
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>A Little Invitation 💙</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    font-family: Georgia, serif;
    color: white;
    text-align: center;
    background: linear-gradient(135deg, #020817, #101b46, #29164d);
    overflow-x: hidden;
}

.star {
    position: fixed;
    color: #c7d8ff;
    animation: twinkle 2s infinite alternate;
    pointer-events: none;
}

@keyframes twinkle {
    from { opacity: .2; }
    to { opacity: 1; }
}

.container {
    width: 90%;
    max-width: 600px;
    margin: 65px auto;
    padding: 35px 22px;
    background: rgba(255,255,255,.08);
    border: 1px solid #a9c4ff55;
    border-radius: 25px;
    box-shadow: 0 0 35px #536dfe55;
}

h1 {
    color: #c7d8ff;
    font-size: 32px;
}

p {
    line-height: 1.8;
}

.subtitle {
    color: #d9dcff;
}

button {
    border: none;
    border-radius: 30px;
    padding: 14px 28px;
    margin: 12px;
    font-size: 16px;
    cursor: pointer;
    transition: .2s;
}

.yes {
    background: #a9c4ff;
    color: #07132f;
}

.yes:hover {
    transform: scale(1.08);
    box-shadow: 0 0 20px #a9c4ff;
}

.no {
    background: #e3e5f5;
    color: #222;
    position: relative;
}

#response {
    display: none;
    margin-top: 25px;
    padding: 20px;
    background: #ffffff12;
    border-radius: 18px;
    animation: appear .7s ease;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.letter {
    display: none;
    text-align: left;
    line-height: 1.8;
    padding: 20px;
    margin-top: 20px;
    background: #ffffff12;
    border-radius: 15px;
}

footer {
    margin-top: 35px;
    font-size: 13px;
    color: #aab8e8;
}

</style>
</head>

<body>

<div class="container">

    <div style="font-size:45px">🌙 💙 ✨</div>

    <h1>A Little Invitation</h1>

    <p class="subtitle">
        To: <b>Christian Raphael Paraiso Segui</b><br>
        From: <b>Xiannnn😛</b>
    </p>

    <h2>Will you go out with me? 💌</h2>

    <p class="subtitle">
        I have something special I want to ask you.
    </p>

    <div>
        <button class="yes" onclick="sayYes()">
            YES! 💙
        </button>

        <button class="no" id="noButton"
                onmouseenter="moveNo()"
                ontouchstart="moveNo()"
                onclick="moveNo()">
            NO
        </button>
    </div>

    <div id="response">
        <h2>YIPPEEEEE! YIPPEEEEE! 🎉💙</h2>
        <h3>FINALLY! I'VE BEEN WAITING FOR THIS!</h3>
        <p>
            You just made my day so much better.
            I can't believe you said YES! 🥹💙
        </p>
        <p>So... it's a date? 🌙</p>
    </div>

    <br>

    <button class="yes" onclick="showLetter()">
        Read my little letter 💌
    </button>

    <div class="letter" id="letter">

        <h3>Dear Christian, 💙</h3>

        <p>
        I don't really know where to begin, but I want
        to be honest about how I feel.
        </p>

        <p>
        I care about you more than I can easily explain.
        Even the little conversations, random moments,
        and simplest things about you have become special
        to me.
        </p>

        <p>
        I know you like someone else, and I respect that.
        I don't want this letter to make you feel guilty
        or pressured to choose me.
        </p>

        <p>
        I just wanted you to know that my feelings are
        genuine. You matter to me, and I'm grateful for
        the moments I've shared with you.
        </p>

        <p>
        Whatever your answer may be, I hope you find
        happiness. You deserve that.
        </p>

        <p>
        With lots of care,<br>
        <b>Xiannnn😛 💙</b>
        </p>

    </div>

    <footer>
        Made with care • A midnight-blue surprise ✨
    </footer>

</div>

<script>

function sayYes() {
    document.getElementById("response").style.display = "block";
    document.getElementById("noButton").style.display = "none";
}

function moveNo() {
    const button = document.getElementById("noButton");

    const maxX = Math.max(0, window.innerWidth - button.offsetWidth - 20);
    const maxY = Math.max(0, window.innerHeight - button.offsetHeight - 20);

    button.style.position = "fixed";
    button.style.left = Math.random() * maxX + "px";
    button.style.top = Math.random() * maxY + "px";
    button.style.zIndex = "999";
}

function showLetter() {
    const letter = document.getElementById("letter");

    letter.style.display =
        letter.style.display === "block" ? "none" : "block";
}

// Create decorative stars
for (let i = 0; i < 45; i++) {
    const star = document.createElement("div");
    star.className = "star";
    star.innerHTML = "✦";
    star.style.left = Math.random() * 100 + "vw";
    star.style.top = Math.random() * 100 + "vh";
    star.style.animationDelay = Math.random() * 2 + "s";
    document.body.appendChild(star);
}

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run()
