// github button functions
document.getElementById("githubButton").onmouseover = switchGithubOn;
document.getElementById("githubButton").onmouseleave = switchGithubOff;

function switchGithubOn() {
    document.getElementById("githubButton").style.backgroundColor = "black";
    document.getElementById("githubPic").style.backgroundColor = "#414df7";
    document.getElementById("githubButton").style.color = "#FFFFFF";
}

function switchGithubOff() {
    document.getElementById("githubButton").style.backgroundColor = "#FFFFFF";
    document.getElementById("githubPic").style.backgroundColor = "#FFFFFF";
    document.getElementById("githubButton").style.color = "black";
}

// discord button functions
document.getElementById("discordButton").onmouseover = switchDiscordOn;
document.getElementById("discordButton").onmouseleave = switchDiscordOff;

function switchDiscordOn() {
    document.getElementById("discordButton").style.backgroundColor = "black";
    document.getElementById("discordPic").style.backgroundColor = "#414df7";
    document.getElementById("discordButton").style.color = "#FFFFFF";
}

function switchDiscordOff() {
    document.getElementById("discordButton").style.backgroundColor = "#FFFFFF";
    document.getElementById("discordPic").style.backgroundColor = "#FFFFFF";
    document.getElementById("discordButton").style.color = "black";
}