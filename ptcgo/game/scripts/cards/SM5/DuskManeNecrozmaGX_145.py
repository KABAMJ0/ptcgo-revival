from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bbc325b2-a9cd-5a4f-828d-3d9bddb34556",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DuskManeNecrozmaGX.Name",
    display_name="Dusk Mane Necrozma-GX",
    searchable_by=["Dusk Mane Necrozma-GX", "Basic", "GX", "Ultra Beast", "DuskManeNecrozmaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=145,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=800,
    abilities=[
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title="Meteor Tempest",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=unimplemented,
        ),
        Attack(
            title="Sun's Eclipse-GX",
            game_text="You can use this attack only if you have more Prize cards remaining than your opponent. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 3},
            damage=250,
            effect=unimplemented,
        ),
    ],
)