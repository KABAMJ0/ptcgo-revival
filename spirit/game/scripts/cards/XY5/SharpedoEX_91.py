from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa90bff5-12e8-5921-a857-7f7c94f8e479",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SharpedoEX.Name",
    display_name="Sharpedo-EX",
    searchable_by=["Sharpedo-EX", "Basic", "EX", "SharpedoEX"],
    subtypes=["Basic", "EX"],
    collector_number=91,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=319,
    abilities=[
        Attack(
            title="Hunt",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon. This attack does 30 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Jagged Fang",
            game_text="Discard an Energy attached to this Pok\u00e9mon. Then, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)