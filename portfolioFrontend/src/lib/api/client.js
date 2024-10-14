const BASE_PATH = "http://localhost:8000//api";


export async function getProjects(highlighted) {
    let url = BASE_PATH + "/list-projects/";

    if (highlighted) {
        url = url + "?highlighted=True";
    }

    const response = await fetch(url);

    if (!response.ok) {
        return {
            error: response.status
        };
    }

    return await response.json();
}