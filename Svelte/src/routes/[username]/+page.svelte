<script lang="ts">
    import { page } from '$app/stores';
    import { onMount } from 'svelte';
    import { userData } from '$lib/apiTypes';
    import { getUserData, getUserProfilePic } from '$lib/api';
    import { auth, user } from '$lib/firebase';
    import { signOut } from 'firebase/auth';
    import { goto } from '$app/navigation';
    import defaultImage from "$lib/assests/user.png";
    import { getModalStore, type ModalSettings } from '@skeletonlabs/skeleton';
			
    const modalStore = getModalStore();

    const modal: ModalSettings = {
        type: 'component',
        component: 'barcodeModal',
        title: 'Scan Barcode'
    };
    
    function triggerModal() {
        modalStore.trigger(modal);
    }
                        
    let username: string;
    $: username = $page.params.username;

    let previewURL: string;

    $: isCurrentUser = ($userData?.username == username);

    onMount( async () => {
        console.log($user?.email)
        console.log($userData?.username)
        if (!$userData || $userData?.username !== username) {
            await getUserData($user!.uid)
        }
        previewURL = URL.createObjectURL(await getUserProfilePic($user!.uid));

    });

    async function signOutEvent() {
        try {
            await signOut(auth)
            goto('/')
        } catch (error) {
            console.log(error)
        }
            
    }


</script>

{#if !isCurrentUser}
    <h1>Auth Failed</h1>
{/if}

{#if isCurrentUser}
    <h1>Welcome, {username}!</h1>
    <img src={$userData?.photo} alt={defaultImage}/>
    <button class="btn btn-md variant-filled-primary" on:click={triggerModal}> modal </button>
    <button class="btn btn-md variant-filled-secondary" on:click={signOutEvent}>Sign Out</button>
{/if}
