// src/app/layout.tsx
import type { Metadata } from "next";
import "@/globals.css"; // Ensure you import global styles

export const metadata: Metadata = {
  title: "My Next.js App",
  description: "A Next.js app with Flask backend",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
