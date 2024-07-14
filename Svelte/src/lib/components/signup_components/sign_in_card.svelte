<script lang="ts">
    import { auth } from "$lib/firebase"
    import { GoogleAuthProvider, signInWithPopup } from "firebase/auth";

    async function signInWithGoogle() {
        const provider = new GoogleAuthProvider();
        const user = await signInWithPopup(auth, provider);
        console.log(user)
    }
</script>

<button class="btn variant-filled-secondary" on:click={signInWithGoogle}>Link Google Account</button>