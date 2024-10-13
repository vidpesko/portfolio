<script>
    // Images & static files
    import Headshot from "$lib/static/images/headshot.jpg";

    // Typewriter on heading effect
	let visible = true;
    let headingWordIndex = 0;
    // List of headings with colors
    let headingWords = [
        {word: "samooklic", color: "text-primary"},
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
    }, 10000);

    // 3D About Me Image
    let aboutImg;
    let aboutImgWidth;
    let aboutImgHeight;
</script>

<div class="w-[70%] max-w-7xl">
    <!-- Hero section -->
    <section class="text-secondary h-screen flex items-center mb-32">
        <div class="">
            <!-- Header / welcome msg -->
            <h1 class="lg:text-8xl text-7xl font-heading font-extrabold leading-[1.1]">
                Zdravo, <button class="animate-wiggle-more animate-twice cursor-default">👋</button><br>
                sem <span class="text-white">Vid Pesko</span>,<br>
                {#if visible}
                <span class="blinking {headingWords[headingWordIndex].color}" transition:typewriter>{headingWords[headingWordIndex].word}</span>
                {/if}
                ‎
                <br class="xl:hidden">
                programer</h1>
                <!-- Short description -->
                <p class="mt-8 text-xl">Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores odit unde quidem nostrum culpa esse labore expedita similique iusto? Enim!</p>

            <!-- CTO -->
            <a href="#projekti" class="btn-custom mt-10">
                <span>Poglej projekte</span>
            </a>
        </div>
    </section>

    <!-- About me -->
    <section id="jaz" class="mb-56">
        <h1 class="text-4xl mb-10"><span>01.</span> O meni</h1>

        <div class="flex gap-x-8">
            <!-- Description -->
            <div class="grow basis-0 text-md">
                <p class="pb-4">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Impedit deleniti, porro beatae doloribus rem ipsum facilis eum <a class="link link-primary" href="https://google.com">similique</a> ratione delectus saepe fuga aliquam quam. Voluptates voluptatem aliquam iste aliquid fugit!</p>
                <p class="pb-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto quibusdam beatae blanditiis. Aliquam expedita distinctio tempore voluptatem saepe nobis quas.</p>
                <p class="pb-4">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Inventore, voluptatum.</p>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt qui, totam fuga, sed autem quasi voluptate nostrum placeat illum nulla explicabo dolore dolores, atque perferendis adipisci amet aut ullam velit.</p>
                <!-- Skills / technologies -->
                <p>Nekaj tehnologij, ki sem jih pred kratkim uporabljal.</p>
                <ul>
                    <li>Svelte / SvelteKit</li>
                    <li>Svelte / SvelteKit</li>
                    <li>Svelte / SvelteKit</li>
                    <li>Svelte / SvelteKit</li>
                    <li>Svelte / SvelteKit</li>
                    <li>Svelte / SvelteKit</li>
                </ul>
            </div>
            <!-- Image -->
            <div class="grow basis-0">
                <!-- svelte-ignore a11y-no-static-element-interactions -->
                <!-- svelte-ignore a11y-mouse-events-have-key-events -->
                <div
                bind:clientHeight={aboutImgHeight}
                bind:clientWidth={aboutImgWidth}
                bind:this={aboutImg}
                on:mousemove={(e) => {
                    const xVal = e.layerX;
                    const yVal = e.layerY;
                    const yRotation = 20 * ((xVal - aboutImgWidth / 2) / aboutImgWidth);
                    const xRotation = -20 * ((yVal - aboutImgHeight / 2) / aboutImgHeight);
                    const string = 'perspective(500px) scale(1.1) rotateX(' + xRotation + 'deg) rotateY(' + yRotation + 'deg)';
                    aboutImg.style.transform = string;
                }}
                on:mouseout={() => {
                    aboutImg.style.transform = 'perspective(500px) scale(1) rotateX(0) rotateY(0)';
                }}
                on:mousedown={() => {
                    aboutImg.style.transform = 'perspective(500px) scale(0.9) rotateX(0) rotateY(0)';
                }}
                on:mouseup={() => {
                    aboutImg.style.transform = 'perspective(500px) scale(1.1) rotateX(0) rotateY(0)';
                }}

                id="tilt"
                class="bg-[url('/src/lib/static/images/headshot.jpg')] w-4/6 h-5/6 mx-auto rounded-lg bg-cover bg-center bg-no-repeat hover:cursor-pointer">
                </div>
            </div>
        </div>
    </section>

    <!-- Projects -->
    <section id="projekti" class="mb-64">
        <h1 class="text-4xl my-10"><span>02.</span> Nekaj projektov</h1>

        <!-- Project -->
        <div class="flex lg:flex-nowrap flex-wrap justify-end items-center p-4 rounded-xl bg-gradient-to-r gap-4 transition hover:scale-105 mb-4 hover:text-white" style="background: linear-gradient(to right, #0f0c29, #302b63, #24243e);">
            <!-- Image -->
            <img class="rounded-lg lg:max-w-[600px] lg:max-h-[1000px] max-h-[300px] w-full object-cover lg:basis-0 lg:grow" src="https://picsum.photos/id/237/500/300" alt="">

            <div class="lg:text-end text-center max-w-full z-10 lg:basis-0 lg:grow">
                <!-- Title -->
                <h2 class="text-3xl mb-4 font-bold">Lorem, ipsum.</h2>
                <!-- Description -->
                <p class="text-md mb-4">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid sunt quia enim nemo quod necessitatibus eligendi eveniet.
                </p>
                <!-- Stats -->
                <div class="stats shadow mb-4 rounded-lg text-inherit w-full">
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
                <!-- Links, technologies -->
                <div class="flex justify-between gap-x-4 mb-4">
                    <!-- Links -->
                    <div class="flex justify-start gap-x-4">
                        <a href="git.com" class="transition hover:translate-y-1">G</a>
                        <a href="web.com">W</a>
                    </div>
                    
                    <!-- Skills / technologies -->
                    <div class="flex justify-end gap-x-4">
                        <p class="badge badge-primary transition hover:translate-y-1">Svelte</p>
                        <p class="badge badge-accent transition hover:translate-y-1">CSS</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="flex justify-end p-4 rounded-xl bg-gradient-to-r gap-4 border-2 border-transparent transition hover:border-stone-500 project-flip" style="background: linear-gradient(to right, #08203e, #557c93);">
            <!-- Image -->
            <img class="rounded w-full object-cover" src="https://picsum.photos/id/237/600/300" alt="">

            <div class="text-end w-3/6 z-10">
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

    <section id="izkusnje" class="mb-64">
        <h1 class="text-4xl mb-10"><span>03.</span> Izkušnje</h1>

        <div class="flex gap-x-10">
            <!-- Sidebar -->
            <div class="">
                <ul>
                    <li>Kolektor Etra</li>
                </ul>
            </div>
            <!-- Job description -->
            <div class="">
                <h3 class="text-2xl text-white">Razvijalec <span class="text-primary">@ Kolektor Etra</span></h3>
                <!-- When -->
                <p class="text-sm">Maj 2018 - Junij 2019</p>
                <!-- My role -->
                <ul>
                    <li>Pomoc pri delu</li>
                    <li>Pomoc pri delu</li>
                </ul>
            </div>
        </div>
    </section>
</div>