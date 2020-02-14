import { AzureFunction, Context, HttpRequest } from "@azure/functions"
import { db } from "./utils/admin";
import { SPOTIFY_PLAYLIST_SCANNER_KEY } from "./utils/env";
import axios from "axios";

const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {
    const term = (req.query.q || (req.body && req.body.q));
    const token = (req.query.token || (req.body && req.body.token));
    const key = (req.query.key || (req.body && req.body.key));

    if (key !== SPOTIFY_PLAYLIST_SCANNER_KEY) {
        context.res = {
            status : 401,
            body: `Key not valid ${key}`
        };
    }
    else {
        axios({
            method : "GET",
            url : `https://api.spotify.com/v1/search?q=${term}&type=playlist`,
            headers : {
                "Accept" : "application/json",
                "Content-Type" : "application/json",
                "Authorization" : `Bearer ${token}`
            }
        }).then(data => {
            data["playlists"]["items"]
        })
        .catch((err) => context.res = {
            status: 404,
            body: err
        })
    }
};

export default httpTrigger;


