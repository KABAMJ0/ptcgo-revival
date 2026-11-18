from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="84e9c8ba-ed45-5b99-becc-a08f23525930",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    display_name="Tinkatuff",
    searchable_by=["Tinkatuff", "Stage 1", "Tinkatuff"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    family_id=957,
    abilities=[
        Attack(
            title="Light Punch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)