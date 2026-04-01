async function analyze() {
    const text = document.getElementById("inputText").value;
    const query = document.getElementById("query").value;

    const actionTable = document.getElementById("actionTable");
    const decisionList = document.getElementById("decisionList");

    actionTable.innerHTML = "";
    decisionList.innerHTML = "";

    const response = await fetch("http://127.0.0.1:8000/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text,
            query: query
        })
    });

    const data = await response.json();

    // 🟢 ACTION ITEMS
    if (!data.action_items || data.action_items.length === 0) {
        actionTable.innerHTML = "<tr><td colspan='3'>No action items found</td></tr>";
    } else {
        data.action_items.forEach(item => {
            const row = `<tr>
                <td>${item.who || "N/A"}</td>
                <td>${item.what || "N/A"}</td>
                <td>${item.when || "N/A"}</td>
            </tr>`;
            actionTable.innerHTML += row;
        });
    }

    // 🔵 DECISIONS
    if (!data.decisions || data.decisions.length === 0) {
        decisionList.innerHTML = "<li>No decisions found</li>";
    } else {
        data.decisions.forEach(d => {
            decisionList.innerHTML += `<li>${d.decision}</li>`;
        });
    }
}

async function uploadFile() {
    const file = document.getElementById("fileInput").files[0];

    if (!file) {
        alert("Please select a file.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    console.log("UPLOAD RESPONSE:", data);  // 🔥 DEBUG

    if (!data.text) {
        alert("No text returned from backend");
        return;
    }

    document.getElementById("inputText").value = data.text;

    analyze();
}