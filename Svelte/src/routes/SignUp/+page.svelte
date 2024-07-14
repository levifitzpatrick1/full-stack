<script lang="ts">
    import { Stepper, Step } from '@skeletonlabs/skeleton';
    import SignInCard from '$lib/components/signup_components/sign_in_card.svelte';
    import PhotoUpload from '$lib/components/signup_components/photo_upload.svelte';
    import UsernameCard from '$lib/components/signup_components/username_card.svelte';
    import { userData } from '$lib/apiTypes';
    import { goto } from '$app/navigation';
    import { user } from '$lib/firebase';

    $: route = $userData?.username ? `/${$userData.username}` : '/';
    $: GoogleAuth = !$user;
    $: createdUsername = !$userData;

    function onCompleteHandler(e: Event): void {
        console.log('Event complete:', e);
        console.log('Navigating to route:', route);

        // Ensure the route is a relative path
        if ($userData?.username) {
            goto(route);
        } else {
            console.error('Username not found in userData');
        }
    }

</script>


<div class="stepper-container p-5">
    <Stepper on:complete={onCompleteHandler}>
        <Step locked={GoogleAuth}>
            <svelte:fragment slot="header">Email</svelte:fragment>
            <div class="text-center">
                <SignInCard />
            </div>
        </Step>
        <Step locked={createdUsername}>
            <svelte:fragment slot="header">Username</svelte:fragment>
            <div class="text-center">
                <UsernameCard />
            </div>
        </Step>
        <Step>
            <svelte:fragment slot="header">Photo</svelte:fragment>
            <div class="text-center">
                <PhotoUpload />
            </div>
        </Step>
    </Stepper>
</div>
