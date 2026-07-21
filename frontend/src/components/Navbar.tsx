"use client";

import { useState } from "react";
import {
  LuLayoutDashboard,
  LuFolderKanban,
  LuClock3,
  LuBrainCircuit,
  LuDatabase,
  LuSettings,
  LuPanelLeftClose,
} from "react-icons/lu";
import { navlist } from "../styles/styles";
import Link from "next/link";

export default function Navbar() {
  /* Estados de animação do mouse */
  const [mouse, setMouse] = useState({ x: 0, y: 0 });
  const [hover, setHover] = useState(false);

  /* Estados de animação */
  const [isOpen, setIsOpen] = useState(false);

  // Lista com todos os itens da navegação superior para o .map()
  const menuItems = [
    { title: "WrenchOS", icon: LuLayoutDashboard, path: "/" },
    { title: "Projects", icon: LuFolderKanban, path: "/projects" },
    { title: "Time", icon: LuClock3, path: "/time" },
    { title: "AI Assistant", icon: LuBrainCircuit, path: "/ai" },
    { title: "Database", icon: LuDatabase, path: "/database" },
  ];

  return (
    <nav
      className={`relative transition-all duration-300 ${navlist.navContent} ${
        isOpen ? "w-60" : "w-12"
      }`}
      onMouseMove={(e) => {
        const rect = e.currentTarget.getBoundingClientRect();
        setMouse({
          x: e.clientX - rect.left,
          y: e.clientY - rect.top,
        });
      }}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
    >
      {/* Light Follower do mouse */}
      <div
        className="absolute w-20 h-20 rounded-full blur-2xl pointer-events-none transition-opacity duration-300"
        style={{
          left: mouse.x,
          top: mouse.y,
          transform: "translate(-50%, -50%)",
          opacity: hover ? 1 : 0,
          background:
            "linear-gradient(145deg, /11012B 0%, #3A164F 50%, #C43A8B 100%)",
        }}
      />

      {/* Menu Superior */}
      <div>
        <ul className={navlist.base}>
          {menuItems.map((item, index) => {
            const Icon = item.icon;

            return (
              <li
                key={index}
                className={`${navlist.icon} 
                  flex items-center w-full
                  ${isOpen ? "justify-between" : "justify-center"}
                  `}
              >
                <div className="flex items-center gap-2">
                  {/* Se for o primeiro item, ele também controla o Toggle do Menu, deixando assim, mais dinamico */}
                  {index === 0 ? (
                    <button
                      className="flex items-center gap-2 cursor-pointer"
                      onClick={() => setIsOpen(!isOpen)}
                    >
                      <Icon size={20} />
                      {isOpen && <span>{item.title}</span>}
                    </button>
                  ) : (
                    <Link href={item.path} className="flex items-center gap-2">
                      <Icon size={20} />
                      {isOpen && <span>{item.title}</span>}
                    </Link>
                  )}
                </div>

                {/* Botão de fechar a barra lateral */}
                {index === 0 && isOpen && (
                  <button
                    onClick={(event) => {
                      event.stopPropagation();
                      setIsOpen(false);
                    }}
                    className="cursor-pointer ml-auto pl-4"
                  >
                    <LuPanelLeftClose size={20} />
                  </button>
                )}
              </li>
            );
          })}
        </ul>
      </div>

      {/* Settings */}
      <div
        className={`
    absolute bottom-0 w-full flex
    ${isOpen ? "justify-start" : "justify-center"}
  `}
      >
        <ul className={navlist.base}>
          <li
            className={`
        ${navlist.icon}
        flex items-center
        ${isOpen ? "justify-start" : "justify-center"}
      `}
          >
            <Link href="/settings" className="flex items-center gap-2">
              <LuSettings size={20} />
              {isOpen && <span>Settings</span>}
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}
