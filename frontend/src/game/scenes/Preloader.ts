import { Scene } from 'phaser';
import Phaser from 'phaser';

export class Preloader extends Scene
{
    constructor ()
    {
        super('Preloader');
    }

    init ()
    {
        //  We loaded this image in our Boot Scene, so we can display it here
//        this.add.image(512, 384, 'background');

        //  A simple progress bar. This is the outline of the bar.
//        this.add.rectangle(512, 384, 468, 32).setStrokeStyle(1, 0xffffff);

        //  This is the progress bar itself. It will increase in size from the left based on the % of progress.
//        const bar = this.add.rectangle(512-230, 384, 4, 28, 0xffffff);

        //  Use the 'progress' event emitted by the LoaderPlugin to update the loading bar
//        
// this.load.on('progress', (progress: number) => {
//
//            //  Update the progress bar (our bar is 464px wide, so 100% = 464px)
//            bar.width = 4 + (460 * progress);
//
//        });
    }

    preload ()
    {
        //  Load the assets for the game - Replace with your own assets
        this.load.setPath('assets');

        this.load.image('logo', 'logo.png');
        this.load.image('star', 'star.png');
        
        // Actual Tilemap assets
        this.load.image('ground', 'A2_Ground.png');
        this.load.image('exteriors', 'Modern_Exteriors_Complete_Tileset_32x32.png');
        
        // Load tilemap JSON
        // this.load.tilemapTiledJSON('tilemap', 'map.json');
        this.load.tilemapTiledJSON('tilemap', 'world.json');


        // Load character atlases
        this.load.atlas('zeke', 'zeke.png', 'zeke.json')

    }

    create ()
    {
        //  When all the assets have loaded, it's often worth creating global objects here that the rest of the game can use.
        //  For example, you can define global animations here, so we can use them in other scenes.
        
        // create the Tilemap
        // const map = this.make.tilemap({ key: 'tilemap' })
        
        // // add the tileset image we are using
        // const grass_ts = map.addTilesetImage('Modern_Exteriors_Complete_Tileset_32x32', 'exteriors')
        
        // // create the layers we want in the right order (FIRST PART MUST BE TILED LAYER NAME)
        // if (grass_ts != null) {
        //     map.createLayer('base', grass_ts) 
        //     map.createLayer('road', grass_ts)
        //     map.createLayer('foliage_2', grass_ts) 
        //     map.createLayer('foilage', grass_ts) 
        //     map.createLayer('fence', grass_ts)
        //     map.createLayer('buildings', grass_ts)
        //     map.createLayer('building_front', grass_ts)
        //     map.createLayer('detail', grass_ts)
        // }
        
        //  Move to the MainMenu. You could also swap this for a Scene Transition, such as a camera fade.
        this.scene.start('Game');
    }
}