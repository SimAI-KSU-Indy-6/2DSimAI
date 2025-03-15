export class Townsperson extends Phaser.GameObjects.Sprite {
    name: string;
    characterType: string;
    speed: number;
    facingDirection: string;

    constructor(scene: Phaser.Scene, x: number, y: number, name: string, characterType: string) {
        super(scene, x, y, characterType);
        scene.add.existing(this);
        this.name = name;
        this.characterType = characterType;
        this.speed = 100;
        this.facingDirection = "down";
    }

    setupAnimations(scene: Phaser.Scene) {
        const actions = ["book", "sit", "pickup", "phone", "walk", "sleep", "stand", "default"];
        const directions = ["up", "down", "left", "right"];
        const frameCount = 5; // Assuming all animations have 5 frames (adjust if necessary)
    
        actions.forEach(action => {
            if (["walk", "stand", "default", "pickup", "sit", "phone"].includes(action)) {
                // Create animations for directional actions
                directions.forEach(dir => {
                    const key = `${this.characterType}-${action}_${dir}`;
                    scene.anims.create({
                        key: key,
                        frames: scene.anims.generateFrameNames(this.characterType, {
                            prefix: key + "-",
                            start: 0,
                            end: action === "default" ? 0 : frameCount,
                            zeroPad: 2 // Zero-padded numbers
                        }),
                        frameRate: 10,
                        repeat: action !== "phone" || "default" || "pickup" ? 0 : -1 // Phone, Default, and Pickup should not loop
                    });
                });
            } else {
                // Create animations for non-directional actions
                const key = `${this.characterType}-${action}`;
                scene.anims.create({
                    key: key,
                    frames: scene.anims.generateFrameNames(this.characterType, {
                        prefix: key + "-",
                        start: 0,
                        end: frameCount - 1,
                        zeroPad: 2
                    }),
                    frameRate: 10,
                    repeat: action === "walk" ? -1 : 0
                });
            }
        });
    }

    /*
    Complete guide to all animation:
        Key:
            characterName-movementType_(directionOptions)-(totalNum):
        Animations:
            book-11
            sit_{left, right}-05
            pickup_{left, right}-05
            phone_{out, up}-05
            walk_{up, down, left, right}-05
            sleep-05
            stand_{up, down, left, right}-05
            default_{up, down, left, right}-00
    */
    playAnimation(action: string) {
        let animationKey: string;
        
        // Actions that require a direction
        const directionalActions = ["walk", "stand", "default", "pickup", "sit", "phone"];
    
        if (directionalActions.includes(action)) {
            animationKey = `${this.characterType}-${action}_${this.facingDirection}`;
        } else {
            // Actions without a direction
            animationKey = `${this.characterType}-${action}`;
        }
    
        // Check if the animation exists before playing
        if (this.anims.exists(animationKey)) {
            this.anims.play(animationKey, true);
        } else {
            console.warn(`Animation '${animationKey}' not found for ${this.name}`);
        }
    }

    moveTo(x: number, y: number) {
        this.scene.tweens.add({
            targets: this,
            x: x,
            y: y,
            duration: 1000,
            ease: 'Linear'
        });
        this.playAnimation("walk");
    }
}