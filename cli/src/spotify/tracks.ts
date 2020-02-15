import axios from "axios";

export const getTracks = (url : string, token : string | undefined) => axios({
    method : "GET",
    url : url,
    headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
    },
}).then(res => res.data.tracks.items); 