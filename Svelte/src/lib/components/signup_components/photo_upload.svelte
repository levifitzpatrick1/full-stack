<script lang="ts">
    import AuthCheck from "../auth_check.svelte";
    import { ProgressBar } from "@skeletonlabs/skeleton";
    import defaultImage from "$lib/assests/user.png";
    import { uploadPhoto, apiPath } from "$lib/api";
    import { userData } from "$lib/types";
    import { user } from "$lib/firebase";


    let previewURL: string;
    let uploading = false;

    async function upload(e: Event) {
        const input = e.target as HTMLInputElement;
        if (input.files && input.files[0]) {
            const file = input.files[0];
            uploading = true

            try {
                const photoPath = await uploadPhoto(file, $user!.uid);
                previewURL = `${apiPath}/uploads/${photoPath}`
            } catch (error) {
                console.error("Photo upload failed", error);
            } finally {
                uploading = false;
            }
        }
    }
</script>

<AuthCheck>
    <form class="max-w-screen-md w-full">
        <div class="form-control w-full max-w-xs my-10 mx-auto text-center">
            <img 
                src = {previewURL ?? $userData?.photo ?? defaultImage}
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