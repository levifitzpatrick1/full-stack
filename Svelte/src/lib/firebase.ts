import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
    apiKey: "AIzaSyAh30sLmChXGsFtpCJiMs566im4ychlXjA",
    authDomain: "fireship-io-test-project.firebaseapp.com",
    projectId: "fireship-io-test-project",
    storageBucket: "fireship-io-test-project.appspot.com",
    messagingSenderId: "132931521119",
    appId: "1:132931521119:web:71857345781465599e69ea",
    measurementId: "G-Y3T9837CLG"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const db = getFirestore();
export const auth = getAuth();
export const storage = getStorage();