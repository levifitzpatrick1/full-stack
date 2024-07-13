<script lang="ts">
    import { Stepper, Step } from '@skeletonlabs/skeleton';
    import SignInCard from '$lib/components/signup_components/sign_in_card.svelte';
    import PhotoUpload from '$lib/components/signup_components/photo_upload.svelte';
    import UsernameCard from '$lib/components/signup_components/username_card.svelte';
    import { userData } from '$lib/firebase';
    import { goto, replaceState } from '$app/navigation';

    $: route = `/${$userData?.username}/edit`;

    function onCompleteHandler(e: Event): void {
        console.log('event:complete', e);
        goto(`/${route}`) 
    }
    let lockedState: boolean = true;

</script>


<style>
    .stepper-container {
        padding: 20px; /* Adjust padding as needed */
    }
</style>


<div class="stepper-container">
    <Stepper on:complete={onCompleteHandler}>
        <Step>
            <svelte:fragment slot="header">Email</svelte:fragment>
            <div class="text-center">
                <SignInCard />
            </div>
        </Step>
        <Step>
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
