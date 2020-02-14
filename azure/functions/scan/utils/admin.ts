import { initializeApp, firestore, credential } from "firebase-admin";
import { FIREBASE_SERVICE_ACCOUNT, FIREBASE_DATABASE_URL } from "./env";
import { Firestore } from "@google-cloud/firestore";

initializeApp({
    credential: credential.cert(FIREBASE_SERVICE_ACCOUNT),
    databaseURL: FIREBASE_DATABASE_URL
});

export const db : Firestore = firestore();