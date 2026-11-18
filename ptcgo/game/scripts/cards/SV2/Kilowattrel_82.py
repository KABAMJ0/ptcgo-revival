from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ded332bf-4f2a-50e7-aaf0-e404394f020c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrel.Name",
    display_name="Kilowattrel",
    searchable_by=["Kilowattrel", "Stage 1", "Kilowattrel"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    family_id=940,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Jet Wing",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=unimplemented,
        ),
    ],
)