export class Townsperson extends Phaser.GameObjects.Sprite {
    name: string;
    characterType: string;
    speed: number;
    facingDirection: string;

    constructor(scene: Phaser.Scene, x: number, y: number, name: string, characterType: string) {
        super(scene, x, y, characterType);
        this.scene = scene;
        scene.add.existing(this);
        this.name = name;
        this.characterType = characterType;
        this.speed = 100;
        this.facingDirection = "down";
    }

    setupAnimations(scene: Phaser.Scene) {
        const actions = ["book", "sit", "pickup", "phone", "walk", "sleep", "stand", "default"];
        const directions = ["up", "down", "left", "right"];
        const frameCount = 5;
    
        actions.forEach(action => {
            if (["walk"].includes(action)) {
                directions.forEach(dir => {
                    const key = `${this.characterType}-${action}_${dir}`;
                    const endFrame = action === "default" ? 3 : frameCount - 1; // Corrected end frame
                    const frameNames = scene.anims.generateFrameNames(this.characterType, {
                        prefix: key + "-",
                        start: 0,
                        end: endFrame,
                        zeroPad: 2
                    });
                    scene.anims.create({
                        key: key,
                        frames: frameNames,
                        frameRate: 10,
                        repeat: action !== "phone" && action !== "default" && action !== "pickup" ? -1 : 0
                    });
                });
            } else if (["default"].includes(action)) {
                const key = `${this.characterType}-${action}`;
                scene.anims.create({
                    key: key,
                    frames: scene.anims.generateFrameNames(this.characterType, {
                        prefix: key + "-",
                        start: 0,
                        end: frameCount - 2,
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
                const directionalActions = ["walk", "stand", "default", "pickup", "sit", "phone"];
            
                if (directionalActions.includes(action)) {
                    animationKey = `${this.characterType}-${action}_${this.facingDirection}`;
                } else {
                    animationKey = `${this.characterType}-${action}`;
                }
            
                // Ensure the animation exists before playing
                if (this.scene.anims.exists(animationKey)) {
                    this.play(animationKey, true);
                } else {
                    console.warn(`Animation '${animationKey}' not found for ${this.name}`);
                }
            }

            moveTo(x: number, y: number) {
                console.log(this.anims)
                if (Math.abs(x - this.x) > Math.abs(y - this.y)) {
                    if (x > this.x) {
                        this.facingDirection = "right";
                    } else {
                        this.facingDirection = "left";
                    }
                } else {
                    if (y > this.y) {
                        this.facingDirection = "down";
                    } else {
                        this.facingDirection = "up";
                    }
                }
        
                this.playAnimation("walk");
        
                this.scene.tweens.add({
                    targets: this,
                    x: x,
                    y: y,
                    duration: 1000,
                    ease: 'Linear',
                    onComplete: () => {
                        this.playAnimation("stand");
                    }
                });
            }
        
}