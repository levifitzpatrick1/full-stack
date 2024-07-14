<script lang="ts">
    import { user } from "$lib/firebase";

</script>

<h2>User Data</h2>
<p>
    @{$user?.uid}
</p>
<p>
    @{$user?.email}
</p>
<p>
    @{$user?.photoURL}
</p>