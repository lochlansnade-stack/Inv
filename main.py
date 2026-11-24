
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>A Midnight Letter 💙</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    min-height: 100vh;
    font-family: Arial, sans-serif;
    color: white;
    text-align: center;
    background: linear-gradient(135deg,#020617,#080F32,#191970);
    background-size: 300% 300%;
    animation: night 12s infinite alternate;
    overflow-x: hidden;
}

@keyframes night {
    to { background-position: 100% 100%; }
}

.stars {
    position: fixed;
    inset: 0;
    pointer-events: none;
    background-image: radial-gradient(white 1px,transparent 1px);
    background-size: 55px 55px;
    opacity: .4;
}

.container {
    position: relative;
    z-index: 2;
    width: 92%;
    max-width: 450px;
    margin: 35px auto;
}

.card {
    background: #101b43ed;
    border: 1px solid #8daaff88;
    border-radius: 25px;
    padding: 25px 18px;
    margin-bottom: 22px;
    box-shadow: 0 0 25px #4169e155;
    animation: appear 1s ease;
}

@keyframes appear {
    from {opacity:0; transform:translateY(20px);}
    to {opacity:1; transform:translateY(0);}
}

h1 { color: #dce8ff; text-shadow: 0 0 15px #829dff; }
h2 { color: #bcd0ff; }

.moon {
    font-size: 55px;
    animation: float 3s infinite ease-in-out;
}

@keyframes float {
    50% { transform: translateY(-9px); }
}

.names {
    color: #c5d5ff;
    line-height: 1.9;
}

button {
    border: none;
    border-radius: 25px;
    padding: 13px 20px;
    margin: 7px;
    font-weight: bold;
    font-size: 15px;
    cursor: pointer;
}

.primary {
    background: linear-gradient(135deg,#527bff,#b16bff);
    color: white;
    box-shadow: 0 0 15px #668bff;
}

.secondary {
    background: #e5e9f5;
    color: #172044;
}

.gallery {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}

.photo {
    background: #24345e;
    border: 1px solid #829dff88;
    border-radius: 15px;
    overflow: hidden;
    min-height: 140px;
}

.photo img {
    width: 100%;
    height: 155px;
    object-fit: cover;
    display: block;
}

.photo p {
    font-size: 12px;
    color: #dce8ff;
    padding: 5px;
}

.letter {
    display: none;
    text-align: left;
    background: #17234f;
    padding: 20px;
    border-radius: 17px;
    color: #e1e9ff;
    line-height: 1.8;
    margin-top: 15px;
    animation: appear .7s;
}

#message {
    color: #ffd7f0;
    font-weight: bold;
    line-height: 1.6;
    margin-top: 20px;
}

.float {
    position: fixed;
    bottom: -30px;
    pointer-events: none;
    animation: rise 6s linear forwards;
}

@keyframes rise {
    to { transform: translateY(-110vh) rotate(360deg); opacity:0; }
}

footer {
    color: #9caed8;
    font-size: 11px;
    padding: 20px;
}
</style>
</head>

<body>
<div class="stars"></div>

<div class="container">

    <section class="card">
        <div class="moon">🌙💙</div>

        <p class="names">
            ✦ A SPECIAL INVITATION ✦<br>
            To: <b>Christian Raphael Paraiso Segui</b><br>
            From: <b>Xiannnn😛</b>
        </p>

        <h1>Will you go out with me?</h1>
        <p>Under a thousand stars, I have one question for you. ✨</p>

        <button class="primary" onclick="sayYes()">YES 💗</button>
        <button class="secondary" id="no" onpointerenter="tryNo()">NO 😭</button>

        <div id="message"></div>
    </section>

    <section class="card">
        <h2>Our Little Gallery 📸</h2>
        <p>Some pictures I'd love to keep close.</p>

        <div class="gallery">
            <div class="photo">
                <img src="/static/photo1.jpg" alt="Memory one"
                     onerror="this.style.display='none';this.nextElementSibling.style.display='block'">
                <p style="display:none">Add photo1.jpg here 💙</p>
                <p>Memory one ✨</p>
            </div>

            <div class="photo">
                <img src="/static/photo2.jpg" alt="Memory two"
                     onerror="this.style.display='none';this.nextElementSibling.style.display='block'">
                <p style="display:none">Add photo2.jpg here 💙</p>
                <p>Memory two 🌙</p>
            </div>

            <div class="photo">
                <img src="/static/photo3.jpg" alt="Memory three"
                     onerror="this.style.display='none';this.nextElementSibling.style.display='block'">
                <p style="display:none">Add photo3.jpg here 💙</p>
                <p>Another favorite 💫</p>
            </div>
        </div>
    </section>

    <section class="card">
        <div class="moon">💌</div>
        <h2>A Letter For You</h2>
        <p>There are some things I want you to know.</p>

        <button class="primary" onclick="toggleLetter()">
            Open My Letter 💙
        </button>

        <div class="letter" id="letter">
            <h3>Dear Christian,</h3>

            I don't really know where to begin, but I
            want to be honest about how I feel.

            <br><br>

            I care about you more than I can easily
            explain. Even the little conversations,
            the random moments, and the simplest
            things about you have become special to me.

            <br><br>

            I know you like someone else, and I respect
            that. I don't want this letter to make you
            feel guilty or pressured to choose me.

            <br><br>

            I just wanted you to know that my feelings
            are genuine. You matter to me, and I'm
            grateful for the moments I've shared with you.

            <br><br>

            Whatever your answer may be, I hope you
            find happiness. You deserve that.

            <br><br>

            With lots of care,<br>
            <b>Xiannnn😛 💙</b>
        </div>
    </section>

    <footer>
        MADE WITH LOVE UNDER THE MIDNIGHT SKY ✦
    </footer>

</div>

<script>
let attempts = 0;

function tryNo() {
    attempts++;

    const no = document.getElementById("no");
    const message = document.getElementById("message");

    if (attempts >= 2) {
        message.innerHTML =
        "UNDER THE BUTTON... ARE YOU SURE ABOUT THAT? 👀😭";
    } else {
        message.innerHTML = "NICE TRY! 😭";
    }

    no.style.position = "fixed";

    const maxX = Math.max(10, window.innerWidth - no.offsetWidth - 10);
    const maxY = Math.max(10, window.innerHeight - no.offsetHeight - 10);

    no.style.left = (10 + Math.random() * (maxX - 10)) + "px";
    no.style.top = (10 + Math.random() * (maxY - 10)) + "px";
}

function sayYes() {
    document.getElementById("message").innerHTML =
    "YIPPEEE YESS FINALLY I'VE BEEN WAITING FOR THIS!!! 💗🎉";

    document.querySelector("h1").innerHTML = "IT'S A YES!!! 💙";
    document.getElementById("no").style.display = "none";

    celebrate();
}

function toggleLetter() {
    const letter = document.getElementById("letter");

    letter.style.display =
    letter.style.display === "block" ? "none" : "block";
}

function createHeart() {
    const heart = document.createElement("div");
    heart.className = "float";
    heart.textContent = ["💙","💗","✨","💕"][
        Math.floor(Math.random() * 4)
    ];

    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = (18 + Math.random() * 20) + "px";

    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 6000);
}

function celebrate() {
    for (let i = 0; i < 50; i++) {
        setTimeout(createHeart, i * 80);
    }
}

setInterval(createHeart, 1000);
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
