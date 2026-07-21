import { greeting } from "@/styles/styles"

export default function Greeting() {
  return (
    <div className={greeting.container}>
      <h1 className={greeting.title}>
        Olá Samuel, o que você tem em mente hoje?
      </h1>
    </div>
  )
}