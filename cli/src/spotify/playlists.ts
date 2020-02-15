import axios from "axios";

export const getPlaylists = (term: string | undefined, token: string | undefined, limit: string | undefined | number) => 
    axios({
        method: "GET",
        url: `https://api.spotify.com/v1/search?q=${term}&type=playlist&market=US&limit=${String(limit)}`,
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
    }).then(res => res.data.playlists.items)