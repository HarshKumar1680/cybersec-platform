async function networkScan(){
    const target = document.getElementById("target").value;
    document.getElementById("output").textContent = "Running network scan...";

    const res = await fetch("http://localhost:5000/api/scan/network",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({target})
    });

    const data = await res.json();
    document.getElementById("output").textContent = data.data;
}

async function webScan(){
    const target = document.getElementById("target").value;
    document.getElementById("output").textContent = "Running web scan...";

    const res = await fetch("http://localhost:5000/api/scan/web",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({target})
    });

    const data = await res.json();
    document.getElementById("output").textContent = JSON.stringify(data, null, 2);
}

async function serverScan(){
    const target = document.getElementById("target").value;
    document.getElementById("output").textContent = "Running server scan (Nikto)...";

    const res = await fetch("http://localhost:5000/api/scan/server",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({target})
    });

    const data = await res.json();

    console.log("SERVER RESPONSE:", data);   // debug

    if(data.data){
        document.getElementById("output").textContent = data.data;
    } else {
        document.getElementById("output").textContent = JSON.stringify(data, null, 2);
    }
}
