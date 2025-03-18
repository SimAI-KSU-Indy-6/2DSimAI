import { useRef, useState } from 'react';
import { IRefPhaserGame, PhaserGame } from './game/PhaserGame';
import { MainMenu } from './game/scenes/MainMenu';

import { EventBus } from './game/EventBus';

function App()
{

    // The sprite can only be moved in the MainMenu Scene
    const [canMoveSprite, setCanMoveSprite] = useState(true);

    //  References to the PhaserGame component (game and scene are exposed)
    const phaserRef = useRef<IRefPhaserGame | null>(null);
    const [spritePosition, setSpritePosition] = useState({ x: 0, y: 0 });
    const [isDevSceneActive, setIsDevSceneActive] = useState(false);

    const changeScene = () => {

        if(phaserRef.current)
        {     
            const scene = phaserRef.current.scene as MainMenu;
            
            if (scene)
            {
                scene.changeScene();
            }
        }
    }

    const moveSprite = () => {

        if(phaserRef.current)
        {

            const scene = phaserRef.current.scene as MainMenu;

            if (scene && scene.scene.key === 'MainMenu')
            {
                // Get the update logo position
                scene.moveLogo(({ x, y }) => {

                    setSpritePosition({ x, y });

                });
            }
        }

    }

    const addSprite = () => {

        if (phaserRef.current)
        {
            const scene = phaserRef.current.scene;

            if (scene)
            {
                // Add more stars
                const x = Phaser.Math.Between(64, scene.scale.width - 64);
                const y = Phaser.Math.Between(64, scene.scale.height - 64);
    
                //  `add.sprite` is a Phaser GameObjectFactory method and it returns a Sprite Game Object instance
                const star = scene.add.sprite(x, y, 'star');
    
                //  ... which you can then act upon. Here we create a Phaser Tween to fade the star sprite in and out.
                //  You could, of course, do this from within the Phaser Scene code, but this is just an example
                //  showing that Phaser objects and systems can be acted upon from outside of Phaser itself.
                scene.add.tween({
                    targets: star,
                    duration: 500 + Math.random() * 1000,
                    alpha: 0,
                    yoyo: true,
                    repeat: -1
                });
            }
        }
    }

    // Event emitted from the PhaserGame component
    const currentScene = (scene: Phaser.Scene) => {

        setCanMoveSprite(scene.scene.key !== 'MainMenu');
        
    }

    const goToDevScene = () => {
        if (phaserRef.current?.scene?.scene.manager) {
            if (isDevSceneActive) {
                phaserRef.current.scene.scene.manager.stop('Dev');
                setIsDevSceneActive(false);
            } else {
                phaserRef.current.scene.scene.manager.start('Dev');
                setIsDevSceneActive(true);
            }
        }
    };


    const goToGameScene = () => {
        if (phaserRef.current?.scene?.scene.manager) {
            phaserRef.current.scene.scene.manager.start('Game');
        }
    };

    const handleStepSimulation = () => {
        fetch('http://localhost:8000/step_simulation/', {
            method: 'POST',
        })
            .then((response) => response.json())
            .then((data) => {
                console.log('Simulation Step Response:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
                if (phaserRef.current && phaserRef.current.scene) {
                    phaserRef.current.scene.add.text(100, 100, 'Simulation step failed', {
                        color: '#ffffff',
                    });
                }
            });


        fetch('http://localhost:8000/agents/', {
            method: 'GET',
        })
            .then((response) => response.json())
            .then((character_data) => {
                console.log('Character Data:', character_data);
    
                // Ensure data is an array before iterating
                if (Array.isArray(character_data)) {
                    for (const character of character_data) {
                        if (character && character.location && Array.isArray(character.location) && character.location.length === 2) {
                            const [x, y] = character.location; // Extract x and y
                            
                            // Emit event for character movement
                            EventBus.emit('move-character', { id: character.id, name: character.name, x, y });
                        } else {
                            console.warn("Invalid character data:", character);
                        }
                    }
                } else {
                    console.error("Unexpected response format, expected an array:", character_data);
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                if (phaserRef.current && phaserRef.current.scene) {
                    phaserRef.current.scene.add.text(100, 100, 'Character Data Error', {
                        color: '#ffffff',
                    });
                }
            });
            
    };
    

    return (
        <div id="app">
            <PhaserGame ref={phaserRef} currentActiveScene={currentScene} />
            <div>
                {/* <div>
                    <button className="button" onClick={changeScene}>Change Scene</button>
                </div>
                <div>
                    <button disabled={canMoveSprite} className="button" onClick={moveSprite}>Toggle Movement</button>
                </div>
                <div className="spritePosition">Sprite Position:
                    <pre>{`{\n  x: ${spritePosition.x}\n  y: ${spritePosition.y}\n}`}</pre>
                </div>
                <div>
                    <button className="button" onClick={addSprite}>Add New Sprite</button>
                </div> */}
                <div>
                    <button className="button" onClick={goToDevScene}>
                        {isDevSceneActive ? 'Hide Dev Scene' : 'Show Dev Scene'}
                    </button>
                </div>
                {/* <div>
                    <button disabled={true} className="button" onClick={goToGameScene}>Game Scene</button>
                </div> */}
                <div>
                    <button className="button" onClick={handleStepSimulation}>
                        Step Simulation
                    </button>
                </div>
            </div>
        </div>
    )
}

export default App
