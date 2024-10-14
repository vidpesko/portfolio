<script>
    //Components
    import Navbar from "$lib/Components/Navbar.svelte";
    import Footer from "$lib/Components/Footer.svelte";
    // Icons
    import GithubIcon from "virtual:icons/mdi/github-box";
    import IGIcon from "virtual:icons/mdi/instagram";
    import EmailIcon from "virtual:icons/mdi/email";
    // Main CSS
    import "../app.css";
</script>

<div class="">
    <!-- Navbar -->
    <Navbar />

    <div class="w-full flex justify-center">
        <!-- Left social links bar -->
        <div class="fixed lg:block hidden left-10 bottom-0 text-white">
            <ul class="after:h-32 after:bg-white after:block after:w-px after:mx-auto text-center">
                <li class="social-link"><a href="https://github.com/vidpesko" target="_blank"><GithubIcon /></a></li>
                <li class="social-link"><a href="https://www.instagram.com/vidpesko/" target="_blank"><IGIcon /></a></li>
                <li class="social-link"><a href="mailto:vid@pesko.si"><EmailIcon /></a></li>
            </ul>
        </div>

        <!-- Main section -->
        <slot />

        <!-- Right email bar -->
        <div class="fixed lg:block hidden right-10 bottom-0 text-white transition hover:text-primary">
            <div class="after:h-32 after:bg-white after:block after:w-px after:mx-auto text-center flex flex-col items-center">
                <a href="mailto:vid@pesko.si" style="writing-mode: vertical-rl;" class="me-6 tracking-widest transition hover:-translate-y-1">vid@pesko.si</a>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <Footer />
</div>