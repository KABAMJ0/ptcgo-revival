from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="03c8c728-d746-5af6-93b7-9ace963e7375",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensMetang.Name",
    display_name="Steven's Metang",
    searchable_by=["Steven's Metang", "Stage 1", "StevensMetang"],
    subtypes=["Stage 1"],
    collector_number=144,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBeldum.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Metal Slash",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)