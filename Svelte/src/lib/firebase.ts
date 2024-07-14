import { initializeApp } from "firebase/app";
import { doc, getFirestore, onSnapshot } from "firebase/firestore";
import { getAuth, onAuthStateChanged, type User } from "firebase/auth";
import { getStorage } from "firebase/storage";
import { derived, writable, type Readable } from "svelte/store";

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

function userStore(){
    let unsubscribe: () => void;

    if (!auth || !globalThis.window) {
        console.warn('Auth is not initialized or not in browser');
        const { subscribe } = writable<User | null>(null);

        return {
            subscribe,
        }
    }

    const { subscribe } = writable(auth?.currentUser, (set) => {
        onAuthStateChanged(auth, (user) => {
            set(user);
        });

        return () => unsubscribe;
    });

    return {
        subscribe,
    };
}

export const user = userStore();

export function docStore<T>(
    path: string,
) {
    let unsubscribe: () => void;
    const docRef = doc(db, path);

    const { subscribe } = writable<T | null>(null, (set) => {
        unsubscribe = onSnapshot(docRef, (snapshot) => {
            set((snapshot.data() as T) ?? null);
        });

        return () => unsubscribe();
    });

    return {
        subscribe,
        ref: docRef,
        id: docRef.id,
    };
}