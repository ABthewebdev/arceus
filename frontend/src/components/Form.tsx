import {
  Link,
  useNavigate,
  useRouter,
  useRouterState,
} from "@tanstack/react-router";
import { useState } from "react";
import api from "../api";

interface FormProps {
  route: string;
  method: string;
}

interface RefreshTokenResponse {
  access: string;
  [key: string]: any; // For other possible response data
}

async function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export default function Form({ route, method }: FormProps) {
  const router = useRouter();
  const isLoading = useRouterState({ select: (s) => s.isLoading });
  const navigate = useNavigate();
  const [isSubmitting, setIsSubmitting] = useState(false);

  const onFormSubmit = async (evt: React.FormEvent<HTMLFormElement>) => {
    setIsSubmitting(true);
    evt.preventDefault();
    try {
      const data = new FormData(evt.currentTarget);
      const fieldValue1 = data.get("username");
      const fieldValue2 = data.get("password");
      if (!fieldValue1 || !fieldValue2) return;
      const username = fieldValue1.toString();
      const password = fieldValue2.toString();
      const res = await api.post<RefreshTokenResponse>(route, {
        username,
        password,
      });

      if (method === "login") {
        localStorage.setItem("access", res.data.access);
        localStorage.setItem("refresh", res.data.refresh);
      } else {
        navigate({ to: "/login" });
      }

      await router.invalidate();

      // This is just a hack being used to wait for the auth state to update
      // in a real app, you'd want to use a more robust solution
      await sleep(1);
    } catch (error) {
      console.error("Error logging in: ", error);
    } finally {
      setIsSubmitting(false);
    }
  };

  const isLoggingIn = isLoading || isSubmitting;
  const name = method === "login" ? "Login" : "Register";

  return (
    <div className="p-2 grid gap-2 place-items-center">
      <h3 className="text-xl">{name}</h3>
      <form className="mt-4 max-w-lg" onSubmit={onFormSubmit}>
        <fieldset disabled={isLoggingIn} className="w-full grid gap-2">
          <div className="grid gap-2 items-center min-w-[300px]">
            <label htmlFor="username-input" className="text-sm font-medium">
              Username
            </label>
            <input
              id="username-input"
              name="username"
              placeholder="Enter your name"
              type="text"
              className="border rounded-md p-2 w-full"
              required
            />
            <input
              id="password-input"
              name="password"
              placeholder="Enter your password"
              type="text"
              className="border rounded-md p-2 w-full"
              required
            />
          </div>
          <button
            type="submit"
            className="bg-blue-500 text-white py-2 px-4 rounded-md w-full disabled:bg-gray-300 disabled:text-gray-500"
          >
            {isLoggingIn ? "Loading..." : "Login"}
          </button>
        </fieldset>
      </form>
      <span>
        Don't have an account? <Link to="/register">Sign Up</Link>
      </span>
    </div>
  );
}
