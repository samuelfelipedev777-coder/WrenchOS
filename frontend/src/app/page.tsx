import ChatBar from "@/components/ChatBar";
import Greeting from "@/components/Greeting";
import SoftAurora from "@/components/SoftAurora";

export default function Home() {
  return (
    <div className="flex min-h-screen bg-black">

      <main className="relative flex-1 min-h-screen overflow-hidden flex flex-col">
        <Greeting />

        <div className="absolute inset-0 z-0">
          <SoftAurora
            speed={0.6}
            scale={1}
            brightness={1}
            color1="#f7f7f7"
            color2="#e100ff"
            noiseFrequency={2}
            noiseAmplitude={1}
            bandHeight={0.5}
            bandSpread={1}
            octaveDecay={0.1}
            layerOffset={0}
            colorSpeed={1}
          />
        </div>

        <div className="relative z-10 flex-1"></div>

        <div className="relative z-10 mt-auto pb-6">
          <ChatBar />
        </div>
      </main>
    </div>
  );
}