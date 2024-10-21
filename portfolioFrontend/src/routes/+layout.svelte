<script>
    import { fade } from "svelte/transition";

    //Components
    import Navbar from "$lib/Components/Navbar.svelte";
    import Footer from "$lib/Components/Footer.svelte";
    import CVBtn from "$lib/Components/CVBtn.svelte";
    // Icons
    import GithubIcon from "virtual:icons/mdi/github-box";
    import IGIcon from "virtual:icons/mdi/instagram";
    import EmailIcon from "virtual:icons/mdi/email";
    // Main CSS
    import "../app.css";

    // Display menu
    let showMenu;
</script>

<div class:overflow-y-hidden={showMenu} class:h-screen={showMenu} class="bg-background">
    <!-- Navbar -->
    <Navbar bind:showMenu={showMenu} />

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

<!-- Full page overlay menu -->
{#if showMenu}
<div transition:fade class="w-screen h-screen bg-[rgba(0,0,0,0.9)] absolute z-20 top-0 left-0 transition duration-500 flex flex-col items-center justify-center">
    <ul class="text-center font-sans font-extrabold text-5xl">
        <li><a on:click={() => showMenu = false} href="#jaz"><span class="font-techno2 text-primary text-3xl">01.</span><br>O meni</a></li>
        <li class="my-1"><a on:click={() => showMenu = false} href="#projekti"><span class="font-techno2 text-primary text-3xl">02.</span><br>Projekti</a></li>
        <li><a on:click={() => showMenu = false} href="#izkusnje"><span class="font-techno2 text-primary text-3xl">03.</span><br>Izkušnje</a></li>
        <li class="mt-1"><span class="font-techno2 text-primary text-3xl">04.</span><br>Kontakt</li>
    </ul>

    <div class="mt-5">
        <CVBtn />
    </div>
</div>
{/if}
