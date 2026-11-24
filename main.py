
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
* { box-sizing: border-box; }

body {
    margin: 0;
    min-height: 100vh;
    font-family: Georgia, serif;
    color: white;
    text-align: center;
    background: linear-gradient(135deg, #020817, #101b46, #29164d);
    background-attachment: fixed;
    overflow-x: hidden;
}

.container {
    width: 90%;
    max-width: 650px;
    margin: 45px auto;
    padding: 28px 20px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 25px;
    box-shadow: 0 0 35px #536dfe44;
}

h1 { color: #c7d8ff; }

.subtitle {
    color: #d9dcff;
    line-height: 1.7;
}

button {
    border: none;
    border-radius: 30px;
    padding: 13px 25px;
    margin: 9px;
    font-size: 16px;
    cursor: pointer;
}

.yes {
    background: #9bbaff;
    color: #07132f;
}

.no {
    background: #e3e5f5;
    color: #222;
}

.gallery {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 25px 0;
}

.gallery img {
    width: 100%;
    border-radius: 15px;
    object-fit: cover;
    border: 2px solid #a9c4ff;
}

.letter {
    display: none;
    text-align: left;
    line-height: 1.8;
    background: #ffffff12;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}

#response {
    margin-top: 20px;
    color: #c7d8ff;
    line-height: 1.7;
}

footer {
    margin-top: 30px;
    color: #aab8e8;
    font-size: 13px;
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

    <div class="gallery">
        <img src="/static/photo1.jpg" alt="Our first picture">
        <img src="/static/photo2.jpg" alt="Our second picture">
    </div>

    <button class="yes" onclick="sayYes()">YES! 💙</button>
    <button class="no" onclick="sayNo()">NO</button>

    <div id="response"></div>

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
        Even the little conversations, the random moments,
        and the simplest things about you have become
        special to me.
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
        Made with care • A little midnight-blue surprise ✨
    </footer>

</div>

<script>
function sayYes() {
    document.getElementById("response").innerHTML =
    "YIPPEEEEE! YIPPEEEEE! 💙🎉<br>" +
    "Thank you for saying YES!";
}

function sayNo() {
    document.getElementById("response").innerHTML =
    "That's okay. Thank you for being honest. 💙";
}

function showLetter() {
    const letter = document.getElementById("letter");
    letter.style.display =
        letter.style.display === "block" ? "none" : "block";
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

                    
