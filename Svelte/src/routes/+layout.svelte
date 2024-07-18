<script lang="ts">
	import "../app.css";
	import { initializeStores, Modal } from '@skeletonlabs/skeleton';
	import BarcodeScannerModal from "$lib/components/barcode_scanner_modal.svelte";
    import type { ModalComponent } from "@skeletonlabs/skeleton";

	const modalRegistry: Record<string, ModalComponent> = {
		barcodeModal: {ref: BarcodeScannerModal}
	}

	initializeStores();
</script>

<Modal components = {modalRegistry} />

<slot />