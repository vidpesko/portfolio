<script>
	let visible = true;
    let headingWordIndex = 0;
    let headingWords = [
        {word: "samooklicani", color: "text-primary"},
        {word: "ponosni", color: "text-red-500"},
    ]

	function typewriter(node, { speed = 0.75 }) {
		const valid = node.childNodes.length === 1 && node.childNodes[0].nodeType === Node.TEXT_NODE;

		if (!valid) {
			throw new Error(`This transition only works on elements with a single text node child`);
		}

		const text = node.textContent;
		const duration = text.length / (speed * 0.01);

		return {
			duration,
			tick: (t) => {
				const i = Math.trunc(text.length * t);
				node.textContent = text.slice(0, i);
			}
		};
	}

    setInterval(() => {
        visible = false;
        headingWordIndex++;
        headingWordIndex = ((headingWordIndex >= headingWords.length) ? 0 : headingWordIndex);
        new Promise(resolve => setTimeout(resolve, 2000)).then(() => {visible = true;});
    }, 10000)
</script>

<div class="w-5/6 max-w-7xl">
    <!-- Hero section -->
    <section class="text-secondary h-screen flex items-center">
        <div class="">
            <!-- Header / welcome msg -->
            <h1 class="lg:text-8xl text-7xl font-heading font-extrabold leading-[1.1]">
                Zdravo, <span class="wave">👋</span><br>
                sem <span class="text-white">Vid Pesko</span>,<br>
                {#if visible}
                <span class="blinking {headingWords[headingWordIndex].color}" transition:typewriter>{headingWords[headingWordIndex].word}</span>
                {/if}
                ‎
                <br class="xl:hidden">
                programer</h1>
                <!-- Short description -->
                <p class="mt-4 text-xl">Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores odit unde quidem nostrum culpa esse labore expedita similique iusto? Enim!</p>

            <!-- CTO -->
            <button class="btn-custom mt-10">
                <span>Poglej projekte</span>
            </button>
        </div>
    </section>

    <!-- About me -->
    <section id="jaz" class="">
        <h1 class="text-4xl"><span>01.</span> O meni</h1>
    </section>

    <section id="projekti" class="h-screen">
        <h1 class="text-4xl my-10"><span>02.</span> Nekaj projektov</h1>

        <!-- Project -->
        <div class="flex justify-end items-center p-4 rounded-xl bg-gradient-to-r gap-4 border-2 border-transparent transition hover:border-stone-500 mb-4 hover:text-white" style="background: linear-gradient(to right, #0f0c29, #302b63, #24243e);">
            <!-- Image -->
            <img class="rounded" src="https://picsum.photos/id/237/600/300" alt="">

            <div class="text-end z-10">
                <!-- Title -->
                <h2 class="text-3xl mb-4 font-bold">Lorem, ipsum.</h2>
                <!-- Description -->
                <p class="text-md mb-4">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid sunt quia enim nemo quod necessitatibus eligendi eveniet.
                </p>
                <!-- Stats -->
                <div class="stats shadow mb-4 rounded-lg text-inherit">
                    <div class="stat place-items-center">
                        <div class="stat-title">Prenosi</div>
                        <div class="stat-value">31K</div>
                        <div class="stat-desc">Od objave, leta 2022</div>
                    </div>
                    <div class="stat place-items-center">
                        <div class="stat-title">Uporabnikov</div>
                        <div class="stat-value">4,200</div>
                        <div class="stat-desc text-secondary">↗︎ 40 (2%)</div>
                    </div>
                    <div class="stat place-items-center">
                        <div class="stat-title">Noih registracij</div>
                        <div class="stat-value">1,200</div>
                        <div class="stat-desc">dnevno </div>
                    </div>
                </div>
                <!-- Skills / technologies -->
                <div class="flex justify-end gap-x-4 mb-4">
                    <p class="badge badge-primary transition hover:translate-y-1">Svelte</p>
                    <p class="badge badge-accent transition hover:translate-y-1">CSS</p>
                </div>
            </div>
        </div>

        <div class="flex justify-end p-4 rounded-xl bg-gradient-to-r gap-4 border-2 border-transparent transition hover:border-stone-500 project-flip" style="background: linear-gradient(to right, #0f0c29, #302b63, #24243e);">
            <!-- Image -->
            <img class="rounded" src="https://picsum.photos/id/237/600/300" alt="">

            <div class="text-end z-10">
                <!-- Title -->
                <h2 class="text-3xl mb-4 text-white font-bold">Lorem, ipsum.</h2>
                <!-- Description -->
                <p class="text-white text-md mb-4">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid sunt quia enim nemo quod necessitatibus eligendi eveniet.
                </p>
                <!-- Stats -->
                <div class="stats shadow mb-4 w-full rounded-lg text-white">
                    <div class="stat place-items-center">
                        <div class="stat-title">Prenosi</div>
                        <div class="stat-value">31K</div>
                        <div class="stat-desc">Od objave, leta 2022</div>
                    </div>
                    <div class="stat place-items-center">
                        <div class="stat-title">Uporabnikov</div>
                        <div class="stat-value text-secondary">4,200</div>
                        <div class="stat-desc text-secondary">↗︎ 40 (2%)</div>
                    </div>
                    <div class="stat place-items-center">
                        <div class="stat-title">Noih registracij</div>
                        <div class="stat-value">1,200</div>
                        <div class="stat-desc">dnevno </div>
                    </div>
                </div>
                <!-- Skills / technologies -->
                <div class="flex justify-end gap-x-4 mb-4">
                    <p class="badge badge-primary">Svelte</p>
                    <p class="badge badge-accent">CSS</p>
                </div>
            </div>
        </div>
    </section>
</div>