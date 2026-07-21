import { chatBar } from "@/styles/styles";
import { BiSend } from "react-icons/bi";
import { FiPaperclip, FiMic } from "react-icons/fi";

export default function ChatBar() {
  return (
    <div className={chatBar.wrapper}>
      <div className={chatBar.container}>

        <button className={chatBar.iconButton}>
          <FiPaperclip />
        </button>

        <input
          className={chatBar.input}
          placeholder="Digite uma mensagem..."
        />

        <button className={chatBar.iconButton}>
          <FiMic />
        </button>

        <button className={chatBar.iconButton}>
          <BiSend />
        </button>

      </div>
    </div>
  )
}