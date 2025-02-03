import { BrowserRouter, Outlet, Route, Routes } from "react-router";

export default function App() {
  return (
    <>
      <h1>Home</h1>
      <Outlet />
    </>
  );
}
