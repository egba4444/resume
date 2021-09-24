async function get_visitors() {
    try{
        let response = await fetch('https://b977mvfj4h.execute-api.us-east-1.amazonaws.com/dev/', {
            method: 'GET',
            headers:{

            }
        });
        let data = await response.json()
        document.getElementById("visitors").innerHTML = data + " " + "visits";
        console.log(data)
        return data;
    } catch (err) {
        console.error(err);
    }
}
get_visitors();