<script>
	import "../../app.css";
    import { AppBar } from "@skeletonlabs/skeleton";
    import logo from '$lib/assests/barcodeLogo.png'
</script>

<style>
    img {
        max-height: 50px;
    }
</style>

<AppBar>
	<svelte:fragment slot="lead">
        <img src={logo} alt="Bar Code Logo" />
    </svelte:fragment>
    <h1 class="h1">My Things List</h1>
</AppBar>
<br>
<main class="card w-4/12 bg-transparent text-neutral-content mx-auto">
    <div class="card-body">
      <slot />
    </div>
</main>