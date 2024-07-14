<script lang="ts">
    import { db, user } from "$lib/firebase";
    import AuthCheck from "../auth_check.svelte";
    import { checkUsernameAvailability, confirmUsername, getUserData } from "$lib/api";
    import { userData } from "$lib/apiTypes";

    let username = "";
    let loading = false;
    let isAvailable = false;

    let debounceTimer: NodeJS.Timeout;

    const re = /^(?=[a-zA-Z0-9._]{3,16}$)(?!.*[_.]{2})[^_.].*[^_.]$/;

    $: isValid = username?.length > 2 && username.length < 16 && re.test(username);
    $: isTouched = username.length > 0;
    $: isTaken = isValid && !isAvailable && !loading

    async function checkAvailability() {
        if (!isValid) {
            isAvailable = false;
            return
        }
        isAvailable = false;
        loading = true;
        clearTimeout(debounceTimer);

        debounceTimer = setTimeout(async () =>{
            console.log("Checking availability of ", username);
            isAvailable = await checkUsernameAvailability(username);
            console.log("finished the check")
            loading = false
        }, 500);

    }
    async function confirmUsernameEvent() {
        console.log("confirming username", username);
        await confirmUsername(username, $user!.uid);
        console.log($user?.uid)
        $userData = await getUserData($user!.uid);
    }
</script>

<AuthCheck>
    <div class="justify-items-center flex flex-col text-center items-center w-full padding 20px">
        <form class="w-3/5" on:submit|preventDefault={confirmUsernameEvent}>
            <input 
                type="text"
                placeholder="Username"
                class="input size-full"
                bind:value={username}
                on:input={checkAvailability}
                class:input-error={(!isValid && isTouched)}
                class:input-warning={isTaken}
                class:input-success={isAvailable && isValid && !loading}
            />
    
            <div class="my-4 min-h-16 px-8 w-full">
                {#if loading && username.length != 0}
                    <p class="text-secondary">Checking availability of @{username}</p>
                {/if}
    
                {#if !isValid && isTouched}
                    <p class="text-error text-sm">must be 3-16 characters long, alphanumerical only</p>
                {/if}
    
                {#if isValid && !isAvailable && !loading}
                    <p class="text-warning text-sm">@{username} is not available</p>    
                {/if}
    
                {#if isAvailable}
                <button type="button" on:click={confirmUsernameEvent} class="btn variant-filled-success">Confirm username @{username} </button>
                {/if}
            </div>
        </form>
    </div>    
    </AuthCheck>

