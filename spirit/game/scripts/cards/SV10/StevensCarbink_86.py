from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d8cd3e6-4f56-5aac-af55-7d2f2cc989b7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensCarbink.Name",
    display_name="Steven's Carbink",
    searchable_by=["Steven's Carbink", "Basic", "StevensCarbink"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=703,
    abilities=[
        Ability(
            title="Stone Palace",
            game_text="As long as this Pok\u00e9mon is on your Bench, all of your Steven's Pok\u00e9mon take 30 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance). The effect of Stone Palace doesn't stack.",
            effect=unimplemented,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)