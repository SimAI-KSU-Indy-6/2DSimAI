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
    //    this.camera.setBackgroundColor(0x00ff00);

    //    this.background = this.add.image(512, 384, 'background');
    //    this.background.setAlpha(0.5);

    //    this.gameText = this.add.text(512, 384, 'Make something fun!\nand share it with us:\nsupport@phaser.io', {
    //        fontFamily: 'Arial Black', fontSize: 38, color: '#ffffff',
    //        stroke: '#000000', strokeThickness: 8,
    //        align: 'center'
    //    }).setOrigin(0.5).setDepth(100);

       EventBus.emit('current-scene-ready', this);

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

       const zeke = new Townsperson(this, 100, 200, "Zeke", "zeke");

       this.characters.push(zeke);
    }

    update() {
        // Example: Move a character if a condition is met
        if (Phaser.Input.Keyboard.JustDown(this.input.keyboard!.addKey("SPACE"))) {
            this.characters[0].moveTo(400, 300); // Moves Zeke to (400, 300)
            this.characters[0].playAnimation('walk');
        }
    }

    changeScene ()
    {
        this.scene.start('GameOver');
    }
}
