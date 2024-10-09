<script>
    //Components
    import Navbar from "$lib/Components/Navbar.svelte";
    import Footer from "$lib/Components/Footer.svelte";
    // Main CSS
    import "../app.css";
</script>

<div class="">
    <!-- Navbar -->
    <Navbar />

    <div class="w-full flex justify-center">
        <!-- Main section -->
        <slot />
    </div>

    <!-- Footer -->
    <Footer />
</div>