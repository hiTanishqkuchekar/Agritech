

const API_URL = "http://127.0.0.1:8000";

/* ===========================
   SIGNUP (Frontend only)
=========================== */
function handleRegister(event){
    event.preventDefault();

    const name = document.getElementById("regName").value;
    const email = document.getElementById("regEmail").value;
    const password = document.getElementById("regPassword").value;

    const user = { name, email };

    // Save locally (since backend auth not available)
    localStorage.setItem("user", JSON.stringify(user));

    alert("Account created successfully");
    window.location.href = "dashboard.html";
}


/* ===========================
   LOGIN (Frontend only)
=========================== */
function handleLogin(event){
    event.preventDefault();

    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    // Dummy login (no backend)
    const user = {
        name: email.split("@")[0],
        email: email
    };

    localStorage.setItem("user", JSON.stringify(user));
    window.location.href = "dashboard.html";
}


/* ===========================
   Load User in Dashboard
=========================== */
function loadUser(){
    const user = JSON.parse(localStorage.getItem("user"));

    if(user){
        const nameElement = document.getElementById("username");
        if(nameElement){
            nameElement.innerText = user.name;
        }
    }else{
        window.location.href = "signin.html";
    }
}


/* ===========================
   AI Recommendation API
=========================== */
async function getRecommendation(land, income){

    const res = await fetch(`${API_URL}/recommend`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            land_size: Number(land),
            income: Number(income),
            documents: ["aadhaar","land_record","bank_account"]
        })
    });

    const data = await res.json();
    console.log("AI Result:", data);
    alert("Recommended Scheme: " + data.recommended_scheme.scheme_name);
}