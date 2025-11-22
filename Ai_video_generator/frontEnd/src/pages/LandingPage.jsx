// src/LandingPage.jsx
import React from "react"
import { motion, useScroll, useSpring } from "motion/react"
import LandingPageNav from "./LandingPageNav.jsx"


const features = [
  {
    id: 1,
    title: "Design beautiful landing pages",
    description:
      "Build responsive layouts in minutes. Mix Tailwind utility classes with reusable components for a clean, modern UI.",
    image: "Ai_video_generator/frontEnd/src/videos/MONGO_Test_endpoint.mp4",
  },
  {
    id: 2,
    title: "Animations that feel natural",
    description:
      "Use Motion to add smooth, hardware-accelerated animations that react to scrolling, hovering, and clicking.",
    image: "Ai_video_generator/frontEnd/src/videos/MONGO_Test_endpoint.mp4",
  },
  {
    id: 3,
    title: "Fully responsive out of the box",
    description:
      "Layouts automatically adapt from mobile to desktop with sensible stacking and spacing presets.",
    image: "Ai_video_generator/frontEnd/src/videos/MONGO_Test_endpoint.mp4",
  },
]


function FeatureSection({ title, description, image, reverse = false }) {
  const textAnimation = {
    hidden: { opacity: 0, x: reverse ? 60 : -60 },
    visible: { opacity: 1, x: 0 },
  }

  const imageAnimation = {
    hidden: { opacity: 0, x: reverse ? -60 : 60 },
    visible: { opacity: 1, x: 0 },
  }

  return (
    <section className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
      <div
        className={`flex flex-col items-center gap-10 py-16 lg:py-24 ${
          reverse ? "lg:flex-row-reverse" : "lg:flex-row"
        }`}
      >
        {/* Text */}
        <motion.div
          className="w-full lg:w-1/2"
          variants={textAnimation}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.6, ease: "easeOut" }}
        >
          <h2 className="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">
            {title}
          </h2>
          <p className="mt-4 text-base leading-relaxed text-slate-600 sm:text-lg">
            {description}
          </p>
        </motion.div>

        {/* Image */}
        <motion.div
          className="w-full lg:w-1/2"
          variants={imageAnimation}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, amount: 0.4 }}
          transition={{ duration: 0.6, ease: "easeOut", delay: 0.1 }}
        >
          <div className="overflow-hidden rounded-3xl border border-slate-200/70 bg-slate-50 shadow-sm">
            <video
              src={image}
              playsInline
              autoPlay
              loop
              muted
              controls
              className="h-full w-full object-cover rounded-3x1"
            />
          </div>
        </motion.div>
      </div>
    </section>
  )
}

function LandingPage() {
  // Scroll-linked progress bar at the very top
  const { scrollYProgress } = useScroll()
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 120,
    damping: 30,
    mass: 0.4,
  })

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 via-white to-slate-100 text-slate-900">
      {/* Scroll progress bar */}
      <motion.div
        className="fixed left-0 top-0 z-50 h-1 w-full origin-left bg-gradient-to-r from-indigo-500 via-sky-500 to-emerald-400"
        style={{ scaleX }}
      />

      <LandingPageNav />

      {/* Hero / intro */}
      <main className="pt-6 sm:pt-10">
        <section className="mx-auto max-w-6xl px-4 pb-10 pt-6 sm:px-6 lg:px-8 lg:pb-16">
          <div className="grid gap-10 lg:grid-cols-[3fr,2fr] lg:items-center">
            <motion.div
              initial={{ opacity: 0, y: 24 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7, ease: "easeOut" }}
            >
              <p className="text-sm font-medium uppercase tracking-[0.2em] text-indigo-500">
                Motion + Tailwind + React
              </p>
              <h1 className="mt-3 text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl lg:text-5xl">
                Build animated, responsive pages in minutes.
              </h1>
              <p className="mt-4 max-w-xl text-base leading-relaxed text-slate-600 sm:text-lg">
                This layout uses a sticky navbar, alternating image sections,
                and scroll-triggered animations powered by{" "}
                <span className="font-semibold text-slate-800">Motion</span>.
              </p>
              <div className="mt-6 flex flex-wrap gap-3">
                <button className="rounded-full bg-slate-900 px-5 py-2 text-sm font-medium text-white shadow-sm hover:bg-slate-800">
                  Get started
                </button>
                <button className="rounded-full border border-slate-300 px-5 py-2 text-sm font-medium text-slate-700 hover:border-slate-400 hover:bg-slate-50">
                  View docs
                </button>
              </div>
            </motion.div>

            <motion.div
              className="order-first lg:order-last"
              initial={{ opacity: 0, scale: 0.96, y: 16 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              transition={{ duration: 0.7, ease: "easeOut", delay: 0.1 }}
            >
              <div className="overflow-hidden rounded-3xl border border-slate-200/80 bg-white shadow-lg">
                <div className="flex items-center justify-between border-b border-slate-100 px-4 py-3 text-xs text-slate-500">
                  <span className="font-medium text-slate-700">
                    Responsive layout
                  </span>
                  <span>Scroll to see sections</span>
                </div>
                <div className="aspect-[4/3] bg-gradient-to-br from-indigo-500/10 via-sky-500/10 to-emerald-400/10" />
              </div>
            </motion.div>
          </div>
        </section>

        {/* Alternating sections */}
        {features.map((feature, idx) => (
          <FeatureSection
            key={feature.id}
            title={feature.title}
            description={feature.description}
            image={feature.image}
            reverse={idx % 2 === 1}
          />
        ))}

        <footer className="mt-10 border-t border-slate-200/80 bg-white/60">
          <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-3 px-4 py-6 text-xs text-slate-500 sm:flex-row sm:px-6 lg:px-8">
            <span>© {new Date().getFullYear()} MotionLanding. All rights reserved.</span>
            <span className="flex gap-4">
              <a href="#" className="hover:text-slate-700">
                Privacy
              </a>
              <a href="#" className="hover:text-slate-700">
                Terms
              </a>
            </span>
          </div>
        </footer>
      </main>
    </div>
  )
}

export default LandingPage
