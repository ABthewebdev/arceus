// Function for set timeout for a set number of seconds
export async function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
