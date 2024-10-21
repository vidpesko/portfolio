<script>
    import { fly } from "svelte/transition";
    import { onMount } from "svelte";
    // Logo
    import logo from "../static/images/logo-white.png";
    // Components
    import CVBtn from "./CVBtn.svelte";
    // Icons
    import MenuIcon from '~icons/streamline/interface-setting-menu-2-button-parallel-horizontal-lines-menu-navigation-staggered-three-hamburger';
    import XIcon from '~icons/material-symbols/close-rounded'

    // Display menu
    export let showMenu = false;

    // Show navbar
    let showNavbar = true;

    onMount(() => {
        // Hide navbar when scrolled down, show it when scroll up
        let prevScrollPosition = window.scrollY;
        let scrollPosition = prevScrollPosition;
        let deltaScrollPosition = 0;

        window.addEventListener("scroll", () => {
            scrollPosition = window.scrollY;
            deltaScrollPosition = scrollPosition - prevScrollPosition;
            if ((deltaScrollPosition > 0) && (deltaScrollPosition > 50) && (showNavbar == true)) {
                showNavbar = false;
                prevScrollPosition = scrollPosition;
                deltaScrollPosition = 0;
            } else if ((deltaScrollPosition < 0) && (deltaScrollPosition > -50)) {
                showNavbar = true;
                prevScrollPosition = scrollPosition;
            } else if (Math.abs(deltaScrollPosition) > 50) {
                deltaScrollPosition = 0;
                prevScrollPosition = scrollPosition;
            } 
        });
    });
</script>


{#if showNavbar}
<div transition:fly={{ y: -200, duration: 500 }} class="w-screen flex items-center p-4 pe-6 z-30 fixed bg-background bg-opacity-80 shadow-lg shadow-[#ffffff0a]">
    <div class="flex-1">
        <a href="/" class="btn btn-ghost text-xl"><img src={logo} alt="" width="60px"></a>
    </div>
    <div class="flex-none">
        <ul class="md:flex hidden items-center gap-x-4">
            <li>
                <a href="#jaz" class="btn-navigation"><span>01.</span>O meni</a>
            </li>
            <li>
                <a href="#projekti" class="btn-navigation"><span>02.</span>Projekti</a>
            </li>
            <li>
                <a href="#izkusnje" class="btn-navigation"><span>03.</span>Izkušnje</a>
            </li>
            <li>
                <CVBtn />
            </li>
        </ul>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div on:click={() => showMenu = !showMenu} tabindex="0" role="button" class="btn m-1 btn-ghost md:hidden">
            {#if !showMenu}
            <MenuIcon class="text-2xl text-white" />
            {:else}
            <XIcon class="text-4xl text-white" />
            {/if}
        </div>
    </div>
</div>
{/if}
