import {Townsperson} from '../classes/Townsperson'
import { EventBus } from '../EventBus';
import { Scene } from 'phaser';

export class Game extends Scene
{
    camera: Phaser.Cameras.Scene2D.Camera;
    background: Phaser.GameObjects.Image;
    gameText: Phaser.GameObjects.Text;
    private characters: Townsperson[] = [];

    constructor ()
    {
        super('Game');
    }

    create ()
    {
        this.camera = this.cameras.main;


        const map = this.make.tilemap({ key: 'tilemap' })

        // add the tileset image we are using
        const grass_ts = map.addTilesetImage('Modern_Exteriors_Complete_Tileset_32x32', 'exteriors')

        // create the layers we want in the right order (FIRST PART MUST BE TILED LAYER NAME)
        if (grass_ts != null) {
            map.createLayer('base', grass_ts) 
            map.createLayer('road', grass_ts)
            map.createLayer('foliage_2', grass_ts) 
            map.createLayer('foilage', grass_ts) 
            map.createLayer('fence', grass_ts)
            map.createLayer('buildings', grass_ts)
            map.createLayer('building_front', grass_ts)
            map.createLayer('detail', grass_ts)
        }

        //initialize joey
        const Joey = new Townsperson(this, 50, 50, "Zeke", "zeke");

        this.characters.push(Joey);
        this.characters[0].setupAnimations(this);

        //initialize amy
        const Amy = new Townsperson(this, 100, 50, "Amy", "amy");

        this.characters.push(Amy);
        this.characters[1].setupAnimations(this);

        // Listen for the move event
        EventBus.on('move-character', (data: { id: number, name: string, x: number, y: number }) => {
            console.log(`Moving ${data.name} (ID: ${data.id}) to (${data.x}, ${data.y})`);
            this.characters[data.id].moveTo((data.x * 32), (data.y * 32));
        });

        EventBus.emit('current-scene-ready', this);
    }

    update() {
        // Example: Move a character if a condition is met
        // if (Phaser.Input.Keyboard.JustDown(this.input.keyboard!.addKey("W"))) {
        //     let frameNames = this.textures.get("zeke").getFrameNames();
        //     console.log(frameNames);
        // }

        // if (Phaser.Input.Keyboard.JustDown(this.input.keyboard!.addKey("SPACE"))) {
        //     this.characters[0].moveTo(400, 300); // Moves Zeke to (400, 300)
        //     //this.characters[0].playAnimation('walk');
        // }

    }

    changeScene ()
    {
        this.scene.start('GameOver');
    }
}
