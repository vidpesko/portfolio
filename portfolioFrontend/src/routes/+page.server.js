// API Client
import { getProjects } from "$lib/api/client.js";
import { getExperiences } from "$lib/api/client.js";


export async function load() {
    return {
        highlightedProj: await getProjects(true),
        projects: await getProjects(false),
        experiences: await getExperiences(),
    };
}