<script lang="ts">
    import { db, storage, user, userData } from "$lib/firebase";
    import { updateDoc, doc } from "firebase/firestore";
    import { ref, uploadBytes, getDownloadURL } from "firebase/storage";
    import AuthCheck from "../auth_check.svelte";
    import { ProgressBar } from "@skeletonlabs/skeleton";

    import defaultImage from "$lib/assests/user.png"

    let previewURL: string;
    let uploading = false;
    
    async function upload(e:any) {
        uploading = true;
        const file = e.target.files[0];
        previewURL = URL.createObjectURL(file);
        const storageRef = ref(storage, `users/${$user!.uid}/profile.png`);
        const result = await uploadBytes(storageRef, file);
        const url = await getDownloadURL(result.ref);
        
        await updateDoc(doc(db, "users", $user!.uid), { photoURL : url });
        uploading = false;
    }
    
</script>

<AuthCheck>
    <form class="max-w-screen-md w-full">
        <div class="form-control w-full max-w-xs my-10 mx-auto text-center">
            <img 
                src = {previewURL ?? $userData?.photoURL ?? defaultImage}
                alt="photoURL"
                width="256"
                height="256"
                class="mx-auto"
            />
            <label for="photoURL" class="label">
                <span class="label-text">Pick a file</span>
            </label>
            <input 
                on:change={upload}
                name="photoURL"
                type="file"
                class="file-input file-input-bordered w-full max-w-xs"
                accept="image/png, image/jpeg, image/gif, image/webp"
            />
            {#if uploading}
                <p>Uploading</p>
                <ProgressBar />
            {/if}
        </div>
    </form>
</AuthCheck>