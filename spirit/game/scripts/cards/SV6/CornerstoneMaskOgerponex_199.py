from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7f413e8-3320-536d-9e8b-3771a88d36d0",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CornerstoneMaskOgerponex.Name",
    display_name="Cornerstone Mask Ogerpon ex",
    searchable_by=["Cornerstone Mask Ogerpon ex", "Basic", "Tera", "ex", "CornerstoneMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=199,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    abilities=[
        Ability(
            title="Cornerstone Stance",
            game_text="Prevent all damage from attacks done to this Pok\u00e9mon by your opponent's Pok\u00e9mon that have an Ability.",
            effect=unimplemented,
        ),
        Attack(
            title="Demolish",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)