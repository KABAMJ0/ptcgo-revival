from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9c273b2-12f4-512d-af34-a86d483a10c0",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2", "Talonflame"],
    subtypes=["Stage 2"],
    collector_number=123,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Aero Chase",
            game_text="If the Retreat Cost of your opponent's Active Pok\u00e9mon is ColorlessColorless or more, this attack does 110 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=110,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)