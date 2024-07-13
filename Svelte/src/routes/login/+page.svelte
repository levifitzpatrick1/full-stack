<script lang="ts">
    import { userData, user } from "$lib/firebase";

</script>

<h2>User Data</h2>
<p>
    @{$userData?.bio}
</p>
<p>
    @{$userData?.username}
</p>
<p>
    @{$userData?.links}
</p>
<p>
    @{$userData?.photoURL}
</p>

<p>
    @{$user?.uid}
</p>


<p>
    @{$user?.email}
</p>


<p>
    @{$user?.photoURL}
</p>