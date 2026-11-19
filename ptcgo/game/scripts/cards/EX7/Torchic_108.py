from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3edc8003-f6b8-52e2-91f2-2f918bbbf578",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    display_name="Torchic ★",
    searchable_by=["Torchic \u2605", "Basic", "Star", "Torchic"],
    subtypes=["Basic", "Star"],
    collector_number=108,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=255,
    abilities=[
        Attack(
            title="Fireworks",
            game_text="Flip a coin. If tails, discard a Fire Energy card attached to Torchic Star.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Spring Back",
            game_text="If your opponent has only 1 Prize card left, this attack does 20 damage plus 50 more damage and the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)