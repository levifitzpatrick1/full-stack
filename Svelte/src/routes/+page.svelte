<script lang="ts">
    import { GoogleAuthProvider, signInWithPopup } from "firebase/auth";
    import { auth, user } from "$lib/firebase";
    import { goto } from "$app/navigation";
    import { userData } from "$lib/apiTypes";
    import { getUserData } from "$lib/api";

// once you log in with google
// 1 get user data
// 2 goto /{username} where username is pulled from user data
    async function signIn() {
        if (!$user){
            const provider = new GoogleAuthProvider();
            await signInWithPopup(auth, provider)
        }

        $userData = await getUserData($user!.uid)
        goto(`/${$userData.username}`)
    }
</script>

<a href="/SignUp" class="btn variant-filled text-center bg-center" data-sveltekit-preload-data="hover">Sign Up</a>

<button class="btn btn-md variant-filled-secondary" on:click={signIn}>Log In</button>